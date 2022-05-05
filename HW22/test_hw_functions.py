import unittest
from hw_functions import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):

    def test_call(self):
        fibo1 = Fibonacci()
        fibo1(10)

        self.assertEqual(fibo1(5), 5)
        self.assertEqual(fibo1(0), 0)
        self.assertEqual(fibo1.cache, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        with self.assertRaises(ValueError):
            fibo1(-1)


class TestFormattedName(unittest.TestCase):

    def test_formatted_name(self):
        first_name = "John"
        last_name = "Doe"
        middle_name = "Jr."
        self.assertEqual(formatted_name(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name
        ),
            "John Jr. Doe")
        self.assertEqual(formatted_name(
            first_name=first_name,
            last_name=last_name,
        ),
            "John Doe")


if __name__ == "__main__":
    unittest.main()












