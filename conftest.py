"""
Pytest configuration and fixtures
"""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import Config
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(
            f'logs/test_run_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Create and tear down Appium driver"""
    # Initialize driver
    logger.info("[Setup] Starting Appium driver...")
    logger.info(f"Connecting to Appium server: {Config.APPIUM_SERVER}")
    logger.info(f"Device: {Config.DEVICE_NAME}, Platform: {Config.PLATFORM_NAME} {Config.PLATFORM_VERSION}")
    
    appium_driver = webdriver.Remote(
        Config.APPIUM_SERVER,
        options=UiAutomator2Options().load_capabilities(
            Config.get_desired_capabilities()
        )
    )
    
    logger.info("Appium driver started successfully")
    
    # Set implicit wait
    appium_driver.implicitly_wait(Config.IMPLICIT_WAIT)
    logger.info(f"Implicit wait set to {Config.IMPLICIT_WAIT} seconds")
    
    # Wait for app to start
    logger.info("Waiting for app to initialize...")
    time.sleep(5)
    logger.info("App initialized")
    
    yield appium_driver
    
    # Teardown
    logger.info("[Teardown] Closing Appium driver...")
    appium_driver.quit()
    logger.info("Appium driver closed")


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    """Session-level setup"""
    logger.info("="*50)
    logger.info("Starting Test Session")
    logger.info(f"Session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*50)
    yield
    logger.info("="*50)
    logger.info("Test Session Completed")
    logger.info(f"Session ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*50)


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
