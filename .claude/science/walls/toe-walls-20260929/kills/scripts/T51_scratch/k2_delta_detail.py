"""K2 detail: 2<->3-symmetric singlet-doublet entry delta at the FULLY retained A=alpha^7 MPl, B=alpha^8 MPl, eps=alpha/2*B."""
import numpy as np
from scipy.optimize import brentq
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
A0 = MPl*aLM**7; B0 = MPl*aLM**8; r=aLM/2
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3)
def spec(d):
    M=np.array([[A0,d,d],[d,r*B0,B0],[d,B0,r*B0]])
    w=np.linalg.eigvalsh(M); m=np.sort(c/np.abs(w))
    return w/B0, m, m[1]**2-m[0]**2, m[2]**2-m[0]**2, m.sum()
for lab,d in [('delta=0 (retained)',0.0),('delta=2A/3',2/3*A0),('delta=0.65A',0.65*A0),('delta=A/sqrt2',A0/np.sqrt(2)),('delta=0.64A',0.64*A0),('delta=0.6675A',0.6675*A0),('delta=0.6676A',0.6676*A0)]:
    w,m,d21,d31,S=spec(d)
    print('%-20s RH eig/B %s  m(meV) %s dm21 %.3e%s dm31 %.3e%s Sigma %.1f'%(lab,np.round(w,3),np.round(m*1e3,2),d21,' [SOL]' if SOL[0]<=d21<=SOL[1] else '',d31,' [ATM]' if ATM[0]<=d31<=ATM[1] else '',S*1e3))
# edges of the solar box in delta/A (atm box is untouched: odd state B(1-r) is decoupled from delta)
f=lambda d,t: spec(d*A0)[2]-t
lo=brentq(lambda d:f(d,SOL[0]),0.5,0.7) if f(0.5,SOL[0])*f(0.7,SOL[0])<0 else None
hi=brentq(lambda d:f(d,SOL[1]),0.5,0.7) if f(0.5,SOL[1])*f(0.7,SOL[1])<0 else None
print('dm21 = SOL edges at delta/A =',lo,hi)
print('dm31 across the window (odd state decoupled):',spec(0.65*A0)[3], 'vs delta=0:',spec(0)[3])
