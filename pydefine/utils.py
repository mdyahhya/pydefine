"""
pydefine.utils
~~~~~~~~~~~~~~

Utility functions for parsing tracebacks, extracting error information,
formatting output, and tokenizing for rich display.

These are helper functions used by core.py and other modules.
"""

import re
import sys
from typing import Dict, Any, List, Optional, Tuple


def extract_error_info(traceback_text: str) -> Dict[str, Any]:
    """
    Extract structured information from a raw traceback string.
    
    Parses the traceback to extract:
    - Error type (exception class name)
    - Original error message
    - Line number where error occurred
    - File name where error occurred
    - Full traceback frames
    
    Args:
        traceback_text: Raw traceback string (multi-line)
        
    Returns:
        Dictionary with extracted information
        
    Example:
        >>> tb = '''Traceback (most recent call last):
        ...   File "test.py", line 10, in <module>
        ...     x = 1/0
        ... ZeroDivisionError: division by zero'''
        >>> info = extract_error_info(tb)
        >>> info['error_type']
        'ZeroDivisionError'
        >>> info['line_number']
        10
    """
    result = {
        "error_type": "UnknownError",
        "original_message": "",
        "line_number": None,
        "file_name": None,
        "frames": []
    }
    
    if not traceback_text:
        return result
    
    lines = traceback_text.strip().split('\n')
    
    # Last line usually contains the error type and message
    # Format: "ExceptionName: error message" or just "ExceptionName"
    last_line = lines[-1].strip() if lines else ""
    
    if ':' in last_line:
        # Split on first colon only
        error_parts = last_line.split(':', 1)
        result["error_type"] = error_parts[0].strip()
        result["original_message"] = error_parts[1].strip() if len(error_parts) > 1 else ""
    else:
        # Just error type, no message
        result["error_type"] = last_line.strip()
        result["original_message"] = ""
    
    # Extract file and line information
    # Pattern: File "filename.py", line 123, in function_name
    file_line_pattern = r'File "([^"]+)", line (\d+)'
    
    for line in lines:
        match = re.search(file_line_pattern, line)
        if match:
            file_name = match.group(1)
            line_number = int(match.group(2))
            
            # The last occurrence is where the error happened
            result["file_name"] = file_name
            result["line_number"] = line_number
            
            result["frames"].append({
                "file": file_name,
                "line": line_number,
                "text": line.strip()
            })
    
    # Handle SyntaxError special case (has additional info)
    if result["error_type"] == "SyntaxError":
        # SyntaxError often has the file/line in a different format
        for i, line in enumerate(lines):
            if line.strip().startswith('File "'):
                match = re.search(r'File "([^"]+)", line (\d+)', line)
                if match:
                    result["file_name"] = match.group(1)
                    result["line_number"] = int(match.group(2))
    
    return result


def format_output(decoded_info: Dict[str, Any]) -> str:
    """
    Format decoded error information into a human-readable string.
    
    Creates a nicely formatted output with emoji, explanations, and fixes.
    
    Args:
        decoded_info: Dictionary from decode_traceback() or decode_exception()
        
    Returns:
        Formatted string ready to print
        
    Example:
        >>> info = decode_exception(some_error)
        >>> print(format_output(info))
    """
    lines = []
    
    # Header
    lines.append("=" * 70)
    emoji = decoded_info.get("emoji", "❓")
    error_type = decoded_info.get("error_type", "UnknownError")
    original_msg = decoded_info.get("original_message", "")
    
    if original_msg:
        lines.append(f"{emoji} {error_type}: {original_msg}")
    else:
        lines.append(f"{emoji} {error_type}")
    
    lines.append("=" * 70)
    lines.append("")
    
    # Simple explanation
    explanation = decoded_info.get("simple_explanation", "No explanation available.")
    lines.append("📖 What happened:")
    lines.append(f"   {explanation}")
    lines.append("")
    
    # Fix suggestion
    fix_suggestion = decoded_info.get("fix_suggestion", "No suggestion available.")
    lines.append("💡 How to fix:")
    lines.append(f"   {fix_suggestion}")
    lines.append("")
    
    # Location information
    line_num = decoded_info.get("line_number")
    file_name = decoded_info.get("file_name")
    
    if line_num or file_name:
        lines.append("📍 Where:")
        if file_name:
            lines.append(f"   File: {file_name}")
        if line_num:
            lines.append(f"   Line: {line_num}")
        lines.append("")
    
    # Tags
    tags = decoded_info.get("tags", [])
    if tags:
        lines.append(f"🏷️  Tags: {', '.join(tags)}")
        lines.append("")
    
    # Branding
    branding = decoded_info.get("branding", "Powered by pyDefine ● Created by Yahya")
    lines.append("─" * 70)
    lines.append(f"✨ {branding} ✨")
    lines.append("=" * 70)
    
    return "\n".join(lines)


