# Contributing to Flutter Appium Test Framework

Thank you for considering contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit your changes: `git commit -m "Add your feature"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Development Setup

```powershell
# Clone repository
git clone <repo-url>
cd flutter_appium

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to classes and methods
- Keep functions focused and modular

## Testing

Before submitting a PR:

```powershell
# Run all tests
pytest -v

# Check for any errors
pytest --tb=short
```

## Adding New Tests

1. Create test file in `tests/` directory
2. Follow existing naming convention: `test_*.py`
3. Use pytest markers (`@pytest.mark.smoke`, `@pytest.mark.regression`)
4. Add proper logging statements
5. Update README.md with new test cases

## Adding New Page Objects

1. Create page file in `pages/` directory
2. Inherit from `BasePage`
3. Define element locators as class variables
4. Implement action methods with logging
5. Use accessibility IDs for Flutter elements

## Commit Messages

Format: `<type>: <description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

Example: `feat: add login page object and tests`

## Pull Request Process

1. Ensure all tests pass
2. Update README.md if needed
3. Add/update test cases
4. Describe your changes clearly in PR description
5. Link any related issues

## Questions?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about usage
- Suggestions for improvement
