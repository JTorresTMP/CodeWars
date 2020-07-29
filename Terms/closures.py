
#Closures

#Wikipedia: 'A closure is a record storing a function together with an environment:
#a mapping associating each free variable of the function with the value or storage
#location to which the name was bound when the closure was created. A closure, unlike
#a plain funnction, allows the function to access those captured variables through the 
#closure's reference to them, even when the function is invoked outside their scope

'''Python Example'''

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    
    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()

'''JavaScript Example'''

# function html_tag(tag){
#     function wrap_text(msg){
#         console.log(`<${tag}>${msg}</${tag}>`) #These are basically F Strings but they are done with ` and ${value}
#     }
#     return wrap_text
# }

# print_h1 = html_tag('h1')
# print_h1('Test Headline') #At this point, print_h1 is equivalent to wrap_text() so that's why we are passing in msg

