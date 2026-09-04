"""T73 - THE MISSING LINK: does the OPERATOR generate the GRAVITATIONAL ACTION?
The campaign now has two structures on one complex: the framework's Kahler-Dirac
operator (Results 25-30) and a Regge/Einstein-Hilbert action (Result 31).  What
makes that a theory rather than a coincidence is whether the operator's vacuum
response IS the gravitational action -- the Sakharov induced-gravity statement.

Two earlier attempts at it went through the heat-kernel coefficient and both died
on numerics (Result 25's chi/6 window, Result 31's note).  Different route here,
and it exploits a fact that makes everything tractable:

    a simplicial complex whose vertices sit in flat R^4 ALWAYS has zero deficit.
    Curvature requires specifying EDGE LENGTHS abstractly.

Both objects are functions of exactly those edge lengths.  So perturb the edge
lengths of the flat 4-torus, ell_e -> ell_e (1 + eps f_e), and measure

    dS/deps   (Regge action)      and      dW/deps   (operator's spectral action)

for SEVERAL different profiles f.  If the operator's effective action contains
c * S_Regge, then dW/dS must be the SAME CONSTANT for every profile.  That is the
induced-gravity claim as a correlation, with no asymptotic expansion needed.

Geometry from edge lengths alone via Cayley-Menger, so nothing is embedded."""
import numpy as np, itertools, math
def cayley_menger_vol(L2, n):
    """volume of an n-simplex from its squared edge lengths L2[i][j]"""
    M=np.ones((n+2,n+2)); M[0,0]=0.0
    for i in range(n+1):
        for j in range(n+1): M[i+1,j+1]=L2[i][j]
    d=float(np.linalg.det(M))
    s=((-1)**(n+1))/(2**n * (math.factorial(n)**2))
    v2=s*d
    return math.sqrt(v2) if v2>0 else float('nan')
def realize(L2,n):
    """place an n-simplex in R^n from squared edge lengths (Gram/Cholesky)"""
    G=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
    w,U=np.linalg.eigh(G)
    w=np.clip(w,0,None)
    X=U@np.diag(np.sqrt(w))
    return np.vstack([np.zeros(n),X])
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
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
L=3; d=4; h=1.0/L
verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
tops=[]
for base in verts:
    for perm in itertools.permutations(range(d)):
        chain=[base]; cur=list(base); pos=[np.array([b*h for b in base])]
        c=np.array([b*h for b in base])
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; chain.append(tuple(cur))
            c=c.copy(); c[a]+=h; pos.append(c)
        tops.append((tuple(vid[x] for x in chain), np.array(pos)))
edges={}
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        edges.setdefault(tuple(sorted((ids[i],ids[j]))), len(edges))
base_len=np.zeros(len(edges))
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        base_len[edges[tuple(sorted((ids[i],ids[j])))]]=float(np.linalg.norm(P[i]-P[j]))
print(f"T73  Kuhn 4-torus L={L}: {len(verts)} vertices, {len(edges)} edges, {len(tops)} 4-simplices")
def measure(scale):
    """given per-edge scale factors, return (Regge action, operator spectral action)"""
    ell=base_len*scale
    hinge_ang={}; hinge_area={}
    K=np.zeros((len(verts),len(verts))); M=np.zeros(len(verts))
    bad=0
    for ids,P in tops:
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            e=ell[edges[tuple(sorted((ids[i],ids[j])))]]
            L2[i][j]=L2[j][i]=e*e
        X=realize(L2,4)
        vol=cayley_menger_vol(L2,4)
        if not np.isfinite(vol) or vol<=0: bad+=1; continue
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            hinge_ang[key]=hinge_ang.get(key,0.0)+a
            hinge_area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
        Jm=(X[1:]-X[0]).T
        Jinv=np.linalg.inv(Jm); G=np.zeros((5,4)); G[1:]=Jinv; G[0]=-np.sum(G[1:],axis=0)
        for a_ in range(5):
            M[ids[a_]]+=vol/5.0
            for b_ in range(5): K[ids[a_],ids[b_]]+=vol*float(np.dot(G[a_],G[b_]))
    Sreg=float(sum(hinge_area[k]*(2*np.pi-hinge_ang[k]) for k in hinge_ang))
    VOL=float(np.sum(M))
    A=np.diag(1.0/np.sqrt(M))@K@np.diag(1.0/np.sqrt(M))
    ev=np.sort(np.clip(np.linalg.eigvalsh(A),0,None))
    W=float(np.sum(np.log(ev[1:41]+1.0)))          # IR-safe spectral action, lowest 40
    return Sreg, W, bad, VOL
