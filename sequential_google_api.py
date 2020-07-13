# def first_non_consecutive(arr):
#     try:
#         for i in range(0, len(arr)):
#             current = arr[i]
#             following = arr[i + 1]
#             if following - current == 1:
#                 continue
#             elif following - current != 1:
#                 return following
#             else:
#                 return None
#     except IndexError:
#         return None


# print(first_non_consecutive([1,2,3,4,5,7]))



# def expressions_matter(a,b,c):
#     results = [] 
#     test = a + b + c
#     test1 = a * b * c
#     test2 = (a + b) * c
#     test3 = a * (b + c)
#     results.extend([test, test1, test2, test3])
#     return max(results)

# print(expressions_matter(2,10,3))


# def combat(health, damage):
#     if health - damage <= 0:
#         return 0
#     else:
#         return health - damage

# print(combat(30,20))


# def weekday(id = None):
#     global switcher 
#     switcher = {
#         1: 'Sunday',
#         2: 'Monday',
#         3: 'Tuesday',
#         4: 'Wednesday',
#         5: 'Thursday',
#         6: 'Friday',
#         7: 'Saturday'
#     }
#     return  switcher.get(id, 'Wrong, please enter a number between 1 and 7') 


# print(weekday())
# print(weekday(3))

# print(switcher)

import math

def calculate_tip(bill_total, rating):
    ratings = {
        'terrible': 0,
        'poor': .05,
        'good': .1,
        'great': .15,
        'excellent': .2
    }
    default = 'Rating not recognised'
    r = ratings.get(rating.lower(),default) * bill_total
    if isinstance(r, int) or isinstance(r, float):
        return math.ceil(r)
    else:
        return default


# print(calculate_tip(9465461, 'gReat'))


def quarter_of(month):
    quarter_1 = {x : 1 for x in [1,2,3]}
    quarter_2 = {x : 2 for x in [4,5,6]}
    quarter_3 = {x : 3 for x in [7,8,9]}
    quarter_4 = {x : 4 for x in [10,11,12]}

    if month in quarter_1:
        return quarter_1[month]
    elif month in quarter_2:
        return quarter_2[month]
    elif month in quarter_3:
        return quarter_3[month]
    elif month in quarter_4:
        return quarter_4[month]
    else:
        return 'Value not found'

    # quarters = {
    #     1: '1',
    #     2: '1',
    #     3: '1',
    #     4, 5, 6 : '2'
    # }
    # return quarters.get(month, 'Hmm')


# print(quarter_of(2))
# print(quarter_of(5))
# print(quarter_of(10))
# print(quarter_of(8))
# print(quarter_of('potato'))


# def to_weird_case(string):
#     split = [char for char in string]
#     print(split)
#     updated = []
#     for i, value in enumerate(split, 0):
#         if i % 2 == 0:
#             updated.append(value.upper()) 
#         else:
#             updated.append(value.lower())
    
#     # for i in split:
#     #     if split.index(i) % 2 == 0:
#     #         updated.append(i.lower())
#     #     else:
#     #         updated.append(i.upper())
#     new = ''.join(updated)
#     return new

# print(to_weird_case('This is a test'))




def pizzaPrice(diameter, price):
    new_area = price / ((diameter/2) ** 2 * 3.14)
    string = '%.2f' % new_area
    return float(string)


# print(pizzaPrice(7, 4.30))





def past2(h, m, s):
    return (3600*h + 60*m + s) * 1000

# print(past2(0,1,1))
# print(past2(1,1,1))
# print(past2(0,0,0))
# print(past2(1,0,1))
# print(past2(1,0,0))




def abbrevName(name):
    try:
        abb = f'{name[0].upper()}.'
        counter = 0
        for char in name:
            following = name[counter + 1]
            if char == ' ':
                abb += following.upper()
                return abb
            counter += 1 
            
        return abb
    except IndexError:
        return None
    
# print(abbrevName('Sam Harris'))

import math
def century(year):
    return math.ceil(year/100)


def digitize(n):
    arr = [x for x in str(n)]
    return arr[::-1]

# print(digitize(35231))

def find_needle(haystack):
    if 'needle' in haystack:
        return (f'found the needle at position {haystack.index("needle")}')

# print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))


from statistics import median

