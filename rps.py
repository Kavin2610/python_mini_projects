
'''requirements
2 player inputs 
score for each player
player should select an option
cpu should select an option 
use if condition to evaluate and write conditions to check for winner
print the winning prompt
ask would you like to play again use while loop
if yes loop else print the score finally
exit
'''


import random  #imported random to choose random nums

CPU_score = 0  #set cpu score to 0 initially 
player_score = 0 #set player score to 0 initially

options = ["rock","paper","scissors"] # options are given a list
while True: #used while loop to continue playing the game until player wants to exit
    print("Player enter your choice \n 1.Rock\n 2.paper\n 3.scissors") 
    player_input = (input("Enter your option: ")).lower() #player input is received and stored in lowercase by default

    cpu_input = random.randint(1,3) #cpu input is selected by random nums between one and three
    if cpu_input == 1:
        cpu_input = "rock" # converting nums into options
    elif cpu_input == 2:
        cpu_input = "paper"
    elif cpu_input == 3:
        cpu_input = "scissors"

    print("The computer selected:",cpu_input) #printing the cpu desicion to show the user what cpu selected

    if cpu_input == player_input: #checks whether the options are same and if yes then print tie
        print("The game is tie")
        CPU_score += 1   #here if tie both the cpu and the player gets one score
        player_score += 1
    elif ((cpu_input == "rock" and player_input == "scissor") or (cpu_input == "scissors" and player_input == "paper" )or (cpu_input == "paper" and player_input == "rock")):
        print("the cpu wins!") #checks for conditions if these set of conditions are true then the cpu wins
        CPU_score += 1
    elif ((player_input == "rock" and cpu_input == "scissor") or (player_input == "scissors" and cpu_input == "paper" )or (player_input == "paper" and cpu_input == "rock")):
        print("You won!") #if these conditions are true then player wins
        player_score += 1

    
    play = input("press x to exit and y to continue: ") #asking player whether he/she wants to play again
    if play == "x":
        break
    else:
        continue
result = (f'The player score is {player_score} and the computer score is {CPU_score}')
print(result)  #finally printing the overall score of the player and the cpu



