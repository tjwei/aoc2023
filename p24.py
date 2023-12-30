#%%
ts="""19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
ts = open('input_p24.txt').read()
coeffs = []
for l in ts.split('\n'):
    if l=='':
        continue
    pos, v = l.split(' @ ')
    pos = [int(x) for x in pos.split(', ')]
    v = [int(x) for x in v.split(', ')]
    a, b, c = v[1], -v[0], v[0]*pos[1]-v[1]*pos[0]
    assert a!=0 and b!=0
    coeffs.append((a,b,c, pos[1]))
    print(pos, v)
# %%
from itertools import combinations
result = 0
for (a1,b1,c1, y1), (a2,b2,c2, y2) in combinations(coeffs, 2):
    print(a1,b1,c1, a2,b2,c2)
    print(y1, y2)
    if a1*b2-a2*b1==0:
        print('parallel')
        print()
        continue
    x = (b1*c2-b2*c1)/(a1*b2-a2*b1)
    y = (a2*c1-a1*c2)/(a1*b2-a2*b1)
    
    if ((a1>0) != (y>=y1)) and ((a2>0) != (y>=y2)):
        print('in the past of both')
    elif (a1>0) != (y>=y1):
        print('in the past of 1')        
    elif (a2>0) != (y>=y2):
        print('in the past of 2')        
    else:
        if (200000000000000 <=x <= 400000000000000) and (200000000000000<=y<=400000000000000):
            print('inside')
            result+=1
        else:
            print('outside')
        print(x,y)    
    print()
# %%
result

# %%
import numpy as np
def f(px, py, pz, vx, vy, vz, t1, t2, t3):
    p1 = np.array([18, 19, 22])
    v1 = np.array([-1, -1, -2])
    #20, 25, 34 @ -2, -2, -4
    p2 = np.array([20, 25, 34])
    v2 = np.array([-2, -2, -4])
    # 12, 31, 28 @ -1, -2, -1
    p3 = np.array([12, 31, 28])
    v3 = np.array([-1, -2, -1])
    p = np.array([px, py, pz])
    v = np.array([vx, vy, vz])
    d1 = (p1-p)+(v1-v)*t1 
    d2 = (p2-p)+(v2-v)*t2
    d3 = (p3-p)+(v3-v)*t3
    return (d1**2+d2**2+d3**2).sum()
def f2(px, py, pz, vx, vy, vz, t1, t2, t3):
    #150191335679733, 257950211885619, 282767497332049 @ 239, 57, 42
    p1 = np.array([150191335679733, 257950211885619, 282767497332049.])
    v1 = np.array([239, 57, 42])
    #310843966440013, 307550528062309, 305058399233591 @ -42, -26, -8
    p2 = np.array([310843966440013, 307550528062309, 305058399233591.])
    v2 = np.array([-42, -26, -8])
    #368278994687085, 361265414214411, 295890220941673 @ -147, -124, 8
    p3 = np.array([368278994687085, 361265414214411, 295890220941673.])
    v3 = np.array([-147, -124, 8])
    
    #240206072440513, 257955942583195, 339853739319015 @ 44, 13, 18
    #p4 = np.array([240206072440513, 257955942583195, 339853739319015])
    #v4 = np.array([44, 13, 18])

    p = np.array([px, py, pz])
    v = np.array([vx, vy, vz])
    d1 = (p1-p)+(v1-v)*t1 
    d2 = (p2-p)+(v2-v)*t2
    d3 = (p3-p)+(v3-v)*t3
    return (d1**2+d2**2+d3**2).sum()
from scipy.optimize import minimize
result = minimize(lambda x: f2(*x), [0,0,0,1,1,1,0,100.,200.])
result
    
# %%
result.x
# %%

ts = open('input_p24.txt').read()
arr = []
for l in ts.split('\n'):
    if l=='':
        continue
    pos, v = l.split(' @ ')
    pos = [int(x) for x in pos.split(', ')]
    v = [int(x) for x in v.split(', ')]
    arr.append(pos+v)
# %%
arr = np.array(arr)
# %%
a
# %%
def cond(a):
    c1 = 320000000000000>=a[0]>=290000000000000
    c2 = 320000000000000>=a[1]>=290000000000000
    c3 = 320000000000000>=a[2]>=290000000000000
    return c1 and c2 and c3
params = [a for a in arr if cond(a)]
# %%
def f2(px, py, pz, vx, vy, vz, t1, t2, t3):
    #150191335679733, 257950211885619, 282767497332049 @ 239, 57, 42
    p1 = np.float64(params[0][:3])-300000000000000
    v1 = np.float64(params[0][3:])
    p2 = np.float64(params[1][:3])-300000000000000
    v2 = np.float64(params[1][3:])
    p3 = np.float64(params[2][:3])-300000000000000
    v3 = np.float64(params[2][3:])

    p = np.array([px, py, pz])
    v = np.array([vx, vy, vz])
    d1 = (p1-p)+(v1-v)*t1 
    d2 = (p2-p)+(v2-v)*t2
    d3 = (p3-p)+(v3-v)*t3
    return (d1**2+d2**2+d3**2).sum()
result = minimize(lambda x: f2(*x), [0,0,0,1,1,1,0,100.,200.])
result
# %%
p1 +v1 t1 = p +v t1
p2 +v2 t2 = p +v t2

(p1-p2) u + (v1 - v2) tu -v2 vu   = (p1-p3) v + (v1-v3) tv - v3 uv
# %%


kx, ky, kz

px+vx t = (k-t)x
py+vy t = (k-t)y
pz+vz t = (k-t)z

qx+ux s = (k-s)x
qy+uy s = (k-s)y
qz+uz s = (k-s)z


(px +vx t)/(qx+ux s) = (py+vy t)/(qy+uy s) = (pz+vz t)/(qz+uz s)
(px +vx t)(qy+uy s) = (py+vy t)(qx+ux s)
(px +vx t)(qz+uz s) = (pz+vz t)(qx+ux s)
# %%
(px +vx t)(qy+uy s) = (py+vy t)(qx+ux s)
(vx uy - vy ux) t s = (-px uy + py ux) s + (qx vy - qy vx) t


(px +vx t)(qz+uz s) = (pz+vz t)(qx+ux s)
(vx uz - vz ux) t s = (-px uz + pz ux) s + (qx vz - qz vx) t
#%%
params
# %%

p1 = np.int64(params[0][:3])
v1 = np.int64(params[0][3:])
p2 = np.int64(params[1][:3])
v2 = np.int64(params[1][3:])
p3 = np.int64(params[2][:3])
v3 = np.int64(params[2][3:])

p = [int(x) for x in p2-p1]
v = [int(x) for x in v2-v1]
q = [int(x) for x in p3-p1]
u = [int(x) for x in v3-v1]
#%%
p, v, q, u
#%%
type(p[0])
#%%

TS1 = v[0]*u[1]-v[1]*u[0]
T1 = v[0]*q[1]-v[1]*q[0]
S1 = p[0]*u[1]-p[1]*u[0]
C1 = p[0]*q[1]-p[1]*q[0]

TS2 = v[0]*u[2]-v[2]*u[0]
T2 = v[0]*q[2]-v[2]*q[0]
S2 = p[0]*u[2]-p[2]*u[0]
C2 = p[0]*q[2]-p[2]*q[0]
#%%
TS1, T1, S1, C1, TS2, T2, S2, C2
#%%

A = TS2*T1 - TS1*T2
B = TS2*S1 - TS1*S2
C = TS2*C1 - TS1*C2
# A t + B s  +C = 0
# so Bs = -A t - C

# TS1 t s + T1 t + S1 s + C1 =0 
# and since s = -A/B t - C/B
# so TS1 t (-A/B t - C/B) + T1 t + S1 (-A/B t - C/B) + C1 =0
#  -(TS1 A) t^2 +  ( -(TS1 C)  + T1 B - (S1 A) )t - (S1 C) + C1 =0
#%%
a = -TS1 * A
b = -(TS1 * C) + T1 * B - (S1 * A)
c = -(S1 * C) + B*C1

a,b,C
#%%
b**2 - 4*a*c
#%%
t = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)


# %%
import math
# %%
r = math.isqrt(b**2-4*a*c)
assert r**2 == b**2-4*a*c
# %%
t = (-b + r)//a//2
t
# %%
(-b - r)//a//2

# %%
s = (-A*t - C)//B
s
# %%
p2 +v2 t = p +v t
p3 +v3 s = p +v s
#%%
_p2 = [int(x) for x in p2]
_v2 = [int(x) for x in v2]
_p3 = [int(x) for x in p3]
_v3 = [int(x) for x in v3]
sol_v = []
sol_p = []
for i in range(3):
    r1 = _p2[i]- _p3[i] + _v2[i]*t -_v3[i]*s
    r2 = t-s
    print(r1%r2, r1//r2)
    sol_v.append(r1//r2)
    r3 = _p2[i] + _v2[i]*t - sol_v[i]*t
    r4 = _p3[i] + _v3[i]*s - sol_v[i]*s
    print(r3==r4)
    sol_p.append(r3)
    
    #- v3 *s = v(t-s)

# %%
type(t)
# %%
sol_p, sol_v
# %%
sum(sol_p)
# %%
