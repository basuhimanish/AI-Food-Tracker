from app.database import engine
from sqlalchemy import inspect

def check_users_table_properties():
    inspector = inspect(engine)
    columns = inspector.get_columns('users')
    
    print("Users Table Properties:")
    print("=" * 50)
    
    for col in columns:
        print(f"\nColumn: {col['name']}")
        print(f"  Type: {col['type']}")
        print(f"  Nullable: {col['nullable']}")
        print(f"  Primary Key: {col.get('primary_key', False)}")
        print(f"  Unique: {col.get('unique', False)}")
        print(f"  Index: {col.get('index', False)}")
        print(f"  Default: {col.get('default', 'None')}")
    
    # Check indexes
    indexes = inspector.get_indexes('users')
    print(f"\nIndexes:")
    for idx in indexes:
        print(f"  - {idx['name']}: {idx['column_names']} (unique: {idx['unique']})")
    
    # Check foreign keys
    foreign_keys = inspector.get_foreign_keys('users')
    print(f"\nForeign Keys:")
    for fk in foreign_keys:
        print(f"  - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")

if __name__ == "__main__":
    check_users_table_properties() 