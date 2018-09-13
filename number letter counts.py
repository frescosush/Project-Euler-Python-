up_to_ten = [[1,2,3,4,5,6,7,8,9], ["one","two","three","four","five","six","seven","eight","nine"]]
ten_to_twenty = [[10,11,12,13,14,15,16,17,18,19],["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]]
ten_to_hundred = [[10,20,30,40,50,60,70,80,90,100],["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","one hundred"]]

up_to_thousand = []

for x in range(0,len(up_to_ten[0])): #adds up to 9
	up_to_thousand.append(up_to_ten[0][x])

for x in range(0,len(ten_to_twenty[0])): #adds 10 to 19
		up_to_thousand.append(ten_to_twenty[0][x])

for x in range(0,len(ten_to_hundred[0]):
	for y in range(0,len(up_to_ten)[0]):
		up_to_thousand.append()
print(up_to_thousand)