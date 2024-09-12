# remake to take input
import math
import copy

wordly = {
    'a1': '?',
    'a2': '?',
    'a3': '?',
    'a4': '?',
    'a5': '?',
}

# choose = 'qwerypfghjkzxcvbnm'
choose_all = 'qwertyuiopasdfghjklzxcvbnm'
# must_have = ['t', 'l']
# a = ['a', '?', '?', 'a', '?']

a = list(input("s?or?: "))
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


permu_group = []
for i in wordly:
    if wordly[i] == "?":
        permu_group.append(i)

print(unknown, "check")
# print(unknown)
# print(permu_group)

permu_table = []
# special for 2 missing

for i in range(unknown):
    permu_table.append([permu_group[(0+i) % 2], permu_group[(1+i) % 2]])

for i in permu_table:
    print(i)

# print(permu_table)
permu_table_c = copy.deepcopy(permu_table)

for i, l in enumerate(permu_table_c):
    for j, c in enumerate(l):
        if c == 'a2':
            permu_table_c[i][j] = must_have[0]
        if c == 'a3':
            permu_table_c[i][j] = must_have[1]
        if c == 'a5':
            permu_table_c[i][j] = "?"


def choose_permu_table(k):
    permu_table_c = copy.deepcopy(permu_table)

    for i, l in enumerate(permu_table_c):
        for j, c in enumerate(l):
            if c == 'a2':
                permu_table_c[i][j] = must_have[0]
            if c == 'a5':
                permu_table_c[i][j] = k

    return permu_table_c


wordly_c = wordly.copy()


pmu_table = choose_permu_table(choose[4])

for i in pmu_table:
    wordly_c['a2'] = i[0]
    wordly_c['a5'] = i[1]
    print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])

for i in list(choose):
    pmu_table = choose_permu_table(i)

    for i in pmu_table:
        wordly_c['a2'] = i[0]
        wordly_c['a5'] = i[1]
        print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])


# permu_table_c

# pmu_table
