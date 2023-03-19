print("Welcome to the quiz Championship")

play = input("Do you wanna play the game? ")
score = 0
if play.lower() != "yes":
	quit()
print("Okay! let's play :)")

answer = input("Who is the father of computer? : ")
if answer.upper() == "CHARLES BABBAGE":
	score += 1
else:
	score += 0
answer = input("who is the Richest person in the world? : ")
if answer.upper() == "ELON MUSK":
	score += 1
else:
	score += 0
answer = input("What is the capital city of Tamil Nadu? : ")
if answer.upper() == "CHENNAI":
	score += 1
else:
	score += 0


print("you've got " + str(score) + " Questions correct!")
print("you've got " + str((score/3)*100) + "%.") 