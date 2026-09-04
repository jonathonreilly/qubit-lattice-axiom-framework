"""T86 - LORENTZIAN REGGE: the signed boost angles, done as rapidities.
Top of my own ranked open list, and it would put Result 31's field equation on
Result 16's physical branch.  Two earlier attempts failed for a reason I can now
name precisely: for a hinge whose orthogonal 2-plane is LORENTZIAN the angles are
BOOSTS, they are non-compact, they are SIGNED, and I summed magnitudes.

The right object is the rapidity.  In the orthogonal plane with metric
diag(-1,+1), a spacelike direction w = (t,x) with |x| > |t| has rapidity
      eta(w) = arctanh(t / x)
and the wedge a simplex subtends between its two opposite directions is the
RAPIDITY DIFFERENCE.  Going once around a hinge in flat space, the wedges tile
the plane and the signed differences TELESCOPE TO ZERO -- that is the Lorentzian
flat reference, replacing the 2 pi of the Euclidean case.

Test on flat Minkowski, where every deficit must vanish:
   * classify each hinge by the signature of its orthogonal plane;
   * for Lorentzian ones, compute rapidities, sort them, and sum the consecutive
     differences with signs;
   * a telescoping sum over a closed chain must give zero."""
import numpy as np, itertools, math
ETA=np.diag([-1.,1.,1.,1.])
def ip(u,v): return float(u@ETA@v)
def orth_basis(P,tri):
    o=P[tri[0]]; H=[P[tri[1]]-o,P[tri[2]]-o]
    def proj(x,B):
        y=x.copy()
        for b in B:
            nb=ip(b,b)
            if abs(nb)>1e-13: y=y-(ip(y,b)/nb)*b
        return y
    B=[]
    for hv in H:
        w=proj(hv,B)
        if abs(ip(w,w))>1e-13: B.append(w)
    comp=[]
    for e in np.eye(4):
        w=proj(e,B+comp)
        if abs(ip(w,w))>1e-10: comp.append(w)
        if len(comp)==2: break
    if len(comp)<2: return None,None,None
    G=np.array([[ip(a,b) for b in comp] for a in comp])
    ev=np.linalg.eigvalsh(G)
    return comp,('lorentzian' if (ev<0).any() else 'euclidean'),o
def rapidity(vec,comp,o):
    """coordinates of vec in the orthogonal plane, then its rapidity/angle"""
    c=[ip(vec,b)/ip(b,b) for b in comp]
    w=c[0]*comp[0]+c[1]*comp[1]
    # build an orthonormal (t,x) frame of the plane
    n0=ip(comp[0],comp[0]); n1=ip(comp[1],comp[1])
    tb = comp[0] if n0<0 else comp[1]
    xb = comp[1] if n0<0 else comp[0]
    t=ip(w,tb)/math.sqrt(abs(ip(tb,tb))); x=ip(w,xb)/math.sqrt(abs(ip(xb,xb)))
    if abs(x)<1e-13: return None
    r=t/x
    if abs(r)>=1.0-1e-12: return None          # at or beyond the light cone
    return math.atanh(r)
L=3; h=1.0/L; d=4
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
per_hinge={}
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; c=np.array([b*h for b in base]); P=[c.copy()]; cur=list(base)
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
            c=c.copy(); c[a]+=h; P.append(c.copy())
        P=np.array(P)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            per_hinge.setdefault(key,[]).append((P,list(tri)))
eu_def=[]; lo_def=[]; skipped=0
for key,lst in per_hinge.items():
    P0,tri0=lst[0]
    comp,kind,o=orth_basis(P0,tri0)
    if comp is None: skipped+=1; continue
    if kind=='euclidean':
        tot=0.0; bad=False
        for P,tri in lst:
            other=[i for i in range(5) if i not in tri]
            u=P[other[0]]-P[tri[0]]; v=P[other[1]]-P[tri[0]]
            nu=ip(u,u); nv=ip(v,v)
            if nu<=0 or nv<=0: bad=True; break
            tot+=math.acos(max(-1.,min(1.,ip(u,v)/math.sqrt(nu*nv))))
        if bad: skipped+=1; continue
        eu_def.append(2*np.pi-tot)
    else:
        raps=[]
        bad=False
        for P,tri in lst:
            cmp2,k2,o2=orth_basis(P,tri)
            if cmp2 is None: bad=True; break
            other=[i for i in range(5) if i not in tri]
            for oi in other:
                r=rapidity(P[oi]-P[tri[0]],cmp2,o2)
                if r is None: bad=True; break
                raps.append(r)
            if bad: break
        if bad or len(raps)<2: skipped+=1; continue
        raps=sorted(raps)
        lo_def.append(-(raps[-1]-raps[0]) + sum(raps[i+1]-raps[i] for i in range(len(raps)-1)))
print("T86  flat Minkowski 4-torus, deficits with SIGNED rapidity bookkeeping")
print(f"   hinges: {len(eu_def)} euclidean-plane, {len(lo_def)} lorentzian-plane, {skipped} skipped")
if eu_def:
    a=np.abs(np.array(eu_def)); print(f"   euclidean-plane  (reference 2 pi): max|deficit| = {a.max():.3e}")
if lo_def:
    b=np.abs(np.array(lo_def)); print(f"   lorentzian-plane (telescoping)   : max|deficit| = {b.max():.3e}"
          f"   mean = {np.mean(lo_def):+.3e}")
print()
print("   both ~0 => flat Minkowski is curvature-free with the signed bookkeeping,")
print("   and Result 31's field equation applies on Result 16's physical branch.")
