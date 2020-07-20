# In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

# # Remove the 3's at indices 0 and 3
# # followed by removing a 4 at index 1
# solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]


def solve(array):
    arr = []
    for i in array:
        try:
            print(array[array.index(i):])
            if array[array.index(i):].count(i) > 1:
                print(i)
                el = array.remove(i)
                arr.append(el)
        except IndexError:
            continue
    # print(arr)
    return array
    # return list(dict.fromkeys(array))

def solve_2(array):
    return [value for index, value in enumerate(array) if value not in array[ : index]]

# print(solve([1,2,3,4,2,5]))
print(solve_2([1,2,1,2,1,2,3]))