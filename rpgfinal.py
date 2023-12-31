import random
charname = input("Welcome to the Battle Nexus! Here you can become a great hero, what is your title? ")
print(f"Pleased to meet you {charname}! You will start with 100 HP and nothing in your inventory. Try to win as many fights as you can and collect different prizes.")
print("To check your items press the 'r' key, to walk forward, press 'w', and if you encounter an enemy you may press either 'a' for attack, or 'f' for flee.")
enemies = ('alien', 'cyclops', 'vampire', 'unicorn', 'samurai')
char_hp = 100
enemy_hp = 100
walk = input("Go ahead and press 'w' to walk! ")
while walk in ("w"):
    enemy_chance = random(1, 2, 3)
    if enemy_chance in 1:
        enemy_encounter = input(f"You found an opponent! This enemy is a {random(enemies)}. Will you attack or flee? ")
        if enemy_encounter in "a":
            while char_hp > 0 or enemy_hp > 0:
                attack_given = random(range(1, 35))
                enemy_hp - attack_given
                print(f"You hit the enemy with {attack_given} damage!")
                attack_taken = random(range(1, 36))
                char_hp - attack_taken
                print(f"The enemy hit you dealing {attack_taken} damage!")
        elif enemy_encounter in "f":
            run_chance = random(1, 2)
            if run_chance == 1:
                print("You ran from the fight!")
            elif run_chance == 2:
                print("You cannot run from this battle.")
                while char_hp > 0 or enemy_hp > 0:
                    attack_given = random(range(1, 100))
                    enemy_hp - attack_given
                    attack_taken = random(range(1, 100))
                    char_hp - attack_taken
        else:
            print("Please press 'a' to attack or 'f' to flee. ")
        if char_hp == 0:
            print("You died! Better luck next time!")
        elif enemy_hp == 0:
            print("You won this round! You got treasure! Open your inventory to check!")
    if 2 or 3:
        print("There are no enemies around. Keep looking!")