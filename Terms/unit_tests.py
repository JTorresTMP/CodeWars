import unittest

# def get_formatted_name(first, last):
#     return f'{first.title()} {last.title()}'

# def get_formatted_name(first, middle, last): #Purposefully breaking our code to see what a failing test looks like
#     return f'{first.title()} {middle.title()} {last.title()}'


def get_formatted_name(first, last, middle = ''): #Best
		if middle:
				return f'{first.title()} {middle.title()} {last.title()}'
		else:
		    return f'{first.title()} {last.title()}'

class NamesTestCase(unittest.TestCase):
    '''Tests for name_function'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()