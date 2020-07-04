class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        if index < len(self.dictionary):
            self.index += 1
            return self.keys[index], self.dictionary[self.keys[index]]
        else:
            raise StopIteration


result = dictionary_iter({1: "3", 2: "4"})
for x in result:
    print(x)