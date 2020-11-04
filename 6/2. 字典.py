def merge(a, b):
	s = []
	for i in a:
		for j in b:
			if i == j:
				a[i] += b[j]
				s.append(j)
	for k in range(0, len(s)):
		del b[s[k]]
	a.update(b)
	c = sorted(a.items(), key=lambda d: d[0])
	return dict(c)


a = eval(input())
b = eval(input())
print(merge(a, b))
