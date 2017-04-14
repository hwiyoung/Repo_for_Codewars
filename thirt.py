remainders = [1, 10, 9, 12, 3, 4]
def thirt(n):
	total = 0
	for i, num in enumerate(reversed(str(n))):
		# i: index, num: value
		total += int(num) * remainders[i%6]
	if n == total:
		return total
	else:
		return thirt(total)	# recursive
		
a = thirt(8529)
print(a)	# 79
a = thirt(85299258)
print(a)	# 31
a = thirt(5634)
print(a)	# 57
a = thirt(1111111111)
print(a)	# 71
a = thirt(987654321)
print(a)	# 30