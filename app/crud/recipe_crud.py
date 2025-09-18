import requests
from dotenv import load_dotenv
import os

load_dotenv()

SPOONACULAR_API = "https://api.spoonacular.com/recipes/findByIngredients"
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")


def get_recipes(ingredients):
    """
    Get recipe suggestions based on available ingredients using Spoonacular API.
    
    Args:
        ingredients: List of ingredient names
        
    Returns:
        dict: Recipe suggestions with success/error status
    """
    if not ingredients:
        return {"error": "No ingredients provided"}
    
    if not SPOONACULAR_API_KEY:
        return {"error": "Spoonacular API key not configured"}
    
    try:
        joined_ingredients = ",".join(ingredients)

        params = {
            "ingredients": joined_ingredients,
            "number": 10,  # Increased to 10 recipes
            "ranking": 1,
            "ignorePantry": True,
            "apikey": SPOONACULAR_API_KEY
        }
        
        url = f"{SPOONACULAR_API}?ingredients={joined_ingredients}&number={params.get('number')}&apiKey={SPOONACULAR_API_KEY}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "ingredients_used": ingredients,
                "recipes": data,
                "total_recipes": len(data) if isinstance(data, list) else 0
            }
        else:
            return {
                "error": f"API request failed with status {response.status_code}",
                "details": response.text
            }
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
