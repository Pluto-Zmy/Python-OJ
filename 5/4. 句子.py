def end_of_dot(sentence):
	return sentence[-1] == "."


def fun(sentence):
	res = list(sentence)
	if not res[0].isupper():
		res[0] = res[0].upper()
	if not end_of_dot(res):
		res.append(".")
	return "".join(res)
