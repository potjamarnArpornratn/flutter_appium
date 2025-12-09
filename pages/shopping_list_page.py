"""
Shopping List Page Object for Flutter App

This page object represents the shopping list feature where users can:
- Add items with name and quantity
- View all items in the list
- Delete items from the list
- Check if list is empty
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import logging

logger = logging.getLogger(__name__)


class ShoppingListPage(BasePage):
    """Page object for the Shopping List page"""
    
    # Element locators
    TITLE = "Shopping List"
    BACK_BUTTON = "Back"
    HEADER_TEXT = "Add items to your shopping list"
    NO_ITEMS_TEXT = "No items yet"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def verify_page_loaded(self, timeout=10):
        """Verify Shopping List page loaded successfully
        
        Verifies page load by checking for:
        1. Header text
        2. EditText input fields (2 expected)
        3. "No items yet" message (if no items)
        
        Args:
            timeout: Maximum time to wait for page load (seconds)
            
        Returns:
            bool: True if page loaded successfully, False otherwise
        """
        try:
            logger.debug("Verifying Shopping List page loaded")
            # Look for the header text
            try:
                element = self.find_element(
                    AppiumBy.ACCESSIBILITY_ID,
                    self.HEADER_TEXT,
                    timeout=timeout
                )
                logger.info("Shopping List page loaded - found header text")
                return True
            except:
                # Fallback: check for EditText elements (shopping list has input fields)
                edit_texts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
                if len(edit_texts) >= 2:
                    logger.info(f"Shopping List page loaded - found {len(edit_texts)} EditText elements")
                    return True
                # Also check for "No items yet" indicator
                try:
                    no_items = self.find_element(
                        AppiumBy.ACCESSIBILITY_ID,
                        self.NO_ITEMS_TEXT,
                        timeout=3
                    )
                    if no_items:
                        logger.info("Shopping List page loaded - found 'No items yet' message")
                        return True
                except:
                    pass
            
            logger.warning("Shopping List page indicators not found")
            return False
        except Exception as e:
            logger.error(f"Shopping List page did not load: {e}")
            return False
    
    def add_item(self, item_name, quantity=1):
        """Add an item to the shopping list with specified name and quantity
        
        Process:
        1. Click on item name field and enter name
        2. Click on quantity field and enter quantity
        3. Click Add button to add item to list
        
        Args:
            item_name: Name of the item to add
            quantity: Quantity of the item (default: 1)
            
        Returns:
            bool: True if item added successfully, False otherwise
        """
        try:
            logger.debug(f"Adding item: {item_name}, quantity: {quantity}")
            
            # Find the EditText fields (index 0 is item name, index 1 is quantity)
            edit_texts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            
            if len(edit_texts) < 2:
                logger.error("Shopping list input fields not found")
                return False
            
            # Step 1: Click on first EditText and enter item name
            item_field = edit_texts[0]
            item_field.click()
            logger.debug("Clicked on item name field")
            item_field.clear()
            item_field.send_keys(item_name)
            logger.debug(f"Entered item name: {item_name}")
            
            # Step 2: Click on second EditText and change quantity
            quantity_field = edit_texts[1]
            quantity_field.click()
            logger.debug("Clicked on quantity field")
            quantity_field.clear()
            quantity_field.send_keys(str(quantity))
            logger.debug(f"Entered quantity: {quantity}")
            
            # Step 3: Find and click the Add button (skip Back button)
            buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
            logger.debug(f"Found {len(buttons)} buttons total")
            
            add_clicked = False
            for i, btn in enumerate(buttons):
                try:
                    desc = btn.get_attribute('content-desc')
                    clickable = btn.get_attribute('clickable')
                    logger.debug(f"  Button[{i}]: desc='{desc}', clickable={clickable}")
                    # Skip the Back button - look for button that's NOT 'Back'
                    if desc != 'Back' and desc != self.BACK_BUTTON:
                        logger.info(f"Clicking Add button (button {i}: desc='{desc}')")
                        btn.click()
                        add_clicked = True
                        break
                except Exception as e:
                    logger.debug(f"  Error with button {i}: {e}")
                    continue
            
            if not add_clicked:
                logger.error("Could not find or click Add button")
                return False
            
            # Wait for item to be added
            import time
            time.sleep(2)
            logger.info(f"[PASS] Successfully added item: {item_name} (quantity: {quantity})")
            return True
        except Exception as e:
            logger.error(f"Error adding shopping item: {e}")
            return False
    
    def get_items(self):
        """Get all items from the shopping list
        
        Items are displayed as View elements with content-desc format: 'ItemName\\nx{quantity}'
        Example: 'Milk\\nx2' or 'Apple\\nx1' (where \\n is an actual newline character)
        
        Returns:
            list: List of item strings in format 'ItemName\\nx{quantity}', or empty list if no items
        """
        try:
            logger.debug("Retrieving shopping list items")
            
            # Look for item entries - items are View elements with specific content-desc pattern
            items = []
            excluded_descs = [
                self.TITLE,
                self.HEADER_TEXT, 
                self.NO_ITEMS_TEXT,
                self.BACK_BUTTON,
                "null",
                "",
                None
            ]
            
            all_views = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
            logger.debug(f"Total Views found: {len(all_views)}")
            
            for view in all_views:
                try:
                    desc = view.get_attribute('content-desc')
                    if desc:
                        logger.debug(f"  View desc: '{desc}'")
                    
                    # Item entries have format 'ItemName\nx{quantity}' where \n is actual newline
                    # Check if desc contains newline and 'x' pattern (not in excluded list)
                    if desc and desc not in excluded_descs:
                        # Filter out Total and Completed views
                        if 'Total:' not in desc and 'Completed:' not in desc:
                            # Check if it looks like an item (contains newline and x followed by number)
                            if '\n' in desc and 'x' in desc.lower():
                                items.append(desc)
                                logger.info(f"  ✓ FOUND ITEM: {repr(desc)}")
                except Exception as e:
                    logger.debug(f"  Error checking view: {e}")
                    continue
            
            logger.info(f"Found {len(items)} items in shopping list")
            if len(items) == 0:
                logger.warning("No items found - check if item format has changed")
            return items
        except Exception as e:
            logger.error(f"Error getting shopping list items: {e}")
            return []
    
    def is_empty(self):
        """Check if shopping list is empty by looking for 'No items yet' message
        
        Returns:
            bool: True if list is empty, False otherwise
        """
        try:
            no_items = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.NO_ITEMS_TEXT,
                timeout=3
            )
            return no_items is not None
        except:
            return False
    
    def delete_item(self, item_name):
        """Delete an item from the shopping list by clicking its delete button (garbage bin icon)
        
        Uses UIAutomator selector to find all buttons and calculate the correct delete button
        index based on the item's position in the list. This approach is platform-independent
        and doesn't rely on screen coordinates.
        
        Process:
        1. Get all items to find target item's index
        2. Find all buttons using UIAutomator selector
        3. Filter out Back button
        4. Calculate delete button index (target_index + 1, accounting for Add button)
        5. Click the delete button
        6. Verify deletion
        
        Args:
            item_name: Name of the item to delete
            
        Returns:
            bool: True if item deleted successfully, False otherwise
        """
        try:
            logger.debug(f"Attempting to delete item: {item_name}")
            
            # Get all items to find the index of the target item
            items = self.get_items()
            logger.debug(f"Current items in list: {items}")
            
            if not items:
                logger.warning(f"No items found in shopping list")
                return False
            
            # Find the index of our target item
            target_item_index = -1
            for idx, item_desc in enumerate(items):
                if item_name in item_desc:
                    target_item_index = idx
                    logger.debug(f"Target item '{item_name}' is at position {idx} in the list")
                    break
            
            if target_item_index == -1:
                logger.warning(f"Item '{item_name}' not found in shopping list")
                return False
            
            # Use UIAutomator selector to find all buttons
            try:
                all_buttons = self.driver.find_elements(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().className("android.widget.Button")'
                )
                
                logger.debug(f"Found {len(all_buttons)} buttons via UIAutomator")
                
                # Filter out the Back button to get Add and delete buttons
                delete_buttons = []
                for btn in all_buttons:
                    desc = btn.get_attribute('content-desc')
                    if desc != 'Back' and desc != self.BACK_BUTTON:
                        delete_buttons.append(btn)
                        logger.debug(f"  Delete button candidate: desc='{desc}'")
                
                logger.debug(f"Found {len(delete_buttons)} button candidates (includes Add button)")
                
                # Button order: [Add button at index 0, Delete buttons for items at index 1+]
                # Delete button index = target_item_index + 1 (accounting for Add button)
                delete_button_index = target_item_index + 1
                
                if delete_button_index < len(delete_buttons):
                    delete_btn = delete_buttons[delete_button_index]
                    logger.info(f"Clicking delete button at index {delete_button_index} for item '{item_name}'")
                    delete_btn.click()
                    
                    import time
                    time.sleep(1)
                    
                    # Verify deletion
                    items_after = self.get_items()
                    if item_name not in str(items_after):
                        logger.info(f"[PASS] Successfully deleted item: {item_name}")
                        return True
                    else:
                        logger.warning(f"Item {item_name} still present after delete attempt")
                        return False
                else:
                    logger.error(f"Delete button index {delete_button_index} out of range (total: {len(delete_buttons)})")
                    return False
                    
            except Exception as selector_error:
                logger.error(f"UIAutomator selector approach failed: {selector_error}")
                return False
                
        except Exception as e:
            logger.error(f"Error deleting item: {e}", exc_info=True)
            return False
    
    def get_item_count(self):
        """Get the number of items currently in the shopping list
        
        Returns:
            int: Number of items in the list
        """
        items = self.get_items()
        return len(items)
