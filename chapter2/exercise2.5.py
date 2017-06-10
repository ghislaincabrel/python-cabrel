#exercise 2.5
#program that reads the raduis of the cicle and print the diameter ,the circonference and the area

#promt the user to enter the raduis
print("enter the raduis : ",end=" ")
raduis = eval(input())
print("the diameter is :",raduis*2)
print("the circonference is : ",(3.14159 * ( 2 * raduis)))
print("the area is : ",(raduis * raduis * 3.14159))