S0,W0,bad0,V0=measure(np.ones(len(edges)))
print(f"   flat: S_Regge = {S0:+.3e}   W = {W0:.6f}   Vol = {V0:.6f}  (bad {bad0})")
print()
print("  REGRESSION: is dW a universal linear combination of dVol and dS_Regge?")
print("  (flat is a STATIONARY point of S -- R31 -- so first order in S is ~0 and the")
print("   curvature information lives at SECOND order; both orders are collected.)")
rng=np.random.default_rng(11)
eps=3e-3
# edge midpoints, so profiles can be given SPATIAL STRUCTURE.  White-noise profiles
# all have the same spectral character, which is what made dVol and dS collinear.
emid=np.zeros((len(edges),4))
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        emid[edges[tuple(sorted((ids[i],ids[j])))]]=0.5*(P[i]+P[j])
def wave_profile(kvec,phase):
    return np.cos(2*np.pi*(emid@np.array(kvec))+phase)
profiles=[]
for k in ((1,0,0,0),(0,1,0,0),(1,1,0,0),(1,1,1,0),(1,1,1,1),(2,0,0,0),(2,1,0,0),
          (2,2,0,0),(3,0,0,0),(3,1,1,0),(2,2,2,0),(3,3,0,0)):
    profiles.append((f"wave {k}", wave_profile(k,0.0)))
    profiles.append((f"wave {k} +ph", wave_profile(k,1.1)))
for t in range(4):
    profiles.append((f"white {t}", rng.normal(size=len(edges))))
rows=[]
for nm,f in profiles:
    mx=np.max(np.abs(f))
    if mx<1e-12: continue
    f=f/mx
    Sp,Wp,b1,Vp=measure(1.0+eps*f); Sm,Wm,b2,Vm=measure(1.0-eps*f)
    if b1+b2: continue
    d2=lambda p,z,m:(p-2*z+m)/eps**2
    rows.append((d2(Vp,V0,Vm), d2(Sp,S0,Sm), d2(Wp,W0,Wm)))
    print(f"   {nm:>16}: d2Vol={rows[-1][0]:+11.4f} d2S={rows[-1][1]:+12.4f} "
          f"d2W={rows[-1][2]:+12.4f}   ratio d2S/d2Vol = {rows[-1][1]/rows[-1][0]:8.3f}", flush=True)
R=np.array(rows)
def fit(X,y,names):
    A=np.column_stack([X, np.ones(len(y))])
    coef,res,rank,sv=np.linalg.lstsq(A,y,rcond=None)
    pred=A@coef; ss=float(np.sum((y-pred)**2)); tot=float(np.sum((y-np.mean(y))**2))
    r2=1-ss/tot if tot>0 else float('nan')
    print(f"      {' + '.join(f'{c:+.5f}*{n}' for c,n in zip(coef,names+['1']))}    R^2 = {r2:.6f}")
    return r2
print()
rr=R[:,1]/R[:,0]
print(f"   decorrelation check: d2S/d2Vol now spans [{rr.min():.3f}, {rr.max():.3f}]"
      f"  (white-noise-only spanned [17.3, 20.0])")
c=np.corrcoef(R[:,0],R[:,1])[0,1]
print(f"   corr(d2Vol, d2S) = {c:.5f}   (collinearity is what killed the first attempt)")
print()
print("   d2W  vs  (d2Vol, d2S)")
r2_both=fit(R[:,[0,1]], R[:,2], ['d2Vol','d2S'])
print("   d2W  vs  d2Vol alone   (drop the curvature term)")
r2_vol=fit(R[:,[0]], R[:,2], ['d2Vol'])
print("   d2W  vs  d2S alone     (drop the volume term)")
fit(R[:,[1]], R[:,2], ['d2S'])
print()
print(f"   adding the Regge term improves R^2 from {r2_vol:.6f} to {r2_both:.6f}")
print("   a large improvement => the operator's spectral action CONTAINS the Regge")
print("   action (induced gravity).  No improvement => it does not.")
