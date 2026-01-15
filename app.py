"""
Amazon Customer Reviews Sentiment Analysis
Entry point for the application.
"""

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from src.app import create_app
from src.config.settings import Config


# Create application instance
app = create_app('development')


if __name__ == "__main__":
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )
