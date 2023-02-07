import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-notifications",
    "disable-infobars"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


class Testwebpage:
    load_dotenv()

    def test_product_categories(self):
        driver.get(os.getenv("BASE_URL"))
        driver.maximize_window()
        page_url = driver.current_url
        assert os.getenv('BASE_URL') in page_url
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        time.sleep(3)
        driver.get("https://rueckwand24.com/collections/kuechenrueckwand")
        time.sleep(2)
        content = driver.find_element(By.CLASS_NAME, value="section-header__title")
        content.text == "Küchenrückwand"
        time.sleep(2)
        driver.get("https://rueckwand24.com/collections/duschrueckwand")
        time.sleep(2)
        content = driver.find_element(By.CLASS_NAME, value="section-header__title")
        content.text == "Duschrückwand"
        time.sleep(2)
        driver.get("https://rueckwand24.com/collections/spritzschutz")
        time.sleep(2)
        content = driver.find_element(By.CLASS_NAME, value="section-header__title")
        content.text == "Spritzschutz"
        time.sleep(2)
        driver.get("https://rueckwand24.com/collections/acryl-bild-foto")
        time.sleep(2)
        content = driver.find_element(By.CLASS_NAME, value="section-header__title")
        content.text == "Acryl Bild-Foto"
        pName = content.text
        print(pName)


    def test_kitchen_background(self):
        driver.get("https://rueckwand24.com/products/kuechenrueckwand-weiss")
        driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1-first"]/div/div[1]/div[1]/button[2]').click()



