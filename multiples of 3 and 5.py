num1 = 3
num2 = 5
multiples = []

for x in range(0,1000):
	if x % 3 == 0:
		multiples.append(x)
	elif x % 5 == 0:
		multiples.append(x)

print(sum(multiples))
