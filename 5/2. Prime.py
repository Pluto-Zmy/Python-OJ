def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True


def primeSum(m, n):
	sum = 0
	for num in range(m, n + 1):
		if isPrime(num):
			sum += num
	return sum
