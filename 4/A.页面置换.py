n, m = map(int, input().split())
visit = input().split()
cache = []
loadTime = 0
for page in visit:
	if page not in cache:
		loadTime += 1
		if len(cache) < n:
			cache.append(page)
		else:
			cache.pop(0)
			cache.append(page)
	else:
		cache.remove(page)
		cache.append(page)
print(loadTime)
cache = list(map(int, cache))
cache.sort()
print(" ".join(list(map(str, cache))))
