#!/usr/bin/python

import sys
import os.path

def count_seqs(filename):
        input_file = open(filename)
        line_count = 0
        for line in input_file:
            if line.startswith(">"):
                line_count += 1
        return(line_count)


if len(sys.argv) != 2:
        print >>sys.stderr,"usage:"
        sys.exit(1)

print os.path.basename(sys.argv[1]), count_seqs(sys.argv[1])
