x = 0
y = 1
fib = 0
evenfib = []

while fib<4000000:
	fib = x + y
	x = y
	y = fib
	if fib % 2 == 0:
		evenfib.append(fib)
	else:
		continue

print(sum(evenfib))
