player1_win = 0
player2_win = 0
winning_score = 3

while player1_win<winning_score and player2_win<winning_score:
    print(f"Player1 Score: {player1_win} Player2 Score: {player2_win}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")

    player1 = input("Player1 make your Move: ").lower()
    print("NO CHEATTING!\n\n"*30)
    player2 = input("Player2 make your Move: ").lower()


    if player1 ==  player2 :
        print("it's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("player1 is win!!")
            player1_win += 1
        if player2 == "paper":
            print("player2 is win!!")
            player2_win += 1

    elif player1 == "paper":
        if player2 == "rock" :
            print("player1 is win!!")
            player1_win += 1
        elif player2 == "scissors" :
            print("player2 is win!!")
            player2_win += 1


    elif player1 == "scissors":
        if player2 == "paper" :
            print("player1 is win!!")
            player1_win += 1            
        elif player2 == "rock" :
            print("player2 is win!!")
            player2_win += 1
    else:
        print("make right choise")
# if player1_win > player2_win:
#     print("CONGRATS, YOU WON!")
# elif player1_win == player2_win:
#     print("IT'S A TIE")
# else: 
#     print("THE Player2 WON...")