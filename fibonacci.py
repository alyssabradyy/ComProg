from re import X


how_deep = int(input("How deep into the Fibonacci would you like to go? "))
def fibonacci(num):
    for i in range(num):
        x = 1
        y = x
        z = x + y
        x = z
        print(x)
fibonacci(how_deep)