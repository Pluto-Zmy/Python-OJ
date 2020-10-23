def multiply(a, b, p, q, r):
	res = [[0 for x in range(r)] for y in range(p)]
	for i in range(p):
		for j in range(r):
			for k in range(q):
				res[i][j] += a[i][k] * b[k][j]
	return res
