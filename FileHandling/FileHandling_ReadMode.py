# File Handling
lines = open(r"C:\Users\Snehal Thakur\Desktop\PythonClass\FileHandling\PythonIntro.txt")

# Print read file read object
print(lines)

# Read all lines
#print(lines.read())

# Read(n) -> read number of characters
#print(lines.read(34))

#for line in lines:
#    print(line)

# Read until new line or EOF (end of the file)
#print(type(lines.readline()))


# readlines() -> read the file object and returns all lines in list
for line in lines.readlines():
    print(line)

# Write operation is not supported as we have opened the file in read mode.
# lines.write("Sample line")

lines.close()
