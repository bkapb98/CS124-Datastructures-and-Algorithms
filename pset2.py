import sys
from collections import deque

def bfs(edges, lst):
    anc = [0] * len(edges)
    dist = [sys.maxint] * len(edges)
    visited = [False] * len(edges)
    lst.sort()
    queue = deque(lst)
    for i in lst:
        dist[i] = 0
        anc[i] = i
        visited[i] = True
    while queue:
        v = queue.popleft()
        for u in edges[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                dist[u] = dist[v] + 1
                anc[u] = anc[v]
    return dist, anc

N, M, K = map(int, raw_input().split()) 
edges = [[] for i in range(N + 1)] 
for i in xrange(M):
    x, y = map(int, raw_input().split()) 
    edges[x].append(y)
    edges[y].append(x)

vacant = map(int, raw_input().split()) 

dist, anc = bfs(edges, vacant)
c = sys.maxsize
pair = (0, 0)
for i in xrange(1, len(edges)):
    for j in edges[i]:
        if anc[j] != anc[i]:
            if c > dist[i] + dist[j] + 1:
                c = dist[i] + dist[j] + 1
                pair = (min (anc[j], anc[i]), max (anc[j], anc[i]))
            if c == dist[i] + dist[j] + 1:
                if pair > (min (anc[j], anc[i]), max (anc[j], anc[i])):
                    pair = (min (anc[j], anc[i]), max (anc[j], anc[i]))

print pair[0], pair[1]


  
