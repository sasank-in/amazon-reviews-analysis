"""
API Routes for the sentiment analysis application.
Follows Single Responsibility Principle - handles only HTTP routing.
"""

from flask import Blueprint, render_template, request, jsonify
import logging

from ..services.sentiment_service import SentimentService, ServiceError


logger = logging.getLogger(__name__)

# Create blueprint
api = Blueprint('api', __name__)

# Service instance
sentiment_service = SentimentService()


@api.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


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
