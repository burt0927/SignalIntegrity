'''
 Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
 Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
 All Rights Reserved.

 Explicit license in accompanying README.txt file.  If you don't have that file
 or do not agree to the terms in that file, then you are not licensed to use
 this material whatsoever.
'''
from SignalIntegrity.Devices.TerminationG import TerminationG
from numpy import math

def TerminationC(C,f,Z0=None,df=0.,esr=0.):
    G=C*2.*math.pi*f*(1j+df)
    try: G=G+1/esr
    except: pass
    return TerminationG(G,Z0)
