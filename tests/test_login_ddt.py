# File: tests/test_login_ddt.py
import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def load_test_data():
    with open('data/users.json') as f:
        return json.load(f)

class TestLoginDDT:
    
    @pytest.mark.parametrize("user_data", load_test_data())
    def test_login_scenarios(self, driver, user_data):
        """
        Data-Driven Test: Loops through users in JSON
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        print(f"Testing login for: {user_data['username']}")
        
        login_page.login(user_data['username'], user_data['password'])
        
        if user_data['should_pass']:
            assert "Products" in inventory_page.get_page_title()
        else:
            actual_error = login_page.get_error_message()
            assert user_data['error_msg'] in actual_error