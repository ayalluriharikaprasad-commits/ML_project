from typeguard import typechecked


@typechecked
def get_number(x: int, y: int) -> int:
    return x * y


print(get_number(x=2, y='3'))
