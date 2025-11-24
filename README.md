# pyDefine

**Convert Python errors into beginner-friendly explanations and guides you with possible solutions** ✨

[![Python Version](https://img.shields.io/pypi/pyversions/pydefine.svg)](https://pypi.org/project/pydefine/)
[![PyPI Version](https://img.shields.io/pypi/v/pydefine.svg)](https://pypi.org/project/pydefine/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/mdyahhya/pydefine/workflows/CI/badge.svg)](https://github.com/mdyahhya/pydefine/actions)

**pyDefine** is a pure-Python library created by **Yahya Mundewadi**. pydefine takes raw Python tracebacks and exceptions and converts them into **extremely simple, beginner-friendly explanations** with actionable fix suggestions. Perfect for students, educators, and anyone learning Python!

## Features 🌟

- **88+ Exception Types Covered** - Comprehensive support for all Python built-in exceptions
- **Beginner-Friendly Explanations** - No jargon, simple English with analogies and emojis
- **Actionable Fix Suggestions** - Every error comes with a clear solution
- **Multiple Interfaces** - Use as library, CLI tool, or interactive decoder
- **Pure Python** - Zero dependencies, works everywhere Python runs
- **Safe Code Execution** - Built-in `safe_run()` for testing code with automatic error decoding
- **i18n Support** - Hinglish (Hindi+English) translations included, extensible to more languages
- **Production Ready** - Fully tested, type-hinted, and documented

---

## Installation 📦

### From PyPI (Recommended)

pip install pydefine


### From Source

git clone https://github.com/mdyahhya/pydefine.git
cd pydefine
pip install -e .


### For Development

pip install -e ".[dev]"

---

## Quick Start 🚀

### Basic Usage
# import pydefine

# That's it! Now all uncaught exceptions automatically show beginner-friendly explanations.
# Just write your Python code normally:

number = 10
divisor = 0
result = number / divisor  # This error will be automatically explained!

Output (automatic):
======================================================================
➗ ZeroDivisionError: division by zero
======================================================================

📖 What happened:
   You tried to divide a number by zero, which is impossible in math. 
   Division by zero breaks the universe's math rules. 
   Python can't calculate infinity ➗

💡 How to fix:
   Check if the divisor is zero before dividing, 
   or add a condition to handle zero values

📍 Where:
   File: script.py
   Line: 3

🏷️  Tags: arithmetic, division, zero, math

──────────────────────────────────────────────────────────────────────
✨ Powered by pyDefine ✨
======================================================================

Command Line Interface

# Run a Python file with error decoding
pydefine script.py

# List all supported exceptions
pydefine --list

# Decode a log file
pydefine --decode-log error.log

### API Reference 📖
# Automatic Global Exception Handler
# When you import pydefine, it automatically catches all uncaught exceptions and displays beginner-friendly explanations. No other code needed!

Advanced Functions (Optional)
For advanced users who need more control, pyDefine also provides these functions:

decode_traceback(traceback_text: str) -> Dict

Decode a raw traceback string into beginner-friendly explanation.

Returns:

{
    'error_type': 'ZeroDivisionError',
    'original_message': 'division by zero',
    'simple_explanation': 'You tried to divide a number by zero...',
    'fix_suggestion': 'Check if the divisor is zero before dividing...',
    'line_number': 5,
    'file_name': 'script.py',
    'tags': ['arithmetic', 'division', 'zero'],
    'emoji': '➗',
    'success': False,
    'formatted_output': '...',
    'branding': 'Powered by pyDefine'
}

decode_exception(e: Exception) -> Dict

Decode an exception object directly.

safe_run(code: str, filename: str = "<input>") -> Dict

Execute Python code safely with automatic error decoding.

explain(exception_or_traceback) -> str

Quick one-liner to get explanation.

## Supported Exceptions 🎯

pyDefine supports **88+ Python built-in exceptions** including:

### Common Errors
- `SyntaxError`, `IndentationError`, `TabError`
- `NameError`, `UnboundLocalError`
- `TypeError`, `ValueError`, `AttributeError`
- `KeyError`, `IndexError`
- `ZeroDivisionError`, `OverflowError`
- `FileNotFoundError`, `PermissionError`, `IOError`
- `ImportError`, `ModuleNotFoundError`

### Advanced Errors
- `RecursionError`, `MemoryError`
- `ConnectionError`, `TimeoutError`
- `UnicodeDecodeError`, `UnicodeEncodeError`
- `RuntimeError`, `NotImplementedError`
- All warning types
- Exception groups (Python 3.11+)

View full list: `pydefine --list-all`

---

## 💡 Example Output

**Before (Standard Python Error):**
Traceback (most recent call last):
File "script.py", line 5, in <module>
print(data['email'])
KeyError: 'email'


**After (pyDefine):**

======================================================================
🔑 KeyError: 'email'
📖 What happened:
You tried to get a value from a dictionary using a key that doesn't
exist. It's like looking for a word in a dictionary that isn't there.
The key you asked for is missing 🔑

💡 How to fix:
Use dict.get(key, default) instead of dict[key], or check if the
key exists with 'key in dict' first

📍 Where:
File: script.py
Line: 5
🏷️ Tags: key, dictionary, lookup, missing

──────────────────────────────────────────────────────────────────────
 Powered by pyDefine ● Created by Yahya 



---

## Internationalization 🌍 (i18n) 

pyDefine supports multiple languages for explanations:

import pydefine
from pydefine.i18n import set_language

Set language to Hinglish (Hindi + English)
set_language('hi')

try:
x = 10 / 0
except Exception as e:
result = pydefine.decode_exception(e)
print(result['translated_explanation'])


**Supported Languages:**
- English (`en`) - Default
- Hinglish (`hi`) - Hindi + English mix

More languages coming soon!

---

## CLI Usage 🛠️

### Run Python Files

pydefine script.py
pydefine --verbose script.py


### List Exceptions

Common exceptions
pydefine --list

All exceptions with categories
pydefine --list-all

Filter by tag
pydefine --list --tag syntax


### Decode Log Files

pydefine --decode-log error.log


---

## Testing 🧪

Run the test suite:

Install dev dependencies
pip install -e ".[dev]"

Run tests
pytest

Run with coverage
pytest --cov=pydefine --cov-report=html

Run specific test file
pytest tests/test_core.py -v

---

## Project Stats 📊

- **88+ Exceptions** covered with full explanations
- **50+ Tags** for classification
- **100% Pure Python** - no dependencies
- **Python 3.8+** compatible
- **95%+ Test Coverage**
- **Type Hints** throughout

---

## Contributing 🤝

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- Add explanations for custom exceptions
- Improve existing explanations
- Add translations for new languages
- Fix bugs or add features
- Improve documentation

---

## License 📜 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments ⚡

- Inspired by the need to make Python more accessible to beginners
- Built with ❤️ for the Python community
- Special thanks to all contributors

---

## Contact 📞

**Author:** Md. Yahya Ab. Wahid Mundewadi  
**Email:** yahyabuilds@gmail.com  
**GitHub:** [@mdyahhya](https://github.com/mdyahhya)
**Instagram:** [@pydefine](https://instagram.com/pydefine)

---

## Show Your Support ❤️

If pyDefine helped you, please:
- 📸 Follow us on Instagram @pydefine
- ⭐ Star this repository
- 🐦 Share on social media
- 📝 Write a blog post about it
- 🤝 Contribute to the project

---

**Powered by pyDefine ● Created by Yahya**




