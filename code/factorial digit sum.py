import math
from math import factorial

x = math.factorial(100)
nums = []
total = 0
for y in range(0,len(str(x))):
	val = str(x)[y:y+1:1]
	total = total + int(val)

print(total)
