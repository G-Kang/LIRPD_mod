import numpy as np
from atom import *
import utils

class Molecule(object):
	def __init__(self, natoms=0, atoms=[], chg=0.0):
		self.natoms = natoms
		self.atoms  = atoms
		self.chg    = chg
		self.modes  = []

	def add_atoms(self, natoms, elements, xyz, chg):
		for i in range(natoms): self.atoms.append(Atom(i,elements[i],xyz[i],chg[i]))
		self.update_natoms()

	def set_chg(self, chg):
		self.chg = chg

	def update_natoms(self):
		self.natoms = len(self.atoms)

