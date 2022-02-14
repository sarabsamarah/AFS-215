import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#driver = webdriver.Firefox('/Users/aaronsams/Desktop/ASF-215/driver/geckodriver')
def setUp(self):
    self.driver = webdriver.Chrome('/Users/aaronsams/Desktop/ASF-215/driver/chromedriver')
    self.driver.implicitly_wait(40)
    self.driver.set_page_load_timeout(50)
    self.driver.maximize_window()
def test_search(self):
    self.driver.get("https://google.com")
    search_bar = self.driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys("Hello World")
    search_bar.send_keys(Keys.RETURN)
def tearDown(self):
    self.driver.close()

if __name__ == '__main__':
unittest.main()