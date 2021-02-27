"""
5.  Write a class called Wordplay. It should have a field that holds a list of words. The user
    of the class should pass the list of words they want to use to the class. There should be the
    following methods:
        • words_with_length(length) — returns a list of all the words of length length
        • starts_with(s) — returns a list of all the words that start with s
        • ends_with(s) — returns a list of all the words that end with s
        • palindromes() — returns a list of all the palindromes in the list
        • only(L) — returns a list of the words that contain only those letters in L
        • avoids(L) — returns a list of the words that contain none of the letters in L

"""

class Wordplay:

    def __init__(self, words: list):
        self.words = words

    def words_with_length(self, length):
        words = []
        for word in self.words:
            if (length == len(word)):
                words.append(word)
        return words

    def starts_with(self, s):
        words = []
        for word in self.words:
            if (word[0] == s):
                words.append(word)
        return words

    def ends_with(self, s):
        words = []
        for word in self.words:
            if (word[-1] == s):
                words.append(word)
        return words

    def palindromes(self):
        words = []
        for word in self.words:
            word_reverse = ""
            for i in word:
                word_reverse = i + word_reverse
            if (word_reverse == word):
                words.append(word)
        return words

    def only(self, L):
        words = []
        for word in self.words:
            if L in word:
                words.append(word)
        return words

    def avoids(self, L):
        words = []
        for word in self.words:
            if L not in word:
                words.append(word)
        return words


# l = ['hello', 'hih', 'welcome1', 'welcome2', 'tenet']
# w = Wordplay(l)
# print(w.words_with_length(8))
# print(w.starts_with('e'))
# print(w.ends_with('2'))
# print(w.palindromes())
# print(w.only('e'))
# print(w.avoids('h'))

