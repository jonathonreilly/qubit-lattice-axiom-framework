"""T80b - the splitting pattern, without imposing blocks.
T80 cut the spectrum into consecutive blocks of 16 and read the multiplicities
inside them.  That was wrong: the blocks straddle the real levels (block 0 held
16 states at 1.849914, block 1 held 8 MORE at the same value plus 4 and 4), so
the '8,4,4' pattern was an artefact of where the cuts fell.

(Result 34 is unaffected -- 'max spread within any block of 16' is a valid
zero-versus-nonzero detector however the cuts fall, and the flat and
flat-in-disguise controls returned 1e-14 under the same blocking.)

Done properly: cluster the WHOLE spectrum by eigenvalue and report the true
level structure, flat against curved, so the splitting pattern can be read off
by comparing them."""
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
def levels(lap,tol=1e-6,n=8):
    nz=lap[lap>1e-8]; out=[]
    for z in nz:
        if out and abs(z-out[-1][0])<tol*max(abs(z),1.0): out[-1][1]+=1; out[-1][0]=z
        else: out.append([z,1])
    return out[:n]
flat=lambda s,L: np.ones(4)
print("T80b  TRUE level structure (value x multiplicity), L=4")
print("\n   FLAT:")
for v,m in levels(spectrum(4,flat)):
    print(f"     {v:12.6f} x {m}")
for A in (0.05,0.15,0.30):
    cf=(lambda AA:(lambda s,L:(1.0+AA*np.cos(2*np.pi*s[1]/L))*np.ones(4)))(A)
    print(f"\n   CONFORMAL curvature A = {A}:")
    lv=levels(spectrum(4,cf))
    tot=0
    for v,m in lv:
        tot+=m; print(f"     {v:12.6f} x {m}")
    print(f"     (first {len(lv)} levels hold {tot} states)")
print()
print("   Compare a flat level of multiplicity 16*k against what it becomes when")
print("   curvature is switched on: the way that number partitions IS the pattern.")
