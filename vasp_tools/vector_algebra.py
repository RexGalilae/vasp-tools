import numpy as np
import math
import sympy as sp
from mpmath import radians, sin, cos, pi
import decimal

class vector(object):
    """A minimalist reimplementation vpython for handling xyz-type file data.

    Attributes
    ----------
    x : float
        x-coordinate of vector
    y : float
        y-coordinate of vector
    z : float
        z-coordinate of vector

    """
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.z = args[2]

    def __repr__(self):
        """Makes vectors human-readable while working on IPython

        Returns
        -------
        str
            <self.x, self.y, self.z>

        """
        return f"<{self.x}, {self.y}, {self.z}>"

    def __add__(self, other):
        """Allows binary addition between two vector-type objects.

        Parameters
        ----------
        self : vector
            A vector
        other : vector
            Another vector

        Returns
        -------
        vector
            The resultant vector of adding the two vectors.

        """
        return vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        """Allows binary subtraction between two vector-type objects.

        Parameters
        ----------
        self : vector
            A vector
        other : vector
            Another vector

        Returns
        -------
        vector
            The resultant vector of subtracting the two vectors.

        """
        return vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def to_list(self):
        """Returns the vector as a list of floats

        Returns
        -------
        list
            [self.x, self.y, self.z] of the vector

        """
        return [self.x, self.y, self.z]

    def rotate(self, angle, axis):
        """Performs a rotation transform on the vector

        Parameters
        ----------
        angle : float
            Angle in radians taken counter-clockwise from the axis.
        axis : str or int
            The axis about which the rotation is to be applied. Can be passed
            either as a string or an int.

            x-axis : "x" <=> 0
            y-axis : "y" <=> 1
            z-axis : "z" <=> 2

        Returns
        -------
        vector
            Returns the rotated vector.

        """
        cs = cos(angle)
        sn = sin(angle)
        list = self.to_list()
        if axis == "x" or axis == 0:
            trans = np.matrix([[1,  0,  0],
                               [0, cs,-sn],
                               [0, sn, cs]]).astype(float)
            list = np.array(np.matmul(trans, self.to_list())).tolist()[0]

        if axis == "y" or axis == 1:
            trans = np.matrix([[cs ,  0,  sn],
                               [0  ,  1 ,  0],
                               [-sn,  0,  cs]]).astype(float)
            list = np.array(np.matmul(trans, self.to_list())).tolist()[0]

        if axis == "z" or axis == 2:
            trans = np.matrix([[cs ,-sn, 0],
                               [sn , cs, 0],
                               [0  ,  0, 1]]).astype(float)
            list = np.array(np.matmul(trans, self.to_list())).tolist()[0]
        return vector(*list)
