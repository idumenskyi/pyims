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

## Testing

Usage import for testing:

```
import unittest
```
Run Test: both files skype_send_message.py and test_skype_send_message.py must be in one directory, run test_skype_send_message.py on terminal or cmd with command:

```
python -m unittest -v test_skype_send_message.py - on Windows

python3 -m unittest -v test_skype_send_message.py - on Linux-like 
```

### Result of Test:

```
Welcome to 'Skype send message'.
Type your username of Skype: nexus1214@ukr.net
Type user name of Skype for 1-to-1 conversation: nexus12142
Sending:
Type your message for user of Skype with you want to 1-to-1 conversation: Hello
Your message is send

setUpClass
==========
test_password (test_skype_send_message.skype_send_message_test)
PASSWORD is SET, TEST ... Set up for [PASSWORD is SET, TEST]
id: test_skype_send_message.skype_send_message_test.test_password
Tear down for [PASSWORD is SET, TEST]

ok

test_password1 (test_skype_send_message.skype_send_message_test)
PASSWORD is NOT SET, TEST ... Set up for [PASSWORD is NOT SET, TEST]
id: test_skype_send_message.skype_send_message_test.test_password1
Tear down for [PASSWORD is NOT SET, TEST]

ok
==========
tearDownClass

----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```
