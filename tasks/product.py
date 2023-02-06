from typing import Any

__all__ = (
    'cartesian_product',
)


import itertools

def cartesian_product(lst1, lst2):
    result = []
    for item in itertools.product(*[lst1, lst2]):
        result.append(item)
    return result
