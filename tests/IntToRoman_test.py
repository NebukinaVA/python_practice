import unittest
import tasks.IntToRoman as task


class MyTestCase(unittest.TestCase):
    '''
    Тесты для функции int_to_roman(), которая переводит целые числа арабского формата в римский
    '''
    def test_num_not_greater_than_3999(self):
        self.assertIsNone(task.int_to_roman(4000))

    def test_num_not_lesser_than_1(self):
        self.assertIsNone(task.int_to_roman(0))

    def test_with_addition(self):
        self.assertEqual('XVI', task.int_to_roman(16))

    def test_with_subtraction(self):
        self.assertEqual('XIV', task.int_to_roman(14))

    def test_max_roman_numeral(self):
        self.assertEqual('MMMCMXCIX', task.int_to_roman(3999))

    def test_min_roman_numeral(self):
        self.assertEqual('I', task.int_to_roman(1))

    def test_one_more_roman_numeral(self):
        self.assertEqual('DCCXLIX', task.int_to_roman(749))

if __name__ == '__main__':
    unittest.main()
