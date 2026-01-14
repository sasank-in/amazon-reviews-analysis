from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1

pipe = pipeline(
    model="./checkpoints/best",
    tokenizer="./checkpoints/best",
    device=device
)

tests = [
    "This product is amazing and works perfectly!",
    "Worst purchase ever. Totally disappointed.",
    "Packaging was okay but delivery was late."
]

for text in tests:
    print(text)
    print(pipe(text))
    print("-" * 80)