import os
import requests
import configparser
import time

# SETUP CONFIG
config = configparser.ConfigParser()
config.read(os.getcwd() + "/spammer.ini")

num = 0
# SET LIMIT
message = config["MESSAGE"]
msg_limit = message["msg_limit"]
_time = config["TIME"]
time_limit = _time["time_limit"]

# GET KEY
_key = config["KEY"]
key = _key["key"]

os.system("clear")
# GET PHONE NUMBER
phonenumber = input("What is the phone number? (e.g. +11111111111): ")
os.system("clear")
# GET MESSAGE
message = input("What do you want to send for a message?: ")

# SPAM
while num != int(msg_limit):
  time.sleep(time_limit)
  num += 1
  response = requests.post('https://textbelt.com/text', {
      'phone': phonenumber,
      'message': message,
      'key': key,
    })
  print(response.json())
  if num == msg_limit:
    os.system("clear")
    break;
