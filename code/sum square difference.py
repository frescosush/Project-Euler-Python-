sum_squares = 0
squares_sum = 0

for x in range(1,101):
	sum_squares = sum_squares + (x*x)

for x in range(1,101):
	squares_sum = squares_sum + x
	if x == 100:
		squares_sum = squares_sum * squares_sum

print(sum_squares)
print(squares_sum)

difference = squares_sum - sum_squares
print("Difference:",difference)
