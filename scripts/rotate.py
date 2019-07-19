#!/usr/bin/env python
from vasp.objects import POSCAR
import argparse
import numpy as np
import sys
from vector_algebra import *

parser = argparse.ArgumentParser(prog="rotate",
                                 description='''A script that rotates a molecule in a POSCAR file along a user-specified axis
                                                and by a user-specified angle (in degrees).''',
                                 epilog="Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('file',
                    help="POSCAR filename", nargs='?')
parser.add_argument('pos',
                    help= "POSCAR taken from pipe", nargs='?',
                    type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-x',
                    help="Rotates about the x-axis", default=None, type=float)
parser.add_argument('-y',
                    help="Rotates about the y-axis", default=None, type=float)
parser.add_argument('-z',
                    help="Rotates about the z-axis", default=None, type=float)
parser.add_argument('-c','--center',
                    help="Optional argument that allows you to specify the center of rotation\n", default=None)

args = parser.parse_args()

# print(vars(args))

if not sys.stdin.isatty():
    mol = POSCAR(args.pos)
elif args.file is not None:
    mol = POSCAR(args.file)
else:
    print("Please pass a POSCAR file corresponding to the molecule you wish to rotate")
    exit()

# If no focal point is specified, take the centroid as the focal point
if args.center is None:
    fp = [np.mean([coord[i] for coord in mol.coords]) for i in range(3)]
else:
    symbol = args.center.rstrip('0123456789')
    fp = mol.locate(symbol, args.center.replace(symbol, ""))

centered_vects = mol.recentered(fp)

## Perform rotation transforms on acquired vects

if args.x is not None:
    for i, centered in enumerate(centered_vects):
        centered_vects[i] = centered.rotate(radians(args.x), axis = "x")
if args.y is not None:
    for i, centered in enumerate(centered_vects):
        centered_vects[i] = centered.rotate(radians(args.y), axis = "y")
if args.z is not None:
    for i, centered in enumerate(centered_vects):
        centered_vects[i] = centered.rotate(radians(args.z), axis = "z")

# Change mol coords to rotated form
## Restore the postion of the molecule in the crystal (eliminate displacement)
fp = vector(*fp)
rotated_vects = [cv+fp for cv in centered_vects]

## Change coords of POSCAR to the rotated vects
for i, rv in enumerate(rotated_vects):
    mol.coords[i] = rv.to_list()

mol.pipe()