def descending_order(num):
    arr = [x for x in str(num)]
    arr = sorted(arr, reverse = True)
    return int(''.join(arr))

# print(descending_order(10))


def high_and_low(numbers):
    arr = numbers.split()
    intified = [int(x) for x in arr]
    new = []
    top, bottom = max(intified), min(intified)
    new.extend([str(top), str(bottom)])
    return ' '.join(new)


# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))


def square_digits(num):
    arr = [i for i in str(num)]
    tup = map(lambda x: int(x) ** 2, arr)
    lst = map(lambda x: str(x),tup)
    to_return = ''.join(lst)
    return int(to_return)

# print(square_digits(9119))

def capitalize(s):
    even, odd = '', ''
    counter = 0
    for char in s:
        if counter % 2 == 0:
            even += char.upper()
            odd += char.lower()
            counter += 1
        else:
            even += char.lower()
            odd += char.upper()
            counter += 1
    return [even, odd] 


# print(capitalize("abcdef"))



import collections
def find_it(seq):
    cnt = collections.Counter()
    for x in seq:
        cnt[x] += 1
    print(cnt)
    for k, v in cnt.items():
        if v % 2 != 0:
            return k
    # return cnt



# print(find_it([5,4,3,2,1,5,4,3,2,10,10]))


def get_middle(s):
    arr = [x for x in s]
    if len(arr) % 2 != 0:
        while len(arr) > 1:
            arr.pop()
            del arr[0]
        return arr[0]
    else:
        while len(arr) > 2:
            arr.pop()
            del arr[0]
        return ''.join(arr)


# print(get_middle("testing"))
# print(get_middle("test"))

import math
def is_square(n):
    if n >= 0:     
        sqr = math.sqrt(n)
        return True if str(sqr).endswith('.0') else False
    else:
        return False


# print(is_square(25))
# print(is_square(-7))
# print(is_square(27))

import collections
def xo(s):
    s = s.lower()
    cnt = collections.Counter()
    for x in s:
        cnt[x] += 1
    if cnt['x'] == cnt['o']:
        return True
    else:
        return False

# 'Codewars Best Solution'
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# print(xo('xoXo'))


def is_isogram(string):
    string = string.lower()
    if string:
        for x in string:
            print(string.count(x))
            if string.count(x) == 1:
                return True
            else:
                return False
    else:
        return True

# print(is_isogram("Dermatoglyphics"))
# print(is_isogram("isogram")) 
# print(is_isogram("aba"))
# print(is_isogram("moOse"))
# print(is_isogram("isIsogram"))
# print(is_isogram(""))

def get_sum(a,b):
    arr = []
    arr.extend([a,b])
    arr.sort()
    new_arr = [x for x in range(arr[0], arr[1] + 1)]
    return sum(new_arr)
    # return arr


# print(get_sum(10,3))



# def nb_year(p0, percent, aug, p):
#     target = p
#     formula = (p0 + (p0 * (percent/100)) + aug)
#     cnt = 0
#     while formula < p:
#         formula

# print(nb_year(1500, 5, 100, 5000))


def longest(s1, s2):
    new_str = s1 + s2
    arr = [s for s in new_str]
    arr = sorted(arr)
    for s in arr:
        while arr.count(s) > 1:
            arr.remove(s)
    return ''.join(arr)

# print((longest("aretheyhere", "yestheyarehere")))



def maskify(cc):
    short = list(cc[:-4])
    for s in range(len(short)):
        short[s] = '#'
    short.extend(cc[-4:])
    return ''.join(short)



# print(maskify("4556364607935616"))
# print(maskify(     "64607935616"))
# print(maskify(               "1"))
# print(maskify(                ""))



# print(string.ascii_lowercase)
import string

def printer_errors(s):
    counter = 0
    for x in s:
        if x in string.ascii_lowercase[14:]:
            counter += 1
    return f'{counter}/{len(s)}'


# print(printer_errors('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'))



def digital_root(n):
    arr = [int(x) for x in str(n)]
    the_sum = sum(arr)
    while True:
        if the_sum > 9:
            arr = [int(x) for x in str(sum(arr))]
            the_sum = sum(arr)
        else: 
            break
    return the_sum




# print(digital_root(132189))

import math

def find_next_square(n):
    sqr = math.sqrt(n)
    return int((sqr + 1) ** 2) if str(sqr).endswith('.0') else -1


