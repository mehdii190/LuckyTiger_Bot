import pymongo
from config import *



con = pymongo.MongoClient(DATABASE_URL)
mydb = con["MyTel_forward"]
mycol = mydb["Users"]
#mycol2 = mydb["Admin"]





async def add_user(user_id:int, name:str) -> None:
    user = mycol.find_one(
        {"user_id":user_id}
    )
    if user is None:
        
        my_dict = {"user_id":user_id, "name":name}
        mycol.insert_one(my_dict)
    else:
        return False
    return

async def del_user(user_id:int) -> None:
   
    user = mycol.find_one(
        {"user_id":user_id}
    )
    if user:
        
        mycol.delete_one({"user_id":user_id})
    else:
        return False
    
    return

async def check(user_id:int):
    
    user = mycol.find_one({"user_id":user_id})
    if user:
        return True
    else:
        return False
    return

#ww = []
#for i in mycol.find():
#    dd = i
#    ww.append(i)
    
#print(dd["user_id"])
#print(ww)