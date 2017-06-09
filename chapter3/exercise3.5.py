#exercise3.5
#convert birary to decimal

print("enter a binary number :",end=" ")
number = input()
n = len(number)
binary = 0
for a in range(0,n):
	x = eval(number[a])
	binary = x * pow(2,n-1) + binary
	n = n-1
		
print("the decimal equivalent of binary ",eval(number)," is :",binary)


