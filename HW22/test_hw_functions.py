import unittest
from hw_functions import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):

    def setUp(self):
        self.fibo1 = Fibonacci()
        self.fibo1(10)

    def test_call_positive(self):
        self.assertEqual(self.fibo1(5), 5)

    def test_call_zeros(self):
        self.assertEqual(self.fibo1(0), 0)

    def test_fibo_cache(self):
        self.assertEqual(self.fibo1.cache, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_negative(self):
        with self.assertRaises(ValueError):
            self.fibo1(-1)

    def test_string(self):
        with self.assertRaises(ValueError):
            self.fibo1("str")

    def test_call_float(self):
        with self.assertRaises(ValueError):
            self.fibo1(5.5)


class TestFormattedName(unittest.TestCase):

    def setUp(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.middle_name = "Jr."

    def test_formatted_fullname(self):
        self.assertEqual(formatted_name(
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.middle_name
        ),
            "John Jr. Doe")

    def test_formatted_no_middle(self):
        self.assertEqual(formatted_name(
            first_name=self.first_name,
            last_name=self.last_name,
        ),
            "John Doe")

    def test_title_method(self):
        self.assertEqual(formatted_name(
            first_name="john",
            last_name="doe",
            middle_name="jr."
        ),
            "John Jr. Doe")

    def test_int(self):
        with self.assertRaises(TypeError):
            formatted_name(
                first_name=1,
                last_name=2,
                middle_name=3
            )


if __name__ == "__main__":
    unittest.main()












