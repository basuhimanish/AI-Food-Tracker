from pydantic import BaseModel # type: ignore
from datetime import date

class UserCreate(BaseModel):
    name : str
    email : str
    password : str

class UserOut(BaseModel):
    id : int
    name : str
    email : str

class FoodItemInput(BaseModel):
    barcode : str

class LoginInfo(BaseModel):
    email : str
    password : str

class SignupInfo(BaseModel):
    name : str
    email : str
    password : str

class UserData(BaseModel):
    # barcode : str
    expiry_date : str
    userid : str

class Ingredients(BaseModel):
    ingredients : list[str]

class UserIdRequest(BaseModel):
    userid: int

class FoodStatus(BaseModel):
    inventory_id : int
    status : str
    notes : str

