"""
pydefine.cli
~~~~~~~~~~~~

Command-line interface for pyDefine library.

Provides the 'pydefine-run' command to execute Python files with
automatic error decoding and beginner-friendly explanations.

Usage:
    pydefine-run script.py
    pydefine-run --help
"""

import sys
import argparse
from pathlib import Path
from typing import Optional

from .core import safe_run, decode_traceback_file, decode_exception
from .version import __version__, LIBRARY_NAME
from .mapping import list_all_exceptions, search_exceptions_by_tag, TOTAL_EXCEPTIONS


def run_file(filepath: str, verbose: bool = False) -> int:
    """
    Execute a Python file with error decoding.
    
    Args:
        filepath: Path to Python file to execute
        verbose: Show detailed output
        
    Returns:
        Exit code (0 for success, 1 for error)
    """
    file_path = Path(filepath)
    
    if not file_path.exists():
        print(f"❌ Error: File '{filepath}' not found")
        print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya ")
        return 1
    
    if not file_path.suffix == '.py':
        print(f"⚠️  Warning: File '{filepath}' doesn't have .py extension")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya ")
        return 1
    
    print(f"🚀 Running: {filepath}")
    print("─" * 70)
    
    # Run the code
    result = safe_run(code, filename=str(file_path))
    
    if result['success']:
        # Success
        if result.get('output'):
            print(result['output'], end='')
        print("\n" + "─" * 70)
        print("✅ Code executed successfully!")
        if verbose:
            print(f"📊 Exit code: 0")
        print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya ")
        return 0
    else:
        # Error occurred
        if result.get('output'):
            print(result['output'], end='')
        
        print("\n" + "=" * 70)
        print(f"❌ ERROR DETECTED")
        print("=" * 70)
        print()
        
        # Print decoded error
        emoji = result.get('emoji', '❓')
        error_type = result.get('error_type', 'UnknownError')
        original_msg = result.get('original_message', '')
        
        print(f"{emoji} {error_type}")
        if original_msg:
            print(f"   Original message: {original_msg}")
        print()
        
        print("📖 What happened:")
        explanation = result.get('simple_explanation', 'No explanation available')
        for line in explanation.split('. '):
            if line.strip():
                print(f"   • {line.strip()}.")
        print()
        
        print("💡 How to fix:")
        fix = result.get('fix_suggestion', 'No suggestion available')
        print(f"   {fix}")
        print()
        
        if result.get('line_number') or result.get('file_name'):
            print("📍 Error location:")
            if result.get('file_name'):
                print(f"   File: {result['file_name']}")
            if result.get('line_number'):
                print(f"   Line: {result['line_number']}")
            print()
        
        if verbose and result.get('tags'):
            print(f"🏷️  Tags: {', '.join(result['tags'])}")
            print()
        
        print("─" * 70)
        print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya")
        return 1


def list_exceptions_command(tag: Optional[str] = None) -> int:
    """
    List all supported exceptions.
    
    Args:
        tag: Optional tag to filter by
        
    Returns:
        Exit code (always 0)
    """
    print(f"📚 {LIBRARY_NAME} - Supported Exceptions")
    print("=" * 70)
    
    if tag:
        exceptions = search_exceptions_by_tag(tag)
        print(f"\n🏷️  Exceptions with tag '{tag}': {len(exceptions)}")
        print()
        for exc in exceptions:
            print(f"  • {exc}")
    else:
        exceptions = list_all_exceptions()
        print(f"\n✅ Total exceptions supported: {TOTAL_EXCEPTIONS}")
        print()
        print("Common exceptions:")
        common = [
            'SyntaxError', 'IndentationError', 'NameError', 'TypeError',
            'ValueError', 'KeyError', 'IndexError', 'ZeroDivisionError',
            'AttributeError', 'FileNotFoundError', 'ImportError', 'ModuleNotFoundError'
        ]
        for exc in common:
            print(f"  • {exc}")
        
        print(f"\n... and {TOTAL_EXCEPTIONS - len(common)} more!")
        print("\nUse --list-all to see complete list")
    
    print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya ")
    return 0


def list_all_exceptions_command() -> int:
    """List all exceptions in detail."""
    print(f"📚 {LIBRARY_NAME} - All Supported Exceptions")
    print("=" * 70)
    print()
    
    exceptions = list_all_exceptions()
    
    # Group by category
    from .utils import get_error_category
    
    categories = {}
    for exc in exceptions:
        cat = get_error_category(exc)
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(exc)
    
    for category, exc_list in sorted(categories.items()):
        print(f"📂 {category} ({len(exc_list)} exceptions)")
        for exc in sorted(exc_list):
            print(f"   • {exc}")
        print()
    
    print(f"✅ Total: {TOTAL_EXCEPTIONS} exceptions")
    print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya")
    return 0


def decode_log_command(filepath: str) -> int:
    """
    Decode a traceback from a log file.
    
    Args:
        filepath: Path to log file containing traceback
        
    Returns:
        Exit code
    """
    print(f"📖 Decoding traceback from: {filepath}")
    print("─" * 70)
    
    result = decode_traceback_file(filepath)
    
    if not result.get('success', True):
        # Print decoded error
        print(result.get('formatted_output', 'Could not decode traceback'))
        return 1
    else:
        print("✅ File decoded successfully")
        return 0


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog='pydefine',
        description=f'{LIBRARY_NAME} - Convert Python errors into beginner-friendly explanations',
        epilog='Created by Yahya | https://github.com/mdyahhya/pydefine'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'{LIBRARY_NAME} {__version__}'
    )
    
    parser.add_argument(
        'file',
        nargs='?',
        help='Python file to execute with error decoding'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show verbose output'
    )
    
    parser.add_argument(
        '--list',
        action='store_true',
        help='List common supported exceptions'
    )
    
    parser.add_argument(
        '--list-all',
        action='store_true',
        help='List all supported exceptions with categories'
    )
    
    parser.add_argument(
        '--tag',
        type=str,
        help='Filter exceptions by tag (use with --list)'
    )
    
    parser.add_argument(
        '--decode-log',
        type=str,
        metavar='FILE',
        help='Decode a traceback from a log file'
    )
    
    args = parser.parse_args()
    
    # Handle different commands
    if args.list_all:
        return list_all_exceptions_command()
    
    if args.list:
        return list_exceptions_command(args.tag)
    
    if args.decode_log:
        return decode_log_command(args.decode_log)
    
    if args.file:
        return run_file(args.file, verbose=args.verbose)
    
    # No file provided, show help
    parser.print_help()
    print(f"\n Powered by {LIBRARY_NAME} ● Created by Yahya ")
    return 0


if __name__ == '__main__':
    sys.exit(main())
