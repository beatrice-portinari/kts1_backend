__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds):
    time_parameters = {
        "d": 3600 * 24,
        "h": 60 * 60,
        "m": 60,
    }
    result = ""
    for key in time_parameters.keys():
        if num := (seconds // time_parameters[key]):
            result += f"{num:0>2}{key}"
        elif result:
            result += f"00{key}"
        seconds -= num * time_parameters[key]
    result += f"{seconds:0>2}s"
    return result




