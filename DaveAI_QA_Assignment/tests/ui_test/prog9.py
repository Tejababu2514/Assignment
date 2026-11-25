
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.iamdave.ai/"


# Setup: open Chrome before each test
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)

    yield browser

    # Teardown: close Chrome after each test and after 10 sec
    time.sleep(10)
    browser.quit()


# Test 1: Verify that the website opens successfully
def test_website_loads(driver):
    driver.get(BASE_URL)

    assert driver.title != ""
    assert "DaveAI" in driver.title


# Test 2: Verify that the homepage heading is displayed
def test_homepage_heading(driver):
    driver.get(BASE_URL)

    heading = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(), 'Automotive Intelligence Across Every Function')]")
        )
    )

    assert heading.is_displayed()




def test_book_demo_navigation_and_form(driver):
    driver.get(BASE_URL)

    # Step 1: Click Book Demo
    book_demo = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='book-demo']")
        )
    )
    book_demo.click()

    # Step 2: Verify navigation
    WebDriverWait(driver, 15).until(
        EC.url_contains("/book-demo/")
    )
    assert "/book-demo/" in driver.current_url

    # Step 3: Fill the form
    wait = WebDriverWait(driver, 20)

    name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Name']")
        )
    )
    name.send_keys("Test User")

    email = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Work Email']"
    )
    email.send_keys("test@example.com")

    company = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Company name']"
    )
    company.send_keys("Test Company")

    phone = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Phone number']"
    )
    phone.send_keys("9876543210")

    # Step 4: Validate entered values
    assert name.get_attribute("value") == "Test User"
    assert email.get_attribute("value") == "test@example.com"
    assert company.get_attribute("value") == "Test Company"

    print("Book Demo navigation and form interaction successful")

# Test 4: Verify Contact form input fields
def test_contact_form_fields(driver):
    driver.get(BASE_URL + "contact-us/")

    name_field = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder*='Name']")
        )
    )

    email_field = driver.find_element(
        By.CSS_SELECTOR, "input[placeholder*='Email']"
    )

    name_field.send_keys("Test User")
    email_field.send_keys("test@example.com")

    assert name_field.get_attribute("value") == "Test User"
    assert email_field.get_attribute("value") == "test@example.com"
