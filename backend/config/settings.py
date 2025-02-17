import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """
    Application configuration settings.
    """
    # Render-specific environment configuration
    ENVIRONMENT = os.getenv('RENDER_ENVIRONMENT', 'development')
    
    # Hugging Face Configuration
    HUGGING_FACE_API_KEY = os.getenv('HUGGING_FACE_API_KEY')
    HUGGING_FACE_MODEL = os.getenv('HUGGING_FACE_MODEL', 'google/flan-t5-large')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'development_secret_key')
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    
    # Rate Limiting
    REQUEST_LIMIT_PER_MINUTE = int(os.getenv('REQUEST_LIMIT_PER_MINUTE', 100))
    
    # CORS Configuration
    CORS_ORIGINS = [
        'http://localhost:3000',  # Local frontend
        os.getenv('FRONTEND_URL', 'https://pathlet.onrender.com'),  # Render frontend
        'https://pathlet-frontend.onrender.com',
        'https://pathlet-api.vercel.app',  # Vercel production
        'https://pathlet-frontend.vercel.app',  # Potential frontend deployment
        'https://pathlet.vercel.app'  # Additional potential domain
    ]

    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'pathlet.log')

    # Validate critical configurations
    @classmethod
    def validate_config(cls):
        errors = []
        if not cls.SECRET_KEY:
            errors.append("SECRET_KEY is not set")
        if not cls.HUGGING_FACE_API_KEY:
            errors.append("HUGGING_FACE_API_KEY is not set")
        return errors

    @classmethod
    def is_production(cls):
        """
        Check if the application is running in production mode.
        
        Returns:
            bool: Whether the app is in production
        """
        return os.getenv('FLASK_ENV', 'development') == 'production'
