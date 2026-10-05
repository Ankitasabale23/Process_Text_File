# Read and Process a Text File

## Description
This Python program reads a text file and generates basic statistics from its content.

The program calculates:
- Number of lines
- Number of words
- Number of characters

It also handles the error if the specified file does not exist.

## Objective
The objective of this program is to practice:
- File handling in Python
- Reading text files
- String processing
- Exception handling

## Tools Used
- Python
- VS Code

## Features
- Reads content from a text file
- Counts the number of lines
- Counts the number of words
- Counts the number of characters
- Handles missing files using exception handling
- Uses with open() to safely open and close the file

## How to Run

1. Create a text file named sample.txt.
2. Add some text to the file.
3. Keep sample.txt in the same folder as the Python program.
4. Open the project folder in VS Code.
5. Run the Python program.
6. Enter the name of the text file when prompted.

## Sample Input File

The sample.txt file contains:

Hello, I am learning Python.
Python is easy to learn.
File handling is an important concept.

## Sample Output

```text
===== TEXT FILE PROCESSOR =====

Enter the file name: sample.txt

===== FILE STATISTICS =====
Lines      : 3
Words      : 17
Characters : 91
=============================
## Exception Handling
If the file does not exist, the program displays a clear error message instead of stopping with a traceback.

Example:
===== TEXT FILE PROCESSOR =====

Enter the file name: abc.txt

Error: File not found. Please check the file name and try again.

## Concepts Learned
open()
with open()
File reading
read()
split()
String length using len()
Exception handling using try-except
Basic text processing

## Conclusion
This project helped me understand how to read and process text files using Python. It also improved my understanding of file handling, text statistics, and exception handling.

