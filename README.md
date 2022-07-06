# Financial Sentiment Analysis AI

This project leverages advanced Natural Language Processing (NLP) to analyze financial news headlines and predict market sentiment. By utilizing a fine-tuned DistilBERT model, it provides real-time "Bullish" or "Bearish" signals for stock tickers, helping investors make data-driven decisions.

## 🚀 Impact & Benefit to the World

In the fast-paced world of finance, information overload is a significant barrier to entry for individual investors. Institutional players have long had access to sophisticated algorithms that process news in milliseconds. This project **democratizes access to high-end sentiment analysis**, leveling the playing field.

-   **Empowering Investors:** Provides clear, actionable sentiment signals from complex news data.
-   **Reducing Noise:** Filters through the noise of financial media to focus on what matters—market sentiment.
-   **Driving Financial Literacy:** Helps users understand how news correlates with market sentiment.

## 🏆 Performance

Our model has been rigorously tested and achieved remarkable results:

-   **98% Accuracy** on binary sentiment classification (Positive vs. Negative) tasks.
-   Fine-tuned on the **Financial PhraseBank** dataset for domain-specific precision.

## 🛠️ Tech Stack

-   **Backend Model:** Hugging Face Transformers (`DistilBertForSequenceClassification`), PyTorch
-   **Web Framework:** Flask
-   **Data Source:** `yfinance` for real-time stock news
-   **Preprocessing:** `nltk` and custom tokenization

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AbhinavSatheesh12/Investiment-Archive.git
    cd financial-sentiment-analysis
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃 Usage

### 1. Run the Web Application
Start the Flask app to use the web interface:

```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`. Enter a stock ticker (e.g., `AAPL`, `TSLA`, `NVDA`) to see the latest news and overall sentiment analysis.

### 2. Train the Model (Optional)
If you wish to retrain the model from scratch:

```bash
python train_model.py
```
*Note: Ensure you have the training dataset in `data/stock_data.csv`.*

### 3. Verify Accuracy
To run the accuracy test script:

```bash
python test_binary_accuracy.py
```

## 📂 Project Structure

-   `app.py`: Main Flask application for the web interface.
-   `train_model.py`: Script to fine-tune the DistilBERT model.
-   `test_binary_accuracy.py`: Validation script to verify model performance.
-   `my_sentiment_model/`: Directory containing the saved model artifacts.
-   `templates/`: HTML templates for the web app.

---
*Built with ❤️ for better investing.*