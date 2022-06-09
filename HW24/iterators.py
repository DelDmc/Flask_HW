import random
import string
import unittest
from unittest import TestCase


def convert_int_to_uid(var):
    first_part = random.randint(10, 99)
    second_part = random.randint(10, 99)
    third_part = random.sample(string.ascii_letters, 3)
    var = str(first_part)[:2] + "".join(third_part) + str(second_part)[:2]
    return var


def title_function(my_word):
    return my_word.title()


class map_dict_iter:
    def __init__(self, func1, func2, my_dict):
        self.func1 = func1
        self.func2 = func2
        self.my_dict = my_dict
        self.key_count = 0
        self.value_count = 0

    def get_key(self):
        return self.func1(list(self.my_dict.keys())[self.key_count])

    def get_value(self):
        return self.func2(list(self.my_dict.values())[self.value_count])

    def __iter__(self):
        return self

    def __next__(self):
        if self.key_count == len(self.my_dict):
            raise StopIteration
        else:
            my_dict = {self.get_key(): self.get_value()}
            self.key_count += 1
            self.value_count += 1
            return my_dict


class MapDictIterTest(TestCase):
    def setUp(self):
        self.test_dict = {
            "1": "james",
            "2": "jordan",
            "3": "clarcsson",
            "4": "michaels",
        }
        self.test_map_dict = map_dict_iter(convert_int_to_uid, title_function, self.test_dict)
        self.test_range = len(self.test_dict)
        self.additional_keys = [convert_int_to_uid(x) for x in range(1, 10**4)]

    def tearDown(self) -> None:
        pass

    def test_stop_iteration(self):
        for i in range(self.test_range):
            next(self.test_map_dict)
        with self.assertRaises(StopIteration):
            next(self.test_map_dict)

    def test_title(self):
        return self.assertEqual(*list(next(self.test_map_dict).values()), "James")

    def test_unique_keys(self):
        name = "john"
        test_empty_dict = {}
        big_dict = dict.fromkeys(self.additional_keys, name)
        big_iter = map_dict_iter(convert_int_to_uid, title_function, big_dict)
        for i in big_iter:
            test_empty_dict.update(i)

        return self.assertEqual(len(test_empty_dict), len(big_dict))


if __name__ == '__main__':
    unittest.main()
