"""T106 - DOES THE REGGE FIELD EQUATION REDUCE TO THE REPO'S WEAK-FIELD BRIDGE?
docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11
builds the gravity chain on a WEAK-FIELD Z^3 graph-Laplacian surface:

     H = -Delta_lat ,   G0 = H^{-1}  on the zero-mode-removed sector
     A[phi; rho] = (1/2)<phi, H phi> - <P0 rho, phi>   ->   H phi = P0 rho

That is a linear Poisson bridge.  This campaign built a FULL NONLINEAR field
equation on the framework's complex (Results 31, 37): the Regge action, with
flat space stationary and the local form dS/dl_e = sum_h delta_h dA_h/dl_e.

If the two are the same theory, the Regge action's SECOND VARIATION at the flat
complex -- its Hessian in the edge lengths -- must be a graph Laplacian, i.e. the
repo's H.  Then their bridge is the linearisation of this campaign's equation,
and this campaign supplies the nonlinear completion of their chain.

Measured: the Hessian of S_Regge at flat, restricted to a conformal (single
scalar per vertex) perturbation, against the graph Laplacian of the same complex.
Compared by (i) proportionality, (ii) matching kernels, (iii) matching spectra
after scaling."""
import numpy as np, itertools, math
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
print(f"T106  Kuhn 4-torus L={L}: {NV} vertices, {len(edges)} edges, {len(tops)} 4-simplices")
def S_of(phi):
    """conformal perturbation: edge (u,v) scaled by exp((phi_u+phi_v)/2)"""
    ell=base_len.copy()
    for (u,v),e in edges.items():
        ell[e]*=np.exp(0.5*(phi[u]+phi[v]))
    ang={}; area={}
    for ids,P in tops:
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            x=ell[edges[tuple(sorted((ids[i],ids[j])))]]; L2[i][j]=L2[j][i]=x*x
        G=np.zeros((4,4))
        for i in range(4):
            for j in range(4): G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
        w,U=np.linalg.eigh(G)
        if np.any(w<1e-13): return None
        X=np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a; area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
    return float(sum(area[k]*(2*np.pi-ang[k]) for k in ang))
S0=S_of(np.zeros(NV))
print(f"   S(flat) = {S0:.3e}")
lap=np.zeros((NV,NV))
for (u,v) in edges:
    lap[u,u]+=1; lap[v,v]+=1; lap[u,v]-=1; lap[v,u]-=1
print()
print("   quadratic form v^T H v of the Regge action against v^T L v of the graph")
print("   Laplacian, on random conformal directions (cheap: 3 evaluations per vector)")
print(f"   {'trial':>6} {'v^T H v':>16} {'v^T L v':>14} {'ratio':>12}")
eps=2e-3; rng=np.random.default_rng(11); ratios=[]
for t in range(10):
    v=rng.normal(size=NV); v-=v.mean(); v/=np.linalg.norm(v)
    Sp=S_of(eps*v); Sm=S_of(-eps*v)
    if Sp is None or Sm is None:
        print(f"   {t:6d}   degenerate"); continue
    q=(Sp-2*S0+Sm)/eps**2
    ql=float(v@lap@v)
    ratios.append(q/ql)
    print(f"   {t:6d} {q:16.6f} {ql:14.6f} {q/ql:12.6f}", flush=True)
r=np.array(ratios)
print()
print(f"   ratio: mean {r.mean():.6f}   spread {r.max()-r.min():.3e}   "
      f"relative spread {(r.max()-r.min())/abs(r.mean()):.4f}")
print()
print("   a CONSTANT ratio across random directions means the Regge action's second")
print("   variation IS the graph Laplacian up to one constant -- i.e. the repo's")
print("   weak-field bridge H = -Delta_lat is the linearisation of Result 31's")
print("   equation, and this campaign supplies its nonlinear completion.")
print("   A varying ratio means the Hessian has structure the graph Laplacian lacks.")
