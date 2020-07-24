# In this Kata, you will be given a string and your task will be to return a list of ints 
# detailing the count of uppercase letters, lowercase, numbers and special characters, as follows:

# Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
# --the order is: uppercase letters, lowercase, numbers and special characters.
import time

def solve(s):
    uppers = [x for x in s if x.isupper()]
    lowers = [x for x in s if x.islower()]
    nums = [x for x in s if x.isdigit()]
    total = len(uppers) + len(lowers) + len(nums)
    return [len(uppers), len(lowers), len(nums), (len(s) - total)]
tic = time.perf_counter()
print(solve("RYT'>s&gO-.CM9AKeH?,5317"))
toc = time.perf_counter()
print(f'Method one: {toc - tic:.06f} seconds')


def solved(s):
    uppers, lowers, nums, rest = [], [], [], []
    for char in s:
        if char.isupper():
            uppers.append(char)
        elif char.islower():
            lowers.append(char)
        elif char.isdigit():
            nums.append(char)
        else:
            rest.append(char)
    return [len(uppers), len(lowers), len(nums), len(rest)]

tic1 = time.perf_counter()
print(solved("RYT'>s&gO-.CM9AKeH?,5317"))
toc1 = time.perf_counter()
print(f'Method two: {toc1 - tic1:.06f} seconds')

'''Method 2 is twice as fast in some instances'''