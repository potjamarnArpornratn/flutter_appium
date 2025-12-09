# Screenshots

This directory contains screenshots of the Flutter app used for testing.

## Available Screenshots

### Current Screenshots
- `flutter_home_page.png` - Home page view showing the three action buttons (Web Search, Open Gmail, Shopping List)
- `shopping_list.png` - Shopping list page showing add form and item list with delete buttons
- `shopping_list_empty.png` - Shopping list empty state showing "No items yet"
- `shopping_list_items.png` - Shopping list with multiple items showing format "ItemName\nxQuantity"

## Adding Screenshots

1. **Start the emulator**:
   ```powershell
   flutter emulators --launch Pixel_7
   ```

2. **Run the Flutter app**:
   ```powershell
   cd D:\development\flutter\my_app
   flutter run
   ```

3. **Navigate to the desired screen** in the app

4. **Capture screenshot using ADB**:
   ```powershell
   # Take screenshot
   adb shell screencap -p /sdcard/screenshot.png
   
   # Pull to local machine
   adb pull /sdcard/screenshot.png docs/images/home_page_buttons.png
   
   # Clean up on device
   adb shell rm /sdcard/screenshot.png
   ```

5. **Or use Android Studio's screenshot tool**: Device File Explorer → Screen Capture

## Screenshot Guidelines

- **Resolution**: Use actual device resolution (1080x2400 for Pixel 7)
- **Format**: PNG for best quality
- **Naming**: Use descriptive snake_case names
- **Focus**: Capture relevant UI elements clearly
- **Annotations**: Consider adding arrows/labels to highlight test elements

## Note

Screenshots help users understand:
- What the app looks like
- Which elements are being tested
- Expected UI layout and behavior
- Test coverage areas
- How features work

## Current App Features

### Home Page (flutter_home_page.png)
- Three action buttons arranged vertically
- App title: "My Assistant"
- Subtitle: "Choose an Action"

### Shopping List (shopping_list.png - to be added)
- Header: "Add items to your shopping list"
- Two input fields: Item name and Quantity
- Back button and Add button
- List of items with format: "ItemName\nxQuantity"
- Each item has a checkbox and delete button (garbage bin icon)
- Footer showing "Total: X items" and "Completed: X"
