from  basic_math import Number

def compute(digit):
	num = Number(digit)
	num=num.add(5)
	num.subtract(5)
	num.multiply(3)
	num.divide(2)
	return num.get()

print compute(10) # should be 15
