#Write a python program to print sum of odd numbers up to given N number.Ex. N = 10 then 1 + 3 + 5 + 7 + 9 = 25

num=int(input())
sum=0
i=0
while i<=num:
    if(i%2==1):
    
        sum=sum+i
    
    i=i+1

print(sum)