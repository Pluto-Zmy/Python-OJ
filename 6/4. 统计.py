words = ""
while True:
	a = input()
	if a == "!!!!!":
		break
	words = words + " " + a
words = words.lower()
words = words.replace('!', ' ').replace(',', ' ').replace('.', ' ').replace(':', ' ').replace('*', ' ').replace('?', ' ')
words = words.split()
s = {}
for i in words:
	if i in s:
		s[i] += 1
	else:
		s[i] = 1
s = list(s.items())
s.sort(reverse=False, key=lambda x: x[0])
s.sort(reverse=True, key=lambda x: x[1])

print(len(s))
for i in range(min(len(s), 10)):
	word, count = s[i]
	print(word + "=" + str(count))
