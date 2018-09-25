import keyring
import argparse
from skpy import Skype
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--username', action="store")
parent_parser.add_argument('--password', action="store")
parent_parser.add_argument('--servicename', action="store")
parent_parser.add_argument('--user_conversation', action="store")
parent_parser.add_argument('--message_conversation', action="store")
def main(servicename, username,  password, user_conversation, message_conversation):
    print("Welcome to 'Skype send message'. ")
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
    message = contact.contacts[user_conversation].chat  # 1-to-1 conversation
    print("Sending: ")
    message.sendMsg(message_conversation)
    message.getMsgs()
    print("Your message is send")
    print(servicename, username, password)
    return str(message_conversation)
    pass
if __name__ == '__main__':
    main('user_conversation', 'message_conversation')
