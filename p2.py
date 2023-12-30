#%%
from collections import defaultdict
ts = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
ts = open('input_p2.txt').read()
constraint = defaultdict(int)
constraint.update({'red': 12, 'green': 13, 'blue': 14})
assert ts.split('\n')[-1]==''
S=0
T = 0
for l in ts.split('\n')[:-1]:
    g, d = l.split(': ')
    assert g[:5]=='Game '
    g = int(g[5:])
    d = d.replace(';', ',').split(', ')
    good = True
    result = defaultdict(int)
    for s in d:
        #print(s)
        n, k = s.split(' ')
        result[k] = max(int(n), result[k])
    good = all(v<= constraint[k] for k, v in result.items())
    power = 1
    for k in ['red', 'green', 'blue']:
        power *= result[k]
    T+=power
    print(good, g, result, power)
    if good:
        S+=g
S, T
# %%