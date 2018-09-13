def collatz(number):
	if number == 0:
		return "Number is 0"
	elif number % 2 == 0:
		return number // 2
	elif number % 2 == 1:
		result = 3 * number + 1


	return result

def find_largest(list):
	length = len(list)
	largest = list[0]
	for i in range (0,len(list)):
		ptr = list[i]
		if ptr > largest:
			print("index",i," is the largest number")
			print(ptr,"is larger than", largest)
			largest = ptr
		else:
			continue
	print("largest:",largest)


collatz_lengths = []

for x in range(1,1000001):
	n = x
	chain_len = 0
	while n != 1:
		n = collatz(int(n))
		chain_len += 1
	if n == 1:
		collatz_lengths.append(chain_len)

print(collatz_lengths)
find_largest(collatz_lengths)
