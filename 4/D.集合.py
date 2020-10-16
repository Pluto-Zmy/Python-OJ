numA = int(input())
listA = list(map(int, input().split()))
numB = int(input())
listB = list(map(int, input().split()))
setA = set()
setB = set()
for num in listA:
	setA.add(num)
for num in listB:
	setB.add(num)
ins = sorted(setA.intersection(setB))
uni = sorted(setA.union(setB))
dif = sorted(setA.difference(setB))
for num in ins:
	print(num, end=" ")
print()
for num in uni:
	print(num, end=" ")
print()
for num in dif:
	print(num, end=" ")
