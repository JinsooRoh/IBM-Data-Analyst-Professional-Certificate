# Writing to a file
# You can create a new text file and write data to it using Python's open() function.
# The open() function takes two main arguments: the file path (including the file name) and the mode parameter, which specifies the operation you want to perform on the file.
# For writing, you should use the mode 'w' Here's an example:
# Create a new file Example2.txt for writing
with open('Example2.txt', 'w') as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")
    # file1 is automatically closed when the 'with' block exits

# Writing multiple lines to a file using a list and loop
# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]
# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as file2:
    for line in Lines:
        file2.write(line + "\n")
    # file2 is automatically closed when the 'with' block exits

# Appending data to an existing file
# Data to append to the existing file
new_data = "This is line C"
# Open an existing file Example2.txt for appending
with open('Example2.txt', 'a') as file1:
    file1.write(new_data + "\n")
    # file1 is automatically closed when the 'with' block exits

# Copying contents from one file to another
# Open the source file for reading
with open('source.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits