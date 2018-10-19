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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'has word less than 100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'good')

wc = {}  # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 
		else:
			wc[word] = 1 # give new key to wc dictionary
for word in wc:
	if wc[word] > 1000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input ('What word you want to find?')
	if word == 'q':
		print('Thank you for using')
		break
	if word in wc:
		print(word, 'Has appeared', wc[word])
	else:
		print('This word is not in the list.')

