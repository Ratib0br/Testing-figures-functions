import unittest
import math
from figures.circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_3(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    def test_area_4(self):
        res = area(0.5)
        self.assertAlmostEqual(res, math.pi * 0.25)

    def test_area_5(self):
        res = area(10**6)
        self.assertAlmostEqual(res, math.pi * 10**12)

    def test_area_6(self):
        res = area(1e-6)
        self.assertAlmostEqual(res, math.pi * 1e-12)

    def test_area_7(self):
        res = area(-5)
        self.assertAlmostEqual(res, -1)


    def test_perimeter_1(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_2(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_3(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)

    def test_perimeter_4(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, math.pi)

    def test_perimeter_5(self):
        res = perimeter(10**6)
        self.assertAlmostEqual(res, 2 * math.pi * 10**6)

    def test_perimeter_6(self):
        res = perimeter(1e-6)
        self.assertAlmostEqual(res, 2 * math.pi * 1e-6)

    def test_perimeter_7(self):
        res = perimeter(-5)
        self.assertAlmostEqual(res, -1)