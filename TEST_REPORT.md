```
Testing started at 1:45 ...
/home/idumenskyi/work/pycharm/test_pyims_with_main/venv/bin/python /home/idumenskyi/apps/pycharm-2018.1.3/helpers/pycharm/_jb_unittest_runner.py --path /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py
Launching unittests with arguments python -m unittest /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py in /home/idumenskyi/work/pycharm/test_pyims_with_main
setUpClass
==========Set up for [MESSAGES]
password is set  None
id: test_skype_send_message.SkypeSendTextMessageTest.test_messages_text_message
Tear down for [MESSAGES]

password deleted:  None

Error
Traceback (most recent call last):
  File "/usr/lib/python3.6/unittest/case.py", line 59, in testPartExecutor
    yield
  File "/usr/lib/python3.6/unittest/case.py", line 605, in run
    testMethod()
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py", line 44, in test_messages_text_message
    self.assertEqual(skype_send_message.messages("nexus12141", "nexus12142"), "HELLO, TEST11")
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/skype_send_message.py", line 39, in messages
    return str(message_text)
NameError: name 'message_text' is not defined

Set up for [SEND MESSAGE is SET, TEST]
password is set  None
id: test_skype_send_message.SkypeSendTextMessageTest.test_send_text_message
Welcome to 'Skype send message'. 
Sending: 
Your message is send
Tear down for [SEND MESSAGE is SET, TEST]

password deleted:  None
==========
tearDownClass

Ran 2 tests in 5.620s

FAILED (errors=1)

Process finished with exit code 1

```
