import string

def is_pangram(s):
	#return set(string.ascii_lowercase) <= set(s.lower())
	# set: https://wikidocs.net/1015
	s = s.lower()
	for i in string.ascii_lowercase:
		if i not in s:
			return False
	return True

pangram = "The quick, brown fox jumps over the lazy dog!"
res = is_pangram(pangram)
print(res)