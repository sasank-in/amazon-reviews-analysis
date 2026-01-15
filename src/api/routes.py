"""
API Routes for the sentiment analysis application.
Follows Single Responsibility Principle - handles only HTTP routing.
"""

from flask import Blueprint, render_template, request, jsonify
import logging

from ..services.sentiment_service import SentimentService, ServiceError
from ..database.repository import FeedbackRepository


logger = logging.getLogger(__name__)

# Create blueprint
api = Blueprint('api', __name__)

# Service instance
sentiment_service = SentimentService()


@api.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@api.route('/admin')
def admin():
    """Render the admin dashboard."""
    return render_template('admin.html')


@api.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint for sentiment analysis.
    
    Request Body:
        {
            "text": "Review text to analyze"
        }
    
    Response:
        {
            "sentiment": "Positive" | "Negative",
            "confidence": 95.5,
            "scores": {
                "positive": 95.5,
                "negative": 4.5
            }
        }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        text = data.get('text', '')
        
        result = sentiment_service.analyze(text)
        return jsonify(result)
        
    except ServiceError as e:
        logger.warning(f"Service error: {e}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@api.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Submit feedback on a prediction.
    
    Request Body:
        {
            "text": "Review text",
            "predicted_sentiment": "Positive",
            "predicted_confidence": 95.5,
            "is_correct": true,
            "correct_label": "Negative" (optional),
            "user_comment": "Comment" (optional)
        }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Validate required fields
        required_fields = ['text', 'predicted_sentiment', 'predicted_confidence', 'is_correct']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create feedback
        feedback = FeedbackRepository.create_feedback(
            text=data['text'],
            predicted_sentiment=data['predicted_sentiment'],
            predicted_confidence=data['predicted_confidence'],
            is_correct=data['is_correct'],
            correct_label=data.get('correct_label'),
            user_comment=data.get('user_comment')
        )
        
        return jsonify({
            "message": "Feedback submitted successfully",
            "feedback_id": feedback.id
        }), 201
        
    except Exception as e:
        logger.error(f"Failed to submit feedback: {e}")
        return jsonify({"error": "Failed to submit feedback"}), 500


@api.route('/feedback/stats', methods=['GET'])
def get_feedback_stats():
    """Get feedback statistics."""
    try:
        stats = FeedbackRepository.get_feedback_stats()
        return jsonify(stats)
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        return jsonify({"error": "Failed to get statistics"}), 500


@api.route('/feedback', methods=['GET'])
def get_all_feedback():
    """Get all feedback entries."""
    try:
        limit = request.args.get('limit', 100, type=int)
        feedback_list = FeedbackRepository.get_all_feedback(limit=limit)
        return jsonify({
            "feedback": [f.to_dict() for f in feedback_list]
        })
    except Exception as e:
        logger.error(f"Failed to get feedback: {e}")
        return jsonify({"error": "Failed to get feedback"}), 500


@api.route('/health')
def health():
    """Health check endpoint."""
    status = sentiment_service.get_status()
    
    if status['ready']:
        return jsonify({"status": "healthy", **status}), 200
    else:
        return jsonify({"status": "unhealthy", **status}), 503


@api.route('/api/v1/analyze', methods=['POST'])
def analyze_v1():
    """Versioned API endpoint for sentiment analysis."""
    return analyze()

