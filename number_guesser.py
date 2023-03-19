import random
score = 0
top_of_range = input("Enter the limit : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0.")
        quit()

correct_number = random.randint(0, top_of_range)
while True:
    user_guess = input("Make a Guess: ")
    if user_guess == correct_number:
        print("You got it right!")
        break
    else:
        print("you got it wrong!")
    break






print(correct_number)