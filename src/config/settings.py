"""
Application configuration settings.
Follows Single Responsibility Principle - handles only configuration.
"""

import os
from pathlib import Path
from typing import Final


class Config:
    """Base configuration class."""
    
    # Application settings
    APP_NAME: Final[str] = "Amazon Reviews Sentiment Analyzer"
    VERSION: Final[str] = "1.0.0"
    DEBUG: bool = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    
    # Server settings
    HOST: str = os.getenv("FLASK_HOST", "0.0.0.0")
    PORT: int = int(os.getenv("FLASK_PORT", "5000"))
    
    # Model settings
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    MODEL_PATH: Path = BASE_DIR / "checkpoints"
    MAX_SEQUENCE_LENGTH: Final[int] = 512
    
    # Device settings
    DEVICE: str = "cuda" if os.getenv("USE_CUDA", "False").lower() == "true" else "cpu"
    
    # Logging settings
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Database settings
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR / 'feedback.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    
    # Environment settings
    TF_ENABLE_ONEDNN_OPTS: str = "0"
    
    @classmethod
    def init_environment(cls) -> None:
        """Initialize environment variables."""
        os.environ['TF_ENABLE_ONEDNN_OPTS'] = cls.TF_ENABLE_ONEDNN_OPTS


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


class TestConfig(Config):
    """Testing configuration."""
    DEBUG = True
    TESTING = True


# Configuration dictionary
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}


def get_config(config_name: str = 'default') -> Config:
    """
    Get configuration object by name.
    
    Args:
        config_name: Name of the configuration to load
        
    Returns:
        Configuration object
    """
    return config_by_name.get(config_name, DevelopmentConfig)
