import re
import string
from collections import Counter

import numpy as np
from pandas import RangeIndex

class SpellChecker(object):

    def __init__(self, corpus_file_path):
        with open(corpus_file_path, "r") as file:
            lines = file.readlines()
            words = []
            for line in lines:
                words += re.findall(r'\w+', line.lower())

        self.vocabs = set(words)
        self.word_counts = Counter(words)
        total_words = float(sum(self.word_counts.values()))
        self.word_probas = {word: self.word_counts[word] / total_words for word in self.vocabs}

    def _level_one_edits(self, word):
        letters = string.ascii_lowercase
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [l + r[1:] for l,r in splits if r]
        swaps = [l + r[1] + r[0] + r[2:] for l, r in splits if len(r)>1]
        replaces = [l + c + r[1:] for l, r in splits if r for c in letters]
        inserts = [l + c + r for l, r in splits for c in letters] 

        return set(deletes + swaps + replaces + inserts)

    def _level_two_edits(self, word):
        return set(e2 for e1 in self._level_one_edits(word) for e2 in self._level_one_edits(e1))

    def checkWord(self, word):
        candidates = self._level_one_edits(word) or self._level_two_edits(word) or [word]
        valid_candidates = [w for w in candidates if w in self.vocabs]
        return sorted([(c, self.word_probas[c]) for c in valid_candidates], key=lambda tup: tup[1], reverse=True)
    def checkPas(self,pas):
        file = open(pas,'r')
        words =[]
        wrong_words = []
        fix_words = []
        pasFix = ""
        pasUnfix = ""
        for line in file:
            words += re.findall(r'\w+', line.lower())
            pasUnfix += line +"\n"
            for word in words:
                if word not in self.vocabs:
                    wrong_words.append(word)
                    suggestions = self._level_one_edits(word) or self._level_two_edits(word) or [word]
                    valid_suggestions = [w for w in suggestions if w in self.vocabs]
                    predict =  sorted([(c, self.word_probas[c]) for c in valid_suggestions], key=lambda tup: tup[1], reverse=True)
                    probs = np.array([c[1] for c in predict])
                    best_ix = np.argmax(probs)
                    word = predict[best_ix][0]
                    pasFix += word +" "
                    fix_words.append(word)
                    continue
                pasFix+= word +" "
        file.close()
        print("File before correct",end="\n\n")
        print(pasUnfix)
        print("File after corrected",end="\n\n")
        print(pasFix)
        print("The list of wrong words")
        print(wrong_words,fix_words,sep = "->")
        return


checker = SpellChecker("engDic.txt")
print(checker.checkWord("hellp"))
checker.checkPas("pasEN.txt")