"""T78 - flavour splitting with a metric that is ACTUALLY curved.
T77b found the 16-fold degeneracy exact (1e-14) under g = diag(a(x_1),1,1,1) --
but that metric is FLAT IN DISGUISE.  It is the very family Result 21 identified:
coframe e^1 = sqrt(a) dx^1 gives de^1 = 0, connection zero, curvature zero.  It
also leaves three translation symmetries intact, so degenerate blocks of 16 could
be momentum multiplets rather than flavour multiplets.  Two faults, one fix:

   g = diag(1 + A cos(2 pi x_1/L), 1 + A cos(2 pi x_2/L), 1 + A cos(2 pi x_3/L), 1)

depends on three different coordinates through three different components, so it
is genuinely curved AND has no residual translation symmetry.  A second profile
with incommensurate phases is run as well, to be sure no accidental symmetry is
carrying the result.

The physics at stake: Lambda*(M) = S tensor S*, so d+delta is the Dirac operator
TWISTED by the spinor bundle.  On flat space the twist is trivial and the four
flavours are exactly degenerate; on a curved manifold the twist is not trivial,
so curvature SHOULD split them.  If it does, curvature is a flavour-splitting
mechanism inside the framework.  If it does not, the degeneracy is more robust
than the continuum picture suggests and that itself needs explaining."""
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
def flat(s,L): return np.array([1.,1.,1.,1.])
def flat_disguise(A):
    return lambda s,L: np.array([1.0+A*np.cos(2*np.pi*s[1]/L),1.,1.,1.])
def truly_curved(A):
    return lambda s,L: np.array([1.0+A*np.cos(2*np.pi*s[1]/L),
                                 1.0+A*np.cos(2*np.pi*s[2]/L),
                                 1.0+A*np.cos(2*np.pi*s[3]/L), 1.0])
def curved_phases(A):
    return lambda s,L: np.array([1.0+A*np.cos(2*np.pi*s[1]/L+0.7),
                                 1.0+A*np.cos(2*np.pi*s[2]/L+2.1)*0.8,
                                 1.0+A*np.cos(2*np.pi*s[0]/L+1.3)*0.6, 1.0])
def blocks(lap,n=6):
    nz=lap[lap>1e-8]; out=[]
    for b in range(n):
        blk=nz[b*16:(b+1)*16]
        if len(blk)<16: break
        out.append(float((blk.max()-blk.min())/max(blk.mean(),1e-12)))
    return out
print("T78  within-block-of-16 relative spread; 0 = flavours still degenerate")
print(f"   {'L':>3} {'metric':>22} {'A':>5} {'block spreads (first 4)':>40} {'max':>11}")
for nm,mk in (("flat (control)",lambda A: flat),
              ("flat-in-disguise",flat_disguise),
              ("TRULY CURVED",truly_curved),
              ("curved, phases",curved_phases)):
    for A in ((0.0,) if nm=="flat (control)" else (0.3,)):
        for L in (3,4,5):
            try: lap=spectrum(L,mk(A))
            except Exception as ex:
                print(f"   {L:3d} {nm:>22} {A:5.2f}  failed: {ex}"); continue
            bs=blocks(lap)
            print(f"   {L:3d} {nm:>22} {A:5.2f} {str([f'{v:.3e}' for v in bs[:4]]):>40} "
                  f"{(max(bs) if bs else float('nan')):11.3e}", flush=True)
    print()
print("   flat-in-disguise ~ 1e-14 (it is flat, so it must not split anything).")
print("   TRULY CURVED nonzero => curvature splits the four flavours: a mechanism.")
print("   TRULY CURVED also ~1e-14 => the degeneracy survives curvature.")
