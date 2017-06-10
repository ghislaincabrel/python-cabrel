# exercise 4.7
# game of  guess number 
import random

def game():
	print("i have a number between 1 and 1000.")
	print("can you guess my number ?")
	print("please type you first guess: ",end=" ")
	guess= random.randrange(1,1000)
	return guess

guess = game()
number = eval(input())
while 1:
	if (number == guess) :
		print("Excellent ! you guessed the number !")
		print("would you like to play again (y or n) :",end=" ")
		ans = input().lower()
		if ans == 'y':
			guess = game()
			number = eval(input())
		else:
			break
	else:
		if number >guess:
			print("To high.\nTry again :",end=" ")
			number = eval(input())
		else :
			print("To low.Try again :",end=" ")
			number = eval(input())

