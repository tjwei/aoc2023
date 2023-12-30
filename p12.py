#%%
import numpy as np
ts = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
ts = open('input_p12.txt').read()
pr = []
for l in ts.split('\n')[:-1]:
    s, cfg = l.split(' ')
    cfg = tuple(int(x) for x in cfg.split(','))
    print(s, cfg)
    pr.append((s, cfg))
# %%
def get_cfg(s):
    assert '?' not in s
    return tuple(len(x) for x in s.split('.') if x)
get_cfg('.#.###.#.######')
# %%
#%% 
from itertools import combinations
def get_combs(s, cfg):
    n_unk = sum(x=='?' for x in s)
    n_ng = sum(x=='#' for x in s)
    lack = sum(cfg)-n_ng
    unk_pos = [i for i, x in enumerate(s) if x=='?'] 
    s0 = list(s.replace('?', '.'))
    rtn = 0
    for c in combinations(unk_pos, lack):
        s2 = s0.copy()
        for i in c:
            s2[i] = '#'
        s2 = "".join(s2)
        cfg2 = get_cfg(s2)
        if cfg2 == cfg:
            #print(s2)
            rtn+=1
    return rtn
S = 0
for s, cfg in pr:
    S += get_combs(s, cfg)
S
#%%
s, cfg = pr[1]
get_combs(s, cfg)
# %%

def rec(s0, cfg, unk_pos=None, i=0):
    cache_key = None
    if unk_pos is None:
        unk_pos = [j for j, x in enumerate(s0) if x=='?']
        s0 = list(s0.replace('?', '.'))
        #print("".join(s0), cfg, unk_pos)
    elif i == len(unk_pos):
        rtn = get_cfg("".join(s0)) == cfg
        #print("return", rtn, "".join(s0), i, len(unk_pos))
        return rtn
    else:
        sl = unk_pos[i]
        sr = "".join(s0[:sl])
        #print(sr,  i)
        scfg = get_cfg(sr)
        if len(scfg):
            if len(scfg)<=len(cfg) and \
                scfg[:-1]==cfg[:len(scfg)-1] and \
                    scfg[-1]<=cfg[len(scfg)-1]:
                cache_key = scfg, i, sr[-1]
                if cache_key in cache:
                    return cache[cache_key]
            else:
                #print(cfg, scfg)
                #print('impossible', sr)
                return 0
    rtn = 0
    rtn += rec(s0, cfg, unk_pos, i+1)
    if sum(1 for x in s0 if x=='#') < sum(cfg):
        s1 = s0.copy()
        s1[unk_pos[i]] = '#'
        rtn += rec(s1, cfg, unk_pos, i+1)
    if cache_key is not None:
        cache[cache_key] = rtn
    return rtn
#for s, cfg in pr:
#    print(s, cfg)

#    print(rec(s, cfg))
#%%
s, cfg = pr[1]
s, cfg
#%%
#%%
S =0
for i, (s, cfg) in enumerate(pr):
    cache = {}
    rtn = rec("?".join([s]*5), cfg+cfg+cfg+cfg+cfg)
    print(i, rtn)
    S+=rtn
S
#%%
len(pr)
# %%
"?".join([s]*5) == '???.###????.###????.###????.###????.###'
#%%

cfg+cfg+cfg+cfg+cfg == (1,1,3,1,1,3,1,1,3,1,1,3,1,1,3)
# %%
get_cfg('#.#')
# %%
