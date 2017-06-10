# exercise 4.5
#  fuction to determine whether a number is perfect 
import math
def perfect(number):
	sum =0
	list=[ ]
	for i in range(1,1000):
		if (number % i == 0):
			sum += i
			list.append(i)
	sum -= number
	list.remove(number)
	if (sum == number ):
		print("factor of ",number ," are :",end = " ")
		print(list)
		print("the number ",number, "is perfect")

	else:
		print("factor of ",number ," are :",end = " ")
		print(list)
		print("the number ",number, "is not perfect")

print("enter a positive number :",end=" ")
number = math.fabs(eval(input())) 
perfect(number)