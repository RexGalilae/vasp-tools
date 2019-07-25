import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set()
parser = argparse.ArgumentParser(prog = "e-plot",
                                 description='''A script that plots the E-curve over multiple
                                                iterations using data taken from a given OSZICAR
                                                file.''',
                                epilog= "Created by Zaid Hassan. Feel free to contact me @WS-2016 for any errors.")

parser.add_argument('file', help="OSZICAR file")
parser.add_argument('-d', '--diff',
                    help="Plots dE instead of E",
                    action= "store_true")
parser.add_argument('-s', '--save',
                    help="Store the result as an image file. Specifying name is optional. Else, load image on screen.",
                    nargs='?', default = None, const= ".unnamed")
args = parser.parse_args()

file = args.file

if args.save == ".unnamed":
    save = os.path.dirname(cwd.replace('\\','/').split('/')[-1]+"-dos-plot"
    print("Saving at {}".format(cwd)
else:
    save = args.save
with open(file) as f:
    ys = []
    Des = []
    for line in f:
        if line.split()[0] == 'N' or line.split()[0] == 'DAV:':
            continue
        elif line.split()[1] == 'F=':
            if args.diff ==  False:
                ys.append(float(line.split()[2]))
            else:
                ys.append(float(line.split()[7].replace("=", "")))

plt.title("Energy Convergence")

plt.xlabel("Iteration")


if args.diff:
    plt.ylabel("dE")
    plt.plot(ys[1:], 'r', linewidth=4)
else:
    plt.ylabel("Free Energy")
    plt.plot(ys, 'b', linewidth=4)

if args.save is None:
    plt.show()
else:
    plt.savefig(save)
