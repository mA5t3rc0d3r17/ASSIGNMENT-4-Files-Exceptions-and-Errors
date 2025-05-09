# ASSIGNMENT-4-Files-Exceptions-and-Errors

# File Handling Scripts

This repository contains two Python scripts demonstrating basic file operations.

### 1. task1.py - File Reading Script

**Purpose**: Reads and displays the contents of a file named 'sample.txt' line by line with line numbers.

**Usage**:
1. Create a file named 'sample.txt' in the same directory as the script
2. Add some text content to the file
3. Run the script: `python task1.py`
4. The script will display each line with its line number

**Note**: If 'sample.txt' doesn't exist, the script will display an error message.

### 2. task2.py - File Writing and Appending Script

**Purpose**: 
- Writes user input to a file named 'output.txt'
- Appends additional user input to the same file
- Displays the final content of the file

**Usage**:
1. Run the script: `python task2.py`
2. Enter text when prompted (the script will ask twice)
3. The script will:
   - Write your first input to 'output.txt'
   - Append your second input on a new line
   - Display the final content of the file

**Note**: 
- If the file doesn't exist initially, it will be created automatically in append mode.
- Each run will append to the existing content unless you delete the file between runs.

## Requirements

- Python 3.x
- No additional libraries required
