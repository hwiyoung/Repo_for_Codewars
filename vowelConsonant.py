def get_count(words=''):
	vowel = 0
	consonant = 0
	
	#vowels = ['a', 'e', 'i', 'o', 'u']
	vowels = 'aeiou'
	consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
	
	try:
		words = words.lower()
		for word in words:
			if word in vowels:
				vowel += 1
			elif word in consonants:
				consonant += 1		
		return {'vowels':vowel, 'consonants':consonant}
	except:	# not isinstnace(words, str)
		return {'vowels':0, 'consonants':0}

res = get_count('Test')
print(res)
res = get_count('Here is some text')
print(res)
res = get_count('To be a Codewarrior or not to be')
print(res)
res = get_count('To Kata or not to Kata')
print(res)
res = get_count('aeiou')
print(res)
res = get_count()
print(res)