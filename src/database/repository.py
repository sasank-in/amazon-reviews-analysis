"""Repository for feedback operations."""

from typing import List, Optional, Dict, Any
import logging

from .models import db, Feedback

logger = logging.getLogger(__name__)


class FeedbackRepository:
    """Repository for managing feedback data."""
    
    @staticmethod
    def create_feedback(
        text: str,
        predicted_sentiment: str,
        predicted_confidence: float,
        is_correct: bool,
        correct_label: Optional[str] = None,
        user_comment: Optional[str] = None
    ) -> Feedback:
        """Create a new feedback entry."""
        try:
            feedback = Feedback(
                text=text,
                predicted_sentiment=predicted_sentiment,
                predicted_confidence=predicted_confidence,
                is_correct=is_correct,
                correct_label=correct_label,
                user_comment=user_comment
            )
            db.session.add(feedback)
            db.session.commit()
            logger.info(f"Feedback created: ID={feedback.id}, is_correct={is_correct}")
            return feedback
        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to create feedback: {e}")
            raise
    
    @staticmethod
    def get_all_feedback(limit: int = 100) -> List[Feedback]:
        """Get all feedback entries."""
        return Feedback.query.order_by(Feedback.created_at.desc()).limit(limit).all()
    
    @staticmethod
    def get_feedback_by_id(feedback_id: int) -> Optional[Feedback]:
        """Get feedback by ID."""
        return Feedback.query.get(feedback_id)
    
    @staticmethod
    def get_feedback_stats() -> Dict[str, Any]:
        """Get feedback statistics."""
        total = Feedback.query.count()
        correct = Feedback.query.filter_by(is_correct=True).count()
        incorrect = Feedback.query.filter_by(is_correct=False).count()
        
        accuracy = (correct / total * 100) if total > 0 else 0
        
        return {
            'total_feedback': total,
            'correct_predictions': correct,
            'incorrect_predictions': incorrect,
            'accuracy': round(accuracy, 2)
        }
    
    @staticmethod
    def delete_feedback(feedback_id: int) -> bool:
        """Delete feedback by ID."""
        try:
            feedback = Feedback.query.get(feedback_id)
            if feedback:
                db.session.delete(feedback)
                db.session.commit()
                logger.info(f"Feedback deleted: ID={feedback_id}")
                return True
            return False
        except Exception as e:
            db.session.rollback()
            logger.error(f"Failed to delete feedback: {e}")
            raise
