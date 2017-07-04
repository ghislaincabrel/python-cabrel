#exercise 13.7
import re
def convertion(val):
	val2 = [ ]
	for x in val :
		x=int(re.sub(r'\$','',x))
		pound = str(0.667*x)+'£'
		val2.append(pound)
	print(val2)

val = ['5$','25$','36$','89$','25$','548$','20$']
convertion(val)
