def bouncingBall(h, bounce, window):
	if h <= 0:
		return -1
	elif (bounce <= 0 or bounce >= 1):
		return -1
	elif window >= h:
		return -1
	else:
		cnt = 1
		while h * bounce >= window:
			cnt = cnt + 2
			h = h * bounce
		return cnt
		
a = bouncingBall(30, 0.66, 1.5)
print(a)