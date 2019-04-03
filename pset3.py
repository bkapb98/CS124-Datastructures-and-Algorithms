N, M, K = map(int, raw_input().split())
edges = []
initLen = 0
#black edges
for i in xrange(M):
    x, y, z = map(int, raw_input().split()) 
    initLen += z
    edges.append((x - 1, y - 1, z))
#white edges
for i in xrange(K):
    x, y, z = map(int, raw_input().split())
    edges.append((x- 1, y-1, z))

anc = [-1] * N

# use recursion to iterate back thru and find intiail tree ancestor
def find(x):
    if anc[x] != x:
        anc[x] = find(anc[x])
    return anc[x]

def union(x, y):
    srcx = find(x)
    srcy = find(y)
    if srcx != srcy:
        if srcx > srcy:
            anc[srcy] = srcx
        else:
            anc[srcx] = srcy

def makeSet(x):
    anc[x] = x

def Kruskal(edge, n):
    x = []
    edge.sort(key=lambda tup: tup[2])
    for u in xrange(n):
        makeSet(u)
    for (u, v, w) in edge:
        if find(u) != find(v):
            x.append((u,v,w))
            union(u, v)
    return(x)

mst = Kruskal(edges, N)
newlen = 0
for e in mst:
    _, _, l = e
    newlen += l

diff = initLen - newlen

print diff

