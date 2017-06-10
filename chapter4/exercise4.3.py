#exercise 4.3
# converting from fahrenheit to ceisuis 
def fahrenheit(c ):
	fah = (9/5 ) * c + 32
	return fah
	
print("enter a celsuis temperatute :",end=" ")
number = eval(input())
print("the fahrenheit equivalent of the celsuis is : %.1f" %(fahrenheit(number)))

