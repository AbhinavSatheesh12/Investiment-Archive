from flask import Flask, jsonify, request
from flask_cors import CORS
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
CORS(app)  # Enable CORS for React frontend

# Load Model
try:
    classifier = pipeline("text-classification", model="./my_sentiment_model", tokenizer="./my_sentiment_model")
except OSError:
    classifier = pipeline("sentiment-analysis") # Fallback

def resolve_ticker(query):
    """
    Resolve a company name or ticker symbol to a valid ticker.
    If the input looks like a ticker (all caps, short), use it directly.
    Otherwise, search for it using yfinance.
    """
    query = query.strip()
    
    # If it looks like a ticker already (all uppercase, <= 5 chars), try it directly
    if query.isupper() and len(query) <= 5:
        return query
    
    # Otherwise, try to search for it
    try:
        search_results = yf.Search(query, max_results=1)
        if search_results.quotes and len(search_results.quotes) > 0:
            return search_results.quotes[0].get('symbol', query.upper())
    except Exception as e:
        print(f"Search failed: {e}")
    
    # Fallback: just use the input as-is (uppercased)
    return query.upper()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    query = data.get('ticker', '').strip()
    
    if not query:
        return jsonify({'error': 'No ticker or company name provided'}), 400

    # Resolve the query to a ticker symbol
    ticker = resolve_ticker(query)

    news_results = []
    overall_sentiment = "N/A"
    sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

    try:
        # Fetch News (yfinance returns what's available, we process up to 100)
        stock = yf.Ticker(ticker)
        news = stock.news[:100] if stock.news else []
        
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
                        sentiment_counts['Negative'] += 1
                    else:
                        sentiment = "Positive"
                        pos_count += 1
                        sentiment_counts['Positive'] += 1
            elif label in ['POSITIVE', 'LABEL_2']:
                sentiment = "Positive"
                pos_count += 1
                sentiment_counts['Positive'] += 1
            else:
                 sentiment_counts['Neutral'] += 1
            
            news_results.append({'title': headline, 'link': link, 'sentiment': sentiment})

        if pos_count > neg_count: overall_sentiment = "Bullish"
        elif neg_count > pos_count: overall_sentiment = "Bearish"
        else: overall_sentiment = "Neutral"
        
        return jsonify({
            'ticker': ticker,
            'overall_sentiment': overall_sentiment,
            'news_results': news_results,
            'sentiment_counts': sentiment_counts
        })

    except Exception as e:
        print("An error occurred:")
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)