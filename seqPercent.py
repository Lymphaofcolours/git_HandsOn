#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line

nuc = list(args.seq)

values, counts = np.unique(nuc, return_counts = True)

print(values)

totalitems = len(args.seq)

print("Percentage per Nucleotide:")

for index,item in enumerate(values):
	print(item + " : " +  str(round((counts[index]/totalitems)*100, 1)) + "%")
