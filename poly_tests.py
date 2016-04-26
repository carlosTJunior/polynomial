import unittest
from poly_wants_a_cracker import Polynomial


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p = Polynomial()

    def test_multiplyByX_1(self):
        self.p = Polynomial(87)
        l = [1, 0, 1, 0, 1, 1, 1, 0]
        self.p.multiplyByX()
        self.assertEqual(l, self.p.polynomial)

    def test_multiplyByX_2(self):
        self.p = Polynomial(137)
        l = [0, 0, 0, 0, 1, 0, 0, 1]
        self.p.multiplyByX()
        self.assertEqual(l, self.p.polynomial)

    def test_multiplyByXTimes_1(self):
        self.p = Polynomial(87)
        l = [0, 1, 0, 0, 0, 1, 1, 1]
        self.p.multiplyByXTimes(2)
        self.assertEqual(l, self.p.polynomial)

    def test_multiplyByXTimes_2(self):
        self.p = Polynomial(87)
        l = [0, 0, 0, 0, 0, 1, 1, 1]
        self.p.multiplyByXTimes(4)
        self.assertEqual(l, self.p.polynomial)

    def test_multiplyByXTimes_3(self):
        self.p = Polynomial(87)
        l = [1, 1, 0, 1, 1, 0, 1, 1]
        self.p.multiplyByXTimes(10)
        self.assertEqual(l, self.p.polynomial)

    def test_multiplyPolynomial(self):
        p = Polynomial(87)
        q = Polynomial(131)
        l = [1, 1, 0, 0, 0, 0, 0, 1]
        r = p.multiplyPolynomial(q)
        self.assertEqual(l, r)

    def test_addOrSubOp_1(self):
        p = Polynomial(8)
        q = Polynomial(9)
        r = p.addOrSubOp(q)
        l = [0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(l, r)

    def test_addOrSubOp_2(self):
        p = Polynomial(87)
        q = Polynomial(150)
        r = p.addOrSubOp(q)
        l = [1, 1, 0, 0, 0, 0, 0, 1]
        self.assertEqual(l, r)

if __name__ == "__main__":
    unittest.main()
