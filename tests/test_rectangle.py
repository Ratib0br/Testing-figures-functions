import unittest
from figures.rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_3(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_4(self):
        res = area(0.5, 4)
        self.assertAlmostEqual(res, 2.0)

    def test_area_5(self):
        res = area(10**6, 10**5)
        self.assertEqual(res, 10**11)

    def test_area_6(self):
        res = area(1e-6, 1e-7)
        self.assertAlmostEqual(res, 1e-13)
    
    def test_area_7(self):
        res = area(-10, 2)
        self.assertAlmostEqual(res, -1)


    def test_perimeter_1(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_perimeter_3(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)
    
    def test_perimeter_4(self):
        res = perimeter(0.5, 1.5)
        self.assertAlmostEqual(res, 4.0)

    def test_perimeter_5(self):
        res = perimeter(10**6, 10**5)
        self.assertEqual(res, 2 * 10**6 + 2 * 10**5)

    def test_perimeter_6(self):
        res = perimeter(1e-6, 1e-6)
        self.assertAlmostEqual(res, 4 * 1e-6)

    def test_perimeter_7(self):
        res = perimeter(3, -4)
        self.assertAlmostEqual(res, -1)