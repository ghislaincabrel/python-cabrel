# exercise 4.4 part b
# print all the prime number between 2 and 1000
def prime(number):
	sum = 0
	list = []
	for i in range(1,number+1):
		if(number % i == 0):
			sum += i
	if (sum == number+1):
		list.append(number)
		for i in range(len(list)):
			print(list[i],end=" ")
				
print("List of prime number between 2 and 1000 :",end=" ")
for x in range(2,100):
	prime(x)

