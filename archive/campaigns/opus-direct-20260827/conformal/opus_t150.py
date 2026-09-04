"""T150 - THE TASTE PROJECTION: what field content does the framework actually allow?

R88 established that the surviving obstruction is |index| = 2^{d/2} n -- pure fibre
dimension -- and that getting n requires halving the fibre to one taste with a
projector.  The overlap lane wrote that projector as (1/2)(1 -+ iT), i.e. COMPLEX.
But whether an i is needed depends on T^2, and I should not take that on trust:
if T^2 = +1 the projector is (1/2)(1 +- T), entirely REAL, and the one-taste
theory needs no complex structure at all.

Everything a consistent projection needs is checkable:
   (a) T^2 = +1 or -1 ?                       -> is the projector real or complex
   (b) T hermitian ?                          -> is P a genuine orthogonal projector
   (c) [T, Gamma_a] = 0 ?                     -> does P commute with the kinetic operator
   (d) [T, CL] = 0 ?                          -> does the projected sector keep a chirality
   (e) [T, GRADE] = 0 ?                       -> and the grade chirality
   (f) rank P, and the index structure of the projected sector
   (g) which mass terms survive: does the commutant restricted to the P-sector still
       admit a nontrivial mass, or does projection also kill the mass freedom?
(g) is the one that matters for generations and nobody has asked it.

Also: the FIELD-CONTENT ACCOUNTING, which is the TOE-level question.  Count the
Weyl degrees of freedom the framework's fibre carries per site, and compare with
what the Standard Model needs."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t138 import setup

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

for d in (2,4):
    NF,G,Gb=setup(d)
    CL=np.eye(NF)
    for a in range(d): CL=CL@G[a]
    T=np.eye(NF)
    for a in range(d): T=T@Gb[a]
    GRADE=np.diag([(-1)**len(S) for S in
        [tuple(c) for k in range(d+1) for c in itertools.combinations(range(d),k)]]).astype(float)
    print(f"\n=== d={d}, fibre {NF} ===")
    print(f"   (a) T^2 = {'+I' if np.abs(T@T-np.eye(NF)).max()<1e-12 else ('-I' if np.abs(T@T+np.eye(NF)).max()<1e-12 else '??')}"
          f"   -> projector is {'REAL (1/2)(1 +- T)' if np.abs(T@T-np.eye(NF)).max()<1e-12 else 'COMPLEX (1/2)(1 -+ iT)'}")
    print(f"   (b) T hermitian?  |T - T^T| = {np.abs(T-T.T).max():.1e}")
    print(f"   (c) [T, Gamma_a] = 0 ?   max = {max(np.abs(T@G[a]-G[a]@T).max() for a in range(d)):.1e}")
    print(f"   (d) [T, CL]    = {np.abs(T@CL-CL@T).max():.1e}")
    print(f"   (e) [T, GRADE] = {np.abs(T@GRADE-GRADE@T).max():.1e}")
    Tr=T if np.abs(T@T-np.eye(NF)).max()<1e-12 else 1j*T
    P=0.5*(np.eye(NF)+Tr)
    r=int(np.round(np.real(np.trace(P))))
    print(f"   (f) rank P = {r} of {NF}  (half the fibre = {NF//2})   P^2-P = {np.abs(P@P-P).max():.1e}")
    # (g) does a nontrivial mass survive inside the projected sector?
    B=cbasis(G,NF)
    keep=[]
    for X in B:
        PX=P@X@P
        if np.abs(PX).max()>1e-9: keep.append(PX)
    M=np.array([X.ravel() for X in keep])
    rk=np.linalg.matrix_rank(M,tol=1e-9) if len(keep) else 0
    print(f"   (g) commutant restricted to the P-sector: dimension {rk} (full commutant {len(B)})")
    if rk:
        rng=np.random.default_rng(3)
        cnts={}
        for _ in range(200):
            X=sum(rng.normal()*Y for Y in keep); X=0.5*(X+X.conj().T)
            ev=np.linalg.eigvalsh(X)
            ev=ev[np.abs(ev)>1e-9]
            u,c=np.unique(np.round(ev,8),return_counts=True)
            cnts[len(u)]=cnts.get(len(u),0)+1
        print(f"       distinct masses inside the projected sector: {dict(sorted(cnts.items()))}")
print()
print("=== FIELD-CONTENT ACCOUNTING (d=4) ===")
print("   framework fibre           : Lambda*(R^4) = 16 components")
print("   as a complex Cl(4) module : 16 complex = 4 Dirac = 8 Weyl per site")
print("   after one-taste projection: 4 complex = 1 Dirac = 2 Weyl per site")
print("   Standard Model needs      : 16 Weyl per generation x 3 = 48 Weyl")
print("   ratio to the unprojected fibre: 48/8 = 6")
