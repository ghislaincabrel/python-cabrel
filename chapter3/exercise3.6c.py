# exercise 3.6 part c
# program to compute the value of e^x
print("Enter a number")
nunber = eval(input())
fact=1
expo = 0
for i in range(1,11):
	for x in range(1,i+1):
		fact = fact*x
	expo = pow(nunber,x)/fact + expo
	fact=1
print(expo+1)