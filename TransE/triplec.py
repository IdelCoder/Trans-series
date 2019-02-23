# triplet classification
import numpy as np
dev = '../data/test/' + 'wn11dev2id.txt'
test = '../data/test/' + 'wn11test2id.txt' 
rel_num = 11
# get the threshold from dev set
threshold = dict()
# valid triple map {rel: triple list}
vtm = dict()
itm = dict()
init = False
batchId = 0
validSize = 0
totalSize = 0
thresholds = {i: (0, 0) for i in range(rel_num)}
testFlag = False

def tripleClassify(ret):
    rel = batchId - 1
    validScores, invalidScores = consList(ret)
    correctC = 0
    thre = thresholds[rel][0]
    for i in range(validSize):
        if validScores[i] <= thre:
            correctC += validSize - i
            break
    invalidSize = totalSize - validSize
    for i in range(invalidSize):
        if invalidScores[i] >= thre:
            correctC += invalidSize - i
            break
    print("rel {}'s accuracy is: {}, {}, {}".format(rel, float(correctC)/totalSize, correctC, totalSize))

def class1(f):
    with open(f) as ff:
        for row in ff:
            lst = row.split()
            head = int(lst[0])
            tail = int(lst[1])
            rel = int(lst[2])
            flag = int(lst[3])
            if flag == 1:
                if rel not in vtm:
                    vtm[rel]=list()
                vtm[rel].append([head, tail, rel])
            else:
                if rel not in itm:
                    itm[rel]=list()
                itm[rel].append([head, tail, rel])

# output batch
def getbatch(batchsize):
    global validSize, totalSize, batchId, init
    if not init:
        if testFlag:
            class1(test)
        else:
            class1(dev)
        init = True
    validtriples = vtm[batchId]
    invalidtriples = itm[batchId]
    validSize = len(validtriples)
    totalSize = validSize + len(invalidtriples)
    print("{} has {} instances\n".format(batchId, totalSize))
    ph = np.zeros(batchsize, dtype = np.int32)
    pt = np.zeros(batchsize, dtype = np.int32)
    pr = np.zeros(batchsize, dtype = np.int32)
    for i in range(validSize):
        ph[i] = validtriples[i][0]
        pt[i] = validtriples[i][1]
        pr[i] = validtriples[i][2]
    for i in range(totalSize - validSize):
        ph[i + validSize] = invalidtriples[i][0]
        pt[i + validSize] = invalidtriples[i][1]
        pr[i + validSize] = invalidtriples[i][2]
    batchId += 1
    return ph, pt, pr

def getThreshold(ret):
    rel = batchId - 1
    validScores, invalidScores = consList(ret)
    thresholds[rel] = find(validScores, invalidScores)

def consList(ret):
    validScores = list()
    invalidScores = list()
    for i in range(validSize):
        validScores.append(ret[i][0])
    for i in range(validSize, totalSize):
        invalidScores.append(ret[i][0])
    # validscores sorting by desc
    validScores.sort(reverse=True)
    # invalidscores sorting by asc
    invalidScores.sort()
    return validScores, invalidScores

def showThreshold():
    for (k, v) in thresholds.items():
        print("({}, {})\n".format(k, v))

def find(lst1, lst2):
    thre1 = findBest(lst1, lst2)
    thre2 = findBest(lst2, lst1, False)
    if(thre1[1] > thre2[1]):
        return thre1
    return thre2

def findBest(lst1, lst2, flag=True):
    threshold = (0, 0)
    size1 = len(lst1)
    size2 = len(lst2)
    for i in range(size1):
        thre = lst1[i]
        correct1 = size1 - i - 1
        p = 0
        while p < size2:
            if (flag and lst2[p] >= thre) or (not flag and lst2[p] <= thre):
                p -= 1
                break                
            p+=1
        correct2 = size2 - p - 1
        if correct1 + correct2 > threshold[1]:
            threshold = (thre, correct1 + correct2)
    # print(threshold[0], threshold[1])
    return threshold
            
