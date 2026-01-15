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
- 🎨 **Modern UI**: Professional dark-themed interface with gradient design
- 📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- 🔥 **Quick Examples**: Pre-loaded sample reviews for instant testing
- ⌨️ **Keyboard Shortcuts**: Press Ctrl+Enter to analyze

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
5. Try the example reviews for quick testing

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
│   │   └── settings.py             # Configuration classes
│   ├── models/
│   │   ├── __init__.py
│   │   └── sentiment_model.py      # ML model wrapper
│   ├── services/
│   │   ├── __init__.py
│   │   └── sentiment_service.py    # Business logic layer
│   └── api/
│       ├── __init__.py
│       └── routes.py               # Flask routes/endpoints
├── templates/
│   └── index.html                  # Professional UI
├── checkpoints/                    # Fine-tuned DistilBERT model
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── ...
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── test.py                         # Model testing script
└── sentiment-analysis.ipynb        # Training notebook
```

## 🏗️ Architecture

The project follows clean architecture principles:

- **Config Layer** (`src/config/`): Application settings and environment configuration
- **Model Layer** (`src/models/`): ML model abstraction with base class pattern
- **Service Layer** (`src/services/`): Business logic and model orchestration
- **API Layer** (`src/api/`): HTTP routes and request handling
- **Application Factory** (`src/app.py`): Flask app creation with dependency injection

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

- **Backend**: Flask 3.1.2
- **ML Framework**: PyTorch 2.2.2
- **NLP Library**: Transformers 4.38.2
- **Model Format**: SafeTensors 0.6.2
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

## 📦 Dependencies

```
flask==3.1.2          # Web framework
torch==2.2.2          # Deep learning framework
transformers==4.38.2  # Hugging Face transformers
safetensors==0.6.2    # Safe model serialization
```

## 🎨 UI Features

- **Gradient backgrounds** with smooth animations
- **Glass-morphism effects** for modern look
- **Responsive grid layout** for score visualization
- **Smooth transitions** and hover effects
- **Color-coded sentiment badges** (green for positive, red for negative)
- **Real-time loading indicators**

## ⚙️ Configuration

### Environment Variables

You can customize the app behavior by setting these environment variables:

```bash
# Disable TensorFlow oneDNN optimizations (already set in app.py)
TF_ENABLE_ONEDNN_OPTS=0

# Flask debug mode (default: True in app.py)
FLASK_DEBUG=1

# Server host (default: 0.0.0.0)
FLASK_HOST=0.0.0.0

# Server port (default: 5000)
FLASK_PORT=5000
```

### Model Path

To use a different model checkpoint location, modify `app.py`:

```python
model_path = "./checkpoints"  # Change this path
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
