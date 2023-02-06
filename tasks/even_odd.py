__all__ = (
    'even_odd',
)


def even_odd(lst):
    even = [i for i in lst if i % 2 == 0]
    odd = list(set(lst) - set(even))
    try:
        result = round(sum(even) / sum(odd), 5)
    except ZeroDivisionError:
        return 0
    return result
