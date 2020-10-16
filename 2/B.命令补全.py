commandNum = int(input())
commandList = [input() for i in range(commandNum)]
commandList.sort()
findString = input()
for currentCommand in commandList:
	if currentCommand.find(findString) == 0:
		print(currentCommand)
