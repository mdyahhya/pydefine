"""
pyDefine - Convert Python errors into beginner-friendly explanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyDefine is a pure-Python library that takes raw Python tracebacks and
exceptions and converts them into extremely simple, beginner-friendly
explanations with fix suggestions.

Basic usage:

   >>> import pydefine
   >>> # That's it! Uncaught exceptions will be explained automatically.

Full documentation:
https://github.com/mdyahhya/pydefine

:copyright: (c) 2025 by Yahya.
:license: MIT, see LICENSE for more details.
"""

import sys

from .version import __version__
from .core import (
    decode_traceback, decode_exception, safe_run, decode_traceback_file, 
    explain, quick_decode
)
from .mapping import (
    get_exception_info, EXCEPTION_MAP, list_all_exceptions, 
    search_exceptions_by_tag, TOTAL_EXCEPTIONS, ALL_TAGS
)
from .utils import (
    extract_error_info, format_output, tokenize_output, strip_ansi_codes,
    get_python_version, get_error_category, clean_traceback_text
)
from .cli import main as cli_main
from .i18n import translate_explanation, set_language, get_language, SUPPORTED_LANGUAGES

__all__ = [
    "__version__",
    # Core functions
    "decode_traceback",
    "decode_exception",
    "safe_run",
    "decode_traceback_file",
    "explain",
    "quick_decode",
    # Mapping
    "get_exception_info",
    "EXCEPTION_MAP",
    "list_all_exceptions",
    "search_exceptions_by_tag",
    "TOTAL_EXCEPTIONS",
    "ALL_TAGS",
    # Utilities
    "extract_error_info",
    "format_output",
    "tokenize_output",
    "strip_ansi_codes",
    "get_python_version",
    "get_error_category",
    "clean_traceback_text",
    # CLI
    "cli_main",
    # i18n
    "translate_explanation",
    "set_language",
    "get_language",
    "SUPPORTED_LANGUAGES",
]

# Automatically install global exception hook on import
def _global_exception_hook(exc_type, exc_value, exc_traceback):
    try:
        from .core import decode_exception
        decoded = decode_exception(exc_value)
        print(decoded['formatted_output'])
    except Exception:
        # If something fails, fallback to default Python behavior
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = _global_exception_hook
