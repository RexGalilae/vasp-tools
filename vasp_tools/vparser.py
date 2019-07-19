'''

Now defunct! Functions have been reimplemented as POSCAR methods in vasp-objects.
Can be used as helper functions but avoid using them. Kept them for future reference.

'''
# from vobjects import POSCAR
# import numpy as np
#
#
# def POS_locate(info, element, index):
#     start = sum(info.nums[:info.atoms.index(element)])
#     return info.coords[start+int(index)-1]
#
# def read_POSCAR(file):
#     with open(file) as f:
#         name = f.readline().replace("\n", "")
#         ## Start reading the file in the tried POSCAR format
#         scale = float(f.readline())
#         trans = []
#         for i in range(3):
#             trans.append([float(n) for n in f.readline().split()])
#         atoms = f.readline().split()
#         nums = [int(n) for n in f.readline().split()]
#         coords = []
#         selective = False
#         fix = None
#         type = f.readline().split()[0]
#         # Skip "Selective dynamics" if it's already a fixed file
#         if type == "Selective":
#             selective = True
#             fix = []
#             type = f.readline().split()[0]
#         for i in range(sum(nums)):
#             line = f.readline().split()
#             if selective == False:
#                 coords.append([float(n) for n in line])
#             else:
#                 coords.append([float(n) for n in line[0:3]])
#                 if len(line) == 6:
#                     fix.append([truth == "T" for truth in line[3:]])
#                 else:
#                     fix.append([True, True, True])
#     # print(dict(name= name, scale=scale, trans = trans,atoms = atoms,
#     #               nums = nums, selective = selective, type = type,
#     #               coords = coords, fix = fix))
#     return POSCAR(name= name, scale=scale, trans = trans, atoms = atoms,
#                   nums = nums, selective = selective, type = type,
#                   coords = coords, fix = fix)
#
# def write_POSCAR(info,file):
#     with open(file,'w') as f:
#         f.write(info.name+"\n")
#         f.write(str(info.scale)+"\n")
#
#         for i in info.trans:
#             for j in i:
#                 print('\t{:<1.10f}'.format(j), file = f, end = "")
#             print(file = f)
#         for atom in info.atoms:
#             print("   {:>2}".format(atom), file=f, end="")
#
#         print(file= f)
#
#         for num in info.nums:
#             print("   {:>2d}".format(num), file=f, end="")
#
#         print(file=f)
#         if info.selective:
#             print("Selective dynamics", file = f)
#         print(info.type, file= f)
#         if info.selective:
#             for coord in info.coords:
#                 print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}    {'  '.join(map(str,fix[i]))}", file=f)
#         else:
#             for coord in info.coords:
#                 print(f"   {coord[0]:>12.9f}         {coord[1]:>12.9f}         {coord[2]:>12.9f}", file=f)
