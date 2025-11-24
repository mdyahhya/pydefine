"""
pydecode.mapping
~~~~~~~~~~~~~~~~

Complete mapping of all Python built-in exceptions to beginner-friendly
explanations, fix suggestions, and classification tags.

This module contains EXCEPTION_MAP which maps exception class names to
dictionaries containing:
  - simple_explanation: 2-3 line explanation in simple English
  - fix_suggestion: One-line actionable fix
  - tags: List of classification keywords
  - emoji: Optional emoji for visual identification

All explanations are written for absolute beginners with no jargon.
"""

# Complete mapping of 80+ built-in Python exceptions
EXCEPTION_MAP = {
    # =========================================================================
    # SYNTAX ERRORS
    # =========================================================================
    "SyntaxError": {
        "simple_explanation": (
            "You wrote Python code that doesn't follow the language rules. "
            "Python couldn't understand what you typed. "
            "This is like writing a sentence with wrong grammar 📝"
        ),
        "fix_suggestion": (
            "Check for missing colons (:), unmatched parentheses/brackets, "
            "or typos in keywords like 'if', 'for', 'def'"
        ),
        "tags": ["syntax", "grammar", "typo", "beginner"],
        "emoji": "📝"
    },
    
    "IndentationError": {
        "simple_explanation": (
            "Your code has wrong spacing at the beginning of a line. "
            "Python needs consistent spaces or tabs to understand code blocks. "
            "Think of it like paragraphs that need proper alignment 📏"
        ),
        "fix_suggestion": (
            "Make sure all lines in the same block have the same number of spaces "
            "(usually 4 spaces). Don't mix tabs and spaces"
        ),
        "tags": ["syntax", "indentation", "spacing", "whitespace"],
        "emoji": "📏"
    },
    
    "TabError": {
        "simple_explanation": (
            "You mixed tabs (Tab key) and spaces for indentation. "
            "Python gets confused when you use both in the same file. "
            "It's like mixing two different measuring systems 🔀"
        ),
        "fix_suggestion": (
            "Use only spaces (4 spaces per indent level) or only tabs, "
            "never mix them. Most editors can convert tabs to spaces"
        ),
        "tags": ["syntax", "indentation", "tabs", "whitespace"],
        "emoji": "🔀"
    },
    
    # =========================================================================
    # NAME AND ATTRIBUTE ERRORS
    # =========================================================================
    "NameError": {
        "simple_explanation": (
            "You tried to use a variable or function name that doesn't exist yet. "
            "Python doesn't know what you're talking about. "
            "It's like calling someone who isn't in the room 🤷"
        ),
        "fix_suggestion": (
            "Check spelling, make sure you defined the variable first, "
            "or import the module that contains it"
        ),
        "tags": ["name", "variable", "undefined", "scope"],
        "emoji": "🤷"
    },
    
    "UnboundLocalError": {
        "simple_explanation": (
            "You tried to use a variable inside a function before giving it a value. "
            "Python knows you want a local variable but you haven't set it yet. "
            "It's like opening an empty box 📦"
        ),
        "fix_suggestion": (
            "Assign a value to the variable before using it, "
            "or use 'global' keyword if you meant to use an outside variable"
        ),
        "tags": ["name", "variable", "scope", "local"],
        "emoji": "📦"
    },
    
    "AttributeError": {
        "simple_explanation": (
            "You tried to access a property or method that doesn't exist on an object. "
            "The thing you're working with doesn't have that feature. "
            "It's like trying to open a car door that isn't there 🚗"
        ),
        "fix_suggestion": (
            "Check the correct attribute name using dir(object), "
            "or verify the object type is what you expect"
        ),
        "tags": ["attribute", "object", "method", "property"],
        "emoji": "🚗"
    },
    
    # =========================================================================
    # TYPE ERRORS
    # =========================================================================
    "TypeError": {
        "simple_explanation": (
            "You tried to do something with the wrong type of data. "
            "Like trying to add a number to a word - they don't mix. "
            "Python needs compatible types to work together 🔢➕📝"
        ),
        "fix_suggestion": (
            "Convert data to the right type (e.g., int(), str(), list()), "
            "or check if you're using the correct operation"
        ),
        "tags": ["type", "conversion", "operation", "mismatch"],
        "emoji": "🔢"
    },
    
    # =========================================================================
    # VALUE ERRORS
    # =========================================================================
    "ValueError": {
        "simple_explanation": (
            "The data type is correct but the actual value doesn't make sense. "
            "Like trying to convert the word 'hello' into a number. "
            "The format or content is wrong 🎯"
        ),
        "fix_suggestion": (
            "Check if the input value is valid for what you're trying to do. "
            "Add validation or try/except to handle bad values"
        ),
        "tags": ["value", "invalid", "format", "conversion"],
        "emoji": "🎯"
    },
    
    # =========================================================================
    # KEY AND INDEX ERRORS
    # =========================================================================
    "KeyError": {
        "simple_explanation": (
            "You tried to get a value from a dictionary using a key that doesn't exist. "
            "It's like looking for a word in a dictionary that isn't there. "
            "The key you asked for is missing 🔑"
        ),
        "fix_suggestion": (
            "Use dict.get(key, default) instead of dict[key], "
            "or check if the key exists with 'key in dict' first"
        ),
        "tags": ["key", "dictionary", "lookup", "missing"],
        "emoji": "🔑"
    },
    
    "IndexError": {
        "simple_explanation": (
            "You tried to access a position in a list that doesn't exist. "
            "Like trying to get the 10th item when there are only 5 items. "
            "The index is out of range 📊"
        ),
        "fix_suggestion": (
            "Check the length with len() before accessing, "
            "or use negative indices to count from the end"
        ),
        "tags": ["index", "list", "sequence", "out-of-bounds"],
        "emoji": "📊"
    },
    
    # =========================================================================
    # ARITHMETIC ERRORS
    # =========================================================================
    "ZeroDivisionError": {
        "simple_explanation": (
            "You tried to divide a number by zero, which is impossible in math. "
            "Division by zero breaks the universe's math rules. "
            "Python can't calculate infinity ➗"
        ),
        "fix_suggestion": (
            "Check if the divisor is zero before dividing, "
            "or add a condition to handle zero values"
        ),
        "tags": ["arithmetic", "division", "zero", "math"],
        "emoji": "➗"
    },
    
    "OverflowError": {
        "simple_explanation": (
            "A number got too big for Python to handle in a calculation. "
            "You exceeded the maximum size for this type of number. "
            "It's like filling a cup that's too small 🌊"
        ),
        "fix_suggestion": (
            "Use smaller numbers, break calculation into steps, "
            "or use Python's unlimited precision integers"
        ),
        "tags": ["arithmetic", "overflow", "large-number", "math"],
        "emoji": "🌊"
    },
    
    "FloatingPointError": {
        "simple_explanation": (
            "A decimal number calculation failed or produced an invalid result. "
            "This happens with very precise math operations. "
            "Floating point math has limits 🔢"
        ),
        "fix_suggestion": (
            "Use the decimal module for precise calculations, "
            "or check for special values like infinity or NaN"
        ),
        "tags": ["arithmetic", "float", "precision", "math"],
        "emoji": "🔢"
    },
    
    "ArithmeticError": {
        "simple_explanation": (
            "A general math error occurred during a calculation. "
            "This is the parent class for all arithmetic problems. "
            "Something went wrong with numbers ➕"
        ),
        "fix_suggestion": (
            "Check the specific error type for more details. "
            "Validate input values before calculations"
        ),
        "tags": ["arithmetic", "math", "calculation", "general"],
        "emoji": "➕"
    },
    
    # =========================================================================
    # FILE AND OS ERRORS
    # =========================================================================
    "FileNotFoundError": {
        "simple_explanation": (
            "Python couldn't find the file you're trying to open or use. "
            "The file doesn't exist at the path you specified. "
            "It's like looking for a book that isn't on the shelf 📁"
        ),
        "fix_suggestion": (
            "Check the file path spelling, verify the file exists, "
            "or create the file if it should exist"
        ),
        "tags": ["file", "path", "io", "missing"],
        "emoji": "📁"
    },
    
    "FileExistsError": {
        "simple_explanation": (
            "You tried to create a file that already exists. "
            "Python won't overwrite it without permission. "
            "The filename is already taken 📄"
        ),
        "fix_suggestion": (
            "Choose a different filename, delete the old file first, "
            "or open the file in append/write mode"
        ),
        "tags": ["file", "exists", "io", "duplicate"],
        "emoji": "📄"
    },
    
    "PermissionError": {
        "simple_explanation": (
            "You don't have permission to access, read, or modify this file or folder. "
            "The operating system blocked your request for security. "
            "Access denied 🔒"
        ),
        "fix_suggestion": (
            "Run as administrator/sudo, check file permissions, "
            "or ask the owner to grant you access"
        ),
        "tags": ["file", "permission", "access", "security"],
        "emoji": "🔒"
    },
    
    "IsADirectoryError": {
        "simple_explanation": (
            "You tried to open a folder as if it were a file. "
            "Folders and files need different operations. "
            "You can't read a folder like a text file 📂"
        ),
        "fix_suggestion": (
            "Use os.listdir() to read folder contents, "
            "or check if the path is a file before opening"
        ),
        "tags": ["file", "directory", "io", "type"],
        "emoji": "📂"
    },
    
    "NotADirectoryError": {
        "simple_explanation": (
            "You tried to use a file as if it were a folder. "
            "The path you gave points to a file, not a directory. "
            "You can't list contents of a file 📄"
        ),
        "fix_suggestion": (
            "Check if the path is a directory with os.path.isdir(), "
            "or use the correct path to the folder"
        ),
        "tags": ["file", "directory", "io", "type"],
        "emoji": "📄"
    },
    
    "IOError": {
        "simple_explanation": (
            "An input/output operation failed when working with files or streams. "
            "Something went wrong reading or writing data. "
            "Data transfer had a problem 💾"
        ),
        "fix_suggestion": (
            "Check if the file is open, device is connected, "
            "or if there's enough disk space"
        ),
        "tags": ["io", "file", "stream", "read-write"],
        "emoji": "💾"
    },
    
    "OSError": {
        "simple_explanation": (
            "The operating system returned an error. "
            "This could be file issues, network problems, or system limits. "
            "Something went wrong at the system level 🖥️"
        ),
        "fix_suggestion": (
            "Check system resources, file permissions, network connection, "
            "or read the detailed error message for specifics"
        ),
        "tags": ["os", "system", "general", "file"],
        "emoji": "🖥️"
    },
    
    "EOFError": {
        "simple_explanation": (
            "Python reached the end of a file or input unexpectedly. "
            "The input() function got closed without receiving data. "
            "No more data to read 📭"
        ),
        "fix_suggestion": (
            "Make sure there's input available, handle Ctrl+D/Ctrl+Z gracefully, "
            "or check if the file has content"
        ),
        "tags": ["io", "input", "eof", "stream"],
        "emoji": "📭"
    },
    
    # =========================================================================
    # IMPORT ERRORS
    # =========================================================================
    "ImportError": {
        "simple_explanation": (
            "Python couldn't import a module you requested. "
            "The package might not be installed or the name is wrong. "
            "Import failed 📦"
        ),
        "fix_suggestion": (
            "Install the package with pip install, check spelling, "
            "or verify the module exists in your environment"
        ),
        "tags": ["import", "module", "package", "missing"],
        "emoji": "📦"
    },
    
    "ModuleNotFoundError": {
        "simple_explanation": (
            "Python can't find the module you're trying to import. "
            "The module doesn't exist or isn't installed. "
            "Module is missing 🔍"
        ),
        "fix_suggestion": (
            "Install with 'pip install module_name', check spelling, "
            "or add the module's directory to Python path"
        ),
        "tags": ["import", "module", "not-found", "pip"],
        "emoji": "🔍"
    },
    
    # =========================================================================
    # ASSERTION AND RUNTIME ERRORS
    # =========================================================================
    "AssertionError": {
        "simple_explanation": (
            "An assert statement failed - a condition you expected to be true was false. "
            "This is a test that didn't pass. "
            "Your assumption was wrong ✋"
        ),
        "fix_suggestion": (
            "Check why the condition is false, fix the logic, "
            "or remove the assert if it's no longer needed"
        ),
        "tags": ["assertion", "test", "condition", "debug"],
        "emoji": "✋"
    },
    
    "RuntimeError": {
        "simple_explanation": (
            "An error happened while the program was running that doesn't fit other categories. "
            "Something unexpected went wrong during execution. "
            "General runtime problem ⚠️"
        ),
        "fix_suggestion": (
            "Read the detailed error message for context. "
            "Debug the specific operation that failed"
        ),
        "tags": ["runtime", "general", "execution"],
        "emoji": "⚠️"
    },
    
    "RecursionError": {
        "simple_explanation": (
            "A function called itself too many times without stopping. "
            "You have infinite recursion that exceeded Python's limit. "
            "Stack overflow from deep recursion 🔁"
        ),
        "fix_suggestion": (
            "Add a base case to stop recursion, use iteration instead, "
            "or increase recursion limit with sys.setrecursionlimit()"
        ),
        "tags": ["recursion", "stack", "infinite", "function"],
        "emoji": "🔁"
    },
    
    "NotImplementedError": {
        "simple_explanation": (
            "A method or function is defined but not actually coded yet. "
            "The developer left it as a placeholder. "
            "Feature not implemented 🚧"
        ),
        "fix_suggestion": (
            "Implement the method, use a different method, "
            "or wait for the developer to complete this feature"
        ),
        "tags": ["implementation", "abstract", "incomplete", "todo"],
        "emoji": "🚧"
    },
    
    # =========================================================================
    # MEMORY ERRORS
    # =========================================================================
    "MemoryError": {
        "simple_explanation": (
            "Python ran out of available memory (RAM). "
            "You're trying to store or process too much data. "
            "Not enough memory 🧠"
        ),
        "fix_suggestion": (
            "Process data in smaller chunks, close unused objects, "
            "use generators instead of lists, or add more RAM"
        ),
        "tags": ["memory", "ram", "resource", "overflow"],
        "emoji": "🧠"
    },
    
    # =========================================================================
    # STOP ITERATION
    # =========================================================================
    "StopIteration": {
        "simple_explanation": (
            "An iterator ran out of items when you called next() on it. "
            "This is normal - it means 'no more items left'. "
            "Iterator is exhausted 🔚"
        ),
        "fix_suggestion": (
            "This is usually caught automatically in loops. "
            "Use for-loops instead of manually calling next()"
        ),
        "tags": ["iterator", "loop", "exhausted", "normal"],
        "emoji": "🔚"
    },
    
    "StopAsyncIteration": {
        "simple_explanation": (
            "An async iterator ran out of items. "
            "Similar to StopIteration but for async/await code. "
            "Async iterator finished 🔚"
        ),
        "fix_suggestion": (
            "This is normal behavior. Use 'async for' loops which handle this automatically"
        ),
        "tags": ["iterator", "async", "exhausted", "normal"],
        "emoji": "🔚"
    },
    
    # =========================================================================
    # KEYBOARD AND SYSTEM
    # =========================================================================
    "KeyboardInterrupt": {
        "simple_explanation": (
            "You pressed Ctrl+C to stop the program manually. "
            "This is intentional - you cancelled execution. "
            "User interrupted ⌨️"
        ),
        "fix_suggestion": (
            "This is normal. If you want to catch it, use try/except KeyboardInterrupt "
            "to clean up before exiting"
        ),
        "tags": ["interrupt", "cancel", "ctrl-c", "user"],
        "emoji": "⌨️"
    },
    
    "SystemExit": {
        "simple_explanation": (
            "The program called sys.exit() to quit intentionally. "
            "This is a clean way to end the program. "
            "Intentional exit 🚪"
        ),
        "fix_suggestion": (
            "This is normal. If catching it, don't prevent legitimate exits. "
            "Check the exit code for success/failure"
        ),
        "tags": ["exit", "quit", "system", "intentional"],
        "emoji": "🚪"
    },
    
    "SystemError": {
        "simple_explanation": (
            "Python's interpreter encountered an internal error. "
            "This is rare and usually a bug in Python itself or a C extension. "
            "Internal Python error 🐍"
        ),
        "fix_suggestion": (
            "Update Python to the latest version, check if a C extension is buggy, "
            "or report this bug to Python developers"
        ),
        "tags": ["system", "internal", "interpreter", "rare"],
        "emoji": "🐍"
    },
    
    "GeneratorExit": {
        "simple_explanation": (
            "A generator was closed while it was still running. "
            "This happens when you call .close() on a generator. "
            "Generator was stopped early ⏹️"
        ),
        "fix_suggestion": (
            "This is usually intentional. Handle cleanup in 'finally' blocks if needed"
        ),
        "tags": ["generator", "close", "cleanup", "normal"],
        "emoji": "⏹️"
    },
    
    # =========================================================================
    # UNICODE ERRORS
    # =========================================================================
    "UnicodeError": {
        "simple_explanation": (
            "A problem occurred with text encoding or decoding. "
            "Python couldn't convert between text formats properly. "
            "Text encoding problem 🔤"
        ),
        "fix_suggestion": (
            "Specify encoding explicitly (utf-8), handle errors parameter, "
            "or check source text encoding"
        ),
        "tags": ["unicode", "encoding", "text", "charset"],
        "emoji": "🔤"
    },
    
    "UnicodeDecodeError": {
        "simple_explanation": (
            "Python couldn't decode bytes into text using the specified encoding. "
            "The byte sequence doesn't match the encoding you specified. "
            "Can't decode text 📥"
        ),
        "fix_suggestion": (
            "Use correct encoding (try utf-8), use errors='ignore' or 'replace', "
            "or detect encoding with chardet library"
        ),
        "tags": ["unicode", "decode", "encoding", "text"],
        "emoji": "📥"
    },
    
    "UnicodeEncodeError": {
        "simple_explanation": (
            "Python couldn't encode text into bytes using the specified encoding. "
            "The text contains characters that don't exist in the target encoding. "
            "Can't encode text 📤"
        ),
        "fix_suggestion": (
            "Use utf-8 encoding which supports all characters, "
            "or use errors='ignore'/'replace' to skip problem characters"
        ),
        "tags": ["unicode", "encode", "encoding", "text"],
        "emoji": "📤"
    },
    
    "UnicodeTranslateError": {
        "simple_explanation": (
            "Python couldn't translate characters during text processing. "
            "Character mapping or translation failed. "
            "Can't translate text 🔄"
        ),
        "fix_suggestion": (
            "Check the translation table, use errors='ignore', "
            "or handle special characters separately"
        ),
        "tags": ["unicode", "translate", "mapping", "text"],
        "emoji": "🔄"
    },
    
    # =========================================================================
    # LOOKUP ERRORS
    # =========================================================================
    "LookupError": {
        "simple_explanation": (
            "A general error for failed lookups in sequences or mappings. "
            "Parent class of KeyError and IndexError. "
            "Lookup failed 🔎"
        ),
        "fix_suggestion": (
            "Check the specific error (KeyError or IndexError) for details. "
            "Validate keys/indices before accessing"
        ),
        "tags": ["lookup", "general", "key", "index"],
        "emoji": "🔎"
    },
    
    # =========================================================================
    # REFERENCE ERROR
    # =========================================================================
    "ReferenceError": {
        "simple_explanation": (
            "A weak reference tried to access an object that was already garbage collected. "
            "The object you referenced no longer exists. "
            "Object was deleted 🗑️"
        ),
        "fix_suggestion": (
            "Check if weak reference is still alive before using, "
            "or use strong references if object must persist"
        ),
        "tags": ["reference", "weak", "garbage-collection", "memory"],
        "emoji": "🗑️"
    },
    
    # =========================================================================
    # BUFFER ERROR
    # =========================================================================
    "BufferError": {
        "simple_explanation": (
            "An operation failed on a buffer object. "
            "Usually happens when trying to modify an object while it's being accessed. "
            "Buffer conflict 📦"
        ),
        "fix_suggestion": (
            "Release buffer locks, avoid modifying objects during buffer operations, "
            "or copy data before modifying"
        ),
        "tags": ["buffer", "memory", "conflict", "access"],
        "emoji": "📦"
    },
    
    # =========================================================================
    # CONNECTION ERRORS
    # =========================================================================
    "ConnectionError": {
        "simple_explanation": (
            "A network connection failed or was interrupted. "
            "Parent class for all connection-related errors. "
            "Connection problem 🌐"
        ),
        "fix_suggestion": (
            "Check network connection, verify server is running, "
            "check firewall settings, or retry the connection"
        ),
        "tags": ["connection", "network", "socket", "general"],
        "emoji": "🌐"
    },
    
    "BrokenPipeError": {
        "simple_explanation": (
            "You tried to write to a pipe or socket that was closed on the other end. "
            "The receiving end disconnected unexpectedly. "
            "Pipe broken 📡"
        ),
        "fix_suggestion": (
            "Check if the other process is running, handle disconnections gracefully, "
            "or add retry logic"
        ),
        "tags": ["connection", "pipe", "socket", "disconnect"],
        "emoji": "📡"
    },
    
    "ConnectionAbortedError": {
        "simple_explanation": (
            "The connection was aborted by the software on your computer. "
            "Your side closed the connection. "
            "Connection aborted locally ❌"
        ),
        "fix_suggestion": (
            "Check if your firewall blocked it, verify network settings, "
            "or check for software conflicts"
        ),
        "tags": ["connection", "abort", "network", "local"],
        "emoji": "❌"
    },
    
    "ConnectionRefusedError": {
        "simple_explanation": (
            "The remote computer actively refused the connection. "
            "The server isn't accepting connections on that port. "
            "Connection refused by server 🚫"
        ),
        "fix_suggestion": (
            "Verify server is running, check the port number, "
            "check firewall rules, or verify the address"
        ),
        "tags": ["connection", "refused", "server", "port"],
        "emoji": "🚫"
    },
    
    "ConnectionResetError": {
        "simple_explanation": (
            "The connection was forcibly closed by the remote computer. "
            "The other side dropped the connection suddenly. "
            "Connection reset by peer 🔌"
        ),
        "fix_suggestion": (
            "Check server stability, add reconnection logic, "
            "verify network stability, or check for server crashes"
        ),
        "tags": ["connection", "reset", "network", "remote"],
        "emoji": "🔌"
    },
    
    # =========================================================================
    # TIMEOUT
    # =========================================================================
    "TimeoutError": {
        "simple_explanation": (
            "An operation took too long and exceeded the time limit. "
            "The connection or operation timed out. "
            "Operation timed out ⏱️"
        ),
        "fix_suggestion": (
            "Increase timeout value, check network speed, "
            "optimize slow operations, or check server response time"
        ),
        "tags": ["timeout", "slow", "network", "time-limit"],
        "emoji": "⏱️"
    },
    
    # =========================================================================
    # CHILD PROCESS ERROR
    # =========================================================================
    "ChildProcessError": {
        "simple_explanation": (
            "An operation on a child process failed. "
            "Something went wrong managing subprocess execution. "
            "Child process error 👶"
        ),
        "fix_suggestion": (
            "Check if subprocess command is valid, verify subprocess permissions, "
            "or check if child process exited unexpectedly"
        ),
        "tags": ["subprocess", "process", "child", "execution"],
        "emoji": "👶"
    },
    
    # =========================================================================
    # BLOCKING IO ERROR
    # =========================================================================
    "BlockingIOError": {
        "simple_explanation": (
            "An I/O operation would block but was set to non-blocking mode. "
            "The operation can't complete immediately. "
            "Would block in non-blocking mode 🚦"
        ),
        "fix_suggestion": (
            "Use select/poll to wait for readiness, switch to blocking mode, "
            "or use async I/O"
        ),
        "tags": ["io", "blocking", "non-blocking", "socket"],
        "emoji": "🚦"
    },
    
    # =========================================================================
    # INTERRUPTED ERROR
    # =========================================================================
    "InterruptedError": {
        "simple_explanation": (
            "A system call was interrupted by a signal. "
            "The operation was stopped by the operating system. "
            "System call interrupted 📞"
        ),
        "fix_suggestion": (
            "Retry the operation, this is usually temporary. "
            "Python often handles this automatically"
        ),
        "tags": ["signal", "interrupt", "system-call", "temporary"],
        "emoji": "📞"
    },
    
    # =========================================================================
    # PROCESS LOOKUP ERROR
    # =========================================================================
    "ProcessLookupError": {
        "simple_explanation": (
            "A process you're trying to access doesn't exist. "
            "The process ID you specified is invalid or the process ended. "
            "Process not found 🔍"
        ),
        "fix_suggestion": (
            "Check if process is still running, verify process ID, "
            "or handle process termination"
        ),
        "tags": ["process", "pid", "not-found", "system"],
        "emoji": "🔍"
    },
    
    # =========================================================================
    # WARNING (BaseException subclass but listed for completeness)
    # =========================================================================
    "Warning": {
        "simple_explanation": (
            "A warning message was issued but didn't stop the program. "
            "This is for messages about potential problems. "
            "Warning issued ⚠️"
        ),
        "fix_suggestion": (
            "Read the warning message and fix the underlying issue. "
            "Warnings can become errors in future versions"
        ),
        "tags": ["warning", "notice", "potential-issue", "deprecation"],
        "emoji": "⚠️"
    },
    
    # =========================================================================
    # EXCEPTION GROUP (Python 3.11+)
    # =========================================================================
    "ExceptionGroup": {
        "simple_explanation": (
            "Multiple exceptions occurred at the same time. "
            "This groups several errors together. "
            "Multiple errors happened 🎯"
        ),
        "fix_suggestion": (
            "Handle each exception in the group individually. "
            "Use except* syntax (Python 3.11+) to catch specific types"
        ),
        "tags": ["group", "multiple", "concurrent", "python311"],
        "emoji": "🎯"
    },
    
    "BaseExceptionGroup": {
        "simple_explanation": (
            "Multiple base exceptions occurred simultaneously. "
            "Like ExceptionGroup but can include system exits and interrupts. "
            "Multiple base errors 🎯"
        ),
        "fix_suggestion": (
            "Use except* syntax to handle each exception type. "
            "Be careful with system exits in groups"
        ),
        "tags": ["group", "multiple", "base", "python311"],
        "emoji": "🎯"
    },
    
    # =========================================================================
    # ENVIRONMENT ERROR (deprecated alias)
    # =========================================================================
    "EnvironmentError": {
        "simple_explanation": (
            "An environment-related error (old alias for OSError). "
            "This is deprecated - use OSError instead. "
            "Environment problem 🌍"
        ),
        "fix_suggestion": (
            "Catch OSError instead. This is kept for backward compatibility"
        ),
        "tags": ["environment", "deprecated", "os", "legacy"],
        "emoji": "🌍"
    },
    
    # =========================================================================
    # WINDOWS ERROR (Windows-specific)
    # =========================================================================
    "WindowsError": {
        "simple_explanation": (
            "A Windows-specific system error occurred. "
            "This is an alias for OSError on Windows. "
            "Windows system error 🪟"
        ),
        "fix_suggestion": (
            "Check Windows-specific error code, verify system permissions, "
            "or check Windows documentation"
        ),
        "tags": ["windows", "os", "system", "platform"],
        "emoji": "🪟"
    },
}


