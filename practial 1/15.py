#Write a python program to print sum of digit in a number. N = 1234 then 1 + 2 + 3 + 4 = 10.
from ctypes import sizeof


num=input()
lista=[*num]
i=0
sum=0
while i<len(lista):
    sum=sum+int(lista[i])
    i=i+1

print(sum)