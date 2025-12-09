# iOS Testing on Windows - Real Device Setup

Since iOS Simulator only works on macOS, you can test on a **real iOS device** connected to Windows.

## Prerequisites

1. **Real iPhone or iPad**
2. **Windows PC**
3. **USB cable** (Lightning or USB-C)
4. **iTunes** installed (provides necessary drivers)
5. **Apple Developer Account** (can be free)

## Setup Steps

### Step 1: Install iTunes

Download and install iTunes from Microsoft Store or Apple website:
```powershell
winget install Apple.iTunes
```

This installs necessary iOS device drivers for Windows.

### Step 2: Install Required Tools

```powershell
# Install usbmuxd for iOS connectivity
npm install -g appium-ios-device

# Install Appium XCUITest driver
appium driver install xcuitest
```

### Step 3: Connect iOS Device

1. Connect iPhone/iPad via USB to Windows PC
2. **Unlock the device**
3. Tap **Trust** when prompted on device
4. Check device connection:
   ```powershell
   appium driver run xcuitest list-devices
   ```

### Step 4: Get Device UDID

```powershell
# Method 1: Using Appium
appium driver run xcuitest list-devices

# Method 2: Using iTunes (legacy)
# Open iTunes -> Device -> Summary -> Serial Number -> Click to show UDID
```

### Step 5: Configure for Real Device

Update `config/config.py`:

```python
# iOS Real Device Configuration
IOS_PLATFORM_NAME = "iOS"
IOS_PLATFORM_VERSION = "17.0"  # Your iOS version
IOS_DEVICE_NAME = "iPhone"  # Can be any name
IOS_UDID = "YOUR_DEVICE_UDID_HERE"  # Get from Step 4
IOS_AUTOMATION_NAME = "XCUITest"
IOS_BUNDLE_ID = "com.example.myApp"  # Your Flutter app bundle ID

# For development build (no code signing needed)
IOS_USE_PREBUILT_WDA = True

@staticmethod
def get_ios_capabilities():
    """Returns iOS capabilities for real device"""
    return {
        'platformName': Config.IOS_PLATFORM_NAME,
        'platformVersion': Config.IOS_PLATFORM_VERSION,
        'deviceName': Config.IOS_DEVICE_NAME,
        'udid': Config.IOS_UDID,
        'bundleId': Config.IOS_BUNDLE_ID,  # Use bundleId instead of app
        'automationName': Config.IOS_AUTOMATION_NAME,
        'noReset': True,  # App must be pre-installed
        'usePrebuiltWDA': Config.IOS_USE_PREBUILT_WDA,
        'newCommandTimeout': 300,
        'autoAcceptAlerts': True,
    }
```

### Step 6: Install App on Device

You need to install your Flutter app on the device first:

**Option A: Using Xcode (requires Mac)**
- Build and install via Xcode
- Or use TestFlight

**Option B: Using Third-party Tools**
- Use Cydia Impactor (free developer account)
- Use AltStore

**Option C: Development Build**
```bash
# On Mac with device connected
flutter build ios
flutter install
```

### Step 7: Run Tests

```powershell
# Start Appium server
appium

# Run tests
pytest --platform=ios -v
```

## Limitations

- ❌ Cannot build iOS app on Windows (need Mac for that)
- ❌ App must be pre-installed on device
- ✅ Can run tests once app is installed
- ✅ Can automate testing on real hardware

## Alternative: Cloud Testing Services

If real device setup is too complex, use cloud services:

### BrowserStack

```python
# BrowserStack configuration
BS_USERNAME = "your_username"
BS_ACCESS_KEY = "your_access_key"
BS_SERVER = f"https://{BS_USERNAME}:{BS_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

capabilities = {
    'platformName': 'iOS',
    'platformVersion': '17',
    'deviceName': 'iPhone 14',
    'app': 'bs://your_app_id',  # Upload app first
    'browserstack.debug': True,
}

driver = webdriver.Remote(BS_SERVER, options=capabilities)
```

### Sauce Labs

```python
# Sauce Labs configuration
SAUCE_USERNAME = "your_username"
SAUCE_ACCESS_KEY = "your_access_key"
SAUCE_SERVER = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.us-west-1.saucelabs.com/wd/hub"

capabilities = {
    'platformName': 'iOS',
    'platformVersion': '17.0',
    'deviceName': 'iPhone 14 Simulator',
    'app': 'sauce-storage:your_app.ipa',
}

driver = webdriver.Remote(SAUCE_SERVER, options=capabilities)
```

### LambdaTest

```python
# LambdaTest configuration
LT_USERNAME = "your_username"
LT_ACCESS_KEY = "your_access_key"
LT_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

capabilities = {
    'platformName': 'iOS',
    'platformVersion': '17',
    'deviceName': 'iPhone 14',
    'app': 'lt://your_app_id',
    'isRealMobile': True,
}

driver = webdriver.Remote(LT_SERVER, options=capabilities)
```

## Cost Comparison

| Solution | Cost | Pros | Cons |
|----------|------|------|------|
| Real Device | Free (need device) | Full control, no recurring cost | Setup complex, need Mac to build |
| BrowserStack | $29-199/mo | Easy, many devices, instant | Recurring cost, internet dependent |
| Sauce Labs | $39-299/mo | Comprehensive, CI/CD ready | Expensive |
| LambdaTest | $15-199/mo | Affordable, real devices | Limited features on cheaper plans |
| AWS Device Farm | Pay per device hour | Flexible, integrates with AWS | Complex setup |

## Recommended Approach for Windows Users

1. **Development Phase**: Use Android emulator (what you have now)
2. **Pre-release Testing**: Use cloud service (BrowserStack/LambdaTest)
3. **Critical Tests**: Borrow a Mac or use real device

## Summary

**For Windows without Mac:**
- ✅ Can test on **real iOS device** (complex setup)
- ✅ Can use **cloud testing services** (easiest, costs money)
- ❌ Cannot use iOS Simulator
- ❌ Cannot build iOS app (need Mac)

**Best option:** Use a cloud testing service for iOS while keeping your Android tests running locally.
