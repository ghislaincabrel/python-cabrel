#exercise 9.5
import math
class Point :
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

	def getPoint(self,name):
		if name=='x':
			return self.x
		elif name == 'y':
			return self.y
		else:
			print("error")

	def setPoint(self ,name,value):
		if name =='x':
			self.x = value
		elif name=='y':
			self.y = value
		else:
			print("error")

	def __str__(self):
		return "%s  %5s"%(self.x,self.y)

class Circle:
	def __init__(self,x=0,y=0,raduis = 0.0):
		self.x=x
		self.y=y
		self.raduis= raduis

	def getPoint(self,name):
		if name=='x':
			return self.x
		elif name == 'y':
			return self.y
		else:
			print("error")

	def setPoint(self ,name,value):
		if name =='x':
			self.x = value
		elif name=='y':
			self.y = value
		else:
			print("error")

	def getRaduis(self):
		return self.raduis

	def setRaduis(self,value):
		self.raduis= value

	def areas(self):
		return math.pi * self.raduis **2

	def __str__(self):
		return "the center is (%d,%d) and the raduis is : %d "%(self.x,self.y,self.raduis)

class Cylindrer:
	def __init__(self,x=0,y=0,raduis = 0.0,height=0):
		self.x=x
		self.y=y
		self.raduis= raduis
		self.height = height

	def getPoint(self,name):
		if name=='x':
			return self.x
		elif name == 'y':
			return self.y
		else:
			print("error")

	def setPoint(self ,name,value):
		if name =='x':
			self.x = value
		elif name=='y':
			self.y = value
		else:
			print("error")

	def getRaduis(self):
		return self.raduis

	def setRaduis(self,value):
		self.raduis= value

	def getHeight(self):
		return self.height

	def setRaduis(self,value):
		self.height= value

	def areas(self):
		return 2* math.pi *self.raduis*self.height

	def volume(self):
		return math.pi *self.height *(self.raduis**2)

	def __str__(self):
		return "the center is (%d,%d) and the raduis is : %d the heigth is : %d"%(self.x,self.y,self.raduis,self.height)

# create point object
print("\n")
print("create point object")
point = Point(5,8)
print(point)
print ("X coordinate is:", point.getPoint('x'))
print ("Y coordinate is:", point.getPoint('y'))

# create Circle object
print("\n")
print("create Circle object")
circle = Circle( 37, 43, 2.5 )
print(circle)
print ("X coordinate is:", circle.getPoint('x'))
print ("Y coordinate is:", circle.getPoint('y'))
print ("Radius is:", circle.raduis)
print("the area is :",circle.areas())

# create cylindre  object
print("\n")
print("create cylindre  object")
cylinder = Cylindrer( 12, 23, 2.5, 5.7 )
print(cylinder)
print ("X coordinate is:", cylinder.getPoint('x'))
print ("Y coordinate is:", cylinder.getPoint('y'))
print ("Radius is:", cylinder.raduis)
print ("Height is:", cylinder.height)
print("the area is :",cylinder.areas())
print("the volume is :",cylinder.volume())
