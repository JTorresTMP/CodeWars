'''Wikipedia
In computer science, recursion is a method of solving a problem where the solution depends on solutions to smaller instances of the same problem.
Most programming languages support recursion by allowing a function to call itself from within it's own code.'''


houses = ['Eric\'s house', 'Amy\'s house', 'John\'s house']

'''ITERATIVE EXAMPLE'''
def deliver_presents_iteratively(arr):
    for house in arr:
        print('Delivery to', house)

# deliver_presents_iteratively(houses)

'''RECURSIVE EXAMPLE'''
#each funtion call represents an elf doing his work
def deliver_presents_recursively(arr):
    #minimum wage elf doing his job
    if len(arr) == 1:
        house = arr[0]
        print('Delivering to', house)
    
    #manager elf, that divides and delegates his work
    else:
        mid = len(arr) // 2
        first_half = arr[:mid]
        second_half = arr[mid:]

        #divides
        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

# deliver_presents_recursively(houses)

#A recursive function will continue to call itself and repeat its behavior until some 
#condition is met to return a result



'''MAINTAINING STATE'''
#By Passing the updated current state to each recursive call as an argument
def sum_recursive(current_num, accumulated_sum): #Sum of all nums up to 10 in this instance
    #base or end case
    if current_num == 11:
        return accumulated_sum
    
    #recursive case
    else:
        return sum_recursive(current_num + 1, accumulated_sum + current_num)

# print(sum_recursive(1, 0))

#Maintaining state by keeping args in global scope

# current_number = 1
# accumulated_sum = 0

# def sum_recursive():
#     global current_number
#     global accumulated_sum
#     #base case
#     if current_number == 11:
#         return accumulated_sum
#     #Recursive case
#     else:
#         accumulated_sum = accumulated_sum + current_number
#         current_number = current_number + 1
#         return sum_recursive


def list_sum_recursive(input_list):
    #base case
    if input_list == []:
        return 0
    
    #recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure 
    # and can be defined in terms if a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)


# print(list_sum_recursive([1,2,3,4,5]))


def recursive_factorial(n):
    #Base Case:  1! == 1
    if n <= 1:
        return 1
    
    #Recursive case n! = n * (n-1)!
    else:
        return n * recursive_factorial(n-1)

print(recursive_factorial(4))
'''We have to calculate recursive_factorial(4).

The function asks, is n == 1? No, n == 4 so let's return 4 * recursive_factorial(4 - 1),
which is 4 * recursive_factorial(3).

Now we have to calculate recursive_factorial(3).

Is n == 1? No, n == 3 so let's return 4 * 3 * recursive_factorial(3 - 1),
which is 4 * 3 * recursive_factorial(2).

Now we have to calculate recursive_factorial(2).

Is n == 1? No, n == 2 so let's return 4 * 3 * 2 * recursive_factorial(2 - 1),
which is 4 * 3 * 3 * recursive_factorial(1).

Now we have to calculate recursive_factorial(1).

Is n == 1? Yes, n == 1, so let's return 4 * 3 * 2 * 1 which gives us 24 that is then returned one last time by
the original function call.'''