# print(find_next_square(121))
# print(find_next_square(625))
# print(find_next_square(319225))
# print(find_next_square(114))


def persistence(num):
    arr = [int(x) for x in str(num)]
    a = 1
    counter = 0
    while True:
        if a > 9:
            for i in arr:
                a *= i
                print(a)
            counter += 1
        else:
            break
    print(a)
    return(counter)

# print(persistence(39))


import functools
def pers(n):
    counter = 0
    if n > 9:
        arr = [int(x) for x in str(n)]
        new = functools.reduce(lambda a,b: a * b, arr)
        counter += 1
        while new > 9:
            arr2 = [int(x) for x in str(new)]
            new = functools.reduce(lambda a,b: a * b, arr2)
            counter += 1
    return counter

# print(pers(39))
# print(pers(4))
# print(pers(25))
# print(pers(999))


# import re
# def validate_pin(pin):
#     test = re.search('\d{1,4}$', str(pin))
#     if pin == test:
#         return True
#     else:
#         return False


# print(validate_pin(1245))



def reverseWords(string):
    return ' '.join(string.split()[::-1])


# print(reverseWords('hello world!'))


def add_binary(a,b):
    return f'{(a+b):b}'


    
# print(add_binary(1,1))
# print(add_binary(0,1))
# print(add_binary(1,0))
# print(add_binary(2,2))
# print(add_binary(51,12))

        

def fizzbuzz(min,max,x,y):
    log = {x:'fizz', y: 'buzz'}
    arr = [x for x in range(min, max + 1)]
    arr2 = []
    for i in arr:
        if i % x == 0 and i % y == 0:
            arr2.append(log[x] + log[y])
        elif i % y == 0:
            arr2.append(log[y])
        elif i % x == 0:
            arr2.append(log[x])
        else:
            arr2.append(i)
    return arr2

# print(fizzbuzz(1,100,3,5))

def fizz2_0(min, max, x, y):
    return ['fizz' + 'buzz' if i % x == 0 and i % y == 0 else 'fizz' if i % x == 0 else 'buzz' if i % y == 0 else i for i in [x for x in range(min, max + 1)]] 

# print(fizz2_0(1,100,3,5))

def fizz3_0(min,max,x,y):
    return list(map(lambda i: "Fizz"*(i%x==0)+"Buzz"*(i%y==0) or str(i), range(min,max+1)))

# print(fizz3_0(1,100,3,5))

def remove_smallest(numbers):
    try:
        arr = sorted(numbers)
        lowest = min(arr)
        numbers.remove(lowest)
        return numbers
    except ValueError:
        return numbers

# print(remove_smallest([211,365,261,354,91,123,117]))


def create_phone_number(n):
    arr = [str(x) for x in n]
    string = ''.join(arr)
    return f'({string[0:3]}) {string[3:6]}-{string[6:10]}'

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

def morse_decoder(string):
    morse = {
        '.-' : 'A',
        '-...' : 'B',
        '-.-.' : 'C',
        '-..' : 'D',
        '.' : 'E',
        '..-.' : 'F',
        '--.' : 'G',
        '....' : 'H',
        '..' : 'I',
        '.---' : 'J',
        '-.-' : 'K',
        '.-..' : 'L',
        '--' : 'M',
        '-.' : 'N',
        '---' : 'O',
        '.--.' : 'P',
        '--.-' : 'Q',
        '.-.' : 'R',
        '...' : 'S',
        '-' : 'T',
        '..-' : 'U',
        '...-' : 'V',
        '.--' : 'W',
        '-..-' : 'X',
        '-.--' : 'Y',
        '--..' : 'Z',
        '-----' : 0,
        '.----' : 1,
        '..---' : 2,
        '...--' : 3,
        '....-' : 4,
        '.....' : 5,
        '-....' : 6,
        '--...' : 7,
        '---..' : 8,
        '----.' : 9
    }
    arr3 = [x for x in string]
    txt = ''.join(arr3)
    arr = string.split()
    print(arr)
    print(arr3)
    print(txt)
    arr2 = []
    for x in arr:
        arr2.append(x.replace(x,morse[x]))
    return arr2


# print(morse_decoder('.... . -.--   .--- ..- -.. .'))


def count_by(x, n):
    arr = [y for y in range(x, (x * n + 1), x)]
    return arr

