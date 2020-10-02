import random
options=("rock","paper","scissor")
print(options)
p1=input("Enter option:")
p2=random.choice(options)
#conditions
if ((p1=='rock' and p2=='paper') or (p1=='paper' and p2=='rock')):
	print('paper wins')
	result='paper'
elif ((p1=='scissor' and p2=='rock') or (p1=='rock' and p2=='scissor')):
	print('rock wins')
	result='rock'
else:
	print('scissor wins')
	result='scissor'

#printing wheather p1 wins or p2 wins

if result==p1:
	print('p1 wins')
else:
	print('p2 wins')



