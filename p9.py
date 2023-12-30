#%%
ts = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
ts = open('input_p9.txt').read()
import numpy as np
all_seq = []
for l in ts.split('\n'):
    if l=='':
        continue
    l = l.split(' ')
    l = [int(x) for x in l]
    l = np.array(l)
    all_seq.append(l)
    print(l)
# %%

def next_value(s):
    #print(s)
    if len(set(s))==1:
        return s[-1]
    d = next_value(s[1:]-s[:-1])
    return s[-1]+d
r = []
for s in all_seq:
    r.append(next_value(s))
print(sum(r))
r = []
for s in all_seq:
    r.append(next_value(s[::-1]))
print(sum(r))
# %%
l
# %%
