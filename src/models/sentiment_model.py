"""Sentiment Analysis Model."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, Optional
import logging

import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from ..config.settings import Config

logger = logging.getLogger(__name__)


class BaseModel(ABC):
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def predict(self, text: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def is_loaded(self) -> bool:
        pass


class SentimentModel(BaseModel):
    LABELS = {0: "Negative", 1: "Positive"}

    def __init__(self, model_path: Optional[Path] = None, device: Optional[str] = None):
        self.model_path = model_path or Config.MODEL_PATH
        self.device = torch.device(device or Config.DEVICE)
        self._model = None
        self._tokenizer = None
        self._is_loaded = False
        logger.info(f"SentimentModel initialized with device: {self.device}")

    def load(self) -> None:
        if self._is_loaded:
            logger.info("Model already loaded")
            return
        try:
            logger.info(f"Loading model from: {self.model_path}")
            self._tokenizer = AutoTokenizer.from_pretrained(str(self.model_path))
            self._model = AutoModelForSequenceClassification.from_pretrained(str(self.model_path))
            self._model.to(self.device)
            self._model.eval()
            self._is_loaded = True
            logger.info("Model loaded successfully!")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise ModelLoadError(f"Failed to load model: {e}") from e


    def predict(self, text: str) -> Dict[str, Any]:
        if not self._is_loaded:
            raise ModelNotLoadedError("Model not loaded")
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")
        try:
            inputs = self._tokenizer(text, return_tensors="pt", truncation=True, max_length=Config.MAX_SEQUENCE_LENGTH, padding=True)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            with torch.no_grad():
                outputs = self._model(**inputs)
                probabilities = F.softmax(outputs.logits, dim=-1)
            predicted_class = torch.argmax(probabilities, dim=-1).item()
            confidence = probabilities[0][predicted_class].item()
            return {
                "sentiment": self.LABELS.get(predicted_class, "Unknown"),
                "confidence": round(confidence * 100, 2),
                "scores": {
                    "negative": round(probabilities[0][0].item() * 100, 2),
                    "positive": round(probabilities[0][1].item() * 100, 2)
                }
            }
        except Exception as e:
            logger.error(f"Prediction failed: {e}")
            raise PredictionError(f"Prediction failed: {e}") from e

    def is_loaded(self) -> bool:
        return self._is_loaded

    @property
    def model(self):
        return self._model

    @property
    def tokenizer(self):
        return self._tokenizer



class ModelError(Exception):
    pass


class ModelLoadError(ModelError):
    pass


class ModelNotLoadedError(ModelError):
    pass


class PredictionError(ModelError):
    pass
