@echo off
echo Starting Appium Test Framework Setup
echo =====================================
echo.

echo Step 1: Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Step 2: Verifying Appium installation...
call appium -v

echo.
echo Step 3: Checking Android device connection...
call adb devices

echo.
echo =====================================
echo Setup complete!
echo.
echo Next steps:
echo 1. Start Appium server: appium
echo 2. Start Android emulator: flutter emulators --launch Pixel_7
echo 3. Run tests: pytest
echo.
pause
