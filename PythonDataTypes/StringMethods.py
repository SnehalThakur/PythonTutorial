# String Methods
string1 = 'python'
string2 = '54321'
string3 = '  Data Science  '
string4 = 'STATISTICS'
string5 = 'Python#Stats#ML#DL'
string6 = "thakursnehal1991@gmail.com"

# 1. len() - To find the length of the string
print("Method 1. len() - To find the length of the string")
print('len(string1) i.e "python" =',len(string1))
print('len(string2) i.e "54321" =',len(string2))
print('len(string3) i.e "  Data Science  " =',len(string3))
print('len(string4) i.e "STATISTICS" =',len(string4))
print('len(string5) i.e "Python#Stats#ML#DL" =',len(string5))
print('len(string6) i.e "thakursnehal1991@gmail.com" =',len(string6))
print('=============================')
# 2. string.upper() - To convert the string into upper case
print("Method 2. string.upper() - To convert the string into upper case")
print("string1.upper() =",string1.upper())
print('=============================')
# 3. string.lower() - TO convert the string into lower case
print("Method 3. string.lower() - TO convert the string into lower case")
print("string4.lower() =", string4.lower())
print('=============================')
# 4. string.capitalize() - TO convert the first char of the string in upper case
print("Method 4. string.capitalize() - TO convert the first char of the string in upper case")
print("string1.capitalize() =", string1.capitalize())
print('============================')
# 5. string.islower() - To check whether the string is in lower case or not
print("Method 5. string.islower() - To check whether the string is in lower case or not")
print("string1.islower() =",string1.islower())
print("string4.islower() =",string4.islower())
print('============================')
# 6. string.isupper() - To check whether the string is in upper case or not
print("Method 6. string.isupper() - To check whether the string is in lower case or not")
print("string1.isupper() =",string1.isupper())
print("string4.isupper() =",string4.isupper())
print('============================')
# 7. string.split() - To spit the string into multiple sub strings using split character
print("Method 7. string.split() - To spit the string into multiple sub strings using split character")
print("string5.split() =",string5.split())
print("len(string5.split()) =",len(string5.split()))
print("type(string5.split()) =",type(string5.split()))
print("string5.split('#') =",string5.split('#'))
print("len(string5.split('#')) =",len(string5.split('#')))
print("string6.split('@') =",string6.split('@'))
print("len(string6.split('@')) =",len(string6.split('@')))
print("type(string6.split('@')) =",type(string6.split('@')))
print('============================')
# 8. "".join([string1, string2]) - To join multiple strings
print("Method 8. '{char}'.join([string1, string2]) - To join multiple strings")
print('",".join([string1, string2])',",".join([string1, string2]))
print('"$".join([string1, string4])',"$".join([string1, string4]))
print('"*".join([string1, string2])',"*".join([string1, string2]))
print('============================')
# 9. String.index() - TO find index position of the char
print("Method 9. String.index() - TO find index position of the char")
print("string1.index('p') =",string1.index('p'))
print("string1.index('y') =",string1.index('y'))
print("string1.index('t') =",string1.index('t'))
print("string1.index('h') =",string1.index('h'))
print("string1.index('o') =",string1.index('o'))
print("string1.index('n') =",string1.index('n'))
print("string5.index('#') =",string5.index('#'))
print('============================')
# 10. String.startswith('{char}') -  To check whether string start with particular char
print("Method 10. startswith('{char}') -  To check whether string start with particular char")
print("string1.startswith('p') =",string1.startswith('p'))
print("string1.startswith('y') =",string1.startswith('y'))
print('============================')
# 11. String.endswith('{char}') -  To check whether string ends with particular char
print("Method 11. endswith() -  To check whether string ends with particular char")
print("string1.endswith('n') =",string1.endswith('n'))
print("string1.endswith('t') =",string1.endswith('t'))
print('============================')
# 12. String.count('{char}') - To count number of specific char
print("Method 12. String.count('{char}') - To count number of specific char")
print("string4 = 'STATISTICS'")
print("string4.count('A')=",string4.count("A"))
print("string4.count('S')=",string4.count("S"))
print("string4.count('T')=",string4.count("T"))
print("string4.count('I')=",string4.count("I"))
print("string4.count('C')=",string4.count("C"))
print('============================')
# 13. String.strip() - To remove leading and trailing white spaces
print("Method 13. String.strip() - To remove leading and trailing white spaces")
print("string3 = '  Data Science  '")
print("string3=",string3)
print("len(string3)=",len(string3))
print("string3.strip()=",string3.strip())
print("len(string3.strip())=",len(string3.strip()))
print('============================')
# 14. String.lstrip() - To remove leading white spaces
print("Method 14. String.lstrip() - To remove leading white spaces")
print("string3 = '  Data Science  '")
print("string3=",string3)
print("len(string3)=",len(string3))
print("string3.lstrip()=",string3.lstrip())
print("len(string3.lstrip())=",len(string3.lstrip()))
print('============================')
# 15. String.rstrip() - To remove trailing white spaces
print("Method 15. String.rstrip() - To remove trailing white spaces")
print("string3 = '  Data Science  '")
print("string3=",string3)
print("len(string3)=",len(string3))
print("string3.rstrip()=",string3.rstrip())
print("len(string3.rstrip())=",len(string3.rstrip()))

