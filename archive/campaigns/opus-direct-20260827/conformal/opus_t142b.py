"""T142b - the realizability question, done properly.

T142(1) perturbed ALL 3840 edges simultaneously by +-q and found every neighbour
degenerate at q = 1 and 0.25.  That is a maximally aggressive move, not a nearest
neighbour, so the conclusion was overstated by my own probe design.  Redo it with
SINGLE-EDGE moves, which is what 'the nearest allowed configuration' means.

The underlying question is realizability: a set of squared edge lengths describes
an actual Euclidean simplex only if its Gram matrix is positive definite (the
triangle inequality, generalised).  Quantizing l^2 to a grid does not just make
the configuration space discrete -- it may make most grid points EMPTY.  That is
the real issue, and it is decidable by counting."""
import numpy as np, itertools, sys
sys.path.insert(0,"/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad")
from opus_t114b import build

L=3
verts,vid,tops,edges,emid,edir,base_len=build(L)
h=1.0/L
l2=np.array([base_len[e]**2 for e in range(len(base_len))])/h**2     # units of a^2
print(f"T142b  realizability of quantized geometries.  L={L}, {len(edges)} edges, {len(tops)} simplices")
print(f"       flat squared edge lengths (units a^2): {sorted(set(np.round(l2,9)))}  -- already integers")
print()
def realizable(l2u):
    """is every simplex geometrically realizable?  Gram matrix positive definite."""
    bad=0
    for ids,P in tops:
        M=[[0.0]*5 for _ in range(5)]
        for i,j in itertools.combinations(range(5),2):
            x=l2u[edges[tuple(sorted((ids[i],ids[j])))]]; M[i][j]=M[j][i]=x
        G=np.empty((4,4))
        for a in range(4):
            for b in range(4): G[a,b]=0.5*(M[0][a+1]+M[0][b+1]-M[a+1][b+1])
        if np.linalg.eigvalsh(G).min()<=1e-12: bad+=1
    return bad

print("   SINGLE-EDGE moves: change one edge by one quantum q, is the geometry still realizable?")
print(f"   {'q':>8} {'edges tried':>12} {'+q realizable':>15} {'-q realizable':>15}")
rng=np.random.default_rng(9)
for q in (1.0,0.5,0.25,0.1,0.01):
    trial=rng.choice(len(l2),size=40,replace=False)
    okp=okm=0
    for e in trial:
        for sgn,acc in ((+1,'p'),(-1,'m')):
            v=l2.copy(); v[e]+=sgn*q
            if v[e]<=0: continue
            if realizable(v)==0:
                if sgn>0: okp+=1
                else: okm+=1
    print(f"   {q:8g} {len(trial):12d} {okp:>10}/{len(trial)} {okm:>10}/{len(trial)}")
print()
print("   Now the density question: what fraction of a RANDOM integer assignment")
print("   near flat is realizable?  (all edges perturbed, so the aggressive move --")
print("   this is what T142(1) actually measured, correctly labelled this time)")
print(f"   {'q':>8} {'trials':>8} {'fully realizable':>18} {'mean bad simplices':>20}")
for q in (1.0,0.25,0.1,0.05,0.01):
    ok=0; bad=[]
    for _ in range(12):
        v=l2+rng.choice([-1.0,1.0],size=len(l2))*q
        if np.any(v<=0): bad.append(len(tops)); continue
        b=realizable(v); bad.append(b)
        if b==0: ok+=1
    print(f"   {q:8g} {12:8d} {ok:>13}/12     {np.mean(bad):20.1f} of {len(tops)}")
print()
print("   Single-edge moves surviving while all-edge moves fail = the quantized space")
print("   is connected but sparse; single-edge moves ALSO failing at q~1 would mean")
print("   integer l^2 gives isolated points with no geometry between them.")
