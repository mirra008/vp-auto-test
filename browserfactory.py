from selenium import webdriver
import config as cfg
import unittest
import os


class PythonAutoTest(unittest.TestCase):

    def get_browsers(self):
        path = os.path.abspath('C:\webdriver\chromedriver.exe')
        DRIVERS_MAP = {
            "chrome": webdriver.Chrome(path),
            "firefox": webdriver.Firefox(),
            "ie": webdriver.Ie(),
        }
        return [DRIVERS_MAP[br] for br in cfg.BROWSERS if br in DRIVERS_MAP]

    def test_foo(self):
        for browser in self.get_browsers():
            browser.get("http://qa1-vp-portal.elasticbeanstalk.com")


if __name__ == '__main__':
    unittest.main()
