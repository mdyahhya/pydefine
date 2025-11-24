"""
pyDefine - Convert Python errors into beginner-friendly explanations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pyDefine is a pure-Python library that takes raw Python tracebacks and
exceptions and converts them into extremely simple, beginner-friendly
explanations with fix suggestions.

Basic usage:

   >>> import pydecode
   >>> result = pydecode.decode_traceback(some_traceback_string)
   >>> print(result['simple_explanation'])

   >>> try:
   ...     1 / 0
   ... except Exception as e:
   ...     result = pydecode.decode_exception(e)
   ...     print(result['simple_explanation'])

Full documentation is available at https://github.com/mdyahhya/pydecode

:copyright: (c) 2025 by Yahya.
:license: MIT, see LICENSE for more details.
"""

import sys
import traceback as tb_module

from .version import __version__
from .core import decode_traceback, decode_exception, safe_run
from .mapping import get_exception_info, EXCEPTION_MAP
from .utils import extract_error_info, format_output, tokenize_output
from .cli import main as cli_main
from .i18n import translate_explanation, set_language, get_language

# Public API
__all__ = [
    "__version__",
    "decode_traceback",
    "decode_exception",
    "safe_run",
    "get_exception_info",
    "EXCEPTION_MAP",
    "extract_error_info",
    "format_output",
    "tokenize_output",
    "cli_main",
    "translate_explanation",
    "set_language",
    "get_language",
]

# Display branding message on import
def _display_branding():
    """Print branding message when library is imported."""
    branding = "\n✨ Powered by pyDefine ● Created by Yahya ✨\n"
    print(branding, file=sys.stderr)

# Automatically display branding on import
_display_branding()
