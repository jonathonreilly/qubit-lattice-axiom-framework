"""T72 - does the Regge action CONVERGE to the continuum Einstein-Hilbert integral?
T71 showed the field equation on the framework's complex has content and selects
a size.  But the S^4 used there was the boundary of a single 5-simplex -- six
vertices, as coarse as a 4-sphere can be.  For the identification 'Regge action =
Einstein-Hilbert action' to be quantitative rather than structural, the action
has to converge under refinement.

Refined S^4 triangulations: take N points on the unit 4-sphere in R^5 and form
their convex hull.  Its facets are 4-simplices, and the hull IS a triangulation
of S^4.  For the unit round S^4:
      R = 12,  Vol = 8 pi^2 / 3 = 26.3189,  so  int R sqrt(g) = 315.827
and the Regge action sum_h A_h delta_h should approach that (up to the standard
factor of 2 between conventions, which is what the measured ratio will show)."""
import numpy as np, itertools, math
from scipy.spatial import ConvexHull
def qr_hull(P):
    O=P[0]; M=P[1:]-O; Q,_=np.linalg.qr(M.T)
    return np.array([Q.T@(p-O) for p in P])
def dihedral(P,tri):
    o=P[tri[0]]; Hs=np.array([P[tri[1]]-o,P[tri[2]]-o]); Q,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Q@(Q.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-13 or nv<1e-13: return None
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
def tri_area(p0,p1,p2):
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
def sphere_points(N,seed,relax=120):
    """random points RELAXED by mutual repulsion -- random hull points approximate
       S^4 badly, and the volume deficit was the dominant error in the first run"""
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(N,5)); X/=np.linalg.norm(X,axis=1,keepdims=True)
    for _ in range(relax):
        D=X[:,None,:]-X[None,:,:]
        d2=np.sum(D*D,axis=2)+np.eye(N)*1e9
        Fv=np.sum(D/ (d2[:,:,None]**1.5), axis=1)
        X=X+0.02*Fv/ (np.linalg.norm(Fv,axis=1,keepdims=True)+1e-12)
        X/=np.linalg.norm(X,axis=1,keepdims=True)
    return X
EXACT_INT_R = 12.0*(8*np.pi**2/3.0)
print(f"T72  unit S^4:  R = 12, Vol = {8*np.pi**2/3:.5f}, int R sqrt(g) = {EXACT_INT_R:.4f}")
print()
print(f"   {'N pts':>7} {'facets':>8} {'hinges':>8} {'sum A*delta':>14} {'vol':>10} "
      f"{'S/intR':>10} {'mean deficit':>13}")
for N in (40,80,150,260,420,650):
    P=sphere_points(N,5)
    try: hull=ConvexHull(P)
    except Exception as ex:
        print(f"   {N:7d}  hull failed: {ex}"); continue
    facets=[tuple(sorted(s)) for s in hull.simplices]
    ang={}; area={}; vol=0.0
    for f in facets:
        Pf=np.array([P[i] for i in f]); Pl=qr_hull(Pf)
        M=Pl[1:]-Pl[0]; vol+=abs(float(np.linalg.det(M)))/math.factorial(4)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([f[i] for i in tri]))
            a=dihedral(Pl,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a
            area[key]=tri_area(Pf[tri[0]],Pf[tri[1]],Pf[tri[2]])
    Sreg=float(sum(area[k]*(2*np.pi-ang[k]) for k in ang))
    md=float(np.mean([2*np.pi-v for v in ang.values()]))
    print(f"   {N:7d} {len(facets):8d} {len(ang):8d} {Sreg:14.4f} {vol:10.4f} "
          f"{Sreg/EXACT_INT_R:10.4f} {md:13.6f}   S/vol = {Sreg/vol:8.4f}  (want 6 if S=intR/2)", flush=True)
print()
print("   S/intR settling on a constant (1/2 or 1) as N grows  =>  the Regge action on")
print("   the framework's complex IS the Einstein-Hilbert action, quantitatively.")
print("   vol should approach the polytope volume, below 26.3189 (inscribed).")
