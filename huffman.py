def frequency(data):
	split = list(data)
	res = [[],[]]
	for i in split:
		if (i not in res[0]):
			res[0].append(i)
			res[1].append(1)
		else: 
			counter = 0
			for j in res[0]:
				if (i == j):
					res[1][counter] += 1
				counter += 1
	return res

def chort(data):
	sorted_data = sorted(zip(*data), key=lambda x: x[1], reverse=True)
	result = [list(t) for t in zip(*sorted_data)]
	return result

def huffman(data):
	info = []
	x = chort(frequency(data))[1]
	while (len(x)>2):
		sum = x[-2:]
		res = sum[0]+sum[1]
		x = x[:-2]
		x.append(res)
		x.sort(reverse=True)
		for i in range(len(x)):
			if (res == x[i] and res != x[(i+1)%len(x)]):
				info.append(i)
	return x, info

def decode_huffman(data, info):
	msg = ["1", "0"]
	while (len(info)>0):
		item = msg.pop(info[-1:][0])
		info = info[:-1]
		msg.append(item+"1")
		msg.append(item+"0")
	return msg

data, info = huffman("Hola me llamo miguel")
print(decode_huffman(data, info))