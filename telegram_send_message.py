import requests

TOKEN = '692124760:AAFoo5kp0FBdSDuvF2J1T-KXtqRUsAXrwZo'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'

def main(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)
    return text

if '__name__' == '__main__':
    main('chat_id', 'text')
    
