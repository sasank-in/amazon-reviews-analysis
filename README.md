# Amazon Reviews Sentiment Analyzer 🎯

A professional web application for analyzing sentiment in Amazon customer reviews using a fine-tuned DistilBERT model. Get instant sentiment predictions with confidence scores through an elegant, modern interface.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)
![PyTorch](https://img.shields.io/badge/PyTorch-2.2.2-red)
![Transformers](https://img.shields.io/badge/Transformers-4.38.2-yellow)

## ✨ Features

- 🤖 **AI-Powered Analysis**: Fine-tuned DistilBERT model for accurate sentiment classification
- ⚡ **Real-time Predictions**: Instant sentiment analysis with confidence scores
- 📊 **Visual Feedback**: Animated progress bars showing positive/negative scores
- 👍👎 **User Feedback System**: Mark predictions as correct/wrong with optional corrections
- 📈 **Analytics Dashboard**: Track model accuracy and view feedback statistics
- 🎨 **Modern UI**: Professional dark-themed interface with gradient design
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- 🔥 **Quick Examples**: Pre-loaded sample reviews for instant testing
- ⌨️ **Keyboard Shortcuts**: Press Ctrl+Enter to analyze
- 💾 **SQLite Database**: Persistent storage for user feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Verify model checkpoints** are in the `checkpoints/` folder

### Running the App

```bash
python app.py
```

The application will start and be accessible at:
- **Local**: http://127.0.0.1:5000
- **Network**: http://[your-ip]:5000

## 📖 Usage

1. Open your browser and navigate to **http://127.0.0.1:5000**
2. Enter or paste a customer review in the text area
3. Click **"Analyze Sentiment"** or press **Ctrl+Enter**
4. View the sentiment prediction with detailed confidence scores
5. **Provide Feedback**:
   - Click 👍 **Correct** if the prediction is accurate
   - Click 👎 **Wrong** to mark incorrect predictions and optionally provide the correct label
6. Try the example reviews for quick testing
7. Visit **http://127.0.0.1:5000/admin** to view feedback statistics and analytics

### Example Reviews

```
✅ Positive: "This product exceeded my expectations! Highly recommend."
❌ Negative: "Terrible quality. Broke after one week of use."
✅ Positive: "Fast shipping and great customer service!"
❌ Negative: "Not worth the money. Very disappointed."
```

## 📁 Project Structure

```
reviews-analysis/
├── app.py                          # Application entry point
├── src/
│   ├── __init__.py
│   ├── app.py                      # Flask application factory
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py             # Configuration classes (Dev/Prod/Test)
│   ├── models/
│   │   ├── __init__.py
│   │   └── sentiment_model.py      # ML model wrapper with base class
│   ├── services/
│   │   ├── __init__.py
│   │   └── sentiment_service.py    # Business logic layer (Singleton)
│   ├── database/
│   │   ├── __init__.py
│   │   ├── models.py               # SQLAlchemy database models
│   │   └── repository.py           # Data access layer for feedback
│   └── api/
│       ├── __init__.py
│       └── routes.py               # Flask routes/endpoints
├── templates/
│   ├── index.html                  # Main UI with feedback system
│   └── admin.html                  # Admin dashboard for analytics
├── checkpoints/                    # Fine-tuned DistilBERT model
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   ├── vocab.txt
│   └── training_args.bin
├── feedback.db                     # SQLite database (auto-generated)
├── requirements.txt                # Python dependencies
├── README.md                       # This documentation
├── FEEDBACK_FEATURE.md             # Feedback system documentation
├── .gitignore                      # Git ignore rules
├── test.py                         # Model testing script
└── sentiment-analysis.ipynb        # Training notebook
```

## 🏗️ Architecture

The project follows **clean architecture principles** with clear separation of concerns:

### Layers

1. **Config Layer** (`src/config/`)
   - Application settings and environment configuration
   - Support for multiple environments (Development, Production, Test)
   - Centralized configuration management

2. **Model Layer** (`src/models/`)
   - ML model abstraction with abstract base class pattern
   - DistilBERT implementation for sentiment classification
   - Custom exception hierarchy for error handling

3. **Service Layer** (`src/services/`)
   - Business logic and model orchestration
   - Singleton pattern for service management
   - Input validation and error handling

4. **Database Layer** (`src/database/`)
   - SQLAlchemy ORM models for data persistence
   - Repository pattern for data access
   - Feedback storage and statistics

5. **API Layer** (`src/api/`)
   - RESTful HTTP routes and request handling
   - JSON request/response formatting
   - Error handling and validation

6. **Application Factory** (`src/app.py`)
   - Flask app creation with dependency injection
   - Database initialization
   - Service initialization and lifecycle management

### Design Patterns Used

- **Factory Pattern**: Application creation (`create_app()`)
- **Singleton Pattern**: Service management (`SentimentService`)
- **Repository Pattern**: Data access (`FeedbackRepository`)
- **Abstract Base Class**: Model interface (`BaseModel`)
- **Dependency Injection**: Configuration and services

## 🧠 Model Details

| Property | Value |
|----------|-------|
| **Base Model** | DistilBERT (distilbert-base-uncased) |
| **Task** | Binary Sentiment Classification |
| **Classes** | Negative (0), Positive (1) |
| **Max Length** | 512 tokens |
| **Framework** | PyTorch + Hugging Face Transformers |
| **Parameters** | ~66M |

### Model Architecture

- **6 Transformer layers** (distilled from BERT's 12 layers)
- **768 hidden dimensions**
- **12 attention heads**
- **Sequence classification head** for binary sentiment

## 🛠️ Technology Stack

### Backend
- **Flask 3.1.2**: Lightweight web framework
- **Flask-SQLAlchemy 3.1.1**: ORM for database operations
- **PyTorch 2.2.2**: Deep learning framework
- **Transformers 4.38.2**: Hugging Face library for NLP models
- **SafeTensors 0.6.2**: Secure model serialization

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **Vanilla JavaScript**: No framework dependencies
- **Google Fonts (Inter)**: Professional typography

### Database
- **SQLite**: Lightweight embedded database for feedback storage

### Model
- **DistilBERT**: Distilled version of BERT (66M parameters)
- **Fine-tuned**: Trained on Amazon customer reviews dataset

## 📦 Dependencies

```
flask==3.1.2              # Web framework
flask-sqlalchemy==3.1.1   # Database ORM
torch==2.2.2              # Deep learning framework
transformers==4.38.2      # Hugging Face transformers
safetensors==0.6.2        # Safe model serialization
```

## 🎨 UI Features

### Main Interface
- **Gradient backgrounds** with smooth animations
- **Glass-morphism effects** for modern look
- **Responsive grid layout** for score visualization
- **Smooth transitions** and hover effects
- **Color-coded sentiment badges** (green for positive, red for negative)
- **Real-time loading indicators**

### Feedback System
- **Interactive feedback buttons** (👍 Correct / 👎 Wrong)
- **Correction form** for providing accurate labels
- **Optional comment field** for detailed feedback
- **Success notifications** after submission
- **Disabled state** after feedback to prevent duplicates

### Admin Dashboard
- **Real-time statistics cards** showing model performance
- **Feedback history table** with filtering and sorting
- **Auto-refresh** every 30 seconds
- **Responsive design** for mobile and desktop
- **Color-coded status badges** for quick scanning

## 📊 Feedback System

The application includes a comprehensive feedback system to track model performance and collect user corrections.

### Features

1. **User Feedback Collection**
   - Mark predictions as correct (👍) or wrong (👎)
   - Provide correct label when prediction is wrong
   - Add optional comments explaining the error
   - Feedback stored in SQLite database

2. **Analytics Dashboard** (`/admin`)
   - Total feedback count
   - Correct vs incorrect predictions
   - Real-time accuracy percentage
   - Complete feedback history with timestamps
   - Text preview with full text on hover

3. **API Endpoints**
   - `POST /feedback` - Submit user feedback
   - `GET /feedback/stats` - Get aggregated statistics
   - `GET /feedback` - Retrieve feedback history

### Database Schema

```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL,
    predicted_sentiment VARCHAR(20) NOT NULL,
    predicted_confidence FLOAT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    correct_label VARCHAR(20),
    user_comment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Benefits

- **Continuous Improvement**: Collect real-world data for model retraining
- **Quality Monitoring**: Track accuracy over time
- **Error Analysis**: Identify systematic prediction errors
- **User Engagement**: Users contribute to system improvement
- **Data Collection**: Build labeled dataset from production usage

## ⚙️ Configuration

### Environment Variables

You can customize the app behavior by setting these environment variables:

```bash
# Flask Configuration
FLASK_DEBUG=1                    # Debug mode (default: True)
FLASK_HOST=0.0.0.0              # Server host (default: 0.0.0.0)
FLASK_PORT=5000                 # Server port (default: 5000)

# Database Configuration
DATABASE_URL=sqlite:///feedback.db   # Database URL (default: SQLite)
# For PostgreSQL: postgresql://user:pass@localhost/dbname

# Model Configuration
USE_CUDA=False                  # Use GPU if available (default: False)

# Logging
LOG_LEVEL=INFO                  # Logging level (default: INFO)

# TensorFlow (already set in app.py)
TF_ENABLE_ONEDNN_OPTS=0        # Disable oneDNN optimizations
```

### Model Path

To use a different model checkpoint location, modify `src/config/settings.py`:

```python
MODEL_PATH: Path = BASE_DIR / "checkpoints"  # Change this path
```

## 🚀 Performance

- **CPU Inference**: ~100-300ms per prediction
- **GPU Inference**: ~20-50ms per prediction (with CUDA)
- **Model Size**: ~250MB
- **Memory Usage**: ~500MB RAM

## 🔧 Troubleshooting

### Model not loading?
- Ensure all checkpoint files are in the `checkpoints/` folder
- Verify file permissions

### Port already in use?
- Change the port in `app.py`: `app.run(port=5001)`

### Slow predictions?
- First prediction is slower due to model loading
- Consider using GPU for faster inference

### Import errors?
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## 📝 API Endpoints

### POST /analyze

Analyze sentiment of provided text.

**Request:**
```json
{
  "text": "This product is amazing!"
}
```

**Response:**
```json
{
  "sentiment": "Positive",
  "confidence": 98.45,
  "scores": {
    "negative": 1.55,
    "positive": 98.45
  }
}
```

### POST /feedback

Submit user feedback on a prediction.

**Request:**
```json
{
  "text": "Review text",
  "predicted_sentiment": "Positive",
  "predicted_confidence": 95.5,
  "is_correct": false,
  "correct_label": "Negative",
  "user_comment": "This is clearly negative"
}
```

**Response:**
```json
{
  "message": "Feedback submitted successfully",
  "feedback_id": 1
}
```

### GET /feedback/stats

Get feedback statistics.

**Response:**
```json
{
  "total_feedback": 100,
  "correct_predictions": 85,
  "incorrect_predictions": 15,
  "accuracy": 85.0
}
```

### GET /feedback

Get all feedback entries (with optional limit parameter).

**Response:**
```json
{
  "feedback": [
    {
      "id": 1,
      "text": "Great product!",
      "predicted_sentiment": "Positive",
      "predicted_confidence": 98.5,
      "is_correct": true,
      "correct_label": null,
      "user_comment": null,
      "created_at": "2026-01-15T12:00:00"
    }
  ]
}
```

### GET /health

Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "ready": true,
  "model_loaded": true,
  "device": "cpu"
}
```

### POST /api/v1/analyze

Versioned API endpoint (same as /analyze).

## 🔒 Security Notes

- This is a **development server** - not suitable for production
- For production, use a WSGI server like **Gunicorn** or **uWSGI**
- Add input validation and rate limiting for public deployment
- Consider adding authentication for sensitive use cases

## 📄 License

This project uses the DistilBERT model from Hugging Face, which is licensed under Apache 2.0.

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📧 Support

For issues or questions, please open an issue in the repository.

---

**Built with ❤️ using Flask, PyTorch, and Transformers**
