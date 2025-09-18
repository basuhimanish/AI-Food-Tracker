import sys
import os
from logging.config import fileConfig

# ✅ Load environment variables from .env
from dotenv import load_dotenv
load_dotenv()

# ✅ Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Import Base and models
from app.database import Base
from app.models.models import *

from sqlalchemy import engine_from_config  # type: ignore
from sqlalchemy import pool  # type: ignore
from alembic import context  # type: ignore

# this is the Alembic Config object, which provides access to the .ini file
config = context.config

# ✅ Set sqlalchemy.url from environment variable
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)
else:
    raise Exception("DATABASE_URL not found in environment variables")

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set target metadata from SQLAlchemy models
target_metadata = Base.metadata
