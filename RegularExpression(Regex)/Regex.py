import re

txt = '''RegExr was created by www.gskinner.com, and is proudly hosted by Media Temple. www.python.org
9970533440
Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode. www.google.com (
9960607939
The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns. thakursnehal@gmail.com www.regex101.com
9960405886 www.course.ai
Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English. www.regexr.cm www.iiitn.in
snehal.hadoop@gmail.com'''
# Find all websites
websites = re.findall("w{3}\.[a-z0-9]+\.[com|ai|in|org]+", txt)
print("websites =", websites)

# Find all mobile numbers
mobileNum = re.findall("[0-9]{10}", txt)
print("mobileNum =", mobileNum)

# Find all email ids
emailIds = re.findall("[a-z0-9_\.]+@[a-z]+\.[com|in|org]+", txt)
print("emailIds =", emailIds)


