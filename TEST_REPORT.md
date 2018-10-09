```
Testing started at 15:57 ...
/home/idumenskyi/work/pycharm/test_pyims_with_main/venv/bin/python /home/idumenskyi/apps/pycharm-2018.1.3/helpers/pycharm/_jb_unittest_runner.py --path /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py
Launching unittests with arguments python -m unittest /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py in /home/idumenskyi/work/pycharm/test_pyims_with_main
setUpClass
==========Set up for [Get messages test]
password is set  None
password is set  None
id: test_skype_send_message.SkypeSendTextMessageTest.test_messages_text_message
Tear down for [Get messages test]

password deleted:  None
password deleted:  None

Error
Traceback (most recent call last):
  File "/usr/lib/python3.6/unittest/case.py", line 59, in testPartExecutor
    yield
  File "/usr/lib/python3.6/unittest/case.py", line 605, in run
    testMethod()
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py", line 45, in test_messages_text_message
    self.assertEqual(skype_send_message.messages("nexus12141", "nexus12142"), "HELLO, TEST11")
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/skype_send_message.py", line 47, in messages
    print(message_text)
NameError: name 'message_text' is not defined

Set up for [Send message test]
password is set  None
password is set  None
id: test_skype_send_message.SkypeSendTextMessageTest.test_send_text_message
Welcome to 'Skype send message'. 
Sending: 
Your message is send
Welcome to 'Skype send message'. 
Sending: 
Your message is send
Tear down for [Send message test]

password deleted:  None


Ran 2 tests in 17.080s

FAILED (errors=1)
password deleted:  None
==========
tearDownClass
Process finished with exit code 1

```
