data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0:
			print(len(data))
print('finish reading, total review number is', len(data))

sum_len = 0
for d in data:
	sum_len += len(d) 

print ('average is', sum_len/len(data))
