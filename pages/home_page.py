"""
Home Page Object for Flutter App
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time
import logging

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    # Element locators
    GMAIL_BUTTON_KEY = "gmailButton"
    INCREMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Increment")
    COUNTER_TEXT = "You have pushed the button this many times:"
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def wait_for_home_page_load(self, timeout=10):
        """Wait for home page to load"""
        logger.debug("Waiting for home page to load...")
        time.sleep(5)  # Give Flutter time to render and initialize
        
        # Log all elements for debugging
        try:
            logger.debug("=== Elements on screen ===")
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
            logger.debug(f"Found {len(elements)} View elements")
            
            text_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            logger.debug(f"Found {len(text_elements)} TextView elements")
            for elem in text_elements[:5]:  # Log first 5
                try:
                    logger.debug(f"  Text: {elem.text}")
                except:
                    pass
            
            buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
            logger.debug(f"Found {len(buttons)} Button elements")
            for btn in buttons[:5]:  # Log first 5
                try:
                    logger.debug(f"  Button text: {btn.text}, content-desc: {btn.get_attribute('content-desc')}")
                except:
                    pass
            logger.debug("========================")
        except Exception as e:
            logger.error(f"Debug error: {e}")
        
        return True
    
    def click_gmail_button(self):
        """Click the Open Gmail button"""
        # Try to find by content-desc (accessibility ID)
        try:
            logger.debug("Attempting to find Gmail button by accessibility ID")
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Open Gmail"
            )
            element.click()
            logger.info("Gmail button clicked successfully")
            return True
        except Exception as e:
            logger.warning(f"Error finding Gmail button by accessibility ID: {e}")
            # Fallback: Try UiAutomator with description
            try:
                logger.debug("Trying fallback method with UiAutomator")
                element = self.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().description("Open Gmail")'
                )
                element.click()
                logger.info("Gmail button clicked successfully (fallback method)")
                return True
            except Exception as e2:
                logger.error(f"Fallback also failed: {e2}")
                return False
    
    def click_increment_button(self):
        """Click the increment (+) button"""
        try:
            logger.debug("Attempting to find increment button by accessibility ID")
            # Use accessibility ID directly
            element = self.find_element(
                AppiumBy.ACCESSIBILITY_ID,
                "Increment"
            )
            element.click()
            logger.info("Increment button clicked successfully")
            return True
        except Exception as e:
            logger.warning(f"Error finding increment button by accessibility ID: {e}")
            # Fallback: Try to find FAB by description
            try:
                logger.debug("Trying fallback method with UiAutomator")
                element = self.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().descriptionContains("Increment")'
                )
                element.click()
                logger.info("Increment button clicked successfully (fallback method)")
                return True
            except Exception as e2:
                logger.error(f"Fallback also failed: {e2}")
                return False
    
    def get_counter_value(self):
        """Get the current counter value"""
        try:
            logger.debug("Attempting to get counter value")
            # For Flutter, counter might be in View elements with semantic labels
            # Try to find by semantics label or content-desc
            all_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.view.View")
            
            for element in all_elements:
                try:
                    # Check content-desc for counter value
                    desc = element.get_attribute('content-desc')
                    if desc and desc.isdigit():
                        logger.debug(f"Found counter value in content-desc: {desc}")
                        return int(desc)
                    # Also check text attribute
                    text = element.text
                    if text and text.isdigit():
                        logger.debug(f"Found counter value in text: {text}")
                        return int(text)
                except:
                    continue
            
            # Fallback: check TextView if any exist
            text_elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            for element in text_elements:
                text = element.text
                if text and text.isdigit():
                    logger.debug(f"Found counter value in TextView: {text}")
                    return int(text)
            
            logger.warning("Counter value not found")
            return None
        except Exception as e:
            logger.error(f"Error getting counter value: {e}")
            return None
    
    def verify_home_page_loaded(self):
        """Verify home page is loaded"""
        try:
            logger.debug("Verifying home page loaded")
            # Try multiple ways to verify page loaded
            
            # Method 1: Check for app package
            current_package = self.driver.current_package
            logger.debug(f"Current package: {current_package}")
            if current_package == "com.example.my_app":
                logger.info("Home page verified by package name")
                return True
            
            # Method 2: Check if counter text is present
            try:
                element = self.find_element(
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    f'new UiSelector().textContains("{self.COUNTER_TEXT}")'
                )
                if element:
                    logger.info("Home page verified by counter text")
                    return True
            except:
                pass
            
            # Method 3: Check for any text elements (Flutter app is loaded)
            elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            if len(elements) > 0:
                logger.info(f"Home page verified by TextView elements ({len(elements)} found)")
                return True
            
            logger.warning("Home page verification failed")
            return False
        except Exception as e:
            logger.error(f"Error verifying home page: {e}")
            return False
    
    def log_page_source(self):
        """Debug method to log page source"""
        logger.debug("=== Page Source ===")
        logger.debug(self.driver.page_source)
        logger.debug("===================")
