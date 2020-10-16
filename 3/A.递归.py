def fun(n, a):
	if n == 1:
		return 1 + a + a * a
	else:
		return fun(n - 1, a) + a ** (n + 1)


n, a = map(int, input().split())
print(fun(n, a))
