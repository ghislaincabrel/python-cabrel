def Binarysearch(list,key):
	n=len(list)
	middle = n/2
	while middle != 1:
		if key == list[middle]:
			print("the element is found at index: ",list.index(key))
			key = list.index(key)
			break
		elif key != list[middle] and key > list[midel]:
			middle = middle / 2 + middle
		elif  key != list[middle] and key < list[midel]:
			middle = middle / 2
		else:
			print("the element is not found")
			key = -1
	return key
  
	
	
print("enter a keys:",end= " ")
key=eval(input())
list=list(range(1024)) 
Binarysearch(list,key)
		
		

