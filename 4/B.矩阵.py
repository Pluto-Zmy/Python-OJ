n, m = map(int, input().split())
time = int(input())
pos = [input().split() for i in range(time)]
mat = [[0 for j in range(m)] for k in range(n)]
cnt = 0
for cur in pos:
	for row in range(int(cur[0]) - 1, int(cur[2])):
		for col in range(int(cur[1]) - 1, int(cur[3])):
			mat[row][col] = 1
for row in mat:
	cnt += row.count(0)
print(cnt)
