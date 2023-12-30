#%%
ts = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""
ts = open('input_16.txt').read()
m = ts.split('\n')[:-1]
# %%
from collections import deque
I = len(m)
J = len(m[0])
U, D, L, R = 0, 1, 2, 3
starts = [(i, -1, R) for i in range(I)]+[(i, J, L) for i in range(I)]+\
    [(-1, j, D) for j in range(J)]+[(I, j, U) for j in range(J)]
maxS = 0
for st in starts:
    stats = [[set() for j in range(J)]for i in range(I)]
    #q = deque([(0,-1,R)])
    q = deque([st])
    while q:
        i, j, DIR = q.popleft()
        #print(i,j, "UDLR"[DIR])
        if i>=0 and j>=0 and i<I and j<J:
            if DIR in stats[i][j]:
                continue
            stats[i][j].add(DIR)
        i, j = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)][DIR]
        if i<0 or j<0 or i>=I or j>=J:                
            continue
        t = m[i][j]
        if t=='.':
            q.append((i,j,DIR))
        elif t=='|':
            if DIR in [U, D]:
                q.append((i,j,DIR))
            else:
                q.append((i,j,U))
                q.append((i,j,D))
        elif t=='-':
            if DIR in [L, R]:
                q.append((i,j,DIR))
            else:
                q.append((i,j,L))
                q.append((i,j,R))
        elif t=='/':
            DIR2 = [R, L, D, U][DIR]
            q.append((i,j,DIR2))
        elif t=='\\':
            DIR2 = [L, R, U, D][DIR]
            q.append((i,j,DIR2))
        else:
            print(t)
        
    S = 0
    for i in range(I):
        for j in range(J):
            if stats[i][j]:
                S+=1
    if S>maxS:
        maxS = S
        print(maxS, st)

maxS
# %%
for i in range(I):
    s = ''.join('#' if stats[i][j] else'.' for j in range(J))
    print(s)
        
# %%
bool(set([0]))
# %%
