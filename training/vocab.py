"""
Constructing and loading dictionaries
"""
import pickle as pkl
import numpy
from collections import OrderedDict

def build_dictionary(text):
    """
    Build a dictionary
    text: list of sentences (pre-tokenized)
    """
    wordcount = {}
    for cc in text:
        words = cc.split()
        for w in words:
            if w not in wordcount:
                wordcount[w] = 0
            wordcount[w] += 1
    words = list(wordcount.keys())
    freqs = list(wordcount.values())
    sorted_idx = numpy.argsort(freqs)[::-1]

    worddict = OrderedDict()
    for i, idx in enumerate(sorted_idx):
        worddict[words[idx]] = i+2 # 0: <eos>, 1: <unk>

    return worddict, wordcount

def load_dictionary(loc='/ais/gobi3/u/rkiros/bookgen/book_dictionary_large.pkl'):
    """
    Load a dictionary
    """
    with open(loc, 'rb') as f:
        worddict = pkl.load(f)
    return worddict

def save_dictionary(worddict, wordcount, loc):
    """
    Save a dictionary to the specified location 
    """
    with open(loc, 'wb') as f:
        pkl.dump(worddict, f)
        pkl.dump(wordcount, f)


def cutSentences(lsentences):
    toAdd = []
    for i, fsent in enumerate(lsentences):
        if fsent = '':
            lsentences.pop(i)
        if '. ' in fsent:
            toAdd.extend(fsent.split('. '))
            lsentences.pop(i)
    lsentences.extend(toAdd)

if __name__ == "__main__":
    pass


