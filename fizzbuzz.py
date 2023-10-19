user_number = int(input("What number between 1 and 12 would you like to replace? "))
message = input("What word would you like to replace this number with? ")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % user_number == 0:
        print(message)
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    # this is what the internet told me to do but it doesn't work
    for i in range(2, i):
        if (i % i) == 0:
            break
        else:
            print("Prime")