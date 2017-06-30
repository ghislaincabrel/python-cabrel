#exercise 12.7
import math
print("program that illustrate rerasing an exception")
print("\n")
print("program that print the square root of a number")
print("enter a number:",end=" ")
number  = input()
try :
	number = eval(number)
	if number <0:
		raise ValueError ("the square root of a negative number is not possible")
	else:
		square =math.sqrt(number) 

except NameError:
	print('the number you have inter is not correct')
print("the square root of %d is :%f"%(number,square))