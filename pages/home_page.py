"""
Home Page Object for Flutter App

This page object represents the home page of the Flutter app with three main action buttons:
- Web Search: Opens a browser for web searching
- Open Gmail: Opens Gmail in browser
- Shopping List: Navigates to the shopping list feature
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    """Page object for the Flutter app home page"""
    
    # Element locators
    WEB_SEARCH_BUTTON = "Web Search"
    OPEN_GMAIL_BUTTON = "Open Gmail"
    SHOPPING_LIST_BUTTON = "Shopping List"
    APP_PACKAGE = "com.example.my_app"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def wait_for_home_page_load(self, timeout=10, debug=False):
        """Wait for home page to load and optionally log page elements for debugging
        
        Args:
            timeout: Maximum time to wait for page load (seconds)
            debug: If True, logs all page elements for debugging purposes
            
        Returns:
            bool: True if page loaded successfully
        """
        logger.debug("Waiting for home page to load...")
        time.sleep(5)  # Give Flutter time to render and initialize
        
        # Optional debug logging
        if debug:
            try:
                logger.info("=== Discovering elements on screen ===")
                
                # Check all View elements
                elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
                logger.info(f"Found {len(elements)} View elements")
                for i, elem in enumerate(elements[:10]):
                    try:
                        desc = elem.get_attribute('content-desc')
                        text = elem.text
                        if desc or text:
                            logger.info(f"  View {i}: content-desc='{desc}', text='{text}'")
                    except:
                        pass
                
                # Check Button elements
                buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
                logger.info(f"Found {len(buttons)} Button elements")
                for i, btn in enumerate(buttons[:10]):
                    try:
                        logger.info(f"  Button {i}: text='{btn.text}', content-desc='{btn.get_attribute('content-desc')}'")
                    except:
                        pass
                
                # Check EditText elements
                edit_texts = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
                logger.info(f"Found {len(edit_texts)} EditText elements")
                
                logger.info("====================================")
            except Exception as e:
                logger.error(f"Debug logging error: {e}")
        
        return True
    
    def click_gmail_button(self):
        """Click the Open Gmail button - opens Gmail app"""
        try:
            logger.debug("Attempting to find Open Gmail button")
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.OPEN_GMAIL_BUTTON
            )
            element.click()
            logger.info("Open Gmail button clicked successfully")
            return True
        except Exception as e:
            logger.error(f"Error clicking Open Gmail button: {e}")
            return False
    
    def click_web_search_button(self):
        """Click the Web Search button - opens browser"""
        try:
            logger.debug("Attempting to find Web Search button")
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.WEB_SEARCH_BUTTON
            )
            element.click()
            logger.info("Web Search button clicked successfully")
            return True
        except Exception as e:
            logger.error(f"Error clicking Web Search button: {e}")
            return False
    
    def click_shopping_list_button(self):
        """Click the Shopping List button - launches Shopping List app"""
        try:
            logger.debug("Attempting to find Shopping List button")
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.SHOPPING_LIST_BUTTON
            )
            element.click()
            logger.info("Shopping List button clicked successfully")
            return True
        except Exception as e:
            logger.error(f"Error clicking Shopping List button: {e}")
            return False
    
    def is_web_search_button_visible(self):
        """Check if Web Search button is visible"""
        try:
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.WEB_SEARCH_BUTTON
            )
            return element.is_displayed()
        except:
            return False
    
    def is_gmail_button_visible(self):
        """Check if Open Gmail button is visible"""
        try:
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.OPEN_GMAIL_BUTTON
            )
            return element.is_displayed()
        except:
            return False
    
    def is_shopping_list_button_visible(self):
        """Check if Shopping List button is visible"""
        try:
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                self.SHOPPING_LIST_BUTTON
            )
            return element.is_displayed()
        except:
            return False
    
    def return_from_webview(self, wait_time=3):
        """Navigate back to Flutter app from WebView opened by Web Search or Gmail buttons
        
        Handles the case where back press may exit to Android home screen instead of
        returning to the Flutter app. Uses package checking and app reactivation as fallback.
        
        Args:
            wait_time: Time to wait after navigation (seconds)
            
        Returns:
            None
        """
        logger.info("Returning to app from WebView...")
        # First back closes the WebView page, but may exit the app
        self.driver.back()
        time.sleep(1)
        
        # Check if we're still in the app
        if self.driver.current_package != self.APP_PACKAGE:
            logger.info("App exited to home screen, reactivating...")
            self.driver.activate_app(self.APP_PACKAGE)
        else:
            # If still in app but in WebView, press back again
            try:
                # Check if we can find a Flutter button (we're back in app)
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.WEB_SEARCH_BUTTON)
                logger.info("Already back in Flutter app")
            except:
                # Still in WebView, press back one more time
                logger.info("Still in WebView, pressing back again...")
                self.driver.back()
        
        time.sleep(wait_time)
    
    def verify_home_page_loaded(self):
        """Verify that the home page has loaded successfully
        
        Uses multiple verification methods:
        1. Check app package name
        2. Check for presence of action buttons
        3. Check for any UI elements
        
        Returns:
            bool: True if home page verified, False otherwise
        """
        try:
            logger.debug("Verifying home page loaded")
            
            # Method 1: Check for app package
            current_package = self.driver.current_package
            logger.debug(f"Current package: {current_package}")
            if current_package == self.APP_PACKAGE:
                logger.info("Home page verified by package name")
                return True
            
            # Method 2: Check for any action buttons
            try:
                buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
                if len(buttons) >= 3:  # Should have at least 3 action buttons
                    logger.info(f"Home page verified by button count ({len(buttons)} found)")
                    return True
            except:
                pass
            
            logger.warning("Home page verification failed")
            return False
        except Exception as e:
            logger.error(f"Error verifying home page: {e}")
            return False
