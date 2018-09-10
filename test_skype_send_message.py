import unittest
import skype_send_message
class skype_send_message_test(unittest.TestCase):
    """skype_send_message tests"""
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print ("setUpClass")
        print ("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print ("==========")
        print ("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print ("Tear down for [" + self.shortDescription() + "]")
        print ("")

    def test_password(self):
        """PASSWORD is SET, TEST"""
        print("id: " + self.id())
        self.assertEqual(skype_send_message.keyring.get_password("Skype", "username"), "password")

    def test_password1(self):
        """PASSWORD is NOT SET, TEST"""
        print("id: " + self.id())
        self.assertNotEqual(skype_send_message.keyring.get_password("username", "password"), "password")
        
if __name__ == '__main__' :
    unittest.main()
