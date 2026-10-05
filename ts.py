import os
import requests
import configparser
import time

os.system("clear")
question = input("Do you want to send a payload? (y), or (n): ")

# SETUP CONFIG
config = configparser.ConfigParser()
config.read(os.getcwd() + "/spammer.ini")

num = 0
# SET LIMIT
message = config["MESSAGE"]
msg_limit = message["msg_limit"]
# SET TIME LIMIT PER SMS
_time = config["TIME"]
time_limit = _time["time"]
# SET PAYLOAD
payload = config["PAYLOAD"]
payload_file = payload["payload_file"]

# GET KEY
_key = config["KEY"]
key = _key["key"]

os.system("clear")
# GET PHONE NUMBER
phonenumber = input("What is the phone number? (e.g. +11111111111): ")
os.system("clear")

# SPAM
if question == "y":
  file = open(os.getcwd() + "/" + payload_file, "r")
  content = file.read()
  while num != int(msg_limit):
    time.sleep(int(time_limit))
    num += 1
    response = requests.post('https://textbelt.com/text', {
      'phone': phonenumber,
      'message': content,
      'key': key,
    })
    print(response.json())
    if num == msg_limit:
      os.system("clear")
      break;
elif question == "n":
  # MESSAGE
  message = input("What do you want to send for a message?: ")
  os.system("clear")

  while num != int(msg_limit):
    time.sleep(int(time_limit))
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
else:
  pass