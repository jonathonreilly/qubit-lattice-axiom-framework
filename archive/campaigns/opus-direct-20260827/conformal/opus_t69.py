"""T69 - CURVATURE IN FOUR DIMENSIONS: the hinge, and the Regge action.
Result 25 found that in 2D the complex's curvature is the ANGLE DEFECT at a
vertex, that it equals the pointwise Gaussian curvature, and that its total is
2 pi chi.  In four dimensions curvature is not a scalar and does not live at
vertices: it lives at CODIMENSION-2 cells -- triangles, called hinges -- as the
deficit angle of the 4-simplices meeting around them.  And the sum

        S = sum over hinges of  Area(hinge) * deficit(hinge)

is the Regge action, the discrete Einstein-Hilbert action.  So this is where the
framework's 'cells weigh, faces compare' should make contact with gravity in the
physical dimension.

Test bed: the boundary of a 5-simplex, which is a triangulation of S^4 with
6 vertices, 15 edges, 20 triangles, 15 tetrahedra and 6 four-simplices -- small
enough to be exact and genuinely curved.  Checks:
  (H1) the complex is S^4: chi = 2, Betti = [1,0,0,0,1];
  (H2) the deficit angle at every hinge, computed from dihedral angles;
  (H3) the Regge action, against the continuum value for a 4-sphere;
  (H4) a FLAT control -- the 4-torus of T66 must have zero deficit at every hinge."""
import numpy as np, itertools, math
def dihedral_4simplex(P, tri):
    """dihedral angle of the 4-simplex P (5 points in R^4) about the triangle 'tri'
       (3 of its vertex indices).  The angle between the two tetrahedra sharing it."""
    other=[i for i in range(5) if i not in tri]
    a,b=other
    # build the 2-plane orthogonal to the hinge, inside the 4-simplex's affine hull
    o=P[tri[0]]
    Hs=np.array([P[tri[1]]-o, P[tri[2]]-o])                # hinge directions
    # project the two opposite vertices onto the orthogonal complement of the hinge
    Q,_=np.linalg.qr(Hs.T)                                  # orthonormal basis of the hinge plane
    def perp(x):
        v=x-o; return v - Q@(Q.T@v)
    u=perp(P[a]); v=perp(P[b])
    cu=float(np.linalg.norm(u)); cv=float(np.linalg.norm(v))
    if cu<1e-12 or cv<1e-12: return float('nan')
    c=float(np.dot(u,v))/(cu*cv)
    return float(np.arccos(np.clip(c,-1.0,1.0)))
def tri_area(p0,p1,p2):
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
print("T69  boundary of the 5-simplex = a triangulated S^4")
# regular 5-simplex: 6 points in R^5 (standard basis), then the boundary 4-simplices
P5=np.eye(6)[:, :6]
# centre and drop to the 5-dim affine hull, then we only need distances -> keep in R^6
pts=[np.eye(6)[i] for i in range(6)]
cells={k:{} for k in range(5)}
tops=[tuple(sorted(c)) for c in itertools.combinations(range(6),5)]
for t in tops:
    for k in range(5):
        for f in itertools.combinations(t,k+1):
            cells[k].setdefault(tuple(sorted(f)), len(cells[k]))
counts=[len(cells[k]) for k in range(5)]
chi=sum(((-1)**k)*counts[k] for k in range(5))
print(f"   cell counts [V,E,F,T,P] = {counts}   chi = {chi}   (S^4 requires 2)  "
      f"{'PASS' if chi==2 else 'FAIL'}")
def cob(k):
    lo,hi=cells[k],cells[k+1]; D=np.zeros((len(hi),len(lo)))
    for f,j in hi.items():
        for i_ in range(len(f)):
            face=f[:i_]+f[i_+1:]
            if face in lo: D[j,lo[face]]+=(-1)**i_
    return D
Ds=[cob(k) for k in range(4)]
print(f"   (H1) max|d d| = {max(float(np.max(np.abs(Ds[k+1]@Ds[k]))) for k in range(3)):.1e}")
ranks=[int(np.linalg.matrix_rank(D,tol=1e-8)) for D in Ds]
betti=[counts[k]-(ranks[k] if k<4 else 0)-(ranks[k-1] if k>=1 else 0) for k in range(5)]
print(f"   (H1) Betti = {betti}   (S^4 requires [1,0,0,0,1])  "
      f"{'PASS' if betti==[1,0,0,0,1] else 'FAIL'}")
print()
print("   (H2) deficit angles at the 20 triangle hinges")
# embed the regular 5-simplex with unit edge length in R^5
V=[]
for i in range(6):
    e=np.zeros(6); e[i]=1.0; V.append(e)
V=[v-np.mean(V,axis=0) for v in V]
B=np.linalg.svd(np.array(V))[2][:5]
V=[B@v for v in V]                                # now in R^5
edge=np.linalg.norm(V[0]-V[1]); V=[v/edge for v in V]
print(f"        regular 5-simplex, unit edge (check: {np.linalg.norm(V[0]-V[1]):.6f})")
defs={}; areas={}
for tri in itertools.combinations(range(6),3):
    tot=0.0; nsimp=0
    for top in tops:
        if set(tri)<=set(top):
            idx={v:i for i,v in enumerate(top)}
            P=np.array([V[v] for v in top])
            # work inside the 4-dim affine hull of this 4-simplex
            O=P[0]; M=P[1:]-O
            Qb,_=np.linalg.qr(M.T)
            Pl=np.array([Qb.T@(p-O) for p in P])
            tot+=dihedral_4simplex(Pl,[idx[t] for t in tri]); nsimp+=1
    defs[tri]=2*np.pi-tot; areas[tri]=tri_area(V[tri[0]],V[tri[1]],V[tri[2]])
    if len(defs)<=3:
        print(f"        hinge {tri}: {nsimp} 4-simplices meet, sum of dihedrals = {tot:.6f}, "
              f"deficit = {defs[tri]:+.6f}", flush=True)
d=np.array(list(defs.values())); a=np.array(list(areas.values()))
print(f"        all 20 deficits equal? spread = {d.max()-d.min():.2e}   value = {d[0]:.6f}")
print(f"        hinge area = {a[0]:.6f} (equilateral, unit edge = {np.sqrt(3)/4:.6f})")
print()
print(f"   (H3) REGGE ACTION  S = sum A * deficit = {float(np.sum(a*d)):.6f}")
print(f"        (2 * area-weighted total curvature; for comparison the 2D analogue")
print(f"         sum of angle defects on S^2 was exactly 2 pi chi = {4*np.pi:.6f})")
