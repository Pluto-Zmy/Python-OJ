def create():
	poke = []
	for i in suit:
		for j in d:
			poke.append(i + j)
	return poke


def shufflecard(pokers):
	random.shuffle(pokers)
	return pokers


def deal(pokers, n):
	own = []
	for i in range(20):
		if (i % 4) == (n - 1):
			own.append(poker[i])
	print("第%d个玩家拿到的牌是：" % n, end="")
	for i in range(5):
		print(own[i][0], end="")
		if i != 4:
			print(own[i][1:], end=",")
		else:
			if n != 4:
				print(own[i][1:])
			else:
				print(own[i][1:], end="")
