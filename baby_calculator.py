from re import S


first_number = int(input("Give me a number: "))
second_number = int(input("Give me a second number: "))
operation = input("What operation would you like to use? ")

def add(first_number, second_number):
    print(first_number + second_number)

def sub(first_number, second_number):
        print(first_number - second_number)

def mult(first_number, second_number):
        print(first_number * second_number)

def div(first_number, second_number):
        print(first_number / second_number)

if operation  == "addition":
    add(first_number, second_number)

elif operation  == "subtraction":
    sub(first_number, second_number)

elif operation  == "multiplication":
    mult(first_number, second_number)

elif operation  == "division":
    div(first_number, second_number)

else:
    print("Start over and try using addition, subtraction, multiplication, or division.")