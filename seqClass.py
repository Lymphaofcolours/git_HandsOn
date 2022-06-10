#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):           # This searches for the strutcure of the query line
    if re.search('T', args.seq):
        print ('The sequence is DNA')              # Specifies if it is DNA
    elif re.search('U', args.seq):
        print ('The sequence is RNA')              # Specifies if it is RNA
    else:
        print ('The sequence can be DNA or RNA')   # Specifies if it may be both
else:
    print ('The sequence is not, neither can be, nor will be, DNA nor RNA')  # Specifies if it cannot be any of both

if args.motif:
    args.motif = args.motif.upper()                                          # Changes query to uppercase
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')   # Prints results
    if re.search(args.motif, args.seq):        
        print("FOUND")                  # Prints found if found
    else:
        print("NOT FOUND")            # Prints not found if not found

=======
        print("FOUND")
    else:
        print("NOT FOUND, BUT HE TRIED")
>>>>>>> motif
