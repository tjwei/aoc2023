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
englis_to_number = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                     'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
for k,v in englis_to_number.items():
    ts = ts.replace(k, v)
S=0
for l in ts.split('\n')[:-1]:
    n = "".join([x for x in l if x.isnumeric()])
    print(n[0]+n[-1])
    S+=int(n[0]+n[-1])
S
# %%
ts
# %%
