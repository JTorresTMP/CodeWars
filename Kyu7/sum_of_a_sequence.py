# Your task is to make function, which returns the sum of a sequence of integers.

# The sequence is defined by 3 non-negative values: begin, end, step.

# If begin value is greater than the end, function should returns 0

# Examples

# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4

import math
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    else:
        terms = math.floor((((end - begin) / step) + 1))
        summation = (terms / 2) * ((2 * begin) + ((terms -1) * step))
        return summation

print(sequence_sum(2,2,2)) #2, 1 Term
print(sequence_sum(2,6,2)) #6, 3 Terms
print(sequence_sum(1,5,1)) #15, 5 Terms
print(sequence_sum(0,15,3)) #45, 6 Terms
print(sequence_sum(1,5,3)) #5, 2 Terms
print(sequence_sum(-1, -5, -3))
print(sequence_sum(-24, -2, 22))