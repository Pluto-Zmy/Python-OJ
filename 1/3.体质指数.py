weight, height = map(float, input().split())
BMI = weight / (height ** 2)
if BMI < 18.5:
	level = 'A'
elif 18.5 <= BMI < 24:
	level = 'B'
elif 24 <= BMI < 28:
	level = 'C'
elif BMI >= 28:
	level = 'D'
print("%s" % level + ":" + "%.2f" % BMI)
