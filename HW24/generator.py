import random
from wonderwords import RandomWord


def random_words_generator(count):
    r = RandomWord()
    for _ in range(count):
        yield r.word()


a = random_words_generator(5)

for i in a:
    print(i)
