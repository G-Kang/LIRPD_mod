class Atom(object):
	def __init__(self, index, elem, xyz, chg=0.0):
		self.index = index
		self.elem  = elem
		self.xyz   = xyz
		self.chg   = chg