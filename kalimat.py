class Kalimat:
    def __init__(self, sentence):
        self.sentence = sentence

    def getSentence(self):
        text = self.removeWords()
        return text

    def removeWords(self):
        finalText = ''
        excludedChars = [',', '.', '!', '?']
        excludedWords = ['2beer', 'mksfess', '[askmf]']
        words = [i for j in self.sentence.split() for i in (j, ' ')][:-1]

        for i, word in enumerate(words):
            if word[0] == '@':  # remove the username
                word = word.replace(word, '')
            if word[0:4] == 'http':  # remove link
                word = word.replace(word, '')

            for ew in excludedWords:  # remove unnecassary words
                word = word.replace(ew, '')
            for i, char in enumerate(word):
                for ec in excludedChars:  # remove unnecessary char
                    char = char.replace(ec, '')
                char = char.lower()
                finalText += char
        self.sentence = finalText
        return self.sentence

    def transform(self):
        finalText = ''
        text = self.removeWords()
        for i, char in enumerate(text):
            if i % 2 != 0:
                char = char.replace(char, char.upper())
                finalText += char
            else:
                finalText += char
        self.sentence = finalText
        return self.sentence

    def trinsfirm(self):
        finalText = ''
        text = self.removeWords()
        consonant = ['a', 'u', 'e', 'o']
        for char in text:
            if char in consonant:
                char = char.replace(char, 'i')
                finalText += char
            else:
                finalText += char
        self.sentence = finalText
        return self.sentence

# Testing purpose
# k = Kalimat("heh gaboleh gitu tapi bener, juga sih haha norak")
# k.trinsfirm()
# print(k.sentence)
