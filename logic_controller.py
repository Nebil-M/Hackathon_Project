import requests
import json


class Model:
    def __init__(self):
        self.word_freq = {}
        self.load()
        self.txt = ''

    def add_freq(self, word):
        if word in self.word_freq.keys():
            self.word_freq[word] += 1
        else:
            self.word_freq.update({word: 1})

    def get_freq_range(self, minimum, maximum):
        word_list = [word for word in self.word_freq.keys() if minimum <= self.word_freq[word] <= maximum]

        with open('export.txt', 'w') as f:
            for word in word_list:
                f.write(word)
                f.write(' | ')
                line_def = self.get_definition(word).replace('\n', '')
                f.write(line_def)
                f.write('\n')

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
        with open("word_freq.json", "w") as outfile:
            json.dump(self.word_freq, outfile)

    def load(self):
        with open('word_freq.json') as user_file:
            json_object = json.load(user_file)
        self.word_freq = json_object

    def get_text(self, file_dir):
        with open(file_dir, 'r', encoding="utf-8") as file:
            text = file.read()
        self.txt = text
        return text


model = Model()

model.get_freq_range(1, 5)
if __name__ == '__main__':
    m = Model()
    print(m.word_freq)
    print(type((m.word_freq)))
    #print(m.get_definition('hell'))
