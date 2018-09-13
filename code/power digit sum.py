n = 2 ** 1000
print(n)

numbers_list = []

for x in range(0,len(str(n))):
	val = str(n)[x:x+1:1]
	print(val)
	numbers_list.append(val)

int_numbers_list = list(map(int, numbers_list))	
print(int_numbers_list)

total = 0

for y in range(0,len(int_numbers_list)):
	total = total + int_numbers_list[y]

print(total)
