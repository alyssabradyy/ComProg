charname = input("Welcome to the Battle Nexus! Here you can become a great hero, what is your title? ")
print(f"Pleased to meet you {charname}! You will start with 100 HP and nothing in your inventory. Try to win as many fights as you can and collect different prizes.")
print("To check your items press the 'r' key, to walk forward, press 'w', and if you encounter an enemy you may press either 'a' for attack, or 'f' for flee.")
enemies = ('tiger', 'cyclops', 'vampire', 'unicorn', 'samurai')
char_hp = 100
enemy_hp = 100
walk = input("Go ahead and press 'w' to walk!")
if walk in ("w"):
    while True:
        import random
        with open (1, 2, 3):
            if 1:
                enemy_encounter = input(f"You found an opponent! This enemy is a {random(enemies)}. Will you attack or flee? ")
                if enemy_encounter in "a":
                    while char_hp > 0 or while enemy_hp > 0:
                        attack_given = random(range(1, 100))
                        enemy_hp - attack_given
                elif enemy_encounter in "f":
                else:
                    ("Please press 'a' to attack or 'f' to flee.")