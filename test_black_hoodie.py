from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://atid.store/product/black-hoodie/")

try:
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
    print(f"Checking page: {title.text}")

    assert title.text.strip() == "Black Hoodie"

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'add-to-cart'))
    ).click()

    confirmation = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'woocommerce-message'))
    )

    if "has been added to your cart" in confirmation.text:
        print("Test Passed")
    else:
        print("Test Failed")

except Exception as e:
    print("Error:", e)

driver.quit()
















