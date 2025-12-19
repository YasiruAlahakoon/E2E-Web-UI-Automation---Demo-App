# File: pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_first_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)