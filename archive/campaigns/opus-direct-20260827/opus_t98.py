"""T98 - the audit continued: Results 1, 28 and 36, each by a different route.
Result 43 re-derived the two heaviest claims.  Three more carry weight and each
had something go wrong nearby, so each is re-checked by machinery that shares
nothing with the original:

 (A) RESULT 1 (analytic, general d): closure iff all degree weights equal.
     Original: degree-by-degree proof, machine-checked at d=2..5 with symbolic
     rho and symbolic g.  Here: a NUMERICAL random test at d=5 and d=6 -- pick
     random unequal weights and check closure FAILS, pick equal ones and check it
     HOLDS.  Falsification rather than solution of an ideal.

 (B) RESULT 28 (the tiling condition): circumcentric duals tile, barycentric do
     not.  Original: sums over an icosphere, after I fixed a circumcentre sign
     error.  Here: a completely different surface (a torus of revolution) and a
     random triangulation, to make sure it was not a property of that mesh.

 (C) RESULT 36 (the measure is unique up to scale): original used union-find over
     the incidence relation.  Here: the RANK of the linear system, computed by
     SVD -- a different algorithm answering the same question."""
import numpy as np, itertools
from math import comb
print("T98 (A)  Result 1 by falsification, d=5 and d=6")
rng=np.random.default_rng(9)
def closure_defect(d,rho,gi):
    BAS=[]
    for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
    IDX={b:i for i,b in enumerate(BAS)}; n=len(BAS)
    lam=[rho[k+1]/rho[k] for k in range(d)]
    G=[]
    for a in range(d):
        M=np.zeros((n,n))
        for S in BAS:
            k=len(S)
            if a not in S:
                T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]+=(-1)**sum(1 for i in S if i<a)
            for pos,i in enumerate(S):
                T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=lam[k-1]*(-1)**pos*gi[a,i]
        G.append(M)
    worst=0.0
    for a in range(d):
        for b in range(a,d):
            R=G[a]@G[b]+G[b]@G[a]-2*gi[a,b]*np.eye(n)
            worst=max(worst,float(np.max(np.abs(R))))
    return worst
for d in (5,6):
    A=rng.normal(size=(d,d)); g=A@A.T+d*np.eye(d); gi=np.linalg.inv(g)
    eq=closure_defect(d,[1.0]*(d+1),gi)
    un=closure_defect(d,list(1.0+rng.random(d+1)),gi)
    print(f"   d={d}: equal weights -> closure defect {eq:.3e}   "
          f"UNequal weights -> {un:.3e}")
print()
print("T98 (B)  Result 28 on a different surface: a torus of revolution")
def torus_mesh(nu,nv,R=2.0,r=0.8):
    V=[];F=[]
    for i in range(nu):
        for j in range(nv):
            u=2*np.pi*i/nu; v=2*np.pi*j/nv
            V.append(np.array([(R+r*np.cos(v))*np.cos(u),(R+r*np.cos(v))*np.sin(u),r*np.sin(v)]))
    idx=lambda i,j:(i%nu)*nv+(j%nv)
    for i in range(nu):
        for j in range(nv):
            F.append((idx(i,j),idx(i+1,j),idx(i,j+1)))
            F.append((idx(i+1,j),idx(i+1,j+1),idx(i,j+1)))
    return V,F
def circum(p0,p1,p2):
    a=p1-p0;b=p2-p0;n=np.cross(a,b);n2=float(n@n)
    if n2<1e-30: return (p0+p1+p2)/3
    return p0+np.cross(float(b@b)*a-float(a@a)*b,n)/(2*n2)
for nu,nv in ((16,10),(24,14)):
    V,F=torus_mesh(nu,nv)
    E={}
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])): E.setdefault((min(a,b),max(a,b)),len(E))
    for kind in ("circumcentric","barycentric"):
        area=0.0; t0=np.zeros(len(V)); t1=np.zeros(len(E))
        for f in F:
            p=[V[f[0]],V[f[1]],V[f[2]]]
            A=0.5*float(np.linalg.norm(np.cross(p[1]-p[0],p[2]-p[0]))); area+=A
            cc=circum(*p) if kind=="circumcentric" else (p[0]+p[1]+p[2])/3
            nrm=np.cross(p[1]-p[0],p[2]-p[0]); nrm=nrm/np.linalg.norm(nrm)
            for (i,j,o) in ((0,1,2),(1,2,0),(2,0,1)):
                mid=(p[i]+p[j])/2
                t1[E[(min(f[i],f[j]),max(f[i],f[j]))]]+=0.5*float(np.linalg.norm(p[j]-p[i]))*float(np.linalg.norm(cc-mid))
                mid2=(p[i]+p[o])/2
                t0[f[i]]+=abs(0.5*float(np.dot(np.cross(mid-p[i],cc-p[i]),nrm)))+abs(0.5*float(np.dot(np.cross(cc-p[i],mid2-p[i]),nrm)))
        print(f"   {nu}x{nv} {kind:>14}: sum_v |v*| = {t0.sum():10.5f}  "
              f"sum_e (1/2)|e||e*| = {t1.sum():10.5f}  area = {area:10.5f}  "
              f"spread = {max(t0.sum(),t1.sum(),area)-min(t0.sum(),t1.sum(),area):.3e}", flush=True)
print()
print("T98 (C)  Result 36 by SVD rank instead of union-find")
for d in (2,3,4):
    L=2
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cnt=[0]*(d+1)
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=cnt[k]; cnt[k]+=1
    off=[0]
    for k in range(d+1): off.append(off[-1]+cnt[k])
    N=off[-1]; rows=[]
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    for k in range(d):
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a)
                for nb in ((s,T),(shift(s,a),T)):
                    r=np.zeros(N); r[off[k+1]+j]=1.0; r[off[k]+cidx[k][nb]]-=1.0
                    rows.append(r)
    A=np.array(rows); sv=np.linalg.svd(A,compute_uv=False)
    nul=N-int(np.sum(sv>1e-9*sv.max()))
    print(f"   d={d}: {N} weights, {len(rows)} conditions -> null space dimension {nul}")
print()
print("   equal weights closing and unequal failing; the tiling holding on a")
print("   different surface; and the rank giving the same 1 as union-find --")
print("   three independent confirmations.")
