from sqlalchemy import create_engine # type: ignore
# from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker, Session, declarative_base# type: ignore
from dotenv import load_dotenv  # type: ignore
import os

# Load .env file first
load_dotenv()

# Use AWS RDS as default, only override if .env file has a different value
DATABASE_URL = "postgresql+psycopg2://ghh:5XS9Nx6QWgxdlt2GZ8us@ai-food-app.cpyg4i0yu30w.ap-south-1.rds.amazonaws.com:5432/postgres"

# Check if .env file has a different DATABASE_URL
env_database_url = os.getenv("DATABASE_URL")
if env_database_url and not env_database_url.startswith("postgresql://localhost"):
    DATABASE_URL = env_database_url

# print(DATABASE_URL)

engine = create_engine(DATABASE_URL) # type: ignore
Sessionlocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()