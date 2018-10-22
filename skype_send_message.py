import keyring
import argparse
from skpy import Skype
SKYPE_KEYRING = 'ims_skype_keyring'
global message_text
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--SKYPE_KEYRING', action="store")  # argument that save IM Platfform
parent_parser.add_argument('--to_user', action="store")
parent_parser.add_argument('--message_text', action="store")
def main(username, to_user, message_text):
    print("Welcome to 'Skype send message'. ")
    password = keyring.get_password(SKYPE_KEYRING, username)
    contact = Skype(username, password)
    contact.user  # you
    contact.contacts  # your contacts
    contact.chats  # your conversations
    message = contact.contacts[to_user].chat  # 1-to-1 conversation
    print("Sending: ")
    message.sendMsg(message_text)
    message.getMsgs()
    mess = message.getMsgs()
    rms = mess[0].content
    print(rms)
    return str(rms)

def messages(username, from_username):
    password = keyring.get_password(SKYPE_KEYRING, username)
    contact = Skype(username, password)
    contact.user  # you
    contact.contacts  # your contacts
    contact.chats  # your conversations
    message = contact.contacts[from_username].chat  # 1-to-1 conversation
    message.getMsgs()
    mess = message.getMsgs()
    rms = mess[0].content
    return str(rms)

if __name__ == '__main__':
    main('username', 'to_user', 'message_text')
