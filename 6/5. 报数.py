def func(n, k):
	for i in range(1, n + 1):
		c.append(i)
	count = 1
	while len(c) != 1:
		c.append(c.pop(0))
		count += 1
		if count == k:
			del c[0]
			count = 1
	return c


n = int(input())
k = int(input())
c = []
print(func(n, k))
