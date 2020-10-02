a=int(input("a:"))
b=int(input('b:'))
def add(a,b):
	c=a+b
	print(c)
	return c
def sub(a,b):
	c=a-b
	print(c)
	return c
def mul(a,b):
	c=a*b
	print(c)
	return c
def div(a,b):
	c=a/b
	print(c)
	return c

option=input("enter your option:")
if option==1:
	add(a,b)
elif option==2:
	sub(a,b)
elif option==3:
	mul(a,b)
else:
	div(a,b)
