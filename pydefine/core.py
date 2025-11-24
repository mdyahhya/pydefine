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

def safe_run(code: str, filename: str = "<input>", globals_dict: Optional[Dict] = None, locals_dict: Optional[Dict] = None) -> Dict[str, Any]:
    if not isinstance(code, str):
        return {
            "success": False,
            "error_type": "InvalidInput",
            "original_message": "Code must be a string",
            "simple_explanation": "The code input is not a valid string.",
            "fix_suggestion": "Pass a string containing Python code",
            "tags": ["invalid-input"],
            "emoji": "❓",
            "branding": "Powered by pyDefine"
        }
    
    if not code.strip():
        return {
            "success": True,
            "result": None,
            "output": "",
            "message": "No code to execute",
            "branding": "Powered by pyDefine"
        }
    
    if globals_dict is None:
        globals_dict = {
            "__builtins__": {
                "print": print,
                "len": len,
                "range": range,
                "int": int,
                "float": float,
                "str": str,
                "bool": bool,
                "list": list,
                "dict": dict,
                "tuple": tuple,
                "set": set,
                "abs": abs,
                "min": min,
                "max": max,
                "sum": sum,
                "sorted": sorted,
                "reversed": reversed,
                "enumerate": enumerate,
                "zip": zip,
                "map": map,
                "filter": filter,
                "round": round,
                "pow": pow,
                "isinstance": isinstance,
                "type": type,
                "dir": dir,
                "help": help,
            },
            "__name__": "__main__",
            "__file__": filename,
        }
    
    if locals_dict is None:
        locals_dict = {}
    
    import io
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        compiled_code = compile(code, filename, 'exec')
        exec(compiled_code, globals_dict, locals_dict)
        output = captured_output.getvalue()
        sys.stdout = old_stdout
        return {
            "success": True,
            "result": locals_dict.get("result", None),
            "output": output,
            "message": "Code executed successfully",
            "branding": "Powered by pyDefine"
        }
    except Exception as e:
        sys.stdout = old_stdout
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        tb_text = ''.join(tb_lines)
        decoded = decode_traceback(tb_text)
        decoded["success"] = False
        decoded["output"] = captured_output.getvalue()
        return decoded


def decode_traceback_file(filepath: str) -> Dict[str, Any]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            traceback_text = f.read()
        return decode_traceback(traceback_text)
    except FileNotFoundError:
        return {
            "success": False,
            "error_type": "FileNotFoundError",
            "original_message": f"File not found: {filepath}",
            "simple_explanation": "The traceback file you specified doesn't exist.",
            "fix_suggestion": f"Check if the file path '{filepath}' is correct",
            "tags": ["file", "not-found"],
            "emoji": "📁",
            "branding": "Powered by pyDefine"
        }
    except Exception as e:
        return {
            "success": False,
            "error_type": type(e).__name__,
            "original_message": str(e),
            "simple_explanation": f"Could not read the file: {str(e)}",
            "fix_suggestion": "Check file permissions and format",
            "tags": ["file", "read-error"],
            "emoji": "📁",
            "branding": "Powered by pyDefine"
        }


def explain(exception_or_traceback: Union[Exception, str]) -> str:
    if isinstance(exception_or_traceback, BaseException):
        decoded = decode_exception(exception_or_traceback)
    elif isinstance(exception_or_traceback, str):
        decoded = decode_traceback(exception_or_traceback)
    else:
        return "❓ Invalid input - pass an exception object or traceback string"
    
    emoji = decoded.get("emoji", "")
    explanation = decoded.get("simple_explanation", "No explanation available")
    return f"{emoji} {explanation}"


def quick_decode(e: Exception) -> None:
    decoded = decode_exception(e)
    print("\n" + "="*70)
    print(f"🔍 {decoded['error_type']}: {decoded['original_message']}")
    print("="*70)
    print(f"\n{decoded['emoji']} {decoded['simple_explanation']}\n")
    print(f"💡 Fix: {decoded['fix_suggestion']}\n")
    if decoded.get('line_number'):
        print(f"📍 Line {decoded['line_number']}")
        if decoded.get('file_name'):
            print(f"📁 File: {decoded['file_name']}")
    print("\n" + decoded['branding'])
    print("="*70 + "\n")
