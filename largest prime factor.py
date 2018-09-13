x = 600851475143 
y = 2
xfactors = []
yfactors = []

while x != y:
	if x % y == 0:
		x = x /y
		xfactors.append(x)
		yfactors.append(y)
	else:
		y = y + 1
print(y)
print(xfactors)
print(yfactors)