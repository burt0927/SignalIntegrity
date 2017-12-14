'''
Created on Oct 18, 2017

@author: pete
'''
from SignalIntegrity.SParameters.SParameters import SParameters

import cmath

class Offset(SParameters):
    # pragma: silent exclude
    calcZc=False
    # pragma: include
    # offset delay in s, offsetLoss in Ohm/s, offsetZ0 in Ohms
    def __init__(self,fList,offsetDelay,offsetZ0,offsetLoss,f0=1e9):
        data=[]
        Z0=50.
        Zc=offsetZ0
        Td=offsetDelay
        R0=offsetLoss
        L=Td*Zc
        C=Td/Zc
        G=0
        for f in fList:
            R=R0*Td*cmath.sqrt(f/f0)
            Z=R+1j*2*cmath.pi*f*L
            Y=G+1j*2*cmath.pi*f*C
            y=cmath.sqrt(Z*Y)
            # pragma: silent exclude
            try:
                if self.calcZc:
                    Zc=cmath.sqrt(Z/Y)
            except:
                Zc=offsetZ0
            # pragma: include
            rho=(Zc-Z0)/(Zc+Z0)
            D=(1-rho*rho*cmath.exp(-2*y))
            S11=rho*(1-cmath.exp(-2*y))/D
            S21=(1-rho*rho)*cmath.exp(-y)/D
            data.append([[S11,S21],[S21,S11]])
        SParameters.__init__(self,fList,data)