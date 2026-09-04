"""T146 - DOES R82'S TWO-MASS CAP SURVIVE THE RIGHT MASS TERM?

R82 concluded that the framework's REAL structure caps the number of distinct
fermion masses at two, from sampling SYMMETRIC elements of the commutant of
{Gamma_a} (400/400 gave exactly 2 distinct eigenvalues, multiplicity (8,8)), with
the discriminating invariant dim(symmetric part) = 6 identifying the algebra as
M(2,H).

But symmetric may be the WRONG class.  T141 found the commutant splits as
   16 = 6 symmetric + 10 ANTISYMMETRIC
and for a real (Majorana-type) Grassmann field the mass term psi^T M psi picks out
the ANTISYMMETRIC part of M -- the symmetric part contributes nothing at all.  So
the physically allowed mass matrices for a real Kahler-Dirac field are the
10-dimensional antisymmetric sector, which R82 never tested.  If antisymmetric
elements carry more distinct masses, the cap is an artifact of my choice of class,
not a fact about the framework, and a recorded obstruction falls.

Three classes to test, in the full operator i Gamma.s + M at a generic momentum:
   (a) M symmetric      -- R82's choice
   (b) M ANTISYMMETRIC  -- the physical class for a real field
   (c) M complex hermitian -- the physical class for a complex (Dirac) field
Count distinct |eigenvalues|, since a real antisymmetric M has purely imaginary
spectrum in +- pairs and the physical masses are the magnitudes.

Control with teeth: an M drawn from OUTSIDE the commutant must not organise into
clean multiplets; if it does, the test is not measuring the commutant structure."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t138 import setup

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

def distinct(vals,tol=8):
    u,c=np.unique(np.round(np.sort(vals),tol),return_counts=True)
    return len(u),list(c)

for d in (2,4):
    NF,G,Gb=setup(d)
    B=cbasis(G,NF)
    Bs=[0.5*(X+X.T) for X in B]; Ba=[0.5*(X-X.T) for X in B]
    # orthonormal bases of the two sectors
    def rank_basis(L):
        M=np.array([X.ravel() for X in L])
        U,s,Vt=np.linalg.svd(M)
        return [Vt[i].reshape(NF,NF) for i in range(int(np.sum(s>1e-9)))]
    RS=rank_basis(Bs); RA=rank_basis(Ba)
    print(f"\nd={d}, fibre {NF}: commutant {len(B)} = {len(RS)} symmetric + {len(RA)} antisymmetric")
    rng=np.random.default_rng(1234)
    s=np.array([0.7,-0.3,0.45,0.9][:d]); Gs=sum(s[a]*G[a] for a in range(d))
    def survey(gen,label,n=300):
        cnt={}
        for _ in range(n):
            M=gen()
            H=1j*Gs+M
            ev=np.linalg.eigvals(H)
            k,_=distinct(np.abs(ev))
            cnt[k]=cnt.get(k,0)+1
        print(f"      {label:<44} distinct |eigenvalues|: {dict(sorted(cnt.items()))}")
    survey(lambda: sum(rng.normal()*X for X in RS), "(a) M symmetric        [R82's class]")
    survey(lambda: sum(rng.normal()*X for X in RA), "(b) M ANTISYMMETRIC    [real/Majorana field]")
    survey(lambda: sum((rng.normal()+1j*rng.normal())*X for X in B) if True else None,
           "(c) M complex in commutant [Dirac field]")
    # hermitian complex combination
    def herm():
        M=sum((rng.normal()+1j*rng.normal())*X for X in B); return 0.5*(M+M.conj().T)
    survey(herm, "(c') M complex HERMITIAN in commutant")
    # CONTROL: outside the commutant
    def outside():
        Y=rng.normal(size=(NF,NF)); Y=0.5*(Y-Y.T)
        P=sum(np.trace(X.conj().T@Y)/np.trace(X.conj().T@X)*X for X in RA)
        return Y-P
    survey(outside, "CONTROL: antisymmetric OUTSIDE the commutant")
print()
print("If (b) gives more than 2 distinct masses, R82's cap was an artifact of testing")
print("the symmetric sector, and the framework's real structure does NOT cap generations.")
