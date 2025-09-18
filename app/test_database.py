from sqlalchemy import create_engine, text  # type: ignore
from dotenv import load_dotenv # type: ignore (installed in venv)
import os

# Load .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine
engine = create_engine(DATABASE_URL)  # type: ignore

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users"))
        print("Database connected successfully!")
        for row in result:
            print("Query result:", row)
        print(DATABASE_URL)
except Exception as e:
    print("Database connection failed:")
    print(e)
