from random import randint
import time
import sys

# This array will be used for comparison. We will reference them by 0, 1, 2
possibleChoices = ["Rock", "Paper", "Scissors"]

def whoWon(player, computer):
    
    if (player == computer):  print("It's a Tie!\n")
    if (player == "r"):
        if(computer == 2):
            print('Yay! You won! Computer chose ' + possibleChoices[computer])
        elif(computer == 1):
            print('Oh no, you\'ve lost. Computer chose ' + possibleChoices[computer])
    if(player == "p"):
        if(computer == 0):
            print('Yay! You won! Computer chose ' + possibleChoices[computer])
        elif(computer == 2):
            print('Oh no, you\'ve lost. Computer chose ' + possibleChoices[computer])
    if(player == "s"):
        if(computer == 1):
            print('Yay! You won! Computer chose ' + possibleChoices[computer])
        elif(computer == 0):
            print('Oh no, you\'ve lost. Computer chose ' + possibleChoices[computer])



keepPlaying = True
print('Welcome to Rock Paper Scissors - Python Edition!')
while (keepPlaying):
    print('Let\'s play!\n')
    playerChoice = input('Press "R" for Rock, "P" for Paper, or "S" for Scissor\n').lower()
    computerChoice = randint(0,2)
    print('Great choice! Here we go! \n\n')
    for i in range(0, 3):
        time.sleep(1)
        print(possibleChoices[i])
    time.sleep(1)
    print('Shoot!\n')
    time.sleep(1)
    whoWon(playerChoice, computerChoice)
    keepPlaying = int(input("Would you like to keep playing? 1 for yes, 0 for no\n"))
    if(keepPlaying == 0): sys.exit(0)