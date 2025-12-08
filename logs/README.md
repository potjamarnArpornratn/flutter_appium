# Test Logs

This directory contains detailed test execution logs.

## Log Files

- Logs are automatically generated during test runs
- Filename format: `test_run_YYYYMMDD_HHMMSS.log`
- UTF-8 encoding for full Unicode support
- `sample_test_run.log` - Example log showing successful test execution

## Log Format

```
timestamp - module - level - message
```

Example:
```
2025-12-07 23:00:17,984 - conftest - INFO - [Setup] Starting Appium driver...
```

## Log Levels

- **INFO**: General information about test execution
- **WARNING**: Warning messages (fallback methods, missing elements)
- **ERROR**: Error messages (failures, exceptions)
- **DEBUG**: Detailed debugging information

## Viewing Logs

### View latest log (PowerShell)
```powershell
Get-Content logs\*.log | Select-Object -Last 50
```

### View specific log
```powershell
Get-Content logs\test_run_20251207_230000.log
```

### Search logs for errors
```powershell
Get-Content logs\*.log | Select-String "ERROR"
```

## What's Logged

- **Session lifecycle**: Start/end timestamps
- **Driver setup**: Appium connection, device info, capabilities
- **Test execution**: Test start/completion markers
- **Actions**: Button clicks, page navigation, element interactions
- **Verifications**: Element checks, assertions
- **Results**: Pass/fail status with [PASS] markers

## Note

Log files are excluded from git (see `.gitignore`) except for `sample_test_run.log` which serves as an example.
