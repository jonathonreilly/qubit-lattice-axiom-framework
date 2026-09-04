"""T139 - CONSTRUCTIVE: what a mass term in the commutant actually does.

T138 established the algebra: the commutant of {Gamma_a} is exactly 2^d
dimensional (4 in d=2, 16 in d=4, with a 2e15 singular-value gap so there is no
tolerance ambiguity of the kind that sank R41), while the commutant of
{Gamma_a} together with {Gb_a} is 1.  That also RESOLVES the old R41 item: the
'commutant dimension 1' recorded there is the commutant of BOTH Clifford sets;
the commutant of Gamma alone is 2^d, and that is the u(2^{d/2}) taste algebra.

Now the constructive question.  D = Gamma.partial + M with M in that commutant.
   * M proportional to the identity  -> tastes stay degenerate (the framework's
     own mass term, and the reason R16 reads det Q = (m^2 + s.g^-1.s)^{2^{d-1}});
   * M non-central                   -> the level splits, and the pattern of the
     split IS the mass spectrum of the tastes.
Measure the pattern, and count what is reachable.  This is the useful form of the
generations question: not 'are generations there' but 'what spectra can the
framework's own algebra produce, and what would have to select one'.

Teeth: a mass term OUTSIDE the commutant must wreck the structure (it fails to
commute with Gamma.s, so it does not act as a clean taste mass) -- run it as the
control."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t138 import setup

def commutant_basis(mats,NF):
    rows=[np.kron(m,np.eye(NF))-np.kron(np.eye(NF),m.T) for m in mats]
    A=np.vstack(rows)
    U,s,Vt=np.linalg.svd(A)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    ns=Vt[len(s)-int(np.sum(s<=tol)):] if np.sum(s<=tol)<len(Vt) else Vt[np.sum(s>tol):]
    return [v.reshape(NF,NF) for v in Vt[np.sum(s>tol):]]

for d in (2,4):
    NF,G,Gb=setup(d)
    B=commutant_basis(G,NF)
    print(f"\nd={d}, fibre {NF}: commutant basis has {len(B)} elements (expect {2**d})")
    # verify each basis element commutes with every Gamma
    err=max(abs(X@m-m@X).max() for X in B for m in G)
    print(f"   max |[X, Gamma_a]| over the basis: {err:.2e}")
    # take a hermitian element with prescribed distinct eigenvalues and see the split
    rng=np.random.default_rng(11)
    X=sum(rng.normal()*Xb for Xb in B); X=0.5*(X+X.conj().T)
    ev=np.linalg.eigvalsh(X)
    print(f"   a random hermitian commutant element has eigenvalues:")
    print(f"      " + " ".join(f"{v:+.5f}" for v in ev))
    u,c=np.unique(np.round(ev,9),return_counts=True)
    print(f"      -> {len(u)} DISTINCT values, multiplicities {list(c)}"
          f"   (fibre {NF} = {len(u)} tastes x {NF//max(len(u),1)} spin)")
    # now the spectrum of Gamma.s + M at a generic momentum
    s=np.array([0.7,-0.3,0.45,0.9][:d])
    Gs=sum(s[a]*G[a] for a in range(d))
    for nm,M in (("M = 0 (framework's massless case)",np.zeros((NF,NF))),
                 ("M = m*I (the framework's own mass)",0.6*np.eye(NF)),
                 ("M in the commutant, non-central",0.6*X/np.abs(ev).max())):
        H=1j*Gs+M
        lam=np.linalg.eigvals(H); lam=lam[np.argsort(lam.real+1e-6*lam.imag)]
        uu,cc=np.unique(np.round(lam,8),return_counts=True)
        print(f"   {nm:<36} -> {len(uu)} distinct eigenvalues, mult {list(cc)}")
    # CONTROL: mass outside the commutant
    Y=rng.normal(size=(NF,NF)); Y=0.5*(Y+Y.T)
    P=sum(np.trace(Xb.conj().T@Y)/np.trace(Xb.conj().T@Xb)*Xb for Xb in B)
    Yout=Y-P                                     # component orthogonal to the commutant
    H=1j*Gs+0.6*Yout/np.abs(np.linalg.eigvalsh(Yout)).max()
    lam=np.linalg.eigvals(H)
    uu,cc=np.unique(np.round(lam,8),return_counts=True)
    print(f"   CONTROL mass OUTSIDE the commutant      -> {len(uu)} distinct, mult {list(cc)}"
          f"   {'(structure destroyed, as it must be)' if len(uu)==NF else ''}")
print()
print("The reachable spectra: a hermitian element of the commutant has 2^{d/2}")
print("eigenvalues, each with spin multiplicity 2^{d/2}.  So the framework's algebra")
print("permits AT MOST 2^{d/2} distinct masses -- 4 in d=4 -- and nothing in the")
print("Clifford relation picks one.  Three generations would need one of the four")
print("removed or made degenerate with another.")
