from transformers import pipeline
from datasets import load_dataset
from sklearn.metrics import accuracy_score, classification_report

# 1. Load Model
MODEL_PATH = "./my_sentiment_model" 
print(f"Loading model...")
try:
    classifier = pipeline("text-classification", model=MODEL_PATH, tokenizer=MODEL_PATH)
except OSError:
    print("Local model not found, using default...")
    classifier = pipeline("sentiment-analysis")

# 2. Load Dataset
print("Loading Financial PhraseBank and removing Neutral items...")

dataset = load_dataset("financial_phrasebank", "sentences_50agree", split="train", trust_remote_code=True)

# Filter: Keep only Negative (0) and Positive (2). Reject Neutral (1).
binary_dataset = dataset.filter(lambda x: x['label'] != 1)

test_data = binary_dataset
# test_data = binary_dataset.select(range(100)) # Uncomment for quick testing

print(f"Testing on {len(test_data)} examples (Positive vs Negative only)...")

y_true = []
y_pred = []

# 3. Run Predictions
for item in test_data:
    text = item["sentence"]
    true_label_id = item["label"]
    
    # Map dataset ID to string: 0 = Negative, 2 = Positive
    correct_answer = "negative" if true_label_id == 0 else "positive"
    
    # Run Model
    try:
        # Truncate text to 512 to prevent model crash
        result = classifier(text[:512])[0]
        label = result['label']
        
        # Map Model Output to "positive" or "negative"
        if label in ['NEGATIVE', 'LABEL_0']:
            prediction = "negative"
        else:
            prediction = "positive"
            
        y_true.append(correct_answer)
        y_pred.append(prediction)
        
    except Exception as e:
        print(f"Error on item: {e}")

# 4. Calculate Score
acc = accuracy_score(y_true, y_pred)
print("\n" + "="*40)
print(f"BINARY ACCURACY: {acc * 100:.2f}%")
print("="*40)

print("\nDetailed Report:")
print(classification_report(y_true, y_pred, target_names=["negative", "positive"]))