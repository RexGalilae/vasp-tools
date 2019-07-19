#!/usr/bin/env python
import argparse
import warnings
import numpy as np

parser = argparse.ArgumentParser(prog="split-by",
                                 description='''A script that splits a POSCAR file into its subsets
                                                based on instructions passed in a 'A B/C' format.
                                                F.ex.
                                                        "Sr Ti O/ C H"
                                                will give the program instructions to create two files-
                                                one with only Sr, Ti and O and the other with C and H
                                                from a POSCAR containing Sr, Ti, O , C and H.''',
                                epilog=        "Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('file', help="POSCAR file")
parser.add_argument('exp', help="A space separated list of atoms (passed as a string) inputted in the format shown in the description")


args = parser.parse_args()

file = args.file
exp = args.exp

'''
file = "C:\\Users\\md_za\\Desktop\\Coding\\VASP-script-packaage\\POSCAR"
exp = "Sr Ti/ O/ C H"
'''

groups = [group.split() for group in exp.split("/")]

groups

with open(file) as f:
    if(f.readline() != "POSCAR"):
        warnings.warn("File doesn't start with 'POSCAR'")
    scale = float(f.readline())
    trans = []
    for i in range(3):
        trans.append([float(n) for n in f.readline().split()])
    tl_mat = np.matrix(trans)
    atoms = f.readline().split()
    nums = [int(n) for n in f.readline().split()]
    coords = []
    type = f.readline()
    if type.split()[0] == "Selective":
        type = f.readline()
    for i in range(sum(nums)):
        coords.append([float(n) for n in f.readline().split()[0:3]])

elind = 0
for group in groups:
    fname = file
    for el in group:
        fname+=f"-{el}"
    indices = [sum(nums[0:i]) for i, num in enumerate(nums)]
    indices.append(sum(nums))
    with open(fname,'w') as f:
        rel_coords = []
        r_nums = []
        for el in group:
            r_nums.append(len(coords[indices[elind]:indices[elind+1]]))
            rel_coords+= coords[indices[elind]:indices[elind+1]]
            elind +=1
        f.write(fname+"\n")
        f.write(str(scale)+"\n")

        for i in trans:
            for j in i:
                print('\t{:<1.10f}'.format(j), file = f, end = "")
            print(file = f)
        for el in group:
            print(f"   {el:>2}", file=f, end="")
        print(file= f)

        for num in r_nums:
            print(f"   {num:>2d}", file=f, end="")

        print(file=f)

        print(type, file= f, end="")

        for coord in rel_coords:
            print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}"
                  ,file=f)
