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

-   **Frontend:** React, Vite, TailwindCSS
-   **Backend:** Flask, Python
-   **AI Model:** Hugging Face Transformers (`DistilBertForSequenceClassification`), PyTorch
-   **Data Source:** `yfinance` for real-time stock news
-   **Preprocessing:** `nltk` and custom tokenization

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AbhinavSatheesh12/Investiment-Archive.git
    cd Investiment-Archive
    ```

2.  **Backend Setup:**
    ```bash
    # Create virtual environment
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

    # Install Python dependencies
    pip install -r requirements.txt
    ```

3.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install
    cd ..
    ```

## 🏃 Usage

You need to run both the backend and frontend servers.

### 1. Start Support Backend
In your main project directory (with venv activated):
```bash
python3 app.py
```
The backend API will run on `http://127.0.0.1:5000`.

### 2. Start Frontend Application
Open a new terminal, navigate to the frontend folder, and start the verified dev server:
```bash
cd frontend
npm run dev
```
Open your browser and navigate to the local URL (usually `http://localhost:5173`) to use the Investiment application.

### 3. Verify Accuracy
To run the accuracy test script on the specialized financial dataset:
```bash
python3 test_binary_accuracy.py
```

## 📂 Project Structure

-   `app.py`: Flask backend API.
-   `frontend/`: React frontend application (Vite + Tailwind).
-   `train_model.py`: Script to fine-tune the DistilBERT model.
-   `test_binary_accuracy.py`: Validation script to verify model performance.
-   `my_sentiment_model/`: Directory containing the saved model artifacts.

---
*Built with ❤️ for better investing.*