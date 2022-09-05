#Write a python program to find N! (5 factorial=1*2*3*4*5 )

i=1
n=5
mul=1
while i<=n:
    mul*=i
    i=i+1
    
print(mul)