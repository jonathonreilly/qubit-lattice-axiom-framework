from t22 import *
from scipy.optimize import brentq
a=0.25
M=proj(UU)+proj(DD)+a*proj(S)
Mall=build_M_all(M)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
def Wd(E,N=72):
    tab=make_tab(E,N)
    o=weights_tab(tab,E,M24,tolN=1e-6)
    return o
f=lambda E: np.linalg.eigvalsh(Wd(E)['Wsum']).max()-3.0
for E in (3.60,3.65,3.70):
    o=Wd(E); print(E,np.linalg.eigvalsh(o['Wsum']),o['null'],o['gap'],o['first'])
Es=brentq(f,3.60,3.70,xtol=1e-13)
print('g*=E*=',repr(Es))
o=Wd(Es)
print('Wsum eig',np.linalg.eigvalsh(o['Wsum']),'null',o['null'],'gap',o['gap'])
W=o['W']
# find v with equal weights
import scipy.optimize as so
def obj(x):
    z=x[:3]+1j*x[3:]; z=z/np.linalg.norm(z)
    w=[ (z.conj()@Wk@z).real for Wk in W]
    return sum((wi-1)**2 for wi in w)
best=min((so.minimize(obj,np.random.default_rng(s).normal(size=6),tol=1e-14) for s in range(5)),key=lambda r:r.fun)
z=best.x[:3]+1j*best.x[3:]; z/=np.linalg.norm(z)
print('weights along x,y,z for v:',[(z.conj()@Wk@z).real for Wk in W],'residual',best.fun)
for k,Wk in enumerate(W): print('W',k,'eig',np.round(np.linalg.eigvalsh(Wk),6))
# exchange sector
Nn=o['nullvecs']; ex=np.linalg.eigvalsh(Nn.conj().T@PEX@Nn); print('exchange eig on null',np.round(ex,6))
np.save('ex_E.npy',np.array([Es]))
