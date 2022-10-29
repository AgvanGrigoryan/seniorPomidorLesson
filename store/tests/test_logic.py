from django.test import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, -1, '+')
        self.assertEqual(5, result)

    def test_minus(self):
        result = operations(15, 4, '-')
        self.assertEqual(11, result)

    def test_multiply(self):
        result = operations(13, 4, '*')
        self.assertEqual(52, result)
