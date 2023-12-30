#%%
import numpy as np
ts ="""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
ts = open('input_p11.txt').read()
m = []
for l in ts.split('\n')[:-1]:
    m.append([x=='#' for x in l])
m = np.array(m)
# %%
m
# %%
py, px = np.where(m)
# %%
m[0,4]
# %%
yaxis=(~m).all(axis=1)*999999+1
xaxis=(~m).all(axis=0)*999999+1
#%%
yaxis = [int(y) for y in yaxis]
xaxis = [int(x) for x in xaxis]
# %%
py
# %%
py[0], px[0]
# %%
py[6], px[6]
# %%
def distance(i, j):
    x1, y1 = px[i], py[i]
    x2, y2 = px[j], py[j]
    x3, x4 = min(x1, x2), max(x1, x2)
    y3, y4 = min(y1, y2), max(y1, y2)
    return sum(xaxis[x3:x4]) + sum(yaxis[y3:y4])
# %%
from itertools import combinations
S = 0
for i, j in combinations(range(len(px)), 2):
    S+= distance(i, j)
S

# %%
yaxis.dtype
# %%
