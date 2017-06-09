#exercise3.5
#convert birary to decimal

print("enter a binary number :",end=" ")
number = input()
n =len(number)
list = []
binary = 0
for i in range(0,n-1):
	val = eval(number[i])
	list.append(val)
i=2
while 0 < i :
	if i in list:
		print("the number",number," you have inter is not a binary number .enter again ")
		print("\n")
		print("enter a binary number :",end=" ")
		number = input()
		n = len(number)
	else:
		break
	i+=1
			
for a in range(0,n):
	x = eval(number[a])
	binary = x * pow(2,n-1) + binary
	n = n-1
		
  
print("the decimal equivalent of binary ",eval(number)," is :",binary)
