N, Q = map(int, raw_input().split()) 
value = [0] * (N + 1)
maxV = [0] * (N + 1)
steps = [0] * (N + 1)

boothes = map(int, raw_input().split()) 
for i in xrange(1, N + 1):
    value[i] = boothes[i - 1]
    steps[i] = steps[i - 1] + value[i]
    if value[i] > value[maxV[i - 1]]:
        maxV[i] = i
    else:
        maxV[i] = maxV[i - 1]

queries = map(int, raw_input().split()) 
queries.sort()

def search(elt, ub, lb):
    cash = 0
    mv = maxV[min(ub, elt)]
    while mv > lb:
        if steps[mv] + (elt - mv) * value[mv] > cash:
            numRecd = mv
        cash = max(steps[mv] + (elt - mv) * value[mv], cash)
        mv = maxV[mv - 1]
    if mv == lb:
        if steps[mv] + (elt - mv) * value[mv] > cash:
            numRecd = mv
        cash = max(steps[mv] + (elt - mv) * value[mv], cash)
        mv = maxV[mv - 1]
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

total = DivConq(queries, maxV[N], 0, 0)

print(total)
