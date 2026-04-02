def validate_ingredients(ingredients: str) -> str:
    
    valid_keywords = ["fire", "water", "earth", "air"]
    lst_ingredients = ingredients.split()
    for ingredient in lst_ingredients:
        if not ingredient in valid_keywords:
            return f"{ingredients} - INVALID"

    return f"{ingredients} - VALID"
