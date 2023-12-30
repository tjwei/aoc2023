#%%
ts="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
#ts = open('input_p1.txt').read()
S=0
for l in ts.split('\n')[:-1]:
    n = "".join([x for x in l if x.isnumeric()])
    print(n[0]+n[-1])
    S+=int(n[0]+n[-1])
S
# %%
ts = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
ts = open('input_p1.txt').read()
englis_to_number = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for k,v in englis_to_number.items():
    ts = ts.replace(k, k+v+k)
S=0
for l in ts.split('\n')[:-1]:
    print(l)
    n = "".join([x for x in l if x.isnumeric()])
    print(n[0]+n[-1])
    S+=int(n[0]+n[-1])
S
# %%
ts
# %%
ts ="""25    8726   2962  ***
24   10035   4810  ***
23   12875   2991  ***
22   14344    970  ***
21   12867   9974  ****
20   16782   4283  ****
19   21047   7013  ****
18   23273   4949  *****
17   22492   1082  *****
16   33857    988  ******
15   39368   4043  *******
14   35155   7239  ******
13   36857   5065  ******
12   29657  14204  ******
11   55599   2295  *********
10   46809  16625  **********
 9   74331   1155  ***********
 8   72136  14341  ************
 7   79970   7133  ************
 6  101073   1815  ***************
 5   78504  30425  ****************
 4  127682  17274  *********************
 3  127854  19386  *********************
 2  192740   9041  ****************************
 1  226807  72476  *****************************************
 """
import pandas as pd
records = []
for l in ts.split('\n')[:-1]:
    qn, gold, silver, _ = l.split()
    print(qn, gold, silver)
    records.append({'qn': int(qn), 'gold': int(gold), 'silver': int(silver)})
df = pd.DataFrame(records)
df
# %%
df['s/g'] = df['silver']/df['gold']
df.sort_values('s/g').set_index('qn')
# %%
