import unittest
from figures.square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_3(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_4(self):
        res = area(0.5)
        self.assertAlmostEqual(res, 0.25)

    def test_area_5(self):
        res = area(10**6)
        self.assertEqual(res, 10**12)

    def test_area_6(self):
        res = area(1e-6)
        self.assertAlmostEqual(res, 1e-12)
    
    def test_area_7(self):
        res = area(-10)
        self.assertAlmostEqual(res, -1)


    def test_perimeter_1(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_perimeter_3(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
    def test_perimeter_4(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 6.0)

    def test_perimeter_5(self):
        res = perimeter(10**6)
        self.assertEqual(res, 4 * 10**6)

    def test_perimeter_6(self):
        res = perimeter(1e-6)
        self.assertAlmostEqual(res, 4 * 1e-6)

    def test_perimeter_7(self):
        res = perimeter(-4)
        self.assertAlmostEqual(res, -1)