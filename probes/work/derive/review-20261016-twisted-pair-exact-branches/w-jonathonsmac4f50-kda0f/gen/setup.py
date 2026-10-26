import itertools, sys, time
from fractions import Fraction as F
import sympy as sp

t0=time.time()
def log(*a): print(f'[{time.time()-t0:6.1f}s]',*a,flush=True)

# ---------- representation: E1/2 + E5/2 (sign twist on the C4 generators) ----------
RZ = sp.Matrix([[0,-1,0],[1,0,0],[0,0,1]]); RX = sp.Matrix([[1,0,0],[0,0,-1],[0,1,0]])
s2=sp.sqrt(2)
dz = sp.diag(sp.exp(-sp.I*sp.pi/4), sp.exp(sp.I*sp.pi/4)).applyfunc(sp.nsimplify)
dx = (sp.Matrix([[1,-sp.I],[-sp.I,1]])/s2)
Dz = sp.diag(dz,-dz); Dx = sp.diag(dx,-dx)
key=lambda M: tuple(int(x) for x in M)
G={key(sp.eye(3)):(sp.eye(3),sp.eye(4))}
fr=list(G.values())
while fr:
    nx=[]
    for R,D in fr:
        for R2,D2 in ((RZ,Dz),(RX,Dx)):
            R3=R*R2;k3=key(R3)
            if k3 not in G:
                G[k3]=(R3,(D*D2).applyfunc(lambda x: sp.nsimplify(sp.simplify(x)))); nx.append(G[k3])
    fr=nx
G=list(G.values()); assert len(G)==24

# ---------- Gaussian-rational helpers ----------
def gq(x):
    x=sp.nsimplify(sp.simplify(x)); r,i=sp.re(x),sp.im(x)
    assert r.is_rational and i.is_rational,x
    return (F(int(r.p),int(r.q)),F(int(i.p),int(i.q)))
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def gconj(a): return (a[0],-a[1])
def gadd(a,b): return (a[0]+b[0],a[1]+b[1])
Z0=(F(0),F(0))

cell=[tuple(v) for v in itertools.product((-1,0,1),repeat=3)]
# ---------- covariant parametrisation by stabiliser commutants ----------
params=[]            # list of (orbit_rep, index)
M={}                 # M[(n,j)] = 4x4 Gaussian matrix (list of lists) : A_n = sum_j p_j M[(n,j)]
done=set()
for n in cell:
    if n in done: continue
    st=[D for R,D in G if key(R*sp.Matrix(n))==n]
    # commutant = image of the averaging projector on matrix units
    imgs=[]
    for a in range(4):
        for b in range(4):
            E=sp.zeros(4); E[a,b]=1
            avg=sum(((D*E*D.H) for D in st),sp.zeros(4))/len(st)
            imgs.append(avg.applyfunc(lambda x: sp.nsimplify(sp.simplify(x))))
    # extract a basis of the span over C (Gaussian elimination)
    basis=[]
    def gdiv(a,b):
        d=b[0]*b[0]+b[1]*b[1]
        return gmul(a,(b[0]/d,-b[1]/d))
    rows=[]
    for I_ in imgs:
        w=[gq(x) for x in I_]
        for (pv,piv) in rows:
            if w[piv]!=Z0:
                f=gdiv(w[piv],pv[piv]); w=[gadd(x,gmul((-f[0],-f[1]),y)) for x,y in zip(w,pv)]
        nz=[i for i,x in enumerate(w) if x!=Z0]
        if nz:
            rows.append((w,nz[0])); basis.append(I_)
    j0=len(params)
    for k,Bk in enumerate(basis):
        params.append((n,k))
    # orbit images
    for R,D in G:
        m=key(R*sp.Matrix(n))
        if m not in done:
            pass
    seen={}
    for R,D in G:
        m=tuple(int(x) for x in R*sp.Matrix(n))
        if m not in seen:
            seen[m]=(R,D)
    for m,(R,D) in seen.items():
        for k,Bk in enumerate(basis):
            Mm=(D*Bk*D.H)
            M[(m,j0+k)]=[[gq(Mm[a,b]) for b in range(4)] for a in range(4)]
        done.add(m)
NP=len(params)
log('complex parameters',NP,'real unknowns',2*NP)
# real variables: x_j = index j, y_j = index NP+j
NV=2*NP
Mn={}   # per n: list of (j, matrix)
for (n,j),mat in M.items():
    Mn.setdefault(n,[]).append((j,mat))

# ---------- polynomial engine: dict {monomial(tuple sorted var idx): Fraction} ----------
def padd(p,q,c=F(1)):
    r=dict(p)
    for m,v in q.items():
        nv=r.get(m,F(0))+c*v
        if nv==0: r.pop(m,None)
        else: r[m]=nv
    return r
def pscale(p,c): return {m:v*c for m,v in p.items()} if c!=0 else {}
def pmul(p,q):
    r={}
    for m1,v1 in p.items():
        for m2,v2 in q.items():
            m=tuple(sorted(m1+m2)); nv=r.get(m,F(0))+v1*v2
            if nv==0: r.pop(m,None)
            else: r[m]=nv
    return r
def padd_inplace(r,m,v):
    nv=r.get(m,F(0))+v
    if nv==0: r.pop(m,None)
    else: r[m]=nv

def build_unitarity():
    """returns dict m -> 4x4 of (re_poly, im_poly) for sum_n A_n A_{n-m}^dagger - delta_{m0} I over real vars."""
    out={}
    diffs={tuple(a-b for a,b in zip(n1,n2)) for n1 in cell for n2 in cell}
    for m in sorted(diffs):
        acc=[[({},{}) for _ in range(4)] for _ in range(4)]
        for n in cell:
            n2=tuple(a-b for a,b in zip(n,m))
            if n2 not in Mn or n not in Mn: continue
            for j,Mj in Mn[n]:
                for l,Ml in Mn[n2]:
                    # (x_j+i y_j)(x_l - i y_l)
                    re_=[((j,l),F(1)),((NP+j,NP+l),F(1))]
                    im_=[((NP+j,l),F(1)),((j,NP+l),F(-1))]
                    for a in range(4):
                        for b in range(4):
                            g=(F(0),F(0))
                            for c in range(4):
                                g=gadd(g,gmul(Mj[a][c],gconj(Ml[b][c])))
                            if g==Z0: continue
                            R_,I_=acc[a][b]
                            for mo,cf in re_:
                                mon=tuple(sorted(mo))
                                padd_inplace(R_,mon,g[0]*cf); padd_inplace(I_,mon,g[1]*cf)
                            for mo,cf in im_:
                                mon=tuple(sorted(mo))
                                padd_inplace(R_,mon,-g[1]*cf); padd_inplace(I_,mon,g[0]*cf)
        if m==(0,0,0):
            for a in range(4): padd_inplace(acc[a][a][0],(),F(-1))
        out[m]=acc
    return out
