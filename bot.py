from pyrogram import Client
from config import *


class Bot(Client):
    
    def __init__(self):
        super().__init__(
            name = "MyLuckyTiger-Bot",
            api_id = API_ID,
            api_hash = API_HASH,
            bot_token = BOT_TOKEN,
            plugins = {"root" : "plugins"}
        )
            
Bot().run()



