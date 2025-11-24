"""
Example: Basic Usage of pyDefine

Demonstrates how to use decode_traceback and decode_exception functions.
"""

import pydefine

print("=" * 70)
print("pyDefine - Example Usage")
print("=" * 70)
print()

# Example 1: Decode a traceback string
print("📝 Example 1: Decoding a traceback string")
print("-" * 70)

traceback_text = """Traceback (most recent call last):
  File "script.py", line 10, in <module>
    result = divide_numbers(10, 0)
  File "script.py", line 5, in divide_numbers
    return a / b
ZeroDivisionError: division by zero"""

result = pydefine.decode_traceback(traceback_text)

print(f"Error Type: {result['error_type']}")
print(f"Emoji: {result['emoji']}")
print(f"\nExplanation:\n{result['simple_explanation']}")
print(f"\nHow to fix:\n{result['fix_suggestion']}")
print(f"\nLocation: Line {result['line_number']} in {result['file_name']}")
print(f"Tags: {', '.join(result['tags'])}")
print()

# Example 2: Decode an exception object directly
print("📝 Example 2: Decoding an exception object")
print("-" * 70)

try:
    my_dict = {'name': 'Alice', 'age': 25}
    print(my_dict['email'])  # Key doesn't exist
except Exception as e:
    decoded = pydefine.decode_exception(e)
    
    print(f"Error: {decoded['error_type']} {decoded['emoji']}")
    print(f"\n{decoded['simple_explanation']}")
    print(f"\n💡 Fix: {decoded['fix_suggestion']}")
print()

# Example 3: Using the explain() convenience function
print("📝 Example 3: Quick explain function")
print("-" * 70)

try:
    numbers = [1, 2, 3]
    print(numbers[10])  # Index out of range
except Exception as e:
    explanation = pydefine.explain(e)
    print(explanation)
print()

# Example 4: Handling NameError
print("📝 Example 4: NameError example")
print("-" * 70)

try:
    print(undefined_variable)
except Exception as e:
    result = pydefine.decode_exception(e)
    print(result['formatted_output'])
print()

# Example 5: Handling TypeError
print("📝 Example 5: TypeError example")
print("-" * 70)

try:
    result = "5" + 5  # Can't add string and int
except Exception as e:
    decoded = pydefine.decode_exception(e)
    print(f"{decoded['emoji']} {decoded['error_type']}")
    print(f"\nWhat happened: {decoded['simple_explanation']}")
    print(f"\nFix: {decoded['fix_suggestion']}")
print()

# Example 6: Multiple error types
print("📝 Example 6: Comparing different errors")
print("-" * 70)

errors_to_test = [
    ("1 / 0", "ZeroDivisionError"),
    ("int('abc')", "ValueError"),
    ("[1,2,3][10]", "IndexError"),
    ("undefined", "NameError"),
]

for code, expected in errors_to_test:
    try:
        eval(code)
    except Exception as e:
        result = pydefine.decode_exception(e)
        print(f"{result['emoji']} {result['error_type']}: {code}")

print()
print("=" * 70)
print("✨ All examples completed! ✨")
print("=" * 70)
