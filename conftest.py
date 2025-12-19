# File: conftest.py
import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from config import Config

# Create screenshots directory
SCREENSHOT_DIR = "screenshots"
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)

@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes driver and attaches it to the test node for screenshot capability.
    """
    print(f"\n[SETUP] Setting up {Config.BROWSER} browser...")
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Uncomment the next line to run without seeing the browser (Headless mode)
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    
    # Attach driver to the request node so the hook can access it
    request.node.driver = driver
    
    yield driver
    
    print("\n[TEARDOWN] Closing browser...")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshot on failure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item, "driver", None)
        if driver:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)
            
            driver.save_screenshot(file_path)
            print(f"Screenshot saved to {file_path}")