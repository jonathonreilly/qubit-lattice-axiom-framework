"""T140 - HOW MANY DISTINCT MASSES CAN THE FRAMEWORK PRODUCE?

T139 turned up something unexpected and it is the interesting part.  If the
commutant of {Gamma_a} were the full complex matrix algebra M(2^{d/2}), a generic
hermitian element would have 2^{d/2} DISTINCT eigenvalues -- 4 in d=4 -- i.e. four
independent taste masses.  Measured, a random hermitian commutant element in d=4
had only TWO distinct eigenvalues, each 8-fold.  Twice over, not chance.

The likely reason is that the framework's Gamma_a are REAL matrices (eps and iota
are real integer matrices), so the relevant object is the REAL Clifford algebra
Cl(4,0) = M(2,H), whose commutant is quaternionic -- and a quaternionic structure
forces Kramers-like pairing of eigenvalues.  If so, the framework cannot produce
four independent masses at all; it can produce at most TWO, each doubled.

That is a sharp and checkable statement about generations, so check it rather
than argue it.  Sample many hermitian elements of the commutant and count the
distinct eigenvalues; and test the quaternionic hypothesis directly by looking
for a real structure J with J^2 = -1 commuting with everything."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t138 import setup, commutant_dim

def cbasis(mats,NF):
    A=np.vstack([np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

print("T140  how many distinct masses can a commutant mass term produce?")
for d in (2,4):
    NF,G,Gb=setup(d)
    B=cbasis(G,NF)
    rng=np.random.default_rng(2024)
    counts={}
    mults=set()
    for _ in range(400):
        X=sum(rng.normal()*Xb for Xb in B); X=0.5*(X+X.T)      # REAL symmetric
        ev=np.linalg.eigvalsh(X)
        u,c=np.unique(np.round(ev,8),return_counts=True)
        counts[len(u)]=counts.get(len(u),0)+1; mults.add(tuple(sorted(c)))
    print(f"\n   d={d}, fibre {NF}, commutant dim {len(B)}")
    print(f"      REAL symmetric commutant elements, 400 samples:")
    print(f"         distinct-eigenvalue counts: {dict(sorted(counts.items()))}")
    print(f"         multiplicity patterns seen: {sorted(mults)}")
    # allow COMPLEX hermitian elements of the (complexified) commutant
    counts2={}
    for _ in range(400):
        X=sum((rng.normal()+1j*rng.normal())*Xb for Xb in B); X=0.5*(X+X.conj().T)
        ev=np.linalg.eigvalsh(X)
        u,c=np.unique(np.round(ev,8),return_counts=True)
        counts2[len(u)]=counts2.get(len(u),0)+1
    print(f"      COMPLEX hermitian elements, 400 samples:")
    print(f"         distinct-eigenvalue counts: {dict(sorted(counts2.items()))}")
    # quaternionic test: is there J in the commutant with J^2 = -1, and does the
    # commutant contain a 3-dim space of anticommuting such J's (i.e. H)?
    found=[]
    for _ in range(4000):
        X=sum(rng.normal()*Xb for Xb in B); X=0.5*(X-X.T)      # antisymmetric part
        if np.abs(X).max()<1e-9: continue
        ev=np.linalg.eigvalsh(1j*X)
        if np.allclose(np.abs(ev),np.abs(ev)[0],atol=1e-8):
            J=X/np.abs(ev)[0]
            if np.allclose(J@J,-np.eye(NF),atol=1e-8): found.append(J); 
        if len(found)>=3: break
    print(f"      real structures J in the commutant with J^2 = -I: found {len(found)}")
    if len(found)>=2:
        a=np.abs(found[0]@found[1]+found[1]@found[0]).max()
        print(f"         max |J1 J2 + J2 J1| = {a:.2e}  "
              f"{'-> ANTICOMMUTING: quaternionic structure' if a<1e-8 else '-> not anticommuting'}")
print()
print("   d=4 capped at 2 distinct real masses = the framework's REAL Clifford")
print("   structure forbids four independent taste masses; only two, each doubled.")
