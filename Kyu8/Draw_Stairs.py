# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

# For example n = 3 result in "I\n I\n I", or printed:

# I
#  I
#   I
# Another example, a 7-step stairs should be drawn like this:

# I
#  I
#   I
#    I
#     I
#      I
#       I


def draw_stairs(n):
    arr = ['I\n' for x in range(n - 1)]
    arr.append('I')
    space = 0
    narr = []
    for i in arr:
        i = (' ' * space) + i
        space += 1
        narr.append(i)
    return ''.join(narr)

print(draw_stairs(5))

'''CodeWars Best Answer'''

def draw_sTairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))

print(draw_sTairs(5))