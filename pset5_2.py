N, Q = map(int, raw_input().split()) 
value = [0] * (N + 2)
maxVlocF = [0] * (N + 1)
maxVV = [0] * (N + 1)
steps = [0] * (N + 1)

boothes = map(int, raw_input().split()) 
boothes.append(0)
for i in xrange(1, N + 1):
    value[i] = boothes[i - 1]
    steps[i] = steps[i - 1] + value[i]
    if value[i] + value[i - 1] > maxVV[maxVlocF[i - 1]]:
        maxVV[i] = value[i] + value[i - 1]
        maxVlocF[i] = i
    else:
        maxVlocF[i] = maxVlocF[i - 1]
        maxVV[i] = maxVV[i - 1]

queries = map(int, raw_input().split()) 
queries.sort()

e = []
o = []
for a in queries:
    if a % 2 == 0:
        e.append(a)
    else:
        o.append(a)

numRecd = 0 

def search(elt, ub, lb):
    cash = 0
    mv = maxVlocF[min(elt, ub)]
    while mv > lb:
        sub = 0
        if (elt - mv) % 2 == 1:
            sub = value[maxVlocF[mv] - 1]
        if steps[mv] + ((elt - mv) / 2) * maxVV[mv] + sub > cash:
            numRecd = mv
        cash = max(steps[mv] + ((elt - mv) / 2) * maxVV[mv] + sub, cash)
        mv = maxVlocF[mv - 1]
    if mv == lb:
        sub = 0
        if (elt - mv) % 2 == 1:
            sub = value[maxVlocF[mv] - 1]
        if steps[mv] + ((elt - mv) / 2) * maxVV[mv] + sub > cash:
            numRecd = mv
        cash = max(steps[mv] + ((elt - mv) / 2) * maxVV[mv] + sub, cash)
        mv = maxVlocF[mv - 1]
    return numRecd, cash

def DivConq (array, ub, lb, total):
    newtotal = 0
    if len(array) == 1:
        _, newtotal = search(array[0], ub, lb)
    elif len(array) == 2:
        _, total1 = search(array[0], ub, lb)
        _, total2 = search(array[1], ub, lb)
        newtotal = total1 + total2
    else:
        index = len(array)/2
        numRecd, total = search(array[index], ub, lb)
        total1 = DivConq(array[:index], numRecd, lb, 0)
        total2 = DivConq(array[index + 1:], ub, numRecd, 0)
        newtotal = total + total1 + total2
    return newtotal

total1 = DivConq(e, maxVlocF[N], 0, 0)
total2 = DivConq(o, maxVlocF[N], 0, 0)
total = total1 + total2

print(total)
