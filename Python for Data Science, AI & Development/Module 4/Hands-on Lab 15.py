# Write and Save Files in Python
# Writing Files
# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
print(Lines)

# Write the strings in the list to text file
with open('/Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)

# Verify if writing to file is successfully executed
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Note that setting the mode to w overwrites all the existing data in the file.
with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Appending Files
# Write a new line to text file
with open('/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

# Verify if the new line is in the text file
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Additional Modes
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

# Let's try out the a+ mode:
with open('/Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())

# Another a+ mode:
with open('/Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )

# a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however, opening a file in w+ overwrites it and deletes all pre-existing data.
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())

# To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    # Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())

# Copy a File
# Copy file to another
# Let's copy the file Example2.txt to the file Example3.txt:
with open('/Example2.txt','r') as readfile:
    with open('/Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed
with open('/Example3.txt','r') as testwritefile:
    print(testwritefile.read())

# Exercise

"""
Your local university's Raptors fan club maintains a register of its active members on a .txt document.
Every month they update the file by removing the members who are not active.
You have been tasked with automating this with your Python skills.
Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file.
Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains )
Run the code block below prior to starting the exercise. The skeleton code has been provided for you. Edit only the cleanFiles function.

"""

# Exercise: Implement the cleanFiles function in the code cell below.¶
'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem, exMem):
    # TODO: Open the currentMem file as in r+ mode
        #TODO: Open the exMem file in a+ mode

        #TODO: Read each member in the currentMem (1 member per row) file into a list.
        # Hint: Recall that the first line in the file is the header.

        #TODO: iterate through the members and create a new list of the innactive members

        # Go to the beginning of the currentMem file
        # TODO: Iterate through the members list. 
        # If a member is inactive, add them to exMem, otherwise write them into currentMem

    pass # Remove this line when done implementation

# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = '/members.txt'
exReg = '/inactive.txt'
cleanFiles(memReg,exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
        
# Answer
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #get the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #remove header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
            The above is the same as 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            # go to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()
                
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())