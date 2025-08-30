import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        value = cache_storage.get(args)
        if value is not None:
            print("Getting from cache")
            return value
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result

    return wrapper
