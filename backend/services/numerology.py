import datetime
import numpy as np
from typing import Dict, Any, List

class NumerologyCalculator:
    """
    Advanced Numerology Calculator with comprehensive life path analysis.
    """
    
    @staticmethod
    def reduce_number(number: int) -> int:
        """
        Reduce a number to a single digit, with special handling for master numbers.
        
        Args:
            number (int): Number to reduce
        
        Returns:
            int: Reduced number
        """
        while number > 9 and number not in [11, 22, 33]:
            number = sum(int(digit) for digit in str(number))
        return number
    
    @staticmethod
    def calculate_life_path(birth_date: str) -> Dict[str, Any]:
        """
        Calculate comprehensive life path number with advanced insights.
        
        Args:
            birth_date (str): Birth date in YYYY-MM-DD format
        
        Returns:
            Dict with life path details
        """
        try:
            # Parse date and extract components
            date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
            day = date.day
            month = date.month
            year = date.year
            
            # Calculate life path number
            life_path_digits = [int(d) for d in f"{day:02d}{month:02d}{year}"]
            life_path_sum = sum(life_path_digits)
            life_path_number = NumerologyCalculator.reduce_number(life_path_sum)
            
            # Advanced life path analysis
            return {
                "life_path_number": life_path_number,
                "description": NumerologyCalculator.get_life_path_description(life_path_number),
                "challenges": NumerologyCalculator.get_life_challenges(life_path_number),
                "potential_careers": NumerologyCalculator.get_career_suggestions(life_path_number)
            }
        
        except Exception as e:
            return {"error": f"Numerology calculation failed: {str(e)}"}
    
    @staticmethod
    def get_life_path_description(number: int) -> str:
        """
        Provide comprehensive description for life path numbers.
        
        Args:
            number (int): Life path number
        
        Returns:
            str: Detailed life path description
        """
        descriptions = {
            1: "The Leader: Independent, innovative, and pioneering. You're destined to forge your own path and inspire others through your originality and courage.",
            2: "The Mediator: Sensitive, diplomatic, and cooperative. Your strength lies in creating harmony, understanding, and building meaningful relationships.",
            3: "The Communicator: Creative, expressive, and social. Your journey involves self-expression, spreading joy, and inspiring others through art and communication.",
            4: "The Builder: Disciplined, practical, and reliable. Your path is about creating stable foundations, working methodically, and bringing structure to chaos.",
            5: "The Freedom Seeker: Adventurous, versatile, and progressive. Your life is about experiencing change, learning through diverse experiences, and embracing personal freedom.",
            6: "The Nurturer: Compassionate, responsible, and harmonious. Your mission involves creating balance, caring for others, and building loving, supportive environments.",
            7: "The Seeker: Analytical, spiritual, and introspective. Your journey is about deep understanding, spiritual growth, and uncovering life's mysteries.",
            8: "The Powerhouse: Ambitious, confident, and material-focused. Your path involves mastering personal power, achieving material success, and creating abundance.",
            9: "The Humanitarian: Compassionate, global-minded, and transformative. Your mission is to serve humanity, show unconditional love, and bring healing.",
            11: "The Intuitive Master: Spiritually advanced, with heightened intuition and potential for significant societal impact. Balancing spiritual insights with practical implementation.",
            22: "The Master Builder: Extraordinary potential to turn big dreams into reality. Capable of creating large-scale systems that benefit humanity.",
            33: "The Master Teacher: Rare spiritual calling to uplift and transform human consciousness through compassion and wisdom."
        }
        return descriptions.get(number, "A unique life path with complex and evolving characteristics.")
    
    @staticmethod
    def get_life_challenges(number: int) -> Dict[str, str]:
        """
        Identify potential life challenges for each life path number.
        
        Args:
            number (int): Life path number
        
        Returns:
            Dict of challenges and growth opportunities
        """
        challenges = {
            1: {
                "core_challenge": "Overcoming self-doubt and fear of failure",
                "growth_opportunity": "Developing confidence and learning to lead authentically"
            },
            2: {
                "core_challenge": "Balancing personal needs with others' expectations",
                "growth_opportunity": "Developing healthy boundaries and self-worth"
            },
            # Add more detailed challenges for other numbers
        }
        return challenges.get(number, {
            "core_challenge": "Navigating personal growth and self-discovery",
            "growth_opportunity": "Embracing life's lessons with openness and resilience"
        })
    
    @staticmethod
    def get_career_suggestions(number: int) -> List[str]:
        """
        Provide career suggestions based on life path number.
        
        Args:
            number (int): Life path number
        
        Returns:
            List of potential career paths
        """
        career_suggestions = {
            1: ["Entrepreneur", "Executive", "Innovation Consultant"],
            2: ["Counselor", "Diplomat", "HR Professional"],
            3: ["Artist", "Performer", "Marketing Creative"],
            # Add more career suggestions
        }
        return career_suggestions.get(number, ["Diverse career paths with multiple opportunities"])

def calculate_numerology(birth_date: str) -> Dict[str, Any]:
    """
    Comprehensive numerology calculation wrapper.
    
    Args:
        birth_date (str): Birth date in YYYY-MM-DD format
    
    Returns:
        Dict with numerological insights
    """
    return NumerologyCalculator.calculate_life_path(birth_date)
