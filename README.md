# selenium-qa-portfolio

Automated end-to-end test suite for SauceDemo built with Python, Selenium, and pytest.


**Tech Stack**

Python 3.14
Selenium WebDriver - browser automation
pytest - test framework
ChromeDriver — Chrome browser driver (auto-managed via webdriver-manager)


**Test Coverage**

TestDescriptiontest_valid_loginVerifies successful login redirects to inventory pagetest_invalid_loginValidates error message for incorrect passwordtest_empty_loginValidates error message when login fields are emptytest_add_to_cartConfirms cart badge updates when item is addedtest_full_checkout_flowComplete user journey: login → add item → checkout → order confirmation


**Setup & Installation**

Clone the repository

bash   git clone https://github.com/yourusername/selenium-qa-portfolio.git
   cd selenium-qa-portfolio

Install dependencies

bash   pip install selenium pytest webdriver-manager



**Run tests**

bash   pytest test_saucedemo.py -v

**Test Results**

All tests pass with 100% success rate:
test_saucedemo.py::test_valid_login PASSED
test_saucedemo.py::test_invalid_login PASSED
test_saucedemo.py::test_empty_login PASSED
test_saucedemo.py::test_add_to_cart PASSED
test_saucedemo.py::test_full_checkout_flow PASSED
