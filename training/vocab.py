"""
Constructing and loading dictionaries
"""
import pickle as pkl
import numpy
from collections import OrderedDict
import argparse
import time

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


def readFile(filename):
    sentences = []
    with open(filename) as f:
        for line in f:
            if line == '':
                continue
            
            if '.' in line:
                sentences.extend(line.split('.'))
            else:
                sentences.append(line)
    return sentences


def cutSentences(lsentences):
    toAdd = []
    for i, fsent in enumerate(lsentences):
        if fsent == '':
            lsentences.pop(i)
        if '. ' in fsent:
            toAdd.extend(fsent.split('. '))
            lsentences.pop(i)
    lsentences.extend(toAdd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--sentences_file', help="File containing sentences",
                        default="/data/wiki+leboncoin_pre.txt")
    parser.add_argument('-d','--dictionary_name', help="Path to save dictionary",
                        default='dictionary.pkl')
    args = parser.parse_args()
    
    print('Loading sentences file')
    t0 = time.time()
    sentences = readFile(args.sentences_file)
    print('File read in', time.time() - t0, ' sec')

    print("Creating dictionary")
    dic, count = build_dictionary(sentences)
    print("Saving dictionary")
    save_dictionary(dic, count, args.dictionary_name)




























