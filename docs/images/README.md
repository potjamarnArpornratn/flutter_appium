# Screenshots

This directory contains screenshots of the Flutter app used for testing.

## Available Screenshots

- `flutter_home_page.png` - Home page showing Gmail button and counter
- `flutter_app_elements.png` (optional) - Annotated screenshot showing test elements

## Adding Screenshots

1. Run the Flutter app on emulator
2. Take screenshot using `adb` or emulator tools
3. Save in this directory
4. Reference in README.md

### Using ADB to capture screenshots:
```powershell
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png docs/images/flutter_home_page.png
```

## Note

Screenshots help users understand:
- What the app looks like
- Which elements are being tested
- Expected UI layout
- Test coverage areas
