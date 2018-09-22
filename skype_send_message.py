import keyring
import argparse
from skpy import Skype
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--username', action="store")
parent_parser.add_argument('--password', action="store")
parent_parser.add_argument('--servicename', action="store")
def main(servicename, username):
    print("Welcome to 'Skype send message'. ")
    password = keyring.get_password(servicename, username) or input("Type your password of Skype: ")
    try:
        keyring.set_password(servicename, username,  password)
        print("password stored successfully")
    except keyring.errors.PasswordSetError:
        print("failed to store password")
        print("password", keyring.get_password(servicename, username))
    contact = Skype(username, password)
    contact.user  # you
    contact.contacts  # your contacts
    contact.chats  # your conversations
    message = contact.contacts[input("Type user name of Skype for 1-to-1 conversation: ")].chat  # 1-to-1 conversation
    print("Sending: ")
    message.sendMsg(input("Type your message for user of Skype with you want to 1-to-1 conversation: "))
    message.getMsgs()
    print("Your message is send")
    print(servicename, username, password)
    return str(password)
    pass
if __name__ == '__main__':
    main('servicename', 'username')
