from operator import truediv

import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input= [[7,8], [9,3]]
        result=lab4.first_element(input)
        expected = [7,9]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input= [8.0, 9.0]
        result=lab4.x_coordinates(input)
        expected=[8.0]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input=[99.1, 7.0]
        result = lab4.x_coordinates(input)
        expected = [99.1]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input=[8.0,4.0]
        result=lab4.are_in_positive_quadrant(input)
        expected=(input,  "is in the first quadrant")
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        input=[879.0,-127.0]
        result=lab4.are_in_positive_quadrant(input)
        expected=(input,  "is not in the first quadrant")
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        input=[[1.0, 3.0], [8.0, 9.0]]
        result=lab4.distance(input)
        expected=(9.2)
        self.assertAlmostEqual(expected, result)
    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
