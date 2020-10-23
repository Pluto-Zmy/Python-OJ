def isHd(n):
	return n == (int("".join(sorted(list(str(n)), reverse=True))) - int("".join(sorted(list(str(n))))))
