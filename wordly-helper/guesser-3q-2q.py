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
must_have = list(input("must have: "))
already_choose = input('already guessed: ')
choose = "".join(c for c in choose_all if c not in already_choose)
count_have = 0
for i, c in enumerate(a):
    if c != '?':
        wordly[f'a{i+1}'] = c
        count_have += 1

unknown = 5-count_have
count_must = len(must_have)

print(a, count_have)
print(must_have, len(must_have))

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
for m in list(choose):
    for n in list(choose):
        pmu_table = choose_permu_table2u(m, n)

        for i in pmu_table:
            # if (i[2] != "r" and 'r' != i[0]):
            wordly_c['a1'] = i[0]
            wordly_c['a3'] = i[1]
            print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])
            sum_options += 1
            # else:
            #         pass

print('sum options: ', sum_options)
# failed at 392 options, do better algo! Even with 1/2 chance failed with web
# help
# good example audio
# untie, 
# u can only be a3,a4,a5
# i can only be a1, a5
# e can only be a1, a3, a4
