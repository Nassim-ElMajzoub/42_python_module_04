*This project has been created as part of the 42 curriculum by nel-majz.*

# Data Archivist: Digital Preservation in the Cyber Archives

## Description

**Data Archivist** is a Python project focused on mastering file operations and stream management for data engineering applications. The project builds a complete digital preservation system called "Cyber Archives" while exploring file I/O, standard streams, context managers, and error handling.

Starting with basic file reading and progressing through writing, stream management, context managers, and crisis response systems, this project demonstrates professional file handling patterns used in real-world applications.

**Project Goals:**
- Master Python's file operations (open, read, write, close)
- Learn proper resource management with context managers
- Understand the three standard data streams (stdin, stdout, stderr)
- Build fault-tolerant systems with proper error handling
- Practice defensive programming and input validation
- Develop skills in building resilient data pipelines

The project consists of 4 exercises (0-3) that progressively introduce file operation concepts, culminating in a comprehensive crisis response system demonstrating all techniques combined.

---

## Instructions

### Requirements

- **Python 3.10+**

---

## Exercise Breakdown

### Exercise 0: Ancient Text Recovery
**Concepts:** File reading, `open()` in read mode (`'r'`), `read()`, `close()`, `FileNotFoundError` handling

**Key Learning:** Programs can read data from files using `open()`, `read()`, and `close()`. Proper error handling with `except FileNotFoundError` prevents crashes when files are missing. Always close file handles after use to free system resources.

### Exercise 1: Archive Creation
**Concepts:** File writing, `open()` in write mode (`'w'`), `write()`, `OSError` handling

**Key Learning:** Write mode (`'w'`) creates new files or overwrites existing ones. `OSError` catches permission errors and other OS-level failures during file operations.

### Exercise 2: Stream Management
**Concepts:** Standard streams (`sys.stdin`, `sys.stdout`, `sys.stderr`), `input()`, stream separation

**Key Learning:** Every program has three standard streams - stdin for input, stdout for normal output, and stderr for error/alert output. `input()` is a higher-level wrapper around `sys.stdin` that displays prompts and strips newlines automatically. Separating normal output from alerts allows tools and pipelines to handle them independently.

### Exercise 3: Vault Security
**Concepts:** Context managers, `with` statement, automatic resource cleanup, RAII principle

**Key Learning:** The `with` statement is Python's context manager protocol - it guarantees files are closed automatically even if errors occur, replacing the manual `open()`/`close()` pattern. The `try` block must wrap the `with` statement so that errors during `open()` itself are also caught. This is the professional standard for all file operations.

---

## Key Programming Principles Demonstrated

### 1. **Resource Management**
- Always close files after use
- Use `with` statements as the Pythonic standard for file handling
- Prevent resource leaks that could corrupt data

### 2. **Stream Separation**
- Normal output goes to `sys.stdout`
- Error and alert output goes to `sys.stderr`
- User input comes from `sys.stdin` (via `input()`)
- Each stream serves a distinct purpose in the data flow

### 3. **Defensive Programming**
- Validate file access before processing
- Catch specific exceptions rather than bare `except`
- Handle `FileNotFoundError`, `PermissionError`, and `OSError` separately
- Provide meaningful error messages for each failure type

### 4. **Progressive Error Handling**
- Basic `try/except` for simple cases
- `with` statements for automatic resource management
- Combined `with` + `try/except` for maximum safety

---

## Technical Skills Acquired

- ✅ File reading with `open()` in read mode
- ✅ File writing with `open()` in write mode
- ✅ Proper file closure with `close()`
- ✅ Standard stream management (`sys.stdin`, `sys.stdout`, `sys.stderr`)
- ✅ User input handling with `input()`
- ✅ Context managers with the `with` statement
- ✅ Automatic resource cleanup (RAII principle)
- ✅ Exception handling (`FileNotFoundError`, `PermissionError`, `OSError`)
- ✅ Type hints on all functions
- ✅ PEP 8 compliance and professional code style

---

## Resources

