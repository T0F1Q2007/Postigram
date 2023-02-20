import telebot
import requests
from io import BytesIO
import telegram
from telegram import *
from telegram.ext import * 
from requests import *

API_KEY=('6049085515:AAH40g8WsIa9xsrpVnGSeTR1LtbLs-vkic4')
bot = telebot.TeleBot(API_KEY)

#Write HTML

def delete_sentence(filename, sentence):
  with open(filename, 'r') as file:
    lines = file.readlines()
  with open(filename, 'w') as file:
    for line in lines:
      if sentence not in line:
        file.write(line)

must_del1 = "\n</body>\n"
must_del2 = "</html>"

def finduser(file_loc, messaje):
  messaje = str(messaje)
  with open(file_loc,"r") as fayl:
    fayllar = fayl.readlines()
  with open(file_loc, "a") as fayl2:
    for fAyl in fayllar:
      fAyl = fAyl.split()
      if messaje==fAyl[0]:
        online+=1
      else:
        online=0
  if online!=0:
    return True
  else:
    return False

def addUser(id, name, prof_lnk, trust):
  with open('users.txt','a') as all:
    all.write(f"\n{id} {name} {prof_lnk} {trust}")

def add_post(profile,name,photo,message,version):
  mesaj = ""
  for i in message:
    mesaj+=f"{i} "
  if version==0:
    delete_sentence("insta.html",must_del1)
    delete_sentence("insta.html",must_del2)
    with open("insta.html","a") as html:
      html.write(f"""
<section class='feed'>
<p class='start'></p>
<p class='xett'></p>
<div class='feedIN'>
<img src='{profile}' class='mypl1'>
<div class='feed-name'>
<p>{name}</p>
</div>
</div>
<img src='{photo}' class='photo'>
<div class='buttons'>
<span class='like material-icons md-28'>favorite</span>
<span class='chat material-icons md-28'>maps_ugc</span>
<span class='share material-icons md-28'>share</span>
<span class='bookmark material-icons md-28'>bookmark_border</span>
</div>
<p class='my-mes'><font class='my-mes-nm'>{name}</font>{mesaj}</p>
<p class='end'></p>
</section>
""")
      html.write(must_del1)
      html.write(must_del2)
  elif version==1:
    delete_sentence("insta.html",must_del1)
    delete_sentence("insta.html",must_del2)
    with open("insta.html","a") as html:
      html.write(f"""
<section class='feed'>
<p class='start'></p>
<p class='xett'></p>
<div class='feedIN'>
<img src='{profile}' class='mypl1'>
<div class='feed-name'>
<p>{name} <span class="has-insta material-icons-outlined">verified_user</span></p>
</div>
</div>
<img src='{photo}' class='photo'>
<div class='buttons'>
<span class='like material-icons md-28'>favorite</span>
<span class='chat material-icons md-28'>maps_ugc</span>
<span class='share material-icons md-28'>share</span>
<span class='bookmark material-icons md-28'>bookmark_border</span>
</div>
<p class='my-mes'><font class='my-mes-nm'>{name}</font>{mesaj}</p>
<p class='end'></p>
</section>
""")
      html.write(must_del1)
      html.write(must_del2)
  elif version==3:
    delete_sentence("insta.html",must_del1)
    delete_sentence("insta.html",must_del2)
    with open("insta.html","a") as html:
      html.write(f"""
<section class='feed'>
<p class='start'></p>
<p class='xett'></p>
<div class='feedIN'>
<img src='{profile}' class='mypl1'>
<div class='feed-name'>
<p>{name} <span class="trusted material-icons md-12">verified</span></p>
</div>
</div>
<img src='{photo}' class='photo'>
<div class='buttons'>
<span class='like material-icons md-28'>favorite</span>
<span class='chat material-icons md-28'>maps_ugc</span>
<span class='share material-icons md-28'>share</span>
<span class='bookmark material-icons md-28'>bookmark_border</span>
</div>
<p class='my-mes'><font class='my-mes-nm'>{name}</font>{mesaj}</p>
<p class='end'></p>
</section>
""")
      html.write(must_del1)
      html.write(must_del2)

#Commamds
@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id,"""
Hi, this is a post generator for Postigram.
If you has no account type `signup` or /signup
For Sharing a post type `new` or /new
Error button
Notificatin sound
  """)

@bot.message_handler(commands=['signup'])
def signup(message):
  mesaj_text = message.text.replace("/signup","")
  if mesaj_text=="" :
    bot.send_message(message.chat.id,"""
If you have Instagram account type this `/signup insta-your_account_name your_profile_picture's_link`
else type this `/signup your_account_name your_profile_picture's_link`
""")
  else:
    if finduser("users.txt",message.chat.id)==False:
      mesaj_text = mesaj_text.split()
      name = mesaj_text[0]
      if "insta-" in name:
        name = name.replace("insta-","")
        profLi = mesaj_text[1]
        addUser(message.chat.id, name, profLi, 1)
      else:
        name = mesaj_text[0]
        profLi = mesaj_text[1]
        addUser(message.chat.id, name, profLi,0)
      bot.send_message(message.chat.id,"Successfully Registred!")
      print("\n",name,profLi,mesaj_text,finduser("users.txt",message.chat.id),message.chat.id)
    else:
      print(finduser("users.txt",message.chat.id))
      bot.send_message(message.chat.id,"Error! The account has been created.")

@bot.message_handler(commands=['new'])
def new(message):
  mesaj_text = message.text.replace("/new","")
  if mesaj_text=="":
    bot.send_message(message.chat.id,"""
Use of this command:
/new photo's_link your_message
Note: Your message appears bottom of the picture
""")
  else:
    if finduser("users.txt",message.chat.id)==True:
      with open("users.txt",'r') as file:
        users = file.readlines()
      for user in users:
        if message.chat.id in user:
          user = user.split()
      name = user[1]
      profLi = user[2]
      mesaj_text = mesaj_text.split()
      photo = mesaj_text[0]
      del mesaj_text[0]
      messg = mesaj_text
      add_post(profLi,name,photo,messg)
      print(profLi,name,photo,messg)
      for i in users:
        print(i)
      bot.send_message(message.chat.id,"""
Added successfully. It'll share in 24 hours. If you want to share now, use /alert to notify admin.
""")
      print("\n",messg)
    else:
      bot.send_message(message.chat.id,"User not found!")

@bot.message_handler(commands=['fake'])
def fake(message):
  bot.send_message(message.chat.id,"name profile photo about")
  mesaj_text = message.text.replace("/fake","")
  mesaj_text = mesaj_text.split()
  for i in range(3,len(mesaj_text)):
    about+= mesaj_text[i]
  add_post(mesaj_text[1],mesaj_text[0],mesaj_text[2],about,0)

@bot.message_handler(commands=['alert'])
def alert(message):
  bot.send_message(1227843251,f"""
User info: 
{message}
""")

@bot.message_handler(commands=['delme'])
def delme(message):
  if finduser("users.txt",message.chat.id):
    with open(file_loc,"r") as fayl:
      fayllar = fayl.readlines()
    with open(file_loc, "a") as fayl2:
      for fAyl in fayllar:
        fAyl = fAyl.split()
        if messaje==fAyl[0]:
          del fayllar[fAyl]
          break
    bot.send_message(message.chat.id,"User successfully deleted!")
  else:
    bot.send_message(message.chat.id,"User not found!")

@bot.message_handler()
def without(message):
  if message.text=="signup":
    bot.send_message(message.chat.id,"Helo World!")

print("Objection Killed...")
bot.polling()