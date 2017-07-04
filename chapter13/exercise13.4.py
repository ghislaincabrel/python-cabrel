#exercise 13.4
import re
print("enter you xhtml string : ",end=" ")
chaine = input()
expression = r"^(http://)[\w.-]+.[a-zA-Z]{3}$"
if re.search(expression,chaine):
	print("the urml is correct")
else:
	print("the urml is not correct")
