inputYear = int(input())
if inputYear % 4 == 0:
	if (inputYear % 100 == 0) and (inputYear % 400 != 0):
		print("No")
	else:
		print("Yes")
else:
	print("No")
