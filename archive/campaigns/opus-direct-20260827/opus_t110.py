"""T110 - DOES MATTER SOURCE THE GEOMETRY THROUGH THE EXACT LINEARISED OPERATOR?
Result 53 gives the linearised gravitational operator in closed form:
     d^2 S[v] = sum_h (d delta_h[v]) (d A_h[v]).
That makes the matter/gravity question sharp for the first time.  The sourced
equation is
     (linearised operator) phi  =  source
and the physical content is whether a matter distribution produces a geometry
response with the right STRUCTURE: localised near the source, falling off with
distance, and linear in the source strength.

Result 17 measured exactly this on the RIGID LATTICE and its gravitational
reading had to be withdrawn (Results 19-22) because that arena was not
diffeomorphism invariant.  The Regge arena is (Result 31: it depends only on edge
lengths, so there are no coordinates to fail to be invariant under).  So the
Result 17 measurement is worth redoing HERE, where it can mean something.

Method: build the linearised operator explicitly in the conformal sector as the
matrix  H_ij = sum_h (d delta_h/d phi_i)(d A_h/d phi_j)  symmetrised, solve
H phi = rho for a point source rho, and measure the response profile against
lattice distance."""
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
def hinge_data(phi):
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
        if np.any(w<1e-13): return None,None
        X=np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a; area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
    keys=sorted(ang.keys())
    return np.array([2*np.pi-ang[k] for k in keys]), np.array([area[k] for k in keys])
print(f"T110  building the exact linearised operator, {NV} vertices")
eps=2e-3
dD=np.zeros((NV,0)); cols_d=[]; cols_a=[]
for i in range(NV):
    e1=np.zeros(NV); e1[i]=eps
    dp,ap=hinge_data(e1); dm,am=hinge_data(-e1)
    cols_d.append((dp-dm)/(2*eps)); cols_a.append((ap-am)/(2*eps))
    if i%20==0: print(f"   column {i}/{NV}", flush=True)
Dd=np.array(cols_d).T          # (hinges x NV)
Da=np.array(cols_a).T
Hm=Dd.T@Da
Hm=0.5*(Hm+Hm.T)
print(f"   operator built: {Hm.shape}, symmetric to {np.max(np.abs(Hm-Hm.T)):.2e}")
ev=np.linalg.eigvalsh(Hm)
print(f"   spectrum: min {ev.min():+.5f}  max {ev.max():+.5f}  #zero {int(np.sum(np.abs(ev)<1e-8))}")
rho=np.zeros(NV); centre=vid[(1,1,1,1)]; rho[centre]=1.0; rho-=rho.mean()
phi,res,rank,sv=np.linalg.lstsq(Hm,rho,rcond=None)
phi-=phi.mean()
print()
print("   response to a POINT SOURCE, by lattice distance from it:")
def dist(a,b):
    return sum(min((a[k]-b[k])%L,(b[k]-a[k])%L) for k in range(d))
prof={}
for v in verts:
    prof.setdefault(dist(v,(1,1,1,1)),[]).append(phi[vid[v]])
print(f"   {'distance':>9} {'sites':>6} {'mean phi':>14} {'|mean|':>12}")
for k in sorted(prof):
    arr=np.array(prof[k])
    print(f"   {k:9d} {len(arr):6d} {arr.mean():14.6e} {abs(arr.mean()):12.3e}")
print()
print("   a response that is largest at the source and falls with distance is the")
print("   structure a gravitational potential must have -- measured here on the")
print("   arena that PASSES the diffeomorphism gate, unlike Result 17's.")
