"""T68 - THE REFINEMENT/COVARIANCE GATE IN FOUR DIMENSIONS.
Results 23 and 24 established, in 1D and 2D, that the physics does not care how
the same geometry is chopped: the gauge response dies as O(h^2) while a genuine
shape change does not.  T66/T67 lifted the construction to d = 4 (Betti
[1,4,6,4,1], kernel exactly 16, flat spectrum 39.478 x8 and 78.957 x24 at O(h^2)).
The gate itself now has to be run in four dimensions.

Same flat 4-torus, chopped two ways: the uniform Kuhn triangulation, and the SAME
triangulation with its vertices displaced by a smooth periodic map (a discrete
4D reparametrisation).  The geometry is identical -- it is still the flat torus --
so the spectrum must agree, and the gap must die as the mesh refines.

Control included: a genuine geometry change (anisotropic rescaling of the torus,
which alters the true spectrum) must NOT die away."""
import numpy as np, itertools, math
def fem4(L, disp=None, scale=(1.,1.,1.,1.)):
    d=4
    verts=list(itertools.product(range(L),repeat=d)); vid={v:i for i,v in enumerate(verts)}
    n=len(verts); h=1.0/L
    def pos(v):
        x=np.array([vi*h*scale[i] for i,vi in enumerate(v)])
        if disp is not None: x=x+disp(np.array([vi*h for vi in v]))
        return x
    X={v:pos(v) for v in verts}
    K=np.zeros((n,n)); M=np.zeros(n)
    for base in verts:
        for perm in itertools.permutations(range(d)):
            ids=[vid[base]]; cur=list(base); pts=[X[base]]; shift=np.zeros(d)
            ok=True
            for a in perm:
                prev=tuple(cur); cur=list(cur)
                cur[a]=(cur[a]+1)%L
                if cur[a]==0: shift=shift.copy(); shift[a]+=1.0*scale[a]   # wrapped
                ids.append(vid[tuple(cur)]); pts.append(X[tuple(cur)]+shift)
            P=np.array(pts); Jm=(P[1:]-P[0]).T
            det=float(np.linalg.det(Jm))
            if abs(det)<1e-14: continue
            vol=abs(det)/math.factorial(d)
            Jinv=np.linalg.inv(Jm); G=np.zeros((d+1,d)); G[1:]=Jinv; G[0]=-np.sum(G[1:],axis=0)
            for a in range(d+1):
                M[ids[a]]+=vol/(d+1)
                for b in range(d+1): K[ids[a],ids[b]]+=vol*float(np.dot(G[a],G[b]))
    return K,M
def levels(K,M,k=3):
    A=np.diag(1.0/np.sqrt(M))@K@np.diag(1.0/np.sqrt(M))
    e=np.sort(np.clip(np.linalg.eigvalsh(A),0,None)); nz=e[e>1e-8]
    out=[]; rest=list(nz)
    for _ in range(k):
        if not rest: break
        x0=rest[0]; g=[z for z in rest if abs(z-x0)<0.06*max(1.0,x0)]
        out.append((float(np.mean(g)),len(g))); rest=[z for z in rest if z>x0*1.06]
    return out
def wave(a):
    def f(x): return np.array([a*np.sin(2*np.pi*x[1]), a*np.sin(2*np.pi*x[2]),
                               a*np.sin(2*np.pi*x[3]), a*np.sin(2*np.pi*x[0])])
    return f
print("T68  flat 4-torus.  GAUGE = vertices displaced by a smooth periodic map")
print("     (same flat geometry, different chopping).  Gap must die as O(h^2).")
print(f"   {'L':>4} {'verts':>7} {'uniform lvl1':>14} {'displaced lvl1':>16} {'|gap|':>12} {'ratio':>8}")
prev=None
for L in (3,4,5,6):
    K,M=fem4(L); u=levels(K,M,1)[0]
    K2,M2=fem4(L,disp=wave(0.10/ (1.0))); g=levels(K2,M2,1)[0]
    gap=abs(g[0]-u[0]); r=(prev/gap) if prev else float('nan'); prev=gap
    print(f"   {L:4d} {len(M):7d} {u[0]:10.5f} x{u[1]:<2d} {g[0]:12.5f} x{g[1]:<2d} {gap:12.6f} {r:8.2f}", flush=True)
print()
print("   expected O(h^2) ratios for L steps x1.33, x1.25, x1.20: 1.78, 1.56, 1.44")
print()
print("  CONTROL - a genuine geometry change (anisotropic torus) must NOT die away")
print(f"   {'L':>4} {'uniform lvl1':>14} {'stretched lvl1':>16} {'|gap|':>12} {'ratio':>8}")
prev=None
for L in (3,4,5,6):
    K,M=fem4(L); u=levels(K,M,1)[0]
    K2,M2=fem4(L,scale=(1.3,1.0,1.0,1.0)); s=levels(K2,M2,1)[0]
    gap=abs(s[0]-u[0]); r=(prev/gap) if prev else float('nan'); prev=gap
    print(f"   {L:4d} {u[0]:10.5f} x{u[1]:<2d} {s[0]:12.5f} x{s[1]:<2d} {gap:12.6f} {r:8.2f}", flush=True)
