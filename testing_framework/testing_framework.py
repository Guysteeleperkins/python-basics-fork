def assert_equals(value_1, value_2) -> bool:
    return value_1 == value_2


def assert_true(value) -> bool:
    return bool(value)


def assert_greater_than(value_1: int, value_2: int) -> bool:
    if not isinstance(value_1, int) or not isinstance(value_2, int):
        raise TypeError(
            "At least one of the values supplied is not an integer"
        )
    return value_1 > value_2


print(assert_equals(2, 2))
print(assert_equals(True, False))
print(assert_equals('', False))
print(assert_equals(bool(''), False))
