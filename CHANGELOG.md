# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-07

### Added
- Initial project setup with Page Object Model architecture
- Pytest framework configuration with fixtures
- Comprehensive logging system (console and file)
- HTML test report generation with pytest-html
- Allure reporting support
- Base page object with common methods
- Home page object for Flutter app interactions
- Gmail button test suite with 3 test cases
- Smoke and regression test markers
- Configuration management for Appium settings
- Support for Flutter app element handling via accessibility IDs
- Virtual environment setup
- Documentation (README, CONTRIBUTING, LICENSE)
- GitHub templates (issues, PRs)
- CI/CD workflow template
- Comprehensive .gitignore

### Features
- **test_gmail_button_visible**: Verify Gmail button on home page
- **test_click_gmail_button**: Test Gmail button launches browser
- **test_increment_counter_then_gmail**: Test counter increment and Gmail launch

### Technical Details
- Python 3.8+ support
- Appium Python Client 3.1.1
- Selenium 4.16.0
- Pytest 7.4.3
- Android support with UiAutomator2
- UTF-8 log file encoding
- Timestamped log files

## [2.0.0] - 2025-12-08

### Added
- Shopping List feature test suite with 7 comprehensive tests
  - `test_navigate_to_shopping_list` - Navigation verification
  - `test_shopping_list_empty_state` - Empty state validation
  - `test_add_single_item` - Single item addition
  - `test_add_multiple_items` - Multiple items addition
  - `test_add_item_with_default_quantity` - Default quantity handling
  - `test_delete_item` - Item deletion
  - `test_add_and_delete_multiple_items` - Complex CRUD operations
- New `pages/shopping_list_page.py` with full Page Object Model implementation
- UIAutomator selector support for cross-platform delete button functionality
- Home page test suite (`tests/test_home_page.py`) with 5 tests for 3-button UI
  - `test_all_buttons_visible` - Button visibility verification
  - `test_web_search_button_opens_browser` - Web search functionality
  - `test_open_gmail_button` - Gmail button functionality
  - `test_shopping_list_button_navigation` - Shopping list navigation
  - `test_all_buttons_clickable` - Button clickability verification
- Comprehensive docstrings to all page objects
  - `pages/base_page.py` - Enhanced with detailed method documentation
  - `pages/home_page.py` - Added module and method docstrings with Args/Returns
  - `pages/shopping_list_page.py` - Complete documentation for CRUD operations
- Enhanced configuration documentation in `config/config.py`
- Improved fixture documentation in `conftest.py`
- Screenshots for documentation
  - `docs/images/flutter_home_page.png` - Updated with 3-button layout (200px width)
  - `docs/images/shopping_list.png` - Shopping list feature screenshot (200px width)
- iOS setup documentation
  - `docs/IOS_ON_WINDOWS.md` - iOS testing setup on Windows
  - `docs/IOS_SETUP.md` - General iOS setup guide
- Complete README rewrite with modern structure
  - Test suite tables showing all 12 tests with status
  - Test results section with actual execution logs (December 8, 2025)
  - Comprehensive troubleshooting guide (8 scenarios)
  - CI/CD integration examples (GitHub Actions)
  - Page Object Model documentation with method listings
  - Best practices section (10 guidelines)
  - Improved setup instructions (9 detailed steps)
  - Logging details with file locations

### Changed
- Refactored `pages/home_page.py` to support 3-button layout
  - Added `APP_PACKAGE` constant: "com.example.my_app"
  - Enhanced all method docstrings with Args and Returns sections
  - Made debug logging optional in `wait_for_home_page_load(debug=False)`
  - Improved `return_from_webview()` to use APP_PACKAGE constant
  - Simplified `verify_home_page_loaded()` verification logic
- Enhanced `pages/base_page.py` with comprehensive method documentation
  - Added module docstring explaining base class purpose
  - Updated `find_element()` to support optional timeout parameter
  - Documented WebDriver instance and wait strategies
- Updated `logs/sample_test_run.log` with current test execution (December 8, 2025)
- Improved `docs/images/README.md` with detailed screenshot capture guidelines
- Updated README images to use HTML img tags with 200px width for better display

### Removed
- Deleted obsolete `tests/test_gmail_button.py` (replaced by home page tests)
- Removed `tests/test_debug_shopping_list.py` (temporary debug file)
- Cleaned up temporary log files (test_output.log, test_output2.log)
- Removed `log_page_source()` debug method from home_page.py
- Removed redundant debug code from shopping_list_page.py

### Fixed
- Element location reliability using UIAutomator selectors for cross-platform compatibility
- WebView navigation handling with improved context switching
- Shopping list item format parsing ('ItemName\nxQuantity')
- Delete button location using class-based UIAutomator selector

### Test Results
- **12/12 tests passing (100%)**
- Execution time: 7 minutes 39 seconds
- Platform: Windows 11, Python 3.12.9, Android 16
- Device: emulator-5554 (Pixel 7)

## [Unreleased]

### Planned
- Data-driven testing with parameterized tests
- Screenshot capture on test failure
- Video recording of test runs
- Performance testing capabilities
- Additional page objects for more app screens
