"""
pyDefine - Convert Python errors into beginner-friendly explanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyDefine is a pure-Python library that takes raw Python tracebacks and
exceptions and converts them into extremely simple, beginner-friendly
explanations with fix suggestions.

Basic usage:

   >>> import pydefine
   >>> result = pydefine.decode_traceback(some_traceback_string)
   >>> print(result['simple_explanation'])

   >>> try:
   ...     1 / 0
   ... except Exception as e:
   ...     result = pydefine.decode_exception(e)
   ...     print(result['simple_explanation'])

Full documentation is available at https://github.com/mdyahhya/pydefine

:copyright: (c) 2025 by Yahya.
:license: MIT, see LICENSE for more details.
"""

import sys
import traceback as tb_module

from .version import __version__
from .core import decode_traceback, decode_exception, safe_run, decode_traceback_file, explain, quick_decode
from .mapping import get_exception_info, EXCEPTION_MAP, list_all_exceptions, search_exceptions_by_tag, TOTAL_EXCEPTIONS, ALL_TAGS
from .utils import extract_error_info, format_output, tokenize_output, strip_ansi_codes, get_python_version, get_error_category, clean_traceback_text
from .cli import main as cli_main
from .i18n import translate_explanation, set_language, get_language, SUPPORTED_LANGUAGES

# Public API
__all__ = [
    # Version
    "__version__",
    
    # Core functions
    "decode_traceback",
    "decode_exception",
    "safe_run",
    "decode_traceback_file",
    "explain",
    "quick_decode",
    
    # Mapping functions
    "get_exception_info",
    "EXCEPTION_MAP",
    "list_all_exceptions",
    "search_exceptions_by_tag",
    "TOTAL_EXCEPTIONS",
    "ALL_TAGS",
    
    # Utility functions
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

# Display branding message on import
def _display_branding():
    """Print branding message when library is imported."""
    branding = "\n✨ Powered by pyDefine ● Created by Yahya ✨\n"
    print(branding, file=sys.stderr)

# Automatically display branding on import
_display_branding()
