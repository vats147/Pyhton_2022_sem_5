# Write a Python program to count the number of strings in list where the string 
# length is 2 or more and the first and last character are same.
# Sample List: ['abc', 'xyz', 'aba', '1221']
# Output: 2

def count_strings(nums):
    count = 0

    for i in nums:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1

    return count

print(count_strings(['abc', 'xyz', 'aba', '1221']))