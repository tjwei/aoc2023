#%%
ts = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
ts = open('input_p19_1.txt').read()
def cond(r, data):
    match r:
        case [dest]:
            return dest
        case [expr, dest]:
            assert expr[1] in ['<', '>']
            k, op, v = expr[0], expr[1], int(expr[2:])
            if op == '<':
                return dest if data[k]<v else None
            elif op == '>':
                return dest if data[k]>v else None
    raise Exception('invalid rule', r)

def run_rule(rule, data):
    for r in rule:
        dest = cond(r, data)
        if dest is not None:
            return dest
    raise Exception('no rule match', rule, data)
            
rules = {}
lines = iter(ts.split('\n'))
for l in lines:
    if l=='':
        break
    name, rs = l.split('{')
    rs = rs[:-1].split(',')
    rs = [r.split(':') for r in rs]
    print('rule', name, rs)
    rules[name] = rs
print()

result = 0
for l in lines:
    if l=='':
        break
    data = l[1:-1].split(',')
    data = (d.split('=') for d in data)
    data = {k:int(v) for k,v in data}
    print('part', data)
    step = 'in'
    while step not in  ['A', 'R']:
        print(step)
        step = run_rule(rules[step], data)
    print(step)
    if step == 'A':
        S = sum(data.values())
        print(S)
        result +=S
print('done', result)
    
# %%
len(rules)
# %%
paths = []
def find_paths(step, path=[], conds=[], prev_conds=[]):
    if step in ['A', 'R']:
        if step == 'A':
            paths.append((path, conds, prev_conds)) 
        return
    prev_conds = prev_conds.copy()
    for r in rules[step]:
        dest = r[-1]
        cond_next = conds
        if len(r)>1:
            cond_next = conds+[r[0]]
        find_paths(dest, path+[dest], conds=cond_next, prev_conds=prev_conds.copy())
        if len(r)>1:
            prev_conds.append(r[0])
find_paths('in', [])
# %%
len(paths)
paths
# %%
result = 0
for path, conds, prev_conds in paths:
    bounds = {k:[1,4000] for k in 'xmas'}
    for cond in prev_conds:
        k, op, v = cond[0], cond[1], int(cond[2:])
        if op == '>':
            bounds[k][1] = min(bounds[k][1], v)
        elif op == '<':
            bounds[k][0] = max(bounds[k][0], v)
    for cond in conds:
        k, op, v = cond[0], cond[1], int(cond[2:])
        if op == '<':
            bounds[k][1] = min(bounds[k][1], v-1)
        elif op == '>':
            bounds[k][0] = max(bounds[k][0], v+1)
    print(bounds)
    total = 1
    for b in bounds.values():
        assert b[0]<=b[1]
        total *= b[1]-b[0]+1
    print(total)
    result += total
print('done', result)
# %%
