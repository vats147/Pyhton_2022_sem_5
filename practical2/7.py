#Write a Python program to change a given string to a new string where the first characters have been exchanged.
# Sample String : 'abcd'
# Expected Result : 'dbca'
# Sample String : ‘12345’
# Expected Result : ' 52341'.

string="12345"
l=len(string)
print(string[-1:]+string[1:-1]+string[:1])