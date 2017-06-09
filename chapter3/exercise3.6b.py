# exercice 3.6 part b
print("extimation of : e = 1+1/1! +1/2! +1/3! ........")
fact=1
expo = 0
for i in range(1,11):
	for x in range(1,i+1):
		fact = fact*x
	expo = 1/fact +expo
	
	fact =1
print(expo+1)