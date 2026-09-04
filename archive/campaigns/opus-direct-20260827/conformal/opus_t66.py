"""T66 - THE CONSTRUCTION IN FOUR DIMENSIONS.
Everything from Result 23 onward has been two-dimensional.  Result 25's operator
was written dimension-independently -- cochains on the complex, d the coboundary,
Hodge weights from cell and dual volumes -- so the claim that d=4 is "a compute
question, not a structural one" needs testing rather than asserting.

Build a genuine 4-complex: the 4-torus, Freudenthal/Kuhn-triangulated (each
4-cube cut into 4! = 24 4-simplices by the orderings of the coordinate
increments).  That gives vertices, edges, triangles, tetrahedra and 4-simplices,
all of it mechanical and checkable.

The checks that do not need a full spectrum, and are the structural ones:
  (K1) d_(k+1) o d_k = 0 at EVERY degree -- the complex is a complex in 4D;
  (K2) the alternating cell count gives chi(T^4) = 0;
  (K3) the Betti numbers from ranks:  b_k = dim ker d_k - rank d_(k-1),
       which for T^4 must be (1, 4, 6, 4, 1) -- sum 16.
That last one is the doubler test in four dimensions: Result 24's cell
construction would have carried 2^4 = 16 spurious zero modes PER topological
one; the complex-native operator should carry exactly the Betti sum."""
import numpy as np, itertools
from collections import defaultdict
def kuhn_torus(L,d=4):
    """Freudenthal triangulation of the d-torus with L^d vertices."""
    verts=list(itertools.product(range(L),repeat=d))
    vid={v:i for i,v in enumerate(verts)}
    tops=[]
    for base in verts:
        for perm in itertools.permutations(range(d)):
            chain=[base]; cur=list(base)
            for a in perm:
                cur=list(cur); cur[a]=(cur[a]+1)%L; chain.append(tuple(cur))
            tops.append(tuple(vid[c] for c in chain))
    return verts,vid,tops
def skeleton(tops,d=4):
    """all k-faces of the top simplices, k = 0..d"""
    cells=[dict() for _ in range(d+1)]
    for t in tops:
        for k in range(d+1):
            for f in itertools.combinations(sorted(t),k+1):
                if f not in cells[k]: cells[k][f]=len(cells[k])
    return cells
def coboundary(cells,k):
    """d_k : C^k -> C^(k+1), signed incidence"""
    lo,hi=cells[k],cells[k+1]
    D=np.zeros((len(hi),len(lo)))
    for f,j in hi.items():
        for i_ in range(len(f)):
            face=f[:i_]+f[i_+1:]
            if face in lo: D[j,lo[face]] += (-1)**i_
    return D
for L in (2,3):
    print(f"\n=== 4-torus, L={L}  ({L**4} vertices)")
    verts,vid,tops=kuhn_torus(L)
    cells=skeleton(tops)
    counts=[len(c) for c in cells]
    print(f"   cell counts by degree: {counts}")
    chi=sum(((-1)**k)*counts[k] for k in range(5))
    print(f"   (K2) chi = sum (-1)^k N_k = {chi}   (T^4 requires 0)   "
          f"{'PASS' if chi==0 else 'FAIL'}")
    Ds=[coboundary(cells,k) for k in range(4)]
    ok=True
    for k in range(3):
        m=float(np.max(np.abs(Ds[k+1]@Ds[k])))
        ok &= (m<1e-9)
        print(f"   (K1) max|d_{k+1} d_{k}| = {m:.2e}")
    print(f"        d o d = 0 at every degree: {'PASS' if ok else 'FAIL'}")
    ranks=[int(np.linalg.matrix_rank(D,tol=1e-8)) for D in Ds]
    betti=[]
    for k in range(5):
        dimk=counts[k]
        rk=ranks[k] if k<4 else 0
        rkm1=ranks[k-1] if k>=1 else 0
        betti.append(dimk-rk-rkm1)
    print(f"   ranks of d_0..d_3: {ranks}")
    print(f"   (K3) Betti numbers = {betti}   (T^4 requires [1,4,6,4,1], sum 16)   "
          f"{'PASS' if betti==[1,4,6,4,1] else 'FAIL'}")
    print(f"        total kernel dimension = {sum(betti)}", flush=True)
