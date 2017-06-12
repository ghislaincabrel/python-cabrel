#exercise 5.5
#

list1 = list(range(1000))
list2=[]
n=2
for i in range(len(list1)):
	for n in range(2,len(list1)):
		if (list1[i] % n ==0 and list1[i] != n):
			list1[i]=0	
	
	
for x in range(len(list1)):
	if list1[x] != 0:
		list2.append(list1[x])
	else:
		continue

#print(list1)		
print(list2)
