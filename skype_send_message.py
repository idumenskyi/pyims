import keyring
import argparse
from skpy import Skype
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--username', action="store")
parent_parser.add_argument('--password', action="store")
print("Welcome to 'Skype send message'. ")
username = input("Type your username of Skype: ")
password = keyring.get_password("Skype", username)
if (password != keyring.get_password("Skype", username)):
    password = input("Type your password of Skype: ")
    try:
        keyring.set_password("Skype", username,  password)
        print("password stored successfully")
    except keyring.errors.PasswordSetError:
        print("failed to store password")
    print("password", keyring.get_password("Skype", username))
contact = Skype(username, password)
contact.user  # you
contact.contacts  # your contacts
contact.chats  # your conversations
message = contact.contacts[input("Type user name of Skype for 1-to-1 conversation: ")].chat  # 1-to-1 conversation
print("Sending: ")
message.sendMsg(input("Type your message for user of Skype with you want to 1-to-1 conversation: "))
message.getMsgs()  # retrieve recent messages
print("Your message is send")
