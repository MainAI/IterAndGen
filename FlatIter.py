class FlatIterator:
    def __init__(self, list_nest):
        self.flat_list = []
        self.list_nest = list_nest

    def __iter__(self):
        self.cursor = -1
        self.flat_list = []
        self.list_merge(self.list_nest)
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.flat_list):
            raise StopIteration
        return self.flat_list[self.cursor]

    def list_merge(self, lst1):
        self.flat_list = []
        for item in lst1:
            if isinstance(item, list):
                self.flat_list += self.list_merge(item)
            else:
                self.flat_list += [item]
        return self.flat_list

