# exercise7.3
class Complexe:
	"complexe class"
	def __init__(self,realPart = 0,imaginaryPart = 0):
		self.realPart = realPart
		self.imaginaryPart = imaginaryPart

	def Addition(self,second):
		real=self.realPart + second.realPart
		imaginar=self.imaginaryPart+second.imaginaryPart
		return  real,imaginar
	

	def Subtration(self,second):
		real=self.realPart - second.realPart
		imaginar=self.imaginaryPart-second.imaginaryPart
		return  real,imaginar
	
 
print("complex number 1 and 2:")
c1=Complexe(4,5)
c2=Complexe(4,-5)
print(c1.realPart," + ",c1.imaginaryPart ,"*i")
print(c2.realPart," + ",c2.imaginaryPart ,"*i")
print("the sum of complexe 1 and 2 is : ",Complexe.Addition(c1,c2))
print("the Subtration  of complexe 1 and 2 is : ",Complexe.Subtration(c1,c2))