#!/usr/bin/python3
import random as rand
import sys

NUM_DOCS=1000
VOCAB_SIZE = 3000
NUM_TOPICS=10
LABELED_RATIO=0.5
MIN_WORDS=5
MAX_WORDS=10
MIN_LABELS=1
MAX_LABELS=4
WORDLIST_PATH='/usr/share/dict/cracklib-small'

def main():
    # load word list
    with open(WORDLIST_PATH, 'r') as wordlist_f:
        wordlist = [w.strip() for w in
                rand.sample(wordlist_f.readlines(),VOCAB_SIZE)]
    labeled_pool = int(NUM_DOCS * LABELED_RATIO)
    unlabeled_pool = NUM_DOCS - labeled_pool
    for count in range(NUM_DOCS):
        # sample label presence
        label_score = rand.randint(0,NUM_DOCS-count-1)
        labeled = True if label_score > unlabeled_pool else False
        if labeled:
            labeled_pool -= 1
            numlabels = rand.randint(MIN_LABELS, MAX_LABELS)
            labels = [str(l) for l in rand.sample(range(1, NUM_TOPICS+1),
                numlabels)]
            print("[%s]" % " ".join(labels), end="")
        else:
            unlabeled_pool -= 1
        numwords = rand.randint(MIN_WORDS, MAX_WORDS)
        words = rand.sample(wordlist, numwords)
        print(" %s" % " ".join(words))

if __name__ == "__main__":
    main()
