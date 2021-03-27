from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config as cfg

PATH = cfg.PATH + "/chromedriver"
driver = webdriver.Chrome(PATH)

# Nav to orders page
driver.get(
    "https://www.amazon.in/gp/css/order-history?ref_=nav_AccountFlyout_orders"
)

# Loggin in
driver.find_element_by_id("ap_email").send_keys(cfg.USERNAME)
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys(cfg.PASSWORD)
driver.find_element_by_id("auth-signin-button").click()

# invoices
for iterator in range(cfg.PAGE):
    time.sleep(5)
    invc = driver.find_elements_by_link_text("Invoice")
    for elm in invc:
        elm.click()
        time.sleep(5)
        # Checking for "Invoice 1"
        try:
            invoiceElement = driver.find_element_by_link_text("Invoice 1")

            # Adding download tag to Invoices
            driver.execute_script(
                "arguments[0].setAttribute('download', 'download');",
                invoiceElement
            )
            time.sleep(3)
            # Downloading click
            invoiceElement.click()
            time.sleep(2)
        except:
            continue
    if (cfg.PAGE != 1):
        driver.find_element_by_link_text(str(iterator+2)).click()
