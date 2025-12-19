# File: pages/inventory_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)