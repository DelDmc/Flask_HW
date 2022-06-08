import random
from wonderwords import RandomWord


def random_words_generator(count):
    r = RandomWord()
    words = [r.word() for _ in range(100)]
    for _ in range(count):
        yield random.choice(words)


a = random_words_generator(5)

for i in a:
    print(i)
