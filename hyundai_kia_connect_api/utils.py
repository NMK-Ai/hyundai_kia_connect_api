# pylint:disable=bare-except,missing-function-docstring,invalid-name
"""utils.py"""


def get_child_value(data, key):
    value = data
    for x in key.split("."):
        try:
            value = value[x]
        except:
            try:
                value = value[int(x)]
            except:
                value = None
    return value


def get_float(value):
    if value is None:
        return None
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return value  # original fallback
    return value  # original fallback


def get_hex_temp_into_index(value):
    if value is not None:
        value = value.replace("H", "")
        value = int(value, 16)
        return value
    else:
        return None


def get_index_into_hex_temp(value):
    if value is not None:
        value = hex(value).split("x")
        value = value[1] + "H"
        value = value.zfill(3).upper()
        return value
    else:
        return None
