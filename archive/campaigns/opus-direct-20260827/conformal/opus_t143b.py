"""T143b - realizability threshold, with T143's bug fixed.

T143 returned p = 1.0000 at every quantum including q = 0.02, contradicting
T142b's 12/12-realizable at q = 0.1 and 0.01.  My bug: building the (T,5,5)
squared-distance array by fancy-indexing an edge-index array whose DIAGONAL was
never set, so IJ[t,i,i] defaulted to 0 and M[t,i,i] became the squared length of
edge 0 instead of zero.  Every Gram matrix was corrupted.  Fixed by zeroing the
diagonal, and sanity-checked against the flat lattice (must give exactly 0) and
against a deliberately impossible configuration (must give > 0)."""
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

IDX=np.arange(5)
def bad_fraction(l2u,IJ):
    M=l2u[IJ].copy(); M[:,IDX,IDX]=0.0
    G=0.5*(M[:,0:1,1:]+M[:,1:,0:1]-M[:,1:,1:])
    w=np.linalg.eigvalsh(0.5*(G+np.transpose(G,(0,2,1))))
    return float(np.mean(w[:,0]<=1e-12))

L=3
l2,IJ,NT=prep(L)
print(f"T143b  L={L}, {NT} simplices, {len(l2)} edges")
print(f"   SANITY  flat lattice p = {bad_fraction(l2,IJ):.6f}  (must be exactly 0)")
print(f"   SANITY  all l^2 = 1     p = {bad_fraction(np.ones_like(l2),IJ):.6f}  (must be > 0)")
print(f"   SANITY  l^2 scaled x9   p = {bad_fraction(9*l2,IJ):.6f}  (similarity: must be 0)")
print()
rng=np.random.default_rng(2718)
QS=[0.02,0.05,0.08,0.10,0.13,0.16,0.195,0.22,0.25,0.265,0.30,0.35,0.45,0.60,0.80,1.00]
NTRIAL=24
print("   p(q) = fraction of simplices with NO realizable geometry")
print(f"   {'q (a^2)':>9} {'A: +-q rough':>14} {'A: snap +-q/2':>15} {'B: length grid':>16}")
res={}
for q in QS:
    pa=np.mean([bad_fraction(l2+rng.choice([-1.,1.],size=len(l2))*q,IJ) for _ in range(NTRIAL)])
    pb=np.mean([bad_fraction(l2+rng.uniform(-q/2,q/2,size=len(l2)),IJ) for _ in range(NTRIAL)])
    l0=np.sqrt(q); pc=[]
    for _ in range(NTRIAL):
        ell=np.sqrt(l2)
        sn=np.maximum(np.round(ell/l0),1.0)*l0
        pc.append(bad_fraction(sn**2,IJ))
    res[q]=(pa,pb,np.mean(pc))
    mk=" <-- l_P^2 (spectral)" if q==0.195 else (" <-- l_P^2 (mode-count)" if q==0.265 else "")
    print(f"   {q:9.3f} {pa:14.5f} {pb:15.5f} {np.mean(pc):16.5f}{mk}")
print()
for nm,fn in (("A rough (+-q)",lambda q: rng.choice([-1.,1.],size=len(l2))*q),
              ("A snap (+-q/2)",lambda q: rng.uniform(-q/2,q/2,size=len(l2)))):
    lo,hi=0.0,2.0
    for _ in range(26):
        mid=0.5*(lo+hi)
        p=np.mean([bad_fraction(l2+fn(mid),IJ) for _ in range(12)])
        if p>0: hi=mid
        else:   lo=mid
    qc=0.5*(lo+hi)
    print(f"   threshold, {nm:<16}: q* = {qc:.4f} a^2   -> length quantum l_0 = {np.sqrt(qc):.4f} a")
print()
print(f"   for comparison  l_P^2 = 0.195-0.265 a^2,  l_P = 0.442-0.515 a")
print(f"   resolution floor: p < 1/{NT} = {1.0/NT:.2e} is indistinguishable from zero here")
