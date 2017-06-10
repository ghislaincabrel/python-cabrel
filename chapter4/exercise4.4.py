#exercise 4.4 part a
# determine whether a number is prime
def prime(number):
	sum = 0
	for i in range(1,number+1):
		if(number % i == 0):
			sum += i
	if (sum == number+1):
		print("the number ",number, "is a prime number ")
	else:
		print("the number ",number, "is not a prime number ")
	
			
print("enter a number :",end=" ")
number = eval(input())
prime(number)





