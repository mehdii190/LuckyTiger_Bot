import pyrogram
from pyrogram.types import Message
from pyrogram import filters, Client
from database import db
from config import *


auth = []
for i in db.mycol.find():
    auth.append(i["user_id"])
    
@Client.on_message(filters.group & filters.text & filters.user(auth) , group=0)
async def forward_to_channel(client:Client, message:Message):
    
    try:
        if message.text == "for":
            print("ok2")
            rep = message.reply_to_message.id
            await Client.forward_messages(client, chat_id = Channel, from_chat_id = message.chat.id, message_ids = rep)
            print("ok")
        else:
            pass
    except Exception as e:
        print(e)
        