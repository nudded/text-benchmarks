#!/usr/bin/env python

import utils, sys

def sort(string):
    lines = string.split('\n')
    lines.sort()
    return '\n'.join(lines)

for f in sys.argv[1:]:
    t = utils.benchmark(lambda:
            utils.with_utf8_file(f, lambda c:
                    sys.stdout.write(sort(c).encode('utf-8'))))
    sys.stderr.write('{0}: {1}\n'.format(f, t))
