from app.database import engine
from sqlalchemy import inspect

def check_database_state():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Current Database Schema:")
    print("=" * 50)
    
    for table in tables:
        columns = inspector.get_columns(table)
        print(f"\n{table}:")
        for col in columns:
            print(f"  - {col['name']}: {col['type']}")

if __name__ == "__main__":
    check_database_state() 