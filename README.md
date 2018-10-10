# Skype Send Message

Python CLI for sending message of Skype. 

### Prerequisites

You need to install the following software 

```
python 3.x+
```
```
SkPy 9.0
```
```
keyring 13.2.1 
```
```
argparse 1.4.0
```

### Installing

For installation python you need to visit the official site of python and move to download page

```
https://www.python.org/downloads/
```

Installation library, start the terminal or cmd as administrator and type next command

```
pip3 install SkPy
```

```
pip3 install argparse
```

```
pip3 install keyring

```

## Running 

double-click on the file skype_send_message.py or use ide.


### API reference for SkPY

API reference - https://skpy.t.allofti.me/api.html
Bacic Usage - https://skpy.t.allofti.me/usage.html

```
class Skype
The main Skype instance. Provides methods for retrieving various other object types.

user
SkypeContact – Contact information for the connected account.

contacts
SkypeContacts – Container of contacts for the connected user.

chats
SkypeChats – Container of conversations for the connected user.

settings
SkypeSettings – Read/write access to server-side account options.

services
dict – Skype credit and other paid services for the connected account.

translate
SkypeTranslator – Connected instance of the translator service.

conn
SkypeConnection – Underlying connection instance.

__init__(user=None, pwd=None, tokenFile=None, connect=True)
Create a new Skype object and corresponding connection.

If user and pwd are given, they will be passed to SkypeConnection.setUserPwd(). This can be either a Skype username/password pair, or a Microsoft account email address and its associated password.

If a token file path is present, it will be used if valid. On a successful connection, the token file will also be written to.

By default, a connection attempt will be made if any valid form of credentials are supplied. It is also possible to handle authentication manually, by working with the underlying connection object instead.

Parameters
user (str) – Skype username of the connecting account
pwd (str) – corresponding Skype account password
tokenFile (str) – path to file used for token storage
connect (bool) – whether to try and connect straight away
Raises
SkypeAuthException – if connecting, and the login request is rejected
SkypeApiException – if connecting, and the login form can’t be processed
getEvents()
Retrieve a list of events since the last poll. Multiple calls may be needed to retrieve all events.

If no events occur, the API will block for up to 30 seconds, after which an empty list is returned. As soon as an event is received in this time, it is returned immediately.

Returns
a list of events, possibly empty
Return type
SkypeEvent list
setPresence(status=Online)
Set the current user’s presence on the network. Supports Status.Online, Status.Busy or Status.Hidden (shown as Status.Offline to others).

Parameters
status (Status) – new availability to display to contacts
setMood(mood)
Update the activity message for the current user.

Parameters
mood (str) – new mood message
setAvatar(image)
Update the profile picture for the current user.

Parameters
image (file) – a file-like object to read the image from
getUrlMeta(url)
Retrieve various metadata associated with a URL, as seen by Skype.

Parameters
url (str) – address to ping for info
Returns
metadata for the website queried
Return type
dict
```
```
class SkypeChats
A container of conversations, providing caching of user info to reduce API requests.

Key lookups allow retrieving conversations by identifier.

recent()
Retrieve a selection of conversations with the most recent activity, and store them in the cache.

Each conversation is only retrieved once, so subsequent calls will retrieve older conversations.

Returns
collection of recent conversations
Return type
SkypeChat list
chat(id)
Get a single conversation by identifier.

Parameters
id (str) – single or group chat identifier
create(members=(), admins=())
Create a new group chat with the given users.

The current user is automatically added to the conversation as an admin. Any other admin identifiers must also be present in the member list.

Parameters
members (str list) – user identifiers to initially join the conversation
admins (str list) – user identifiers to gain admin privileges
static urlToIds(url)
Resolve a join.skype.com URL and returns various identifiers for the group conversation.

Parameters
url (str) – public join URL, or identifier from it
Returns
related conversation’s identifiers – keys: id, long, blob
Return type
dict
```

```
class SkypeMsg
A message either sent or received in a conversation.

An edit is represented by a follow-up message with the same clientId, which replaces the earlier message.

id
str – Identifier of the message provided by the server, usually a timestamp.

type
str – Raw message type, as specified by the Skype API.

time
datetime.datetime – Original arrival time of the message.

clientId
str – Identifier generated by the client, used as a reference for edits.

user
SkypeUser – User that sent the message.

chat
SkypeChat – Conversation where this message was received.

content
str – Raw message content, as received from the API.

html
str – Recreated content string based on the field values.

deleted
bool – Whether the message content was deleted by the sender.
```
