from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


import re

def find_shortest_longest_word(sentence):

    str_lst = re.sub(r'[(\t|\s|,|\n)]', ' ', sentence).split()

    if not str_lst:
        return (None, None)

    shortest = min(str_lst, key=len)
    longest = max(str_lst, key=len)

    return (shortest, longest)
