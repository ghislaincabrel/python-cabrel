#exercise13.8
#remove extra space
import re
print("enter  a string of word :",end=" ")
word = input()
if re.search(r' +',word):
	word=re.sub(' +',' ',word)
	print("the word whithout extra space is : ",word)
else:
	print("the word is :",word)




