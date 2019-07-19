import numpy as np
from numpy.linalg import inv
import sys
import copy
from vector_algebra import *

class POSCAR(object):
    """An object that encapsulates all the information contained within
       a POSCAR file."""
    def __init__(self, file, **kwargs):
        """Initializes POSCAR object by reading POSCAR data from a specified
           file.

        Parameters
        ----------
        file : str/FileType
            Path to POSCAR file/File object.
        **kwargs : dict
            Stores any additional keyword arguments and overrides read data.

        Returns
        -------
        POSCAR-type object
            An encapsulation of a POSCAR file in Python.

        """
        if isinstance(file, str):
            f =  open(file)
        else:
            f = file
        self.name = f.readline().replace("\n", "")
        ## Start reading the file in the tried POSCAR format
        self.scale = float(f.readline())
        self.trans = []
        for i in range(3):
            self.trans.append([float(n) for n in f.readline().split()])
        self.atoms = f.readline().split()
        self.nums = [int(n) for n in f.readline().split()]
        self.coords = []
        self.selective = False
        self.fix = None
        self.type = f.readline().split()[0]
        # Skip "Selective dynamics" if it's already a fixed file
        if self.type == "Selective":
            self.selective = True
            self.fix = []
            self.type = f.readline().split()[0]
        for i in range(sum(self.nums)):
            line = f.readline().split()
            if self.selective == False:
                self.coords.append([float(n) for n in line])
            else:
                self.coords.append([float(n) for n in line[0:3]])
                if len(line) == 6:
                    self.fix.append([truth == "T" for truth in line[3:]])
                else:
                    self.fix.append([True, True, True])
        f.close()
        # Get additional kwargs and store them
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def locate(self, element, index):
        """Prints the location of a specified atom in the POSCAR file.

        Parameters
        ----------
        element : str
            The Atomic Symbol of the element.
        index : int
            Index of the atom based on its location in the POSCAR file.

        Returns
        -------
        list
            Location of the atom in the crystal in xyz-form.

        """
        try:
            start = sum(self.nums[:self.atoms.index(element)])
        except:
            print("Specified atom not found in POSCAR.")
            return None
        return self.coords[start+int(index)-1]

    def write(self, file):
        """Writes POSCAR object to file in POSCAR format.

        Parameters
        ----------
        file : str
            Name of the new POSCAR file.
        """
        with open(file,'w+') as f:
            f.write(self.name+"\n")
            f.write(str(self.scale)+"\n")

            for i in self.trans:
                for j in i:
                    print('\t{:<1.10f}'.format(j), file = f, end = "")
                print(file = f)
            for atom in self.atoms:
                print("   {:>2}".format(atom), file=f, end="")

            print(file= f)

            for num in self.nums:
                print("   {:>2d}".format(num), file=f, end="")

            print(file=f)
            if self.selective:
                print("Selective dynamics", file = f)
            print(self.type, file= f)
            if self.selective:
                fix = [['T' if truth else 'F' for truth in line] for line in self.fix]
                for i, coord in enumerate(self.coords):
                    print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}    {'  '.join(map(str,fix[i]))}", file=f)
            else:
                for coord in self.coords:
                    print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}", file=f)

    def pipe(self):
        """Prints POSCAR file to stdout for piping.

        Parameters
        ----------
        file : str
            Name of the new POSCAR file.
        """
        print(self.name)
        print(str(self.scale))

        for i in self.trans:
            for j in i:
                print('\t{:<1.10f}'.format(j), end = "")
            print()
        for atom in self.atoms:
            print("   {:>2}".format(atom), end="")

        print()

        for num in self.nums:
            print("   {:>2d}".format(num), end="")

        print()
        if self.selective:
            print("Selective dynamics")
        print(self.type)
        if self.selective:
            fix = [['T' if truth else 'F' for truth in line] for line in self.fix]
            for i, coord in enumerate(self.coords):
                print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}    {'  '.join(map(str,fix[i]))}")
        else:
            for coord in self.coords:
                print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}")

    def to_direct(self):
        """Converts POSCARs coordinate system to Direct.

        Returns
        -------
        self
            An object that encapsulates all the information contained within
            a POSCAR file.

        """
        if self.type.lower() == "direct":
            return self
        else:
            self.coords = [list(np.matmul(inv(self.trans), coord)) for coord in self.coords]
            self.type = "Direct"
            return self
    def to_cart(self):
        """Converts POSCARs coordinate system to Cartesian.

        Returns
        -------
        self
            An object that encapsulates all the information contained within
            a POSCAR file.

        """
        if self.type.lower() == "cartesian":
            return self
        else:
            self.coords = [list(np.matmul(self.trans, coord)) for coord in self.coords]
            self.type = "Cartesian"
            return self

    def fix_upto(self, cutoff, direct = True):
        """Converts all atomic postions below the cutoff distance to "Fixed" state.

        Parameters
        ----------
        cutoff : float
            Cutoff distance is taken in angstroms if 'direct' is set to False.
        direct : bool
            Set to True by default. Interprets cutoff distance in Direct coordinates.
            Uses Cartesian otherwise.

        Returns
        -------
        self
            An object that encapsulates all the information contained within
            a POSCAR file.

        """
        if direct:
            co_vect = np.array([0.0, 0.0, cutoff])
            cutoff = np.dot(self.trans, co_vect).tolist()[0][2]
        if (self.type.lower() == "direct"):
            self.to_cart()
        self.fix = [[True, True, True] if x[2] > cutoff*self.scale else [False, False, False] for x in self.coords]
        self.selective = True
        return self

    def recentered(self,fp):
        """Returns the coords in POSCAR but with fp as its new origin.

        Parameters
        ----------
        fp : list
            Focal point. Molecule will be translated with this point as the new origin

        Returns
        -------
        list
            A list of vectors centered around fp.

        """
        # Set focal point as origin and translate it along the user specified coordinates
        ## Convert all arrays to vector-type
        fp = vector(*fp)
        vects = [vector(*x) for x in self.coords]

        ## Center the molecules fp at the origin
        centered_vects = [vect-fp for vect in vects]
        return centered_vects
    
