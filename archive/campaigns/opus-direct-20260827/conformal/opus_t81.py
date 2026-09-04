"""T81 - IS IT THE FLAVOURS SPLITTING, OR JUST THE MOMENTA?  (auditing Result 34)
T80b read the true level structure and it raises a serious objection to Result
34's attribution.  Under conformal curvature the flat level of multiplicity 128
splits as  24 + 4 + 48 + 24 + 24 + 4 -- and EVERY one of those is divisible by 4,
as are the higher levels (60, 120, 24).  A 4-fold degeneracy survives everywhere.

That is what one expects if curvature lifts the MOMENTUM degeneracies -- which a
curved geometry must do -- while leaving the four flavours degenerate.  And my
flat-in-disguise control cannot tell the two apart: a flat metric has the flat
spectrum, so it splits neither momenta nor flavours.

Decisive test: use a metric with NO residual symmetry at all, so every momentum
degeneracy is already broken.  Then any surviving degeneracy can only be internal.
   * multiplicities still all divisible by 4  ->  the FOUR FLAVOURS STAY
     DEGENERATE, and Result 34's headline is wrong -- curvature splits momenta,
     not flavours.
   * multiplicities dropping to 1 or 2  ->  the flavours really do split."""
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
def mults(lap,tol=1e-7,n=14):
    nz=lap[lap>1e-8]; out=[]
    for z in nz:
        if out and abs(z-out[-1][0])<tol*max(abs(z),1.0): out[-1][1]+=1; out[-1][0]=z
        else: out.append([z,1])
    return out[:n]
rng=np.random.default_rng(3)
L=4
RAND={s: 1.0+0.35*rng.random(4) for s in itertools.product(range(L),repeat=4)}
def fully_random(s,LL): return RAND[s]
def incommensurate(s,LL):
    return np.array([1.0+0.3*np.cos(2*np.pi*s[0]/LL+0.4)+0.17*np.cos(4*np.pi*s[2]/LL),
                     1.0+0.25*np.cos(2*np.pi*s[1]/LL+1.9)+0.11*np.cos(2*np.pi*s[3]/LL),
                     1.0+0.21*np.cos(2*np.pi*s[2]/LL+2.7)+0.13*np.cos(4*np.pi*s[0]/LL),
                     1.0+0.19*np.cos(2*np.pi*s[3]/LL+0.9)+0.15*np.cos(2*np.pi*s[1]/LL)])
for nm,g in (("fully RANDOM per-site metric",fully_random),
             ("incommensurate, all 4 dirs",incommensurate)):
    lv=mults(spectrum(L,g))
    ms=[m for _,m in lv]
    print(f"\n  {nm}")
    print(f"    first {len(lv)} level multiplicities: {ms}")
    print(f"    all divisible by 4? {all(m%4==0 for m in ms)}     "
          f"by 2? {all(m%2==0 for m in ms)}     minimum {min(ms)}")
    print(f"    values: {[f'{v:.6f}' for v,_ in lv[:8]]}", flush=True)
print()
print("  If the minimum multiplicity is 4 with a metric that has NO symmetry left,")
print("  the surviving 4-fold cannot be momentum degeneracy: it is the flavours,")
print("  and they are NOT split by curvature.")
