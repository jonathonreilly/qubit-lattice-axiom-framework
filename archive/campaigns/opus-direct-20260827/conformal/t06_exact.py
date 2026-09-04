"""T06 - EXACT check of the Bloch trace assembly: dense eigendecomposition with
analytic dK/ds, dM/ds (no finite differences anywhere)."""
import numpy as np, itertools, sys; sys.path.insert(0,".")
from bridge_geom import *; from bridge_spec import *
L=int(sys.argv[1]) if len(sys.argv)>1 else 4
AMP=0.06; AL=[0,1,-1,0]; TAU=3.0
for M2, IMP in ((0.25,True),(0.0,True),(0.0,False)):
    S=edge_s(L,AMP,1,AL); g=geometry(S,L)
    verts=list(itertools.product(range(L),repeat=4)); vid={v:i for i,v in enumerate(verts)}; N=len(verts)
    VA=np.array(verts)
    K=np.zeros((N,N)); Mf=np.zeros(N)
    for p in range(24):
        a=CORN[p]
        ids=np.stack([np.array([vid[tuple(v)] for v in (VA+a[i])%L]) for i in range(NC)],1)  # (N,5)
        for i in range(NC):
            for j in range(NC): np.add.at(K,(ids[:,i],ids[:,j]),g['loc'][p,VA[:,0],i,j])
            np.add.at(Mf,ids[:,i],g['V'][p,VA[:,0]]/5.0)
    isq=1/np.sqrt(Mf); B=K*isq[:,None]*isq[None,:]; B=0.5*(B+B.T)
    lam,U=np.linalg.eigh(B)
    mu = lam+lam*lam/24.0 if IMP else lam
    mup= 1+lam/12.0 if IMP else np.ones_like(lam)
    x=mu+M2
    with np.errstate(divide='ignore'):
        Fv=np.where(x>1e-13, np.exp(-TAU*x)*mup/np.where(x>1e-13,x,1.0), 0.0)
    dW=dW_reduced(S,L,TAU,m2=M2,improved=IMP,geom=g)
    rng=np.random.default_rng(11); errs=[]; rms=np.sqrt((dW**2).mean())
    for _ in range(4):
        c=int(rng.integers(NE)); x0=int(rng.integers(L))
        dK=np.zeros((N,N)); dM=np.zeros(N)
        for p in range(24):
            a=CORN[p]
            for k in range(10):
                if SEC[p,k]!=c: continue
                sel=(VA[:,0]+SEX[p,k])%L==x0
                if not sel.any(): continue
                vs=VA[sel]
                ids=np.stack([np.array([vid[tuple(v)] for v in (vs+a[i])%L]) for i in range(NC)],1)
                for i in range(NC):
                    for j in range(NC): np.add.at(dK,(ids[:,i],ids[:,j]),g['dloc'][p,vs[:,0],k,i,j])
                    np.add.at(dM,ids[:,i],g['dV'][p,vs[:,0],k]/5.0)
        Yh=dK*isq[:,None]*isq[None,:]; Zh=dM*isq*isq
        dlam=np.einsum('ai,ab,bi->i',U,Yh,U)-lam*np.einsum('ai,a,ai->i',U,Zh,U)
        ex=0.5*float(np.sum(Fv*dlam))/L**3
        errs.append(abs(ex-dW[c,x0])/rms)
        print(f"   m2={M2} imp={IMP} (c={c},x0={x0}):  Bloch {dW[c,x0]:+.14e}  dense {ex:+.14e}  d/rms {errs[-1]:.2e}")
    print(f"T06 L={L} m2={M2} improved={IMP}:  MAX |Bloch-dense|/rms = {max(errs):.3e}\n")
