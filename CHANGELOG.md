# Changelog

All notable changes to pyDefine will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-24

### Added
- Initial release of pyDefine
- Support for 88+ Python built-in exceptions
- `decode_traceback()` function for parsing traceback strings
- `decode_exception()` function for decoding exception objects
- `safe_run()` function for safe code execution with error decoding
- `decode_traceback_file()` function for reading error logs
- `explain()` convenience function for quick explanations
- `quick_decode()` interactive function for terminal use
- CLI tool `pydefine` with multiple commands
- Internationalization (i18n) support with Hinglish translations
- Comprehensive test suite with 95%+ coverage
- Full documentation and examples
- Rich output formatting with emojis
- Token-based output for future rich rendering
- Tag-based exception search and filtering
- Error categorization system
- Branding message on import

### Features
- Pure Python implementation (no dependencies)
- Python 3.8+ compatibility
- Type hints throughout
- Complete exception mapping with beginner-friendly explanations
- Actionable fix suggestions for every error
- Line number and file name extraction
- Safe execution environment for `safe_run()`
- ANSI code stripping for terminal output
- Multiple output formats (dict, formatted string, tokens)

### Documentation
- Comprehensive README with examples
- API reference documentation
- Contributing guidelines
- Security policy
- Release instructions
- Example scripts demonstrating all features
- Detailed docstrings for all public functions

### Testing
- Unit tests for core functionality
- Tests for all 88+ exception types
- Edge case testing
- GitHub Actions CI/CD workflow
- Test coverage reporting

## [Unreleased]

### Planned Features
- Web-based error decoder interface
- Integration with popular Python IDEs
- More language translations (Spanish, French, German, etc.)
- Custom exception registry for third-party libraries
- Error statistics and analytics
- Interactive tutorial mode
- VS Code extension
- Jupyter notebook integration
- Real-time code analysis
- Learning paths based on common errors

---

**✨ Powered by pyDefine ● Created by Yahya ✨**
