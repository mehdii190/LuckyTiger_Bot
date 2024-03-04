

<h1 align="center"> 
    ✨ Lucky Tiger  ✨ 
</h1>

<p align="center">
    <img src="https://wallpapers.com/images/high/dragon-ball-goku-ultra-instinct-1rxiloa6jbwui6v0.webp">
</p>



<p align="center">
    <b>LuckyTiger Bot</b>
</p>


<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
    <a href="https://github.com/mehdii190">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love">
    </a> 
</p>

<p align="center">
    A Support and ready-to-use running instance of this bot can be found on Telegram <br>
    <a href="https://t.me/Forward_CowCusism_Bot"> Forward CowCusism Bot </a> | 
    <a href="https://t.me/mehdi_190_gym"> Founder </a>
</p>



# Project Title

A Telegram Bot  based on [Pyrogram](https://github.com/pyrogram/pyrogram)

A bot telegram forwarder as when you send a message into group and bot will forward your message into channel 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The things you need before installing the software.

* You need this
* And you need this
* Oh, and don't forget this


<h2 align="center"> 
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"> Python-3.12.2 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> | 
    <a href="https://www.mongodb.com/atlas/database"> MongoDB URI </a>
</p>


<h2 align="center"> 
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
LuckyTiger@me:~$ git clone https://github.com/mehdii190/LuckyTiger_Bot
LuckyTiger@me:~$ cd LuckyTiger_Bot
LuckyTiger@me:~$ pip3 install -U -r requirements.txt
LuckyTiger@me:~$ cp config.py new_config.py
```


<h3 align="center"> 
    Edit <b>new_config.py</b> with your own values
</h3>

<h2 align="center"> 
   ⇝ Run Your Host or PC ⇜
</h2>

```console
LuckyTiger@me:~$ python bot.py
```


<h2 align="center"> 
   ⇝ You must edit that <a href="https://github.com/mehdii190/LuckyTiger_Bot/blob/main/config.py">Config</a> ⇜
</h2>

```py
from os import environ
import re


# APIs

API_ID = environ.get("API_ID","")  ## you should go to website Telegram and get your api
API_HASH = environ.get("API_HASH","") ## you should go to website Telegram and get your hash
BOT_TOKEN = environ.get("BOT_TOKEN","") ## you should go to Bot of father 


# AdminS
ADMIN = 339338222 ## you should go to https://t.me/myidbot and send him a message and he will send your id 

# MongoDB information

DATABASE_URL = environ.get('DATABASE_URL', "")


# CHannel

Channel = environ.get("Channel_id","") ## you should go to https://t.me/myidbot and send a message



```

# Thanks to

*  [Dan](https://t.me/haskell) for his [Pyrogram Library](https://github.com/pyrogram/pyrogram)

---
<p align="center">Made with love from the Maldives ❤</p>