"""
tests.test_mapping
~~~~~~~~~~~~~~~~~~

Test suite for pydefine.mapping module.

Tests exception mapping, search functionality, and coverage.
"""

import pytest
from pydefine.mapping import (
    get_exception_info,
    list_all_exceptions,
    search_exceptions_by_tag,
    EXCEPTION_MAP,
    TOTAL_EXCEPTIONS,
    ALL_TAGS
)


class TestExceptionMap:
    """Test EXCEPTION_MAP dictionary."""
    
    def test_map_not_empty(self):
        """Test that exception map is not empty."""
        assert len(EXCEPTION_MAP) > 0
        assert TOTAL_EXCEPTIONS > 0
    
    def test_total_exceptions_count(self):
        """Test that TOTAL_EXCEPTIONS matches actual count."""
        assert TOTAL_EXCEPTIONS == len(EXCEPTION_MAP)
        assert TOTAL_EXCEPTIONS >= 80  # Should have at least 80 exceptions
    
    def test_all_exceptions_have_required_fields(self):
        """Test that all exceptions have required fields."""
        required_fields = ['simple_explanation', 'fix_suggestion', 'tags', 'emoji']
        
        for exc_name, exc_data in EXCEPTION_MAP.items():
            for field in required_fields:
                assert field in exc_data, f"{exc_name} missing {field}"
                assert exc_data[field], f"{exc_name} has empty {field}"
    
    def test_explanations_not_empty(self):
        """Test that all explanations are non-empty."""
        for exc_name, exc_data in EXCEPTION_MAP.items():
            assert len(exc_data['simple_explanation']) > 20, f"{exc_name} explanation too short"
            assert len(exc_data['fix_suggestion']) > 10, f"{exc_name} fix too short"
    
    def test_tags_are_lists(self):
        """Test that tags are lists."""
        for exc_name, exc_data in EXCEPTION_MAP.items():
            assert isinstance(exc_data['tags'], list), f"{exc_name} tags not a list"
            assert len(exc_data['tags']) > 0, f"{exc_name} has no tags"
    
    def test_emojis_present(self):
        """Test that all exceptions have emojis."""
        for exc_name, exc_data in EXCEPTION_MAP.items():
            assert exc_data['emoji'], f"{exc_name} has no emoji"
            assert len(exc_data['emoji']) > 0


class TestCommonExceptions:
    """Test that common Python exceptions are covered."""
    
    def test_syntax_errors_present(self):
        """Test syntax-related errors."""
        syntax_errors = ['SyntaxError', 'IndentationError', 'TabError']
        for exc in syntax_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_name_errors_present(self):
        """Test name-related errors."""
        name_errors = ['NameError', 'UnboundLocalError']
        for exc in name_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_type_errors_present(self):
        """Test type-related errors."""
        assert 'TypeError' in EXCEPTION_MAP
        assert 'ValueError' in EXCEPTION_MAP
        assert 'AttributeError' in EXCEPTION_MAP
    
    def test_lookup_errors_present(self):
        """Test lookup errors."""
        lookup_errors = ['KeyError', 'IndexError', 'LookupError']
        for exc in lookup_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_arithmetic_errors_present(self):
        """Test arithmetic errors."""
        arith_errors = ['ZeroDivisionError', 'OverflowError', 'ArithmeticError']
        for exc in arith_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_file_errors_present(self):
        """Test file/IO errors."""
        file_errors = [
            'FileNotFoundError', 'FileExistsError', 'PermissionError',
            'IsADirectoryError', 'NotADirectoryError', 'IOError', 'OSError'
        ]
        for exc in file_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_import_errors_present(self):
        """Test import errors."""
        import_errors = ['ImportError', 'ModuleNotFoundError']
        for exc in import_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_runtime_errors_present(self):
        """Test runtime errors."""
        runtime_errors = ['RuntimeError', 'RecursionError', 'NotImplementedError']
        for exc in runtime_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_system_errors_present(self):
        """Test system-related errors."""
        system_errors = ['SystemError', 'SystemExit', 'KeyboardInterrupt']
        for exc in system_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_unicode_errors_present(self):
        """Test Unicode errors."""
        unicode_errors = [
            'UnicodeError', 'UnicodeDecodeError', 
            'UnicodeEncodeError', 'UnicodeTranslateError'
        ]
        for exc in unicode_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"
    
    def test_connection_errors_present(self):
        """Test connection errors."""
        conn_errors = [
            'ConnectionError', 'BrokenPipeError', 'ConnectionAbortedError',
            'ConnectionRefusedError', 'ConnectionResetError', 'TimeoutError'
        ]
        for exc in conn_errors:
            assert exc in EXCEPTION_MAP, f"{exc} not in map"


class TestGetExceptionInfo:
    """Test get_exception_info function."""
    
    def test_get_known_exception(self):
        """Test getting info for known exception."""
        info = get_exception_info('ZeroDivisionError')
        
        assert 'simple_explanation' in info
        assert 'fix_suggestion' in info
        assert 'tags' in info
        assert 'emoji' in info
        assert 'zero' in info['simple_explanation'].lower()
    
    def test_get_unknown_exception(self):
        """Test getting info for unknown exception."""
        info = get_exception_info('UnknownCustomError')
        
        assert 'simple_explanation' in info
        assert 'fix_suggestion' in info
        assert 'unknown' in info['tags']
        assert info['emoji'] == '❓'
    
    def test_get_multiple_exceptions(self):
        """Test getting info for multiple exceptions."""
        exceptions = ['NameError', 'TypeError', 'FileNotFoundError']
        
        for exc in exceptions:
            info = get_exception_info(exc)
            assert info is not None
            assert len(info['simple_explanation']) > 0


