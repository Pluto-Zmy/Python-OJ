def get_upper(string):
	return ''.join([ch for ch in string if ch.isupper()])


bookNum = int(input())
bookList = [input() for i in range(bookNum)]
bookListPlus = []
for currentName in bookList:
	bookListPlus.append([get_upper(currentName), currentName])
sortedListPlus = sorted(bookListPlus, key=(lambda x: x[0]))
for i in sortedListPlus:
	print(i[1])
