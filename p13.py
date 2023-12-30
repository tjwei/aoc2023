#%%
ts="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
ts = open('input_p13.txt').read()
import numpy as np
maps = []
cm = []
for l in ts.split('\n'):
    if l=='':
        maps.append(np.array(cm))
        cm = []
    else:
        cm.append([x=='#' for x in l])

# %%
maps
# %%

m = maps[0]
# %%
m
# %%
def get_ans(m):
    for i in np.where((m[1:]==m[:-1]).all(axis=1))[0]:
        i = i+1
        p1 = m[:i]
        p2 = m[i:]
        mlen = min(p1.shape[0], p2.shape[0])
        if  (p1[::-1][:mlen] == p2[:mlen]).all():
            return i*100
    for j in np.where((m[:, 1:]==m[:, :-1]).all(axis=0))[0]:
        j = j+1
        p1 = m[:, :j]
        p2 = m[:, j:]
        mlen = min(p1.shape[1], p2.shape[1])
        if (p1[:, ::-1][:, :mlen] == p2[:, :mlen]).all():
            return j
    raise Exception("No answer")
S = 0
for m in maps:
    r = get_ans(m)
    S+=r
S
# %%
def get_ans2(m):
    print(m.astype(int))
    for i in np.where((m[1:]!=m[:-1]).sum(axis=1)<=1)[0]:
        #print(f"{i=}")
        i = i+1
        p1 = m[:i]
        p2 = m[i:]
        mlen = min(p1.shape[0], p2.shape[0])
        if  (p1[::-1][:mlen] != p2[:mlen]).sum()==1:
            return i*100
    for j in np.where((m[:, 1:]!=m[:, :-1]).sum(axis=0)<=1)[0]:
        #print(f"{j=}")
        j = j+1
        p1 = m[:, :j]
        p2 = m[:, j:]
        mlen = min(p1.shape[1], p2.shape[1])
        #print(mlen)
        if (p1[:, ::-1][:, :mlen] != p2[:, :mlen]).sum()==1:
            return j
    raise Exception("No answer")
S = 0
for m in maps:
    r = get_ans2(m)
    S+=r
S
#%%
m = maps[0]
m.shape
# %%
(m[1:]==m[:-1]).shape
#%%
(m[1:]==m[:-1]).sum(axis=1)
#%%
(m[:, 1:]!=m[:, :-1]).sum(axis=1)

# %%

p1 = m[:, :j]
p2 = m[:, j:]
mlen = min(p1.shape[1], p2.shape[1])
#%%
p1.shape
#%%
p2.shape
#%%
mlen
#%%
p1[:, ::-1][:, :mlen]
#%%
p2[:, :mlen]
# %%
(p1[:, ::-1][:, :mlen] == p2[:, :mlen]).all()
# %%
