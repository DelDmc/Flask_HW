import functools
from collections import OrderedDict

import psutil
import requests

value = 0
counter = 1


def profile(msg="Memory used= "):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            p = psutil.Process()
            start = p.memory_info().rss
            deco._num_call += 1
            result = f(*args, **kwargs)
            deco._num_call -= 1
            stop = p.memory_info().rss
            if deco._num_call == 0:
                print(msg, f'{f.__name__}: {stop - start}')
            return result

        deco._num_call = 0
        return deco

    return internal


def cache(max_limit=3):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key][counter] += 1
                return deco._cache[cache_key][value]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                key_to_delete = min(deco._cache,
                                    key=lambda dict_key: deco._cache[dict_key][counter])
                del deco._cache[key_to_delete]
            deco._cache[cache_key] = [result, 1]
            return result
        deco._cache = OrderedDict()
        return deco
    return internal


@profile()
@cache(max_limit=3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://youtube.com')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://ain.ua')
fetch_url('https://youtube.com')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
