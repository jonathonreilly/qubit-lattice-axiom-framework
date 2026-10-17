import sys, numpy as np
sys.path.insert(0,'.')
from core import *
P=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def U_of(R):
    # find U in SU(2) with U s_b U^+ = sum_c R_cb s_c by solving over candidate generators
    from scipy.linalg import expm, logm
    w,v=np.linalg.eig(R); k=np.argmin(abs(w-1)); n=np.real(v[:,k]); n/=np.linalg.norm(n)
    th=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    for sgn in (1,-1):
        U=expm(-0.5j*sgn*th*sum(n[i]*P[i+1] for i in range(3)))
        if all(np.allclose(U@P[b+1]@U.conj().T, sum(R[c,b]*P[c+1] for c in range(3))) for b in range(3)): return U
    raise Exception
bad=0
for R in O:
    U=U_of(R)
    for b in range(3):
        s,T=act(R,tuple([0]*0+[b+1]+[0]*20))   # single label at origin qubit 0
    # check act on generic single-qubit labels at each site/qubit
    for k in range(21):
        for l in (1,2,3):
            S=[0]*21; S[k]=l; s,T=act(R,tuple(S))
            j=[m for m in range(21) if T[m]][0]
            img=U@P[l]@U.conj().T
            if not np.allclose(img, s*P[T[j]]): bad+=1
            i,a=divmod(k,3); i2,a2=divmod(j,3)
            if tuple(R.dot(POS[i]))!=POS[i2] or abs(R[a2,a])!=1: bad+=1
print('SU(2) consistency failures:',bad)
