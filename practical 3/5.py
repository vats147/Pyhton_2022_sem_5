#Write a Python program to find the list of words that are longer than n from a 
# given list of words.
# N=3, Word List =The quick brown fox jumps over the lazy dog
# Output: ['quick', 'brown', 'jumps', 'over', 'lazy']
# Write a Python program to print the numbers from the list after removing even 
# numbers from it



word="The Quick BROWN fox JUms over"

p=list(word)
i=0;
while i<len(p):
    if(len(p[i])<=3):
        p.remove(p[i])
    i=i+1
    

# p.remove(p[0])
print(p)

