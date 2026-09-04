"""T109 - WHAT THE LINEARISED REGGE OPERATOR ACTUALLY IS.
Result 51 found the Regge Hessian is 6-8% away from ANY simple edge-weighted
graph Laplacian, and I guessed the reason: the true linearised operator lives on
HINGES (2-cells), which no weighting of EDGES can reproduce.  That guess is
testable exactly, because at a flat complex every deficit vanishes, so the second
variation of S = sum_h A_h delta_h collapses to

        d^2 S [v]  =  2 * sum_h  (d delta_h[v]) (d A_h[v])

with no  A * d^2 delta  term surviving (delta = 0) and no  delta * d^2 A  term
(delta = 0 again).  That is a HINGE bilinear form, built from the directional
derivatives of the deficit and the area at each hinge.

If the identity holds numerically, the linearised Regge operator IS a hinge
operator, exactly, and the repo's weak-field H = -Delta_lat is its edge-space
shadow -- which is why no edge weighting could match it."""
import numpy as np, itertools
def dihedral(P,tri):
    o=P[tri[0]]; Hs=np.array([P[tri[1]]-o,P[tri[2]]-o]); Q,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Q@(Q.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-12 or nv<1e-12: return None
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
def tri_area(p0,p1,p2):
    a=p1-p0;b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
L=3; d=4; h=1.0/L
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
NV=len(verts)
tops=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        ids=[vid[base]]; cur=list(base); pos=[np.array([b*h for b in base])]
        c=np.array([b*h for b in base])
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
            c=c.copy(); c[a]+=h; pos.append(c.copy())
        tops.append((tuple(ids),np.array(pos)))
edges={}
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        edges.setdefault(tuple(sorted((ids[i],ids[j]))),len(edges))
base_len=np.zeros(len(edges))
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        base_len[edges[tuple(sorted((ids[i],ids[j])))]]=float(np.linalg.norm(P[i]-P[j]))
def geom(phi):
    """conformal perturbation; returns (deficit per hinge, area per hinge, action)"""
    ell=base_len.copy()
    for (u,v),e in edges.items(): ell[e]*=np.exp(0.5*(phi[u]+phi[v]))
    ang={}; area={}
    for ids,P in tops:
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            x=ell[edges[tuple(sorted((ids[i],ids[j])))]]; L2[i][j]=L2[j][i]=x*x
        G=np.zeros((4,4))
        for i in range(4):
            for j in range(4): G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
        w,U=np.linalg.eigh(G)
        if np.any(w<1e-13): return None,None,None
        X=np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a; area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
    keys=sorted(ang.keys())
    defs=np.array([2*np.pi-ang[k] for k in keys])
    ars=np.array([area[k] for k in keys])
    return defs,ars,float(np.sum(ars*defs))
d0,a0,S0=geom(np.zeros(NV))
print(f"T109  Kuhn 4-torus L={L}: {NV} vertices, {len(edges)} edges, {len(d0)} hinges")
print(f"   flat: max|deficit| = {np.max(np.abs(d0)):.2e}, S = {S0:.3e}")
print()
print("   testing   d^2 S[v]  ==  sum_h (d delta_h)(d A_h)   on random directions")
print(f"   {'trial':>6} {'d2S (finite diff)':>19} {'sum (ddelta)(dA)':>21} {'rel diff':>11}")
eps=2e-3; rng=np.random.default_rng(3); rels=[]
for t in range(8):
    v=rng.normal(size=NV); v-=v.mean(); v/=np.linalg.norm(v)
    dp,ap,Sp=geom(eps*v); dm,am,Sm=geom(-eps*v)
    if Sp is None or Sm is None: print(f"   {t:6d}  degenerate"); continue
    lhs=(Sp-2*S0+Sm)/eps**2
    ddel=(dp-dm)/(2*eps); dar=(ap-am)/(2*eps)
    rhs=float(np.sum(ddel*dar))   # NO factor 2: Schlaefli differentiated gives sum A d2delta = -sum (dA)(ddelta)
    rel=abs(lhs-rhs)/max(abs(lhs),1e-12); rels.append(rel)
    print(f"   {t:6d} {lhs:19.8f} {rhs:21.8f} {rel:11.3e}", flush=True)
print()
print(f"   worst relative difference: {max(rels) if rels else float('nan'):.3e}")
print()
print("   agreement means the linearised Regge operator is EXACTLY a hinge bilinear")
print("   form -- the product of the deficit's and the area's response at each")
print("   hinge -- so no weighting of EDGES can reproduce it, which is precisely why")
print("   Result 51 found a 6-8% floor against every edge-Laplacian candidate.")
