# Contributing to pyDefine

Thank you for considering contributing to pyDefine! 🎉

This document provides guidelines for contributing to the project. Following these guidelines helps maintain code quality and makes the contribution process smooth for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Adding New Exceptions](#adding-new-exceptions)
- [Adding Translations](#adding-translations)

---

## 🤝 Code of Conduct

Be respectful, inclusive, and professional. This project follows standard open-source community guidelines.

---

## 💡 How Can I Contribute?

### Reporting Bugs
- Check if the bug is already reported in [Issues](https://github.com/mdyahhya/pydefine/issues)
- Use the bug report template
- Include Python version, OS, and error traceback
- Provide minimal reproducible example

### Suggesting Features
- Check existing feature requests first
- Explain the use case and benefits
- Provide examples if possible

### Improving Documentation
- Fix typos, clarify explanations
- Add examples or use cases
- Update outdated information

### Writing Code
- Fix bugs or implement features
- Improve performance
- Add new exception explanations
- Add language translations

---

## 🛠️ Development Setup

### 1. Fork and Clone

git clone https://github.com/YOUR_USERNAME/pydefine.git
cd pydefine


### 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate



### 3. Install Development Dependencies

pip install -e ".[dev]"


### 4. Create a Branch

git checkout -b feature/your-feature-name

or
git checkout -b fix/your-bug-fix


---

## 📝 Coding Standards

### Python Style
- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://github.com/psf/black) for formatting: `black pydefine/`
- Use [Ruff](https://github.com/astral-sh/ruff) for linting: `ruff check pydefine/`
- Maximum line length: 100 characters

### Type Hints
- Add type hints to all function signatures
- Use Python 3.8+ compatible types

### Docstrings
- Use Google-style docstrings
- Include Args, Returns, and Examples sections

**Example:**
def decode_traceback(traceback_text: str) -> Dict[str, Any]:
"""
Decode a raw traceback string into beginner-friendly explanation.

Args:
    traceback_text: Raw traceback string (multi-line)
    
Returns:
    Dictionary with decoded error information
    
Example:
    >>> result = decode_traceback(tb_string)
    >>> print(result['simple_explanation'])
"""

### Naming Conventions
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

---

## 🧪 Testing

### Run Tests

All tests
pytest

With coverage
pytest --cov=pydefine --cov-report=html

Specific test file
pytest tests/test_core.py -v

Specific test
pytest tests/test_core.py::TestDecodeTraceback::test_decode_name_error -v

### Writing Tests
- Add tests for all new features
- Test edge cases and error conditions
- Aim for 90%+ code coverage
- Use descriptive test names

**Example:**
def test_decode_zero_division_error(self):
"""Test decoding a ZeroDivisionError."""
traceback_text = """..."""
result = decode_traceback(traceback_text)
assert result['error_type'] == 'ZeroDivisionError'


---

## 📤 Submitting Changes

### Before Submitting

1. **Run tests:** `pytest`
2. **Check formatting:** `black pydefine/ tests/`
3. **Run linter:** `ruff check pydefine/`
4. **Update documentation** if needed
5. **Add entry to CHANGELOG.md**

### Pull Request Process

1. **Update your fork:**

git fetch upstream
git rebase upstream/main


2. **Push your changes:**

git push origin feature/your-feature-name


3. **Create Pull Request:**
- Use descriptive title
- Reference related issues
- Explain what and why
- Include screenshots if UI changes

4. **PR Template:**

Description
Brief description of changes

Related Issue
Fixes #123

Changes Made
Added X feature

Fixed Y bug

Testing
Added tests for X

All tests passing

Checklist
 Tests pass

 Code formatted with Black

 Documentation updated

 CHANGELOG updated

 
---

## 🆕 Adding New Exceptions

### Step 1: Add to `mapping.py`

"NewExceptionName": {
"simple_explanation": (
"First sentence explaining what happened. "
"Second sentence with more context. "
"Third sentence with an analogy 🎯"
),
"fix_suggestion": (
"Clear, actionable fix in one line"
),
"tags": ["tag1", "tag2", "category"],
"emoji": "🔥"
}


### Step 2: Add Test in `test_mapping.py`

def test_new_exception_present(self):
"""Test NewExceptionName is in map."""
assert 'NewExceptionName' in EXCEPTION_MAP


### Guidelines
- **Explanations:** 2-3 sentences, simple English, no jargon
- **Analogies:** Use everyday comparisons
- **Emojis:** Pick relevant, single emoji
- **Tags:** 3-5 descriptive tags
- **Fixes:** Actionable, beginner-friendly

---

## 🌍 Adding Translations

### Step 1: Add to `i18n.py`

TRANSLATION_TEMPLATES = {
"fr": { # French
"NameError": {
"simple_explanation": "Vous avez essayé d'utiliser...",
"fix_suggestion": "Vérifiez l'orthographe..."
}
}
}


### Step 2: Update `SUPPORTED_LANGUAGES`

SUPPORTED_LANGUAGES = {
"en": "English",
"hi": "Hinglish (Hindi + English)",
"fr": "French", # Add new language
}


### Step 3: Add Tests


def test_french_translation(self):
"""Test French translation works."""
set_language('fr')
# ... test translation


---

## ✅ Review Process

1. **Automated Checks:** CI runs tests, linting
2. **Code Review:** Maintainer reviews code
3. **Feedback:** Address any comments
4. **Approval:** Once approved, will be merged
5. **Release:** Included in next version

---

## 🎁 Recognition

Contributors will be:
- Listed in README acknowledgments
- Mentioned in release notes
- Given credit in commit messages

---

## 📞 Questions?

- Open a [Discussion](https://github.com/mdyahhya/pydefine/discussions)
- Email: yahyabuilds@gmail.com
- Check existing issues/PRs

---

**Thank you for contributing to pyDefine! 🚀**

 Powered by pyDefine ● Created by Yahya 

