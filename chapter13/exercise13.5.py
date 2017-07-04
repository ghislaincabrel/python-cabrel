#exercise 13.5
import re
print("enter your number :",end=" ")
number = input()
expression = r" ^[ ][0-9]+([.]{1})?[0-9]+[ ]$ "
if re.search(expression,number):
	print("the number is valid")
else:
	print("the number is not valid")