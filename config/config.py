"""
Appium Configuration for Flutter App Testing

This module contains all configuration settings for Appium test execution including:
- Appium server settings
- Device capabilities
- App details
- Timeout values
"""
import os


class Config:
    """Configuration class for Appium test framework"""
    
    # Appium Server
    APPIUM_SERVER = "http://localhost:4723"
    
    # Flutter App Details
    APP_PACKAGE = "com.example.my_app"
    APP_ACTIVITY = ".MainActivity"
    
    # APK Path - auto-resolved from project structure
    APK_PATH = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "flutter", "my_app", "build", "app", "outputs", "flutter-apk", "app-debug.apk"
    )
    
    # Device Configuration
    PLATFORM_NAME = "Android"
    PLATFORM_VERSION = "16"  # Android API level
    DEVICE_NAME = "emulator-5554"
    AUTOMATION_NAME = "UiAutomator2"
    
    # Test Configuration
    NO_RESET = False  # Don't reset app state between sessions
    FULL_RESET = False  # Don't uninstall app between sessions
    
    # Timeouts (in seconds)
    IMPLICIT_WAIT = 10  # Default wait for element finding
    EXPLICIT_WAIT = 20  # Maximum wait for explicit waits
    
    @staticmethod
    def get_desired_capabilities():
        """Returns desired capabilities for Appium session
        
        Returns:
            dict: Appium capabilities dictionary
        """
        return {
            'platformName': Config.PLATFORM_NAME,
            'platformVersion': Config.PLATFORM_VERSION,
            'deviceName': Config.DEVICE_NAME,
            'app': Config.APK_PATH,
            'appPackage': Config.APP_PACKAGE,
            'appActivity': Config.APP_ACTIVITY,
            'automationName': Config.AUTOMATION_NAME,
            'noReset': Config.NO_RESET,
            'fullReset': Config.FULL_RESET,
            'newCommandTimeout': 300,
            'autoGrantPermissions': True,
        }
