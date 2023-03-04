dictionary = {"rando": 1, "banana": 1, "apple": 1, "fruit": 1}


def Frequency(word):
    if word in dictionary.keys():
        dictionary[word] += 1
    else:
        dictionary.update({word: 1})
print(dictionary)
Frequency('banana')
print(dictionary)












