import random

mainList = [random.randint(0, 4) for count in range(10)]

print('Printing the main list before grouping - ', mainList)

allNumCounts = {}

for num in range(5):
    allNumCounts[num] = 0

for num in mainList:
    if num in allNumCounts:
        allNumCounts[num] = allNumCounts[num] + 1

seenOnce = []
seenMoreThanOnce = []
notSeen = []
for num in allNumCounts:
    if allNumCounts[num] > 1:
        seenMoreThanOnce.append(num)
    elif allNumCounts[num] == 1:
        seenOnce.append(num)
    else:
        notSeen.append(num)

print(seenMoreThanOnce, seenOnce, notSeen)
