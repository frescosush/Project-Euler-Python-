palindromes = []

for x in range(100,999):
	for y in range (100,999):
		candidate = x * y
		candidate_string = str(candidate)
		if len(candidate_string) == 5:
			firsthalf = candidate_string[0:2:1]
			secondhalf = candidate_string[3:5:1]
			secondhalf = secondhalf[::-1]
			if firsthalf == secondhalf:
				palindromes.append(candidate_string)
		elif len(candidate_string) == 6:
			firsthalf = candidate_string[0:3:1]
			secondhalf = candidate_string[3:6:1]
			secondhalf = secondhalf[::-1]
			if firsthalf == secondhalf:
				palindromes.append(candidate_string)

for x in range(0,len(palindromes)-1):
	largest = palindromes[0]
	next = palindromes[x+1]
	if next > largest:
		largest = next
	else:
		next = palindromes[x+1]	

print(palindromes)