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




