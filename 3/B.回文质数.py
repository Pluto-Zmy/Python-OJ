def prime(num):
	for i in range(2, num):
		if num % i == 0:
			return 0
	else:
		return 1


def palindrome(num):
	num = str(num)
	m = num[::-1]
	return num == m


a, b = map(int, input().split())
for i in range(a, b + 1):
	if palindrome(i) and prime(i):
		print(i)
