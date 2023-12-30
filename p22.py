
#%%
blocks = []
ts = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
for l in open('input_p22_1.txt').read().split('\n'):
#for l in ts.split('\n'):
    if l=='':
        continue
    print(l)
    s, e = l.split('~')
    s = [int(x) for x in s.split(',')]
    e = [int(x) for x in e.split(',')]
    print(s, e)
    if s == e:
        block = [s]
    else:
        for i in range(3):
            if s[i] != e[i]:
                break
        block = []
        if i == 2:
            if s[i] > e[i]:
                s, e = e, s
            block = [s, e]
        else:
            for j in range( min(s[i], e[i]), max(s[i], e[i])+1):
                x = s.copy()
                x[i] = j
                block.append(x)
    blocks.append(block)
    


    
# %%
from collections import defaultdict
touch_map = defaultdict(set)
for block in blocks:
    for x,y,z in block:
        touch_map[(x,y)].add(z)
# %%
touch_map
# %%
def fall(block, dry=False):
    if len(block) ==  2 and block[0][2] != block[1][2]:
        x, y, z = block[0]
        if z==1:
            return False
        if z-1 in touch_map[x,y]:
            return False
    else:
        for x,y,z in block:
            if z==1 or z-1 in touch_map[x,y]:
                return False
    if not dry:            
        for cube in block:
            x, y, z = cube
            touch_map[x,y].remove(z)
            touch_map[x,y].add(z-1)
            cube[2] = z-1
            #print(f'falling {cube}')
    return True
#%%
while True:
    did_fall = False
    for b in blocks:
        r = fall(b)
        did_fall |= r
    if not did_fall:
        break
# %%
import copy
result = 0
blocks0 = copy.deepcopy(blocks)
orig_touch_map = copy.deepcopy(touch_map)
#%%
for block in blocks0:
    print('block', block)
    touch_map = copy.deepcopy(orig_touch_map)    
    for x,y,z in block:
        touch_map[(x,y)].remove(z)
    blocks = copy.deepcopy(blocks0)
    blocks = [b for b in blocks if b!=block]
    fall_i = set()
    while True:
        did_fall = False
        for i, b in enumerate(blocks):
            r = fall(b)
            if r:
                if i not in fall_i:
                    fall_i.add(i)
                    did_fall = True
        if not did_fall:
            break
    result += len(fall_i)

    print(result)
# %%
result
# %%
