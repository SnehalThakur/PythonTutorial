# File Handling - Append Mode (It will add new lines after the text that are already present in the file)
file = open(r"C:\Users\Snehal Thakur\Desktop\PythonClass\FileHandling\file.txt","a+")
file.write("This is Python file.\n")
file.write("This file is opened in append mode.\n")
file.write("Append mode will not overwrite the exisitng content.\n")
file.seek(0) # Moving cursor position at the beginning of the file
print(file.readlines())
file.close()



with open(r"C:\Users\Snehal Thakur\Desktop\PythonClass\FileHandling\file.txt","a+") as file:
    file.write("Opening file Using with keyword\n")
    file.write("The file is in append and read mode.\n")
    file.seek(0) # Moving cursor position at the beginning of the file
    print(file.readlines())
    file.close()
    
