player1 = input("Would Player 1 like to play rock, paper, or clamp? ")
player2 = input("Would Player 2 like to play rock, paper, or clamp? ")

if player1 == "Rock" or player1 == "rock":
    if player2 == "Paper" or player2 == "paper":
        print("Player 2 wins!")
    elif player2 == "Clamp" or player2 == "clamp":
        print("Player 1 wins!")
    elif player2 == "Rock" or player2 == "rock":
        print("You tied!")

if player1 == "Paper" or player1 == "paper":
    if player2 == "Paper" or player2 == "paper":
        print("You tied!")
    elif player2 == "Clamp" or player2 == "clamp":
        print("Player 2 wins!")
    elif player2 == "Rock" or player2 == "rock":
        print("Player 1 wins!")

if player1 == "Clamp" or player1 == "clamp":
    if player2 == "Paper" or player2 == "paper":
        print("Player 1 wins!")
    elif player2 == "Clamp" or player2 == "clamp":
        print("You tied!")
    elif player2 == "Rock" or player2 == "rock":
        print("Player 2 wins!")