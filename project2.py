# Author Name -Akash Sarkar
# College Finder Internship Project 2 
# Rock Paper Scissors Game 
# Date - 11.07.22 

##user input 
print("Lets play Rock,Paper and Scissor")
player1 = str(input("choose between r,p,s [Rock,Paper or Scissor"))
player2 = str(input("choose between r,p,s [Rock,Paper or Scissor"))

##logic using conditional checks 
#logic for rock
if (player1 == 'r') and (player2 == 'r'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("that's a tie")
elif (player1 == 'r') and (player2 == 'p'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player2 has own the game")
elif (player1 == 'r') and (player2 == 's'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player1 has own the game")

#logic for paper
if (player1 == 'p') and (player2 == 'p'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("that's a tie")
elif (player1 == 'p') and (player2 == 'r'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player1 has own the game")
elif (player1 == 'p') and (player2 == 's'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player2 has own the game")

#logic for scissor
if (player1 == 's') and (player2 == 's'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("that's a tie")
elif (player1 == 's') and (player2 == 'r'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player2 has own the game")
elif (player1 == 's') and (player2 == 'p'):
    print("player 1 choose {option} and player 2 choose {option2}".format(player1=option,player2=option2))
    print("Player1 has own the game")

#logic for error
else: print("Error! please choose correct option")
