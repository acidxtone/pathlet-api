import sys
import os
import unittest
from datetime import datetime

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Dependency check
DEPENDENCIES_INSTALLED = True
try:
    import ephem
    import pytz
    import numpy
    import scipy
except ImportError:
    DEPENDENCIES_INSTALLED = False

# Conditional import
if DEPENDENCIES_INSTALLED:
    from backend.services.hugging_face import get_possible_ascendants
    from backend.services.numerology import calculate_numerology
    from backend.services.human_design import calculate_human_design

class ServiceTests(unittest.TestCase):
    @unittest.skipIf(not DEPENDENCIES_INSTALLED, "Required dependencies not installed")
    def test_astrology_calculator(self):
        """Test Astrology Calculations"""
        test_cases = [
            {"birth_date": "1990-05-15", "birth_location": "New York"},
            {"birth_date": "1985-12-22", "birth_location": "Los Angeles"}
        ]
        
        for case in test_cases:
            result = get_possible_ascendants(
                case['birth_date'], 
                case['birth_location']
            )
            
            self.assertIn('possible_ascendants', result)
            self.assertTrue(len(result['possible_ascendants']) > 0)
            self.assertIn('description', result)
    
    @unittest.skipIf(not DEPENDENCIES_INSTALLED, "Required dependencies not installed")
    def test_numerology_calculator(self):
        """Test Numerology Calculations"""
        test_dates = ["1990-05-15", "1985-12-22", "2000-01-01"]
        
        for date in test_dates:
            result = calculate_numerology(date)
            
            self.assertIn('life_path_number', result)
            self.assertIn('description', result)
            self.assertIn('challenges', result)
            self.assertIn('potential_careers', result)
    
    @unittest.skipIf(not DEPENDENCIES_INSTALLED, "Required dependencies not installed")
    def test_human_design_calculator(self):
        """Test Human Design Calculations"""
        test_cases = [
            {"birth_date": "1990-05-15", "birth_time": "10:30 AM", "birth_location": "New York"},
            {"birth_date": "1985-12-22", "birth_time": None, "birth_location": None}
        ]
        
        for case in test_cases:
            result = calculate_human_design(
                case['birth_date'], 
                case['birth_time'], 
                case['birth_location']
            )
            
            self.assertIn('type', result)
            self.assertIn('strategy', result)
            self.assertIn('authority', result)
            self.assertIn('description', result)

def print_dependency_status():
    """Print dependency installation status"""
    print("Dependency Status:")
    dependencies = ['ephem', 'pytz', 'numpy', 'scipy']
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"{dep}: ✅ Installed")
        except ImportError:
            print(f"{dep}: ❌ Not Installed")

if __name__ == '__main__':
    print_dependency_status()
    unittest.main()
