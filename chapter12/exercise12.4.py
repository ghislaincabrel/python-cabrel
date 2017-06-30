#exercise 12.4
print("division of 2 number ")
print("enter the numerator:",end=" ")
numerator= eval(input())
print("enter the numerator :",end=" ")
denominator = eval(input())
try:
	div = numerator/denominator
except Exception as exception :
	print(exception) 
else:
	print("the division of %f by %f is %f"%(numerator,denominator,div))



    
