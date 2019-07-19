#!/usr/bin/env python
from vasp.objects import POSCAR
import argparse
import numpy as np
import pathlib
import copy
import sys

parser = argparse.ArgumentParser(prog="place-at",
                                 description='''A script that places an adsorbing molecule on a user-specified position
                                                relative to the adsorbate surface. The x & y coordinates are specified
                                                using Direct coordinates''',
                                 epilog="Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('POS',
                    help="POSCAR files. First filename is always assumed to belong to the crystal.\
                                 Adsorbate POSCAR can be passed through Linux pipe\n", nargs='*')
parser.add_argument('pos',
                    help= "Adsorbate POSCAR taken from pipe", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('xyz',
                    nargs=3, help="Coordinates for the Placement of the Adsorbate\
                                   Molecule on the Surface. x & y are passed in Direct coordinates\
                                   and z is passed relative to the surface in angstroms\n",
                    type=float)
parser.add_argument('-x','--center',
                    help="Optional argument that allows you to specify the reference atom in the adsorbate\n", default=None)
args = parser.parse_args()

# print(vars(args))

if not sys.stdin.isatty():
    ads = POSCAR(args.pos)
elif len(args.POS) == 2:
    ads = POSCAR(args.POS[1])
else:
    print("It seems you didn't specify the adsorbate POSCAR file. Either pass it as a second argument or by using pipe.")
    exit()

crystal = POSCAR(args.POS[0])

# For Debugging
# ######################################################
# xyz = [0.5,0.5,2.0]
# save = "POSCAR-Merged"
# crystal = POSCAR("VASP/POSCAR-Sr-Ti-O")
# ads = POSCAR("VASP/POSCAR-C-H")
# shit = POSCAR("VASP/POSCAR")
# shit.__dict__
# crystal.__dict__
# ads.__dict__
# ######################################################

# Instantiate a new POSCAR object based on the Adsorbate POSCAR
sim = copy.deepcopy(crystal)

sim.name = f"{crystal.name.split('/')[-1]} + {ads.name.split('/')[-1]}"
sim.atoms.extend(ads.atoms)
sim.nums.extend(ads.nums)

# If no focal point is specified, take the centroid as the focal point
if args.center is None:
    fp = [np.mean([coord[i] for coord in ads.coords]) for i in range(3)]
else:
    symbol = args.center.rstrip('0123456789')
    fp = ads.locate(symbol, args.center.replace(symbol, ""))

# Set focal point as origin and translate it along the user specified coordinates
temp_coords = []
for cunt in ads.coords:
    temp_coords.append([x-f for x, f in zip(cunt,fp)])

# Set coordinates for the focal point
cent_coords = list(np.matmul(crystal.trans, args.xyz))[:2]
## Get height of surface
zs = [coord[2] for coord in crystal.coords]

## Set up an initial guess for z for the surface atom cloest to the adsorption point
z_surface = max([z for z in zs if z <= 0.95*crystal.trans[2][2]])

## Compute distances to all atoms from a point <xyz[2]> angstroms above the initial guess
dist = [np.linalg.norm(np.array(coord) - np.array(cent_coords+[z_surface+args.xyz[2]])) for coord in crystal.coords]
# print(f"Initial guess :{z_surface} <+> {z_surface/crystal.trans[2][2]}")

## The z-value of the surface atom closest to the adsorption point is found
z_surface = crystal.coords[dist.index(min(dist))][2]
# print(f"Final :{z_surface} <+> {z_surface/crystal.trans[2][2]}")
cent_coords.append(z_surface+args.xyz[2])

# Position the molecule at the specified position wrt the focal point
pos = []

# Position all the atoms around this central point and append coords to combined POSCAR
for coord in temp_coords:
    pos.append([float(f"{x+c:>12.9f}") for x, c in zip(coord, cent_coords)])
sim.coords.extend(pos)

sim.pipe()
