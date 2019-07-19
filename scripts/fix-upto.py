#!/usr/bin/env python
from vasp.objects import POSCAR
import argparse
import sys

parser = argparse.ArgumentParser(prog = "fix-upto",
                                 description='''A script that modifies an existing/generates a new POSCAR file
                                                with atoms specified as fixed/free based on user input on the cutoff height.''',
                                 epilog="Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('file',
                    help="POSCAR file", nargs = '?')
parser.add_argument('pos',
                    help= "POSCAR taken from pipe", nargs='?',
                    type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('cutoff',
                    help="Cut-off distance below which all atoms are fixed in place",
                    type =float)
parser.add_argument('-d','--direct',
                    help="Specify if not passing cutoff distance in terms of Cartesian coordinates",
                    action = "store_true")

args = parser.parse_args()

if not sys.stdin.isatty():
    mol = POSCAR(args.pos)
elif args.file is not None:
    mol = POSCAR(args.file)
else:
    print("Please pass a POSCAR file either explicitly or through pipe")
    exit()

mol.fix_upto(args.cutoff,direct=args.direct)

mol.pipe()
