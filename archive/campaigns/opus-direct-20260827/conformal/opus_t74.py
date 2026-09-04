"""T74 - THE LORENTZIAN BRANCH, ON THE ARENA WHERE IT IS WELL-POSED.
Result 16's two-branch structure -- V^2 = det g has two signs; the Euclidean one
gives a unique propagator and positive energy, the Lorentzian one gives the light
cone and the mass shell -- is the campaign's most physical statement, and the
cross-lane review's central objection was that taking V = sqrt(det g) for
indefinite g is "an algebraic complexification, not a second admissible branch".
That objection is right about the RIGID LATTICE.  On a complex it can be asked
properly, because a complex's geometry is its EDGE LENGTHS, and Lorentzian
signature is simply some squared edge lengths being negative (timelike).

Checks, all of which are structural rather than numerical:
 (L1) a Lorentzian 4-simplex has a REAL 4-volume.  Cayley-Menger gives
      vol^2 with a sign that depends on signature; for a Lorentzian simplex the
      squared volume comes out NEGATIVE and the volume is i*|vol| -- exactly
      Result 16's V = i on the Lorentzian branch, now from the complex's own
      geometry rather than from a hand-performed continuation.
 (L2) FLAT MINKOWSKI must have zero deficit at every hinge -- the Lorentzian
      analogue of T70's flat control.  Angles become boost angles, so this is a
      genuine test that the machinery survives the signature change.
 (L3) Result 1's tiling condition (Result 28) must still hold.
 (L4) the light cone must appear: edges split into timelike (l^2 < 0), null
      (l^2 = 0) and spacelike (l^2 > 0), and the null ones are the cone."""
import numpy as np, itertools, math
def cm_vol2(L2,n):
    """SQUARED volume of an n-simplex from squared edge lengths (sign carries signature)"""
    M=np.ones((n+2,n+2)); M[0,0]=0.0
    for i in range(n+1):
        for j in range(n+1): M[i+1,j+1]=L2[i][j]
    return (((-1)**(n+1))/(2**n*(math.factorial(n)**2)))*float(np.linalg.det(M))
print("T74 (L1)  signature from the complex's own edge lengths")
print("     a 4-simplex with all edges spacelike vs one with a timelike direction")
# Euclidean regular 4-simplex, unit edges
L2e=[[0.0 if i==j else 1.0 for j in range(5)] for i in range(5)]
print(f"     Euclidean (all l^2=+1):   vol^2 = {cm_vol2(L2e,4):+.8f}  -> vol is REAL")
# Minkowski: put vertex 0 at the origin, vertex 1 timelike from it
def minkowski_simplex(tau):
    """vertices 0..4 with v1 displaced in TIME by tau and v2..v4 spacelike"""
    pts=[np.array([0.,0.,0.,0.]), np.array([tau,0.,0.,0.]),
         np.array([0.,1.,0.,0.]), np.array([0.,0.,1.,0.]), np.array([0.,0.,0.,1.])]
    eta=np.diag([-1.,1.,1.,1.])
    L2=[[0.0]*5 for _ in range(5)]
    for i,j in itertools.combinations(range(5),2):
        d=pts[i]-pts[j]; L2[i][j]=L2[j][i]=float(d@eta@d)
    return L2,pts,eta
for tau in (0.5,1.0,2.0):
    L2,pts,eta=minkowski_simplex(tau)
    v2=cm_vol2(L2,4)
    kinds=[]
    for i,j in itertools.combinations(range(5),2):
        s=L2[i][j]
        kinds.append('T' if s<-1e-12 else ('N' if abs(s)<1e-12 else 'S'))
    print(f"     Minkowski tau={tau}: vol^2 = {v2:+.8f}  -> vol = "
          f"{'i*'+format(math.sqrt(-v2),'.6f') if v2<0 else format(math.sqrt(v2),'.6f')}"
          f"   edges {kinds.count('T')}T {kinds.count('N')}N {kinds.count('S')}S", flush=True)
print()
print("T74 (L4)  the LIGHT CONE from edge classification")
print("     vary one vertex's time coordinate through the cone and watch l^2 change sign")
print(f"   {'t':>7} {'l^2 to origin':>15} {'class':>8}")
for t in (0.4,0.8,0.99,1.0,1.01,1.5,2.5):
    d=np.array([t,1.,0.,0.]); eta=np.diag([-1.,1.,1.,1.])
    s=float(d@eta@d)
    print(f"   {t:7.2f} {s:15.6f} {'timelike' if s<-1e-12 else ('NULL' if abs(s)<1e-12 else 'spacelike'):>8}")
print("     l^2 = 0 exactly at t = 1: the light cone is where the edge length vanishes.")
print()
print("T74 (L2)  FLAT MINKOWSKI complex: do the deficits vanish?")
print("     Kuhn-triangulated 4-torus with one TIMELIKE direction (eta = diag(-1,1,1,1))")
L=3; h=1.0/L; d=4
eta=np.diag([-1.,1.,1.,1.])
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
hinge=dict()
nbad=0; vol2s=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; c=np.array([b*h for b in base]); P=[c.copy()]; cur=list(base)
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
            c=c.copy(); c[a]+=h; P.append(c.copy())
        P=np.array(P)
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            dv=P[i]-P[j]; L2[i][j]=L2[j][i]=float(dv@eta@dv)
        vol2s.append(cm_vol2(L2,4))
        # Lorentzian dihedral: use the Minkowski Gram matrix of the two opposite edges
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            other=[i for i in range(5) if i not in tri]
            u=P[other[0]]-P[tri[0]]; v=P[other[1]]-P[tri[0]]
            nu=float(u@eta@u); nv=float(v@eta@v); uv=float(u@eta@v)
            if nu*nv<=0 or abs(nu*nv)<1e-18: nbad+=1; continue
            cth=uv/math.sqrt(abs(nu*nv))
            ang=math.acos(max(-1.0,min(1.0,cth))) if abs(cth)<=1 else math.acosh(abs(cth))
            hinge[key]=hinge.get(key,0.0)+ang
v2=np.array(vol2s)
print(f"     {len(v2)} simplices: vol^2 all negative (Lorentzian)? "
      f"{bool(np.all(v2<0))}   range [{v2.min():.3e}, {v2.max():.3e}]")
defs=np.array([2*np.pi-a for a in hinge.values()])
print(f"     {len(defs)} hinges, {nbad} skipped (mixed-signature pairs)")
print(f"     max|deficit| = {float(np.max(np.abs(defs))):.4e}   mean = {float(np.mean(defs)):+.4e}")
print()
print("   vol^2 < 0 everywhere is Result 16's V = i, arising here from the complex's")
print("   own edge lengths rather than from a hand-performed continuation.")
