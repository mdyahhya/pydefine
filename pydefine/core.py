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
    """
    Decode a raw traceback string into beginner-friendly explanation.
    
    This is the main function for parsing complete traceback text from
    terminal output, log files, or string captures.
    
    Args:
        traceback_text: Raw traceback string (multi-line)
        
    Returns:
        Dictionary with keys:
            - error_type: Exception class name (e.g., 'ValueError')
            - original_message: Original error message
            - simple_explanation: 2-3 line beginner explanation
            - fix_suggestion: One-line actionable fix
            - line_number: Line number where error occurred (if found)
            - file_name: File name where error occurred (if found)
            - tags: List of classification keywords
            - emoji: Visual identifier emoji
            - formatted_output: Pretty formatted string (optional)
            - success: Always False for errors
            
    Example:
        >>> tb_text = '''Traceback (most recent call last):
        ...   File "test.py", line 5, in <module>
        ...     print(x)
        ... NameError: name 'x' is not defined'''
        >>> result = decode_traceback(tb_text)
        >>> print(result['simple_explanation'])
        You tried to use a variable or function name that doesn't exist yet...
    """
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
            "branding": "Powered by pyDefine ● Created by Yahya"
        }
    
    # Extract error information from traceback text
    error_info = extract_error_info(traceback_text)
    
    # Get exception mapping info
    exception_data = get_exception_info(error_info["error_type"])
    
    # Build result dictionary
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
    
    # Add translation if language is not English
    current_lang = get_language()
    if current_lang != "en":
        result["translated_explanation"] = translate_explanation(
            result["simple_explanation"],
            current_lang
        )
    
    # Add formatted output
    result["formatted_output"] = format_output(result)
    
    # Add tokenized output (for rich rendering with images/audio)
    result["tokens"] = tokenize_output(result)
    
    # Add branding footer
    result["branding"] = "Powered by pyDefine ● Created by Yahya"
    
    return result


def decode_exception(e: Exception) -> Dict[str, Any]:
    """
    Decode an exception object directly into beginner-friendly explanation.
    
    This is useful when you catch an exception in a try/except block and
    want to decode it immediately without converting to string.
    
    Args:
        e: Exception object (any subclass of BaseException)
        
    Returns:
        Same dictionary format as decode_traceback()
        
    Example:
        >>> try:
        ...     result = 10 / 0
        ... except Exception as e:
        ...     decoded = decode_exception(e)
        ...     print(decoded['simple_explanation'])
        You tried to divide a number by zero, which is impossible in math...
    """
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
            "branding": "Powered by pyDefine ● Created by Yahya"
        }
    
    # Extract exception details
    error_type = type(e).__name__
    original_message = str(e)
    
    # Try to get traceback information
    line_number = None
    file_name = None
    
    if hasattr(e, '__traceback__') and e.__traceback__ is not None:
        tb = e.__traceback__
        # Walk to the last frame (where error occurred)
        while tb.tb_next is not None:
            tb = tb.tb_next
        line_number = tb.tb_lineno
        file_name = tb.tb_frame.f_code.co_filename
    
    # Get exception mapping info
    exception_data = get_exception_info(error_type)
    
    # Build result dictionary
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
    
    # Add translation if language is not English
    current_lang = get_language()
    if current_lang != "en":
        result["translated_explanation"] = translate_explanation(
            result["simple_explanation"],
            current_lang
        )
    
    # Add formatted output
    result["formatted_output"] = format_output(result)
    
    # Add tokenized output
    result["tokens"] = tokenize_output(result)
    
    # Add branding footer
    result["branding"] = "Powered by pyDefine ● Created by Yahya"
    
    return result


