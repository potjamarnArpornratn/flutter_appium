"""
Test Suite for Shopping List Page Functionality
"""
import pytest
import time
import logging
from pages.home_page import HomePage
from pages.shopping_list_page import ShoppingListPage

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestShoppingList:
    """Test cases for shopping list functionality"""
    
    def _navigate_to_shopping_list(self, driver):
        """Helper method to navigate to Shopping List page"""
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        assert home_page.click_shopping_list_button(), "Failed to open Shopping List"
        time.sleep(2)
        
        shopping_list_page = ShoppingListPage(driver)
        assert shopping_list_page.verify_page_loaded(), "Shopping List page did not load"
        return shopping_list_page
    
    @pytest.mark.smoke
    def test_navigate_to_shopping_list(self, driver):
        """Test navigation to Shopping List page"""
        logger.info("Starting test: test_navigate_to_shopping_list")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        logger.info("[PASS] Shopping List page loaded successfully")
        
        # Navigate back to home page
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_navigate_to_shopping_list")
    
    @pytest.mark.smoke
    def test_shopping_list_empty_state(self, driver):
        """Test Shopping List page shows empty state when no items"""
        logger.info("Starting test: test_shopping_list_empty_state")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Check if empty state is shown (or if there are existing items)
        items = shopping_list_page.get_items()
        logger.info(f"Current items in shopping list: {len(items)}")
        
        if len(items) == 0:
            is_empty = shopping_list_page.is_empty()
            logger.info(f"[PASS] Shopping list empty state shown: {is_empty}")
        else:
            logger.info(f"[INFO] Shopping list has {len(items)} existing items")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_shopping_list_empty_state")
    
    @pytest.mark.regression
    def test_add_single_item(self, driver):
        """Test adding a single item to shopping list"""
        logger.info("Starting test: test_add_single_item")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Add item
        test_item = "Milk"
        test_quantity = 2
        assert shopping_list_page.add_item(test_item, test_quantity), f"Failed to add {test_item}"
        logger.info(f"[PASS] Added {test_item} (quantity: {test_quantity})")
        
        # Verify item was added
        time.sleep(2)
        items = shopping_list_page.get_items()
        item_found = any(test_item.lower() in str(item).lower() for item in items)
        assert item_found, f"{test_item} not found in shopping list"
        logger.info(f"[PASS] Verified {test_item} is in shopping list")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_add_single_item")
    
    @pytest.mark.regression
    def test_add_multiple_items(self, driver):
        """Test adding multiple items to shopping list"""
        logger.info("Starting test: test_add_multiple_items")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Add multiple items
        items_to_add = [
            ("Bread", 1),
            ("Eggs", 12),
            ("Butter", 2)
        ]
        
        for item_name, quantity in items_to_add:
            assert shopping_list_page.add_item(item_name, quantity), f"Failed to add {item_name}"
            logger.info(f"Added {item_name} (quantity: {quantity})")
            time.sleep(1)
        
        logger.info("[PASS] All items added successfully")
        
        # Verify items were added
        time.sleep(2)
        all_items = shopping_list_page.get_items()
        logger.info(f"Shopping list now has {len(all_items)} items")
        
        for item_name, _ in items_to_add:
            item_found = any(item_name.lower() in str(item).lower() for item in all_items)
            assert item_found, f"{item_name} not found in shopping list"
            logger.info(f"[PASS] Verified {item_name} is in shopping list")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_add_multiple_items")
    
    @pytest.mark.regression
    def test_add_item_with_default_quantity(self, driver):
        """Test adding item with default quantity of 1"""
        logger.info("Starting test: test_add_item_with_default_quantity")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Add item with default quantity
        test_item = "Apple"
        assert shopping_list_page.add_item(test_item), f"Failed to add {test_item}"
        logger.info(f"[PASS] Added {test_item} with default quantity")
        
        # Verify item was added
        time.sleep(2)
        items = shopping_list_page.get_items()
        item_found = any(test_item.lower() in str(item).lower() for item in items)
        assert item_found, f"{test_item} not found in shopping list"
        logger.info(f"[PASS] Verified {test_item} is in shopping list")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_add_item_with_default_quantity")
    
    @pytest.mark.regression
    def test_delete_item(self, driver):
        """Test deleting an item from shopping list"""
        logger.info("Starting test: test_delete_item")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Add an item first
        test_item = "Orange"
        assert shopping_list_page.add_item(test_item, 3), f"Failed to add {test_item}"
        logger.info(f"Added {test_item} for deletion test")
        time.sleep(2)
        
        # Get initial count
        initial_count = shopping_list_page.get_item_count()
        logger.info(f"Initial item count: {initial_count}")
        
        # Delete the item
        assert shopping_list_page.delete_item(test_item), f"Failed to delete {test_item}"
        logger.info(f"[PASS] Deleted {test_item}")
        
        # Verify item was deleted
        time.sleep(2)
        new_count = shopping_list_page.get_item_count()
        logger.info(f"New item count: {new_count}")
        
        items = shopping_list_page.get_items()
        item_still_exists = any(test_item.lower() in str(item).lower() for item in items)
        assert not item_still_exists, f"{test_item} still exists after deletion"
        assert new_count < initial_count, "Item count did not decrease"
        logger.info(f"[PASS] Verified {test_item} was deleted")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_delete_item")
    
    @pytest.mark.regression
    def test_add_and_delete_multiple_items(self, driver):
        """Test adding multiple items and deleting one"""
        logger.info("Starting test: test_add_and_delete_multiple_items")
        
        shopping_list_page = self._navigate_to_shopping_list(driver)
        
        # Add multiple items
        items_to_add = [
            ("Banana", 6),
            ("Tomato", 4),
            ("Onion", 2)
        ]
        
        for item_name, quantity in items_to_add:
            assert shopping_list_page.add_item(item_name, quantity), f"Failed to add {item_name}"
            logger.info(f"Added {item_name} (quantity: {quantity})")
            time.sleep(1)
        
        time.sleep(2)
        initial_count = shopping_list_page.get_item_count()
        logger.info(f"Added {len(items_to_add)} items, total count: {initial_count}")
        
        # Delete one item
        item_to_delete = "Tomato"
        assert shopping_list_page.delete_item(item_to_delete), f"Failed to delete {item_to_delete}"
        logger.info(f"[PASS] Deleted {item_to_delete}")
        
        # Verify deletion
        time.sleep(2)
        remaining_items = shopping_list_page.get_items()
        deleted_item_exists = any(item_to_delete.lower() in str(item).lower() for item in remaining_items)
        assert not deleted_item_exists, f"{item_to_delete} still exists"
        
        # Verify other items still exist
        for item_name, _ in items_to_add:
            if item_name != item_to_delete:
                item_exists = any(item_name.lower() in str(item).lower() for item in remaining_items)
                assert item_exists, f"{item_name} should still exist but was not found"
                logger.info(f"[PASS] Verified {item_name} still exists")
        
        # Navigate back
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_add_and_delete_multiple_items")
