from re import X


my_name = "Alyssa"

def give_a_name():
    a_name = "William"
    print(a_name)

user_input = input("What is your name? ")
print(f"Nice to meet you, {user_input}!")

# data types
my_string = "This is my string."
my_integer = 4
my_float = 5.67
is_my_boolean = True
my_declaration = ""
my_initialization = "Hello world"

print(my_integer + my_float)

add = 2 + 3
subtract = 5 - 1
multiply = 3 * 8
divide = 6 / 2
modulo = 10 / 3


statement = 4 > 2
statement2 = 4 >= 2
statement3 = 4 == 2
statement4 = 4 != 2

message = 4 > 2 and 33 < 43
message2 = 4 < 2 or 33 < 43
x = False
print(not x)

y = 10
x = y + 10

z = 7 // 2
t = 7 / 2
print(z)

def my_function():
    print("I am so great!")

my_function()

def add(num1, num2):
    [print(num1, num2)]

my_name = "poop"
words = my_name.split("o")
print(words)

def subtract(num1, num2):
    return num1 - num2
print(subtract(4,2))
difference = subtract(4,2)
print(difference)