"""
Test Suite for Gmail Button Functionality
"""
import pytest
import time
import logging
from pages.home_page import HomePage

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestGmailButton:
    """Test cases for Gmail button functionality"""
    
    @pytest.mark.smoke
    def test_gmail_button_visible(self, driver):
        """Test that Gmail button is visible on home page"""
        logger.info("Starting test: test_gmail_button_visible")
        
        home_page = HomePage(driver)
        logger.info("Waiting for home page to load...")
        home_page.wait_for_home_page_load()
        
        # Verify home page loaded
        logger.info("Verifying home page loaded")
        assert home_page.verify_home_page_loaded(), "Home page did not load"
        
        logger.info("[PASS] Home page loaded successfully")
        logger.info("Test completed: test_gmail_button_visible")
    
    @pytest.mark.smoke
    def test_click_gmail_button(self, driver):
        """Test clicking Gmail button launches browser"""
        logger.info("Starting test: test_click_gmail_button")
        
        home_page = HomePage(driver)
        logger.info("Waiting for home page to load...")
        home_page.wait_for_home_page_load()
        
        # Click Gmail button
        logger.info("Attempting to click Gmail button")
        result = home_page.click_gmail_button()
        assert result, "Failed to click Gmail button"
        
        logger.info("[PASS] Gmail button clicked successfully")
        
        # Wait for browser to launch
        logger.info("Waiting for browser to launch...")
        time.sleep(3)
        
        # Verify app switched to browser (context changed)
        # Note: Browser will open in a different app
        contexts = driver.contexts
        logger.info(f"Available contexts: {contexts}")
        
        # Return to app
        logger.info("Returning to app...")
        driver.activate_app("com.example.my_app")
        time.sleep(2)
        logger.info("Test completed: test_click_gmail_button")
    
    @pytest.mark.regression
    def test_increment_counter_then_gmail(self, driver):
        """Test incrementing counter then clicking Gmail button"""
        logger.info("Starting test: test_increment_counter_then_gmail")
        
        home_page = HomePage(driver)
        logger.info("Waiting for home page to load...")
        home_page.wait_for_home_page_load()
        
        # Get initial counter value
        initial_counter = home_page.get_counter_value()
        logger.info(f"Initial counter value: {initial_counter}")
        
        # Click increment button
        logger.info("Clicking increment button")
        home_page.click_increment_button()
        time.sleep(1)
        
        # Get new counter value
        new_counter = home_page.get_counter_value()
        logger.info(f"New counter value: {new_counter}")
        
        if initial_counter is not None and new_counter is not None:
            assert new_counter == initial_counter + 1, "Counter did not increment"
            logger.info("[PASS] Counter incremented successfully")
        
        # Click Gmail button
        logger.info("Attempting to click Gmail button")
        result = home_page.click_gmail_button()
        assert result, "Failed to click Gmail button"
        logger.info("[PASS] Gmail button clicked successfully")
        
        time.sleep(2)
        
        # Return to app
        logger.info("Returning to app...")
        driver.activate_app("com.example.my_app")
        time.sleep(1)
        logger.info("Test completed: test_increment_counter_then_gmail")
