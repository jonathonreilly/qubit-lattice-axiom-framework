"""T112 - DOES THE REGGE CONFORMAL HESSIAN MATCH CONTINUUM GENERAL RELATIVITY?
Result 58 flagged a puzzle: the discrete conformal Hessian came out POSITIVE
definite, while the 'conformal factor problem' says the Euclidean gravitational
action has a wrong-sign conformal mode.  The puzzle resolves analytically, and
resolving it turns Result 53 into a QUANTITATIVE test against continuum GR.

Under g -> exp(2 phi) g in d=4:  sqrt(g) -> e^(4 phi) sqrt(g)  and
R -> e^(-2 phi) (R - 6 lap phi - 6 (d phi)^2).  So at a flat background (R=0),
expanding int R sqrt(g) to second order in phi:

    int (1 + 2 phi)(-6 lap phi - 6 (d phi)^2)
      = -6 int lap phi   [= 0]   - 12 int phi lap phi   - 6 int (d phi)^2
      = +12 int (d phi)^2 - 6 int (d phi)^2
      = +6 int (d phi)^2                                   POSITIVE

so the sign is right, and the 'conformal factor problem' refers to the action
with its -1/(16 pi G) prefactor, which flips it.  Result 58 was not anomalous.

That gives a NUMBER to check.  Result 31/T72 measured S_Regge -> (1/2) int R sqrt(g).
So the prediction is

        d^2 S_Regge [phi]  =  3 * int (d phi)^2

with int (d phi)^2 discretised on the same complex.  If the measured Hessian
matches 3 * (discrete Dirichlet energy), then Result 53's operator is quantitatively
the linearised Einstein-Hilbert action, not merely structurally like it."""
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
def run(L):
    d=4; h=1.0/L
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
    def S_of(phi):
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
            if np.any(w<1e-13): return None
            X=np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
            for tri in itertools.combinations(range(5),3):
                key=tuple(sorted([ids[i] for i in tri]))
                a=dihedral(X,list(tri))
                if a is None: continue
                ang[key]=ang.get(key,0.0)+a; area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
        return float(sum(area[k]*(2*np.pi-ang[k]) for k in ang))
    # discrete Dirichlet energy int (d phi)^2 on the SAME complex:
    # sum over edges of (dphi)^2 * (edge weight), with the FEM/cotan-analogue weight.
    # For the Kuhn torus the natural weight per edge is vol_of_dual / |e|^2 summed;
    # use the simplest consistent one: sum over simplices of vol * |grad phi|^2.
    import math
    def dirichlet(phi):
        tot=0.0
        for ids,P in tops:
            Jm=(P[1:]-P[0]).T
            vol=abs(float(np.linalg.det(Jm)))/math.factorial(4)
            Ji=np.linalg.inv(Jm); G4=np.zeros((5,4)); G4[1:]=Ji; G4[0]=-np.sum(G4[1:],axis=0)
            g=sum(phi[ids[a]]*G4[a] for a in range(5))
            tot+=vol*float(g@g)
        return tot
    S0=S_of(np.zeros(NV))
    eps=2e-3; rng=np.random.default_rng(7); rows=[]
    for t in range(6):
        v=rng.normal(size=NV); v-=v.mean(); v/=np.linalg.norm(v)
        Sp=S_of(eps*v); Sm=S_of(-eps*v)
        if Sp is None or Sm is None: continue
        d2=(Sp-2*S0+Sm)/eps**2
        dir_=dirichlet(v)
        rows.append((d2,dir_,d2/dir_ if dir_ else float('nan')))
    return NV,S0,rows
print("T112  is the Regge conformal Hessian = 3 * int (d phi)^2 ?")
print("      (prediction from S_Regge = (1/2) int R sqrt(g) and the +6 (dphi)^2 expansion)")
for L in (3,4):
    NV,S0,rows=run(L)
    print(f"\n   L={L}, {NV} vertices, S(flat)={S0:.2e}")
    print(f"   {'trial':>6} {'d2S':>14} {'int (dphi)^2':>15} {'ratio':>12}")
    for i,(a,b,c) in enumerate(rows):
        print(f"   {i:6d} {a:14.6f} {b:15.6f} {c:12.6f}", flush=True)
    r=np.array([c for _,_,c in rows])
    print(f"   mean ratio {r.mean():.6f}   spread {r.max()-r.min():.3e}   (prediction 3)")
