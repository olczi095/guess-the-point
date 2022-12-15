import unittest
from guess_the_point import Rectangle


class TestRectangle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rectangle = Rectangle()

    def test_validation_should_be_greater_or_equal_minus_two_hundred(self):
        self.assertGreaterEqual(self.rectangle.point1[0], -200)
        self.assertGreaterEqual(self.rectangle.point1[1], -200)
        self.assertGreaterEqual(self.rectangle.point2[0], -200)
        self.assertGreaterEqual(self.rectangle.point2[1], -200)

    def test_validation_should_be_less_or_equal_two_hundred(self):
        self.assertLessEqual(self.rectangle.point1[0], 200)
        self.assertLessEqual(self.rectangle.point1[1], 200)
        self.assertLessEqual(self.rectangle.point2[0], 200)
        self.assertLessEqual(self.rectangle.point2[1], 200)
