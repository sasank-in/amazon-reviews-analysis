"""
Sentiment Analysis Service.
Follows Single Responsibility Principle - handles business logic for sentiment analysis.
"""

from typing import Dict, Any, Optional
import logging

from ..models.sentiment_model import (
    SentimentModel,
    ModelNotLoadedError,
    PredictionError
)


logger = logging.getLogger(__name__)


class SentimentService:
    """
    Service layer for sentiment analysis operations.
    Acts as a facade between the API and the model.
    """
    
    _instance: Optional['SentimentService'] = None
    _model: Optional[SentimentModel] = None
    
    def __new__(cls):
        """Singleton pattern to ensure only one instance exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the service."""
        if self._model is None:
            self._model = SentimentModel()
    
    def initialize(self) -> None:
        """Initialize and load the model."""
        logger.info("Initializing SentimentService...")
        self._model.load()
        logger.info("SentimentService initialized successfully")
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment of the given text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Analysis result with sentiment, confidence, and scores
            
        Raises:
            ServiceError: If analysis fails
        """
        try:
            # Validate input
            text = self._validate_input(text)
            
            # Get prediction
            result = self._model.predict(text)
            
            logger.debug(f"Analysis complete: {result['sentiment']} ({result['confidence']}%)")
            return result
            
        except ModelNotLoadedError:
            logger.error("Model not loaded")
            raise ServiceError("Service not initialized. Please try again later.")
        except PredictionError as e:
            logger.error(f"Prediction error: {e}")
            raise ServiceError("Failed to analyze text. Please try again.")
        except ValueError as e:
            raise ServiceError(str(e))
    
    def _validate_input(self, text: str) -> str:
        """
        Validate and clean input text.
        
        Args:
            text: Raw input text
            
        Returns:
            Cleaned text
            
        Raises:
            ValueError: If text is invalid
        """
        if text is None:
            raise ValueError("Text cannot be None")
        
        text = text.strip()
        
        if not text:
            raise ValueError("Text cannot be empty")
        
        if len(text) > 10000:
            raise ValueError("Text is too long (max 10000 characters)")
        
        return text
    
    def is_ready(self) -> bool:
        """Check if the service is ready to handle requests."""
        return self._model is not None and self._model.is_loaded()
    
    def get_status(self) -> Dict[str, Any]:
        """Get service status information."""
        return {
            "ready": self.is_ready(),
            "model_loaded": self._model.is_loaded() if self._model else False,
            "device": str(self._model.device) if self._model else None
        }


class ServiceError(Exception):
    """Exception raised for service-level errors."""
    pass
