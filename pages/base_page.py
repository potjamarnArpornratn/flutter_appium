"""
Base Page Object for common methods
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def find_element(self, by, value):
        """Find element with explicit wait"""
        return self.wait.until(
            EC.presence_of_element_located((by, value))
        )
    
    def find_element_by_key(self, key):
        """Find element by Flutter key"""
        # For Flutter apps, we need to use content-desc or resource-id
        # Flutter keys are exposed as accessibility IDs
        try:
            return self.find_element(
                AppiumBy.ACCESSIBILITY_ID, 
                key
            )
        except:
            # Fallback to searching by text
            return None
    
    def click_element(self, by, value):
        """Click element with explicit wait"""
        element = self.find_element(by, value)
        element.click()
        return element
    
    def get_text(self, by, value):
        """Get text from element"""
        element = self.find_element(by, value)
        return element.text
    
    def wait_for_element_visible(self, by, value, timeout=None):
        """Wait for element to be visible"""
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait
        return wait.until(EC.visibility_of_element_located((by, value)))
    
    def is_element_present(self, by, value, timeout=5):
        """Check if element is present"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except:
            return False
