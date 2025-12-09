"""
Test Suite for Home Page Functionality
Tests for all buttons on the home page: Web Search, Open Gmail, Shopping List
"""
import pytest
import time
import logging
from pages.home_page import HomePage
from pages.shopping_list_page import ShoppingListPage

# Configure logger for this test module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestHomePage:
    """Test cases for home page button functionality"""
    
    @pytest.mark.smoke
    def test_all_buttons_visible(self, driver):
        """Test that all buttons are visible on home page"""
        logger.info("Starting test: test_all_buttons_visible")
        
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        
        # Verify all buttons are visible
        assert home_page.is_web_search_button_visible(), "Web Search button not visible"
        logger.info("[PASS] Web Search button is visible")
        
        assert home_page.is_gmail_button_visible(), "Open Gmail button not visible"
        logger.info("[PASS] Open Gmail button is visible")
        
        assert home_page.is_shopping_list_button_visible(), "Shopping List button not visible"
        logger.info("[PASS] Shopping List button is visible")
        
        logger.info("Test completed: test_all_buttons_visible")
    
    @pytest.mark.smoke
    def test_web_search_button_opens_browser(self, driver):
        """Test clicking Web Search button opens browser"""
        logger.info("Starting test: test_web_search_button_opens_browser")
        
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        
        # Click Web Search button
        assert home_page.click_web_search_button(), "Failed to click Web Search button"
        logger.info("[PASS] Web Search button clicked successfully")
        
        # Verify browser opened
        time.sleep(3)
        current_package = driver.current_package
        assert current_package != "com.example.my_app", "Browser did not open"
        logger.info(f"[PASS] Browser opened with package: {current_package}")
        
        home_page.return_from_webview(wait_time=2)
        logger.info("Test completed: test_web_search_button_opens_browser")
    
    @pytest.mark.smoke
    def test_open_gmail_button(self, driver):
        """Test clicking Open Gmail button launches Gmail app"""
        logger.info("Starting test: test_open_gmail_button")
        
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        
        # Click Open Gmail button
        assert home_page.click_gmail_button(), "Failed to click Open Gmail button"
        logger.info("[PASS] Open Gmail button clicked successfully")
        
        # Verify Gmail opened (com.google.android.gm or browser)
        time.sleep(3)
        current_package = driver.current_package
        assert current_package != "com.example.my_app", "Gmail did not open"
        logger.info(f"[PASS] Gmail opened with package: {current_package}")
        
        home_page.return_from_webview(wait_time=2)
        logger.info("Test completed: test_open_gmail_button")
    
    @pytest.mark.smoke
    def test_shopping_list_button_navigation(self, driver):
        """Test clicking Shopping List button navigates to Shopping List page"""
        logger.info("Starting test: test_shopping_list_button_navigation")
        
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        
        # Click Shopping List button
        assert home_page.click_shopping_list_button(), "Failed to click Shopping List button"
        logger.info("[PASS] Shopping List button clicked successfully")
        
        # Verify Shopping List page loaded
        time.sleep(2)
        shopping_list_page = ShoppingListPage(driver)
        assert shopping_list_page.verify_page_loaded(), "Shopping List page did not load"
        logger.info("[PASS] Shopping List page loaded successfully")
        
        # Navigate back to home page
        driver.back()
        time.sleep(2)
        logger.info("Test completed: test_shopping_list_button_navigation")
    
    @pytest.mark.regression
    def test_all_buttons_clickable(self, driver):
        """Test all buttons are clickable in sequence without errors"""
        logger.info("Starting test: test_all_buttons_clickable")
        
        home_page = HomePage(driver)
        home_page.wait_for_home_page_load()
        
        # Test each button
        buttons = [
            (home_page.click_web_search_button, "Web Search"),
            (home_page.click_gmail_button, "Open Gmail"),
            (home_page.click_shopping_list_button, "Shopping List")
        ]
        
        for click_method, button_name in buttons:
            assert click_method(), f"{button_name} button not clickable"
            logger.info(f"[PASS] {button_name} button is clickable")
            
            # Return to app with appropriate navigation method
            if button_name in ["Web Search", "Open Gmail"]:
                home_page.return_from_webview(wait_time=5)
                # Wait for home page to fully reload after external app
                home_page.wait_for_home_page_load()
            else:
                # Shopping List is in-app, use driver.back()
                driver.back()
                time.sleep(3)
        
        logger.info("Test completed: test_all_buttons_clickable")
