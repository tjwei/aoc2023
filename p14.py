#%%
import numpy as np
ts="""O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
ts = open('input_p14.txt').read()
m = []
c2i = {'.':0, 'O':1, '#':2}
for l in ts.split('\n')[:-1]:
    m.append([c2i[x]  for x in l])
m = np.array(m)
m
# %%
def count_support(m):
    w = np.full(m.shape[1], m.shape[0])
    S=0
    for i, l in enumerate(m):
        #print(l, w*(l==1))
        S+=w[l==1].sum()
        w[l==1]-=1
        w[l==2]= m.shape[0]-i-1
    return S
def support(m):
    w = np.full(m.shape[1], m.shape[0])
    S=0
    for i, l in enumerate(m):
        S+=w[l==1].sum()
        w -=1
    return S
# %%
import numba
def m2s(m):
    return "\n".join("".join(".O#"[x] for x in l) for l in m)
def show(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(".O#"[m[i, j]], end='')
        print()
    print()

@numba.njit
def north(m):
    for j in range(m.shape[1]):
        rocks = 0
        for i in range(m.shape[0]-1, -1, -1):
            t = m[i, j]
            if t==1:
                m[i, j] = 0
                rocks+=1
            elif t==2:
                m[i+1:i+1+rocks, j] = 1
                rocks = 0
        m[:rocks, j] = 1
    return m
                
show(m)
count_support(north(m.copy()))
# %%

m1 = m.copy()
record = {}
history = []
for n in range(1000):
    for i in range(4):
        m1 = north(m1)
        m1 = np.rot90(m1, -1)
    s = m2s(m1)
    if s in record:
        print('found duplicate', n, record[s])
        period_start = record[s]
        assert (history[period_start]==m1).all()
        period = n-period_start
        idx = (1000000000-1-period_start)%period+period_start
        ans_m = history[idx]
        print(support(ans_m))
        break
    record[s] = n
    history.append(m1.copy())


# %%
show(history[5])
# %%
count_support(m)
# %%
idx

# %%
mm = history[idx].copy()
mm = north(mm)
show(mm)
# %%
for mm in history:
    print(count_support(mm))
# %%
count_support(m)
# %%
