words = open('text.txt').read().lower().split() #text into words

# get unique words
uniques = []
for word in words:
  if word not in uniques:
    uniques.append(word)

# list of unique words with their counts 
counts = []
for unique in uniques:
  count = 0              
  for word in words:     
    if word == unique:   
      count += 1         
  counts.append((count, unique))

counts.sort()            
counts.reverse()         

for i in range(len(counts)):
  count, word = counts[i]
 
  
for i in range(len(counts)):
	if (counts[0][0]==counts[i+1][0]):
		print("-")
		break
	else:
		print(counts[0][1])
		break


