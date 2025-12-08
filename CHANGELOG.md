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

## [Unreleased]

### Planned
- iOS support
- More page objects for different screens
- Data-driven testing
- Screenshot capture on failure
- Video recording of test runs
- Performance testing capabilities
