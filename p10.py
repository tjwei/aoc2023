#%%
ts = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
ts = open('input_p10.txt').read()
m = ts.split('\n')[:-1]
# %%
len(m[0])
# %%
for i, l in enumerate(m):
    if 'S' in l:
        print(i, l.index('S'))
        y0 = i
        x0 = l.index('S')
        break
print(y0, x0)
#%%
def get_nb(y, x):
    p = m[y][x]
    match p:
        case '|':
            return [(y-1, x), (y+1, x)]
        case '-':
            return [(y, x-1), (y, x+1)]
        case 'L':
            return [(y-1, x), (y, x+1)]
        case 'F':
            return [(y+1, x), (y, x+1)]
        case '7':
            return [(y+1, x), (y, x-1)]
        case 'J':
            return [(y-1, x), (y, x-1)]
        case '.':
            return []
        case _:
            raise ValueError(p)

# %%
for y, x in [(y0-1, x0), (y0+1, x0), (y0, x0+1), (y0, x0-1)]:
    if (y0, x0) in get_nb(y, x):
        break
print(y,x)

#%%
y1, x1 = y0, x0
path = [(y0,x0)]

while (y, x)!=(y0, x0):
    path.append((y,x))
    nb = set(get_nb(y, x)) - set([(y1,x1)])
    y1, x1 = y, x
    y, x = list(nb)[0]
len(path)//2
# %%
# %%
A = 0
for i in range(len(path)):
    y1, x1 = path[i-1]
    y2, x2 = path[i]
    A += x2*y1-x1*y2

(abs(A)-len(path))//2+1
#%%
