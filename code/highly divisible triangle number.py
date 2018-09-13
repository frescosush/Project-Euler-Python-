from functools import reduce

def triangle_generator(n):
	total = 0
	list_triangles = []
	for i in range(1, n):
		total = total + i
		list_triangles.append(total)
	return list_triangles

def factors(n):    
    factor_amount = set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    return len(factor_amount)

x = 100001
final_triangles = triangle_generator(x)
list_of_factors = []

for x in range (0,len(final_triangles)):
	if factors(final_triangles[x]) < 500:
		list_of_factors.append(factors(final_triangles[x]))
	else:
		print("Number:",final_triangles[x])
		print(factors(final_triangles[x]))
		break
