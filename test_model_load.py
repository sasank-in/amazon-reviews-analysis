from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

print("Loading model...")
try:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    model_path = "./checkpoints"
    print(f"Loading from: {model_path}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    print("Tokenizer loaded!")
    
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    print("Model loaded!")
    
    model.to(device)
    model.eval()
    print("Model ready!")
    
    # Test prediction
    text = "This is a great product!"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
        print(f"Prediction successful! Logits: {outputs.logits}")
    
    print("\nModel test PASSED!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
