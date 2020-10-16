n, s = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]
time = []
for cur in info:
	if cur[0] < s:
		time.append((s - cur[0]) / cur[1])
maxTime = max(time)
print("%.2f" % maxTime)
