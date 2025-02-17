import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """
    Application configuration settings.
    """
    # Hugging Face Configuration
    HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
    HUGGING_FACE_MODEL = os.getenv('HUGGING_FACE_MODEL', 'google/flan-t5-large')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'development_secret_key')
    DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    # Rate Limiting
    REQUEST_LIMIT_PER_MINUTE = int(os.getenv('REQUEST_LIMIT_PER_MINUTE', 100))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'pathlet.log')

    @classmethod
    def is_production(cls):
        """
        Check if the application is running in production mode.
        
        Returns:
            bool: Whether the app is in production
        """
        return os.getenv('FLASK_ENV', 'development') == 'production'
