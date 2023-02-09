import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType#
from selenium.webdriver.support import expected_conditions as EC
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
        time.sleep(3)
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
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
        )
        driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1-first"]/div/div[1]/div[1]/button[2]').click()
        driver.find_element(By.XPATH,'//*[@id="ProductSection-product-template-1-first"]/div/div[1]/div[1]/button[1]').click()
        material = driver.find_element(By.XPATH,'//*[@id="material-accordion"]/div[1]')
        material.click()
        driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
        time.sleep(0.5)

        inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
        inputWidth.click()
        inputWidth.clear()
        inputWidth.send_keys("5")
        FalseDimensions = driver.find_element(By.XPATH, '//*[@id="AddToCartForm-product-template-1"]/div[1]/div/div[2]')
        FalseDimensions.text == "Die Mindestgröße muss min. 10 cm betragen"
        pName = FalseDimensions.text
        print(pName)
        inputWidth.send_keys("10")
        inputWidth.send_keys("150")
        inputWidth.send_keys("300")
        time.sleep(0.5)
        inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
        inputHeight.click()
        inputHeight.clear()
        inputHeight.send_keys("5")
        FalseDimensions = driver.find_element(By.XPATH, '//*[@id="AddToCartForm-product-template-1"]/div[1]/div/div[2]')
        FalseDimensions.text == "Die Mindestgröße muss min. 10 cm betragen"
        pName = FalseDimensions.text
        inputHeight.send_keys("10")
        inputHeight.send_keys("75")
        inputHeight.send_keys("150")
        material.click
        # Stückzahl Input und Button prüfen
        driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
        driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
        driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        inputQuantity = driver.find_element(By.CLASS_NAME, value="js-qty__input")
        action = ActionChains(driver)
        action.move_to_element(inputQuantity)
        time.sleep(5)
        #inputQuantity.click()
        #inputQuantity.clear()
        #inputQuantity.send_keys(2)

        # zu Einkaufswagen gehen über Warenkorb Button
        driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
        time.sleep(5)
        driver.find_element(By. XPATH, '//*[@id="jsCrosssell"]/div/div/div[2]/div[1]/div[3]/div[3]/a[1]').click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2'))
        )
        cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2')
        cart.text == 'Einkaufswagen'
        #driver.find_element(By.LINK_TEXT, 'Entfernen').click()
        #emptyMessage = driver.find_element(By.CLASS_NAME,  value="cart--empty-message")
        #emptyMessage.text == "Ihr Einkaufswagen ist im Moment leer."
        #driver.find_element(By.CLASS_NAME, value="cart--continue-message")
        messageField = driver.find_element(By.XPATH, '//*[@id="CartSpecialInstructions"]')
        messageField.click()
        messageField.send_keys("ABCdefg1234")
        cash = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/form/div/div[2]/button[2]')
        cash.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Form1"]/div[1]/div/div[1]/div[1]/span/h2'))
        )
        expressCheckout = driver.find_element(By.CLASS_NAME, value='_3SwDm')
        expressCheckout.text == 'Express Checkout'
        driver.back()
        time.sleep(20)

    def test_kitchen_background_slider(self):
        driver.get("https://rueckwand24.com/products/kuechenrueckwand-weiss")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
        )
        driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()

        slider = driver.find_element(By.CLASS_NAME, value='class="cropper-crop-box')
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(50, 0).perform()




























