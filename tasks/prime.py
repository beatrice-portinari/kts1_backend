__all__ = (
    'is_prime',
)

def is_prime(num):
    if num == 4 or num == 0 or num == 1: return False

    for i in range(2, int(num / 2)):
        if (num % i) == 0:
            return False
    return True

