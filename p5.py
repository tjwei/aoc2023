#%%
ts="""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
ts = open('input_p5.txt').read()
rules = {}
next_target = {}
for l in ts.split('\n'):
    if l=='':
        continue
    if l.startswith('seeds:'):
        seeds = [int(x) for x in l.split(' ')[1:]]
        print(seeds)
    elif ':' in l:
        f, t = l.split(':')[0][:-4].split('-to-')
        rules[f]=[]
    else:
        ti, fi, n = [int(x) for x in l.split(' ')]
        rules[f].append((ti, fi, n))
        next_target[f] = t
rules
# %%
def translate(rule_list, i):
    for ti, fi, n in rule_list:
        if fi+n > i>=fi:
            return ti + (i-fi)
    return i
rules
#%%
next_target
# %%
locations = []
for s in seeds:
    i = s
    f = 'seed'
    chain = [(f, i)]
    while f!='location':
        i = translate(rules[f], i)
        f = next_target[f]
        chain.append((f, i))
    print(chain)
    locations.append(i)
print(min(locations))



# %%
seeds
it = iter(seeds)
seed_ranges = [(a, a+b-1) for a, b in zip(it, it)]
seed_ranges
# %%

def translate_range_1(rule, r):
    ti, fi, n = rule
    rs, re = r
    fs, fe = fi, fi+n-1
    ts, te = ti, ti+n-1
    shift = ti - fi
    # 4x3 = 12, there are 12 possible segments, but some of them are invalid
    unmapped_segs = []
    mapped_segs = []
    # fs, fe
    if  rs <=fs <= fe <= re:
        #print('fs fe', fs+shift, fe+shift)
        mapped_segs.append( (ts, te))
    # fs rs # not possible
    # fs re
    if rs <=fs <= re <= fe:
        #print('fs re', fs+shift, re+shift)
        mapped_segs.append( (fs+shift, re+shift))
    # fe fs # not possible
    # fe rs # not possible
    # fe re
    if rs<=fe < re:
        #print('fe re', fe+1, re)
        unmapped_segs.append((fe+1, re))
    # rs fs 
    if rs < fs <= re:
        #print('rs fs', rs, fs-1)
        unmapped_segs.append((rs, fs-1))
    # rs fe
    if fs<=rs <= fe<=re:
        #print('rs fe', rs+shift, fe+shift)
        mapped_segs.append((rs+shift, fe+shift))
    # rs re
    if fs <= rs <= re <=fe:
        #print('rs re', rs+shift, re+shift)
        mapped_segs.append((rs+shift, re+shift)) 
    if re < fs or rs > fe:
        #print('rs re', rs, re)
        unmapped_segs.append((rs, re))
    for s, e in mapped_segs:
        assert s<=e
    for s, e in unmapped_segs:
        assert s<=e
    mapped_segs = set(mapped_segs)
    unmapped_segs = set(unmapped_segs)
    return mapped_segs, unmapped_segs

def simplify_ranges(range_list):
    sorted_ranges = sorted(range_list)
    #print(sorted_ranges)
    output_ranges = []
    current_range = None
    for r in sorted_ranges:
        if current_range is None:
            current_range = r
            continue
        if r[0] <= current_range[1]+1:
            assert r[0] == current_range[1]+1
            current_range = (current_range[0], max(current_range[1], r[1]))
        else:
            output_ranges.append(current_range)
            current_range = r
    if current_range is not None:
        output_ranges.append(current_range)
    return output_ranges

def translate_ranges_1(rule, ranges):
    mapped_ranges = []
    unmapped_ranges = []
    #print('translate_ranges_1', rule, ranges)
    for r in ranges:
        mapped, unmapped = translate_range_1(rule, r)
        mapped_ranges.extend(mapped)
        unmapped_ranges.extend(unmapped)
    return mapped_ranges, unmapped_ranges

def translate_ranges(rule_list, ranges):
    unmapped_ranges = ranges
    mapped_ranges = []
    for rule in rule_list:        
        mapped, unmapped_ranges = translate_ranges_1(rule, unmapped_ranges)
        mapped_ranges.extend(mapped)
        #print('mapped_ranges', mapped_ranges)
        #print('unmapped_ranges', unmapped_ranges)
    output_ranges = simplify_ranges(mapped_ranges+unmapped_ranges)
    return output_ranges

#%%

locations = []
for s in seed_ranges:
    r = [s]
    f = 'seed'
    chain = [(f, r)]
    #print(f, r)
    while f!='location':        
        r = translate_ranges(rules[f], r)
        f = next_target[f]
        chain.append((f, r))
        #print(f,r)
    #print(chain)
    locations.append(min(r)[0])
#%%
min(locations)

# %%
translate_range_1(rules['seed'][0], (1,100) )
#%%
translate_ranges_1(rules['seed'][0], [(1,100)] )
#%%
translate_ranges(rules['seed'], [(79, 92)] )
#%%
rules['seed'][0]
# %%
rules['seed'][0]
# %%
# %%
seed_ranges
# %%
