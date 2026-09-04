"""T143 - MAPPING THE REALIZABILITY THRESHOLD FINELY AROUND THE PLANCK SCALE.

T142b located a threshold between q = 0.1 a^2 (unconstrained) and q = 0.25 a^2
(6.5% of simplices non-realizable), with l_P^2 = 0.195 a^2 sitting between them.
Map it properly.  Four things that first probe got wrong or did not separate:

(1) WRONG OBSERVABLE.  'Fraction of configurations fully realizable' is
    N-dependent: if each simplex fails independently with probability p, a
    configuration of N simplices is clean with probability (1-p)^N -> 0.  The
    N-independent observable is p itself -- the FRACTION OF SIMPLICES that fail.
    Physically p > 0 means some region of any large universe is non-geometric,
    which is the actual content.

(2) WRONG PERTURBATION SIZE.  I perturbed by +-q, the full quantum.  But snapping
    a smooth geometry onto a grid of spacing q gives per-edge errors UNIFORM IN
    [-q/2, +q/2].  That is half the roughness, so my threshold was pessimistic by
    roughly a factor of two.  Test both.

(3) TWO DIFFERENT GRIDS, and 'the length between sites is Planck' means the second:
       (A) l^2 in Z . l_0^2   -- uniform grid in SQUARED length (what I tested)
       (B) l   in Z . l_0     -- uniform grid in LENGTH, so l^2 takes values
                                 n^2 l_0^2 and the effective l^2-spacing at length
                                 l is about 2 l l_0, which is COARSER.
    Scheme (B) is the physically natural reading and is the harsher test.

(4) NO ERROR BARS.  12 trials.  Use enough to resolve where p leaves zero.

The Planck scale to mark: R73 gives l_P/a = 0.442 (spectral cutoff convention)
to 0.515 (mode-counting), so l_P^2/a^2 = 0.195 to 0.265."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t114b import build

def prep(L):
    verts,vid,tops,edges,emid,edir,base_len=build(L)
    h=1.0/L
    l2=np.array([base_len[e]**2 for e in range(len(base_len))])/h**2
    IJ=np.zeros((len(tops),5,5),dtype=np.int64)
    for t,(ids,P) in enumerate(tops):
        for i,j in itertools.combinations(range(5),2):
            e=edges[tuple(sorted((ids[i],ids[j])))]; IJ[t,i,j]=e; IJ[t,j,i]=e
    return l2,IJ,len(tops)

def bad_fraction(l2u,IJ):
    """vectorised: fraction of simplices whose Gram matrix is not positive definite"""
    M=l2u[IJ].copy()                              # (T,5,5) squared lengths
    idx=np.arange(5); M[:,idx,idx]=0.0            # BUGFIX: d(v,v)=0, not l2u[0]
    G=0.5*(M[:,0:1,1:]+M[:,1:,0:1]-M[:,1:,1:])    # (T,4,4)
    w=np.linalg.eigvalsh(0.5*(G+np.transpose(G,(0,2,1))))
    return float(np.mean(w[:,0]<=1e-12))

L=3
l2,IJ,NT=prep(L)
rng=np.random.default_rng(2718)
print(f"T143  realizability threshold, L={L}, {NT} simplices, {len(l2)} edges")
print(f"      flat l^2 values (units a^2): {sorted(set(np.round(l2,9)))}")
print(f"      Planck scale to mark: l_P^2/a^2 = 0.195 (spectral) to 0.265 (mode-counting)")
print()
QS=[0.02,0.05,0.08,0.10,0.13,0.16,0.195,0.22,0.25,0.30,0.35,0.45,0.60,0.80,1.00]
NTRIAL=24
print("   p(q) = fraction of simplices with no realizable geometry, mean over trials")
print(f"   {'q (a^2)':>9} {'A: +-q rough':>14} {'A: snap +-q/2':>15} {'B: length grid':>16}  {'':>3}")
for q in QS:
    pa=np.mean([bad_fraction(l2+rng.choice([-1.,1.],size=len(l2))*q,IJ) for _ in range(NTRIAL)])
    pb=np.mean([bad_fraction(l2+rng.uniform(-q/2,q/2,size=len(l2)),IJ) for _ in range(NTRIAL)])
    # scheme B: l on a grid of spacing l0, with l0^2 = q  (so l0 = sqrt(q))
    l0=np.sqrt(q)
    pc=[]
    for _ in range(NTRIAL):
        ell=np.sqrt(l2)+rng.uniform(-1e-9,1e-9,size=len(l2))
        snapped=np.round(ell/l0)*l0
        snapped=np.maximum(snapped,l0)
        pc.append(bad_fraction(snapped**2,IJ))
    mark=" <-- l_P^2" if abs(q-0.195)<1e-9 else (" <-- 0.265" if abs(q-0.265)<1e-9 else "")
    print(f"   {q:9.3f} {pa:14.4f} {pb:15.4f} {pc and np.mean(pc):16.4f}{mark}")
print()
print("   locating where p leaves zero, scheme A snap (the physical one):")
lo,hi=0.0,1.0
for _ in range(22):
    mid=0.5*(lo+hi)
    p=np.mean([bad_fraction(l2+rng.uniform(-mid/2,mid/2,size=len(l2)),IJ) for _ in range(16)])
    if p>0: hi=mid
    else:   lo=mid
print(f"      first nonzero p at q = {0.5*(lo+hi):.4f} a^2   (l_P^2 = 0.195-0.265 a^2)")
print(f"      as a length quantum: l_0 = {np.sqrt(0.5*(lo+hi)):.4f} a   vs  l_P = 0.442-0.515 a")
