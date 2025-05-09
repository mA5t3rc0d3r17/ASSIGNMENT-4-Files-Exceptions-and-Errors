# Task 1: File Reading Script
# This script reads and displays the contents of 'sample.txt' line by line

try:
    # Open the file in read mode
    fl = open("sample.txt", "r")
    # Read all lines from the file into a list
    reading_file = fl.readlines()

    print("Reading file content: ")

    # Loop through each line and print with line number
    for x in range(0, len(reading_file)):
        print("Line " + str(x+1) + ": " + reading_file[x])

    # Close the file
    fl.close()

except FileNotFoundError:
    # Handle case where file doesn't exist
    print("The file 'sample.txt' was not found.")