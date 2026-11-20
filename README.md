# selenium-qa-portfolio

Automated end-to-end test suite for [SauceDemo](https://www.saucedemo.com) built with Python, Selenium, and pytest.

## Tech Stack

- Python 3
- Selenium WebDriver (browser automation)
- pytest (test framework)
- webdriver-manager (ChromeDriver management)

## Test Coverage

| Test | Description |
|------|-------------|
| `test_valid_login` | Successful login redirects to the inventory page |
| `test_false_login` | Error message shown for a wrong username and password |
| `test_empty_login` | Error message shown when login fields are empty |
| `test_add_to_cart` | Cart badge updates when an item is added |
| `test_full_checkout_flow` | Login, add item, checkout, order confirmation |
| `test_remove_item_from_cart` | Cart badge disappears after removing the item |

## Setup

```bash
git clone https://github.com/prymakyrylo/selenium-qa-portfolio.git
cd selenium-qa-portfolio
pip install selenium pytest webdriver-manager
```

## Run tests

```bash
pytest test_saucedemo.py -v
```
