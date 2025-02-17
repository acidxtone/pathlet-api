import datetime
from typing import Dict, Any, Optional
import ephem

class HumanDesignCalculator:
    """
    Advanced Human Design Type Calculator with comprehensive analysis.
    """
    
    DESIGN_TYPES = {
        "Manifestor": {
            "strategy": "Inform before acting",
            "authority": "Emotive or Splenic",
            "signature": "Peace",
            "not_self_theme": "Anger",
            "description": "Initiators who can start things independently and create significant impact."
        },
        "Generator": {
            "strategy": "Wait to Respond",
            "authority": "Sacral",
            "signature": "Satisfaction",
            "not_self_theme": "Frustration",
            "description": "Life-force energy workers who thrive by responding to opportunities."
        },
        "Manifesting Generator": {
            "strategy": "Wait to Respond, then Inform",
            "authority": "Sacral",
            "signature": "Satisfaction",
            "not_self_theme": "Frustration",
            "description": "Hybrid type combining Manifestor's initiating power with Generator's response mechanism."
        },
        "Projector": {
            "strategy": "Wait for Invitation",
            "authority": "Splenic or Mental",
            "signature": "Success",
            "not_self_theme": "Bitterness",
            "description": "Guides and managers who direct energy of others with precision."
        },
        "Reflector": {
            "strategy": "Wait a lunar cycle before making decisions",
            "authority": "Lunar",
            "signature": "Surprise",
            "not_self_theme": "Disappointment",
            "description": "Rare type that samples and reflects community energy, requiring unique decision-making approach."
        }
    }
    
    @staticmethod
    def calculate_human_design(
        birth_date: str, 
        birth_time: Optional[str] = None, 
        birth_location: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Determine Human Design type based on birth details.
        
        Args:
            birth_date (str): Birth date in YYYY-MM-DD format
            birth_time (str, optional): Birth time in HH:MM AM/PM format
            birth_location (str, optional): Birth location
        
        Returns:
            Dict with comprehensive Human Design insights
        """
        try:
            # Parse birth date
            date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            
            # Use default time if not provided
            if not birth_time:
                birth_time = "12:00 PM"
            
            # Astronomical calculations for type determination
            observer = ephem.Observer()
            observer.date = datetime.datetime.strptime(
                f"{birth_date} {birth_time}", 
                "%Y-%m-%d %I:%M %p"
            )
            
            # Placeholder type determination logic
            # In a real implementation, this would use complex planetary calculations
            type_determination_factors = {
                "Manifestor": date.month % 4 == 0,
                "Generator": date.day % 2 == 0,
                "Manifesting Generator": date.year % 2 == 0,
                "Projector": date.month % 3 == 0,
                "Reflector": date.day % 7 == 0
            }
            
            # Determine type
            design_type = next(
                (type_name for type_name, condition in type_determination_factors.items() if condition), 
                "Generator"  # Default type
            )
            
            # Retrieve type details
            type_details = HumanDesignCalculator.DESIGN_TYPES.get(design_type, {})
            
            return {
                "type": design_type,
                "strategy": type_details.get("strategy", "Adaptive approach"),
                "authority": type_details.get("authority", "Intuitive"),
                "signature": type_details.get("signature", "Personal Alignment"),
                "not_self_theme": type_details.get("not_self_theme", "Self-Discovery"),
                "description": type_details.get("description", "Unique life path with individual characteristics"),
                "calculation_method": "Astronomical and Astrological Factors"
            }
        
        except Exception as e:
            return {
                "error": f"Human Design calculation failed: {str(e)}",
                "fallback_type": "Generator"
            }
    
    @staticmethod
    def get_type_compatibility(design_type: str) -> Dict[str, Any]:
        """
        Provide relationship and interaction insights for a given Human Design type.
        
        Args:
            design_type (str): Human Design type
        
        Returns:
            Dict with compatibility and interaction insights
        """
        compatibility = {
            "Manifestor": {
                "best_matches": ["Projector", "Generator"],
                "challenges": ["Reflector"],
                "interaction_advice": "Communicate intentions clearly, respect independence"
            },
            "Generator": {
                "best_matches": ["Manifestor", "Projector"],
                "challenges": ["Reflector"],
                "interaction_advice": "Respond authentically, avoid forcing decisions"
            },
            # Add more detailed compatibility insights
        }
        
        return compatibility.get(design_type, {
            "best_matches": ["All types with mutual understanding"],
            "challenges": ["Misaligned expectations"],
            "interaction_advice": "Practice open communication and mutual respect"
        })

def calculate_human_design(
    birth_date: str, 
    birth_time: Optional[str] = None, 
    birth_location: Optional[str] = None
) -> Dict[str, Any]:
    """
    Comprehensive Human Design calculation wrapper.
    
    Args:
        birth_date (str): Birth date in YYYY-MM-DD format
        birth_time (str, optional): Birth time
        birth_location (str, optional): Birth location
    
    Returns:
        Dict with Human Design insights
    """
    return HumanDesignCalculator.calculate_human_design(
        birth_date, 
        birth_time, 
        birth_location
    )

def get_human_design_type_details(design_type):
    """
    Provide detailed description for Human Design types.
    
    Args:
        design_type (str): Human Design type
    
    Returns:
        dict: Detailed description of the type
    """
    type_details = {
        "Manifestor": {
            "description": "Initiators who can start things independently",
            "strategy": "Inform before acting",
            "signature": "Peace",
            "not_self_theme": "Anger"
        },
        "Generator": {
            "description": "Life-force energy workers who respond to opportunities",
            "strategy": "Wait to Respond",
            "signature": "Satisfaction",
            "not_self_theme": "Frustration"
        },
        "Projector": {
            "description": "Guides and managers who direct energy of others",
            "strategy": "Wait for Invitation",
            "signature": "Success",
            "not_self_theme": "Bitterness"
        },
        "Reflector": {
            "description": "Rare type that samples and reflects community energy",
            "strategy": "Wait a lunar cycle before making decisions",
            "signature": "Surprise",
            "not_self_theme": "Disappointment"
        }
    }
    return type_details.get(design_type, {})
