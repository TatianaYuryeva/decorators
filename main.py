from generators import flat_generator

NESTED_LIST = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

if __name__ == '__main__':

    for item in flat_generator(NESTED_LIST):
        print(item)
