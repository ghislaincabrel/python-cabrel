#exercise 13
import re
print("Enter a string :",end =" ")
chaine = input()
count1,count2,count3,count4=0,0,0,0
for x in chaine:
	if re.match(r"[0-9]",x):
		count1+=1
	elif re.match(r"[a-z-A-Z]",x):
		count2+=1
	elif re.match(r" ",x):
		count3+=1
	elif re.match(r"\s",x):
		count4+=1

print("the string you have inter have :",count1,"digits")
print("the string you have inter have :",count2,"words")
print("the string you have inter have :",count3,"whitespace characters")
print("the string you have inter have :",count4,"non_digits characters")