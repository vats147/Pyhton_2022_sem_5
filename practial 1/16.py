#Write a python program to print sum of even numbers up to given N number.Ex. N = 10 then 2 + 4 + 6 + 8 + 10 = 3

num=int(input())
sum=0
i=0
while i<=num:
    if(i%2==0):
    
        sum=sum+i
    
    i=i+1

print(sum)