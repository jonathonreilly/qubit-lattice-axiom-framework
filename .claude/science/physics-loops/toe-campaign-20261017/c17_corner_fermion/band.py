import numpy as np, itertools, sys
ARGS=sys.argv[1:]
from shell import *
def spin_char(j2,U):
    tr=max(-1,min(1,np.real(np.trace(U))/2)); th=2*np.arccos(tr)
    if abs(np.sin(th/2))<1e-12: return float(j2+1)*(1 if np.isclose(tr,1) else (-1)**j2)
    return np.sin((j2+1)*th/2)/np.sin(th/2)
E12=np.array([spin_char(1,U) for U in G2]); G32=np.array([spin_char(3,U) for U in G2]); E52=np.array([spin_char(5,U) for U in G2])-G32
irr={'E1/2':E12,'E5/2':E52,'G3/2':G32}
def dec(ch):
    d={k:int(round(np.real(np.sum(np.conj(v)*ch)/48))) for k,v in irr.items()}
    return {k:v for k,v in d.items() if v}
import scipy.sparse as sp, scipy.sparse.linalg as sla
F=dict(square=1,triangle=int(ARGS[0]),plaquette=1,tube=int(ARGS[1]))
out,u,Ms=C.classify(F)
print('PSG', {k:sorted(v) for k,v in out.items()})
r=run(F,twist=True,verbose=False); Mt,loc,_=r
# lift signs per 2O element relative to bare M(R): sign = Mt[k][a,b]/ (i^w1 * Mloc)
n=len(C.VERTS)
def Mfull(R):
    Pm,s=Ms[R]; return sp.csr_matrix(((-1.0)**s,(Pm,np.arange(n))),shape=(n,n))
Mf=[Mfull(R) for R in range(24)]
# sign of each 2O element: compare Mt[k] to local block of Mf
li={g:i for i,g in enumerate(loc)}
sgn=[]
for k in range(48):
    R=proj[k]; blk=Mf[R].toarray()[np.ix_(loc,loc)]*(1j**W1[R])
    sgn.append(1 if np.allclose(Mt[k],blk) else (-1 if np.allclose(Mt[k],-blk) else None))
assert None not in sgn
def H(t1,t2):
    rows=[];cols=[];vals=[]
    for k in C.EDGES:
        i,j=tuple(k); t=t1 if C.edges[k]=='onsite' else t2
        a=-t*(-1.0)**u[C.EID[k]]
        rows+= [i,j]; cols+=[j,i]; vals+=[a,a]
    return sp.csr_matrix((vals,(rows,cols)),shape=(n,n))
for t1,t2 in [(-1,0.3),(-1,-0.3),(1,0.3),(1,-0.3),(-1,1),(-1,-1)]:
    Hm=H(t1,t2).toarray(); ev,V=np.linalg.eigh(Hm)
    e0=ev[0]; m=np.sum(np.abs(ev-e0)<1e-7); Pj=V[:,:m]
    ch=np.array([sgn[k]*(1j**W1[proj[k]])*np.trace(Pj.conj().T@(Mf[proj[k]]@Pj)) for k in range(48)])
    gap=ev[m]-e0
    print(f't1={t1:+} t2={t2:+}: lowest level E={e0:.4f} deg={m} gap={gap:.4f} irreps(site-O)={dec(ch)}')
