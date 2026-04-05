# Section B: Modules

# Here we learn about Modules. Once we've created a Class
# we can import it into another file and make use of its 
# attributes and methods. 

from a_classes import MyAge

# Instantiate a new object using the imported module, make
# a function call, then print the result.
my_new_age = MyAge("2000-01-01", "Mr. Henry")
print(my_new_age.show_me_my_age())
