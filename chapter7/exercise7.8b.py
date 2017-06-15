#exercise 7.8
# game of tictactoe  humnan and computer
import random
class TicTacToe:
	def __init__(self):
		self.cells = [" "," "," "," "," "," "," "," "," ",]
	def Display(self):
		print(" %s | %s | %s " %(self.cells[6],self.cells[7],self.cells[8]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[3],self.cells[4],self.cells[5]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[0],self.cells[1],self.cells[2]))

	def update(self,number,player):
		if self.cells[number]==" ":
			self.cells[number]=player
				
	def updateMachine(self,number,player):
		while 1:
			if self.cells[number]!=" ":
				number=random.randint(0,8)
			else:
				self.cells[number]=player
				break
			


	def end(self):
		count = 0
		for i in range(len(self.cells)):
			if self.cells[i]!=' ':
				count+=1
		if count==9:
			return True

	def winner(self):
		if val=='X' :
			if (self.cells[0]==self.cells[1]==self.cells[2]=='X' or self.cells[3]==self.cells[4]==self.cells[5]=='X'or self.cells[6]==self.cells[7]==self.cells[8]=='X'or self.cells[6]==self.cells[3]==self.cells[0]=='X'or self.cells[7]==self.cells[4]==self.cells[1]=='X'or self.cells[8]==self.cells[5]==self.cells[2]=='X') :
				print("the game is end ",player1," is the winner")
				return True
			elif (self.cells[0]==self.cells[1]==self.cells[2]=='O' or self.cells[3]==self.cells[4]==self.cells[5]=='O'or self.cells[6]==self.cells[7]==self.cells[8]=='O'or self.cells[6]==self.cells[3]==self.cells[0]=='O'or self.cells[7]==self.cells[4]==self.cells[1]=='O'or self.cells[8]==self.cells[5]==self.cells[2]=='O') :
				print("the game is end ,the computer  is the winner")
				return True

		elif val =='O':
			if (self.cells[0]==self.cells[1]==self.cells[2]=='O' or self.cells[3]==self.cells[4]==self.cells[5]=='O'or self.cells[6]==self.cells[7]==self.cells[8]=='O'or self.cells[6]==self.cells[3]==self.cells[0]=='O'or self.cells[7]==self.cells[4]==self.cells[1]=='O'or self.cells[8]==self.cells[5]==self.cells[2]=='O') :
				print("the game is end" , player1 ," is the winner")
				return True

			elif (self.cells[0]==self.cells[1]==self.cells[2]=='X' or self.cells[3]==self.cells[4]==self.cells[5]=='X'or self.cells[6]==self.cells[7]==self.cells[8]=='X'or self.cells[6]==self.cells[3]==self.cells[0]=='X'or self.cells[7]==self.cells[4]==self.cells[1]=='X'or self.cells[8]==self.cells[5]==self.cells[2]=='X') :
				print("the game is end ,the computer is the winner")
				return True
			
	

board = TicTacToe()
board.Display()
print("welcome to the tic tac toe game ")
print("now you are playing with the computer")
print("enter you name :")
print("player 1: ",end=" ")
player1 = input()

print(player1," do you want to be X or O ?  :",end =" ")
val = input().upper()
if val == 'X':
    pl1= 'X'
    pl2 = 'O'
else:
	pl2= 'X'
	pl1 = 'O'
    
while 1: 
	print(player1 ,"play :",end=" ")
	val1 = eval(input())
	val1-=1
	board.update(val1,pl1)
	board.Display()
	if board.winner():
		break
	if board.end():
		print("\n")
		print("the game is war ")
		break

	print("\n")
	val2 = random.randint(0,8)
	board.updateMachine(val2,pl2)
	board.Display()
	if board.winner():
		break
	if board.end():
		print("the game is war ")
		break