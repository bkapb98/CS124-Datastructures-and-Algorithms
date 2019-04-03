def find(x):
    if anc[x] == 0:
        return 0
    if anc[x] != x:
        anc[x] = find(anc[x])
    return anc[x]

def union(x, y):
    srcx = find(x)
    srcy = find(y)
    if srcx != srcy and srcx != 0 and srcy != 0:
        if rank[srcx] > rank[srcy]:
            holder = srcx
            srcx = srcy
            srcy = holder
        anc[srcx] = srcy
        if rank[srcx] == rank[srcy]:
            rank[srcy] += 1

def makeSet(x):
    anc[x] = x

def addEdge(x, y):
    union(x, enemies[y])
    union(y, enemies[x])
    enemies[x] = y
    enemies[y] = x

N, M, Q = map(int, raw_input().split()) 
enemies = [0] * (N + 1)
anc = [0] * (N + 1)
rank = [0] * (N + 1)

for u in xrange(N + 1):
    makeSet(u)
for i in xrange(M):
    x, y = map(int, raw_input().split()) 
    addEdge(x, y)
count = 0
for j in xrange(Q):
    t, x, y = map(int, raw_input().split()) 
    if t == 1:
        addEdge(x, y)
    elif t == 2:
        if find(enemies[x]) == find(y):
            count += 1

print count
