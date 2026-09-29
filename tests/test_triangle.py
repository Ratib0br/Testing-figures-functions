import unittest
from figures.triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(4, 5)
        self.assertEqual(res, 10)

    def test_area_4(self):
        res = area(3, 1.5)
        self.assertAlmostEqual(res, 2.25)

    def test_area_5(self):
        res = area(10**6, 10**6)
        self.assertEqual(res, 5 * 10**11)

    def test_area_6(self):
        res = area(1e-6, 1e-6)
        self.assertAlmostEqual(res, 5e-13)

    def test_area_7(self):
        res = area(-4, 5)
        self.assertAlmostEqual(res, 0)


    def test_perimeter_1(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_3(self):
        res = perimeter(6, 6, 6)
        self.assertEqual(res, 18)

    def test_perimeter_4(self):
        res = perimeter(0.5, 1.5, 2)
        self.assertAlmostEqual(res, 4.0)

    def test_perimeter_5(self):
        res = perimeter(10**6, 10**6, 10**6)
        self.assertEqual(res, 3 * 10**6)

    def test_perimeter_6(self):
        res = perimeter(1e-6, 1e-6, 1e-6)
        self.assertAlmostEqual(res, 3e-6)

    def test_perimeter_7(self):
        res = perimeter(3, -4, 5)
        self.assertAlmostEqual(res, 0)
    
    def test_perimeter_8(self):
        res = perimeter(8, 4, 3)
        self.assertAlmostEqual(res, 0)
