#Simple unitest template
import unittest
from selenium import webdriver


class title_test2(unittest.TestCase):
    broswser = webdriver.Firefox()
    names = ['Bingo', 'Yahoo', 'Google', 'Dabar Yahoo yra „Oath“ dalis']

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
        self.assertTrue('Google'==self.broswser.title,'Name is not same')

    def test_browser2(self):
        self.broswser.get('https://www.google.com/')
        self.assertFalse('Googlase'==self.broswser.title,'Name is Googlase')

    def test_browser3(self):
        self.assertIsNotNone(self.broswser)

    def test_browser4(self):
        self.broswser.get('https://www.yahoo.com/')
        self.assertIn(self.broswser.title,self.names)




if __name__ =="__main__":
    unittest.main()