class TestListAllExceptions:
    """Test list_all_exceptions function."""
    
    def test_list_returns_list(self):
        """Test that function returns a list."""
        exceptions = list_all_exceptions()
        assert isinstance(exceptions, list)
    
    def test_list_not_empty(self):
        """Test that list is not empty."""
        exceptions = list_all_exceptions()
        assert len(exceptions) > 0
        assert len(exceptions) == TOTAL_EXCEPTIONS
    
    def test_list_is_sorted(self):
        """Test that list is sorted alphabetically."""
        exceptions = list_all_exceptions()
        assert exceptions == sorted(exceptions)
    
    def test_list_contains_common_exceptions(self):
        """Test that list contains common exceptions."""
        exceptions = list_all_exceptions()
        common = ['NameError', 'TypeError', 'ValueError', 'ZeroDivisionError']
        
        for exc in common:
            assert exc in exceptions


class TestSearchExceptionsByTag:
    """Test search_exceptions_by_tag function."""
    
    def test_search_by_syntax_tag(self):
        """Test searching by 'syntax' tag."""
        results = search_exceptions_by_tag('syntax')
        
        assert isinstance(results, list)
        assert len(results) > 0
        assert 'SyntaxError' in results
        assert 'IndentationError' in results
    
    def test_search_by_file_tag(self):
        """Test searching by 'file' tag."""
        results = search_exceptions_by_tag('file')
        
        assert len(results) > 0
        assert 'FileNotFoundError' in results
    
    def test_search_by_network_tag(self):
        """Test searching by 'network' tag."""
        results = search_exceptions_by_tag('network')
        
        assert isinstance(results, list)
        # Should have connection-related errors
    
    def test_search_case_insensitive(self):
        """Test that search is case-insensitive."""
        results1 = search_exceptions_by_tag('syntax')
        results2 = search_exceptions_by_tag('SYNTAX')
        results3 = search_exceptions_by_tag('Syntax')
        
        assert results1 == results2 == results3
    
    def test_search_nonexistent_tag(self):
        """Test searching for nonexistent tag."""
        results = search_exceptions_by_tag('nonexistent_tag_xyz')
        
        assert isinstance(results, list)
        assert len(results) == 0
    
    def test_results_are_sorted(self):
        """Test that search results are sorted."""
        results = search_exceptions_by_tag('syntax')
        assert results == sorted(results)


class TestAllTags:
    """Test ALL_TAGS constant."""
    
    def test_all_tags_not_empty(self):
        """Test that ALL_TAGS is not empty."""
        assert len(ALL_TAGS) > 0
    
    def test_all_tags_is_list(self):
        """Test that ALL_TAGS is a list."""
        assert isinstance(ALL_TAGS, list)
    
    def test_all_tags_sorted(self):
        """Test that ALL_TAGS is sorted."""
        assert ALL_TAGS == sorted(ALL_TAGS)
    
    def test_common_tags_present(self):
        """Test that common tags are present."""
        common_tags = ['syntax', 'file', 'type', 'name', 'arithmetic']
        
        for tag in common_tags:
            assert tag in ALL_TAGS, f"Tag '{tag}' not in ALL_TAGS"
    
    def test_no_duplicate_tags(self):
        """Test that there are no duplicate tags."""
        assert len(ALL_TAGS) == len(set(ALL_TAGS))


class TestExplanationQuality:
    """Test quality of explanations."""
    
    def test_explanations_beginner_friendly(self):
        """Test that explanations avoid jargon."""
        # Words to avoid in beginner explanations
        jargon_words = ['instantiate', 'polymorphism', 'encapsulation']
        
        for exc_name, exc_data in EXCEPTION_MAP.items():
            explanation = exc_data['simple_explanation'].lower()
            for jargon in jargon_words:
                assert jargon not in explanation, f"{exc_name} uses jargon: {jargon}"
    
    def test_explanations_have_analogies(self):
        """Test that explanations use analogies (like/as)."""
        explanations_with_analogies = 0
        
        for exc_data in EXCEPTION_MAP.values():
            explanation = exc_data['simple_explanation']
            if "like" in explanation.lower() or "as if" in explanation.lower():
                explanations_with_analogies += 1
        
        # At least 30% should have analogies
        percentage = (explanations_with_analogies / TOTAL_EXCEPTIONS) * 100
        assert percentage >= 30, f"Only {percentage:.1f}% have analogies"
    
    def test_fix_suggestions_actionable(self):
        """Test that fix suggestions are actionable."""
        for exc_name, exc_data in EXCEPTION_MAP.items():
            fix = exc_data['fix_suggestion'].lower()
            # Should contain action words
            action_words = ['check', 'use', 'install', 'add', 'remove', 'verify', 'make sure']
            has_action = any(word in fix for word in action_words)
            assert has_action, f"{exc_name} fix suggestion not actionable"


# Run tests if executed directly
if __name__ == '__main__':
    pytest.main([__file__, '-v'])
