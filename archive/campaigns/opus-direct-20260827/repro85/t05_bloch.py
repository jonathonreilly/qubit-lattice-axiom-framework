"""T05 - validate the Bloch reduction against a brute-force DENSE calculation."""
import numpy as np, itertools, sys, scipy.special as sp; sys.path.insert(0,".")
from bridge_geom import *; from bridge_spec import *
L=4; AMP=0.06; AL=[0,1,-1,0]; TAU=3.0; M2=0.25
S=edge_s(L,AMP,1,AL); g=geometry(S,L)
# ---- dense operator
verts=list(itertools.product(range(L),repeat=4)); vid={v:i for i,v in enumerate(verts)}; N=len(verts)
K=np.zeros((N,N)); Mfull=np.zeros(N)
for p in range(24):
    a=CORN[p]
    for x in verts:
        x0=x[0]
        ids=[vid[tuple((np.array(x)+a[i])%L)] for i in range(NC)]
        K[np.ix_(ids,ids)] += g['loc'][p,x0]
        for i in range(NC): Mfull[ids[i]] += g['V'][p,x0]/5.0
print(f"T05 dense L={L}: N={N}  mass check {np.abs(Mfull-g['Mv'][[v[0] for v in verts]]).max():.2e}")
B=K/np.sqrt(np.outer(Mfull,Mfull)); B=0.5*(B+B.T)
lam=np.linalg.eigvalsh(B)
lamB=local_Hmatrix(S,L,{'F':lambda w:w*0},ret_spec=True)[1]
print(f"T05 spectrum: dense vs Bloch, max diff = {np.abs(np.sort(lam)-np.sort(lamB)).max():.3e}")
# ---- W and its gradient by finite differences of the dense spectrum
def Wtot(S_):
    gg=geometry(S_,L)
    KK=np.zeros((N,N)); MM=np.zeros(N)
    for p in range(24):
        a=CORN[p]
        for x in verts:
            ids=[vid[tuple((np.array(x)+a[i])%L)] for i in range(NC)]
            KK[np.ix_(ids,ids)]+=gg['loc'][p,x[0]]
            for i in range(NC): MM[ids[i]]+=gg['V'][p,x[0]]/5.0
    BB=KK/np.sqrt(np.outer(MM,MM)); BB=0.5*(BB+BB.T)
    l=np.linalg.eigvalsh(BB); mu=l+l*l/24.0
    return -0.5*np.sum(sp.exp1(TAU*(mu+M2)))
dW=dW_reduced(S,L,TAU,m2=M2,improved=True,geom=g)
rng=np.random.default_rng(3); h=1e-5; err=[]
rms=np.sqrt((dW**2).mean())
for _ in range(6):
    c=int(rng.integers(NE)); x=int(rng.integers(L))
    Sp=S.copy(); Sp[c,x]+=h; Sm=S.copy(); Sm[c,x]-=h
    fd=(Wtot(Sp)-Wtot(Sm))/(2*h)/L**3
    err.append(abs(fd-dW[c,x])/rms)
    print(f"    (c={c},x0={x}) dW ana {dW[c,x]:+.12e}  fd {fd:+.12e}   rel(rms) {err[-1]:.2e}")
print(f"T05 max |ana-fd|/rms(dW) = {max(err):.3e}   [rms dW = {rms:.4e}]")
