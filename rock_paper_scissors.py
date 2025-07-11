print("Welcome to Rock, Paper, Scissors!")

player = (0)
computer = (0)
round = (0)

while round < 3:
    player = int(input("Pick a number between 1 and 3. "))
    round = round + 1
    
    print("✊")
    print("✋")
    print("✌️")
    print("Shoot!")

    1 == ("✊")
    2 == ("✋")
    3 == ("✌️")

    import random
    computer = random.randint(1, 3)

    if computer == 1 and player == 2:
        print(player)
        print(computer)
        print("You Win!")
    elif computer == 2 and player == 3:
        print(player)
        print(computer)
        print("You Win!")
    elif computer == 3 and player == 1:
        print(player)
        print(computer)
        print("You Win!")
    elif computer == 2 and player == 1:
        print(player)
        print(computer)
        print("Computer Wins!")
    elif computer == 3 and player == 2:
        print(player)
        print(computer)
        print("Computer Wins!")
    elif computer == 1 and player == 3:
        print(player)
        print(computer)
        print("Computer Wins!")
    else:
        print("It's a tie!")

print("Thanks for playing!")