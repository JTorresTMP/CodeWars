# Write a function named sumDigits which takes a number as input and returns the 
# sum of the absolute value of each of the number's decimal digits. For example:

#   sum_digits(10)  # Returns 1
#   sum_digits(99)  # Returns 18
#   sum_digits(-32) # Returns 5

def sum_digits(number):
    arr = [int(x) for x in str(number) if x in '0123456789']
    return sum(arr)

print(sum_digits(10)) #1
print(sum_digits(99)) #18
print(sum_digits(-32)) #5

