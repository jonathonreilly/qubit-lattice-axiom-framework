"""T45b (equilateral torus, degenerate-star guard) - CURVED GEOMETRY IN THE COMPLEX.  Does the rule's operator SEE curvature?
Everything through Result 24 was flat space cut up cleverly.  The next structural
question is a complex that is NOT a diffeomorphic image of a flat grid.  Take the
construction to its native limit: put the exterior algebra on the COMPLEX'S OWN
CELLS -- values on vertices, on edges, on faces -- instead of attaching a whole
2^d fibre to every cell.  Then

    d  = the coboundary (signed incidence: faces compare their boundary)
    *  = the Hodge weights from cell volumes and dual volumes (cells weigh)
    delta = *^-1 d^T *  ,        D = d + delta

is the Kahler-Dirac operator of the complex.  Same slogan as Result 24 -- faces
compare, cells weigh -- but now the fibre lives ON the complex.

Four things are tested, and each is sharp:
  (C1) d o d = 0 exactly -- the complex is a complex.
  (C2) dim ker D = sum of Betti numbers.  Sphere 1+0+1 = 2; torus 1+2+1 = 4.
       NOTE this is also a DOUBLER test: the Result 24 cell construction had
       2^d spurious zero modes (16 on the torus).  If ker D is exactly the Betti
       sum, the doublers are GONE.
  (C3) McKean-Singer:  Str exp(-t D^2) = chi(M)  for EVERY t.  An exact,
       t-independent identity -- the sharpest possible check that the operator
       knows the topology.
  (C4) does it see CURVATURE?  The 0-form Laplacian on the unit sphere has
       eigenvalues l(l+1) = 0, 2, 6, 12, 20 with multiplicities 1, 3, 5, 7, 9.
       A flat complex cannot produce those.  If the sphere complex does, the
       operator sees curvature."""
import numpy as np, itertools
from collections import defaultdict
def icosphere(nsub):
    t=(1+5**0.5)/2
    V=[(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),(0,-1,-t),(0,1,-t),
       (t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]
    V=[np.array(v,dtype=float) for v in V]
    F=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),
       (10,7,6),(7,1,8),(3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),
       (2,4,11),(6,2,10),(8,6,7),(9,8,1)]
    for _ in range(nsub):
        mid={}; NF=[]
        def m(i,j):
            k=(min(i,j),max(i,j))
            if k not in mid:
                V.append((V[i]+V[j])/2); mid[k]=len(V)-1
            return mid[k]
        for (a,b,c) in F:
            ab,bc,ca=m(a,b),m(b,c),m(c,a)
            NF += [(a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)]
        F=NF
    V=[v/np.linalg.norm(v) for v in V]
    return V,F
def flat_torus(n):
    """EQUILATERAL triangular lattice.  A square grid split by diagonals gives
    right-isoceles triangles, whose hypotenuse is opposite a right angle, so its
    cotan Hodge weight is exactly zero and the operator is singular -- that is
    what broke the first run.  Equilateral triangles give cot(60) = 1/sqrt(3) on
    every edge."""
    V=[];idx={}
    a1=np.array([1.0,0.0,0.0]); a2=np.array([0.5,np.sqrt(3)/2,0.0])
    for i in range(n):
        for j in range(n):
            idx[(i,j)]=len(V); V.append((i*a1+j*a2)/n)
    F=[]
    for i in range(n):
        for j in range(n):
            a=idx[(i,j)]; b=idx[((i+1)%n,j)]; c=idx[(i,(j+1)%n)]; d=idx[((i+1)%n,(j+1)%n)]
            F += [(a,b,c),(b,d,c)]
    return V,F,n
def geometry(V,F,torus_n=None):
    """edges, d0, d1, and circumcentric (cotan) Hodge weights"""
    A1=np.array([1.0,0.0,0.0]); A2=np.array([0.5,np.sqrt(3)/2,0.0])
    B=np.array([[A1[0],A2[0]],[A1[1],A2[1]]]); Binv=np.linalg.inv(B)
    def pos(i,ref=None):
        p=V[i].copy()
        if torus_n is not None and ref is not None:
            uv=Binv@(p[:2]-ref[:2])
            for k in (0,1):
                while uv[k] >  0.5: uv[k]-=1.0
                while uv[k] < -0.5: uv[k]+=1.0
            p=np.array([*(B@uv + ref[:2]), 0.0])
        return p
    E={}; 
    for f in F:
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            E.setdefault((min(a,b),max(a,b)), len(E))
    nv,ne,nf=len(V),len(E),len(F)
    d0=np.zeros((ne,nv)); d1=np.zeros((nf,ne))
    for (a,b),e in E.items(): d0[e,b]=1.0; d0[e,a]=-1.0
    for k,f in enumerate(F):
        for a,b in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
            e=E[(min(a,b),max(a,b))]; d1[k,e]= 1.0 if a<b else -1.0
    star1=np.zeros(ne); star0=np.zeros(nv); star2=np.zeros(nf)
    for k,f in enumerate(F):
        p=[pos(f[0]), pos(f[1],V[f[0]]), pos(f[2],V[f[0]])]
        A=0.5*np.linalg.norm(np.cross(p[1]-p[0], p[2]-p[0])); star2[k]=1.0/A
        for (i,j,o) in ((0,1,2),(1,2,0),(2,0,1)):
            u=p[i]-p[o]; v=p[j]-p[o]
            cot=float(np.dot(u,v)/max(np.linalg.norm(np.cross(u,v)),1e-300))
            e=E[(min(f[i],f[j]),max(f[i],f[j]))]; star1[e]+=0.5*cot
    star0=np.zeros(nv)
    for k,f in enumerate(F):
        p=[pos(f[0]), pos(f[1],V[f[0]]), pos(f[2],V[f[0]])]
        A=0.5*np.linalg.norm(np.cross(p[1]-p[0], p[2]-p[0]))
        for i in f: star0[i]+=A/3.0
    return d0,d1,star0,star1,star2,nv,ne,nf
