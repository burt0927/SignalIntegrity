import cmath

class RLGCElement():
	def __init__(self,R,L,G,C,Z,Y):
		self.m_R = R
		self.m_L = L
		self.m_G = G
		self.m_C = C
		self.m_Z = Z
		self.m_Y = Y
	
class RLGC():
	def __init__(self,sp,Td):
		self.m_RLGC = None
		for n in range(len(sp.m_d)):
			S = sp[n]
			S11=S[0][0]
			S12=S[0][1]
			S21=S[1][0]
			S22=S[1][1]
			rhol = 1./(2.*S11)*(S11*S11+1.-S21*S21)
			rhor = 1./(2.*S11)*cmath.sqrt((S11+1.-S21)*(S11+1.+S21)*(S11-1.-S21)*(S11-1.+S21))
			rhop = rhol + rhor
			rhom = rhol - rhor
			engml = 1./(2.*S21*rhom*rhom)*(rhom*rhom-1.)
			engpl = 1./(2.*S21*rhop*rhop)*(rhop*rhop-1.)
			engmr = 1./(2.*S21*rhom*rhom)*cmath.sqrt(rhom*rhom*rhom*rhom+(4.*S21*S21-2.)*rhom*rhom+1.)
			engpr = 1./(2.*S21*rhop*rhop)*cmath.sqrt(rhop*rhop*rhop*rhop+(4.*S21*S21-2.)*rhop*rhop+1.)
			engmm = engml - engmr
			engmp = engml + engmr
			engpm = engpl - engpr
			engpp = engpl + engpr
			# now we need to pick out non absurd ones
			eng = engmp
			rho = rhom
			
			pass
#	def __getitem__(self,item):
#		return self.m_RLGC[item]