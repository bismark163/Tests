# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from group import ggg

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class LogIn(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("https://spb13.ukit.com/")

    def login(self, wd, ggg):
        wd.find_element_by_link_text("Log In").click()
        wd.find_element_by_id("sign_in_email").click()
        wd.find_element_by_id("sign_in_email").clear()
        wd.find_element_by_id("sign_in_email").send_keys(ggg.mail)
        wd.find_element_by_id("sign_in_password").click()
        wd.find_element_by_id("sign_in_password").clear()
        wd.find_element_by_id("sign_in_password").send_keys(ggg.passw)
        wd.find_element_by_id("sign_in_btn").click()
        wd.find_element_by_xpath("//div[3]/span").click()
        wd.find_element_by_css_selector("span.icon-content-special-off").click()


    
    def test_LogIn(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, ggg(mail="veider-93@mail.ru", passw="24775252d"))
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
