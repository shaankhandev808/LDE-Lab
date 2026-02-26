# Here we learn about classes in Python.
# The thing to realize is that a Class providess a blueprint for an Object.

# First we import some modules.
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

# Create a MyAge Class. A class definition has attributes and functions.
class MyAge:
    # Init is like a Constructor in Java. Takes self + two pieces of data for attributes. 
    def __init__(self, date_of_birth, my_name):
        # double underscores indicate "private-ish" attributes, meant for internal use in the Class.
        # Datetime() is used to parse a string into a datetime object.
        self.__date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')     
        self.__my_name = my_name
        # Find the delta between today's date and the given birthday.
        self.__my_age_years = relativedelta(
            date.today(), self.__date_of_birth).years

    # Classes can also have methods.
    def show_me_my_age(self):
        return f"{self.__my_name}, you are so young, only {self.__my_age_years} years old!"

# Instantiate the class, thus creating an object. Make a function call then print its result.
age = MyAge("1988-08-08", "Shaan Khan aka Mac Daddy")
print(age.show_me_my_age())
# > 'Mr SHaan Khan aka Mac Daddy, you are so young, only 37 years old!'