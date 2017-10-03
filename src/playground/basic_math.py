

class Number(object):
	def __init__(self,x):
		self.x = x

	def add(self,y):
		return Number(self.x  + y)

	def subtract(self,y):
		return Number(self.x - y)

	def multiply(self,y):
		return Number(self.x * y)

	def divide(self,y):
		return Number(self.x / y)

	def get(self):
		return self.x



