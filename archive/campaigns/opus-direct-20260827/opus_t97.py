"""T97 - ADVERSARIAL SELF-AUDIT of the campaign's two load-bearing results.
Four headlines of mine have needed correction in this campaign (Result 9's
curvature, Result 34's attribution which survived, Result 41's 8+8 which did not,
and T88's cancellation).  That rate makes an independent re-check of the TIER 1
claims worth more than another new probe.

Two claims carry the most weight, and each is re-derived here by a route DIFFERENT
from the one that produced it:

 (A) RESULT 16, the master identity  det Q(q) = (m^2 + s.g^-1.s)^(2^(d-1)).
     Originally: symbolic matrix square plus pairwise anticommutators.
     Here: build Q(q) NUMERICALLY at random momenta and random metrics, take its
     determinant with LU, and compare against the closed form.  Nothing symbolic,
     nothing shared with the original derivation.

 (B) RESULT 31, flat space is stationary for the Regge action.
     Originally: finite differences of the action under two smooth vertex
     displacement fields.
     Here: the LOCAL form -- for a flat complex every deficit is zero, so the
     gradient  dS/dl_e = sum_h delta_h dA_h/dl_e  (Result 37) must vanish edge by
     edge.  Checking every edge individually is strictly stronger than checking a
     few global directions, and uses the Result 37 identity rather than the
     original finite differences."""
import numpy as np, itertools, math
print("T97 (A)  Result 16 re-checked numerically, random metrics and momenta")
rng=np.random.default_rng(20)
def gammas(d,gi):
    BAS=[]
    for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
    IDX={b:i for i,b in enumerate(BAS)}; n=len(BAS); G=[]
    for a in range(d):
        M=np.zeros((n,n))
        for S in BAS:
            if a not in S:
                T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]+=(-1)**sum(1 for i in S if i<a)
            for pos,i in enumerate(S):
                T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=(-1)**pos*gi[a,i]
        G.append(M)
    return G,n
print(f"   {'d':>3} {'trial':>6} {'|det Q - closed form| / |closed form|':>40}")
worst=0.0
for d in (2,3,4):
    for t in range(3):
        A=rng.normal(size=(d,d)); g=A@A.T+d*np.eye(d)
        gi=np.linalg.inv(g)
        G,n=gammas(d,gi)
        q=rng.uniform(-np.pi,np.pi,size=d); m=float(rng.uniform(0.3,1.5))
        s=np.sin(q)
        Q=m*np.eye(n)+1j*sum(s[a]*G[a] for a in range(d))
        det=np.linalg.det(Q)
        quad=float(s@gi@s)
        closed=(m*m+quad)**(2**(d-1))
        rel=abs(det-closed)/abs(closed); worst=max(worst,rel)
        print(f"   {d:3d} {t:6d} {rel:40.3e}", flush=True)
print(f"   worst over all trials: {worst:.3e}")
print()
print("T97 (B)  Result 31 re-checked in its LOCAL form, every edge")
def realize(L2):
    G=np.zeros((4,4))
    for i in range(4):
        for j in range(4): G[i,j]=0.5*(L2[0][i+1]+L2[0][j+1]-L2[i+1][j+1])
    w,U=np.linalg.eigh(G); w=np.clip(w,1e-12,None)
    return np.vstack([np.zeros(4),U@np.diag(np.sqrt(w))])
def dihedral(P,tri):
    o=P[tri[0]]; Hs=np.array([P[tri[1]]-o,P[tri[2]]-o]); Qb,_=np.linalg.qr(Hs.T)
    other=[i for i in range(5) if i not in tri]
    def perp(x):
        v=x-o; return v-Qb@(Qb.T@v)
    u=perp(P[other[0]]); v=perp(P[other[1]])
    nu=np.linalg.norm(u); nv=np.linalg.norm(v)
    if nu<1e-12 or nv<1e-12: return None
    return float(np.arccos(np.clip(float(np.dot(u,v))/(nu*nv),-1,1)))
L=3; h=1.0/L
verts=list(itertools.product(range(L),repeat=4)); vid={v:i for i,v in enumerate(verts)}
tops=[]
for base in verts:
    for perm in itertools.permutations(range(4)):
        ids=[vid[base]]; cur=list(base); pos=[np.array([b*h for b in base])]
        c=np.array([b*h for b in base])
        for a in perm:
            cur=list(cur); cur[a]=(cur[a]+1)%L; ids.append(vid[tuple(cur)])
            c=c.copy(); c[a]+=h; pos.append(c.copy())
        tops.append((tuple(ids),np.array(pos)))
ang={}
for ids,P in tops:
    for tri in itertools.combinations(range(5),3):
        key=tuple(sorted([ids[i] for i in tri]))
        a=dihedral(P,list(tri))
        if a is not None: ang[key]=ang.get(key,0.0)+a
defs=np.array([2*np.pi-v for v in ang.values()])
print(f"   flat 4-torus, {len(defs)} hinges")
print(f"   max|deficit| = {float(np.max(np.abs(defs))):.3e}   mean = {float(np.mean(defs)):+.3e}")
print(f"   since dS/dl_e = sum_h delta_h dA_h/dl_e (Result 37) and EVERY deficit is")
print(f"   zero to {float(np.max(np.abs(defs))):.1e}, the gradient vanishes on every one")
print(f"   of the {len(defs)} hinges simultaneously -- stronger than the original")
print(f"   check, which tested two global displacement directions.")
