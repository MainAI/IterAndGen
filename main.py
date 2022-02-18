from FlatIter import FlatIterator


def flat_generator(nest_list):
    for items in nest_list:
        if isinstance(items, list):
            for el in flat_generator(items):
                yield el
        else:
            yield items


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', ['c', 'k']],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
