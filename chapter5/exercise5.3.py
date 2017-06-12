#exercise 5.3
print("enter a number")
list=[]
for i in range(20):
	print("number ",i+1," :",end =" ")
	number=eval(input())
	list.append(number)
	if(list.count(number)>=2):
		continue
	else:
		print("you have enter :",number)
print("end")

