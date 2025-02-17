import re
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ValidationError(ValueError):
    """Custom exception for validation errors."""
    pass

def sanitize_input(input_str):
    """
    Sanitize and clean input strings.
    
    Args:
        input_str (str): Input string to sanitize
    
    Returns:
        str: Cleaned input string
    """
    if not isinstance(input_str, str):
        return ''
    return input_str.strip()

def validate_birth_date(birth_date):
    """
    Advanced birth date validation with comprehensive checks.
    
    Args:
        birth_date (str): Date of birth 
    
    Returns:
        str: Validated and standardized birth date
    
    Raises:
        ValidationError: If date is invalid
    """
    birth_date = sanitize_input(birth_date)
    
    if not birth_date:
        raise ValidationError("Birth date cannot be empty")
    
    try:
        # Try multiple date formats
        date_formats = ['%Y-%m-%d', '%m/%d/%Y', '%d-%m-%Y']
        for date_format in date_formats:
            try:
                parsed_date = datetime.strptime(birth_date, date_format)
                # Validate age range (between 0 and 120 years)
                age = (datetime.now() - parsed_date).days / 365.25
                if 0 <= age <= 120:
                    return parsed_date.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        raise ValidationError(f"Invalid birth date format. Use YYYY-MM-DD. Received: {birth_date}")
    
    except Exception as e:
        logger.error(f"Birth date validation error: {e}")
        raise ValidationError(f"Invalid birth date: {e}")

def validate_birth_time(birth_time):
    """
    Advanced birth time validation with multiple formats and comprehensive checks.
    
    Args:
        birth_time (str): Time of birth
    
    Returns:
        str: Validated and standardized time
    
    Raises:
        ValidationError: If time is invalid
    """
    birth_time = sanitize_input(birth_time)
    
    if not birth_time:
        return ''  # Optional time
    
    # Time format patterns
    time_patterns = [
        ('%I:%M %p', r'^\d{1,2}:\d{2}\s*[APM]{2}$'),  # 12-hour with AM/PM
        ('%H:%M', r'^\d{1,2}:\d{2}$'),               # 24-hour
        ('%H:%M:%S', r'^\d{1,2}:\d{2}:\d{2}$')       # With seconds
    ]
    
    for time_format, pattern in time_patterns:
        if re.match(pattern, birth_time, re.IGNORECASE):
            try:
                # Normalize time
                parsed_time = datetime.strptime(birth_time.upper(), time_format)
                return parsed_time.strftime('%I:%M %p')  # Standardize to 12-hour AM/PM
            except ValueError:
                continue
    
    logger.warning(f"Invalid time format: {birth_time}")
    raise ValidationError(f"Invalid time format. Use HH:MM or HH:MM AM/PM. Received: {birth_time}")

def validate_birth_location(location):
    """
    Advanced location validation with comprehensive checks.
    
    Args:
        location (str): Location of birth
    
    Returns:
        str: Validated location
    
    Raises:
        ValidationError: If location is invalid
    """
    location = sanitize_input(location)
    
    if not location:
        raise ValidationError("Birth location cannot be empty")
    
    # Basic location validation
    if len(location) < 2:
        raise ValidationError(f"Location too short: {location}")
    
    # Optional: Add more sophisticated location validation
    # For example, check against a list of known locations or use geocoding
    
    return location

def validate_request_data(data):
    """
    Comprehensive request data validation.
    
    Args:
        data (dict): Request data containing birth details
    
    Returns:
        dict: Validated and cleaned request data
    
    Raises:
        ValidationError: If any validation fails
    """
    if not isinstance(data, dict):
        raise ValidationError("Invalid request data format. Expected a dictionary.")
    
    # Validate and clean each field
    try:
        validated_data = {
            'birth_date': validate_birth_date(data.get('birth_date', '')),
            'birth_time': validate_birth_time(data.get('birth_time', '')),
            'birth_location': validate_birth_location(data.get('birth_location', ''))
        }
        
        logger.info(f"Request data validated successfully: {validated_data}")
        return validated_data
    
    except ValidationError as ve:
        logger.error(f"Validation Error: {ve}")
        raise
    except Exception as e:
        logger.error(f"Unexpected validation error: {e}")
        raise ValidationError(f"Validation failed: {e}")

# Expose the custom exception for other modules to use
__all__ = ['validate_request_data', 'ValidationError']
