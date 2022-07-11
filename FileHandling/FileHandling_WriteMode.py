# File Handling Write Mode
file = open(r"C:\Users\Snehal Thakur\Desktop\PythonClass\FileHandling\file.txt","w+")
print(file)
file.write("This is 1st line\n") 
file.write("This is 2nd line\n")
file.write("This is 3rd line\n")
file.write("This is 4th line\n")
file.seek(0) # Moving cursor position at the beginning of the file
print(file.readlines())  # io.UnsupportedOperation: not readable
file.close()
