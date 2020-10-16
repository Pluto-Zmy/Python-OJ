findChar = input()
stringNum = int(input())
stringList = [input() for i in range(stringNum)]
stringList.reverse()
for currentString in stringList:
	if currentString.upper().count(findChar.upper()) >= 3:
		print(currentString)
