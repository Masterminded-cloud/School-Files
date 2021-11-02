import numpy as np


f = open('a6.txt', 'r')

firstLine = f.readline()

dataList = []

for line in f:

    dataList.append(line.rstrip().split(','))

f.close()

print(dataList[0:2])
for item in dataList:

    for field in range(3,7):

        if item[field] == "":
item[field] = 0

print(dataList[1])

neighbourhood = np.array([item[1] for item in dataList])

dwelling = np.array([[int(item[3]),int(item[4]),int(item[5]),int(item[6])] for item in dataList])
print(dwelling[0,:])
dwellingList = []

neighbourhoodList = []

for item in dataList:

   neighbourhoodList.append(item[1])

   dwellingList.append([int(item[3]),int(item[4]),int(item[5]),int(item[6])])

neighbourhood = np.array(neighbourhoodList)

dwelling = np.array(dwellingList)

print(neighbourhood.shape)

print(dwelling.shape)




nonzero = dwelling[:,3] != 0

neighbourhood = neighbourhood[nonzero]

dwelling = dwelling[nonzero,:]

print(neighbourhood.shape)

print (dwelling.shape)

notsingle = dwelling[:,1] + dwelling[:,2]

print(notsingle[0:2])

dense_ratio = notsingle / dwelling[:,3]

print(dense_ratio[0:2])




dense_boolean = dense_ratio > 0.6

print(neighbourhood[dense_boolean])








