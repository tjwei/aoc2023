#%%
ts = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
ts = open('input_p15.txt').read()
l= ts.split('\n')[0].split(',')

# %%
def HASH(s):
    cv =0
    for x in s:
        cv = (cv+ord(x))*17%256
    return cv
S = 0
for x in l:
    S+=HASH(x)
S
# %%
for x in l:
    print(len(x))
# %%
ts.split('\n')[0]
# %%
HASH('qp')
# %%
box = [{} for i in range(256)]
for x in l:
    if '-' in x:
        assert x[-1]=='-'
        label = x[:-1]
        n = HASH(label)
        if label in box[n]:
            del box[n][label]
    elif '=' in x:
        label, value = x.split('=')
        value = int(value)
        n = HASH(label)
        box[n][label] = value
#%%
S = 0
for i, b in enumerate(box):
    for j, (l, v) in enumerate(b.items()):
        n = i+1
        m = j+1
        print(v, n, m, v*n*m)
        S+=v*n*m
S
# %%
box
# %%
