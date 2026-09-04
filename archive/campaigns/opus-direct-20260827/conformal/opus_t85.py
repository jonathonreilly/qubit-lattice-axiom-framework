"""T85 - THE LOCAL EINSTEIN EQUATION, verified as an identity.
T84 tried to SOLVE the sourced Regge equation by gradient descent and failed:
with 1215 edges the driving force is nonzero on only the 3 edges of the sourced
hinge, and the Regge action is not bounded below, so descent is the wrong solver.
The more fundamental thing is checkable directly.

Regge's variation, made possible by the Schlaefli identity (T70, verified to
1e-14), is the statement that for EVERY edge

        dS / d(ell_e)  =  sum over hinges h containing e  of  delta_h * dA_h/d(ell_e)

with NO derivative-of-deficit term.  That identity is the local Einstein equation:
the left side is how the action responds to stretching one edge, the right side
is curvature contracted with the geometry, and it involves ONLY the hinges that
touch that edge.  Verifying it establishes that Result 31's field equation is
genuinely LOCAL -- one equation per edge, each seeing only its own neighbourhood.

Measured on a genuinely CURVED complex (random edge lengths), where every deficit
is nonzero, comparing the two sides edge by edge."""
import numpy as np, itertools, math
def realize(L2):
    G=np.zeros((4,4))
    for i in range(4):
        for j in range(4): G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
    w,U=np.linalg.eigh(G)
    if np.any(w<1e-12): return None
    return np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
def dihedral(P,tri):
    o=P[tri[0]]; Hs=np.array([P[tri[1]]-o,P[tri[2]]-o]); Q,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Q@(Q.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-12 or nv<1e-12: return None
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
def tri_area_from_lengths(a,b,c):
    s=(a+b+c)/2.0
    v=s*(s-a)*(s-b)*(s-c)
    return math.sqrt(v) if v>0 else 0.0
L=2; d=4; h=1.0
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
tops=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; cur=list(base)
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
        if len(set(ids))==5: tops.append(tuple(ids))
tops=list(dict.fromkeys(tops))
edges={}
for ids in tops:
    for i,j in itertools.combinations(range(5),2):
        edges.setdefault(tuple(sorted((ids[i],ids[j]))),len(edges))
E=len(edges)
rng=np.random.default_rng(5)
ell=1.0+0.10*rng.random(E)          # genuinely curved: random edge lengths
print(f"T85  4-complex from the L=2 Kuhn torus: {len(tops)} 4-simplices, {E} edges")
def geometry(ell):
    ang={}; area={}
    ok=True
    for ids in tops:
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            e=ell[edges[tuple(sorted((ids[i],ids[j])))]]; L2[i][j]=L2[j][i]=e*e
        X=realize(L2)
        if X is None: ok=False; continue
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a
            ls=[ell[edges[tuple(sorted((ids[tri[x]],ids[tri[y]])))]] for x,y in ((0,1),(1,2),(0,2))]
            area[key]=tri_area_from_lengths(*ls)
    return ang,area,ok
ang,area,ok=geometry(ell)
defs={k:2*np.pi-ang[k] for k in ang}
print(f"     hinges {len(ang)}; all simplices realisable: {ok}")
print(f"     deficits: min {min(defs.values()):+.5f}  max {max(defs.values()):+.5f}  "
      f"(genuinely curved)")
def S_of(ell):
    a,ar,_=geometry(ell)
    return float(sum(ar[k]*(2*np.pi-a[k]) for k in a))
print()
print("   comparing  dS/dl_e  against  sum_h delta_h dA_h/dl_e   for 12 edges")
print(f"   {'edge':>6} {'dS/dl (finite diff)':>21} {'sum delta dA/dl':>18} {'|diff|':>12} {'rel':>10}")
eps=1e-6
worst=0.0
for e in range(0,E,max(1,E//12))[:12]:
    ep=ell.copy(); ep[e]+=eps; em=ell.copy(); em[e]-=eps
    lhs=(S_of(ep)-S_of(em))/(2*eps)
    # right side: deficits held FIXED, only the areas varied
    ap,arp,_=geometry(ep); am,arm,_=geometry(em)
    rhs=float(sum(defs[k]*(arp[k]-arm[k])/(2*eps) for k in defs if k in arp and k in arm))
    dd=abs(lhs-rhs); worst=max(worst,dd/max(abs(lhs),1e-12))
    print(f"   {e:6d} {lhs:21.9f} {rhs:18.9f} {dd:12.3e} {dd/max(abs(lhs),1e-12):10.2e}", flush=True)
print()
print(f"   worst relative discrepancy: {worst:.3e}")
print("   agreement => the derivative-of-deficit term is absent (Schlaefli), so the")
print("   field equation is LOCAL: one equation per edge, each seeing only the")
print("   hinges that touch it.  With a source T_h the equation reads delta_h = T_h.")
