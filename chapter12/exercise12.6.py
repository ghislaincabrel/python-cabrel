# exercise 12.6
class Employe:
	def __init__(self,first,last,salary,departement):
		self.fisrtName = first
		self.lastName = last 

		try:
			self.salary = salary
			assert self.salary >0
		except AssertionError :
			print("the salary cannot be negative please correct you value")

		self.departement = departement
		
	def __str__(self):
		return " first Name :%s \n last Name : %s\n salary : %d\n departement : %s\n"%(self.fisrtName,self.lastName,self.salary,self.departement)

employe1=Employe('ghislain','cabrel',250000,'software')
print(employe1)

employe2 = Employe('ghislain','cabrel',-250000,'software')
print(employe2)

		
	