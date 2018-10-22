import unittest
import telegram_send_message


class TelegramSendTextMessageTest(unittest.TestCase):
    """telgram_send_message tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_send_text_message(self):
        """SEND MESSAGE is SET, TEST"""
        print("id: " + self.id())
        self.assertEqual(telegram_send_message.main('Your chat_id', 'TEST'), 'TEST')


if __name__ == '__main__':
    unittest.main()
