"""
Example: Using safe_run() function

Demonstrates how to execute Python code safely with automatic error decoding.
"""

import pydefine

print("=" * 70)
print("pyDefine - safe_run() Examples")
print("=" * 70)
print()

# Example 1: Successful code execution
print("📝 Example 1: Successful execution")
print("-" * 70)

code1 = """
message = "Hello from pyDefine!"
print(message)
for i in range(3):
    print(f"  Count: {i + 1}")
"""

result1 = pydefine.safe_run(code1, filename="example1.py")

if result1['success']:
    print("✅ Code executed successfully!")
    print(f"Output:\n{result1['output']}")
else:
    print("❌ Error occurred")
print()

# Example 2: Code with ZeroDivisionError
print("📝 Example 2: Handling ZeroDivisionError")
print("-" * 70)

code2 = """
x = 10
y = 0
result = x / y
print(f"Result: {result}")
"""

result2 = pydefine.safe_run(code2, filename="example2.py")

if not result2['success']:
    print(f"❌ {result2['error_type']}: {result2['original_message']}")
    print(f"\n{result2['emoji']} {result2['simple_explanation']}")
    print(f"\n💡 {result2['fix_suggestion']}")
print()

# Example 3: Code with NameError
print("📝 Example 3: Handling NameError")
print("-" * 70)

code3 = """
print("Starting calculation...")
total = price * quantity  # Variables not defined
print(f"Total: {total}")
"""

result3 = pydefine.safe_run(code3, filename="example3.py")

if not result3['success']:
    print(f"{result3['emoji']} Error on line {result3['line_number']}")
    print(f"\nProblem: {result3['simple_explanation']}")
    print(f"\nSolution: {result3['fix_suggestion']}")
print()

# Example 4: Code with SyntaxError
print("📝 Example 4: Handling SyntaxError")
print("-" * 70)

code4 = """
if True
    print("Missing colon!")
"""

result4 = pydefine.safe_run(code4, filename="example4.py")

if not result4['success']:
    print(result4['formatted_output'])
print()

# Example 5: Code with TypeError
print("📝 Example 5: Handling TypeError")
print("-" * 70)

code5 = """
numbers = [1, 2, 3]
text = "Count: "
combined = text + numbers  # Can't add list to string
print(combined)
"""

result5 = pydefine.safe_run(code5, filename="example5.py")

if not result5['success']:
    print(f"Error: {result5['error_type']}")
    print(f"Explanation: {result5['simple_explanation']}")
    print(f"Fix: {result5['fix_suggestion']}")
print()

# Example 6: Code with multiple operations
print("📝 Example 6: Complex code execution")
print("-" * 70)

code6 = """
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

data = [10, 20, 30, 40, 50]
avg = calculate_average(data)
print(f"Average: {avg}")

# This will cause an error
empty_list = []
bad_avg = calculate_average(empty_list)  # Division by zero
"""

result6 = pydefine.safe_run(code6, filename="example6.py")

print(f"Success: {result6['success']}")
if result6.get('output'):
    print(f"Output before error:\n{result6['output']}")
if not result6['success']:
    print(f"\n{result6['emoji']} {result6['error_type']}")
    print(f"{result6['simple_explanation']}")
print()

# Example 7: Using custom globals
print("📝 Example 7: Custom execution environment")
print("-" * 70)

custom_globals = {
    "__builtins__": {
        "print": print,
        "len": len,
        "sum": sum,
        "range": range,
    },
    "pi": 3.14159,
    "greeting": "Welcome to pyDefine!"
}

code7 = """
print(greeting)
print(f"Pi value: {pi}")
numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum(numbers)}")
"""

result7 = pydefine.safe_run(code7, globals_dict=custom_globals, filename="example7.py")

if result7['success']:
    print("✅ Code with custom environment executed!")
    print(result7['output'])
print()

# Example 8: Comparing multiple error scenarios
print("📝 Example 8: Error comparison")
print("-" * 70)

test_cases = [
    ("Missing variable", "print(x)"),
    ("Wrong type", "'hello' + 5"),
    ("Index error", "[1,2,3][99]"),
    ("Key error", "{'a':1}['b']"),
    ("Division by zero", "10 / 0"),
]

for name, code in test_cases:
    result = pydefine.safe_run(code)
    if not result['success']:
        print(f"{result['emoji']} {name}: {result['error_type']}")

print()
print("=" * 70)
print("✨ All safe_run examples completed! ✨")
print("=" * 70)
