# exercise 3.6

print("enter a nonnagative number :",end=" ")
number= eval(input())
while 1:
	if number<0:
		print("the number you have inter in not correct :")
		print("\n")
		print("enter a nonnagative number :",end=" ")
		number= eval(input())
	else:
		break

fact =1
for i in range(1,number+1):
	fact = fact*i

print("the factorial of ",number," is :",fact)


