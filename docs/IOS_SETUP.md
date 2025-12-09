# iOS Testing Setup Guide

## Prerequisites

- **macOS** (Monterey or later recommended)
- **Xcode** 13+ installed from App Store
- **Xcode Command Line Tools**
- **Node.js and npm**
- **Appium 2.x**
- **Python 3.8+**

## Step 1: Install Xcode Command Line Tools

```bash
xcode-select --install
```

## Step 2: Accept Xcode License

```bash
sudo xcodebuild -license accept
```

## Step 3: Install Appium XCUITest Driver

```bash
appium driver install xcuitest
```

Verify installation:
```bash
appium driver list
```

## Step 4: Install Additional Dependencies

```bash
# Install Carthage (dependency manager)
brew install carthage

# Install ios-deploy (for real devices)
npm install -g ios-deploy

# Install idb (iOS development bridge - optional)
brew tap facebook/fb
brew install idb-companion
```

## Step 5: Build iOS App

Navigate to your Flutter project:
```bash
cd /path/to/your/flutter/app
flutter build ios --debug
```

The app will be at: `build/ios/iphonesimulator/Runner.app`

## Step 6: List Available Simulators

```bash
xcrun simctl list devices
```

Example output:
```
iPhone 14 (UUID) (Shutdown)
iPhone 14 Pro (UUID) (Shutdown)
```

## Step 7: Create iOS Configuration

Add to `config/config.py`:

```python
# iOS Configuration
IOS_PLATFORM_NAME = "iOS"
IOS_PLATFORM_VERSION = "17.0"  # Your iOS version
IOS_DEVICE_NAME = "iPhone 14"
IOS_AUTOMATION_NAME = "XCUITest"
IOS_APP_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    "flutter", "my_app", "build", "ios", "iphonesimulator", "Runner.app"
)

@staticmethod
def get_ios_capabilities():
    """Returns iOS capabilities for Appium"""
    return {
        'platformName': Config.IOS_PLATFORM_NAME,
        'platformVersion': Config.IOS_PLATFORM_VERSION,
        'deviceName': Config.IOS_DEVICE_NAME,
        'app': Config.IOS_APP_PATH,
        'automationName': Config.IOS_AUTOMATION_NAME,
        'noReset': Config.NO_RESET,
        'fullReset': Config.FULL_RESET,
        'newCommandTimeout': 300,
        'autoAcceptAlerts': True,
    }
```

## Step 8: Update conftest.py for iOS

Add iOS support to the driver fixture:

```python
import platform

@pytest.fixture(scope="function")
def driver(request):
    """Create and tear down Appium driver"""
    
    # Get platform from command line or use Android as default
    test_platform = request.config.getoption("--platform", default="android")
    
    logger.info(f"[Setup] Starting Appium driver for {test_platform}...")
    
    if test_platform.lower() == "ios":
        capabilities = Config.get_ios_capabilities()
    else:
        capabilities = Config.get_desired_capabilities()
    
    appium_driver = webdriver.Remote(
        Config.APPIUM_SERVER,
        options=get_options_for_platform(test_platform, capabilities)
    )
    
    # ... rest of fixture
```

## Step 9: Run Tests on iOS

```bash
# Start Appium server
appium

# Run tests (in another terminal)
pytest --platform=ios -v
```

## Step 10: Install Dependencies

```bash
pip install Appium-Python-Client==3.1.1
```

## Troubleshooting

### WebDriverAgent Issues

If you get WebDriverAgent errors:
```bash
# Navigate to Appium's WebDriverAgent
cd ~/.appium/node_modules/appium-xcuitest-driver/node_modules/appium-webdriveragent

# Open in Xcode
open WebDriverAgent.xcodeproj

# Sign the app with your Apple ID in Xcode
# Build -> WebDriverAgentRunner -> Select your team
```

### Simulator Not Found

```bash
# List simulators
xcrun simctl list devices

# Boot specific simulator
xcrun simctl boot "iPhone 14"
```

### Permission Issues

```bash
sudo xcode-select --reset
```

## iOS Element Locators

iOS uses different locators than Android:

```python
# iOS uses accessibility identifiers
element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "gmailButton")

# Or iOS predicate strings
element = driver.find_element(
    AppiumBy.IOS_PREDICATE, 
    'label == "Open Gmail"'
)

# Or XPath
element = driver.find_element(
    AppiumBy.XPATH,
    '//XCUIElementTypeButton[@name="Open Gmail"]'
)
```

## Testing on Real iOS Device

Requires:
1. Apple Developer Account
2. Device UDID
3. Provisioning profile
4. Code signing certificate

Additional config:
```python
'udid': 'YOUR_DEVICE_UDID',
'xcodeOrgId': 'YOUR_TEAM_ID',
'xcodeSigningId': 'iPhone Developer',
```

## Next Steps

1. Build your Flutter app for iOS
2. Update configuration for iOS
3. Create iOS-specific page objects if UI differs
4. Run tests on iOS Simulator
5. Add iOS to CI/CD pipeline

## Resources

- [Appium XCUITest Driver](https://github.com/appium/appium-xcuitest-driver)
- [iOS Testing Best Practices](https://appium.io/docs/en/drivers/ios-xcuitest/)
- [Flutter iOS Setup](https://docs.flutter.dev/get-started/install/macos)
