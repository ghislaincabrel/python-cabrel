#exercise 9.8
import datetime
i=datetime.datetime.now()
class Employee:
	def __init__(self, first , last, code):
		self.firstName = first
		self.lastName = last
		self.departementCode = code
	def __str__(self):
		return "%s  %s  \ncode : %d"%(self.firstName,self.lastName,self.departementCode)

class Date :
	def __init__(self,day,month,year):
		self.day=day
		self.month = month
		self.year = year
		self.birthday = [day,month,year]
	def __str__(self):
		return " birthday :%s "%self.birthday

class Boss(Employee,Date):
	def __init__(self,first,last,code,salary,day,month,year):
		Employee.__init__(self, first , last, code)
		Date.__init__(self,day,month,year)
		self.salary= salary
	def earnings(self):
		if (i.day==self.day and i.month==self.month and i.year==self.year):
			return self.salary + 10000
		else :
			return self.salary 
	def __str__(self):
		return " %5s: %s  \n %5s"%('Boss' ,Employee.__str__(self),Date.__str__(self))
class CommissionWorker( Employee ,Date):
	def __init__( self, first, last, code,salary, commission, quantity ,day,month,year):
		Employee.__init__(self, first , last, code)
		Date.__init__(self,day,month,year)
		self.salary= salary
		self.commission =commission
		self.quantity =quantity

	def earnings( self ):
		if (i.day==self.day and i.month==self.month and i.year==self.year):
			return self.salary + self.commission * self.quantity + 10000
		else :
			return self.salary + self.commission * self.quantity

	def __str__( self ):
		return " %5s: %s  \n %5s"%('CommissionWorker' ,Employee.__str__(self),Date.__str__(self))

class PieceWorker( Employee ,Date):
	def __init__( self, first, last, code ,wage, quantity,day,month,year ):
		Employee.__init__(self, first , last, code)
		Date.__init__(self,day,month,year)
		self.wagePerPiece=wage
		self.quantity= quantity
	def earnings(self):
		if (i.day==self.day and i.month==self.month and i.year==self.year):
			return self.quantity * self.wagePerPiece + 10000
		else :
			return self.quantity * self.wagePerPiece
	def __str__( self ):
		return " %5s: %s  \n %5s"%('PieceWorker' ,Employee.__str__(self),Date.__str__(self))
class HourlyWorker( Employee ,Date):
	def __init__( self, first, last,code, wage, hours ,day,month,year):
		Employee.__init__(self, first , last, code)
		Date.__init__(self,day,month,year)
		self.wage =wage
		self.hours = hours
	def earnings( self ):
		if (i.day==self.day and i.month==self.month and i.year==self.year):
			if self.hours <= 40:
				return self.wage * self.hours +100000
			else:
				return (40 * self.wage + ( self.hours - 40 ) *( self.wage * 1.5))+10000
		else :
			if self.hours <= 40:
				return self.wage * self.hours 
			else:
				return (40 * self.wage + ( self.hours - 40 ) *( self.wage * 1.5))
	def __str__( self ):
		return " %5s: %s  \n %5s"%('HourlyWorker' ,Employee.__str__(self),Date.__str__(self))


employees = [ Boss( "John", "Smith", 105,800.00 ,2,10,1995),
CommissionWorker( "Sue", "Jones", 201,200.0, 3.0, 150 ,5,8,1998),
PieceWorker( "Bob", "Lewis",521, 2.5, 200,8,5,1995 ),
HourlyWorker( "Karen", "Price", 210,13.75, 40 ,5,5,2001) ]

for employee in employees:
	print( "%s  earned $%.2f" % ( employee, employee.earnings() ))

