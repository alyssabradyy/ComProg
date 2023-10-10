school = ('p', 'a', 'r', 'a', 'd', 'i', 'g', 'm')
for i in school:
    print(i)

for x in range(5):
    print(x)

animals = ('cat', 'dog', 'tiger', 'cow')
for n in animals:
    print(n)

flowers = ('Jasmine', 'Lotus', 'Rose', 'Sunflower')
for f in flowers:
    print(f)
else:
    print("Done")

list1 = (5, 10, 15, 20)
list2 = ('Tomatoes', 'Potatoes', 'Carrots', 'Cucumbers')
for z in list1:
    for y in list2:
        print(z, y)

vehicles = ('Car', 'Cycle', 'Bus', 'Tempo')
for v in vehicles:
    print(v)
    if v == 'Bus':
        break

for m in vehicles:
    if m == 'Bus':
        continue
    print(m)

numbers = (12, 3, 56, 67, 89, 90)
sum = 0

for i in numbers:
    sum += i
print(sum)

for q in numbers:
    enumerate = q
print(enumerate)

for i in range(1, 101):
    if(i % 5 == 0):
        print(i)

fruit_list = ['Mango', 'Banana', 'Orange']
new_list = []
for r in fruit_list:
    new_list.append(r)
print(new_list)

lst = [34, 7, 12, 22, 5, 87, 57, 3]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)

minimum = lst[0]
for i in lst:
    if minimum > i:
        minimum = i
print(minimum)

