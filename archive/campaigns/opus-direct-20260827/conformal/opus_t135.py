"""T135 - CAN TOPOLOGY DO WHAT GEOMETRY CANNOT?  The taste degeneracy on a NON-SPIN space.

T134 closed the geometric route: curvature lifts accidental symmetry degeneracies
but leaves the 2^{d/2}-fold taste degeneracy untouched at 1e-13, because
Lambda*(M) = S (x) S-bar and the Kahler-Dirac operator is D (x) 1 -- S-bar
contributes multiplicity, not spectrum.

But that protection runs entirely through S, and S EXISTS ONLY ON A SPIN
MANIFOLD.  On a non-spin space there is no spinor bundle to factor through, so
the argument has nothing to stand on.  Lambda*(M) still exists -- it is built from
the tangent bundle and needs no spin structure -- so the Kahler-Dirac field is
still defined.  That is the asymmetry worth exploiting, and it is exactly the
framework's own situation: its arena is a CELL COMPLEX, and nothing in the
framework has ever required that complex to be spin.

Cheapest decisive test: RP^2 = S^2 / antipodal.  Non-orientable, hence non-spin,
and constructible by quotienting the icosphere, which is antipodally symmetric by
construction at every subdivision level.

TECHNICAL POINT that makes this legitimate: DEC on a non-orientable surface.
Face orientations cannot be chosen consistently, but that does not matter --
d_1 is defined up to a sign per face, and B_1^T B_1 is INVARIANT under flipping
one (the sign enters twice), while B_1 B_1^T changes only by conjugation with a
diagonal sign matrix, so its spectrum is unchanged.  Both Laplacians are
therefore well defined with arbitrary face orientations.

VALIDATION: McKean-Singer must now give chi(RP^2) = 1, not 2.  A quotient that
returns 1 is a quotient that actually happened; if it returns 2 the identification
silently failed and nothing below means anything."""
import numpy as np, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t121 import icosphere
from opus_t134 import dec, spectra, bumpy

def quotient_antipodal(P,Fc,tol=1e-9):
    """identify antipodal vertices; returns the RP^2 complex"""
    n=len(P); rep={}; keep=[]
    for i in range(n):
        if i in rep: continue
        # find the antipode
        j=int(np.argmin(np.linalg.norm(P+P[i],axis=1)))
        assert np.linalg.norm(P[j]+P[i])<tol, "mesh not antipodally symmetric"
        rep[i]=len(keep); rep[j]=len(keep); keep.append(i)
    Q=np.array([P[i] for i in keep])
    G=set()
    for f in Fc:
        g=tuple(rep[v] for v in f)
        if len(set(g))<3: continue
        key=tuple(sorted(g))
        if key in G: continue
        G.add(key); 
    Gl=[]
    seen=set()
    for f in Fc:
        g=tuple(rep[v] for v in f)
        if len(set(g))<3: continue
        key=tuple(sorted(g))
        if key in seen: continue
        seen.add(key); Gl.append(g)
    return Q,Gl

print("T135  the taste degeneracy on a NON-SPIN space (RP^2)")
print()
P,Fc=icosphere(3)
print(f"   sphere: {len(P)} vertices, {len(Fc)} faces,  chi = {len(P)-(3*len(Fc))//2+len(Fc)}")
for nm,Psrc in (("RP^2 from the ROUND sphere",P),("RP^2 from a BUMPY sphere",None)):
    if Psrc is None:
        # bumpy but ANTIPODALLY SYMMETRIC (even powers only), else the quotient fails
        Pb=np.array([p*(1.0+0.25*(p[2]**2-0.6*p[0]*p[1]+0.3*p[0]**2)) for p in P])
        Psrc=Pb
    Q,G=quotient_antipodal(Psrc,Fc)
    nE=len(set(tuple(sorted((g[a],g[(a+1)%3]))) for g in G for a in range(3)))
    print(f"\n   {nm}: {len(Q)} vertices, {len(G)} faces, {nE} edges,"
          f"  chi = {len(Q)-nE+len(G)}   (RP^2 has chi = 1)")
    l0,l1,l2,area=spectra(Q,G)
    ms=[float(np.sum(np.exp(-t*l0))-np.sum(np.exp(-t*l1))+np.sum(np.exp(-t*l2))) for t in (0.05,0.2,1.0,5.0)]
    print(f"      McKean-Singer at t=0.05,0.2,1,5 -> " + "  ".join(f"{v:.7f}" for v in ms)
          + "   (must be chi = 1)")
    lam=np.sort(np.concatenate([l0,l1,l2])); lam=lam[lam>1e-8]
    print(f"      lowest 12 nonzero Lambda* eigenvalues:")
    print("         " + "  ".join(f"{v:.5f}" for v in lam[:6]))
    print("         " + "  ".join(f"{v:.5f}" for v in lam[6:12]))
    d=np.abs(lam[1:24:2]-lam[0:24:2])/lam[0:24:2]
    print(f"      consecutive-pair relative splitting: max {d.max():.3e}  median {np.median(d):.3e}")
print()
print("   Splitting jumping from 1e-13 to O(1) on the non-spin quotient = topology")
print("   breaks the taste degeneracy, and the framework's arena need not be spin.")
print("   Still 1e-13 = the degeneracy is protected more broadly than by spin structure.")
