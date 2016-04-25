class Polynomial:
    def __init__(self, a):
        self.polynomial = []
        i = a
        while i >= 1:
            remainder = i % 2
            i = i // 2
            self.polynomial.insert(0, remainder)

    def toString(self):
        polyToString = ""

        for i in range(len(self.polynomial)):
            last = self.polynomial.pop()
            if last > 0:
                if i == 0:
                    polyToString += "x^{} ".format(i)
                else:
                    polyToString += "+ x^{} ".format(i)
            elif last < 0:
                polyToString += "- x^{} ".format(i)

        return polyToString

    def addPolynomial(self, other):
        s = []
        # len(self.polynomial) >= len(b)
        for i in range(len(self.polynomial)):
            if len(other.polynomial) > 0:
                si = (self.polynomial.pop() + other.polynomial.pop()) % 2
                print si
                s.insert(0, si)
            else:
                s.insert(0, self.polynomial.pop())

        return s

    def negativePolinomial(self, a):
        n = []
        for i in range(len(a)):
            ni = -(a.pop())
            n.insert(0, ni)

        return n

    def subPolynomial(self, a, b):
        s = negativePolinomial(b)
        result = addPolynomial(a, s)

        return result


if __name__ == "__main__":
    p = Polynomial(8)
    print p.polynomial
    print p.toString()

    q = Polynomial(9)
    print p.addPolynomial(q)
    print "q = {}".format(q.polynomial)
