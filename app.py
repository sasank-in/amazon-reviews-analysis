"""
Amazon Customer Reviews Sentiment Analysis
A professional web application for analyzing sentiment in customer reviews.
"""

from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import torch.nn.functional as F

app = Flask(__name__)

# Global model and tokenizer
model = None
tokenizer = None
device = None

def load_model():
    """Load the fine-tuned DistilBERT model and tokenizer."""
    global model, tokenizer, device
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    model_path = "./checkpoints"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.to(device)
    model.eval()
    print("Model loaded successfully!")

def predict_sentiment(text):
    """
    Predict sentiment for the given text.
    Returns sentiment label and confidence scores.
    """
    if not text or not text.strip():
        return None
    
    # Tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    # Get prediction
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = F.softmax(logits, dim=-1)
    
    # Get predicted class and confidence
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    confidence = probabilities[0][predicted_class].item()
    
    # Map to sentiment labels (assuming binary: 0=Negative, 1=Positive)
    labels = {0: "Negative", 1: "Positive"}
    sentiment = labels.get(predicted_class, "Unknown")
    
    return {
        "sentiment": sentiment,
        "confidence": round(confidence * 100, 2),
        "scores": {
            "negative": round(probabilities[0][0].item() * 100, 2),
            "positive": round(probabilities[0][1].item() * 100, 2)
        }
    }

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """API endpoint for sentiment analysis."""
    data = request.get_json()
    text = data.get("text", "").strip()
    
    if not text:
        return jsonify({"error": "Please provide text to analyze"}), 400
    
    result = predict_sentiment(text)
    if result is None:
        return jsonify({"error": "Failed to analyze text"}), 500
    
    return jsonify(result)

if __name__ == "__main__":
    load_model()
    app.run(debug=True, host="0.0.0.0", port=5000)
