#Write a Python program to remove the nth index character from a nonempty string.

def remove_Char(str,n):
    first_part=str[:n]
    last_part=str[n+1:]
    return first_part+last_part
string="Hello"


#code   
# string.replace('H','')
print(remove_Char(string,0))