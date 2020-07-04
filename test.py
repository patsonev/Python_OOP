class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sbor(self):
        c = self.a + self.b
        return c

    def deleno(self):
        d = Test.sbor(self) / 2
        return d

    def umnojenie(self):
        e = Test.deleno(self) ** 2
        return e


chisla = Test(2, 4)
print(chisla.deleno())
print(chisla.umnojenie())
