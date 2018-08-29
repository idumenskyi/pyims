import argparse
import bcrypt
from skpy import Skype
import time
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--username', action="store")
ShDo = "" # variable for complete work, ShDo = "shutdown"
outputfile = "contact"
print ("Welcome to 'Skype send message'. ")
username = str(input("Type your username of Skype: "))
password = str(input("Type your password of Skype: "))
contact = Skype(username, password)
hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
with open(outputfile, mode='wb') as f:
    f.write(hashed)
with open(outputfile, mode='rb') as f:
    f.read()
contact.user # you
contact.contacts # your contacts
contact.chats # your conversations
message = contact.contacts[str(input("Type user name of Skype for 1-to-1 conversation: "))].chat # 1-to-1 conversation
while ShDo != 'stop'.upper():
    print("Sending: ")
    message.sendMsg(str(input("Type your message for user of Skype with you want to 1-to-1 conversation: ")))
    message.getMsgs()  # retrieve recent messages
    print("Your message is send")
    time.sleep(5)
    ShDo = str(input("Type the STOP to finish or Press the Enter key to continue: "))
