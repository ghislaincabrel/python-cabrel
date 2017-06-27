#exercise 9.6
import math
class Quadrilateral:
	def __init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
		self.p1x= p1x
		self.p1y= p1y
		self.p2x= p2x
		self.p2y= p2y
		self.p3x= p3x
		self.p3y= p3y
		self.p4x= p4x
		self.p4y= p4y
	def __str__(self):
		return "A: (%s,%s)\nB: (%s,%s)\nC: (%s,%s) \nD: (%s,%s) "%(self.p1x,self.p1y,self.p2x,self.p2y,self.p3x,self.p3y,self.p4x,self.p4y)

	def getDistance(self,x1,y1,x2,y2):
		return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
		

class Parallelogram(Quadrilateral):
    
	def __init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
		Quadrilateral.__init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)

	def perimeter(self):
		return (Quadrilateral.getDistance(self.p1x,self.p1y,self.p2x,self.p2y)+Quadrilateral.getDistance(self.p2x,self.p2y,self.p3x,self.p3y)+Quadrilateral.getDistance(self.p3x,self.p3y,self.p4x,self.p4y)+Quadrilateral.getDistance(self.p4x,self.p4y,self.p1x,self.p1y))
		
	def __str__(self):
		return"paralellogram :\n %s"%Quadrilateral.__str__(self)

class Rectangle(Parallelogram):
	def __init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
		Parallelogram.__init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)

	def perimeter(self):
		return (Quadrilateral.getDistance(p1x,p1y,p2x,p2y)+Quadrilateral.getDistance(p2x,p2y,p3x,p3y))*2

	def areas(self):
		return Quadrilateral.getDistance(p1x,p1y,p2x,p2y)+Quadrilateral.getDistance(p2x,p2y,p3x,p3y)

	def __str__(self):
		return"rectangle :\n %s"%Quadrilateral.__str__(self)



class Square(Parallelogram)	:
	def __init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y):
		Parallelogram.__init__(self,p1x,p1y,p2x,p2y,p3x,p3y,p4x,p4y)

	def perimeter(self):
		return Quadrilateral.getDistance(p1x,p1y,p2x,p2y) *4

	def areas(self):
		return pow(Quadrilateral.getDistance(p1x,p1y,p2x,p2y) ,2)

	
	def __str__(self):
		return"square :\n %s"%Quadrilateral.__str__(self)



# create Parallelogram object
print("\n")
print("create Parallelogram object")
parallelogram = Parallelogram(1,2,2,5,5,6,5,9)
print(parallelogram)
print("the perimeter is :",parallelogram.perimeter())

# create rectangle object
print("\n")
print("create rectangle object")
rectangle= Rectangle(5,2,8,9,4,3,8,2)
print(rectangle)
print("the perimeter is :",rectangle.perimeter())
print("the areas is :",rectangle.areas())


# create Square object
print("\n")
print("create Square object")
square= Square(1,5,4,7,9,3,0,5)
print(square)
print("the perimeter is :",Square.perimeter())
print("the areas is :",Square.areas())



