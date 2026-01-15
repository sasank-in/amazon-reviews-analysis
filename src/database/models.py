"""Database models for feedback storage."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Feedback(db.Model):
    """Model for storing user feedback on predictions."""
    
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    predicted_sentiment = db.Column(db.String(20), nullable=False)
    predicted_confidence = db.Column(db.Float, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    correct_label = db.Column(db.String(20), nullable=True)
    user_comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'text': self.text,
            'predicted_sentiment': self.predicted_sentiment,
            'predicted_confidence': self.predicted_confidence,
            'is_correct': self.is_correct,
            'correct_label': self.correct_label,
            'user_comment': self.user_comment,
            'created_at': self.created_at.isoformat()
        }
