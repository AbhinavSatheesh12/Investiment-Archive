from flask import Flask, render_template, request
from transformers import pipeline
import yfinance as yf
import nltk

# Download basics
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')

app = Flask(__name__)

# Load Model
try:
    classifier = pipeline("text-classification", model="./my_sentiment_model", tokenizer="./my_sentiment_model")
except OSError:
    classifier = pipeline("sentiment-analysis") # Fallback

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker = ""
    news_results = []
    overall_sentiment = "N/A"

    if request.method == 'POST':
        ticker = request.form.get('ticker', '').upper()
        if ticker:
            try:
                # Fetch News
                stock = yf.Ticker(ticker)
                news = stock.news
                
                pos_count = 0
                neg_count = 0
                
                for item in news:
                    content = item.get('content', {})
                    
                    # Extract title from inside 'content'
                    headline = content.get('title')
                    
                    # If there's no title, skip it
                    if not headline:
                        continue
                        
                    # Extract link (usually in 'clickThroughUrl' or 'canonicalUrl')
                    # We check multiple places just to be safe
                    link_data = content.get('clickThroughUrl') or content.get('canonicalUrl')
                    
                    # Sometimes the link is a dictionary object itself, sometimes a string
                    if isinstance(link_data, dict):
                        link = link_data.get('url', '#')
                    else:
                        link = link_data or '#'

                    # Run AI
                    result = classifier(headline[:512])[0]
                    label = result['label']
                    
                    # Map labels
                    sentiment = "Neutral"
                    if label in ['NEGATIVE', 'LABEL_0', 'LABEL_1']: 
                         if label == 'NEGATIVE' or label == 'LABEL_0':
                             sentiment = "Negative"
                             neg_count += 1
                         else:
                             sentiment = "Positive"
                             pos_count += 1
                    elif label in ['POSITIVE', 'LABEL_2']:
                        sentiment = "Positive"
                        pos_count += 1
                    
                    news_results.append({'title': headline, 'link': link, 'sentiment': sentiment})

                if pos_count > neg_count: overall_sentiment = "Bullish"
                elif neg_count > pos_count: overall_sentiment = "Bearish"
                else: overall_sentiment = "Neutral"
                
            except Exception as e:
                print("An error occurred:")
                print(e)

    return render_template('index.html', ticker=ticker, news_results=news_results, overall_sentiment=overall_sentiment)

if __name__ == '__main__':
    app.run(port=5000, debug=True)