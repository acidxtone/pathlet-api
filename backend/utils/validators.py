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
    Validate birth time format.
    
    Args:
        birth_time (str): Time of birth in HH:MM AM/PM format
    
    Returns:
        bool: Whether the birth time is valid
    """
    time_pattern = r'^(0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$'
    return bool(re.match(time_pattern, birth_time))

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
    if not data:
        return False, "No data provided"
    
    birth_date = data.get('birth_date')
    birth_time = data.get('birth_time', '')
    birth_location = data.get('birth_location')
    
    if not birth_date:
        return False, "Birth date is required"
    
    if not validate_birth_date(birth_date):
        return False, "Invalid birth date format. Use YYYY-MM-DD"
    
    if birth_time and not validate_birth_time(birth_time):
        return False, "Invalid birth time format. Use HH:MM AM/PM"
    
    if not birth_location:
        return False, "Birth location is required"
    
    if not validate_birth_location(birth_location):
        return False, "Invalid birth location"
    
    return True, ""
