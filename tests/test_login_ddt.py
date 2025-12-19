# File: tests/test_login_ddt.py
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
# Import the function from the file we just created
from utils.db_manager import get_test_users_from_db

def load_test_data():
    """
    Fetches data from PostgreSQL.
    If it fails (empty list), it stops the test immediately.
    """
    data = get_test_users_from_db()
    if not data:
        pytest.fail("STOPPING TEST: No data found or Database Connection Failed. Check utils/db_manager.py password.")
    return data

class TestLoginDDT:
    
    @pytest.mark.parametrize("user_data", load_test_data())
    def test_login_scenarios(self, driver, user_data):
        """
        Data-Driven Test: Loops through users fetched from PostgreSQL
        """
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        
        print(f"Testing login for: {user_data['username']}")
        
        # Perform Login
        login_page.login(user_data['username'], user_data['password'])
        
        # Check Success or Failure based on DB data
        if user_data['should_pass']:
            assert "Products" in inventory_page.get_page_title()
        else:
            actual_error = login_page.get_error_message()
            # If error_msg is NULL in DB, treat it as empty string
            expected_msg = user_data['error_msg'] if user_data['error_msg'] else ""
            assert expected_msg in actual_error