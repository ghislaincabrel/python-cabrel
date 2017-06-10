# exercise 4.6
import random 
def question():
	rand =random.randrange(1,9)
	rand2 =random.randrange(1,9)
	print("How is ",rand," times ",rand2 ," ?",end =" ")
	return rand2*rand


answer = question()
number = eval(input())
while 1:
	if answer == number :
		print("very goog")
		answer = question()
		number = eval(input())
		
	else:
		print("NO.please try agiant :",end=" ")
		number = eval(input())