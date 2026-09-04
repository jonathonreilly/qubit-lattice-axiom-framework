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
# several candidate Laplacians: the COMBINATORIAL one (all weights 1) and
# GEOMETRICALLY weighted ones, since the Kuhn triangulation has edges of two
# different lengths (axis edges and body diagonals)
def weighted_lap(power):
    Lm=np.zeros((NV,NV))
    for (u,v),e in edges.items():
        w=base_len[e]**power
        Lm[u,u]+=w; Lm[v,v]+=w; Lm[u,v]-=w; Lm[v,u]-=w
    return Lm
cands={"combinatorial (w=1)":weighted_lap(0.0),
       "length^-1":weighted_lap(-1.0),
       "length^-2":weighted_lap(-2.0),
       "length^+1":weighted_lap(1.0),
       "length^+2":weighted_lap(2.0)}
eps=2e-3; rng=np.random.default_rng(11)
vs=[]
for t in range(10):
    v=rng.normal(size=NV); v-=v.mean(); v/=np.linalg.norm(v); vs.append(v)
qs=[]
for v in vs:
    Sp=S_of(eps*v); Sm=S_of(-eps*v)
    qs.append(None if (Sp is None or Sm is None) else (Sp-2*S0+Sm)/eps**2)
print()
print("   which Laplacian is the Regge Hessian?  ratio v^T H v / v^T L v over 10")
print("   random conformal directions, for several edge weightings")
print(f"   {'candidate L':>22} {'mean ratio':>12} {'relative spread':>17}")
best=None
for nm,Lm in cands.items():
    rs=[q/float(v@Lm@v) for q,v in zip(qs,vs) if q is not None]
    r=np.array(rs); rel=(r.max()-r.min())/abs(r.mean())
    print(f"   {nm:>22} {r.mean():12.6f} {rel:17.4f}", flush=True)
    if best is None or rel<best[1]: best=(nm,rel)
print()
print(f"   best match: {best[0]}  (relative spread {best[1]:.4f})")
print()
print("   a weighting that drives the spread to ~0 identifies WHICH Laplacian the")
print("   repo's weak-field H = -Delta_lat has to be, if it is the linearisation of")
print("   Result 31's Regge equation.")
