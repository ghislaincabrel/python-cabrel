#exercise 2.7
#program that read 2 numbers and print whether the fist is the multiple of the second
print("enter 2 numbers ")
print("numner 1 :",end =" ")
numb1= eval(input())
print("numner 2 :",end =" ")
numb2= eval(input())
if numb1%numb2:
	print(numb1," is not a multiplle of ",numb2)
else:
	print(numb1," is  a multiplle of ",numb2)