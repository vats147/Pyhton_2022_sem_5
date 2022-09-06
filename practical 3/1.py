#Write a Python program to sum all the items in a list.

number=[1,2,3,4]

i=0
sum=0
while i<len(number):
    sum+=number[i]
    i=i+1
print(sum)