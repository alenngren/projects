import time


def cnumber(x, y):
    return x, y


def add(c1, c2):
    return c1[0]+c2[0], c1[1]+c2[1]


def mult(c1, c2):
    return c1[0]*c2[0]-c1[1]*c2[1], c1[0]*c2[1]+c1[1]*c2[0]


def cconju(z):
    return z[0], -1*z[1]


def absc(z):
    return mult(z, cconju(z))


def readx(x):
    print(type(x))
    breakout_index = []
    for i, c in enumerate(x):
        if (c == "("):
            breakout_index.append(i)
            for j, c in enumerate(x):
                if (c == ")"):
                    breakout_index.append(j)



    oper = ["+"]
    numb = ['1', '2', '3']
    print(breakout_index)
    for i in range(breakout_index[0]+1, breakout_index[1]):
        print(i, x[i])
        if (x[i] in oper):
            print(f"operator {x[i]}")
            y = int(x[i-1])+int(x[i+1])
            print("y =",  y)
        if (x[i] in numb):
            print(f"numb in {int(x[i])}")
            if(x[i+1] in numb):
                print(x[i:i+1])



def main():
    x = input()
    if (x == "exit"):
        return 1
    else:
        start = time.time()
        readx(x)
        end = time.time()
        print(end-start, "seconds")
        return 1
        return main()


print("---")
main()


# x = cnumber(1, 2)
# y = cnumber(2, 3)
# print('x = ', x)
# print('y = ', y)
# print("x + y = ", add(x, y))
# print("x * y = ", mult(x, y))
# print('abs(x) = ', absc(x))
