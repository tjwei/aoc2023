#%%
case1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

case2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

txt = case2
txt = open('input_p20_1.txt').read()
nodes = {}
for l in txt.split('\n'):
    if l=='':
        continue
    src, dests = l.split(' -> ')
    dests = dests.split(', ')
    for n in dests:
        if n not in nodes:
            nodes[n] = {'type': 'output', 'inputs': {}, 'outputs': []} 
    if src[0] in ['%', '&']:
        src_type = src[0]
        src = src[1:]
    elif src == 'broadcaster':
        src_type = 'broadcaster'
    if src not in nodes:
        nodes[src] = {'inputs': {}}
    nodes[src]['type'] = src_type
    for n in dests:
        nodes[n]['inputs'][src] = 0
    nodes[src]['outputs'] = dests
    print(src, dests)
for n in nodes:
    if nodes[n]['type'] != '&':
        del nodes[n]['inputs']
    if nodes[n]['type'] == '%':
        nodes[n]['state'] = 0
nodes
#%%
nodes['broadcaster']['outputs']
# %%
nodes['broadcaster']['outputs']=['fd']
#%%
nodes['nr']['outputs'].remove('fn')
#%%
n = 'fd'
node_keys = []
while True:
    node_keys.append(n)
    next_n = nodes[n]['outputs'].copy()
    if 'nr' in next_n:
        next_n.remove('nr')
    if next_n == []:
        break
    assert len(next_n)==1
    n = next_n[0]
node_keys
#%%
from collections import deque
high, low = 1, 0
queue = deque()
total_high = 0
total_low = 0
for i in range(3847*3):
    queue.append(('button', 'broadcaster', low))
    while queue:
        s, n, signal = queue.popleft()
        if signal == high:
            total_high +=1
        else:
            total_low +=1
        #if not (signal==high and nodes[n]['type']=='%'):
        #    print(f"{s} -{['low', 'high'][signal]}-> {n}")
        node = nodes[n]
        if node['type'] == 'broadcaster':
            for o in node['outputs']:
                #print(f'\tadd {(n, o, signal)}')
                queue.append((n, o, signal))        
        elif node['type'] == '%':
            if signal ==low:
                node['state'] = 1-node['state']
                for o in node['outputs']:
                    #print(f'\tadd {(n, o, signal)}')
                    queue.append((n, o, node['state']))
        elif node['type'] == '&':
            assert s in node['inputs']
            node['inputs'][s] = signal
            #print(node)
            signal = low if all(node['inputs'].values()) else high
            if signal ==low:
                print('signal is low', i)
            for o in node['outputs']:
                #print(f'\tadd {(n, o, signal)}')
                queue.append((n, o, signal))
        elif node['type'] == 'output':
            #print('output', n, signal)
            pass
        else:
            raise Exception('invalid node type', node)
    if (i+1)%3847==0:
        print('---------------')
    print(i+1, bin(i+1), [nodes[n]['state'] for n in node_keys])
    #print(i+1, bin(i+1), [nodes['nr']['inputs'].get(n, 2) for n in node_keys])
    

#%%


#%%
next_n 
    

# %%
total_high * total_low
# %%
for n in nodes:
    if 'rx' in nodes[n]['outputs']:
        print(n)
#%%
nodes['nc']
# %%
for n in nodes['nc']['inputs']:
    n2 = list(nodes[n]['inputs'].keys())[0]
    print(n, nodes[n], nodes[n2])

# %%
nodes['lk']
#%%
import networkx as nx
G = nx.DiGraph()
for n in nodes:
    for o in nodes[n]['outputs']:
        G.add_edge(n, o)

nx.nx_agraph.to_agraph(G).draw('graph.png', prog='dot')
# %%
sg_v = {}
for sg in nx.strongly_connected_components(G):
    n = ",".join(sg)
    sg_v[n] = sg
#%%
G = nx.DiGraph()
for n in nodes:
    for o in nodes[n]['outputs']:
        for sg in sg_v:
            if n in sg_v[sg]:
                n_sg = sg
            if o in sg_v[sg]:
                o_sg = sg
        if n_sg != o_sg:
            G.add_edge(n_sg, o_sg)
nx.nx_agraph.to_agraph(G).draw('graph2.png', prog='dot')
# %%
#sg = sg_v['tf,cf,cb,nr,kd,gr,fd,nv,cm,df,xc,jh,vq'] #3847
#sg = sg_v['hr,xl,kv,jd,bm,qq,xr,fj,nm,rb,pt,lg,dh'] # 4027
#sg = sg_v['ls,gl,xn,ms,zg,sp,mz,rz,xg,dd,hx,mj,vm'] # 3851
sg = sg_v['gk,mp,dg,fp,fl,jk,bn,hq,ql,rj,kj,tp,cc'] # 4003
#sg = sg_v['ls,gl,xn,ms,zg,sp,mz,rz,xg,dd,hx,mj,vm']
sg.add('broadcaster')
G = nx.DiGraph()
for n in nodes:
    for o in nodes[n]['outputs']:
        if n in sg and o in sg:
            o2, n2 = o, n
            if nodes[n]['type'] == '&':
                n2 = '&'+n
            if nodes[o]['type'] == '&':
                o2 = '&'+o
            print(n, o)
            if nodes[n]['type'] != '&':
                G.add_edge(n2, o2)
nx.nx_agraph.to_agraph(G).draw('graph6.png', prog='dot')
# %%
sg_v
# %%
from math import gcd, lcm
lcm(3847, 4027, 3851, 4003)
# %%
