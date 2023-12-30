#%%
ts = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
ts = open('input_p8.txt').read()
lines = list(ts.split('\n'))
instruction = lines[0]
map = {}
for l in lines[2:]:
    if l=='':
        continue
    k, v = l.split(' = ')
    v = v[1:-1].split(', ')
    print(k, v)
    map[k] = v

n = 'AAA'
i = 0
while n!='ZZZ':
    d = instruction[i%len(instruction)]
    d = d == 'R'
    n = map[n][d]
    i+=1
print(i)
# %%
lines
# %%
len(lines)
# %%
starts = [x for x in map if x[2]=='A']
# %%
all_z = []
for n in starts:
    print(n)
    visited = {}
    history = []
    i = 0
    while True:
        j = i%len(instruction)
        state = n, j
        if state in visited:
            break
        visited[state] = i
        history.append(state)
        d = instruction[j]
        d = d == 'R'
        n = map[n][d]
        i+=1
    period = i-visited[state]
    period_start = visited[state]
    print(state, i, visited[state])
    for i, (n, j) in enumerate(history):
        if n[2]=='Z':
            print(n, i)
            break
    print(i, period)
    assert i==period
    all_z.append(i)
    print()
#%%
from math import lcm
lcm(*all_z)
# %%
