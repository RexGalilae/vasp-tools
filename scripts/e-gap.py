#!/usr/bin/env python
import argparse
import os
import re
import subprocess


parser = argparse.ArgumentParser(prog="e-gap",
                                 description='''A script that prints out a list of Energy-gap values from a given
                                                OUTCAR file for each k-point present in it.

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
    f.seek(f.tell()+f.read().find(' k-point     1 '), os.SEEK_SET)
    # Loop over all k-points
    kinfo = []
    kline = f.readline().replace("\n","")
    eli = []
    eui = []
    while kline.split()[0] == "k-point":
        f.readline()
        # Loop within a k-point
        table = []
        while True:
            te = f.readline().split()
            if len(te) == 3:
                table.append([float(x) for x in te])
                continue
            break
        diffs = [abs(table[i+1][2] - table[i][2]) for i,e in enumerate(table[:-2])]
        md_index = diffs.index(max(diffs))
        e1 = table[md_index][1]
        e2 = table[md_index+1][1]

        eli += [e1]
        eui += [e2]

        kinfo.append(f"{kline} | Energy Gap: {abs(e1-e2):.4f} eV")
        kline = f.readline().replace("\n", "")
        if len(kline.split()) < 6:
            break

for k in kinfo:
    print(k, end="\n--------------------------------------------------------------------------\n")

print(f"Overall Energy Gap : {min(eui)-max(eli):.4f} eV")
