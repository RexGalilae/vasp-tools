#!/usr/bin/env python
# -*- coding: utf-8 -*-
from vasp_tools.objects import POSCAR
import unittest
import json

class TestVaspObjects(unittest.TestCase):
    """Tests if everything in the module works as intended"""
    def setUp(self):
        refPOS = POSCAR(**json.load(open("refPOS.json")))
        testPOS = POSCAR("sample-vasp-files/POSCAR-C-H")

    def testPOSCAR(self):
        self.assertEqual(testPOS.__dict__, refPOS.__dict__)

    def test_cart_direct(self):
        self.assertEqual(testPOS.to_cart().__dict__, refPOS.to_cart().__dict__)
        self.assertEqual(testPOS.to_direct().__dict__, refPOS.to_direct().__dict__)

    def test_recentered(self):
        self.assertEqual(testPOS.recentered().__dict__, refPOS.recentered().__dict__)

if __name__ == '__main__':
    unittest.main()
