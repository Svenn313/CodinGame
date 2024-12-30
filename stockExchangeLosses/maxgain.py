#!/usr/bin/env python3

import unittest


# Function to calculate max gain
def calculate_max_gain(values):
    if values == []:
        max_gain = 0
        return max_gain

    cur_min = values[0]
    max_gain = 0

    for i in range(len(values)):
        if values[i] < cur_min:
            cur_min = values[i]
        elif values[i] > cur_min:
            gain = values[i] - cur_min
            if gain > max_gain:
                max_gain = gain 
    return max_gain

# Test suite
class TestMaxGain(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(calculate_max_gain([3, 2, 4, 2, 12, 11]), 10)

    def test_no_gain(self):
        self.assertEqual(calculate_max_gain([10, 9, 8, 7, 6]), 0)

    def test_all_increasing(self):
        self.assertEqual(calculate_max_gain([1, 2, 3, 4, 5]), 4)

    def test_all_decreasing(self):
        self.assertEqual(calculate_max_gain([5, 4, 3, 2, 1]), 0)

    def test_single_element(self):
        self.assertEqual(calculate_max_gain([42]), 0)

    def test_empty_list(self):
        self.assertEqual(calculate_max_gain([]), 0)

    def test_repeated_values(self):
        self.assertEqual(calculate_max_gain([7, 7, 7, 7, 7]), 0)

    def test_large_gain_at_end(self):
        self.assertEqual(calculate_max_gain([5, 1, 2, 3, 10]), 9)

    def test_large_list(self):
        values = [i for i in range(1000, 0, -1)]  # Decreasing list
        self.assertEqual(calculate_max_gain(values), 0)

    def test_fluctuating_values(self):
        self.assertEqual(calculate_max_gain([1, 5, 3, 8, 4, 9]), 8)

# Run tests
if __name__ == "__main__":
    unittest.main()