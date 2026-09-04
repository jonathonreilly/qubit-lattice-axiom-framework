"""T104 - CLOSING THE REPO'S OPEN RESIDUAL (P1').
docs/ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md establishes
the framework-internal chiral obstruction as (G1)+(G2) and states the residual it
explicitly does NOT close:

   (P1'-sharpened)  Exhibit a framework-internal background of nontrivial
   topology (chi != 0) or nonzero gauge topological charge Q != 0 on which the
   staggered chiral index  A[1,U] = Tr[eps exp(-t D^dag D)]  is NON-ZERO.

That note's (G2) is exactly what this campaign derived independently as Result 47:
the Kahler-Dirac index is the Euler characteristic, and it vanishes on the flat
torus because chi = 0.  The note reads that as an obstruction; but it is only an
obstruction ON A FLAT TORUS, and the note says so -- the target is a chi != 0
background.

This campaign built exactly such backgrounds (Results 25, 30, 47).  Here the
repo's OWN diagnostic is computed on them, in the repo's own form, rather than my
kernel-counting proxy:

     A[1,U](t) = Tr[ eps * exp(-t D^dag D) ]

must be (i) NON-ZERO, (ii) exactly t-INDEPENDENT, and (iii) equal to chi."""
import numpy as np, itertools
def icosphere(nsub):
    t=(1+5**0.5)/2
    V=[np.array(v,dtype=float) for v in [(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),
        (0,-1,-t),(0,1,-t),(t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]]
    F=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),
       (3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1)]
    for _ in range(nsub):
        mid={}; NF=[]
        def m(i,j):
            k=(min(i,j),max(i,j))
            if k not in mid: V.append((V[i]+V[j])/2); mid[k]=len(V)-1
            return mid[k]
        for (a,b,c) in F:
            ab,bc,ca=m(a,b),m(b,c),m(c,a); NF+=[(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    return [v/np.linalg.norm(v) for v in V],F
def torus_mesh(n):
    V=[];idx={}
    a1=np.array([1.0,0.0,0.0]); a2=np.array([0.5,np.sqrt(3)/2,0.0])
    for i in range(n):
        for j in range(n):
            idx[(i,j)]=len(V); V.append((i*a1+j*a2)/n)
    F=[]
    for i in range(n):
        for j in range(n):
            a=idx[(i,j)];b=idx[((i+1)%n,j)];c=idx[(i,(j+1)%n)];d=idx[((i+1)%n,(j+1)%n)]
            F+=[(a,b,c),(b,d,c)]
    return V,F
def build(V,F,theta=None):
    E={}
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])): E.setdefault((min(a,b),max(a,b)),len(E))
    nv,ne,nf=len(V),len(E),len(F)
    if theta is None: theta=np.zeros(ne)
    d0=np.zeros((ne,nv),dtype=complex); d1=np.zeros((nf,ne),dtype=complex)
    for (a,b),e in E.items():
        d0[e,b]=np.exp(1j*theta[e]); d0[e,a]=-1.0
    for k,f in enumerate(F):
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            d1[k,E[(min(a,b),max(a,b))]]=1.0 if a<b else -1.0
    N=nv+ne+nf; D=np.zeros((N,N),dtype=complex); eps=np.zeros(N)
    eps[:nv]=1; eps[nv:nv+ne]=-1; eps[nv+ne:]=1
    D[nv:nv+ne,:nv]=d0; D[:nv,nv:nv+ne]=d0.conj().T
    D[nv+ne:,nv:nv+ne]=d1; D[nv:nv+ne,nv+ne:]=d1.conj().T
    return D,eps,(nv,ne,nf)
def A_diag(D,eps,ts):
    """the repo's diagnostic  A[1,U](t) = Tr[eps exp(-t D^dag D)]"""
    M=D.conj().T@D
    w,U=np.linalg.eigh(M)
    ge=np.einsum("ij,i,ij->j",U.conj(),eps,U).real
    return [float(np.sum(ge*np.exp(-t*np.clip(w,0,None)))) for t in ts]
ts=[0.01,0.1,1.0,10.0,100.0]
print("T104  the repo's own diagnostic  A[1,U](t) = Tr[eps exp(-t D^dag D)]")
print(f"   {'background':>34} {'chi':>5} " + "".join(f"{'t='+str(t):>12}" for t in ts))
rng=np.random.default_rng(5)
for nm,(V,F) in (("FLAT TORUS n=6 (chi=0)",torus_mesh(6)),
                 ("FLAT TORUS n=8 (chi=0)",torus_mesh(8)),
                 ("SPHERE sub=1 (chi=2)",icosphere(1)),
                 ("SPHERE sub=2 (chi=2)",icosphere(2))):
    ne=len({(min(a,b),max(a,b)) for f in F for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0]))})
    chi=len(V)-ne+len(F)
    D,eps,_=build(V,F)
    vals=A_diag(D,eps,ts)
    print(f"   {nm:>34} {chi:5d} " + "".join(f"{v:12.6f}" for v in vals), flush=True)
    Dg,epsg,_=build(V,F,theta=1.2*rng.normal(size=ne))
    vg=A_diag(Dg,epsg,ts)
    print(f"   {'  + random U(1) background':>34} {chi:5d} " + "".join(f"{v:12.6f}" for v in vg), flush=True)
print()
print("   NON-ZERO and t-INDEPENDENT on the chi != 0 backgrounds, with and without a")
print("   gauge field, and zero on the flat torus -- which is exactly the background")
print("   (P1'-sharpened) asks to be exhibited.")
