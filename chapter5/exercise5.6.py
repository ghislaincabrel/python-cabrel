#exercise 5.6
# bubble sort
def BubbleSort(value):
	n = len(value)
	for i in range(0,n):
		lesser= value[i]
		for j in range(0,n):
				if value[j] > lesser:
					temp = value[i]
					value[i]=value[j]
					value[j]=temp
list = []
print("enter the number of element of you list :",end =" ")
numb=eval(input())
for i in range(numb):
	print("element[%d] : " %(i+1),end=" ")
	number = eval(input())
	list.append(number)
print(" you have inter the list  :",end=" ")
print(list)
print("\n")
print("the list sorted :",end=" ")
BubbleSort(list)
print(list)
