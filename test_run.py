import os
import sys
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
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

    def test_kitchen_background_slider(self):
        try:
            driver.get("https://rueckwand24.com/products/kuechenrueckwand-weiss")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        except:
            exit("Cookie Pop up funktioniert nicht [Küchenrückwand Slider]")
        try:
            slider = driver.find_element(By.CLASS_NAME, value='cropper-crop-box')
            action = ActionChains(driver)
            action.click_and_hold(slider).move_by_offset(50, 0).perform()
            action.click_and_hold(slider).move_by_offset(-50, 0).perform()
            action.click_and_hold(slider).move_by_offset(90, 0).perform()
            action.click_and_hold(slider).move_by_offset(-90, 0).perform()
            action.click_and_hold(slider).move_by_offset(-50, 0).perform()
            action.click_and_hold(slider).move_by_offset(50, 0).perform()
            action.click_and_hold(slider).move_by_offset(-90, 0).perform()
            action.click_and_hold(slider).move_by_offset(90, 0).perform()
            time.sleep(3)
        except:
            exit("Image Cropper funktioniert nicht richtig [Küchenrückwand Slider]")
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("200")
        except:
            exit("Eingabefeld für Maße:Breite funktioniert nicht [Küchenrückwand Slider]")
        action.click_and_hold(slider).move_by_offset(0, 50).perform()
        action.click_and_hold(slider).move_by_offset(0, -50).perform()
        action.click_and_hold(slider).move_by_offset(0, 70).perform()
        action.click_and_hold(slider).move_by_offset(0, -70).perform()
        action.click_and_hold(slider).move_by_offset(0, -50).perform()
        action.click_and_hold(slider).move_by_offset(0, 50).perform()
        action.click_and_hold(slider).move_by_offset(0, -70).perform()
        action.click_and_hold(slider).move_by_offset(0, 70).perform()
        time.sleep(3)



    def test_product_categories(self):
        driver.get(os.getenv("BASE_URL"))
        driver.maximize_window()
        page_url = driver.current_url
        assert os.getenv('BASE_URL') in page_url
        time.sleep(3)
        """driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        time.sleep(0.5)"""
        driver.get("https://rueckwand24.com/collections/kuechenrueckwand")
        time.sleep(0.5)
        try:
            content = driver.find_element(By.CLASS_NAME, value="section-header__title")
            content.text == "Küchenrückwand"
            time.sleep(0.5)
        except:
            exit('H1 "Küchenrückwand" wurde nicht gefunden [Produkt Kategorien Collection Pages]')

        driver.get("https://rueckwand24.com/collections/duschrueckwand")
        time.sleep(0.5)
        try:

            content = driver.find_element(By.CLASS_NAME, value="section-header__title")
            content.text == "Duschrückwand"
            time.sleep(0.5)
        except:
            exit('H1 "Duschrückwand" wurde nicht gefunden [Produkt Kategorien Collection Pages]')

        driver.get("https://rueckwand24.com/collections/spritzschutz")
        time.sleep(0.5)
        try:
            content = driver.find_element(By.CLASS_NAME, value="section-header__title")
            content.text == "Spritzschutz"
            time.sleep(0.5)
        except:
            exit('H1 "Spritzschutz" wurde nicht gefunden [Produkt Kategorien Collection Pages]')

        driver.get("https://rueckwand24.com/collections/acryl-bild-foto")
        time.sleep(0.5)
        try:
            content = driver.find_element(By.CLASS_NAME, value="section-header__title")
            content.text == "Acryl Bild-Foto"
            pName = content.text
            print(pName)
        except:
            exit('H1 "Spritzschutz" wurde nicht gefunden [Produkt Kategorien Collection Pages]')




    def test_kitchen_background(self):
        driver.get("https://rueckwand24.com/products/kuechenrueckwand-weiss")
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        except:
            print("Cookie Pop up funktioniert nicht [Küchenrückwand]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1-first"]/div/div[1]/div[1]/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1-first"]/div/div[1]/div[1]/button[1]').click()
            time.sleep(0.5)
        except:
            print('Vor- und Zurück-Button für Bilderanzeige funktioniert nicht [Küchenrückwand]')
        try:
            material = driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]')
            material.click()
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Probleme mit Materialienauswahl [Küchenrückwand]')

        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("5")
            FalseDimensions = driver.find_element(By.XPATH, '//*[@id="AddToCartForm-product-template-1"]/div[1]/div/div[2]')
            FalseDimensions.text == "Die Mindestgröße muss min. 10 cm betragen"
            pName = FalseDimensions.text
            print(pName)
        except:
            exit('Warnnachricht für falche Maße:Breite wird nicht richtig angezeigt oder Inputfeld:Breite funktioniert nicht [Küchenrückwand]')
        try:
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("150")
            inputWidth.send_keys("300")
        except:
            exit("Inputfeld:Breite funktioniert nicht richtig [Küchenrückwand]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("5")
            FalseDimensions = driver.find_element(By.XPATH, '//*[@id="AddToCartForm-product-template-1"]/div[1]/div/div[2]')
            FalseDimensions.text == "Die Mindestgröße muss min. 10 cm betragen"
            pName = FalseDimensions.text
            print(pName)
        except:
            exit('Warnnachricht für falche Maße:Höhe wird nicht richtig angezeigt oder Inputfeld:Höhe funktioniert nicht [Küchenrückwand]')
        try:
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
        except:
            exit("Inputfeld:Höhe funktioniert nicht richtig [Küchenrückwand]")

        # Stückzahl Input und Button prüfen
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [Küchenrückwand]")

        inputQuantity = driver.find_element(By.CLASS_NAME, value="js-qty__input")
        action = ActionChains(driver)
        action.move_to_element(inputQuantity)
        time.sleep(5)
        #inputQuantity.click()
        #inputQuantity.clear()
        #inputQuantity.send_keys(2)

        # zu Einkaufswagen gehen über Warenkorb Button
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
            time.sleep(7)
        except:
            exit('Fehler: Warenkorbbutton')
        try:
            driver.find_element(By.XPATH, '//*[@id="jsCrosssell"]/div/div/div[2]/div[1]/div[3]/div[3]/a[1]').click()
        except:
            exit('Fehler: Bestellübersicht Pop up/ Einkaufswagen-Button auf Pop up [Küchenrückwand]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2'))
            )
            cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2')
            cart.text == 'Einkaufswagen'
        except:
            exit('Fehler: H1 "Einkaufswagen" auf Einkaufswagenseite [Küchenrückwand]')
        #driver.find_element(By.LINK_TEXT, 'Entfernen').click()
        #emptyMessage = driver.find_element(By.CLASS_NAME,  value="cart--empty-message")
        #emptyMessage.text == "Ihr Einkaufswagen ist im Moment leer."
        #driver.find_element(By.CLASS_NAME, value="cart--continue-message")
        try:
            messageField = driver.find_element(By.XPATH, '//*[@id="CartSpecialInstructions"]')
            messageField.click()
            messageField.send_keys("ABCdefg1234")
        except:
            exit('Fehler: Eingabefeld für "Hinweise für den Verkäufer" [Küchenrückwand]')
        try:
            cash = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/form/div/div[2]/button[2]')
            cash.click()
        except:
            exit('Fehler: Zur-Kasse-Button auf ein Einkaufswagenseite [Küchenrückwand]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Form1"]/div[1]/div/div[1]/div[1]/span/h2'))
            )
            expressCheckout = driver.find_element(By.CLASS_NAME, value='_3SwDm')
            expressCheckout.text == 'Express Checkout'
            driver.back()
            time.sleep(3)
        except:
            exit('Fehler: Anzeigen/Laden der Bezahlpage [Küchenrückwand]')

    def test_upload_own_image(self):
        driver.get("https://rueckwand24.com/collections/kuechenrueckwand")
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print("Cookie Pop up funktioniert nicht [Küchenrückwand eigenes Motiv]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[1]/div').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Eigenes Motiv Produkt auf Collectionpage [Küchenrückwand eigenes Motiv]')
        try:
            element = driver.find_element(By.XPATH, '//*[@id="dropZoneInput"]')
            element.send_keys(r"C:\Users\parha\Pictures\DummyBild.jpg")
            time.sleep(15)
        except:
            exit('Fehler: Bild hochladen (DragandDrop oder Button) [Küchenrückwand eigenes Motiv]')
        try:
            driver.find_element(By.ID, "redirect-group-btn_4").click()
            time.sleep(1)
        except:
            exit('Fehler: "Jetzt Konfiguren" Button bei Bild Hochladen [Küchenrückwand eigenes Motiv]')
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("20")
        except:
            exit("Fehler: Inputfeld: Maße Höhe funktioniert nicht richtig [Küchenrückwand eigenes Motiv]")
        try:
            action = ActionChains(driver)
            slider = driver.find_element(By.CLASS_NAME, value='cropper-crop-box')
            action.click_and_hold(slider).move_by_offset(0, 30).perform()
            action.click_and_hold(slider).move_by_offset(0, -30).perform()
            action.click_and_hold(slider).move_by_offset(0, -30).perform()
            action.click_and_hold(slider).move_by_offset(0, 30).perform()
        except:
            exit("Fehler: Cropper Box/ Cropper Box Bewegung Y-Achse")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("25")
        except:
            exit("Fehler: Inputfeld: Maße Höhe funktioniert nicht richtig [Küchenrückwand eigenes Motiv]")
        try:
            action.click_and_hold(slider).move_by_offset(0, 30).perform()
            action.click_and_hold(slider).move_by_offset(0, -30).perform()
            action.click_and_hold(slider).move_by_offset(0, -30).perform()
            action.click_and_hold(slider).move_by_offset(0, 30).perform()
        except:
            exit("Fehler: Cropper Box/ Cropper Box Bewegung X-Achse [Küchenrückwand eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Probleme mit Materialienauswahl [Küchenrückwand eigenes Motiv]')
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [Küchenrückwand eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
            time.sleep(7)
        except:
            exit('Fehler: Warenkorbbutton [Küchenrückwand eigenes Motiv]')
        try:
            driver.find_element(By.XPATH, '//*[@id="jsCrosssell"]/div/div/div[2]/div[1]/div[3]/div[3]/a[1]').click()
        except:
            exit('Fehler: Bestellübersicht Pop up/ Einkaufswagen-Button auf Pop up [Küchenrückwand eigenes Motiv]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2'))
            )
            cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2')
            cart.text == 'Einkaufswagen'
        except:
            exit('Fehler: H1 "Einkaufswagen" auf Einkaufswagenseite [Küchenrückwand eigenes Motiv]')
        try:
            messageField = driver.find_element(By.XPATH, '//*[@id="CartSpecialInstructions"]')
            messageField.click()
            messageField.send_keys("ABCdefg1234")
        except:
            exit('Fehler: Eingabefeld für "Hinweise für den Verkäufer" [Küchenrückwand eigenes Motiv]')
        try:
            cash = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/form/div/div[2]/button[2]')
            cash.click()
        except:
            exit('Fehler: Zur-Kasse-Button auf ein Einkaufswagenseite [Küchenrückwand eigenes Motiv]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Form1"]/div[1]/div/div[1]/div[1]/span/h2'))
            )
            expressCheckout = driver.find_element(By.CLASS_NAME, value='_3SwDm')
            expressCheckout.text == 'Express Checkout'
            driver.back()
            time.sleep(3)
        except:
            exit('Fehler: Anzeigen/Laden der Bezahlpage [Küchenrückwand eigenes Motiv]')



    def test_shower_background(self):
        driver.get('https://rueckwand24.com/collections/duschrueckwand')
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print("Cookie Pop up funktioniert nicht [Duschrückwand]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[2]/div').click()
            driver.find_element(By.XPATH, '//*[@id="main-carousel"]/div[1]/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="main-carousel"]/div[1]/button[1]').click()
        except:
            exit('Vor- und Zurück-Button für Bilderanzeige funktioniert nicht [Duschrückwand]')
        # 1 Rückwand
        try:
            driver.find_element(By.XPATH, '//*[@id="switch-button-3__3er_Box-2"]').click()
        except:
            exit('Fehler: Auswahl 3 Duschrückwände [Duschrückwand]')
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            time.sleep(0.5)
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld1: Maße Breite funktioniert nicht [Duschrückwand]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
            time.sleep(3)
        except:
            exit("Eingabefeld1: Maße Höhe funktioniert nicht richtig [Duschrückwand]")
        # 2 Rückwand
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width2"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld2: Maße Breite funktioniert nicht [Duschrückwand]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height2"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
        except:
            exit("Eingabefeld2: Maße Höhe funktioniert nicht richtig [Duschrückwand]")
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width3"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld3: Maße Breite funktioniert nicht")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height3"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
            time.sleep(3)
        except:
            exit("Eingabefeld3: Maße Höhe funktioniert nicht richtig [Duschrückwand]")
        try:
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Probleme mit Materialienauswahl [Duschrückwand]')
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [Duschrückwand]")
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
        except:
            exit('Fehler: Warenkorbbutton [Duschrückwand]')

    def test_shower_number_backgrounds(self):
        driver.get('https://rueckwand24.com/collections/duschrueckwand')
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
        except:
            print("Cookie Pop up funktioniert nicht [Duschrückwand]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[2]/div').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Aufrufen von Produkt von Collectionseite nach anklicken [Duschrückwand]')
        try:
            driver.find_element(By.XPATH, '//*[@id="switch-button-active-2_Контур_13-2"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="switch-button-3__3er_Box-2"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="switch-button-1__1er_Box"]').click()
        except:
            exit('Fehler: Auswahlbuttons für 1, 2 oder 3 Duschrückwände [Duschrückwand]')




    def test_shower_upload_own_image(self):
        driver.get("https://rueckwand24.com/collections/duschrueckwand")
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print("Cookie Pop up funktioniert nicht [Duschrückwand eigenes Motiv]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[1]/div').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Eigenes Motiv Produkt auf Collectionpage [Duschrückwand eigenes Motiv]')
        try:
            element = driver.find_element(By.XPATH, '//*[@id="dropZoneInput"]')
            element.send_keys(r"C:\Users\parha\Pictures\DummyBild.jpg")
            time.sleep(15)
        except:
            exit('Fehler: Bild hochladen (DragandDrop oder Button) [Duschrückwand eigenes Motiv]')
        try:
            driver.find_element(By.ID, "redirect-group-btn_4").click()
            time.sleep(1)
        except:
            exit('Fehler: "Jetzt Konfiguren" Button bei Bild Hochladen [Duschrückwand eigenes Motiv]')
        try:
            driver.find_element(By.XPATH, '//*[@id="switch-button-active-2_Контур_13-2"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="switch-button-1__1er_Box"]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="switch-button-3__3er_Box-2"]').click()
        except:
            exit('Fehler: Auswahlbuttons für 1, 2 oder 3 Duschrückwände [Duschrückwand eigenes Motiv]')
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            time.sleep(0.5)
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld1: Maße Breite funktioniert nicht [Duschrückwand eigenes Motiv]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
            time.sleep(3)
        except:
            exit("Eingabefeld1: Maße Höhe funktioniert nicht richtig [Duschrückwand eigenes Motiv]")
            # 2 Rückwand
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width2"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld2: Maße Breite funktioniert nicht [Duschrückwand eigenes Motiv]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height2"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
        except:
            exit("Eingabefeld2: Maße Höhe funktioniert nicht richtig [Duschrückwand eigenes Motiv]")
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width3"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("10")
            inputWidth.send_keys("75")
            inputWidth.send_keys("150")
        except:
            exit("Eingabefeld3: Maße Breite funktioniert nicht [Duschrückwand eigenes Motiv]")
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height3"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("10")
            inputHeight.send_keys("75")
            inputHeight.send_keys("150")
            time.sleep(3)
        except:
            exit("Eingabefeld3: Maße Höhe funktioniert nicht richtig [Duschrückwand eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Probleme mit Materialienauswahl [Duschrückwand eigenes Motiv]')
        try:
            driver.find_element(By.XPATH,
                                '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH,
                                '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH,
                                '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [Duschrückwand eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
        except:
            exit('Fehler: Warenkorbbutton [Duschrückwand eigenes Motiv]')


    def test_splash_guard(self):
        driver.get("https://rueckwand24.com/collections/Spritzschutz")
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print("Cookie Pop up funktioniert nicht [Spritzschutz]")"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[2]/div').click()
            time.sleep(1)
        except:
            exit('Fehler: SpritzschutzProdukt auf Collectionpage  klicken und laden [Spritzschutz]')
        try:
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("15")
            time.sleep(0.5)
        except:
            exit("Eingabefeld: Maße Breite funktioniert nicht [Spritzschutz]")
        try:
            action = ActionChains(driver)
            slider = driver.find_element(By.CLASS_NAME, value='cropper-crop-box')
            action.click_and_hold(slider).move_by_offset(30, 0).perform()
            action.click_and_hold(slider).move_by_offset(-30, 0).perform()
            action.click_and_hold(slider).move_by_offset(-30, 0).perform()
            action.click_and_hold(slider).move_by_offset(30, 0).perform()
        except:
            exit("Fehler: Cropper Box/ Cropper Box Bewegung X-Achse [Spritzschutz")
            raise
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("25")
            inputWidth.clear()
            inputWidth.send_keys("40")
        except:
            exit("Inputfeld: Maße Höhe funktioniert nicht richtig [Spritzschutz]")
        try:
            action.click_and_hold(slider).move_by_offset(0, 20).perform()
            action.click_and_hold(slider).move_by_offset(0, -20).perform()
            action.click_and_hold(slider).move_by_offset(0, -20).perform()
            action.click_and_hold(slider).move_by_offset(0, 20).perform()
        except:
            exit("Fehler: Cropper Box/ Cropper Box Bewegung X-Achse [Spritzschutz]")
        try:
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Probleme mit Materialienauswahl [Spritzschutz]')
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [Spritzschutz]")
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
            time.sleep(7)
        except:
            exit('Fehler: Warenkorbbutton [Spritzschutz]')
        try:
            driver.find_element(By.XPATH, '//*[@id="jsCrosssell"]/div/div/div[2]/div[1]/div[3]/div[3]/a[1]').click()
        except:
            exit('Fehler: Bestellübersicht Pop up/ Einkaufswagen-Button auf Pop up [Spritzschutz]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2'))
            )
            cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2')
            cart.text == 'Einkaufswagen'
        except:
            exit('Fehler: H1 "Einkaufswagen" auf Einkaufswagenseite [Spritzschutz]')
        try:
            messageField = driver.find_element(By.XPATH, '//*[@id="CartSpecialInstructions"]')
            messageField.click()
            messageField.send_keys("ABCdefg1234")
        except:
            exit('Fehler: Eingabefeld für "Hinweise für den Verkäufer" [Spritzschutz]')
        try:
            cash = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/form/div/div[2]/button[2]')
            cash.click()
        except:
            exit('Fehler: Zur-Kasse-Button auf ein Einkaufswagenseite [Spritzschutz]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Form1"]/div[1]/div/div[1]/div[1]/span/h2'))
            )
            expressCheckout = driver.find_element(By.CLASS_NAME, value='_3SwDm')
            expressCheckout.text == 'Express Checkout'
            driver.back()
            time.sleep(3)
        except:
            exit('Fehler: Anzeigen/Laden der Bezahlpage [Spritzschutz]')

    def test_spash_guard_upload_own_image(self):
        driver.get("https://rueckwand24.com/collections/spritzschutz")
        """try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print('Fehler: Cookie Pop up funktioniert nicht [SpritzSchutz eigenes Motiv]')"""
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[1]/div').click()
            time.sleep(0.5)
        except:
            exit('Fehler: SpritzschutzProdukt mit eigenem Bild auf Collectionpage  klicken und laden [SpritzSchutz eigenes Motiv]')
        try:
            element = driver.find_element(By.XPATH, '//*[@id="dropZoneInput"]')
            element.send_keys(r"C:\Users\parha\Pictures\DummyBild.jpg")
            time.sleep(15)
        except:
            exit('Fehler: Bild hochladen (DragandDrop oder Button)[SpritzSchutz eigenes Motiv]')
        try:
            driver.find_element(By.ID, "redirect-group-btn_4").click()
            time.sleep(1)
        except:
            exit('Fehler: "Jetzt Konfiguren" Button bei Bild Hochladen [SpritzSchutz eigenes Motiv]')
        try:
            inputHeight = driver.find_element(By.XPATH, '//*[@id="config_height"]')
            inputWidth = driver.find_element(By.XPATH, '//*[@id="config_width"]')
            inputWidth.click()
            inputWidth.clear()
            inputWidth.send_keys("15")
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("25")
        except:
            exit("Eingabefeld: Maße Breite funktioniert nicht [SpritzSchutz eigenes Motiv]")
        try:
            action = ActionChains(driver)
            slider = driver.find_element(By.CLASS_NAME, value='cropper-crop-box')
            action.click_and_hold(slider).move_by_offset(20, 0).perform()
            action.click_and_hold(slider).move_by_offset(-20, 0).perform()
            action.click_and_hold(slider).move_by_offset(-20, 0).perform()
            action.click_and_hold(slider).move_by_offset(20, 0).perform()
        except:
            exit("Fehler: Cropper Box/ Cropper Box Bewegung X-Achse [SpritzSchutz eigenes Motiv]")
        try:
            inputHeight.click()
            inputHeight.clear()
            inputHeight.send_keys("25")
        except:
            exit("Eingabefeld: Maße Höhe funktioniert nicht richtig [SpritzSchutz eigenes Motiv]")
        inputWidth.click()
        inputWidth.clear()
        inputWidth.send_keys("60")
        try:
            action.click_and_hold(slider).move_by_offset(0, 20).perform()
            action.click_and_hold(slider).move_by_offset(0, -20).perform()
            action.click_and_hold(slider).move_by_offset(0, -20).perform()
            action.click_and_hold(slider).move_by_offset(0, 20).perform()
        except:
            exit('Fehler: Cropper Box/ Cropper Box Bewegung Y-Achse [SpritzSchutz eigenes Motiv]')

        try:
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[1]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[2]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[3]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[4]').click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//*[@id="material-accordion"]/div[5]').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Probleme mit Materialienauswahl [SpritzSchutz eigenes Motiv]')
        try:
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[2]').click()
            driver.find_element(By.XPATH, '//*[@id="ProductSection-product-template-1"]/div[5]/div[5]/div/div/div[2]/div[1]/div/button[1]').click()
        except:
            exit("Fehler:Stückzahl-Erhöhen und Stückzahl-senken-Button [SpritzSchutz eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="AddToCart-product-template-1"]').click()
            time.sleep(7)
        except:
            exit('Fehler: Warenkorbbutton')
        try:
            driver.find_element(By.XPATH, '//*[@id="jsCrosssell"]/div/div/div[2]/div[1]/div[3]/div[3]/a[1]').click()
        except:
            exit('Fehler: Bestellübersicht Pop up/ Einkaufswagen-Button auf Pop up [SpritzSchutz eigenes Motiv]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2'))
            )
            cart = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/h2')
            cart.text == 'Einkaufswagen'
        except:
            exit('Fehler: H1 "Einkaufswagen" auf Einkaufswagenseite [SpritzSchutz eigenes Motiv]')
        try:
            messageField = driver.find_element(By.XPATH, '//*[@id="CartSpecialInstructions"]')
            messageField.click()
            messageField.send_keys("ABCdefg1234")
        except:
            exit('Fehler: Eingabefeld für "Hinweise für den Verkäufer" [SpritzSchutz eigenes Motiv]')
        try:
            cash = driver.find_element(By.XPATH, '//*[@id="shopify-section-cart-template"]/div[1]/div/form/div/div[2]/button[2]')
            cash.click()
        except:
            exit('Fehler: Zur-Kasse-Button auf ein Einkaufswagenseite [SpritzSchutz eigenes Motiv]')
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Form1"]/div[1]/div/div[1]/div[1]/span/h2'))
            )
            expressCheckout = driver.find_element(By.CLASS_NAME, value='_3SwDm')
            expressCheckout.text == 'Express Checkout'
            driver.back()
            time.sleep(3)
        except:
            exit('Fehler: Anzeigen/Laden der Bezahlpage [SpritzSchutz eigenes Motiv]')

    def test_upload(self):
        driver.get("https://rueckwand24.com/collections/kuechenrueckwand")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]'))
            )
            driver.find_element(By.XPATH, '//*[@id="pandectes-banner"]/div/div[2]/a[3]').click()
            time.sleep(0.5)
        except:
            print("Cookie Pop up funktioniert nicht [Küchenrückwand eigenes Motiv]")
        try:
            driver.find_element(By.XPATH, '//*[@id="js-product-ajax"]/div[1]/div[1]/div').click()
            time.sleep(0.5)
        except:
            exit('Fehler: Eigenes Motiv Produkt auf Collectionpage [Küchenrückwand eigenes Motiv]')
        try:
            element = driver.find_element(By.XPATH, '//*[@id="dropZoneInput"]')
            element.send_keys(r"DummyBilder/DummyBild1.jpg")
            time.sleep(15)
        except:
            exit('Fehler: Bild hochladen (DragandDrop oder Button) [Küchenrückwand eigenes Motiv]')
            raise
        try:
            driver.find_element(By.ID, "redirect-group-btn_4").click()
            time.sleep(1)
        except:
            exit('Fehler: "Jetzt Konfiguren" Button bei Bild Hochladen [Küchenrückwand eigenes Motiv]')























































