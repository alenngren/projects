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

choose = 'qwerypfghjkzxcvbnm'
# must_have = ['t', 'l']
# a = ['a', '?', '?', 'a', '?']

a = list(input("a??a?: "))
must_have = list(input("must have: "))

count_have = 0
for i, c in enumerate(a):
    if c != '?':
        wordly[f'a{i+1}'] = c
        count_have+=1

count_must = len(must_have)

# for i in list(choose):
#     wordly_c = wordly.copy()
#     for j in wordly_c:
#         if wordly_c[j] == '?':
#             wordly_c[j] = i
#     print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])


# for i in must_have:
#     wordly_c = wordly.copy()
#     for j in wordly_c:
#         if wordly_c[j] == '?':
#             wordly_c[j] = i
#     print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])

# add rotation to words testing

unknown = 0
permu_group = []
for i in wordly:
    if wordly[i] == "?":
        unknown += 1
        permu_group.append(i)

# print(unknown)
# print(permu_group)

permu_table = []
for i in range(unknown):
    permu_table.append([permu_group[(0+i)%3], permu_group[(1+i)%3], permu_group[(2+i)%3]])

for i in range(unknown):
    permu_table.append([permu_group[(2+i)%3], permu_group[(1+i)%3], permu_group[(0+i)%3]])

(permu_table)


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
            if c == 'a3':
                permu_table_c[i][j] = must_have[1]
            if c == 'a5':
                permu_table_c[i][j] = k

    return permu_table_c


permu_table_c


wordly_c = wordly.copy()



pmu_table = choose_permu_table(choose[4])

for i in pmu_table:
    wordly_c['a2'] = i[0]
    wordly_c['a3'] = i[1]
    wordly_c['a5'] = i[2]
    print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])

for i in list(choose):
    pmu_table = choose_permu_table(i)

    for i in pmu_table:
        wordly_c['a2'] = i[0]
        wordly_c['a3'] = i[1]
        wordly_c['a5'] = i[2]
        print(wordly_c['a1'],wordly_c['a2'],wordly_c['a3'],wordly_c['a4'],wordly_c['a5'])


# permu_table_c

# pmu_table
