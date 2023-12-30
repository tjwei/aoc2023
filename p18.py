#%%
import numpy as np
from IPython.display import display
from PIL import Image
plan = np.zeros((400,500,3), dtype=np.uint8)
y,x = 250,50
ss = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""
A = 1
for l in open('input_p18_1.txt').read().split('\n'):
#for l in ss.split('\n'):
    if l=='':
        continue
    a, b, c = l.split(' ')
    c = c[2:-1]    
    c0 = c
    c = (int(c[:2], 16), int(c[2:4], 16), int(c[4:], 16))
    assert c!=(0,0,0)
    c = (255,255,255)
    b = int(b)
    b = int(c0[:5], 16)
    a = "RDLU"[int(c0[5])]
    print(a, b, c)
    assert a in "UDRL"
    if a == 'U':
        #plan[y-b:y+1,x] = c        
        y -= b
        A -= b*x
        A+=(b)/2        
    elif a == 'D':
        #plan[y:y+b+1,x] = c
        y += b
        A += b*x
        A+=(b)/2
    elif a == 'L':
        #plan[y,x-b:x+1] = c
        x -= b
        A+=(b)/2
    elif a == 'R':
        #plan[y,x:x+b+1] = c
        x += b    
        A+=(b)/2
print(A)


#plane = (plan!=0).any(axis=2).astype(np.uint8)*255
#Image.fromarray(plane)
#%%
A = 1
for l in open('input_p18_1.txt').read().split('\n'):
#for l in ss.split('\n'):
    if l=='':
        continue
    a, b, c = l.split(' ')
    c0 = c[2:-1]    
    b = int(c0[:5], 16)
    a = "RDLU"[int(c0[5])]
    assert a in "UDRL"
    if a == 'U':
        #plan[y-b:y+1,x] = c        
        y -= b
        A -= b*x
        A+= b/2        
    elif a == 'D':
        #plan[y:y+b+1,x] = c
        y += b
        A += b*x
        A+=(b)/2
    elif a == 'L':
        #plan[y,x-b:x+1] = c
        x -= b
        A+=(b)/2
    elif a == 'R':
        #plan[y,x:x+b+1] = c
        x += b    
        A+=(b)/2
print(A)


#%%
plane[1,1] = 127
for i in range(100):
    cond = np.roll(plane, 1, axis=0)==127
    cond |= np.roll(plane, -1, axis=0)==127
    cond |= np.roll(plane, 1, axis=1)==127
    cond |= np.roll(plane, -1, axis=1)==127
    cond &= plane==0
    plane[cond] = 127
    if not cond.any():
        break
Image.fromarray(plane)
#%%
cond[:3, :3]

# %%
Image.fromarray(plan)
#%%
(plane!=127).sum()
# %%
t = 0
for y in range(400):
    p = 0
    s = 0
    for x in range(500):
        c = tuple(plan[y,x])        
        if p ==0 and c!=(0,0,0):            
            p = 1
        elif p == 1 and c==(0,0,0):
            p = 2
        elif p == 2 and c!=(0,0,0):
            p = 3
            t += s
            #print('add s', s, t)
            plan[y,x-s:x] = (255,0,0)
            s = 0
        elif p == 3 and c==(0,0,0):
            p = 0
        if p in [1, 3]:
            t += 1
            #print(y, x, c, p, t)
        if p == 2:
            s +=1    
#%%
Image.fromarray(plan)        
#%%
t
# %%
import cv2 as cv

p = (plan>0).any(axis=2).astype(np.uint8)
cv.connectedComponents_with_stats(p)
# %%
