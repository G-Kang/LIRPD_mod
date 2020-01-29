import atom

class Molecule(object):
	def __init__(self, natoms, atoms, modes, chg):
		self.natoms = natoms
		self.atoms  = atoms
		self.modes  = modes
		self.chg    = chg

	def add_atom(self, natoms, elements, xyz, chg):
		for i in range(natoms):
			self.atoms.append(Atom(i, elements[i], xyz[i], chg))

	def set_chg(self, chg):
		self.chg = chg

	def read_xyzfile(self, xyzfile):
		try:
			f = open(xyzfile,'r')
			self.natoms = int(f.readline())
			elements    = np.loadtxt(xyzfile, skiprows=2, usecols=0, dtype=str)
			xyz         = np.loadtxt(xyzfile, skiprows=2, usecols=(1, 2, 3), dtype=float)

			self.add_atom(self.natoms, elements, xyz, 0.0)

		except IOError:
			exit("Error loading {}".format(xyzfile))

	def read_modes(self, modefile='nmodes.inp'):
		self.modes = []

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
		def __init__(self, index, freq):
			self.index = index
			self.freq  = freq
			self.disp  = []
			self.norm  = 0.0

		def add_disp(self, atdisp):
			self.disp.append(atdisp)

		def norm_mode(self):
			if len(self.disp) > 0:
				init_norm = 0.0
				for i,atom in enumerate(self.atoms):
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




