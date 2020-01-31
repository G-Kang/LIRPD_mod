import os

class Tensor(object):
	def __init__(self,tape=tape):
		self.keys = {"real":False,"damp":False,"quad":False}

		get_keys(tape)



	def get_keys(tape=tape):
		os.system("pkf {0} > keys".format(tape))
		with open("keys") as f:
			for line in f.readlines():
				if "alpha" in line:
					self.keys["real"] = True
				if "alpha_imag" in line:
					self.keys["damp"] = True
				if "Atensor" in line:
					self.keys["quad"] = True