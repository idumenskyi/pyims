from flask import Flask, url_for
import requests as req
app = Flask(__name__)

@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/IMs')
def IMs(): pass

@app.route('/skype')
def skype(): pass

@app.route('/telegram')
def skype(): pass

@app.route('/facebook')
def skype(): pass

@app.route('/viber')
def skype(): pass

@app.route('/user/')
def profile(username): pass

@app.route('/new/')
def new(new): pass

@app.route('/messages/')
def messages(messages): pass

r = req.post('http://index/login/IMs/skype/user/new')
r = req.get('http://index/login/IMs/skype/user/messages')
r = req.post('http://index/login/IMs/telegram/user/new')
r = req.get('http://index/login/IMs/telegram/user/messages')
r = req.post('http://index/login/IMs/facebook/user/new')
r = req.get('http://index/login/IMs/facebook/user/messages')
r = req.post('http://index/login/IMs/viber/user/new')
r = req.get('http://index/login/IMs/viber/user/messages')

with app.test_request_context():
    print url_for('index')
    print url_for('index', _external=True)
    print url_for('login')
    print url_for('login', next='/')
    print url_for('IMs')
    print url_for('IMs', next='/')
    print url_for('skype')
    print url_for('skype', next='/')    
    print url_for('telegram')
    print url_for('telegram', next='/')    
    print url_for('facebook')
    print url_for('facebook', next='/')  
    print url_for('viber')
    print url_for('viber', next='/')
    print url_for('profile', username='user_IMs')
    print url_for('new')
    print url_for('new', next='/')
    print url_for('messages')
    print url_for('messages', next='/')