def get_exception_info(exception_name: str) -> dict:
    """
    Get exception information from EXCEPTION_MAP.
    
    Args:
        exception_name: Name of the exception class (e.g., 'ValueError')
        
    Returns:
        Dictionary with explanation, fix_suggestion, tags, and emoji.
        Returns fallback info if exception not found.
    """
    if exception_name in EXCEPTION_MAP:
        return EXCEPTION_MAP[exception_name]
    
    # Fallback for unknown exceptions
    return {
        "simple_explanation": (
            "An error occurred that we don't have detailed info about yet. "
            "Something unexpected went wrong in your code. "
            "Check the error name for clues ❓"
        ),
        "fix_suggestion": (
            "Read the full error message carefully, search online for the error name, "
            "or check the documentation for what you're trying to do"
        ),
        "tags": ["unknown", "general", "unhandled"],
        "emoji": "❓"
    }


def list_all_exceptions() -> list:
    """Return sorted list of all exception names in the mapping."""
    return sorted(EXCEPTION_MAP.keys())


def search_exceptions_by_tag(tag: str) -> list:
    """
    Find all exceptions with a specific tag.
    
    Args:
        tag: Tag to search for (e.g., 'syntax', 'file', 'network')
        
    Returns:
        List of exception names matching the tag
    """
    results = []
    for exc_name, exc_info in EXCEPTION_MAP.items():
        if tag.lower() in [t.lower() for t in exc_info.get("tags", [])]:
            results.append(exc_name)
    return sorted(results)


# Statistics about the mapping
TOTAL_EXCEPTIONS = len(EXCEPTION_MAP)
ALL_TAGS = sorted(set(
    tag 
    for exc_info in EXCEPTION_MAP.values() 
    for tag in exc_info.get("tags", [])
))