def safe_run(code: str, filename: str = "<input>", globals_dict: Optional[Dict] = None, locals_dict: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Execute Python code safely and decode any exceptions that occur.
    
    This function runs arbitrary Python code in a controlled environment,
    catches any exceptions, and returns either success or decoded error info.
    
    SECURITY WARNING: This uses exec() which can be dangerous with untrusted
    code. Only use with code from trusted sources or in sandboxed environments.
    
    Args:
        code: Python code string to execute (can be multi-line)
        filename: Name to use in traceback (default: "<input>")
        globals_dict: Global namespace for execution (optional, uses safe defaults)
        locals_dict: Local namespace for execution (optional)
        
    Returns:
        Dictionary with keys:
            - success: True if code ran without errors, False otherwise
            - result: Return value if success, None otherwise
            - output: Any printed output (captured from stdout)
            
        If error occurred, also includes all decode_traceback() fields:
            - error_type, simple_explanation, fix_suggestion, etc.
            
    Example:
        >>> result = safe_run("print(10 / 2)")
        >>> print(result['success'])  # True
        >>> result = safe_run("print(10 / 0)")
        >>> print(result['success'])  # False
        >>> print(result['simple_explanation'])
        You tried to divide a number by zero...
    """
    if not isinstance(code, str):
        return {
            "success": False,
            "error_type": "InvalidInput",
            "original_message": "Code must be a string",
            "simple_explanation": "The code input is not a valid string.",
            "fix_suggestion": "Pass a string containing Python code",
            "tags": ["invalid-input"],
            "emoji": "❓",
            "branding": "Powered by pyDefine ● Created by Yahya"
        }
    
    if not code.strip():
        return {
            "success": True,
            "result": None,
            "output": "",
            "message": "No code to execute",
            "branding": "Powered by pyDefine ● Created by Yahya"
        }
    
    # Prepare safe execution environment
    if globals_dict is None:
        # Provide a minimal safe globals dict
        globals_dict = {
            "__builtins__": {
                # Safe built-ins only
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
                "ValueError": ValueError,
                "TypeError": TypeError,
                "KeyError": KeyError,
                "IndexError": IndexError,
                "ZeroDivisionError": ZeroDivisionError,
                "NameError": NameError,
                "AttributeError": AttributeError,
                # Add more as needed, but avoid dangerous ones like open, eval, exec, __import__
            },
            "__name__": "__main__",
            "__file__": filename,
        }
    
    if locals_dict is None:
        locals_dict = {}
    
    # Capture stdout to get print output
    import io
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    
    try:
        # Compile code first to get better error messages
        compiled_code = compile(code, filename, 'exec')
        
        # Execute the compiled code
        exec(compiled_code, globals_dict, locals_dict)
        
        # Get captured output
        output = captured_output.getvalue()
        
        # Restore stdout
        sys.stdout = old_stdout
        
        # Return success result
        result = {
            "success": True,
            "result": locals_dict.get("result", None),  # If code sets a 'result' variable
            "output": output,
            "message": "Code executed successfully",
            "branding": "Powered by pyDefine ● Created by Yahya"
        }
        
        return result
        
    except Exception as e:
        # Restore stdout
        sys.stdout = old_stdout
        
        # Get the full traceback
        tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
        tb_text = ''.join(tb_lines)
        
        # Decode the exception using our decoder
        decoded = decode_traceback(tb_text)
        
        # Add success flag and captured output
        decoded["success"] = False
        decoded["output"] = captured_output.getvalue()
        
        return decoded
    
    except BaseException as e:
        # Catch system exits, keyboard interrupts, etc.
        sys.stdout = old_stdout
        
        # Still try to decode
        decoded = decode_exception(e)
        decoded["success"] = False
        decoded["output"] = captured_output.getvalue()
        
        return decoded


def decode_traceback_file(filepath: str) -> Dict[str, Any]:
    """
    Read a traceback from a file and decode it.
    
    Useful for analyzing error logs or saved traceback output.
    
    Args:
        filepath: Path to file containing traceback text
        
    Returns:
        Same as decode_traceback()
        
    Example:
        >>> result = decode_traceback_file("error.log")
        >>> print(result['simple_explanation'])
    """
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
            "branding": "Powered by pyDefine ● Created by Yahya"
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
            "branding": "Powered by pyDefine ● Created by Yahya"
        }


# Convenience function for quick debugging
def explain(exception_or_traceback: Union[Exception, str]) -> str:
    """
    Quick one-line function to get simple explanation from exception or traceback.
    
    Args:
        exception_or_traceback: Either an Exception object or traceback string
        
    Returns:
        Simple explanation string (formatted with emoji)
        
    Example:
        >>> try:
        ...     x = 10 / 0
        ... except Exception as e:
        ...     print(explain(e))
        ➗ You tried to divide a number by zero, which is impossible in math...
    """
    if isinstance(exception_or_traceback, BaseException):
        decoded = decode_exception(exception_or_traceback)
    elif isinstance(exception_or_traceback, str):
        decoded = decode_traceback(exception_or_traceback)
    else:
        return "❓ Invalid input - pass an exception object or traceback string"
    
    emoji = decoded.get("emoji", "")
    explanation = decoded.get("simple_explanation", "No explanation available")
    
    return f"{emoji} {explanation}"


# Module-level convenience for interactive use
def quick_decode(e: Exception) -> None:
    """
    Print a quick decoded explanation of an exception (interactive use).
    
    Example:
        >>> try:
        ...     bad_code()
        ... except Exception as e:
        ...     quick_decode(e)
    """
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
