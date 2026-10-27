from operations import *
from utils import *

number = get_user_number()
number2 = get_user_number()

operation = get_operation()
if operation == "+":
    print(add(number,number2))

elif operation == "-":
    print(subtract(number,number2))

elif operation == "*":
    print(multiply(number,number2))

elif operation == "/" and number2 == 0:
    print("Impossible, choose a different second number")
    number2 = get_user_number()
    while True:
        if number2 == 0:
            print("Impossible, choose a different second number")
            number2 = get_user_number()
        else:
            break
    print(divide(number, number2))
else:
    print(divide(number,number2))