from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)


KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(data):
    return {value: key for key, value in data.items()}

def flip_kv_vk_safe(data):
    result = {}
    for key, value in data.items():
        result.setdefault(value, []).append(key)
    return result
