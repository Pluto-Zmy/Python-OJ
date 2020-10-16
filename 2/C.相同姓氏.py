nameNum = int(input())
nameList = [input() for i in range(nameNum)]
nameList.sort()
findLastName = input()
for currentName in nameList:
	if currentName.split()[1] == findLastName:
		print(currentName.split()[0])
