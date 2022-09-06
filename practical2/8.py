#Write a Python program to remove the characters which have odd index values of a given string.
# from tokenize import String


# string="Hello"
# i=0
# string.replace('H','')
# print(string)
# while i<len(string):
string="Hello"
i=0
while i<len(string):
    if(i%2)
    i++

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  print(result.upper())
  print(result.lower())   
  return result


print(odd_values_string('abcdef'))
print(odd_values_string('python'))



# Write a Python program that takes string from the user and displays that string in upper and lower case