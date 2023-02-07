import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class Testwebpage:
    load_dotenv()

    def test_url(self):
        driver.get(os.getenv("BASE_URL"))
        driver.maximize_window()
        page_url = driver.current_url
        assert os.getenv('BASE_URL') in page_url



    def test_cleanup(self):
        driver.quit()
