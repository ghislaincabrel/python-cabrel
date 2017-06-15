#exercise 7.6
class Rectangle:

	def __init__(self,__length=1,__width =1):
		self.__length =__length
		self.__width = __width

	def getLength(self):
		return self.__length

	def getWidth(self):
		return self.__width

	def setLenght(self,__length):
		self.__length = __length if __length>0 and __length<20.0 else 1

	def setWidth(self,__width):
		self.__width = __width if __width>0 and __width<20.0 else 1

	def Perimeter(self):
		return (self.__length + self.__width)*2

	def Areas(self):
		return self.__length * self.__width

rectangle1 = Rectangle(5,2)
print("the perimeter of the rectngle is : ",rectangle1.Perimeter())
print("the areas of rectangle is : ",rectangle1.Areas())
print("input a new value for the width:",end=" " )
val = eval(input())
rectangle1.setWidth(val)
print("the new value of the width is : ",rectangle1.getWidth()) 