### Official Documentation
- [Python Built-in Functions - open()](https://docs.python.org/3/library/functions.html#open) - File opening modes and options
- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) - Official file I/O tutorial
- [sys Module](https://docs.python.org/3/library/sys.html) - Standard streams documentation
- [Context Managers](https://docs.python.org/3/reference/compound_stmts.html#with) - The `with` statement
- [Python Exceptions](https://docs.python.org/3/library/exceptions.html) - Built-in exception types
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/) - Python coding standards

### File Operations
- [Real Python - Reading and Writing Files](https://realpython.com/read-write-files-python/) - Comprehensive file I/O guide
- [Real Python - Context Managers](https://realpython.com/python-with-statement/) - Understanding the `with` statement
- [Real Python - Exception Handling](https://realpython.com/python-exceptions/) - Exception handling patterns

### Stream Management
- [Real Python - stdin, stdout, stderr](https://realpython.com/python-subprocess/#the-standard-io-streams) - Standard streams guide
- [Unix Standard Streams](https://en.wikipedia.org/wiki/Standard_streams) - The philosophy behind stream separation

### Tools
- [flake8 Documentation](https://flake8.pycqa.org/en/latest/) - Linting tool documentation

---

## AI Usage

AI (Claude by Anthropic) was used as an **interactive learning assistant** throughout this project, following the 42 curriculum's AI guidelines.

### Tasks AI Assisted With:

#### 1. **Concept Explanation**
- **What:** Understanding file modes, stream differences, context managers, exception types
- **How:** Interactive Q&A sessions explaining when and why to use each concept
- **Which parts:** All exercises - conceptual foundation before implementation

#### 2. **Syntax Clarification**
- **What:** Correct Python syntax for `with` statements, `sys.stdout.write()`, type hints
- **How:** Learning proper patterns through targeted questions and examples
- **Which parts:** Exercises 2-3 - advanced syntax for streams and context managers

#### 3. **Debugging Guidance**
- **What:** Understanding why code wasn't working as expected
- **How:** Discussing issues like incorrect `try/with` ordering, bare `except` blocks, hardcoded values
- **Which parts:** All exercises - identifying structural and logic issues

#### 4. **Code Review**
- **What:** Feedback on implementation correctness and code quality
- **How:** Identifying issues like missing type hints, unnecessary f-strings, wrong exception types
- **Which parts:** All exercises - ensuring correct patterns and clean code

### What AI Did NOT Do:

❌ **Write complete solutions** - All code was written by me
❌ **Copy-paste implementations** - Every line was typed and understood by me
❌ **Make design decisions** - I chose approaches after understanding the options
❌ **Debug code without my analysis** - I identified issues before discussing solutions

### Learning Approach:

The AI was used as a **tutor and guide**, not a solution provider. For each exercise:
1. AI explained the concept and relevant Python mechanisms
2. I asked clarifying questions until I fully understood
3. I implemented the solution myself
4. I identified issues and asked specific questions about them
5. AI provided hints and explanations, not complete code
6. I understood and could explain every line of my implementation

This approach ensured **genuine learning** while leveraging AI as an **educational resource**, fully aligned with 42's philosophy of peer learning and deep understanding.

### Key Principle Followed:

> *"Only use AI-generated content that you fully understand and can take responsibility for."*

Every piece of code submitted represents my understanding and ability to work with Python file operations independently.

---

## Reflection

This project provided comprehensive mastery of Python's file operations and resource management patterns. Starting from basic file reading and progressing through writing, stream management, context managers, and crisis response systems, each exercise built essential skills for professional data engineering.

The Cyber Archives theme made abstract concepts concrete: reading ancient fragments demonstrated file I/O, creating new archives showed write operations, managing communication channels illustrated stream separation, vault security protocols introduced context managers, and crisis response combined everything into a fault-tolerant system.

The skills acquired here - from basic file I/O to fault-tolerant crisis response systems - form the foundation for building reliable data pipelines that handle real-world failures gracefully.

---

## Author

Nassim El Majzoub - 42 Student

*Project completed as part of the 42 programming curriculum*