"""T51 S1b: which parts of the lane's (A, B, r) space satisfy BOTH gap boxes (NO/lane, U_e=I)?
(a) retained rungs A=alpha^7, B=alpha^8, r free  -> joint set?
(b) A fixed, B and r free                        -> region and Sigma
(c) B fixed, A and r free                        -> region and Sigma
"""
import numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
SOL = (6.92e-5, 8.05e-5); ATM = (2.451e-3, 2.578e-3)
A0 = MPl*aLM**7; B0 = MPl*aLM**8
def no(A,B,r):
    A,B,r = np.broadcast_arrays(np.asarray(A,float),np.asarray(B,float),np.asarray(r,float))
    ms,me,mo = c/A, c/(B*(1+r)), c/(B*(1-r))
    m1,m2,m3 = np.sort(np.stack([ms,me,mo]),axis=0)
    return m2**2-m1**2, m3**2-m1**2, m1+m2+m3
rg = np.linspace(1e-4,0.99,4000)
d21,d31,S = no(A0,B0,rg)
okS = (SOL[0]<=d21)&(d21<=SOL[1]); okA=(ATM[0]<=d31)&(d31<=ATM[1])
print('(a) retained rungs: r with dm21 in SOL:', (rg[okS].min(),rg[okS].max()) if okS.any() else None,
      '; r with dm31 in ATM:', (rg[okA].min(),rg[okA].max()) if okA.any() else None, '; both:', (okS&okA).any())
print('    min over r in (0,0.99) of dm21 =', d21.min(), '(solar box lower edge 6.92e-5): ratio', d21.min()/SOL[0], ' at r=', rg[d21.argmin()])
rr=rg[(d21/d31>=0.0268)&(d21/d31<=0.0328)]; print('    ratio-window r range (B fixed):', (rr.min(), rr.max()) if rr.size else None, ' dm31 there / ATM_hi:', (d31[(d21/d31>=0.0268)&(d21/d31<=0.0328)]/ATM[1]).min() if rr.size else None)
# (b) A fixed, B (as multiple x of B0) and r free
xs = np.exp(np.linspace(np.log(0.05), np.log(50), 1500)); 
R_, X_ = np.meshgrid(rg[::4], xs)
d21,d31,S = no(A0, B0*X_, R_)
ok = (SOL[0]<=d21)&(d21<=SOL[1])&(ATM[0]<=d31)&(d31<=ATM[1])
print('(b) A=alpha^7 fixed; B=x*alpha^8, r free: joint region x in', (X_[ok].min(), X_[ok].max()), ' r in', (R_[ok].min(), R_[ok].max()),
      ' Sigma range meV', (S[ok].min()*1e3, S[ok].max()*1e3), ' -> in rungs kB = 8 - ln x/ln(1/alpha):', 8-np.log(X_[ok].max())/np.log(1/aLM), 8-np.log(X_[ok].min())/np.log(1/aLM))
okS72 = ok & (S<0.072)
print('    with Sigma<72:', okS72.any(), ' fraction', okS72.sum()/ok.sum())
# (c) B fixed, A (multiple x of A0) and r free
d21,d31,S = no(A0*X_, B0, R_)
ok = (SOL[0]<=d21)&(d21<=SOL[1])&(ATM[0]<=d31)&(d31<=ATM[1])
print('(c) B=alpha^8 fixed; A=x*alpha^7, r free: joint region exists:', ok.any(),
      (' x in %s r in %s Sigma meV %s'%((X_[ok].min(), X_[ok].max()),(R_[ok].min(),R_[ok].max()),(S[ok].min()*1e3,S[ok].max()*1e3))) if ok.any() else '')
print('    with Sigma<72:', (ok&(S<0.072)).any())
