#exercise 3.4
#
#prompt the user to enter a number 
print("enter  a five-digit intergers:",end=" ")
number = input()
while len(number) != 5:
	print("the number you have inter is not a five-digit interger ")
	print("\n")
	print("enter  a five-digit intergers:",end=" ")
	number = input()
first = eval(number[0])
last = eval(number[-1])
if first== last:
	print("the number ",eval(number),"is polindrome")
else:
	print("the number ",eval(number),"is not polindrome")