from utils import *
import sys,os,glob
from molecule import *
from numpy import *
from copy import deepcopy


fxyz = 'test.xyz'
mol = Molecule().read_xyzfile(fxyz)
mol.read_modes(modefile='nmodes.inp')

vibs = mol.modes
freq = '45.749'

norm = 0.0
for v in vibs:
    if v.freq == float(freq):
        v.norm_mode(mol)
        norm = v.norm

if norm == 0.0:
    print ('xx')
    sys.exit(-1)

print(norm)
