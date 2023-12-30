#%%
ts = """.|...\....
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

m = ts.split('\n')[:-1]
# %%
I = len(m)
J = len(m[0])
stats = [[set() for j in range(J)]for i in range(I)]
U, D, L, R = 0, 1, 2, 3

def rec(i,j, DIR):
    print(i,j, "UDLR"[DIR])
    if DIR in stats[i][j]:
        return
    stats[i][j].add(DIR)
    i, j = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)][DIR]
    if i<0 or j<0 or i>=I or j>=J:
        return
    t = m[i][j]
    if t=='.':
        rec(i,j,DIR)
    elif t=='|':
        if DIR in [U, D]:
            rec(i,j,DIR)
        rec(i,j, L)
        rec(i,j, R)
    elif t=='-':
        if DIR in [L, R]:
            rec(i,j,DIR)
        rec(i,j, U)
        rec(i,j, D)
    elif t=='/':
        DIR2 = [R, L, D, U][DIR]
        rec(i,j,DIR2)
    elif t=='\\':
        DIR2 = [L, R, U, D][DIR]
        rec(i,j,DIR2)
rec(0,0,R)
    




# %%
