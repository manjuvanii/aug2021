
while True:
    choice = input("Do you wish to play a game of Rock-paper-scissor? y/n\n")
    if choice == 'y':
        print("Choose rock, paper or scissor")
        player1 = str(input("Player 1 Enter your choice: "))
        player2 = str(input("Player 2 Enter your choice: "))
        if player1 == player2:
            print("Its a Tie!")
        elif player1 == "rock":
            if player2 == "paper":
                print("player 2 wins!!")
            else:
                print("player1 wins!!")
        elif player1 == "paper":
            if player2 == "scissor":
                print("player 2 wins!!")
            else:
                print("player1 wins!!")

        elif player1 == "scissor":
            if player2 == "rock":
                print("player 2 wins!!")
            else:
                print("player1 wins!!")
        else:
            print("not valid choice")

    else:
        print("Run again to play!!")
        break
