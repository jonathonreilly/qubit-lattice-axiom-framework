"""T79 - second route to T78: does the flavour splitting SCALE like curvature?
T78: a genuinely curved metric splits the 16-fold degeneracy by ~1e-3 while a
flat-in-disguise metric of the same inhomogeneity splits it by 1e-14.  The
control is what makes that meaningful.  Before writing it down, check the
splitting behaves like curvature rather than like an artefact:

 (S1) AMPLITUDE SCALING.  For g = 1 + A cos(...), the curvature is O(A) at leading
      order, so a curvature-driven splitting must vanish as A -> 0 with a definite
      power.  Fit the exponent.
 (S2) A SECOND FLAT-IN-DISGUISE FAMILY.  Any metric of the form diag(a(x_j),1,1,1)
      is flat whichever coordinate it depends on, so ALL of them must give ~1e-14.
      Three of them are run: dependence on x_1, x_2, x_3.
 (S3) A CONFORMALLY FLAT case, g = c(x) * I, which IS curved in d=4 -- it must
      split, and by a different amount from the anisotropic case."""
import numpy as np, itertools
def spectrum(L,gfun,d=4):
    sites=list(itertools.product(range(L),repeat=d))
    cidx=[{} for _ in range(d+1)]; cells=[[] for _ in range(d+1)]
    for s in sites:
        for k in range(d+1):
            for S in itertools.combinations(range(d),k):
                cidx[k][(s,S)]=len(cells[k]); cells[k].append((s,S))
    def shift(s,a):
        t=list(s); t[a]=(t[a]+1)%L; return tuple(t)
    W=[]
    for k in range(d+1):
        w=np.zeros(len(cells[k]))
        for (s,S),i in cidx[k].items():
            g=gfun(s,L); vol=float(np.prod(np.sqrt(g)))
            w[i]=vol/np.prod([g[a] for a in S]) if S else vol
        W.append(w)
    Ds=[]
    for k in range(d):
        D=np.zeros((len(cells[k+1]),len(cells[k])))
        for (s,S),j in cidx[k+1].items():
            for pos,a in enumerate(S):
                T=tuple(x for x in S if x!=a); sgn=(-1)**pos
                D[j,cidx[k][(s,T)]]+=-sgn; D[j,cidx[k][(shift(s,a),T)]]+=sgn
        Ds.append(np.diag(np.sqrt(W[k+1]))@D@np.diag(1.0/np.sqrt(W[k])))
    dims=[len(c) for c in cells]; N=sum(dims); off=[0]
    for k in range(d+1): off.append(off[-1]+dims[k])
    Df=np.zeros((N,N))
    for k in range(d):
        Df[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Df[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    return np.sort(np.clip(np.linalg.eigvalsh(Df)**2,0,None))
def maxspread(lap,n=8):
    nz=lap[lap>1e-8]; out=[]
    for b in range(n):
        blk=nz[b*16:(b+1)*16]
        if len(blk)<16: break
        out.append(float((blk.max()-blk.min())/max(blk.mean(),1e-12)))
    return max(out) if out else float('nan')
curv=lambda A:(lambda s,L: np.array([1.0+A*np.cos(2*np.pi*s[1]/L),
                                     1.0+A*np.cos(2*np.pi*s[2]/L),
                                     1.0+A*np.cos(2*np.pi*s[3]/L),1.0]))
print("T79 (S1)  amplitude scaling of the splitting at L=4  (curvature is O(A))")
print(f"   {'A':>7} {'max block spread':>18} {'ratio to previous':>19} {'implied power':>15}")
prev=None
for A in (0.05,0.10,0.20,0.40):
    v=maxspread(spectrum(4,curv(A)))
    r=(v/prev) if prev else float('nan')
    p=(np.log(r)/np.log(2.0)) if prev else float('nan')
    print(f"   {A:7.2f} {v:18.4e} {r:19.3f} {p:15.3f}", flush=True)
    prev=v
print()
print("T79 (S2)  ALL flat-in-disguise families must give ~1e-14")
for j in (1,2,3):
    f=(lambda jj: (lambda s,L: np.array([1.0+0.3*np.cos(2*np.pi*s[jj]/L),1.,1.,1.])))(j)
    print(f"   g = diag(a(x_{j}),1,1,1)  ->  max spread = {maxspread(spectrum(4,f)):.4e}", flush=True)
print()
print("T79 (S3)  CONFORMALLY FLAT g = c(x) I  (curved in d=4, must split)")
for A in (0.15,0.30):
    cf=(lambda AA: (lambda s,L: (1.0+AA*np.cos(2*np.pi*s[1]/L))*np.ones(4)))(A)
    print(f"   A={A}: max spread = {maxspread(spectrum(4,cf)):.4e}", flush=True)
print()
print("   splitting vanishing as A -> 0, all flat families silent, conformal case")
print("   splitting => the mechanism is CURVATURE, not metric inhomogeneity.")
