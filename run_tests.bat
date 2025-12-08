@echo off
echo Running Flutter Appium Tests
echo ============================
echo.

rem Check if Appium server is running
echo Checking Appium server...
curl -s http://localhost:4723/status >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Appium server is not running!
    echo Please start Appium server first: appium
    pause
    exit /b 1
)

rem Check if device is connected
echo Checking device connection...
adb devices | find "device" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: No Android device connected!
    echo Please start emulator: flutter emulators --launch Pixel_7
    pause
    exit /b 1
)

echo.
echo Running tests...
pytest %*

echo.
echo Test execution completed!
pause
