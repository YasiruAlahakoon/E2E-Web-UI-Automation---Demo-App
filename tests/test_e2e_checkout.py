# File: tests/test_e2e_checkout.py
import pytest
from config import Config
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestE2ECheckout:
    
    def test_buy_backpack_success(self, driver):
        """
        Test Case: Login -> Add Backpack -> Verify in Cart
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        # 1. Login
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # 2. Add to Cart
        inventory_page.add_backpack_to_cart()

        # 3. Go to Cart
        inventory_page.go_to_cart()

        # 4. Verify
        item_name = cart_page.get_first_item_name()
        
        assert "Sauce Labs Backpack" == item_name