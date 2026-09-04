"""T77 - DOES ANYTHING SPLIT THE FOUR FLAVOURS?  The generation question.
Result 33: the rule carries 16 components per site in d=4 -- four DEGENERATE
Dirac flavours.  Nature has three generations and they are not degenerate, so
either the prediction is wrong or something splits them.

In the continuum the Kahler-Dirac flavour symmetry is EXACT, so any splitting
produced by discretisation alone is an artefact and must vanish under refinement.
That makes this testable rather than hopeful:

   put an inhomogeneous METRIC on the cubical complex (Hodge weights from
   varying cell volumes and face areas -- the framework's own 'cells weigh')
   and watch the 16-fold degeneracy at each level.
     * splitting that SHRINKS under refinement  -> lattice artefact, no mechanism
     * splitting that SURVIVES                  -> a real degeneracy-breaking
                                                   mechanism inside the framework

Weights: degree-k cells get a weight from the metric; a diagonal metric
g = diag(a_0..a_3) gives the k-cell in directions S the weight
prod_(a in S) (vol / a_a^2) -- the induced metric on Lambda^k times the density,
which is exactly the Result 1 carrier."""
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
            g=gfun(s); vol=float(np.prod(np.sqrt(g)))
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
    Dfull=np.zeros((N,N))
    for k in range(d):
        Dfull[off[k+1]:off[k+2],off[k]:off[k+1]]=Ds[k]
        Dfull[off[k]:off[k+1],off[k+1]:off[k+2]]=Ds[k].T
    return np.sort(np.clip(np.linalg.eigvalsh(Dfull)**2,0,None)), len(sites)
def flat(s): return np.array([1.,1.,1.,1.])
def curved(amp):
    def f(s):
        return np.array([1.0+amp*np.cos(2*np.pi*s[1]/3), 1.0, 1.0, 1.0])
    return f
print("T77  does an inhomogeneous metric split the 16-fold flavour degeneracy?")
print(f"   {'L':>3} {'metric':>14} {'first level':>13} {'multiplicity':>13} {'spread within level':>21}")
for L in (3,4,5):
    for nm,g in (("flat",flat),("curved 0.30",curved(0.30)),("curved 0.60",curved(0.60))):
        try: lap,ns=spectrum(L,g)
        except Exception as ex:
            print(f"   {L:3d} {nm:>14}  failed: {ex}"); continue
        nz=lap[lap>1e-8]
        lvl=nz[0]; grp=nz[nz<lvl*1.35]
        print(f"   {L:3d} {nm:>14} {lvl:13.6f} {len(grp):13d} "
              f"{float(grp.max()-grp.min()):21.6e}", flush=True)
print()
print("   spread within the first cluster shrinking with L  =>  lattice artefact.")
print("   spread persisting  =>  a genuine flavour-splitting mechanism.")
