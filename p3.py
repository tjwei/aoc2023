#%%
import numpy as np
ts = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
ts = open('input_p3.txt').read()
symbols = set(ts)-set(".0123456789\n")
for s in symbols:
    ts = ts.replace(s, '#')
#%%
arr = []
for l in ts.split('\n')[:-1]:
    arr.append('.'+l +'.')
arr.append('.'*len(arr[0]))
#%%
results = []
for i, l in enumerate(arr):
    pos = 0
    for s in l.split('.'):
        if '#' in s:
            for n in s.split('#'):
                if n.isnumeric():
                    results.append(int(n))
            
        elif s.isnumeric():            
            if '#' in arr[i-1][pos-1:pos+len(s)+1]:
                results.append(int(s))
            elif '#' in arr[i+1][pos-1:pos+len(s)+1]:
                results.append(int(s))            
        pos+=len(s)+1
sum(results)
#%%

ts = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
ts = open('input_p3.txt').read()
symbols = set(ts)-set(".0123456789\n")
arr = []
for l in ts.split('\n')[:-1]:
    arr.append('.'+l +'.')
arr.append('.'*len(arr[0]))

def get_num_prefix(s, reverse=False):
    num = ''
    for c in s:
        if not c.isnumeric():
            break
        num = num+c
    if reverse:
        return num[::-1]
    else:
        return num
S = 0
for i in range(len(arr)-1):
    for j in range(len(arr[0])-1):
        if arr[i][j]!='*':
            continue
        all_nums = []
        # search left numbers        
        l_num = get_num_prefix(arr[i][j-1::-1], reverse=True)
        if l_num:
            all_nums.append(int(l_num))
        # search right numbers
        r_num = get_num_prefix(arr[i][j+1:])
        if r_num:
            all_nums.append(int(r_num))
        # search upper left and upper right numbers
        ul_num = get_num_prefix(arr[i-1][j-1::-1], reverse=True)
        ur_num = get_num_prefix(arr[i-1][j+1:])
        if arr[i-1][j].isnumeric():
            all_nums.append(int(ul_num + arr[i-1][j] + ur_num))
        else:
            if ul_num:
                all_nums.append(int(ul_num))
            if ur_num:
                all_nums.append(int(ur_num))
        # search lower left and lower right numbers
        ll_num = get_num_prefix(arr[i+1][j-1::-1], reverse=True)
        lr_num = get_num_prefix(arr[i+1][j+1:])
        if arr[i+1][j].isnumeric():
            all_nums.append(int(ll_num + arr[i+1][j] + lr_num))
        else:
            if ll_num:
                all_nums.append(int(ll_num))
            if lr_num:
                all_nums.append(int(lr_num))
        if all_nums:
            print(all_nums)
            if len(all_nums)==2:
                S+=all_nums[0]*all_nums[1]
S
#%%
type(ll_num)

get_num_prefix(arr[i+1][j-1::-1], reverse=True)
#%%
arr = []
def c2i(c:str):
    if c=='.':
        return 0
    elif c.isnumeric():
        return int(c)
    else:
        return -1
for l in ts.split('\n')[:-1]:
    arr.append([c2i(x) for x in l]+[0])
arr.append([0]*len(arr[0]))
arr = np.array(arr)
arr
# %%
cond = np.full(arr.shape, False)
for i in [-1, 0, 1]:
    for j in [-1, 0, 1]:
        if i==0 and j==0:
            continue
        cond |= np.roll(arr, (i, j), axis=(0, 1))==-1
cond.astype(int)
# %%
arr[cond].sum()
# %%
symbols
# %%
