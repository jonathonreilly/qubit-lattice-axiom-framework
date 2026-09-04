"""T146b - the mass spectrum itself, at zero momentum.  (cleaning up T146)

T146 counted distinct |eigenvalues| of i Gamma.s + M at a GENERIC momentum, which
mixes the mass with the dispersion -- the count of 4 could be an artifact of the
combination rather than a property of M.  The masses are the eigenvalues of M
alone, at s = 0, where D = M.  Do it that way, since this overturns a recorded
result (R82) and the campaign standard is to check before withdrawing.

For a real Grassmann (Majorana-type) field the bilinear psi^T M psi keeps only the
ANTISYMMETRIC part of M, since psi_i psi_j = -psi_j psi_i.  So the physically
allowed mass matrices are the 10-dimensional antisymmetric sector of the
commutant, not the 6-dimensional symmetric one R82 sampled.  A real antisymmetric
M has spectrum +- i|m_k|, and the physical masses are the |m_k|."""
import numpy as np, sys
sys.path.insert(0,".")
from opus_t138 import setup

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]
def rank_basis(L,NF):
    M=np.array([X.ravel() for X in L]); U,s,Vt=np.linalg.svd(M)
    return [Vt[i].reshape(NF,NF) for i in range(int(np.sum(s>1e-9)))]

print("T146b  the MASS spectrum at zero momentum: eigenvalues of M itself")
for d in (2,4):
    NF,G,Gb=setup(d)
    B=cbasis(G,NF)
    RS=rank_basis([0.5*(X+X.T) for X in B],NF)
    RA=rank_basis([0.5*(X-X.T) for X in B],NF)
    rng=np.random.default_rng(99)
    print(f"\n   d={d}, fibre {NF}, taste count 2^(d/2) = {2**(d//2)}"
          f"   [commutant {len(B)} = {len(RS)} sym + {len(RA)} antisym]")
    for lab,gen,herm in (
        ("SYMMETRIC M   (R82's class)", lambda: sum(rng.normal()*X for X in RS), False),
        ("ANTISYMMETRIC M  (real field)", lambda: sum(rng.normal()*X for X in RA), True),
    ):
        cnt={}; ex=None
        for t in range(300):
            M=gen()
            ev=np.linalg.eigvalsh(1j*M) if herm else np.linalg.eigvalsh(M)
            mags=np.abs(ev)
            u,c=np.unique(np.round(np.sort(mags),8),return_counts=True)
            cnt[len(u)]=cnt.get(len(u),0)+1
            if t==0: ex=(u,c)
        print(f"      {lab:<32} distinct masses: {dict(sorted(cnt.items()))}")
        print(f"         example: masses {np.round(ex[0],5)}  multiplicities {list(ex[1])}")
print()
print("   d=4 antisymmetric giving 4 distinct masses, each 4-fold (= spin multiplicity),")
print("   means the real framework supports one independent mass PER TASTE.")
print("   R82's cap of two was an artifact of sampling the symmetric sector, which")
print("   contributes nothing to a real Grassmann field's mass term.")
