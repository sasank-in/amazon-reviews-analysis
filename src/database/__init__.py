"""Database module for feedback storage."""

from .models import db, Feedback
from .repository import FeedbackRepository

__all__ = ['db', 'Feedback', 'FeedbackRepository']
