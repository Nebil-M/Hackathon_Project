import json

class Model:
    def __init__(self):
        self.word_freq = {}


    def add_freq(self, word):
        if word in self.word_freq.keys():
            self.word_freq[word] += 1
        else:
            self.word_freq.update({word: 1})

    def get_freq_range(self, minimum, maximum):
        word_list = [word for word in self.word_freq.keys() if minimum <= self.word_freq[word] <= maximum]
        return word_list


    def get_definition(self):
        pass

    def save(self):
        y = json.dumps(self.word_freq)
        with open("word_freq.json", "w") as outfile:
            json.dump(y, outfile)

    def load(self):
        with open('word_freq.json') as user_file:
            file_contents = user_file.read()


        self.word_freq = json.loads(file_contents)


if __name__ == '__main__':
    m = Model()
    #print(m.word_freq)
    #m.add_freq('non')
    #m.add_freq('non')
    m.load()
    print(m.word_freq)
    #print(m.get_freq_range(1, 5))
    #m.save()












