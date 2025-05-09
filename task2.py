# Task 2: File Writing and Appending Script
# This script writes to and appends a file, then displays the final content

try:
    # Get user input for new content
    new_line = input("Enter text to write to the file: ")
    
    # Open file in append mode and write the new content
    fl = open("output.txt", "a")
    fl.write(new_line)
    fl.close()
    print("\nData successfully written to output.txt.")
    
    # Get additional input from user
    next_line = input("\nEnter additional text to append: ")
    
    # Open file again to append the new line
    fl1 = open("output.txt", "a")
    fl1.write("\n" + next_line)
    fl1.close()
    print("\nData successfully appended.")
    
    # Open file in read mode to display final content
    fl2 = open("output.txt", "r")
    read_file = fl2.read()
    print("\nFinal content of output.txt: \n" + read_file)
    fl2.close()

except FileNotFoundError:
    # Handle case where file operations fail
    print("The file 'output.txt' was not found.")