from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from database import db
from config import * 



@Client.on_message(filters.group & filters.command("add") & filters.user(ADMIN), group=1)
async def AddUser(client:Client, message:Message):
    
    try:
            user = message.chat.id
            rep = message.reply_to_message.from_user.id
            await db.add_user(user_id = rep, name = message.from_user.first_name)
            print("done !")
            await Client.send_message(client,user,text = "add shod")
    except Exception as e:
        print(e)

        #await db.add_user(user_id = rep, name = message.from_user.first_name)
        #await Client.send_message(client,user,text = "add shod")
    