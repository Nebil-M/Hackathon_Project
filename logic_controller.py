

class Model:
    def __init__(self):
        self.word_freq = {"rando": 1, "banana": 1, "apple": 1, "fruit": 1}


    def add_freq(self, word):
        if word in self.word_freq.keys():
            self.word_freq[word] += 1
        else:
            self.word_freq.update({word: 1})

    def get_freq_range(self):
        pass

    def get_definition(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

if __name__ == '__main__':
    m = Model()
    print(m.word_freq)
    m.add_freq('non')
    m.add_freq('non')
    print(m.word_freq)












