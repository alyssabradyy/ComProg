import random
with open("sowpods.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split()))
    print(random.choice(words))

# I copied this entire code from like the 20th site I looked at so I still have no clue as to how to do this