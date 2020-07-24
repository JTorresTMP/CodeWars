
# First Class Functions:
# 'A programming language is said to have first-class functions if it treats functions as first class citizens'

# First Class Citizen (Programming):
# 'A first class citizen in a programming language is an entity which supports all the operations generally'
# 'available to  other entities. These operations typically include being passed as an argument, returned from'
# 'a function, and assigned to a variable'

'''In essence, a higher order function is one that can receive another function(s) as an argument, or return a function'''

'ASSIGNING FUNCTIONS TO VARIABLES'

def square(x):
    return x * x

f = square #Make sure you don't include parentheses since that means you are executing the function

# print(square)
# print(f(5))


# JS

# function square(x) {
#     return x * x
# }

# let f = square

# console.log(square)
# console.log(f)

'If a function accepts other functions as arguments or returns functions as the result, that is a Higher Order Function'

'USING FUNCTIONS AS PARAMETERS' #Custom built map function
def cubes(x):
    return x ** 3

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cubes, [1,2,3,4,5])

print(squares)



#JS

# function my_map(func, arg_list) {
#     const result = [];
#     for (let i = 0; i < arg_list.length; i++){
#         result.push(func(arg_list[i]))
#     }
#     return result
# }

# let squares = my_map(cubes, [1,2,3,4,5])

# console.log(squares)

# function cubes(x) {
#     return x ** 3
# }

'RETURNING A FUNCTION'

def logger(msg):

    def log_message():
        print('Log:', msg)
    
    return log_message

log_hi = logger('Hi!')
log_hi()


#JS

# function logger(msg) {
#     function log_message(){
#         console.log('Log: ' + msg)
#     }
#     return log_message
# }

# log_hi = logger('Hi!')
# log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline!')

print_p = html_tag('p')
print_p('Test paragraph')

#JS

# function html_tag(tag) {
#     function wrap_text(msg) {
#         console.log(``<${tag}>${msg}</${tag}>``)
#     }
#     return wrap_text
# }

# print_h1 = html_tag('h1')
# print_h1('Test headline!')

# print_p = html_tag('p')
# print_p('Test paragraph')