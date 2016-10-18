"""
9. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
"""

text = raw_input("enter a text:")
if len(text) >= 3:
	if text[:-3] !='ing':
		text = text+'ly'
	else:
		text = text+'ing'
else:
	print text
print text