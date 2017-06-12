#exercice 5.8
import random
dict = {}
for i in range(1,21):
	x=random.randrange(1,99)
	dict[i] =x
print(dict)
list = list(dict.values())
print("\n")
print("list of values :",end =" ")
list.sort()
print(list)
count=0
for i in range(len(list)):
	if  (list.count(list[i]) >= 2) :
		count+=1
	else:
		continue
print("\n")
if count != 0:
	print("the are duplicated value in the dictionary")
else:
	print("the are not duplicated value in the dictionary")


