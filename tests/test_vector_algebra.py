from vasp_tools.vector_algebra import *
import sys, os
import unittest

sys.path.append("/home/alhazen/Desktop/Coding/VASP-script-package/vasp-git/vasp_tools")

class TestVectors(unittest.TestCase):
    """Tests if everything in the module works as intended"""
    def setUp(self):
        u = vector(0,0,1)
        v = vector(1,1,1)

    def test_vector(self):
        self.assertEqual(u.__dict__, vector(0,0,1).__dict__)

    def test_add(self):
        self.assertEqual((u+v).to_list(), [1,1,2])

    def test_sub(self):
        self.assertEqual((u-v).to_list(), [-1,-1,0])

    def test_rotate(self):
        self.assertEqual(u.rotate(pi/2, 'x').to_list(), [0.0,-1.0,0.0])

if __name__ == '__main__':
    unittest.main()
