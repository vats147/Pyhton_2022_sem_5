#Write a Python program to print a string made of the first two and the last two
#characters from a given a string.
#If the string length is less than 2, then print 
#“Empty String”
#Sample String : 'Python'
#Expected Result : 'Pyon'
#Sample String : 'PY'
#Expected Result : 'PYPY'
#Sample String : ' P'
#Expected Result : “Empty String

string=input()

if(len(string)<2):
    print("Empty String")
else:
    print(string[:2]+string[-2:])