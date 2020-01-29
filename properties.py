import math
import numpy as np
from constants import *

class Atom(object):
	def __init__(self, xyz, elem, chg=0.0):
		self.xyz   = xyz
		self.elem  = elem
		self.chg   = chg

class Molecule(object):
	def __init__(self, xyzfile):
		self.modes = []
		self.read_xyzfile(xyzfile)

	def read_xyzfile(self,xyzfile):
		try:
			f = open(xyzfile,'r')
			self.natoms = int(f.readline())
			self.atoms  = np.loadtxt(xyzfile, skiprows=2, usecols=0, dtype=str)
			self.xyz    = np.loadtxt(xyzfile, skiprows=2, usecols=(1, 2, 3), dtype=float)
		except IOError:
			exit("Error loading {}".format(xyzfile))

	def read_modes(self,modefile='nmodes.inp'):
		with open(modefile) as f:
			line = f.readline()
			nmodes = 0

			while len(line) > 0:
				freqs = line.split()
				curr_modes = len(freqs)
				for i in range(curr_modes): self.modes.append(Vib(float(freqs[i]),nmodes+i))
				for i in range(2): line = f.readline()

				while len(line) > 2:
					disp = list(map(float,line.split()[1:]))
					for i in range(curr_modes): self.modes[nmodes+i].add_disp(disp[3*i:3*i+2])
					line = f.readline()

				nmodes += curr_modes
				for i in range(2): line = f.readline()
		f.close()

class Vib(object):
	def __init__(self, freq, index):
		self.freq  = freq
		self.index = index
		self.disp  = []
		self.norm  = 0.0

	def add_disp(self, atdisp):
		self.disp.append(atdisp)

	def norm_mode(self, mol):
		if len(self.disp) > 0:
			init_norm = 0.0
			for i,atom in enumerate(mol.atoms):
				mass = atomic_mass(atom)
				init_norm += sum(map(lambda x : x**2*mass, self.disp[i]))

			init_norm = math.sqrt(init_norm)

			for i in range(mol.natoms):
				self.norm += sum(map(lambda x : x**2/init_norm**2, self.disp[i]))

		else: self.norm = 1.0

	def raman_scat(self, coord):
		asq_r = []
		asq_i = []
		gsq_r = []
		gsq_i = []
		self.s_fact_r = []
		self.s_fact_i = []

		for k in range(len(self.alpha_diff)):
			if 'x' in coord or 'y' in coord or 'z' in coord:
				if 'x' in coord: j = 0
				if 'y' in coord: j = 1
				if 'z' in coord: j = 2

				asq_r.append(self.alpha_diff[k][j][j].real**2)
				asq_i.append(self.alpha_diff[k][j][j].imag**2)

			else:
				asq_r.append(((self.alpha_diff[k][0][0].real)))
				asq_i.append(((self.alpha_diff[k][0][0].imag)))




