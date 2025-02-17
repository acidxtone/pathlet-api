import re
from datetime import datetime

def validate_birth_date(birth_date):
    """
    Validate birth date format and ensure it's a valid date.
    
    Args:
        birth_date (str): Date of birth in YYYY-MM-DD format
    
    Returns:
        bool: Whether the birth date is valid
    """
    try:
        datetime.strptime(birth_date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_birth_time(birth_time):
    """
    Validate birth time format with multiple input styles.
    
    Supports formats:
    - HH:MM AM/PM (12-hour)
    - HH:MM (24-hour)
    - HH:MM:SS
    
    Args:
        birth_time (str): Time of birth 
    
    Returns:
        str: Standardized time format or raises ValueError
    """
    if not birth_time:
        return ""  # Allow empty time
    
    # Remove any whitespace
    birth_time = birth_time.strip()
    
    # Patterns to match different time formats
    time_patterns = [
        r'^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$',  # 12-hour with AM/PM
        r'^([01][0-9]|2[0-3]):[0-5][0-9]$',       # 24-hour
        r'^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$'  # With seconds
    ]
    
    for pattern in time_patterns:
        if re.match(pattern, birth_time):
            return birth_time
    
    # If no match, try to parse and standardize
    try:
        # Try parsing with multiple formats
        parsed_time = datetime.strptime(birth_time, '%I:%M %p')
        return parsed_time.strftime('%I:%M %p')
    except ValueError:
        try:
            parsed_time = datetime.strptime(birth_time, '%H:%M')
            return parsed_time.strftime('%H:%M')
        except ValueError:
            raise ValueError("Invalid birth time format. Use HH:MM, HH:MM AM/PM")

def validate_birth_location(location):
    """
    Validate birth location.
    
    Args:
        location (str): Location of birth
    
    Returns:
        bool: Whether the location is valid
    """
    return bool(location and len(location.strip()) > 2)

def validate_request_data(data):
    """
    Validate complete request data for calculations.
    
    Args:
        data (dict): Request data containing birth details
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(data, dict):
        return False, "Invalid request data format"
    
    # Birth date validation
    birth_date = data.get('birth_date', '')
    if not validate_birth_date(birth_date):
        return False, f"Invalid birth date: {birth_date}. Use YYYY-MM-DD format"
    
    # Birth time validation (optional)
    birth_time = data.get('birth_time', '')
    if birth_time:
        try:
            validated_time = validate_birth_time(birth_time)
            data['birth_time'] = validated_time
        except ValueError as e:
            return False, str(e)
    
    # Birth location validation
    birth_location = data.get('birth_location', '')
    if not validate_birth_location(birth_location):
        return False, f"Invalid birth location: {birth_location}"
    
    return True, ""
