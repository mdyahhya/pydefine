"""
pydefine.core
~~~~~~~~~~~~~

Core functionality for pyDefine library.

This module provides the main API functions:
  - decode_traceback(traceback_text): Parse and decode a traceback string
  - decode_exception(e): Decode an exception object directly
  - safe_run(code, filename): Execute code safely with error decoding

All functions return structured dictionaries with error information,
simple explanations, and fix suggestions.
"""

import sys
import traceback
import re
from typing import Dict, Any, Optional, Union

from .mapping import get_exception_info
from .utils import extract_error_info, format_output, tokenize_output
from .i18n import translate_explanation, get_language


def decode_traceback(traceback_text: str) -> Dict[str, Any]:
    if not traceback_text or not isinstance(traceback_text, str):
        return {
            "error_type": "InvalidInput",
            "original_message": "No traceback provided",
            "simple_explanation": "No error information was provided to decode.",
            "fix_suggestion": "Pass a valid traceback string to decode_traceback()",
            "line_number": None,
            "file_name": None,
            "tags": ["invalid-input"],
            "emoji": "❓",
            "success": False,
            "branding": "Powered by pyDefine"
        }
    error_info = extract_error_info(traceback_text)
    exception_data = get_exception_info(error_info["error_type"])
    result = {
        "error_type": error_info["error_type"],
        "original_message": error_info["original_message"],
        "simple_explanation": exception_data["simple_explanation"],
        "fix_suggestion": exception_data["fix_suggestion"],
        "line_number": error_info.get("line_number"),
        "file_name": error_info.get("file_name"),
        "tags": exception_data.get("tags", []),
        "emoji": exception_data.get("emoji", "❓"),
        "success": False
    }
    current_lang = get_language()
    if current_lang != "en":
        result["translated_explanation"] = translate_explanation(
            result["simple_explanation"],
            current_lang
        )
    result["formatted_output"] = format_output(result)
    result["tokens"] = tokenize_output(result)
    result["branding"] = "Powered by pyDefine"
    return result


def decode_exception(e: Exception) -> Dict[str, Any]:
    if not isinstance(e, BaseException):
        return {
            "error_type": "InvalidInput",
            "original_message": "Not a valid exception object",
            "simple_explanation": "The input is not a valid Python exception.",
            "fix_suggestion": "Pass an exception object caught in try/except block",
            "line_number": None,
            "file_name": None,
            "tags": ["invalid-input"],
            "emoji": "❓",
            "success": False,
            "branding": "Powered by pyDefine"
        }
    error_type = type(e).__name__
    original_message = str(e)
    line_number = None
    file_name = None
    if hasattr(e, '__traceback__') and e.__traceback__ is not None:
        tb = e.__traceback__
        while tb.tb_next is not None:
            tb = tb.tb_next
        line_number = tb.tb_lineno
        file_name = tb.tb_frame.f_code.co_filename
    exception_data = get_exception_info(error_type)
    result = {
        "error_type": error_type,
        "original_message": original_message,
        "simple_explanation": exception_data["simple_explanation"],
        "fix_suggestion": exception_data["fix_suggestion"],
        "line_number": line_number,
        "file_name": file_name,
        "tags": exception_data.get("tags", []),
        "emoji": exception_data.get("emoji", "❓"),
        "success": False
    }
    current_lang = get_language()
    if current_lang != "en":
        result["translated_explanation"] = translate_explanation(
            result["simple_explanation"],
            current_lang
        )
    result["formatted_output"] = format_output(result)
    result["tokens"] = tokenize_output(result)
    result["branding"] = "Powered by pyDefine"
    return result

# ... rest of core.py (safe_run, decode_traceback_file, explain, quick_decode) remains unchanged except for any "branding" string to be "Powered by pyDefine"
