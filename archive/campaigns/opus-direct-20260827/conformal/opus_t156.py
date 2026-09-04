"""T156 - THE RECORD PATTERN SWITCHES THE DIRAC CHANNELS ON.

T155 looked like bad news for R92's reading.  Imposing that the output is a
normalised state kills the DIVERGENCE channel (b=0), and the GRADIENT channel is
identically zero because sum_i n_i = 0 when every neighbour carries the same
trace.  Those are exactly two of the three channels R92 identified as the Dirac
structure.

But that computation assumed all six neighbours are alike, and the Record axiom
says otherwise: "A site with no record cannot be read."  Records form at some
sites and not others, so the neighbour conditions include WHICH neighbours carry
records.  Write o_i in {0,1} for the occupancy.  Then

        G = sum_i o_i t_i n_i = (1/2) sum_i o_i n_i

which vanishes only when the occupied directions are balanced.  For any
INHOMOGENEOUS record pattern it is nonzero, and it points along the imbalance.

That is a real structural statement and it is testable: enumerate all 2^6 = 64
occupancy patterns and measure which channels survive on each.  If the Dirac
channels are switched on precisely by record inhomogeneity, then the Record axiom
is not a passive bookkeeping clause -- it is what activates the derivative
structure.

Control: the fully-occupied and fully-empty patterns must give G = 0 exactly, and
patterns related by a cubic rotation must give the same |G| (covariance)."""
import numpy as np, itertools
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
print("T156  do the Dirac channels survive on inhomogeneous record patterns?")
print()
rows={}
for occ in itertools.product([0,1],repeat=6):
    k=sum(occ)
    G=0.5*sum(occ[i]*DIRS[i] for i in range(6))
    rows.setdefault(k,[]).append((occ,np.linalg.norm(G)))
print(f"   {'#records':>9} {'patterns':>9} {'|G| = |(1/2) sum o_i n_i|':>28}")
for k in sorted(rows):
    vals=np.array([v for _,v in rows[k]])
    u=sorted(set(np.round(vals,9)))
    print(f"   {k:9d} {len(rows[k]):9d}   {'values: '+', '.join(f'{x:.4f}' for x in u):>26}")
print()
print("   CONTROL: fully empty and fully occupied must both give exactly 0")
print(f"      k=0 -> {rows[0][0][1]:.1e}      k=6 -> {rows[6][0][1]:.1e}")
print()
print("   CONTROL: covariance -- patterns in the same octahedral orbit share |G|")
def orbit_ok():
    def rot_perm(R):
        P=[]
        for j,d in enumerate(DIRS):
            rd=R@d; P.append([k for k,e in enumerate(DIRS) if np.allclose(e,rd)][0])
        return P
    ROT=[]
    for perm in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,p in enumerate(perm): M[i,p]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: ROT.append(M)
    bad=0
    Gof={}
    for occ in itertools.product([0,1],repeat=6):
        Gof[occ]=np.linalg.norm(0.5*sum(occ[i]*DIRS[i] for i in range(6)))
    for occ in Gof:
        for R in ROT:
            P=rot_perm(R)
            occ2=tuple(occ[P.index(i)] for i in range(6)) if False else tuple(occ[j] for j in [P.index(i) for i in range(6)])
            if abs(Gof[occ]-Gof[occ2])>1e-12: bad+=1
    return bad
print(f"      covariance violations across all 64 patterns x 24 rotations: {orbit_ok()}")
print()
print("   Now the DIVERGENCE channel on an inhomogeneous pattern.")
rng=np.random.default_rng(3)
print(f"   {'#records':>9} {'max |D| over random spins':>28}")
for k in range(7):
    best=0.0
    for occ in [o for o in itertools.product([0,1],repeat=6) if sum(o)==k]:
        for _ in range(2000):
            D=0.0
            for i in range(6):
                if not occ[i]: continue
                u=rng.normal(size=3); u/=np.linalg.norm(u); v=0.5*u
                D+=DIRS[i]@v
            best=max(best,abs(D))
    print(f"   {k:9d} {best:28.4f}")
print()
print("   |G| nonzero exactly for unbalanced occupancy = the Record axiom's")
print("   formation pattern is what turns on the gradient channel.")
