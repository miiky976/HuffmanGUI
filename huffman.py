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
		# for i in range(len(x)):
		# 	if (res == x[i] and res != x[(i+1)%len(x)]):
		# 		info.append(i)
		info.append(len(x) - 1 - x[::-1].index(res))
	return x, info

def decode_huffman(data, info):
	msg = ["1", "0"]
	while (len(info)>0):
		item = msg.pop(info[-1:][0])
		info = info[:-1]
		msg.append(item+"1")
		msg.append(item+"0")
	return msg

def join_sort(data, msg):
	tar = chort(frequency(data))
	tar.append(msg)
	return tar

def write(data, msg):
	final = ""
	split = list(data)
	for i in split:
		counter = 0
		for j in msg[0]:
			if (i == j):
				if (counter == len(msg[0])):
					break
				final += msg[2][counter]
			counter += 1
	return final

# chain = "Hola me llamo miguel Angel ramos ruiz"
# data, info = huffman(chain)
# msg = decode_huffman(data, info)
# join = join_sort(chain, msg)
# writes = write(chain, join)
# print(join)