import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

class Testwebpage:
    load_dotenv()

    def test_url(self):
        driver.get(os.getenv("BASE_URL"))
        driver.maximize_window()
        page_url = driver.current_url
        assert os.getenv('BASE_URL') in page_url

        time.sleep(10)

    def test_cleanup(self):
        driver.quit()