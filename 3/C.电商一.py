from operator import itemgetter

bookNum = int(input())
bookInfo = [input().split() for i in range(bookNum)]
for i in bookInfo:
	for j in range(1, 7):
		i[j] = int(i[j])
for i in [6, 1, 4, 3, 2]:
	bookInfo = sorted(bookInfo, key=itemgetter(i), reverse=True)
bookInfo = sorted(bookInfo, key=itemgetter(5))

for i in bookInfo:
	for j in range(1, 7):
		i[j] = str(i[j])
	print(' '.join(i))
