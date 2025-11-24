"""
tests.test_core
~~~~~~~~~~~~~~~

Comprehensive test suite for pydefine.core module.

Tests all core functions: decode_traceback, decode_exception, safe_run, etc.
"""

import pytest
import sys
from pydefine.core import (
    decode_traceback, 
    decode_exception, 
    safe_run,
    decode_traceback_file,
    explain,
    quick_decode
)


class TestDecodeTraceback:
    """Test decode_traceback function."""
    
    def test_decode_name_error(self):
        """Test decoding a NameError traceback."""
        traceback_text = """Traceback (most recent call last):
  File "test.py", line 5, in <module>
    print(x)
NameError: name 'x' is not defined"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'NameError'
        assert result['success'] is False
        assert 'variable' in result['simple_explanation'].lower()
        assert result['line_number'] == 5
        assert result['file_name'] == 'test.py'
        assert 'name' in result['tags']
        assert result['emoji'] == '🤷'
    
    def test_decode_zero_division_error(self):
        """Test decoding a ZeroDivisionError."""
        traceback_text = """Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'ZeroDivisionError'
        assert 'divide' in result['simple_explanation'].lower()
        assert 'zero' in result['simple_explanation'].lower()
        assert result['emoji'] == '➗'
        assert 'arithmetic' in result['tags']
    
    def test_decode_syntax_error(self):
        """Test decoding a SyntaxError."""
        traceback_text = """  File "script.py", line 10
    if True
           ^
SyntaxError: invalid syntax"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'SyntaxError'
        assert 'syntax' in result['tags']
        assert result['line_number'] == 10
        assert 'grammar' in result['simple_explanation'].lower()
    
    def test_decode_file_not_found_error(self):
        """Test decoding a FileNotFoundError."""
        traceback_text = """Traceback (most recent call last):
  File "main.py", line 3, in <module>
    f = open('missing.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'FileNotFoundError'
        assert 'file' in result['tags']
        assert result['emoji'] == '📁'
        assert 'find' in result['simple_explanation'].lower()
    
    def test_decode_type_error(self):
        """Test decoding a TypeError."""
        traceback_text = """Traceback (most recent call last):
  File "test.py", line 1, in <module>
    x = '5' + 5
TypeError: can only concatenate str (not "int") to str"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'TypeError'
        assert 'type' in result['tags']
        assert 'wrong type' in result['simple_explanation'].lower()
    
    def test_decode_invalid_input(self):
        """Test with invalid input."""
        result = decode_traceback("")
        assert result['error_type'] == 'InvalidInput'
        assert result['success'] is False
        
        result = decode_traceback(None)
        assert result['error_type'] == 'InvalidInput'
    
    def test_decode_unknown_error(self):
        """Test decoding an unknown/custom error."""
        traceback_text = """Traceback (most recent call last):
  File "test.py", line 5, in <module>
    raise CustomError('test')
CustomError: test"""
        
        result = decode_traceback(traceback_text)
        
        assert result['error_type'] == 'CustomError'
        assert 'unknown' in result['tags']
        assert result['emoji'] == '❓'
    
    def test_branding_present(self):
        """Test that branding is present in result."""
        traceback_text = """Traceback (most recent call last):
  File "test.py", line 1, in <module>
    1/0
ZeroDivisionError: division by zero"""
        
        result = decode_traceback(traceback_text)
        
        assert 'branding' in result
        assert 'pyDefine' in result['branding']
        assert 'Yahya' in result['branding']
    
    def test_formatted_output_present(self):
        """Test that formatted output is generated."""
        traceback_text = """Traceback (most recent call last):
  File "test.py", line 1, in <module>
    print(undefined_var)
NameError: name 'undefined_var' is not defined"""
        
        result = decode_traceback(traceback_text)
        
        assert 'formatted_output' in result
        assert isinstance(result['formatted_output'], str)
        assert len(result['formatted_output']) > 0


class TestDecodeException:
    """Test decode_exception function."""
    
    def test_decode_zero_division_exception(self):
        """Test decoding ZeroDivisionError exception object."""
        try:
            x = 1 / 0
        except Exception as e:
            result = decode_exception(e)
            
            assert result['error_type'] == 'ZeroDivisionError'
            assert result['success'] is False
            assert 'zero' in result['simple_explanation'].lower()
    
    def test_decode_name_error_exception(self):
        """Test decoding NameError exception object."""
        try:
            print(undefined_variable)
        except Exception as e:
            result = decode_exception(e)
            
            assert result['error_type'] == 'NameError'
            assert 'variable' in result['simple_explanation'].lower()
    
    def test_decode_key_error_exception(self):
        """Test decoding KeyError exception object."""
        try:
            d = {'a': 1}
            x = d['b']
        except Exception as e:
            result = decode_exception(e)
            
            assert result['error_type'] == 'KeyError'
            assert 'dictionary' in result['simple_explanation'].lower()
            assert result['emoji'] == '🔑'
    
    def test_decode_index_error_exception(self):
        """Test decoding IndexError exception object."""
        try:
            lst = [1, 2, 3]
            x = lst[10]
        except Exception as e:
            result = decode_exception(e)
            
            assert result['error_type'] == 'IndexError'
            assert 'list' in result['simple_explanation'].lower()
    
    def test_decode_invalid_input(self):
        """Test with invalid input (not an exception)."""
        result = decode_exception("not an exception")
        
        assert result['error_type'] == 'InvalidInput'
        assert result['success'] is False
    
    def test_traceback_info_extraction(self):
        """Test that line number and file name are extracted."""
        try:
            x = 1 / 0
        except Exception as e:
            result = decode_exception(e)
            
            # Should have traceback info
            assert 'line_number' in result
            assert 'file_name' in result


class TestSafeRun:
    """Test safe_run function."""
    
    def test_safe_run_success(self):
        """Test successful code execution."""
        code = "print('Hello, World!')"
        result = safe_run(code)
        
        assert result['success'] is True
        assert 'Hello, World!' in result['output']
    
    def test_safe_run_zero_division(self):
        """Test code that raises ZeroDivisionError."""
        code = "x = 10 / 0"
        result = safe_run(code)
        
        assert result['success'] is False
        assert result['error_type'] == 'ZeroDivisionError'
        assert 'zero' in result['simple_explanation'].lower()
    
    def test_safe_run_name_error(self):
        """Test code that raises NameError."""
        code = "print(undefined_variable)"
        result = safe_run(code)
        
        assert result['success'] is False
        assert result['error_type'] == 'NameError'
    
    def test_safe_run_syntax_error(self):
        """Test code with syntax error."""
        code = "if True print('test')"
        result = safe_run(code)
        
        assert result['success'] is False
        assert result['error_type'] == 'SyntaxError'
    
    def test_safe_run_empty_code(self):
        """Test with empty code."""
        result = safe_run("")
        
        assert result['success'] is True
        assert result['output'] == ""
    
    def test_safe_run_invalid_input(self):
        """Test with invalid input type."""
        result = safe_run(123)
        
        assert result['success'] is False
        assert result['error_type'] == 'InvalidInput'
    
    def test_safe_run_multiline_code(self):
        """Test with multiline code."""
        code = """
x = 5
y = 10
print(x + y)
"""
        result = safe_run(code)
        
        assert result['success'] is True
        assert '15' in result['output']
    
    def test_safe_run_with_custom_filename(self):
        """Test safe_run with custom filename."""
        code = "x = 1 / 0"
        result = safe_run(code, filename="custom_script.py")
        
        assert result['success'] is False
        assert 'custom_script.py' in result.get('file_name', '')


class TestExplainFunction:
    """Test explain convenience function."""
    
    def test_explain_with_exception(self):
        """Test explain with exception object."""
        try:
            x = 1 / 0
        except Exception as e:
            explanation = explain(e)
            
            assert isinstance(explanation, str)
            assert '➗' in explanation
            assert 'zero' in explanation.lower()
    
    def test_explain_with_traceback_string(self):
        """Test explain with traceback string."""
        tb = """Traceback (most recent call last):
  File "test.py", line 1, in <module>
    print(x)
NameError: name 'x' is not defined"""
        
        explanation = explain(tb)
        
        assert isinstance(explanation, str)
        assert 'variable' in explanation.lower()
    
    def test_explain_with_invalid_input(self):
        """Test explain with invalid input."""
        explanation = explain(123)
        
        assert 'Invalid input' in explanation


class TestMultipleErrorTypes:
    """Test various error types comprehensively."""
    
    def test_value_error(self):
        """Test ValueError."""
        try:
            int('not a number')
        except Exception as e:
            result = decode_exception(e)
            assert result['error_type'] == 'ValueError'
            assert 'value' in result['tags']
    
    def test_attribute_error(self):
        """Test AttributeError."""
        try:
            x = "string"
            x.nonexistent_method()
        except Exception as e:
            result = decode_exception(e)
            assert result['error_type'] == 'AttributeError'
            assert result['emoji'] == '🚗'
    
    def test_import_error(self):
        """Test ImportError."""
        try:
            import nonexistent_module_xyz
        except Exception as e:
            result = decode_exception(e)
            assert result['error_type'] == 'ModuleNotFoundError'
            assert 'import' in result['tags']
    
    def test_type_error_function_call(self):
        """Test TypeError from wrong function arguments."""
        try:
            len(123)
        except Exception as e:
            result = decode_exception(e)
            assert result['error_type'] == 'TypeError'


class TestEdgeCases:
    """Test edge cases and unusual inputs."""
    
    def test_multiline_error_message(self):
        """Test error with multiline message."""
        tb = """Traceback (most recent call last):
  File "test.py", line 5, in <module>
    some_function()
  File "test.py", line 2, in some_function
    return 1/0
ZeroDivisionError: division by zero"""
        
        result = decode_traceback(tb)
        assert result['error_type'] == 'ZeroDivisionError'
        assert len(result['frames']) > 0
    
    def test_traceback_with_ansi_codes(self):
        """Test traceback with ANSI color codes (should be handled)."""
        from pydefine.utils import clean_traceback_text
        
        tb_with_ansi = "\x1b[31mTraceback (most recent call last):\x1b[0m\nNameError: test"
        cleaned = clean_traceback_text(tb_with_ansi)
        
        assert '\x1b' not in cleaned
        assert 'Traceback' in cleaned


# Run tests if executed directly
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
