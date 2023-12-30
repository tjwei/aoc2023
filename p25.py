#%%
import networkx as nx
G = nx.Graph()
for l in open('input_p25_1.txt').read().split('\n'):
    if l=='':
        continue
    assert l[3:5]==': '
    x = l[:3]
    for y in l[5:].split(' '):
        print(x, y)
        G.add_edge(x, y)

# %%
G.plot()
# %%
nx.draw(G)
# %%
nx.k_edge_components(G, k=4)
# %%
d = _
# %%
xx = list(d)
# %%
xx[0]
# %%
len(xx)
# %%
len(xx[0])*len(xx[1])
# %%
(L-s)*s

s=(L+1)/2

(L/2)**2


