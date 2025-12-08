"""
Appium Configuration for Flutter App Testing
"""
import os

class Config:
    # Appium Server
    APPIUM_SERVER = "http://localhost:4723"
    
    # Flutter App Details
    APP_PACKAGE = "com.example.my_app"
    APP_ACTIVITY = ".MainActivity"
    
    # APK Path
    APK_PATH = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "flutter", "my_app", "build", "app", "outputs", "flutter-apk", "app-debug.apk"
    )
    
    # Device Configuration
    PLATFORM_NAME = "Android"
    PLATFORM_VERSION = "16"  # Adjust based on your emulator
    DEVICE_NAME = "emulator-5554"
    AUTOMATION_NAME = "UiAutomator2"
    
    # Test Configuration
    NO_RESET = False
    FULL_RESET = False
    
    # Timeouts
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    
    @staticmethod
    def get_desired_capabilities():
        """Returns desired capabilities for Appium"""
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
