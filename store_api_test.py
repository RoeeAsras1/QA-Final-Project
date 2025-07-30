def test_contact_us_valid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://atid.store")
    driver.find_element(By.XPATH, '//*[@id="menu-item-829"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="wpforms-15-field_0"]').send_keys("israel")
    driver.find_element(By.ID, 'wpforms-15-field_5').send_keys("test")
    driver.find_element(By.ID, 'wpforms-15-field_4').send_keys("test@test.com")
    driver.find_element(By.ID, 'wpforms-15-field_2').send_keys("test my selenium")
    driver.find_element(By.ID, 'wpforms-submit-15').click()
    sleep(5)
    text = driver.find_element(By.XPATH, '//*[@id="wpforms-confirmation-15"]/p').get_attribute('innerText')
    if text == 'Thanks for contacting us! We will be in touch with you shortly.':
        print('Test Passed V')
    else:
        print('Test Failed X')
















