# In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

# Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception 
# RangeError (JavaScript) or ValueError (Python)

def factorial(n):
    num = n
    if n == 0 or n == 1:
        return 1
    elif 0 < n <= 12:
        while num > 1:
            n = (n * (num - 1)) #You need to recursively call the factorial formula 
            num -= 1
        return n
    else:
        raise ValueError

print(factorial(0))
print(factorial(12))
print(factorial(3))

