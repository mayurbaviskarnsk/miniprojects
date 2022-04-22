from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_login:

    def test_001_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/")
        self.driver.close()
        # self.driver.close()


    def test_002_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/")
        search = self.driver.find_element(By.XPATH,"/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[2]/ytd-searchbox[1]/form[1]/div[1]/div[1]/input[1]")
        search.send_keys("kanbai songs")
        self.driver.find_element(By.ID,"search-icon-legacy").click()
        # self.driver.close()
        # self.driver.get("https://github.com/")
        # self.driver.close()

