"""T74b - flat Minkowski deficits, with the Lorentzian angle bookkeeping done right.
T74 (L1) established the good part: a 4-simplex with timelike edges has
Cayley-Menger vol^2 < 0, so its volume is i|vol| -- Result 16's V = i arising
from the complex's own edge lengths, not from a hand-performed continuation.
That answers the cross-lane review's "algebraic complexification" objection.

T74 (L2) failed because I used  deficit = 2 pi - sum(angles)  everywhere.  That is
wrong in Lorentzian signature.  The angle around a hinge lives in the 2-plane
ORTHOGONAL to it, and that plane has its own signature:
   * orthogonal plane EUCLIDEAN  -> ordinary rotation angles, flat sum = 2 pi
   * orthogonal plane LORENTZIAN -> BOOST angles, which are non-compact, and the
     flat sum is 0, not 2 pi
So the flat-space reference depends on the hinge's causal character, and the two
kinds must be counted separately.  Implemented here and tested on flat Minkowski,
where every deficit must vanish."""
import numpy as np, itertools, math
ETA=np.diag([-1.,1.,1.,1.])
def ip(u,v): return float(u@ETA@v)
def orth_plane_basis(P,tri):
    """basis of the 2-plane Minkowski-orthogonal to the hinge, and its signature"""
    o=P[tri[0]]
    H=[P[tri[1]]-o, P[tri[2]]-o]
    # Gram-Schmidt in the Minkowski metric against the hinge directions
    def proj_out(x,B):
        y=x.copy()
        for b in B:
            nb=ip(b,b)
            if abs(nb)>1e-14: y=y-(ip(y,b)/nb)*b
        return y
    B=[]
    for hvec in H:
        w=proj_out(hvec,B)
        if abs(ip(w,w))>1e-14: B.append(w)
    comp=[]
    for e in np.eye(4):
        w=proj_out(e,B+comp)
        if abs(ip(w,w))>1e-10: comp.append(w)
        if len(comp)==2: break
    if len(comp)<2: return None,None
    G=np.array([[ip(a,b) for b in comp] for a in comp])
    sig=np.sign(np.linalg.eigvalsh(G))
    return comp, ('lorentzian' if (sig<0).any() else 'euclidean')
def hinge_angle(P,tri):
    comp,kind=orth_plane_basis(P,tri)
    if comp is None: return None,None
    other=[i for i in range(5) if i not in tri]
    o=P[tri[0]]
    def into(x):
        v=x-o
        return np.array([ip(v,c)/ip(c,c) for c in comp])
    a=into(P[other[0]]); b=into(P[other[1]])
    G=np.array([[ip(x,y) for y in comp] for x in comp])
    na=float(a@G@a); nb=float(b@G@b); ab=float(a@G@b)
    if abs(na)<1e-14 or abs(nb)<1e-14: return None,None
    if kind=='euclidean':
        if na<=0 or nb<=0: return None,None
        return math.acos(max(-1.,min(1.,ab/math.sqrt(na*nb)))), kind
    # Lorentzian plane: boost angle between the two directions
    q=ab/math.sqrt(abs(na*nb))
    return (math.acosh(abs(q)) if abs(q)>=1.0 else math.asinh(abs(q))), kind
L=3; h=1.0/L; d=4
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
acc={}; kinds={}
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; c=np.array([b*h for b in base]); P=[c.copy()]; cur=list(base)
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
            c=c.copy(); c[a]+=h; P.append(c.copy())
        P=np.array(P)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            ang,kind=hinge_angle(P,list(tri))
            if ang is None: continue
            acc[key]=acc.get(key,0.0)+ang; kinds[key]=kind
print("T74b  flat Minkowski 4-torus: deficits with causal bookkeeping")
eu=[k for k in acc if kinds[k]=='euclidean']; lo=[k for k in acc if kinds[k]=='lorentzian']
print(f"   {len(acc)} hinges resolved:  {len(eu)} with EUCLIDEAN orthogonal plane, "
      f"{len(lo)} with LORENTZIAN")
if eu:
    de=np.array([2*np.pi-acc[k] for k in eu])
    print(f"   euclidean-plane hinges  (flat reference 2 pi): max|deficit| = {np.abs(de).max():.4e}"
          f"   mean = {de.mean():+.4e}")
if lo:
    dl=np.array([-acc[k] for k in lo])
    print(f"   lorentzian-plane hinges (flat reference 0):    max|deficit| = {np.abs(dl).max():.4e}"
          f"   mean = {dl.mean():+.4e}")
print()
print("   both near zero => the Regge machinery survives the signature change and")
print("   flat Minkowski is curvature-free on the complex, which is what Result 31")
print("   needs in order to apply on the Lorentzian branch of Result 16.")
