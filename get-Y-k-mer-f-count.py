import json
from collections import Counter

listn = []

with open("sorted_Y.txt") as f:
    for line in f:
        lineElements = line.split()
        listn.append(lineElements[1])

dict1 = Counter(listn)

def sortVal(item):
    return item[0]

arr = []

for key, value in dict1.items():
    arr.append([int(key), int(value)])

arr.sort(key=sortVal)

with open('k_Y_mer_dist.txt', 'w') as file:
    for i in range(0, len(arr)):
        file.write('%s\t%s\n' % (arr[i][0], arr[i][1]))

# Plot 2 distributions in gnu plot
# plot "k_X_mer_dist.txt" with line, "k_Y_mer_dist.txt" with line