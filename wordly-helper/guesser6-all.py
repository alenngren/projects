# add plasticity to be either 2 or 3 with 0,1, or 2 must have
import math
import copy

wordly = {
    'a1': '?',
    'a2': '?',
    'a3': '?',
    'a4': '?',
    'a5': '?',
}

choose_all = 'qwertyuiopasdfghjklzxcvbnm'

a = list(input("a??e?: "))
must_have = list(input("must have: ").split())
must_c = [i[0] for i in must_have]
must_ni = [i[1::] for i in must_have]
already_choose = input('already guessed: ')
choose = "".join(c for c in choose_all if c not in already_choose)

count_have = 0
for i, c in enumerate(a):
    if c != '?':
        wordly[f'a{i+1}'] = c
        count_have += 1

unknown = 5-count_have
count_must = len(must_c)

print(a, count_have)
print(must_have, len(must_c))

permu_group = []
for i in wordly:
    if wordly[i] == "?":
        permu_group.append(i)

permu_table = []
# special for 2 missing
if unknown == 3:
    for i in range(unknown):
        permu_table.append([permu_group[(0+i) % 3], permu_group[(1+i) % 3],
                            permu_group[(2+i) % 3]])
    for i in range(unknown):
        permu_table.append([permu_group[(2+i) % 3], permu_group[(1+i) % 3],
                            permu_group[(0+i) % 3]])
if unknown == 2:
    for i in range(unknown):
        permu_table.append([permu_group[(0+i) % 2], permu_group[(1+i) % 2]])

for i in permu_table:
    print(i)

# special to not generate what we already know
# permu_table.pop(1)
# permu_table.pop(2)
print('---')
# # add arsey and can take away a2 aswell from generating matrix
# permu_table.pop(2)
# permu_table.pop(0)
for i in permu_table:
    print(i)

# print(permu_table)
permu_table_c = copy.deepcopy(permu_table)


def choose_permu_table(k):
    permu_table_c = copy.deepcopy(permu_table)

    for i, l in enumerate(permu_table_c):
        for j, c in enumerate(l):
            if c == 'a2':
                permu_table_c[i][j] = must_have[0]
            if c == 'a3':
                permu_table_c[i][j] = must_have[1]
            if c == 'a5':
                permu_table_c[i][j] = k

    return permu_table_c


# have knowns, unknows, must_have here
def choose_permu_table3u(*args):
    if len(args) == 2 and isinstance(args[0], str):
        permu_table_c = copy.deepcopy(permu_table)
        for i, l in enumerate(permu_table_c):
            for j, c in enumerate(l):
                if c == 'a2':
                    permu_table_c[i][j] = must_have[0]
                if c == 'a3':
                    permu_table_c[i][j] = args[0]
                if c == 'a5':
                    permu_table_c[i][j] = args[1]
    elif len(args) == 1 and isinstance(args[0], str):
        permu_table_c = copy.deepcopy(permu_table)
        for i, l in enumerate(permu_table_c):
            for j, c in enumerate(l):
                if c == 'a2':
                    permu_table_c[i][j] = must_have[0]
                if c == 'a3':
                    permu_table_c[i][j] = must_have[1]
                if c == 'a5':
                    permu_table_c[i][j] = args[0]
    else:
        print('my error')
    return permu_table_c


def choose_permu_table2u(*args):
    if len(args) == 2 and isinstance(args[0], str):
        permu_table_c = copy.deepcopy(permu_table)
        for i, l in enumerate(permu_table_c):
            for j, c in enumerate(l):
                if c == 'a1':
                    permu_table_c[i][j] = args[0]
                if c == 'a3':
                    permu_table_c[i][j] = args[1]
    elif len(args) == 1 and isinstance(args[0], str):
        permu_table_c = copy.deepcopy(permu_table)
        for i, l in enumerate(permu_table_c):
            for j, c in enumerate(l):
                if c == 'a1':
                    permu_table_c[i][j] = must_have[0]
                if c == 'a3':
                    permu_table_c[i][j] = args[0]
    else:
        print('not accounted for, error!')
    return permu_table_c

wordly_c = wordly.copy()

sum_options = 0
# for m in list(choose):
#     for n in list(choose):
#         pmu_table = choose_permu_table2u(m, n)
#
#         for i in pmu_table:
#             # if (i[2] != "r" and 'r' != i[0]):
#             wordly_c['a1'] = i[0]
#             wordly_c['a3'] = i[1]
#             print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])
#             sum_options += 1
#             # else:
#             #         pass

# idea, iter over a1, a2, a3, a4, a5 (most possible options) -> improve from
# this number. Algorithm falls in choose function
choose_m = choose
choose_n = choose
choose_o = choose
choose_p = choose
choose_q = choose

index_list = [choose_m, choose_n, choose_o, choose_p, choose_q]
for i, k in enumerate(must_c):
    if '1' in must_ni[i]:
        choose_m = "".join(c for c in choose_m if c not in k)  # remove k (=u)
    if '2' in must_ni[i]:
        choose_n = "".join(c for c in choose_n if c not in k)
    if '3' in must_ni[i]:
        choose_o = "".join(c for c in choose_o if c not in k)
    if '4' in must_ni[i]:
        choose_p = "".join(c for c in choose_p if c not in k)
    if '5' in must_ni[i]:
        choose_q = "".join(c for c in choose_q if c not in k)


if wordly['a1'] != '?':
    choose_m = wordly['a1']
if wordly['a2'] != '?':
    choose_n = wordly['a2']
if wordly['a3'] != '?':
    choose_o = wordly['a3']
if wordly['a4'] != '?':
    choose_p = wordly['a4']
if wordly['a5'] != '?':
    choose_q = wordly['a5']

for m in list(choose_m):
    for n in list(choose_n):
        for o in list(choose_o):
            for p in list(choose_p):
                for q in list(choose_q):
                    if all(x in [m, n, o, p, q] for x in must_c):
                        wordly_c['a1'] = m
                        wordly_c['a2'] = n
                        wordly_c['a3'] = o
                        wordly_c['a4'] = p
                        wordly_c['a5'] = q
                        print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])
                        sum_options += 1


print('sum options: ', sum_options)
print(choose_m)
print(choose_n)
print(choose_o)
print(choose_p)
print(choose_q)
