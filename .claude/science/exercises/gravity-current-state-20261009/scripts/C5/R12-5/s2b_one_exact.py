# R12-5 s2b: one constraint exact, the other energetic (Gaussian). Power counting check of the <= k^2 cap and stability.
#  Case GX: G exact (E restricted to ker G, h quotiented by Im V), h side strongly G-invariant only (R^T R, O(k^4)) + W S^2 penalty;
#           E side weak K_N (allowed since S is only energetic).
#  Case SX: S exact (h restricted to ker S, E quotiented by S-gauge), E side strongly S-invariant only (C^T C, O(k^2));
#           h side weak h:R + U|G|^2 penalty on E.
import numpy as np, io, contextlib, sys
with contextlib.redirect_stdout(io.StringIO()):
    from s2_gauss_energetic import Vmap,Svec,Rmap,Cmap,KN,PTT
rng=np.random.default_rng(3); out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def nullbasis(A,tol=1e-10):
    u,sv,vt=np.linalg.svd(A); r=np.sum(sv>tol*max(1,sv.max())); return vt[r:].T
def reduced(case,q,U=1.0,W=1.0):
    V=Vmap(q); s=Svec(q)
    if case=='GX':
        Eb=nullbasis(V.T)                  # E in ker G
        hb=nullbasis(V.T)                  # h representatives orthogonal to Im V (quotient)
        K=Eb.T@KN@Eb; B=hb.T@(Rmap(q).T@Rmap(q)+W*np.outer(s,s))@hb
        M=Eb.T@hb                          # canonical pairing between reduced spaces
    else:
        hb=nullbasis(s[None,:])            # h in ker S
        Eb=nullbasis(s[None,:])            # E representatives orthogonal to S-gauge direction
        K=Eb.T@(Cmap(q).T@Cmap(q)+U*V@V.T)@Eb; B=hb.T@(-Rmap(q))@hb
        M=Eb.T@hb
    # hdot = K E (in h-coords via pairing): omega^2 = eig( M^-T K M^-1 B ) ; use generalized form with pairing
    Mi=np.linalg.pinv(M)
    w2=np.linalg.eigvals(Mi.T@K@Mi@B) if False else np.linalg.eigvals(np.linalg.pinv(M.T)@K@np.linalg.pinv(M)@B)
    return K,B,w2
for case in ['GX','SX']:
    d=rng.normal(size=3); d/=np.linalg.norm(d); ks=[0.04,0.02,0.01,0.005]; tt=[]
    for km in ks:
        q=2*np.sin(km*d/2); K,B,w2=reduced(case,q)
        w2=np.sort(w2.real); tt.append(np.sqrt(np.abs(w2[-2:])))
    tt=np.array(tt)
    slopes=[np.polyfit(np.log(ks),np.log(tt[:,i]),1)[0] for i in range(2)]
    minK=min(np.linalg.eigvalsh(reduced(case,2*np.sin(rng.uniform(-np.pi,np.pi,3)/2))[0]).min() for _ in range(200))
    minB=min(np.linalg.eigvalsh(reduced(case,2*np.sin(rng.uniform(-np.pi,np.pi,3)/2))[1]).min() for _ in range(200))
    P(f"case {case}: top-two (TT) omega exponents {slopes[0]:.3f},{slopes[1]:.3f};  min eig reduced K over 200 random k: {minK:.2e};  min eig reduced B: {minB:.2e}")
P("reading: GX (exact G, energetic S, weak E-side): K,B >= 0 => stable Gaussian, TT ~ k^2.  SX (exact S, energetic G, weak h-side h:R): B has a negative direction iff h:R is indefinite on ker S mod nothing (h_t removed by S; check sign above).")
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
