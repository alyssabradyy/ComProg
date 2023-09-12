first_number = input("Give me a number: ")
second_number = input("Give me a second number: ")
operation = input("What operation would you like to use? ")

if operation in ("addition"): 
    def add(first_number, second_number):
        print[first_number, second_number]

if operation in ("subtraction"):
    def subtract(num1, num2):
        return num1 - num2
    print(subtract(first_number, second_number))

if operation in ("multiplication"):
    print(first_number * second_number)

if operation in ("division"):
    print(first_number / second_number)

elif operation:
    print("Try using addition, subtraction, multiplication, or division.")