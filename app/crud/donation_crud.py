from sqlalchemy.orm import Session
from app.models import models
from datetime import datetime


def donate_items(db: Session, inventory_ids: list, user_id: int):
    """
    Mark selected items as donated by moving them to FoodStatusLog with 'donated' status.
    Also awards 50 points per donated item.
    
    Args:
        db: Database session
        inventory_ids: List of inventory item IDs to donate
        user_id: User ID
        
    Returns:
        dict: Success/failure message with donation details and points earned
    """
    try:
        donated_count = 0
        
        for inventory_id in inventory_ids:
            # Check if the item belongs to the user
            inventory_item = db.query(models.Inventory).filter(
                models.Inventory.id == inventory_id,
                models.Inventory.u_id == user_id
            ).first()
            
            if not inventory_item:
                continue
            
            # Check if this item is already in FoodStatusLog
            existing_log = db.query(models.FoodStatusLog).filter(
                models.FoodStatusLog.inventory_id == inventory_id
            ).first()
            
            if not existing_log:
                # Move to FoodStatusLog with 'donated' status
                food_status_log = models.FoodStatusLog(
                    inventory_id=inventory_id,
                    status="donated",
                    notes="Donated to NGO",
                    timestamp=datetime.now()
                )
                db.add(food_status_log)
                donated_count += 1
        
        if donated_count > 0:
            # Award points to the user (50 points per donated item)
            points_earned = donated_count * 50
            user = db.query(models.Users).filter(models.Users.id == user_id).first()
            if user:
                user.points += points_earned
            
            db.commit()
            return {
                "message": f"Successfully donated {donated_count} items", 
                "donated_count": donated_count, 
                "points_earned": points_earned,
                "total_points": user.points if user else 0,
                "status": True
            }
        else:
            return {"message": "No items were donated", "donated_count": 0, "status": False}
            
    except Exception as e:
        return {"message": "Failed to donate items", "error": str(e), "status": False}
