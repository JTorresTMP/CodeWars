# In this Kata, you will be given an array of integers whose elements have both a 
# negative and a positive value, except for one integer that is either only 
# negative or only positive. Your task will be to find that integer.

# Examples:
# [1, -1, 2, -2, 3] => 3
# 3 has no matching negative appearance

# [-3, 1, 2, 3, -1, -4, -2] => -4
# -4 has no matching positive appearance

# [1, -1, 2, -2, 3, 3] => 3
# (the only-positive or only-negative integer may appear more than once)
import time

def solve(arr):
    for i in range(len(arr)):
        if arr[i] * -1 in arr:
            continue
        else:
            return arr[i]
tic = time.perf_counter()
print(solve([-110,110,-38,-38,-62,62,-38,-38,-38])) #should return -38
toc = time.perf_counter()
print(f'Running Time: {toc - tic:.08f}')


def solved(arr):
    return sum(set(arr))

    
tic = time.perf_counter()
print(solved([-110,110,-38,-38,-62,62,-38,-38,-38])) #should return -38
toc = time.perf_counter()
print(f'Running Time: {toc - tic:.08f}')