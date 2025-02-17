from typing import Dict, List, Any
from .human_design import HumanDesignCalculator
from .numerology import NumerologyCalculator

class CompatibilityAnalyzer:
    """
    Advanced compatibility analysis across multiple dimensions.
    """
    
    @staticmethod
    def analyze_human_design_compatibility(type1: str, type2: str) -> Dict[str, Any]:
        """
        Analyze Human Design type compatibility.
        
        Args:
            type1 (str): First person's Human Design type
            type2 (str): Second person's Human Design type
        
        Returns:
            Dict with compatibility insights
        """
        compatibility_matrix = {
            "Manifestor": {
                "Generator": "High potential for dynamic collaboration",
                "Projector": "Balanced energy exchange",
                "Reflector": "Requires careful communication"
            },
            "Generator": {
                "Manifestor": "Complementary energy flow",
                "Projector": "Potential for mutual growth",
                "Reflector": "Needs patient understanding"
            }
        }
        
        return {
            "type1": type1,
            "type2": type2,
            "compatibility_score": compatibility_matrix.get(type1, {}).get(type2, "Neutral"),
            "interaction_advice": "Practice open communication and respect individual strategies."
        }
    
    @staticmethod
    def analyze_numerology_compatibility(life_path1: int, life_path2: int) -> Dict[str, Any]:
        """
        Analyze numerological life path compatibility.
        
        Args:
            life_path1 (int): First person's life path number
            life_path2 (int): Second person's life path number
        
        Returns:
            Dict with numerological compatibility insights
        """
        compatibility_matrix = {
            (1, 3): "Creative and inspiring partnership",
            (2, 6): "Nurturing and supportive relationship",
            (4, 8): "Stable and goal-oriented connection",
            (5, 7): "Adventurous and intellectual bond"
        }
        
        # Check combinations in both directions
        compatibility_key = (life_path1, life_path2)
        reverse_compatibility_key = (life_path2, life_path1)
        
        compatibility_description = (
            compatibility_matrix.get(compatibility_key) or 
            compatibility_matrix.get(reverse_compatibility_key) or 
            "Unique and complex relationship dynamic"
        )
        
        return {
            "life_path1": life_path1,
            "life_path2": life_path2,
            "compatibility_description": compatibility_description,
            "growth_potential": "Opportunities for mutual understanding and personal development"
        }

def calculate_compatibility(
    person1_data: Dict[str, str], 
    person2_data: Dict[str, str]
) -> Dict[str, Any]:
    """
    Comprehensive compatibility calculation.
    
    Args:
        person1_data (Dict): Birth details for first person
        person2_data (Dict): Birth details for second person
    
    Returns:
        Dict with multi-dimensional compatibility insights
    """
    # Calculate Human Design types
    person1_human_design = HumanDesignCalculator.calculate_human_design(
        person1_data['birth_date'], 
        person1_data.get('birth_time'), 
        person1_data.get('birth_location')
    )
    
    person2_human_design = HumanDesignCalculator.calculate_human_design(
        person2_data['birth_date'], 
        person2_data.get('birth_time'), 
        person2_data.get('birth_location')
    )
    
    # Calculate Life Path Numbers
    person1_numerology = NumerologyCalculator.calculate_life_path(person1_data['birth_date'])
    person2_numerology = NumerologyCalculator.calculate_life_path(person2_data['birth_date'])
    
    return {
        "human_design_compatibility": CompatibilityAnalyzer.analyze_human_design_compatibility(
            person1_human_design['type'], 
            person2_human_design['type']
        ),
        "numerology_compatibility": CompatibilityAnalyzer.analyze_numerology_compatibility(
            person1_numerology['life_path_number'], 
            person2_numerology['life_path_number']
        ),
        "insights": {
            "person1": {
                "human_design_type": person1_human_design['type'],
                "life_path_number": person1_numerology['life_path_number']
            },
            "person2": {
                "human_design_type": person2_human_design['type'],
                "life_path_number": person2_numerology['life_path_number']
            }
        }
    }
