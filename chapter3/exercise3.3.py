#exercise
sum = 0
n=0
while  1 :
	print("Enter the gallons used  (-1 to end) :",end =" ")
	number = eval(input())
	if number==-1:
		break
	else:
		print("Enter the mille driven :",end=" ")
		number2 = eval(input())
		report = number2/number
	print("The miles / gallon for this tank was :%0.6f " % report)
	sum += report
	n+=1
print("the overall average mille/gallon was : %0.6f" %(sum/n))
	 