def tokenize_output(decoded_info: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    Convert decoded error info into tokens for rich display.
    
    Tokens can include special markers like [IMG:url] and [AUDIO:url]
    for future rich rendering in web interfaces.
    
    Args:
        decoded_info: Dictionary from decode_traceback() or decode_exception()
        
    Returns:
        List of token dictionaries with 'type' and 'content' keys
        
    Example:
        >>> info = decode_exception(some_error)
        >>> tokens = tokenize_output(info)
        >>> for token in tokens:
        ...     print(f"{token['type']}: {token['content']}")
    """
    tokens = []
    
    # Emoji token
    emoji = decoded_info.get("emoji", "❓")
    tokens.append({"type": "emoji", "content": emoji})
    
    # Error type token
    error_type = decoded_info.get("error_type", "UnknownError")
    tokens.append({"type": "error_type", "content": error_type})
    
    # Original message token
    original_msg = decoded_info.get("original_message", "")
    if original_msg:
        tokens.append({"type": "original_message", "content": original_msg})
    
    # Explanation token
    explanation = decoded_info.get("simple_explanation", "")
    if explanation:
        tokens.append({"type": "explanation", "content": explanation})
        
        # Check for special rich content markers
        # [IMG:url] for images
        img_matches = re.findall(r'\[IMG:([^\]]+)\]', explanation)
        for img_url in img_matches:
            tokens.append({"type": "image", "content": img_url})
        
        # [AUDIO:url] for audio
        audio_matches = re.findall(r'\[AUDIO:([^\]]+)\]', explanation)
        for audio_url in audio_matches:
            tokens.append({"type": "audio", "content": audio_url})
    
    # Fix suggestion token
    fix_suggestion = decoded_info.get("fix_suggestion", "")
    if fix_suggestion:
        tokens.append({"type": "fix_suggestion", "content": fix_suggestion})
    
    # Location tokens
    line_num = decoded_info.get("line_number")
    if line_num:
        tokens.append({"type": "line_number", "content": str(line_num)})
    
    file_name = decoded_info.get("file_name")
    if file_name:
        tokens.append({"type": "file_name", "content": file_name})
    
    # Tags token
    tags = decoded_info.get("tags", [])
    if tags:
        tokens.append({"type": "tags", "content": tags})
    
    # Branding token
    branding = decoded_info.get("branding", "Powered by pyDefine ● Created by Yahya")
    tokens.append({"type": "branding", "content": branding})
    
    return tokens


def strip_ansi_codes(text: str) -> str:
    """
    Remove ANSI color codes from text.
    
    Useful when parsing traceback from colored terminal output.
    
    Args:
        text: String potentially containing ANSI codes
        
    Returns:
        Clean text without ANSI codes
    """
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def truncate_message(message: str, max_length: int = 200) -> str:
    """
    Truncate long error messages for display.
    
    Args:
        message: Error message to truncate
        max_length: Maximum length (default: 200)
        
    Returns:
        Truncated message with ellipsis if needed
    """
    if len(message) <= max_length:
        return message
    return message[:max_length - 3] + "..."


def extract_exception_from_string(text: str) -> Optional[str]:
    """
    Try to find exception name in arbitrary text.
    
    Useful for parsing log files or mixed content.
    
    Args:
        text: Text that might contain an exception
        
    Returns:
        Exception name if found, None otherwise
    """
    # Common exception name pattern: CapitalizedWord ending in Error or Exception
    pattern = r'\b([A-Z][a-zA-Z]*(?:Error|Exception|Warning))\b'
    matches = re.findall(pattern, text)
    
    # Return the last match (most specific)
    return matches[-1] if matches else None


def get_python_version() -> str:
    """
    Get current Python version as a string.
    
    Returns:
        Python version (e.g., "3.10.5")
    """
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def is_syntax_error(error_type: str) -> bool:
    """
    Check if error type is a syntax-related error.
    
    Args:
        error_type: Name of exception class
        
    Returns:
        True if syntax-related, False otherwise
    """
    syntax_errors = [
        "SyntaxError",
        "IndentationError",
        "TabError"
    ]
    return error_type in syntax_errors


def get_error_category(error_type: str) -> str:
    """
    Categorize an error into a broad category.
    
    Args:
        error_type: Name of exception class
        
    Returns:
        Category name (e.g., "Syntax", "Type", "File", etc.)
    """
    syntax_errors = ["SyntaxError", "IndentationError", "TabError"]
    type_errors = ["TypeError", "ValueError", "AttributeError"]
    name_errors = ["NameError", "UnboundLocalError"]
    lookup_errors = ["KeyError", "IndexError", "LookupError"]
    file_errors = ["FileNotFoundError", "FileExistsError", "PermissionError", 
                   "IsADirectoryError", "NotADirectoryError", "IOError", "OSError"]
    import_errors = ["ImportError", "ModuleNotFoundError"]
    arithmetic_errors = ["ZeroDivisionError", "OverflowError", "FloatingPointError", "ArithmeticError"]
    runtime_errors = ["RuntimeError", "RecursionError", "NotImplementedError"]
    connection_errors = ["ConnectionError", "BrokenPipeError", "ConnectionAbortedError",
                        "ConnectionRefusedError", "ConnectionResetError", "TimeoutError"]
    
    if error_type in syntax_errors:
        return "Syntax"
    elif error_type in type_errors:
        return "Type"
    elif error_type in name_errors:
        return "Name"
    elif error_type in lookup_errors:
        return "Lookup"
    elif error_type in file_errors:
        return "File/IO"
    elif error_type in import_errors:
        return "Import"
    elif error_type in arithmetic_errors:
        return "Arithmetic"
    elif error_type in runtime_errors:
        return "Runtime"
    elif error_type in connection_errors:
        return "Connection"
    else:
        return "Other"


def clean_traceback_text(traceback_text: str) -> str:
    """
    Clean and normalize traceback text.
    
    Removes ANSI codes, extra whitespace, and normalizes line endings.
    
    Args:
        traceback_text: Raw traceback string
        
    Returns:
        Cleaned traceback text
    """
    # Remove ANSI codes
    cleaned = strip_ansi_codes(traceback_text)
    
    # Normalize line endings
    cleaned = cleaned.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove excessive blank lines
    lines = cleaned.split('\n')
    cleaned_lines = []
    prev_blank = False
    
    for line in lines:
        is_blank = line.strip() == ''
        if is_blank and prev_blank:
            continue  # Skip consecutive blank lines
        cleaned_lines.append(line)
        prev_blank = is_blank
    
    return '\n'.join(cleaned_lines).strip()


def highlight_code_line(code_line: str, position: Optional[int] = None) -> str:
    """
    Add visual highlighting to a code line (for error location).
    
    Args:
        code_line: Line of code
        position: Character position to highlight (optional)
        
    Returns:
        Highlighted code line with caret (^) indicator
    """
    result = [code_line]
    
    if position is not None and 0 <= position < len(code_line):
        # Add caret line
        caret_line = ' ' * position + '^'
        result.append(caret_line)
    
    return '\n'.join(result)


# Export all utility functions
__all__ = [
    'extract_error_info',
    'format_output',
    'tokenize_output',
    'strip_ansi_codes',
    'truncate_message',
    'extract_exception_from_string',
    'get_python_version',
    'is_syntax_error',
    'get_error_category',
    'clean_traceback_text',
    'highlight_code_line',
]
