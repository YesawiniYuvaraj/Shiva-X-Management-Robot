import logging
import os
import time
import config as c
from pyrogram import filters
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient



MONGODB_URL = "mongodb+srv://Rss-bro:rss-bro-2008@cluster0.nncixin.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO = MongoClient(MONGODB_URL)
DATABASE = MONGO.SOLO


FORMAT = "[SOLO]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)

StartTime = time.time()

prefix = [".","!","?","*","$","#","/"]

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time



app = Client(
    "demon", 
    api_id=c.api_id, 
    api_hash=c.api_hash,
    bot_token=c.bot_token,
    plugins=dict(root="Plugins")
      )