# print(count_by(2, 5))


def to_alternating_case(string):
    arr = [x.upper() if x.islower() else x.lower() for x in string]
    return ''.join(arr)


# print(to_alternating_case('hello world'))


def feast(beast, dish):
    return beast[0] == dish[0]

# print(feast('bear', 'brownie'))


# def reverse_words(string): #must keep spaces
#     text = string
#     arr = [x for x in string]
#     arr2 = string.split()
    
#     pass


# print(reverse_words('apple'))

def hash_loop(reps):
    counter = reps
    for _ in range(reps):
        print('#' * counter)
        counter -= 1
    
# hash_loop(5)


def series_sum(n):
    start = 4
    arr = [1]
    if n:
        if n == 1:
            return '1.00'
        for _ in range(n - 1):
            arr.append(1/start)
            start += 3
        print(arr)
        return f'{float(round(sum(arr), 2)):.02f}'
    else:
        return '0.00'


# print(series_sum(5))
# print(series_sum(0))
# print(series_sum(1))


def decode(s, num): #Reversing a process
    alph = {chr(x + 97): x for x in range(26)}
    elph = {x: chr(x + 97) for x in range(26)}
    s_arr = [x for x in s]
    decoded_arr = []
    for s in s_arr:
        initial = alph.get(s) * num % 26
        decoded_arr.append(elph.get(initial))
    try:
        return f"{num}{''.join(decoded_arr)}"
    except IndexError:
        raise 'Value is out of alphabet range'

# print(decode('mer', 6015))




def spin_words(s):
    arr = s.split()
    new = []
    for x in arr:
        if len(x) > 5:
            back = x[::-1]
            new.append(str(back))
        else:
            new.append(x)
    return ' '.join(new)


# print(spin_words('Hey fellow warriors this is a test or perhaps not insurmountable pyramid hello'))

import re

def song_decoder(s):
    arr = s.split('WUB')
    comp = [x for x in arr if x != '']
    return ' '.join(comp)

# print(song_decoder('WUBIWUBAMWUBLIFE'))
# print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))



def alphabet_war(fight):
    right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
    left = {'w':4, 'p': 3, 'b': 2, 's': 1}
    rarr = []
    larr = []
    for s in fight:
        if s in 'mqdz':
            rarr.append(right.get(s))
        elif s in 'wpbs':
            larr.append(left.get(s))
    return 'Left side wins!' if sum(larr) > sum(rarr) else 'Right side wins!' if sum(rarr) > sum(larr) else 'Let\'s fight again!'


# print(alphabet_war("z"))
# print(alphabet_war("zdqmwpbs"))
# print(alphabet_war("wq"))
# print(alphabet_war("zzzzs"))
# print(alphabet_war("wwwwww"))

import time

tic = time.perf_counter()

def dont_give_me_five(start,end):
    test = [x for x in range(start, end + 1) if '5' not in str(x)]
    return len(test)

# toc = time.perf_counter()

# print(f'Time Elapsed: {toc-tic:.02f}')

def unique_sequence(n):
    arr = [x for x in range(n)]
    return arr

def mult_3_5(n):
    return sum([x for x in range(n) if (x % 5 == 0 or x % 3 == 0)])



# print(mult_3_5(200))


def how_much_i_love_you(nb_petals):
    petals = {
        1: 'I love you',
        2: 'a little',
        3: 'a lot',
        4: 'passionately',
        5: 'madly',
        6: 'not at all'}
    while nb_petals > 6:
        nb_petals -= 6
    return petals.get(6) if nb_petals == 0 else petals.get(nb_petals)


# print(how_much_i_love_you(401))
# print(how_much_i_love_you(356))
# print(how_much_i_love_you(318))

def calculate_age(birthyear, target):
    if birthyear == target:
        return 'You were born this very year!'
    elif birthyear > target:
        return 'You will be born in {} year{}.'.format(birthyear - target, 's' * ((birthyear - target) > 1))
    else:
        return 'You are {} year{} old.'.format(target - birthyear, 's' * ((target - birthyear) > 1 ))


def hydrate(drinks):
    arr = []
    for s in drinks.split(' '):
        try:
            arr.append(int(s))
        except ValueError:
            continue
    return f"{sum(arr)} glass{'es' if sum(arr) > 1 else ''} of water"



