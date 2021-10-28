from pyrogram import filters , Client
from pymongo import MongoClient
from config import BOT_USERNAME, DATABASE_URL as db_url

users_db = MongoClient(db_url)['users']
col = users_db['USER']
grps = users_db['GROUPS']


@Client.on_message(command(["newstats", f"newstats@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
def stats(_,message):
  users = col.find({})
  mfs = []
  for x in users:
    mfs.append(x['user_id'])
    
  total = len(mfs)
  
  grp = grps.find({})
  grps_ = []
  for x in grp:
    grps_.append(x['chat_id'])
    
  total_ = len(grps_)
  
  bot.send_message(message.chat.id , f"Total Users: {total}\nTotal Groups: {total_}")
