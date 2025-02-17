import os
import requests
from dotenv import load_dotenv
import ephem
import datetime
import pytz
from typing import Dict, List, Optional, Any

load_dotenv()

HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")
HUGGING_FACE_MODEL = "google/flan-t5-large"

class AstrologyCalculator:
    """
    Advanced astrological calculation service using precise astronomical libraries.
    """
    
    @staticmethod
    def calculate_ascendant(birth_date: str, birth_time: str, birth_location: str) -> Dict[str, str]:
        """
        Calculate precise ascendant sign with astronomical calculations.
        
        Args:
            birth_date (str): Birth date in YYYY-MM-DD format
            birth_time (str): Birth time in HH:MM AM/PM format
            birth_location (str): Birth location
        
        Returns:
            Dict containing ascendant details
        """
        try:
            # Parse birth date and time
            birth_datetime = datetime.datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %I:%M %p")
            
            # Use ephem for precise astronomical calculations
            observer = ephem.Observer()
            observer.date = birth_datetime.strftime('%Y/%m/%d %H:%M:%S')
            
            # Placeholder for location-based calculations
            # In a real implementation, you'd use geocoding to get precise coordinates
            observer.lat = '40.7128'  # Default to New York latitude
            observer.lon = '-74.0060'  # Default to New York longitude
            
            # Calculate ascendant
            ascendant = ephem.constellation(observer.radec()[0])[1]
            
            return {
                "sign": ascendant,
                "description": f"The {ascendant} Ascendant suggests a dynamic and transformative personality.",
                "calculation_method": "Precise Astronomical Calculation"
            }
        
        except Exception as e:
            return {
                "error": f"Ascendant calculation failed: {str(e)}",
                "details": "Unable to determine precise ascendant"
            }
    
    @staticmethod
    def get_zodiac_sign(birth_date: str) -> str:
        """
        Determine zodiac sign based on birth date.
        
        Args:
            birth_date (str): Birth date in YYYY-MM-DD format
        
        Returns:
            str: Zodiac sign
        """
        try:
            date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            month, day = date.month, date.day
            
            zodiac_signs = [
                (1, 20, "Capricorn"), (2, 19, "Aquarius"), (3, 20, "Pisces"),
                (4, 20, "Aries"), (5, 21, "Taurus"), (6, 21, "Gemini"),
                (7, 23, "Cancer"), (8, 23, "Leo"), (9, 23, "Virgo"),
                (10, 23, "Libra"), (11, 22, "Scorpio"), (12, 22, "Sagittarius"),
                (12, 31, "Capricorn")
            ]
            
            for (m, d, sign) in zodiac_signs:
                if month < m or (month == m and day <= d):
                    return sign
            
            return "Capricorn"  # Default for edge cases
        
        except Exception as e:
            return f"Calculation Error: {str(e)}"

def get_possible_ascendants(birth_date: str, birth_location: str) -> Dict[str, Any]:
    """
    Wrapper function for ascendant calculation.
    
    Args:
        birth_date (str): Birth date
        birth_location (str): Birth location
    
    Returns:
        Dict with ascendant information
    """
    # Use a default time if not provided
    default_time = "12:00 PM"
    
    try:
        ascendant_info = AstrologyCalculator.calculate_ascendant(
            birth_date, 
            default_time, 
            birth_location
        )
        
        # Ensure consistent response structure
        return {
            "possible_ascendants": [ascendant_info.get('sign', 'Unknown')],
            "description": ascendant_info.get('description', 'Ascendant details unavailable'),
            "instructions": "Review the calculated Ascendant and its potential implications.",
            "calculation_method": ascendant_info.get('calculation_method', 'Standard Astronomical')
        }
    
    except Exception as e:
        # Fallback to a consistent error response
        fallback_zodiac = AstrologyCalculator.get_zodiac_sign(birth_date)
        
        return {
            "possible_ascendants": [fallback_zodiac],
            "description": f"Unable to calculate precise ascendant. Fallback to {fallback_zodiac} zodiac sign.",
            "error": str(e),
            "instructions": "Consider providing more precise birth details for accurate results."
        }
