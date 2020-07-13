# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, function should returns 0

# Examples

# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4

from math import ceil
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    else:
        terms = ceil((((end - begin) / step) + 1))
        # ans = (length * (begin + end)) / 2
        summation = (terms / 2) * ((2 * begin) + ((terms -1) * step))
        # print(terms)
        return summation
        # return sum([x for x in range(begin, end + 1, step)])

print(sequence_sum(2,2,2)) #2
print(sequence_sum(2,6,2)) #6
print(sequence_sum(1,5,1)) #15
print(sequence_sum(0,15,3)) #45
print(sequence_sum(1,5,3)) #5
