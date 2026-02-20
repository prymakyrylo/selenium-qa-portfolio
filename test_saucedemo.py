from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import pytest 
import time

BASE_URL = "https://www.saucedemo.com"

# ── HELPER FUNCTIONS ──────────────────────────────────────────────────────────

def login(driver, username, password):
     driver.get(BASE_URL)
     driver.find_element(By.ID, "user-name").send_keys(username)
     driver.find_element(By.ID, "password").send_keys(password)
     driver.find_element(By.ID, "login-button").click()

def nameFill(driver, first, last, zip_num):
     driver.find_element(By.ID, "first-name").send_keys(first)
     driver.find_element(By.ID, "last-name").send_keys(last)
     driver.find_element(By.ID, "postal-code").send_keys(zip_num)

# ── SETUP ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Nuclear option
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# ── TESTS ─────────────────────────────────────────────────────────────────────

def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce") 
    assert "inventory" in driver.current_url

def test_false_login(driver): 
     login(driver, "standard_use", "not-valid-password")  
     error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
     assert "Username and password do not match" in error.text

def test_empty_login(driver): 
     login(driver, "", "")  
     error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
     assert "Username is required" in error.text

def test_add_to_card(driver):
     login(driver, "standard_user", "secret_sauce")
     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
     badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
     assert badge.text == "1"

def test_full_checkout_flow(driver):
     login(driver, "standard_user", "secret_sauce")
     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
     driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
     driver.find_element(By.ID, "checkout").click() 
     nameFill(driver, "Kai", "Pryma", "10000") 
     driver.find_element(By.ID, "continue").click()

     wait = WebDriverWait(driver, 10)
     finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
     finish_button.click()

     message = driver.find_element(By.CLASS_NAME, "complete-header")
     assert "Thank you for your order!" in message.text

def test_remove_item_from_cart(driver):
     login(driver, "standard_user", "secret_sauce")
     driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
     driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()  

     # XPATH selector
     driver.find_element(By.XPATH, "//button[text()='Remove']").click()

     badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
     assert len(badges) == 0, f"Expected no badge, but found {len(badges)}"





