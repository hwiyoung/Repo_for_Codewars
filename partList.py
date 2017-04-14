def partlist(arr):
	return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]

res = partlist(["I", "wish", "I", "hadn't", "come"])
print(res)