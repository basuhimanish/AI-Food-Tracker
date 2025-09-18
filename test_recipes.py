#!/usr/bin/env python3
"""
Test script for recipe functionality without OpenCV dependencies
"""
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_recipe_api():
    """Test the recipe API functionality"""
    
    # Check if API key is set
    api_key = os.getenv("SPOONACULAR_API_KEY")
    if not api_key or api_key == "your_spoonacular_api_key_here":
        print("❌ SPOONACULAR_API_KEY not configured")
        print("Please set your Spoonacular API key in the .env file")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...")
    
    # Test ingredients
    ingredients = ["tomato", "onion", "garlic"]
    
    try:
        # Test the API call directly
        url = "https://api.spoonacular.com/recipes/findByIngredients"
        params = {
            "ingredients": ",".join(ingredients),
            "number": 5,
            "ranking": 1,
            "ignorePantry": True,
            "apiKey": api_key
        }
        
        print(f"🔍 Testing API with ingredients: {ingredients}")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API call successful! Found {len(data)} recipes")
            
            if data:
                print("\n📋 Sample recipe:")
                recipe = data[0]
                print(f"  Title: {recipe.get('title', 'N/A')}")
                print(f"  Used ingredients: {recipe.get('usedIngredientCount', 0)}")
                print(f"  Missing ingredients: {recipe.get('missedIngredientCount', 0)}")
            
            return True
        else:
            print(f"❌ API call failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_backend_endpoint():
    """Test the backend recipe endpoint"""
    try:
        import sys
        sys.path.append('.')
        
        # Import only the recipe function without OpenCV
        from app.crud.crud import get_recipes
        
        print("🔍 Testing backend recipe function...")
        result = get_recipes(["tomato", "onion", "garlic"])
        
        if result.get("success"):
            print("✅ Backend recipe function working!")
            print(f"Found {result.get('total_recipes', 0)} recipes")
            return True
        else:
            print(f"❌ Backend recipe function failed: {result.get('error', 'Unknown error')}")
            return False
            
    except ImportError as e:
        print(f"❌ Import error (likely OpenCV issue): {e}")
        return False
    except Exception as e:
        print(f"❌ Backend test error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Recipe Suggestions Functionality\n")
    
    # Test 1: Direct API call
    print("=" * 50)
    print("TEST 1: Direct Spoonacular API Call")
    print("=" * 50)
    api_success = test_recipe_api()
    
    # Test 2: Backend endpoint
    print("\n" + "=" * 50)
    print("TEST 2: Backend Recipe Function")
    print("=" * 50)
    backend_success = test_backend_endpoint()
    
    # Summary
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    if api_success and backend_success:
        print("✅ All tests passed! Recipe suggestions should work.")
    elif api_success:
        print("⚠️  API works but backend has issues (likely OpenCV dependency)")
    else:
        print("❌ Recipe suggestions not working. Check API key configuration.")
