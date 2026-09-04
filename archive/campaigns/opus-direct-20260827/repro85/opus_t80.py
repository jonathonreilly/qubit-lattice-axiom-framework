"""T80 - WHAT IS THE PATTERN OF THE SPLIT?
Result 34: curvature lifts the 16-fold degeneracy.  Result 33's counting problem
stands -- four flavours, not three.  So the question that matters now is the
PATTERN: when curvature splits a block of 16, what does it split INTO?

  16 = 4 flavours x 4 spinor components.
  If the spinor structure is untouched and only the flavours split, the pattern is
  4 groups of 4.  A 3+1 pattern would be striking.  An unstructured 16 would say
  the splitting does not respect the flavour decomposition at all.

Measured directly: take a block of 16 under conformal curvature (the strongest
splitter, Result 34) and print the sub-multiplicities -- how the 16 eigenvalues
cluster, and how those clusters behave as the curvature is turned down."""
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
def pattern(blk,tol):
    grp=[]
    for z in blk:
        if grp and abs(z-grp[-1][-1])<tol*max(abs(z),1e-12): grp[-1].append(z)
        else: grp.append([z])
    return [len(g) for g in grp], [float(np.mean(g)) for g in grp]
print("T80  how does curvature split a block of 16?   (conformal metric, L=4)")
for A in (0.30,0.15,0.05):
    cf=(lambda AA:(lambda s,L:(1.0+AA*np.cos(2*np.pi*s[1]/L))*np.ones(4)))(A)
    lap=spectrum(4,cf); nz=lap[lap>1e-8]
    print(f"\n   A = {A}")
    for b in range(3):
        blk=nz[b*16:(b+1)*16]
        if len(blk)<16: break
        mult,vals=pattern(blk,1e-4)
        print(f"     block {b}: multiplicities {mult}   spread {(blk.max()-blk.min())/blk.mean():.3e}")
        print(f"               values {[f'{v:.6f}' for v in vals]}", flush=True)
print()
print("   [4,4,4,4] => only the flavours split, the spinor structure is intact.")
print("   [3,...]  => a three-fold structure, which would be striking.")
print("   many singletons => the split does not respect the flavour decomposition.")
