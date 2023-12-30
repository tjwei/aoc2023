#%%
ts = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
ts = open('input_p7.txt').read()
from collections import Counter
def get_rank(h):
    stats = sorted(Counter(h).values(), reverse=True)
    stats = tuple(stats)
    return stats
tbl = {c: 14-i for i, c in enumerate("AKQJT98765432")}
def hand_num(h):
    return tuple(tbl[c] for c in h)

all_hands = []
for l in ts.split('\n'):
    if l=='':
        continue
    assert l[5]==' '
    h, b = l.split(' ')
    assert len(h)==5
    b = int(b)
    r = get_rank(h)
    n = hand_num(h)
    print(r, n, b, h)
    all_hands.append((r, n, b, h))
# %%
# %%
all_hands.sort()
# %%
sum((i+1)*b for i, (r,n,b,h) in enumerate(all_hands))
# %%

#%%
ts = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
ts = open('input_p7.txt').read()
from collections import Counter
def get_rank(h):
    h2 = "".join(x for x in h if x!='J')
    jn = len(h)-len(h2)
    if jn == 5:
        return (5,)
    stats = sorted(Counter(h2).values(), reverse=True)
    stats[0]+=jn
    stats = tuple(stats)
    return stats
tbl = {c: 14-i for i, c in enumerate("AKQT98765432J")}
def hand_num(h):
    return tuple(tbl[c] for c in h)

all_hands = []
for l in ts.split('\n'):
    if l=='':
        continue
    assert l[5]==' '
    h, b = l.split(' ')
    assert len(h)==5
    b = int(b)
    r = get_rank(h)
    n = hand_num(h)
    print(r, n, b, h)
    all_hands.append((r, n, b, h))
# %%
all_hands.sort()
# %%
sum((i+1)*b for i, (r,n,b,h) in enumerate(all_hands))
# %%
