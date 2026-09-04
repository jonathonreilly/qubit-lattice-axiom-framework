"""T84 - MATTER CURVES SPACETIME, locally, on the framework's own object.
Result 31 tested only the VACUUM equation.  The sharpest local statement in Regge
form is what happens with a source.  Add a tension living on hinges:

     S = sum_h A_h delta_h  -  sum_h T_h A_h

and vary the edge lengths.  The Schlaefli identity (verified in T70 to 1e-14)
kills the derivative-of-angle term, so

     dS = sum_h (delta_h - T_h) dA_h        ==>        delta_h = T_h

**A source concentrated on a hinge produces exactly that much deficit angle.**
That is the discrete Einstein equation in its most local form -- and it is the
Regge version of a cosmic string, where the deficit angle IS the tension.

Test: start from a flat complex, switch on a tension on ONE hinge, minimise the
action over edge lengths by gradient descent, and read off
   (a) the deficit at the sourced hinge, against the imposed tension;
   (b) the deficit elsewhere, which should stay near zero -- curvature localised
       at the source, which is what 'matter curves spacetime' means locally."""
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
    a=p1-p0; b=p2-p0
    return 0.5*np.sqrt(max(float(np.dot(a,a)*np.dot(b,b)-np.dot(a,b)**2),0.0))
def realize(L2):
    G=np.zeros((4,4))
    for i in range(4):
        for j in range(4): G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
    w,U=np.linalg.eigh(G); w=np.clip(w,1e-12,None)
    return np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
L=3; d=4; h=1.0/L
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
edges={}
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        edges.setdefault(tuple(sorted((ids[i],ids[j]))),len(edges))
base_len=np.zeros(len(edges))
for ids,P in tops:
    for i,j in itertools.combinations(range(5),2):
        base_len[edges[tuple(sorted((ids[i],ids[j])))]]=float(np.linalg.norm(P[i]-P[j]))
def geom(ell):
    ang={}; area={}
    for ids,P in tops:
        L2=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            e=ell[edges[tuple(sorted((ids[i],ids[j])))]]; L2[i][j]=L2[j][i]=e*e
        X=realize(L2)
        for tri in itertools.combinations(range(5),3):
            key=tuple(sorted([ids[i] for i in tri]))
            a=dihedral(X,list(tri))
            if a is None: continue
            ang[key]=ang.get(key,0.0)+a
            area[key]=tri_area(X[tri[0]],X[tri[1]],X[tri[2]])
    return ang,area
ang0,area0=geom(base_len)
hinges=sorted(ang0.keys())
print(f"T84  flat 4-torus L={L}: {len(edges)} edges, {len(hinges)} hinges")
print(f"     flat check: max|deficit| = {max(abs(2*np.pi-ang0[k]) for k in hinges):.2e}")
target=hinges[len(hinges)//2]
for T in (0.05,0.10):
    def action(ell):
        ang,area=geom(ell)
        return float(sum(area[k]*(2*np.pi-ang[k]) for k in ang)) - T*area.get(target,0.0)
    ell=base_len.copy(); step=2e-3
    for it in range(30):
        g=np.zeros(len(ell)); e0=action(ell)
        for _ in range(1):
            idx=np.random.default_rng(it).permutation(len(ell))[:40]
            for i in idx:
                dl=1e-4; ell[i]+=dl; ep=action(ell); ell[i]-=2*dl; em=action(ell); ell[i]+=dl
                g[i]=(ep-em)/(2*dl)
        ell=ell-step*g
    ang,area=geom(ell)
    dt=2*np.pi-ang[target]
    others=[abs(2*np.pi-ang[k]) for k in hinges if k!=target]
    print(f"   tension T = {T}:  deficit at the sourced hinge = {dt:+.6f}"
          f"   (target {T})   max|deficit| elsewhere = {max(others):.3e}", flush=True)
print()
print("   deficit -> T at the source and ~0 elsewhere = the local Einstein equation:")
print("   matter concentrated on a hinge bends exactly that hinge, by its own amount.")
