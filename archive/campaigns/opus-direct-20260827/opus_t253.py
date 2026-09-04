"""
T253 - can the non-abelian route be reopened?  Gr(2,3) separates R169's two
candidate mechanisms.

R169 found rank>1 disorders and blamed the TARGET SIZE (dim Gr(k,n) = 2k(n-k)
vs dim CP^{n-1} = 2(n-1)); it refuted the CONTRAST hypothesis (max/mean = n/k).
Gr(2,3) tests them against each other:

   Gr(2,3):  gauge group U(2)  -- NON-ABELIAN
             target dim 2*2*1 = 4   -- SMALLER than CP^3's 6
             contrast: two 2-planes in C^3 always intersect, so
                       Tr(P P') in [1,2] -- never zero, contrast only 2

  target-size mechanism  -> should ORDER (4 < 6)
  contrast mechanism     -> should DISORDER (2 < 4)

If it orders, the framework CAN carry a non-abelian U(2) and R170 needs
qualifying.
"""
import numpy as np, time

def orth(A):
    k = A.shape[-1]; cols=[]
    for j in range(k):
        v = A[...,j]
        for u in cols: v = v - np.sum(np.conj(u)*v,axis=-1,keepdims=True)*u
        v = v/np.maximum(np.linalg.norm(v,axis=-1,keepdims=True),1e-300)
        cols.append(v)
    return np.stack(cols,axis=-1)

def wt(Q,Nb):
    U = np.einsum('...ik,...il->...kl', np.conj(Q), Nb)
    return np.real(np.einsum('...kl,...kl->...', np.conj(U), U))

def run(n,k,L,cold,nsweep=2500,seed=311):
    rng = np.random.default_rng(seed)
    if cold:
        A = rng.normal(size=(n,k))+1j*rng.normal(size=(n,k))
        Q0,_ = np.linalg.qr(A); Q = np.broadcast_to(Q0,(L,)*4+(n,k)).copy()
    else:
        Q = orth(rng.normal(size=(L,)*4+(n,k))+1j*rng.normal(size=(L,)*4+(n,k)))
    idx=np.indices((L,)*4); masks=[(idx.sum(axis=0)%2==p) for p in (0,1)]
    cone=0.5; hist=[]
    for t in range(nsweep):
        ar=[]
        for mask in masks:
            nbs=[]
            for ax in range(4):
                nbs.append(np.roll(Q,1,ax)); nbs.append(np.roll(Q,-1,ax))
            prop=orth(Q+cone*(rng.normal(size=Q.shape)+1j*rng.normal(size=Q.shape)))
            wo=np.ones(Q.shape[:4]); wn=np.ones(Q.shape[:4])
            for nb in nbs: wo*=wt(Q,nb); wn*=wt(prop,nb)
            a=(rng.random(Q.shape[:4])<np.clip(wn/np.maximum(wo,1e-300),0,1))&mask
            Q[a]=prop[a]; ar.append(a[mask].mean())
        if t%100==99:
            m=np.mean(ar); cone*=1.15 if m>0.55 else (0.87 if m<0.35 else 1.0)
            cone=min(max(cone,0.02),4.0)
        if t%500==499:
            P=np.einsum('...ik,...jk->...ij',Q,np.conj(Q))
            hist.append(np.linalg.norm(P.mean(axis=(0,1,2,3))-np.eye(n)*k/n))
    return hist, cone

L=8
print(f"L={L}, Z^4, Born point Tr(P P')\n")
print(f"{'case':22s} {'gauge':8s} {'dim':>4s} {'contrast':>9s}  {'cold start':>34s}  {'hot final':>9s}")
for (n,k,tag,g) in ((4,1,"CP^3   (rank 1)","U(1)"),
                    (3,2,"Gr(2,3) (rank 2)","U(2)"),
                    (4,2,"Gr(2,4) (rank 2)","U(2)")):
    dim = 2*k*(n-k); ideal=np.sqrt(k*(1-k/n))
    hc,_ = run(n,k,L,True); hh,_ = run(n,k,L,False)
    print(f"{tag:22s} {g:8s} {dim:4d} {n/k:9.1f}  "
          f"{' '.join(f'{v:.4f}' for v in hc):>34s}  {hh[-1]:9.4f}"
          f"   (perfect {ideal:.3f})")
