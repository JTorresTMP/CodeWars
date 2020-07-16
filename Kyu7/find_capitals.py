# Write a function that takes a single string (word) as argument. 
# The function must return an ordered list containing the indexes 
# of all capital letters in the string.

# Example
# Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

def capitals(word):
    arr = []
    for key, value in enumerate(word):
        if value.isupper():
            arr.append(key)
    return arr


print(capitals('CodEWaRs'))
print(capitals('CODEWARS'))
print(capitals('codewars'))
print(capitals('cCCoddEE'))
