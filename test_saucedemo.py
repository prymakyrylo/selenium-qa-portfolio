from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

BASE_URL = "https://www.saucedemo.com"

# ── HELPER FUNCTIONS ──────────────────────────────────────────────────────────

def login(driver, username, password):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# ── SETUP ─────────────────────────────────────────────────────────────────────

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# ── TESTS ─────────────────────────────────────────────────────────────────────

def test_valid_login(driver):
    login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
