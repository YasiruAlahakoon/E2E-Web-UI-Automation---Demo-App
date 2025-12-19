# File: pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def _highlight_element(self, element):
        """Highlights an element in red (Advanced UI debugging)"""
        self.driver.execute_script("arguments[0].setAttribute('style', 'border: 2px solid red;');", element)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        try:
            element = self.wait_for_element(locator)
            self._highlight_element(element) # Visual debugging
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {e}")
            raise

    def set_text(self, locator, text):
        try:
            element = self.wait_for_element(locator)
            self._highlight_element(element)
            element.clear()
            element.send_keys(text)
            # Mask password in logs for security
            log_text = "*****" if "password" in str(locator).lower() else text
            self.logger.info(f"Entered text '{log_text}' into {locator}")
        except Exception as e:
            self.logger.error(f"Failed to enter text: {e}")
            raise

    def get_text(self, locator):
        element = self.wait_for_element(locator)
        text = element.text
        self.logger.info(f"Retrieved text '{text}' from {locator}")
        return text

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )