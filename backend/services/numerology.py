def calculate_numerology(birth_date):
    """
    Calculate various numerological numbers based on birth date.
    
    Args:
        birth_date (str): Date of birth in YYYY-MM-DD format
    
    Returns:
        dict: Numerological calculations
    """
    digits = list(map(int, birth_date.replace('-', '')))
    life_path = sum(digits)
    while life_path > 9:
        life_path = sum(map(int, str(life_path)))
    
    personal_year = (sum(map(int, birth_date.split('-'))) % 9) or 9
    expression_number = (sum(digits) % 9) or 9
    soul_urge_number = (sum(digits[:2]) % 9) or 9
    karmic_debt_number = (sum(digits[-2:]) % 9) or 9
    
    return {
        "life_path": life_path,
        "personal_year": personal_year,
        "expression_number": expression_number,
        "soul_urge_number": soul_urge_number,
        "karmic_debt_number": karmic_debt_number
    }

def get_numerology_description(number):
    """
    Provide a descriptive interpretation of a numerology number.
    
    Args:
        number (int): Numerology number to describe
    
    Returns:
        str: Descriptive interpretation
    """
    descriptions = {
        1: "Leadership, independence, and originality",
        2: "Cooperation, diplomacy, and sensitivity",
        3: "Creativity, communication, and self-expression",
        4: "Stability, discipline, and hard work",
        5: "Freedom, adventure, and versatility",
        6: "Harmony, responsibility, and nurturing",
        7: "Spirituality, analysis, and introspection",
        8: "Personal power, ambition, and material success",
        9: "Compassion, generosity, and global consciousness"
    }
    return descriptions.get(number, "Unique life path with complex characteristics")
