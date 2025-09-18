from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        # Check inventory table
        result = connection.execute(text("SELECT * FROM inventory"))
        print("All inventory items:")
        for row in result:
            print("Inventory:", row)
        
        # Check food_items table
        result = connection.execute(text("SELECT * FROM food_items"))
        print("\nAll food items:")
        for row in result:
            print("Food item:", row)
            
        # Check users table
        result = connection.execute(text("SELECT * FROM users"))
        print("\nAll users:")
        for row in result:
            print("User:", row)
            
except Exception as e:
    print("Database connection failed:")
    print(e) 