#%%
ts = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
ts = open('input_p4.txt').read()
total = 0
for l in ts.split('\n'):
    if l=='':
        continue
    l = l.split(': ')    
    a, b = l[1].split(' | ')
    a = a.replace('  ', ' ').lstrip(' ').rstrip(' ')
    b = b.replace('  ', ' ').lstrip(' ').rstrip(' ')
    a = [int(x) for x in a.split(' ')]
    b = [int(x) for x in b.split(' ')]
    print(a, b)
    n = len(set(a)&set(b))
    print(n)
    if n >0:
        total += 2**(n-1)
total

# %%
a
# %%
b
# %%

ts = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
ts = open('input_p4.txt').read()
cards = []
for l in ts.split('\n'):
    if l=='':
        continue
    l = l.split(': ')    
    a, b = l[1].split(' | ')
    a = a.replace('  ', ' ').lstrip(' ').rstrip(' ')
    b = b.replace('  ', ' ').lstrip(' ').rstrip(' ')
    a = [int(x) for x in a.split(' ')]
    b = [int(x) for x in b.split(' ')]
    print(a, b)
    n = len(set(a)&set(b))
    print(n)
    cards.append([n, 1])
cards
# %%
from collections import deque
q = deque(cards)
total = 0
while q:
    n, copies = q.popleft()
    if n >0:
        for i in range(n):
            q[i][1] += copies
    print(q)
    total += copies
total

# %%
q[1]
# %%
