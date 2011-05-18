#!/usr/bin/env python

import utils, sys

def wordcount(string):
    freqs = {}
    for w in string.split():
        w = w.lower()
        if freqs.get(w):
            freqs[w] += 1
        else:
            freqs[w] = 1
    return freqs

for f in sys.argv[1:]:
    t = utils.benchmark(lambda: utils.with_utf8_file(f, wordcount))
    print('{0}: {1}'.format(f, t))
