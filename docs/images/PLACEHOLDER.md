# Add Your Screenshot Here

To add the Flutter app screenshot:

1. **Run your Flutter app** on the emulator/device
2. **Capture screenshot** using one of these methods:

### Method 1: Using ADB
```powershell
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png flutter_home_page.png
```

### Method 2: Using Android Studio
- Click the camera icon in the emulator toolbar
- Save the screenshot

### Method 3: Using Emulator
- Press Ctrl+S (Windows) while emulator is focused
- Screenshot saved to desktop

3. **Rename and move** the screenshot to `docs/images/flutter_home_page.png`
4. **Commit and push** to GitHub

The screenshot should show:
- Gmail button
- Counter text
- Increment FAB button
- Overall app layout

This helps users understand what elements the tests interact with.
