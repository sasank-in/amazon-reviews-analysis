"""
Flask Application Factory.
Follows Factory Pattern for creating Flask app instances.
"""

import logging
from flask import Flask

from .config.settings import Config, get_config
from .api.routes import api, sentiment_service
from .database.models import db


def create_app(config_name: str = 'default') -> Flask:
    """
    Application factory for creating Flask app instances.
    
    Args:
        config_name: Configuration name ('development', 'production', 'test')
        
    Returns:
        Configured Flask application
    """
    # Initialize environment
    Config.init_environment()
    
    # Get configuration
    config = get_config(config_name)
    
    # Setup logging
    setup_logging(config)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Creating app with config: {config_name}")
    
    # Create Flask app
    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )
    
    # Load configuration
    app.config.from_object(config)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(api)
    
    # Initialize services and database
    with app.app_context():
        initialize_database()
        initialize_services()
    
    logger.info(f"{Config.APP_NAME} v{Config.VERSION} initialized")
    
    return app


def setup_logging(config: Config) -> None:
    """Configure application logging."""
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT
    )


def initialize_database() -> None:
    """Initialize database tables."""
    logger = logging.getLogger(__name__)
    logger.info("Initializing database...")
    try:
        db.create_all()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise


def initialize_services() -> None:
    """Initialize application services."""
    logger = logging.getLogger(__name__)
    logger.info("Initializing services...")
    
    try:
        sentiment_service.initialize()
        logger.info("All services initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize services: {e}")
        raise

