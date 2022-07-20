# Author Name - Akash Sarkar 
#College Finder Data Science Internship Projects - Project 4 - Real Calculator 
#Date - 20.07.22

def add(a,b):
    addition = a+b
    print(f"The sum of {a} and {b} is {addition}")
def subtract(a,b):
    subtraction = a-b
    print(f"The subtraction of {a} and {b} is {subtraction}")
def multiply(a,b):
    multiplication = a*b
    print(f"The multiplication of {a} and {b} is {multiplication}")
def division(a,b):
    division = a/b
    print(f"The division of {a} and {b} is {division}")
def mod(a,b):
    modulous = a%b
    print(f"The modulous of {a} and {b} is {modulous}")
number1,operator,number2 =map(str,input("Enter your equation: ").split()) #8/9
number1 = int(number1)
number2 = int(number2)
if operator == '+':
    add(number1,number2)
elif operator == '-':
    subtract(number1,number2)
elif operator == '*':
    multiply(number1,number2)
elif operator == '/':
    division(number1,number2)
elif operator == '%':
    mod  (number1,number2)
else:
    print("Invalid type error! please type something like 8 / 4")
