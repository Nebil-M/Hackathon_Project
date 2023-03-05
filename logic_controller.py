import requests
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

    def get_definition(self, word):
        s = ''
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        dict = response.json()
        try:
            definitions = dict[0]['meanings']
        except:
            return "Sorry pals no definitions here."
        else:
            for part_of_speech in definitions:
                s += part_of_speech['partOfSpeech']
                s += '\n---\n'
                defs = '\n'.join([defs['definition'] for defs in part_of_speech['definitions']])
                s += defs
                s += '\n------------------------------------------\n'
            return s

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
    m.load()
    print(m.get_definition('hell'))













