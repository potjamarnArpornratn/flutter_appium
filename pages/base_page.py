"""
Base Page Object for common methods

This module provides the base page class that all page objects inherit from.
Contains common methods for element interaction, waiting, and utilities.
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config


class BasePage:
    """Base class for all page objects providing common functionality"""
    
    def __init__(self, driver):
        """Initialize BasePage with driver and wait
        
        Args:
            driver: Appium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
    
    def find_element(self, by, value, timeout=None):
        """Find element with explicit wait
        
        Args:
            by: Locator strategy (e.g., AppiumBy.ACCESSIBILITY_ID)
            value: Locator value
            timeout: Optional custom timeout (uses config default if not specified)
            
        Returns:
            WebElement: Found element
        """
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_element_by_key(self, key):
        """Find element by Flutter key (exposed as accessibility ID)
        
        Args:
            key: Flutter key value
            
        Returns:
            WebElement: Found element, or None if not found
        """
        try:
            return self.find_element(AppiumBy.ACCESSIBILITY_ID, key)
        except:
            return None
    
    def click_element(self, by, value):
        """Click element with explicit wait
        
        Args:
            by: Locator strategy
            value: Locator value
            
        Returns:
            WebElement: Clicked element
        """
        element = self.find_element(by, value)
        element.click()
        return element
    
    def get_text(self, by, value):
        """Get text from element
        
        Args:
            by: Locator strategy
            value: Locator value
            
        Returns:
            str: Element text
        """
        element = self.find_element(by, value)
        return element.text
    
    def wait_for_element_visible(self, by, value, timeout=None):
        """Wait for element to be visible
        
        Args:
            by: Locator strategy
            value: Locator value
            timeout: Optional custom timeout
            
        Returns:
            WebElement: Visible element
        """
        if timeout:
            wait = WebDriverWait(self.driver, timeout)
        else:
            wait = self.wait
        return wait.until(EC.visibility_of_element_located((by, value)))
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
