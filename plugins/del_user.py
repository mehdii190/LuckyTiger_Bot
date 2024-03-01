from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from database import db
from config import * 


@Client.on_message(filters.group & filters.command("del") & filters.user(ADMIN), group=2)
async def AddUser(client:Client, message:Message):
    
    try:
        user = message.chat.id
        rep = message.reply_to_message.from_user.id
        await db.del_user(user_id=rep)
        print("done !")
        await Client.send_message(client,user,text = "sik shod")
    except Exception as e:
        print(e)