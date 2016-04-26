FIELD = 8

class Polynomial:
    def __init__(self, a=0):
        if a > 255:
            raise Exception('polynomial not in GF(2^8)')

        self.polynomial = []
        i = a
        while i >= 1:
            remainder = i % 2
            self.polynomial.insert(0, remainder)
            i = i // 2
        # pad with 0
        while len(self.polynomial) < FIELD:
            self.polynomial.insert(0, 0)
        

    def toString(self):
        polyToString = ""
        s = self.polynomial[:]
        for i in range(len(s)):
            last = s.pop()
            if last > 0:
                if i == 0:
                    polyToString += "x^{} ".format(i)
                else:
                    polyToString += "+ x^{} ".format(i)
            elif last < 0:
                polyToString += "- x^{} ".format(i)

        return polyToString

    def addPolynomial(self, other):
        return self.addOrSubOp(other)

    def subPolynomial(self, other):
        return self.addOrSubOp(other)
 
    def addOrSubOp(self, other):
        result = []
        s = self.polynomial[:]
        o = other.polynomial[:]
        # do XOR operation for each elements in the polynomials
        for i in range(0, FIELD):
            si = (s.pop() ^ o.pop())
            result.insert(0, si)

        return result

    def multiplyPolynomial(self, other):
        times = 7
        for i in range(0, 7):
            if other.polynomial[i] == 1:
                self.multiplyByXTimes(times - 1)
            times -= 1

    def multiplyByXTimes(self, times):
        for i in range(times):
            self.multiplyByX()

    def multiplyByX(self):
        """Multiply a polynomial in GF(2^8)
        using m(x) = x^8 + x^4 + x^3 + x + 1
        as modulus polynomial"""
        aes_polynomial = [0, 0, 0, 1, 1, 0, 1, 1]
 
        # shift left
        self.polynomial.append(0)
        mvb = self.polynomial.pop(0)
        # if most valuable bit is 1, do the XOR with aes polynomial
        if mvb == 1:
            for i in range(0, FIELD):
                self.polynomial[i] = (self.polynomial[i] ^ aes_polynomial[i])
        print "function: {}".format(self.polynomial)


if __name__ == "__main__":
    p = Polynomial(18)
    print p.toString()
    print p.polynomial
    q = Polynomial(19)
    print q.toString()
    print q.polynomial
    r = p.addPolynomial(q)
    print r
