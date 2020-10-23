def fib(n, fib_num={0: 1, 1: 1}):
	if n in fib_num:
		return fib_num[n]
	res = fib(n - 1) + fib(n - 2)
	fib_num[n] = res
	return res


def PrintFN(m, n):
	res = []
	fib_num = [fib(i) for i in range(1, 27)]
	for num in range(m, n + 1):
		if num in fib_num:
			res.append(num)
	return res
