#%%
M = []
T = {'.': 0, 'S':1, '#':-1}
for l in open('input_p21_1.txt').read().split('\n'):
    if l=='':
        continue
    M.append([T[x] for x in l]+[-1])
M.append([-1]*len(M[0]))
len(M[0])
# %%
import numpy as np
M = np.int8(M)
# %%
for i in range(64):
    cond = np.roll(M, 1, axis=0)==1
    cond |= np.roll(M, -1, axis=0)==1
    cond |= np.roll(M, 1, axis=1)==1
    cond |= np.roll(M, -1, axis=1)==1
    cond &= (M==0)

    M2 = np.zeros_like(M)
    M2[M==-1] = -1
    M2[cond] = 1
    M=M2

(M==1).sum()
# %%
(M2==1).sum()
# %%
M.shape
# %%

M = []
T = {'.': 0, 'S':1, '#':-1}
for l in open('input_p21_1.txt').read().split('\n'):
    if l=='':
        continue
    M.append([T[x] for x in l])
import numpy as np
M = np.int8(M)
M.shape
M0 = M.copy()
M2 = M.copy()
M2[M2==1] = 0
M3 = np.concatenate([M2]*23, axis=1)
M3 = np.concatenate([M3]*23, axis=0)
M3.shape
S = M.shape[0]
M3[S*11:S*12, S*11:S*12] = M0
M = M3
D = np.full(M.shape, -1, dtype=np.int64)
D[M==1] = 0
# %%
for i in range(1000):
    cond = np.roll(M, 1, axis=0)==1
    cond |= np.roll(M, -1, axis=0)==1
    cond |= np.roll(M, 1, axis=1)==1
    cond |= np.roll(M, -1, axis=1)==1
    cond &= (M==0)

    M2 = np.zeros_like(M)
    M2[M==-1] = -1
    M2[cond] = 1
    M=M2
    D[(M==1) & (D==-1)] = i+1
#%%
#%%
x = list(range(S*11, S*23, S))
y = list(range(S*11, S*23, S))
x[-1]= S*10
y[-1]= S*10
for i in range(10):
    for j in range(10):
        x1, x2, x3 = x[i-1], x[i], x[i+1]
        y1, y2, y3 = y[j-1], y[j], y[j+1]
        left = down = False
        cond = D[y2:y3, x2:x3] != -1
        # left
        diff = D[y2:y3,x2:x3] - D[y2:y3, x1:x2]        
        if cond.any() and (diff[cond] == 131).all():
            left = True
            #print('left', i, j)
        diff = D[y2:y3,x2:x3] - D[y1:y2, x2:x3]        
        if cond.any() and (diff[cond] == 131).all():
            #print('down', i, j)
            down = True
        if left and down:
            print(i, j)
            diff = D[y2:y3,x2:x3] - D[y1:y2, x1:x2]        
            if cond.any() and (diff[cond] == 262).all():
                print('ok')
            else:
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                #print('down', i, j)
                
#%%
x = list(range(0, S*23, S))
y = list(range(0, S*23, S))
#%%
rect1 = D[y[11]:y[12], x[11]:x[12]]
total = ((rect1 >=0) & (rect1%2==1)) .sum()
total
#%%
STEP = 26501365
#odd
for rect2 in [
    D[y[11]:y[12], x[12]:x[13]],
    D[y[11]:y[12], x[10]:x[11]],
    D[y[12]:y[13], x[11]:x[12]],
    D[y[10]:y[11], x[11]:x[12]],
]:
    # odd
    cond = ((rect2 >=0) & (rect2%2==1))
    T = np.floor((STEP-rect2)/(131*2))+1
    total+=T[cond].sum()
    #even
    cond = ((rect2 >=0) & (rect2%2==0))
    T = np.floor((STEP-rect2-131)/(131*2))+1
    total+=T[cond].sum()
#%%
for rect3 in  [D[y[12]:y[13], x[12]:x[13]],
                D[y[12]:y[13], x[10]:x[11]],
                D[y[10]:y[11], x[12]:x[13]],
                D[y[10]:y[11], x[10]:x[11]],
]:
    # odd
    cond = ((rect3 >=0) & (rect3%2==1))
    T = np.floor((STEP-rect3)/262)+1 # max sum 0->1, 2->4, 4->9
    T = T**2
    total+=T[cond].sum()
    # even
    cond = ((rect3 >=0) & (rect3%2==0))
    T = np.floor((STEP-rect3-131)/262)+1 # max sum, 2+4+6+8
    T = T*(T+1)
    total+=T[cond].sum()
#%%
int(total)
#%%
rect2
#%%

#%%
#%%
# 602259574630890 too high
# 502259574630890 too low
#%%
602259568764248
602259568764234>  602259574630890 
#%%
k = 1
y1, x1 = S*(6+k), S*6
y2, y3 = y1 + S, y1 + S*2
x2, x3 = x1 + S, x1 + S*2
cond = D[y1:y2, x2:x3] != -1
diff = D[y1:y2,x2:x3] - D[y1:y2, x1:x2]
(diff[cond] == 131).all()
#%%
diff
#%%
from PIL import Image
def plot(M):
    img = np.zeros(M.shape+(3,), dtype=np.uint8)
    img[M==1, 0] = 255
    img[M==-1, 1] = 255
    print(img.sum())
    return Image.fromarray(img)
plot(M)

# %%
M.shape
# %%
