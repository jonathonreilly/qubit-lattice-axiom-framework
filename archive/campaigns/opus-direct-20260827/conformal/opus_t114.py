"""T114 - DOES THE FRAMEWORK HAVE A GRAVITON?  The transverse-traceless sector.
Results 60/63 settled the CONFORMAL sector: the Regge action's conformal second
variation is the continuum one, with S = (1/2) int R sqrt(g).  But the conformal
mode is NOT the graviton -- it is a gauge/constraint mode.  The physical graviton
is the TRANSVERSE-TRACELESS perturbation, and whether the framework propagates one
is a different and more important question.

In the continuum, linearised gravity about flat space gives for a TT perturbation
h_ij(x) = e_ij cos(k.x), with e traceless and transverse (e_ij k_j = 0):
      d^2 S_EH  ~  (1/2) k^2 |e|^2 * Volume        (up to the overall normalisation)
i.e. the second variation grows as k^2 -- that IS the graviton kinetic term, and
its positivity is what makes gravitational waves propagate with positive energy.

Test: perturb the EDGE LENGTHS of the Kuhn 4-torus by a TT plane wave and measure
d^2 S_Regge as a function of k.  A metric perturbation h_ab enters an edge in
direction u as  ell -> ell * (1 + (1/2) u^a u^b h_ab).
  * d^2 S growing as k^2 with a POSITIVE coefficient  =>  a propagating graviton
    with positive energy.
  * flat in k, or negative  =>  no propagating graviton in this sector."""
import numpy as np, itertools, math
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
def build(L):
    d=4; h=1.0/L
    verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
    tops=[]
    for base in verts:
        for perm in itertools.permutations(range(d)):
            ids=[vid[base]]; cur=list(base); pos=[np.array([b*h for b in base])]
            c=np.array([b*h for b in base])
            for a in perm:
                cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
                c=c.copy(); c[a]+=h; pos.append(c.copy())
            tops.append((tuple(ids),np.array(pos)))
    edges={}; emid={}; edir={}
    for ids,P in tops:
        for i,j in itertools.combinations(range(5),2):
            key=tuple(sorted((ids[i],ids[j])))
            if key not in edges:
                edges[key]=len(edges); emid[key]=0.5*(P[i]+P[j]); edir[key]=P[j]-P[i]
    base_len=np.zeros(len(edges))
    for k,e in edges.items(): base_len[e]=float(np.linalg.norm(edir[k]))
    return verts,vid,tops,edges,emid,edir,base_len
def S_of(tops,edges,ell):
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
print("T114  the TRANSVERSE-TRACELESS (graviton) sector of the Regge action")
print("      h_ab = e_ab cos(k.x), e traceless and transverse to k")
for L in (3,4):
    verts,vid,tops,edges,emid,edir,base_len=build(L)
    S0=S_of(tops,edges,base_len)
    print(f"\n   L={L}: {len(verts)} vertices, {len(edges)} edges, S(flat)={S0:.2e}")
    print(f"   {'n (k=2pi n/L)':>14} {'k^2':>10} {'d2S':>15} {'d2S / k^2':>13}")
    kdir=np.array([1.0,0.0,0.0,0.0])
    e_pol=np.zeros((4,4)); e_pol[1,2]=e_pol[2,1]=1.0      # TT: traceless, transverse to k=x0
    for n in range(1,L//2+1):
        kv=2*np.pi*n*kdir
        k2=float(kv@kv)
        def ell_of(eps):
            ell=base_len.copy()
            for key,e in edges.items():
                u=edir[key]; nu=np.linalg.norm(u); uh=u/nu
                hab=eps*np.cos(float(kv@emid[key]))*e_pol
                ell[e]=nu*(1.0+0.5*float(uh@hab@uh))
            return ell
        eps=1e-3
        Sp=S_of(tops,edges,ell_of(eps)); Sm=S_of(tops,edges,ell_of(-eps))
        if Sp is None or Sm is None:
            print(f"   {n:14d}  degenerate"); continue
        d2=(Sp-2*S0+Sm)/eps**2
        print(f"   {n:14d} {k2:10.3f} {d2:15.6f} {d2/k2:13.6f}", flush=True)
print()
print("   d2S growing with k^2 and POSITIVE => the framework propagates a graviton")
print("   with positive energy.  Flat in k, or negative => it does not.")
print("   (transversality check: e_12 with k along x0 is exactly transverse)")
