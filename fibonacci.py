how_deep = int(input("How deep into the Fibonacci would you like to go? "))
x = 0
y = 1
z = y
count = 1

while count <= how_deep:
    print(f"{z} ")
    count += 1
    x, y = y, z
    z = x + y