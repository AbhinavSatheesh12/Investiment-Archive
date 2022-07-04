import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

def train_model():
    #Load Data
    try:
        # Uses semicolon separator based on file format
        df = pd.read_csv('data/stock_data.csv', sep=';')
    except FileNotFoundError:
        print("Error: 'stock_data.csv' not found.")
        return

    # Clean & Map Data
    df = df.dropna(subset=['sentiment', 'text'])
    label_map = {'negative': 0, 'neutral': 1, 'positive': 2}
    
    # Filter valid rows and map to numbers
    df = df[df['sentiment'].isin(label_map.keys())]
    df['label'] = df['sentiment'].map(label_map)
    
    # Split data
    train_df, val_df = train_test_split(df, test_size=0.2)
    train_dataset = Dataset.from_pandas(train_df)
    val_dataset = Dataset.from_pandas(val_df)

    # Tokenize
    model_name = "distilbert-base-uncased"
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)

    train_tokenized = train_dataset.map(tokenize_function, batched=True)
    val_tokenized = val_dataset.map(tokenize_function, batched=True)

    # Setup Model
    model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=3)

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,              
        per_device_train_batch_size=8,   
        per_device_eval_batch_size=16,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        save_strategy="epoch"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_tokenized,
        eval_dataset=val_tokenized,
    )

    # Train & Save
    print("Starting training...")
    trainer.train()
    
    print("Saving model...")
    model.save_pretrained("./my_sentiment_model")
    tokenizer.save_pretrained("./my_sentiment_model")
    print("Done!")

if __name__ == "__main__":
    train_model()