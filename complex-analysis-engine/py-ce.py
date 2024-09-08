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
    y = x.split('+')
    print(y)
    print(sum(list(map(int, y))))


def main():
    x = input()
    if (x == "exit"):
        return 1
    else:
        start = time.time()
        readx(x)
        end = time.time()
        print(end-start, "seconds")
        return main()

print("---")
# main()


x = cnumber(1, 2)
y = cnumber(2, 3)
print('x = ', x)
print('y = ', y)

print("x + y = ", add(x, y))
print("x * y = ", mult(x, y))
print('abs(x) = ', absc(x))
