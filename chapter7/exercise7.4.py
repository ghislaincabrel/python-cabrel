#exercise 7.4
from fractions import *
class RationalNumber:
	def __init__(self,numerator =1,denominator=1):
		self.numerator = numerator
		self.denominator = denominator

	def Addition(self,second):
		f1 =Fraction(self.numerator,self.denominator)
		f2=Fraction(second.numerator,second.denominator)
		print("the sum of ",f1," and ",f2," is :",f1+f2)

	def Subtration(self,second):
		f1 =Fraction(self.numerator,self.denominator)
		f2=Fraction(second.numerator,second.denominator)
		print("the difference of ",f1," and ",f2," is :",f1-f2)

	def Mutiplication(self,second):
		f1 =Fraction(self.numerator,self.denominator)
		f2=Fraction(second.numerator,second.denominator)
		print("the product of ",f1," time  ",f2," is :",f1*f2)

	def Division(self,second):
		f1 =Fraction(self.numerator,self.denominator)
		f2=Fraction(second.numerator,second.denominator)
		print("the division of ",f1," and ",f2," is :",f1/f2)
	def Display(self):
		f1 =Fraction(self.numerator,self.denominator)
		print("the  rational Number  is :",self.numerator,"/",self.denominator)
		

fraction1= RationalNumber(4,5)
fraction2=RationalNumber(4,5)
RationalNumber.Addition(fraction1,fraction2)
RationalNumber.Subtration(fraction1,fraction2)
RationalNumber.Mutiplication(fraction1,fraction2)
RationalNumber.Division(fraction1,fraction2)
RationalNumber.Display(fraction1)
