#%%
ts="""Time:      7  15   30
Distance:  9  40  200
"""
ts = """Time:        62     64     91     90
Distance:   553   1010   1473   1074"""
ts="""Time:      71530
Distance:  940200
"""

ts = """Time:        62649190
Distance:   553101014731074"""
lines = list(ts.split('\n'))
times = [int(x) for x in lines[0].split(':')[1].split(' ') if x]
distances = [int(x) for x in lines[1].split(':')[1].split(' ') if x]
times, distances
# %%
from math import isqrt 
ans = 1
for t,d in zip(times, distances):
    #print(t,d)
    # s**2-t*s +d+1 <=0
    m = isqrt(t**2-4*d-4)
    a, b = (t-m)//2+(t-m)%2, (t+m)//2
    #print(a,b, a*(t-a), b*(t-b))
    rtn = b - a +1
    #print(m)
    print(rtn)
    ans*=rtn
ans


# %%
7**2-40
# %%
