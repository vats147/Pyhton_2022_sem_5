#Write a Python program to print a single string from two given strings, 
#separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'.

string=input()
string2=input()

print(string2[0:2]+string[2]+" "+string[0:2]+string2[2])
