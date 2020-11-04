bin_str = bin(int(input()[4:-1], base=16))[2:]
lst = list(('0' * (8 - len(bin_str)) + bin_str)[::-1])
res = [True if i == '1' else False for i in lst]
print(res)
