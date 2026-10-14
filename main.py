from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def open_form():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

def test_text_and_password_input():
    try:
        open_form()
        driver.find_element(By.NAME, "my-text").send_keys("Hello Selenium")
        driver.find_element(By.NAME, "my-password").send_keys("secret123")
        driver.find_element(By.TAG_NAME, "form").submit()
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Form submitted"))
        print("Test 1 passed: Text and password input")
    except Exception as e:
        print(f"Test 1 failed: {e}")

def test_dropdown_and_checkbox():
    try:
        open_form()
        dropdown = driver.find_element(By.NAME, "my-select")
        dropdown.find_element(By.XPATH, "//option[. = 'Two']").click()
        checkbox = driver.find_element(By.ID, "my-check-1")
        if not checkbox.is_selected():
            checkbox.click()
        driver.find_element(By.TAG_NAME, "form").submit()
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Form submitted"))
        print("Test 2 passed: Dropdown and checkbox")
    except Exception as e:
        print(f"Test 2 failed: {e}")

def test_color_and_range():
    try:
        open_form()
        driver.find_element(By.NAME, "my-colors").send_keys("#ff0000")
        driver.find_element(By.NAME, "my-range").send_keys("7")
        driver.find_element(By.TAG_NAME, "form").submit()
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Form submitted"))
        print("Test 3 passed: Color picker and range slider")
    except Exception as e:
        print(f"Test 3 failed: {e}")

def test_radio_buttons():
    try:
        open_form()
        radio = driver.find_element(By.ID, "my-radio-2")
        if not radio.is_selected():
            radio.click()
        checkbox = driver.find_element(By.ID, "my-check-2")
        if not checkbox.is_selected():
            checkbox.click()
        driver.find_element(By.TAG_NAME, "form").submit()
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Form submitted"))
        print("Test 4 passed: Radio and checkbox")
    except Exception as e:
        print(f"Test 4 failed: {e}")

if __name__ == "__main__":
    try:
        test_text_and_password_input()
        test_dropdown_and_checkbox()
        test_color_and_range()
        test_radio_buttons()
    finally:
        driver.quit()
