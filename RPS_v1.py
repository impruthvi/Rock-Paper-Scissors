print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1 make your Move: ")
print("NO CHEATTING!\n\n"*30)
player2 = input("Player2 make your Move: ")


if player1 ==  player2 :
    print("it's a tie!")
elif player1 == "Rock":
    if player2 == "Scissors":
       print("player1 is win!!")
    if player2 == "Paper":
        print("player2 is win!!")

elif player1 == "Paper":
    if player2 == "Rock" :
        print("player1 is win!!")
    elif player2 == "Scissors" :
         print("player2 is win!!")


elif player1 == "Scissors":
    if player2 == "Paper" :
        print("player1 is win!!")
    elif player2 == "Rock" :
         print("player2 is win!!")
else:
    print("make right choise")