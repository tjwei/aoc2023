#%%
ts = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
M = []
for l in open('input_p23_1.txt').read().split('\n'):
#for l in ts.split('\n'):
    if l=='':
        continue
    M.append([x for x in l])
#%%
import numpy as np
M = np.array(M)
M
# %%
M[0]
# %%
from collections import deque
q = deque([(0,1)])
graph = {(0,1): []}
while q:
    i, j = q.popleft()
    parent = graph[(i, j)]
    if M[i, j] == '.':        
        nextp = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    elif M[i, j] == '>':
        nextp = [(i, j+1)]
    elif M[i, j] == '<':
        nextp = [(i, j-1)]
    elif M[i, j] == '^':
        nextp = [(i-1, j)]
    elif M[i, j] == 'v':
        nextp = [(i+1, j)]

    for i2, j2 in nextp:
        if i2<0 or j2<0:
            continue
        if i2>=M.shape[0] or j2>=M.shape[1]:
            continue
        if M[i2, j2]=="#":
            continue
        if (i2, j2) in parent:
            continue
        if M[i2, j2] == '>' and j2 == j-1:
            continue
        if M[i2, j2] == '<' and j2 == j+1:
            continue
        if M[i2, j2] == '^' and i2 == i+1:
            continue
        if M[i2, j2] == 'v' and i2 == i-1:
            continue
        if M[i,j]=='.' and (i2, j2) in graph:
            raise Exception('already visited')
        if (i2, j2) in graph:
            graph[(i2, j2)].append((i, j))
            continue
        graph[(i2, j2)] = [(i, j)]
        q.append((i2, j2))

#%%
import networkx as nx
G = nx.DiGraph()
for i, j in graph:
    for i2, j2 in  graph[(i,j)]:
        G.add_edge( (i2, j2), (i,j))
#%%
nx.dag_longest_path_length(G)
# %%
len(graph)
# %%
for i, j in np.indices(M.shape).reshape(2, -1).T:
    if M[i,j]!='#':
        assert (i,j) in graph

# %%
M[graph[i2, j2]]

#%%
i, j, i2, j2, graph[i2, j2]
#%%
i2, j2
# %%
M.shape
# %%
graph
# %%
M[i-1:i+2,j-1:j+2]
# %%
M[graph[i2,j2]]
# %%
i2,j2
# %%

#%%
ts = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
M = []
for l in open('input_p23_1.txt').read().split('\n'):
#for l in ts.split('\n'):
    if l=='':
        continue
    M.append([x!='#' for x in l])
#%%
import numpy as np
M = np.array(M)
M
# %%
from collections import defaultdict
L = M.shape[0]
edges = defaultdict(set)
for i in range(L):
    for j in range(L):
        if not M[i,j]:
            continue
        if i>0 and M[i-1,j]:
            edges[(i,j)].add((i-1,j))
        if j>0 and M[i,j-1]:
            edges[(i,j)].add((i,j-1))
        if i<L-1 and M[i+1,j]:
            edges[(i,j)].add((i+1,j))
        if j<L-1 and M[i,j+1]:
            edges[(i,j)].add((i,j+1))
# %%
super_edges = {}
for k, v in edges.items():
    if len(v) == 2:
        continue
    for n in v:
        p = k
        i = 1
        while len(edges[n]) == 2:
            m = list(edges[n] - set([p]))[0]
            p, n = n, m
            i+=1
        super_edges[k, n] = i
super_edges
#%%
import networkx as nx
G = nx.Graph()
for s,t in super_edges:
    G.add_edge( s, t)
#%%
nx.draw(G)
#%%
G.nodes
# %%
maxlen = 0
for p in nx.all_simple_edge_paths(G, (0,1), (140,139)):    
    lenp = sum([super_edges[x] for x in p])
    if lenp > maxlen:
        maxlen = lenp
        print(maxlen)
#%%
#%%
M[140][139]
# %%
M.shape
# %%
p[0]
# %%
nx.node_connectivity(G)
# %%
len([x for x in dict(nx.degree(G)).values() if x!=2])
# %%