# print(hydrate('1 beer'))
# print(hydrate('1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer'))
# print(hydrate('10 IPAs, 200 shots'))

import string

def solve(st):
    alph = string.ascii_lowercase
    arr = [x for x in st]
    arr.sort()
    return ''.join(arr) in alph


# print(solve('dabcefg'))

def stray(arr):
    for x in set(arr):
        if arr[:3].count(x) < 2:
            return x


# print(stray([1,1,1,2]))

def catch_sign_change(lst):
    pos = [x for x in lst if x <= 0]
    neg = [x for x in lst if x < 0]
    return min([len(pos), len(neg)])

# print(catch_sign_change([-47,84,-30,-11,-5,74,77]))


def counting_valleys(s): 
    compass = {'F': 0, 'U': 1, 'D': -1}
    arr = [compass.get(x) for x in s if compass.get(x) != 0]
    state = 0
    # print(state)
    states = [0]
    for i in arr:
        state += i
        # print(state)
        states.append(state)
    print(states)
    print(int((states.count(0) / 2)))
    return arr


# print(counting_valleys('UFFFD'))

def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get(int((s1 + s2 + s3) / 30), 'F')

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

# print(divisible_by([1,2,3,4,5,6], 2))

def stringy(size):
    string = '1'
    for _ in range(size - 1):
        if len(string) % 2 != 0:
            string += '0'
        else:
            string += '1'
    return string

# print(stringy(4))

def stringy2_0(size):
    arr = ['1' if x % 2 == 0 else '0' for x in range(size)]
    return arr

# print(stringy2_0(4))

# arr = ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]
# arr.sort()
# print('*'.join(x for x in arr[0]))

import re
def no_boring_zeros(n):
    if n:
        arr = [str(x) for x in str(n)]
        arr.reverse()
        text = ''.join(arr)
        index = re.search("[1-9]",''.join(arr))
        index2 = text.find(index.group())
        text = text[index2:]
        narr = [x for x in text]
        narr.reverse()
        return int(''.join(narr))
    else:
        return 0

# print(no_boring_zeros(1450))
# print(no_boring_zeros(96000))

def find_longest(string):
    arr = string.split(' ')
    for i in arr:
        arr[arr.index(i)] = len(i)
    return max(arr)



# print(find_longest("The quick white fox jumped around the massive dog"))

# Last digit of a huge number 3 Kyu

def sum_mul(n, m):
    if n > 0 and m > 0:
        return sum([x for x in range(n,m,n)])
    return 'INVALID'

# print(sum_mul(2, 9))

import math
def square_or_square_root(arr):
    narr = [int(math.sqrt(x)) if str(math.sqrt(x)).endswith('0') else x ** 2 for x in arr]
    return narr

# print(square_or_square_root([1,2,3,4,5,6,7,8,9,10]))


def solution(digits):
    if digits:
        ans = 0
        for i in range(len(digits)):
            new = digits[i:i + 5]
            if int(new) > ans:
                ans = int(new)
        return ans
    return 0

# print(solution('1234567980'))


def indexkyu(arr, n):
    try:
        return arr[n] ** 2
    except IndexError:
        return -1


# print(indexkyu([1,2,3,4,5], 3))

def the_valley(s):
    level, v = 0,0
    for char in s:
        if char == 'U':
            if level + 1 == 0:
                v += 1
        elif char == 'D':
            level -= 1
    return v

# print(the_valley('FDUFUDFUDFUDUFUUDDF'))

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    for s in birds:
        for x in geese:
            if s == x:
                birds.remove(s)
            
    return birds

# print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))
# print(goose_filter(["Mallard", "Barbary", "Hook Bill", "Blue Swedish", "Crested"]))
# print(goose_filter(["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]))



# def fizz34(n):
#     return list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,n+1)))

# print(fizz34(10))


# def replace_exclamation(s):
#     return ''.join(['!' if x in 'aeiouAEIOU' else x for x in s])


# print(replace_exclamation('hello'))


def removed(s, n):
    arr = list(s)
    for _ in range(n):
        try:
            arr.remove('!')
        except ValueError:
            continue
    return ''.join(arr)

#CodeWars Answer
# def removed(s,n):
#     return s.replace('!','', n)

# print(removed('Hi!!!', 4))