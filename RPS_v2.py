from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player= input("Player make your Move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else :
    computer = "scissors"
print(f"The Computer move {computer}")

if player ==  computer :
    print("it's a tie!")
elif player == "rock":
    if computer == "scissors":
       print("player is win!!")
    if computer == "paper":
        print("computer is win!!")

elif player == "paper":
    if computer == "rock" :
        print("player is win!!")
    elif computer == "scissors" :
         print("computer is win!!")


elif player == "scissors":
    if computer == "paper" :
        print("player is win!!")
    elif computer == "rock" :
         print("computer  is win!!")
else:
    print("make right choise")