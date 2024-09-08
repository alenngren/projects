class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __str__(self):
        return f'{self.real}, i{self.imag}'

    def __repr__(self):
        return f'Complex, {self.real}, i{self.imag}'


def main():
    z = Complex(1, 1)
    w = Complex(0, 5)

    print(w)
    print(z)
    print(z.__add__(w))
    print(z+w)


main()
