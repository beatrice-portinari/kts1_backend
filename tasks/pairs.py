from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(i, items):
    res = []
    for n, x in enumerate(i):
        try:
            res.append((x, items[n]))
        except IndexError:
            break
    return res
