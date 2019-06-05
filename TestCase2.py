#Simple unitest template
import unittest
from selenium import webdriver


class title_test2(unittest.TestCase):
    broswser = webdriver.Firefox()

    @classmethod
    def setUp(self):
        print('Naujas testas')

    @classmethod
    def tearDown(self):
        print('Testas done')

    @classmethod
    def tearDownClass(cls):
        cls.broswser.close()

    def test_browser(self):
        self.broswser.get('https://www.google.com/')
        self.assertEqual('Google',self.broswser.title,'Name is not same')

    def test_browser2(self):
        self.broswser.get('https://www.google.com/')
        self.assertNotEqual('Googlase',self.broswser.title,'Name is Googlase')

    def test_browser3(self):
        self.broswser.get('https://www.google.com/')
        self.assertNotEqual('', self.broswser.title, 'Name is Googlae')


if __name__ =="__main__":
    unittest.main()