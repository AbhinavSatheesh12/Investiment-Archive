from transformers import pipeline

# Load trained model
try:
    classifier = pipeline("text-classification", model="./my_sentiment_model", tokenizer="./my_sentiment_model")
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    exit()

# Test it with a fake headline
test_text = "Tesla stock is crashing hard today!"
result = classifier(test_text)[0]

# Print result
label = result['label']
score = result['score']

print(f"\nTest Sentence: '{test_text}'")
print(f"Prediction: {label} (Confidence: {round(score*100, 1)}%)")

# Interprets answer
if label == 'LABEL_0': print("Meaning: Negative")
if label == 'LABEL_1': print("Meaning: Neutral")
if label == 'LABEL_2': print("Meaning: Positive")