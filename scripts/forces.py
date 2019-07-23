#!/usr/bin/env python
import argparse
import os
import re
import subprocess
from tabulate import tabulate

parser = argparse.ArgumentParser(prog="forces",
                                 description='''A script that parses an OUTCAR file to compute a the net positive
                                                and negative Forces acting on every atom along x, y and z.

                                                WARNING: Script assumes that the corresponding OSZICAR file is also
                                                present in the same directory.''',
                                 epilog="Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")
parser.add_argument('file', help="OUTCAR file")

args = parser.parse_args()

OUT = args.file
OSZ = re.sub(r"OUTCAR",'OSZICAR',OUT)
try:
    line = subprocess.check_output(['tail', '-1', OSZ])
    if len(line.split()) <= 1:
        line = subprocess.check_output(['tail', '-2', OSZ])

    f_iter = int(line.split()[0])
except Exception as e:
    print(e,"\nInfoMissing Error: OSZICAR and OUTCAR files are either missing or incomplete. "+
          "This might be because the simulation was interrupted.")
    exit()

with open(OUT) as f:
    # Seek to last Iteration
    f.seek(f.read().find(f"----------------------------------------- Iteration{f_iter:>5}"))
    # Seek to "spin component 1"
    f.seek(f.tell()+f.read().find('POSITION'), os.SEEK_SET)
    # Skip two lines and cut to the chase
    f.readline()
    f.readline()

    fx =[]
    fy =[]
    fz =[]

    while True:
        try:
            line = [float(num) for num in f.readline().split()]
            if len(line) == 6:
                fx.append(line[3])
                fy.append(line[4])
                fz.append(line[5])
            else:
                break
        except:
            break
    # print(fx,fy,fz)

#####################
# For Debugging
# fx = [-1,2,-3,4]
# fy = [-1,2,-3,4]
# fz = [-1,2,-3,4]
#####################

# Compute net positive and negative forces for x, y and z separately
pos_fx=sum([f for f in fx if f > 0])
neg_fx=sum([f for f in fx if f < 0])

pos_fy=sum([f for f in fy if f > 0])
neg_fy=sum([f for f in fy if f < 0])

pos_fz=sum([f for f in fz if f > 0])
neg_fz=sum([f for f in fz if f < 0])

print(tabulate([
                ['Fx', pos_fx, neg_fx],
                ['Fy', pos_fy, neg_fy],
                ['Fz', pos_fz, neg_fz]
               ], headers=['Positive', 'Negative'], tablefmt="fancy_grid"))
