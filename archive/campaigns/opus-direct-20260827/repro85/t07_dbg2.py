import numpy as np, sys; sys.path.insert(0,".")
from bridge_geom import *; from bridge_spec import *
L=4; S=edge_s(L,0.06,1,[0,1,-1,0]); g=geometry(S,L)
acc,lam=local_Hmatrix(S,L,{'F':lambda w:w*0},ret_spec=True,geom=g)
lam=np.sort(lam); print("smallest 6 Bloch eigenvalues:", lam[:6])
# per-block smallest
C=cband(g['loc'],L); Mv=g['Mv']; isq=1/np.sqrt(Mv); P=phases(L); idx=np.arange(L)
Kb=(C.reshape(3*L,27)@P).reshape(3,L,-1)
Kq=np.zeros((P.shape[1],L,L),dtype=complex)
for b in range(3): Kq[:,idx,(idx+b-1)%L]=Kb[b].T
Kq*=isq[None,:,None]*isq[None,None,:]; Kq=0.5*(Kq+np.conj(np.transpose(Kq,(0,2,1))))
w,_=np.linalg.eigh(Kq)
print("block q=0 eigenvalues:", w[0][:4])
print("min over all blocks of the smallest eigenvalue:", w[:,0].min(), " at block", int(w[:,0].argmin()))
print("number of blocks with smallest eig < 1e-10:", int((w[:,0]<1e-10).sum()))
