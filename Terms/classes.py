#This is based on Chapter 9 of Python Crash Course
class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name.title()} is now sitting')

    def roll_over(self):
        print(f'{self.name.title()} rolled over!')

my_dog = Dog('Willie', 6)


class Restaurant():

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0 #This is a default attribute that is defined within init, so no parameter has to be passed

    def describe(self):
        print(f'{self.name} specializes in {self.cuisine} cuisine.')

    def open_restaurant(self):
        print(f'{self.name} is now open for business!')

    def numbers(self):
        print(f'Over {str(self.number_served)} served')

    def increment_customers_served(self, customers):
        if customers > 0:
            self.number_served += customers

my_restaurant = Restaurant('Tacos Jose', 'Mexican')
your_restaurant = Restaurant('Mr. BBQ', 'Korean-BBQ')
his_restaurant = Restaurant('Joe\'s subs', 'American?')

# my_restaurant.describe()
# your_restaurant.describe()
# his_restaurant.describe()
# my_restaurant.number_served = 25
# my_restaurant.numbers()

class User():

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.login_attempts = 0
    
    def describe(self):
        print(f'This user\'s full name is {self.first} {self.last}.')

    def greet_user(self):
        print(f'Hello there {self.first}, fancy meeting you here.')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('Mike', 'Wazowski')
user_2 = User('Tyrande', 'Whisperwind')
user_3 = User('Khada', 'Jhin')

# user_1.describe()
# user_2.describe()
# user_3.describe()
# user_1.greet_user()
# user_2.greet_user()
# user_3.greet_user()


class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year  = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{str(self.year)} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')
    
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('Trying to pull a fast one eh?')



# my_new_car = Car('honda', 'accord', '2020')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(25)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'This car has a {str(self.battery_size)}-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            car_range = 240
        elif self.battery_size == 85:
            car_range = 270
        
        msg = f'This car can go approx. {str(car_range)} miles on a full charge.'
        print(msg)
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85



class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() #This attribute is its own class!

    def fill_gas_tank(self):
        print('This car does not have a gas tank!')

# my_tesla = ElectricCar('tesla', 'model S', '2018')
# print(my_tesla.get_descriptive_name()) #Verifying that the inheritance worked
# my_tesla.battery.describe_battery() #This line had to be changed as a result of using a class as an attribute
# my_tesla.battery.get_range()

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine, flavors = ['Strawberry', 'Vanilla', 'Chocolate']):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def list_flavors(self):
        print(f"The flavors that we currently offer are {', '.join(self.flavors)}.")

# joes_italian = IceCreamStand('Joe\'s Italian Ice', 'Dessert', ['Mango', 'Guava', 'Pistachio'])
# joes_italian.describe()
# joes_italian.list_flavors()

class Privileges():

    def __init__(self, privileges = ['can create a new post', 'can edit own posts']):
        self.privileges = privileges

    def show_privileges(self):
        print(f'An admin user {", ".join(self.privileges)}')


class Admin(User):

    def __init__(self, first, last, privileges = ['can add posts', 'can delete posts', 'can ban users']):
        super().__init__(first, last)
        self.privileges = Privileges()

# scott = Admin('Scott', 'Langley')
# scott.privileges.show_privileges()

my_model_3 = ElectricCar('tesla', 'model 3', '2019')

# print(my_model_3.get_descriptive_name())
# my_model_3.battery.get_range()
# my_model_3.battery.upgrade_battery()
# my_model_3.battery.get_range()


#Corey Schafer

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@email.com'

    def full_name(self):
        return f'Full Name: {self.first.title()} {self.last.title()}'

test_user = Employee('John', 'Doe', 40000)

print(test_user.full_name()) #We need parentheses here because we are running a method and not reading an attribute