def operator(d0,d1,s0,s1,s2):
    bad=int(np.sum(s1<=1e-12))
    if bad: raise ValueError(f"{bad} edges have a non-positive cotan Hodge weight "
                            f"(min {s1.min():.3e}) -- degenerate triangulation")
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    A1=np.diag(np.sqrt(s2))@d1@np.diag(1.0/np.sqrt(s1))
    nv,ne,nf=d0.shape[1],d0.shape[0],d1.shape[0]
    N=nv+ne+nf; D=np.zeros((N,N))
    D[nv:nv+ne,0:nv]=A0; D[0:nv,nv:nv+ne]=A0.T
    D[nv+ne:,nv:nv+ne]=A1; D[nv:nv+ne,nv+ne:]=A1.T
    return D,A0,A1,nv,ne,nf
def report(name,V,F,tn=None,chi_exp=None,betti=None,show_lap=False):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,tn)
    c1=float(np.max(np.abs(d1@d0)))
    try:
        D,A0,A1,nv,ne,nf=operator(d0,d1,s0,s1,s2)
    except ValueError as ex:
        print(f"  {name}: SKIPPED -- {ex}"); return
    print(f"     star1 range [{s1.min():.4f},{s1.max():.4f}]  star0 range [{s0.min():.5f},{s0.max():.5f}]")
    ev=np.linalg.eigvalsh(D)
    nz=int(np.sum(np.abs(ev)<1e-8))
    chi_comb=nv-ne+nf
    print(f"  {name}:  V={nv} E={ne} F={nf}   V-E+F = {chi_comb}  (expected chi = {chi_exp})")
    print(f"     (C1) max|d1 d0| = {c1:.2e}")
    print(f"     (C2) dim ker D = {nz}   (Betti sum expected {sum(betti)})   -> {'PASS' if nz==sum(betti) else 'FAIL'}")
    d2=ev**2
    grade=np.array([0]*nv+[1]*ne+[2]*nf)
    # supertrace needs the eigenvectors' grading; use the block decomposition instead:
    L0=A0.T@A0; L2=A1@A1.T
    L1=A0@A0.T + A1.T@A1
    e0=np.linalg.eigvalsh(L0); e1=np.linalg.eigvalsh(L1); e2=np.linalg.eigvalsh(L2)
    print(f"     (C3) McKean-Singer  Str exp(-t D^2):", end="")
    for t in (0.05,0.2,1.0,5.0,50.0):
        st=float(np.sum(np.exp(-t*np.clip(e0,0,None)))-np.sum(np.exp(-t*np.clip(e1,0,None)))
                 +np.sum(np.exp(-t*np.clip(e2,0,None))))
        print(f"  t={t}: {st:+.6f}", end="")
    print(f"   (chi = {chi_exp})", flush=True)
    if show_lap:
        lo=np.sort(e0)[:26]
        print(f"     (C4) 0-form Laplacian spectrum (want l(l+1) = 0,2x3,6x5,12x7):")
        cl=[]
        for z in lo:
            if cl and abs(z-cl[-1][0])<0.12*max(1,abs(z)): cl[-1][1]+=1
            else: cl.append([z,1])
        print(f"          {[f'{v:.4f}x{c}' for v,c in cl[:5]]}", flush=True)
print("T45  the Kahler-Dirac operator built ON the complex (cochains), not on cells")
print()
for n in (6,10):
    V,F,tn=flat_torus(n)
    report(f"FLAT TORUS n={n}",V,F,tn=tn,chi_exp=0,betti=(1,2,1))
print()
for k in (1,2,3):
    V,F=icosphere(k)
    report(f"SPHERE (icosphere sub={k})",V,F,chi_exp=2,betti=(1,0,1),show_lap=True)
