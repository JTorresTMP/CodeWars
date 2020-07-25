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

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# unittest.main()

def province(city, country, population = 0):
    return f'{city.title()}, {country.title()} - {population}'

class ProvinceTestCase(unittest.TestCase):
    '''Tests for the province function'''

    def test_city_country(self):
        formatted_location = province('san diego', 'united states of america', 50000)
        self.assertEqual(formatted_location, 'San Diego, United States Of America - 50000')

# unittest.main()

class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print('Survey Results: ')
        for response in self.responses:
            print(f'- {response}')

question = 'What language did you first learn to speak?'

my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Enter \'q\' at any time to quit. \n')
# while True:
#     response = input('Language: ')
#     if response == 'q':
#         break
#     my_survey.store_response(response)

# print('Thanks for taking the survey!')
# my_survey.show_results()


class TestAnonymousSurvey(unittest.TestCase):
    '''Tests for the class AnonymousSurvey'''

    def setUp(self):
        question ='What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Portugese']

    def test_store_single_response(self):
        '''Test that a single response is stored properly'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        '''Test that three individual responses are stored properly'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

# unittest.main()

class Employee():

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, bump = 5000):
        self.salary += bump

class TestEmployee(unittest.TestCase):
    '''Tests for the Employee Class'''

    def setUp(self):
        self.employee = Employee('Jose', 'Torres', 45000)

    def test_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 50000)
    
    def test_variable_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 55000)

unittest.main()