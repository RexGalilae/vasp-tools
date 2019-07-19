import argparse
from vasp.objects import POSCAR
import sys

parser = argparse.ArgumentParser(prog = "cart-direct",
                                 description='''Converts a POSCAR file from Cartesian to Direct coordinates and vice versa.

                                                WARNING: Due to truncation during the write-file process, the
                                                conversion isn't 100% lossless. Minor distortions may occur as
                                                a result. Avoid performing repeated conversions of the same file.''',
                                epilog=        "Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('file', help="POSCAR file", nargs='?')
parser.add_argument('pos',
                    help= "POSCAR taken from pipe", nargs='?',
                    type=argparse.FileType('r'), default=sys.stdin)

args = parser.parse_args()

if not sys.stdin.isatty():
    mol = POSCAR(args.pos)
elif args.file is not None:
    mol = POSCAR(args.file)
else:
    print("Please pass a POSCAR file corresponding to the molecule you wish to rotate")

if mol.type.lower() == "direct":
    mol.to_cart().pipe()
else:
    mol.to_direct().pipe()
