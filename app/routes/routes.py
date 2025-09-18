from app.schemas.schemas import *
from app.crud import *
from fastapi import APIRouter, Depends,Query # type: ignore
from datetime import date, datetime
from app.database import get_db
from sqlalchemy.orm import Session # type: ignore

router = APIRouter()

@router.post("/item/scan")
async def scan_item(senddata : UserData, db: Session = Depends(get_db)):
    barcode_data = scan_barcode_live()

    if barcode_data:
        barcode = barcode_data
        item_data = fetch_items_offAPI(barcode)

        try:
            exp_dt = datetime.strptime(senddata.expiry_date, '%Y-%m-%d').date()
            expiry_datetime = datetime.combine(exp_dt, datetime.min.time())
            status = add_to_database(db, item_data, expiry_datetime, int(senddata.userid))
            return status
        
        except Exception as e:
            return {"message" : e}
        
    else:
        return {"message": "No barcode detected."}

# @router.post("/item/scan")
# async def scan_item(senddata : UserData, db: Session = Depends(get_db)):
#     item_data = fetch_items_offAPI(senddata.barcode)
#     status = add_to_database(db, item_data, senddata.expiry_date, int(senddata.userid))
#     return status

@router.post("/user/add")
async def add_new_user(signupinfo : SignupInfo, db : Session = Depends(get_db)):
    name = signupinfo.name
    email = signupinfo.email
    password = signupinfo.password
    
    status = add_user_to_database(db, name, email, password)

    return status


@router.post("/user/verify")
async def verify_user(logininfo : LoginInfo, db : Session = Depends(get_db)):
    email = logininfo.email
    password = logininfo.password

    return verify_user_from_db(email, password, db)

@router.post("/admin/verifyitem")
async def verify_item(barcode:str):
    return fetch_items_offAPI(barcode)

# @router.post("/user/inventory")
# async def show_inventory(userid, db : Session = Depends(get_db)):
#     return user_inventory(userid, db)


@router.post("/user/inventory")
async def show_inventory(request: UserIdRequest, db: Session = Depends(get_db)):
    return user_inventory(request.userid, db,models.FoodStatusLog,models.Inventory)

# @router.get("/user/recipe/input")
# async def recipes(ingredients: list[str] = Query(...)):
#     return get_recipes(ingredients)

@router.post("/user/recipe/suggestions")
async def get_recipe_suggestions(ingredients: Ingredients):
    return get_recipes(ingredients.ingredients)
 

@router.post("/user/expiry_alerts")
async def expiry_alerts(userid: int, db: Session = Depends(get_db)):
    items = get_expiring_items(db, userid)
    if not items:
        return {"message": "No items expiring soon."}
    
    return [
        {
            "name": item.f_name,
            "expiry": item.expiry_date.strftime("%Y-%m-%d"),
            "quantity": item.quantity,
            "brand": item.brands
        } 
        for item in items
    ]

@router.post("/admin/verifyitem")
async def verify_item(barcode:str):
    return fetch_items_offAPI(barcode)

@router.post("/user/foodstatus")
async def food_status(foodstatus:FoodStatus,db:Session = Depends(get_db)):
    return update_food_status(db,foodstatus)

@router.delete("/user/inventory/{inventory_id}")
async def delete_inventory_item_route(inventory_id: int, userid: int, db: Session = Depends(get_db)):
    return delete_inventory_item(db, inventory_id, userid)

@router.post("/user/check-expired")
async def check_expired_items_route(userid: int = None, db: Session = Depends(get_db)):
    return check_and_move_expired_items(db, userid)

@router.post("/user/donate")
async def donate_items_route(request: dict, db: Session = Depends(get_db)):
    inventory_ids = request.get("inventory_ids", [])
    userid = request.get("userid")
    
    if not inventory_ids or not userid:
        return {"message": "Missing inventory_ids or userid", "status": False}
    
    return donate_items(db, inventory_ids, int(userid))

@router.get("/user/points/{user_id}")
async def get_user_points_route(user_id: int, db: Session = Depends(get_db)):
    return get_user_points(db, user_id)

