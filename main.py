

#:Q1 Make a lambda function which returns True if a number is even and false when it is odd.

is_even = lambda x: x % 2 == 0


#Q2: Use reduce to find the maximum value in a given list of numbers.
from functools import reduce

def find_max(numbers):
  return reduce(lambda x, y: x if x > y else y, numbers)

numbers = [3, 7, 2, 8, 5]
max_value = find_max(numbers)
print(max_value) 

#Q3: Given a list of strings, use map to create a list of integers representing the length of each string in the original list. For instance, if the input is ["apple", "banana", "kiwi"], the output should be [5, 6, 4].

def string_lengths(strings):
  """Returns a list of integer lengths for each string in the input list."""
  return list(map(len, strings))

words = ["apple", "banana", "kiwi"]
lengths = string_lengths(words)
print(lengths)  

"""///////////////////////////////////////////////////////////////////////
"""




#Q7 Give an example code for handling errors and exceptions in python.



try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
try:
    file = open("myfile.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close() 


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return x / y




"""..............................................."""

# Q5 What is a Docstring? Give an example.
"""ans A docstring is a string literal that occurs as the first statement in a module,
function, class, or method definition. It's used to provide a brief explanation of what the code does.   """

def add(x, y):
  """Adds two numbers together.

  Args:
    x: The first number.
    y: The second number.

  Returns:
    The sum of x and y.
  """

  return x + y

""".........................................................."""





#Q6: Give code to loop through a python dictionary. How can we add and remove elements from a python dictionary?
#ans 

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

# Iterating over keys
for key in my_dict:
    print(key)  

# Iterating over values
for value in my_dict.values():
    print(value)  

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)  
    
#adding element to dict
    
    my_dict = {'apple': 3, 'banana': 5}

my_dict['grape'] = 7

print(my_dict)  


#removing elemnt to dictionory

my_dict = {'apple': 3, 'banana': 5, 'orange': 2}

del my_dict['banana']

print(my_dict)  


value = my_dict.pop('apple')
print(value)  
print(my_dict)  

removed_item = my_dict.popitem()
print(removed_item) 
print(my_dict)  


""".........................................."""





"""
Q8 Let's suppose there is a class A with function display() which is then inherited byclass B and C. B has its own display function while C doesn’t. See the code:


"""


class A:
    def display():
        print("Display from A")


class C(A):
    def display():
        print("Display from C")
        
        
        """.........................................."""
        
        
        
#Q9 In the example above lets say there is another class class D with display function which is also inherited by class C 

class A:
    def display(self):
        print("A's display")

class D:
    def display(self):
        print("D's display")

class C(A, D):
    pass

def __main__():
    c = C()
    c.display()  # Output: D's display

"""............................................"""




