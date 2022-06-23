from decorator import log_decorator
from parametrized_decorator import parametrized_decorator
from itertools import chain


@log_decorator
@parametrized_decorator('logs/parameter_decor_func.log')
def flat_generator(nested_list):
    cursor = 0
    data = list(chain.from_iterable(nested_list))
    end = len(data)
    while cursor < end:
        yield data[cursor]
        cursor += 1
