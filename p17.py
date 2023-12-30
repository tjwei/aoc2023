#%%
ts = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""
ts2 = """111111111111
999999999991
999999999991
999999999991
999999999991
"""
ts = ts2
ts = open('input_p17.txt').read()
nodes = []
for l in ts.split('\n')[:-1]:
    nodes.append([int(x) for x in l])
import numpy as np
nodes = np.array(nodes)
nodes
# %%
nodes.shape
# %%
import networkx as nx
G = nx.DiGraph()
w = nodes[1,0]
G.add_edge((0,0), (1, 0, 1, 0), weight=w)
w = nodes[0,1]
G.add_edge((0,0), (0, 1, 0, 1), weight=w)
for i in range(nodes.shape[0]):
    for j in range(nodes.shape[1]):
        if i+1 < nodes.shape[0]:
            w = nodes[i+1,j]
            if i+1==nodes.shape[0]-1 and j==nodes.shape[1]-1:
                G.add_edge((i,j, 1, 0), (i+1, j), weight=w)
                G.add_edge((i,j, 2, 0), (i+1, j), weight=w)
                for s in [-3, -2,-1, 1, 2, 3]:
                    G.add_edge((i,j, 0, s), (i+1, j), weight=w)
            else:            
                G.add_edge((i,j, 1, 0), (i+1, j, 2, 0), weight=w)
                G.add_edge((i,j, 2, 0), (i+1, j, 3, 0), weight=w)
                for s in [-3, -2,-1, 1, 2, 3]:
                    G.add_edge((i,j, 0, s), (i+1, j, 1, 0), weight=w)
        if i>0:
            w = nodes[i-1,j]
            G.add_edge((i,j, -1, 0), (i-1, j, -2, 0), weight=w)
            G.add_edge((i,j, -2, 0), (i-1, j, -3, 0), weight=w)
            for s in [-3, -2,-1, 1, 2, 3]:
                G.add_edge((i,j, 0, s), (i-1, j, -1, 0), weight=w)
        if j+1 < nodes.shape[1]:
            w = nodes[i,j+1]
            if j+1==nodes.shape[1]-1 and i==nodes.shape[0]-1:
                G.add_edge((i,j, 0, 1), (i, j+1), weight=w)
                G.add_edge((i,j, 0, 2), (i, j+1), weight=w)
                for s in [-3, -2,-1, 1, 2, 3]:
                    G.add_edge((i,j, s, 0), (i, j+1), weight=w)
            else:
                G.add_edge((i,j, 0, 1), (i, j+1, 0, 2), weight=w)
                G.add_edge((i,j, 0, 2), (i, j+1, 0, 3), weight=w)
                for s in [-3, -2,-1, 1, 2, 3]:
                    G.add_edge((i,j, s, 0), (i, j+1, 0, 1), weight=w)
        if j>0:
            w = nodes[i,j-1]
            G.add_edge((i,j, 0, -1), (i, j-1, 0, -2), weight=w)
            G.add_edge((i,j, 0, -2), (i, j-1, 0, -3), weight=w)
            for s in [-3, -2,-1, 1, 2, 3]:
                G.add_edge((i,j, s, 0), (i, j-1, 0, -1), weight=w)
# %%
nx.shortest_path_length(G, (0,0), (nodes.shape[0]-1,nodes.shape[1]-1), weight='weight')
# %%
# %%

import networkx as nx
G = nx.DiGraph()
for l in range(4, 11):
    w = nodes[1:l+1,0].sum()
    G.add_edge((0,0), (l, 0, 1, 0), weight=w)
    w = nodes[0,1:l+1].sum()
    G.add_edge((0,0), (0, l, 0, 1), weight=w)
sink = (nodes.shape[0]-1, nodes.shape[1]-1)

for i in range(nodes.shape[0]):
    for j in range(nodes.shape[1]):
        for l in range(4, 11):
            if i+l < nodes.shape[0]:
                tgt = (i+l, j, 1, 0) if (i+l, j) != sink else (i+l, j)
                G.add_edge((i,j, 0, 1), tgt, weight=nodes[i+1:i+l+1,j].sum())
            if j+l < nodes.shape[1]:
                tgt = (i, j+l, 0, 1) if (i, j+l) != sink else (i, j+l)
                G.add_edge((i,j, 1, 0), tgt, weight=nodes[i,j+1:j+l+1].sum())
            if i-l >= 0:
                tgt = (i-l, j, 1, 0)
                G.add_edge((i,j, 0, 1), tgt, weight=nodes[i-l:i,j].sum())
            if j-l >= 0:
                tgt = (i, j-l, 0, 1)
                G.add_edge((i,j, 1, 0), tgt, weight=nodes[i,j-l:j].sum())

nx.shortest_path_length(G, (0,0), (nodes.shape[0]-1,nodes.shape[1]-1), weight='weight')
# %%
