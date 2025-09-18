from sqlalchemy.orm import Session
from app.models import models
from datetime import datetime


def add_to_database(db: Session, data, expirydate, user_id):
    """
    Add a food item to the database and user's inventory.
    
    Args:
        db: Database session
        data: Food item data from API
        expirydate: Expiry date for the item
        user_id: User ID
        
    Returns:
        dict: Success/failure message
    """
    try:
        f_id = int(data.get("code"))

        food_item = db.query(models.Food_Items).filter(models.Food_Items.f_id == f_id).first()

        if not food_item:
            food_item = models.Food_Items(
                f_id=f_id,
                f_name=data.get("product_name_en"),
                brands=data.get("brands"),
                quantity=data.get("quantity"),
                energy=data.get("energy_kcal_100g") or 0,
                category=data.get("category"),
                categorystatus=data.get("categorystatus"),
                imageurl=data.get("imageurl")
            )
            db.add(food_item)
            db.commit()
            db.refresh(food_item)

        inventory_item = models.Inventory(
            f_id=food_item.f_id,
            u_id=user_id,
            expiry_date=expirydate
        )
        db.add(inventory_item)
        db.commit()

        return {"message": "success"}

    except Exception as e:
        return {"message": "Failed to add item", "error": str(e)}


def user_inventory(userid: int, db, foodstatus, inventory):
    """
    Get user's inventory items that haven't been logged in FoodStatusLog.
    
    Args:
        userid: User ID
        db: Database session
        foodstatus: FoodStatusLog model
        inventory: Inventory model
        
    Returns:
        list: List of inventory items with food details
    """
    try:
        # First, check and move any expired items for this user
        expired_result = check_and_move_expired_items(db, userid)
        print(f"Expired items check: {expired_result}")
        
        # Subquery to get inventory IDs that are already logged in FoodStatusLog
        subquery = db.query(foodstatus.inventory_id).subquery()

        # Main query to fetch unlogged inventory items with food item details
        results = (
            db.query(inventory, models.Food_Items)
            .join(models.Food_Items, inventory.f_id == models.Food_Items.f_id)
            .filter(
                inventory.u_id == userid,
                ~inventory.id.in_(subquery)
            )
            .all()
        )

        inventory_data = []
        for inventory_item, food_item in results:
            inventory_data.append({
                "inventory_id": inventory_item.id,
                "expiry_date": inventory_item.expiry_date.strftime("%Y-%m-%d"),
                "f_id": inventory_item.f_id,
                "f_name": food_item.f_name,
                "brands": food_item.brands,
                "quantity": food_item.quantity,
                "energy": food_item.energy,
                "category": food_item.category,
                "categorystatus": food_item.categorystatus,
                "imageurl": food_item.imageurl,
            })

        return inventory_data

    except Exception as e:
        return {"message": "Failed to fetch inventory", "error": str(e)}


def delete_inventory_item(db: Session, inventory_id: int, user_id: int):
    """
    Delete an inventory item for a specific user.
    
    Args:
        db: Database session
        inventory_id: Inventory item ID
        user_id: User ID
        
    Returns:
        dict: Success/failure message and status
    """
    try:
        # First check if the item belongs to the user
        inventory_item = db.query(models.Inventory).filter(
            models.Inventory.id == inventory_id,
            models.Inventory.u_id == user_id
        ).first()
        
        if not inventory_item:
            return {"message": "Item not found or not authorized", "status": False}
        
        # Delete the inventory item
        db.delete(inventory_item)
        db.commit()
        
        return {"message": "Item deleted successfully", "status": True}
        
    except Exception as e:
        return {"message": "Failed to delete item", "error": str(e), "status": False}


def check_and_move_expired_items(db: Session, user_id: int = None):
    """
    Check for expired items and automatically move them to FoodStatusLog with 'expired' status.
    Items are considered expired when the current date is greater than the expiry date.
    If user_id is provided, only check that user's items. Otherwise, check all users.
    
    Args:
        db: Database session
        user_id: Optional user ID to check specific user's items
        
    Returns:
        dict: Message about moved items and count
    """
    try:
        today = datetime.now().date()  # Get today's date only (without time)
        
        # Query for expired items - compare dates only
        query = db.query(models.Inventory).filter(
            models.Inventory.expiry_date < datetime.combine(today, datetime.min.time())
        )
        
        if user_id is not None:
            query = query.filter(models.Inventory.u_id == user_id)
        
        expired_items = query.all()
        
        moved_count = 0
        for item in expired_items:
            # Check if this item is already in FoodStatusLog
            existing_log = db.query(models.FoodStatusLog).filter(
                models.FoodStatusLog.inventory_id == item.id
            ).first()
            
            if not existing_log:
                # Move to FoodStatusLog with 'expired' status
                food_status_log = models.FoodStatusLog(
                    inventory_id=item.id,
                    status="expired",
                    notes="Automatically moved due to expiration",
                    timestamp=datetime.now()
                )
                db.add(food_status_log)
                moved_count += 1
        
        if moved_count > 0:
            db.commit()
            return {"message": f"Moved {moved_count} expired items to FoodStatusLog", "moved_count": moved_count}
        else:
            return {"message": "No expired items found", "moved_count": 0}
            
    except Exception as e:
        return {"message": "Failed to check expired items", "error": str(e)}
