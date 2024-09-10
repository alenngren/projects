import numpy as np
import time


def main():
    return scan_eq()


def scan_eq():
    eq_string = input()
    print(eq_string)
    # print(id_eq(eq_string))
    gn = group_numbers(eq_string)
    id_eq(gn)
    return eq_string


def id_eq(grouped_numbers):
    n = grouped_numbers
    for i, c in enumerate(n):
        if (c == '+'):
            print(int(n[i-1])+int(n[i+1]))


def group_numbers(eq_string):
    split_eq = list(eq_string)
    group_split_eq = []
    numb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    oper = ['+']
    for i, c in enumerate(split_eq):
        if (i == len(split_eq)-1):
            if (split_eq[i-1] in numb):
                break
            else:
                group_split_eq.append(c)
        elif (c in numb):
            if (split_eq[i+1] in numb):
                i_tmp = "".join(split_eq[i:i+2])
                group_split_eq.append(i_tmp)
            else:
                if (i > 0): pass
                else:
                    group_split_eq.append(c)
        if (c in oper):
            group_split_eq.append(c)

    print(group_split_eq)
    return group_split_eq


main()
