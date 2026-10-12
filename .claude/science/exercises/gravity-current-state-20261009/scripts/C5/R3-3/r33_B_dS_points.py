"""R3-3 (b1): an exact curved LRL on de Sitter: integral points on the quadric Q5(n) = -n0^2 + n1^2+...+n4^2 = N.
Y_N = {n in Z^5 : Q5(n) = N} is discrete and invariant under Gamma = SO(Q5)(Z) (a lattice in SO(1,4), Borel-Harish-Chandra);
X = g Y_N with g ~ Haar probability on SO(1,4)/Gamma is SO(1,4)-invariant in law (same argument as R2-2 Prop. (a)).
Checks: (1) integral reflections generate an infinite orthochronous subgroup preserving Y_N; (2) orbit/point counts;
(3) null-separated pairs (Q5(n-n') = 0) exist for this Z-form (isotropic, Meyer) -> a no-null version needs the Z[sqrt2] form;
(4) invariant pair separations: Q5(n-n') = 2N - 2B(n,n') is an even integer -> chordal separations quantized (Bragg-gap analogue
    holds for the pair-difference *values*, but null pairs are present for the Z-form)."""
import numpy as np, itertools
def Q(n): return -n[...,0]**2 + (n[...,1:]**2).sum(-1)
def B(a, b): return -a[...,0]*b[...,0] + (a[...,1:]*b[...,1:]).sum(-1)
N = 50
# (2) enumerate Y_N in a box |n0| <= T
T = 12
pts = []
for n0 in range(-T, T+1):
    r2 = N + n0*n0; r = int(np.floor(np.sqrt(r2)))
    g = np.arange(-r, r+1)
    A, Bb, C = np.meshgrid(g, g, g, indexing='ij')
    s = A**2 + Bb**2 + C**2
    for d in range(-r, r+1):
        k = s + d*d == r2
        if k.any():
            pts.append(np.stack([np.full(k.sum(), n0), A[k], Bb[k], C[k], np.full(k.sum(), d)], 1))
Y = np.concatenate(pts)
print(f"[2] N={N}: integral points on -n0^2+|n|^2=N with |n0|<={T}: {len(Y)}; check Q: {set(Q(Y).tolist())}")
cnt = [int((np.abs(Y[:, 0]) == t).sum()) for t in range(0, T+1)]
print(f"    points per |n0| slice: {cnt}")
# (1) integral reflections: r with Q(r) in {1,2}, 2B(x,r)/Q(r) integral for all integral x
def refl(x, r): return x - (2*B(x, r)//Q(r))[..., None]*r
r1 = np.array([1, 1, 1, 0, 0]); r2 = np.array([0, 1, 0, 0, 0]); r3 = np.array([1, -1, -1, 0, 0])
for r in (r1, r2, r3): print(f"    root {r.tolist()}: Q={Q(r)}")
gm = lambda x: refl(refl(x, r1), r3)   # product of two spacelike reflections: orthochronous, det +1
E = np.eye(5, dtype=int)
Mg = np.stack([gm(E[i]) for i in range(5)], 1)
J = np.diag([-1, 1, 1, 1, 1])
print(f"[1] gamma = s_r1 s_r3 (B(r1,r3) = -3: hyperbolic) integral matrix; gamma^T J gamma == J: {np.array_equal(Mg.T@J@Mg, J)}; det = {round(np.linalg.det(Mg))}; gamma00 = {Mg[0,0]}")
P = np.eye(5, dtype=int); g00 = []
for k in range(1, 7):
    P = P @ Mg; g00.append(int(P[0, 0]))
print(f"    (gamma^k)_00, k=1..6: {g00}  (unbounded -> infinite orthochronous group preserving Y_N)")
YY = (Mg @ Y.T).T
print(f"    gamma maps Y_N to integral points with Q = N: {set(Q(YY).tolist())}")
# (3)/(4) pair separations among points with small |n0|
Ys = Y[np.abs(Y[:, 0]) <= 4]
D = Ys[:, None, :] - Ys[None, :, :]
QD = Q(D)
iu = np.triu_indices(len(Ys), 1)
vals = QD[iu]
print(f"[3] pairs among {len(Ys)} points with |n0|<=4: null-separated pairs (Q(n-n')=0): {(vals==0).sum()}; "
      f"Q(n-n') values are even: {np.all(vals % 2 == 0)}; smallest |Q(n-n')|>0: {np.abs(vals[vals!=0]).min()}")
ex = np.argwhere(QD == 0)
ex = [e for e in ex if e[0] < e[1]][:3]
for i, j in ex: print(f"    null pair example: {Ys[i].tolist()} , {Ys[j].tolist()}")
# dS radius vs spacing: hyperboloid radius sqrt(N) (lattice units); local density from counts near n0 = 0
# count points with |n0|<=1 and compare with induced 4-volume of that slab ~ 2*sqrt(N)*... (leading order, dS4 of radius R: slab vol = 2 * area(S^3 of radius ~R) * dt )
R = np.sqrt(N)
slab_pts = int((np.abs(Y[:, 0]) <= 1).sum())
# proper time across |n0|<=1 at waist ~ 2 lattice units (t = n0 at waist, metric ~ -dn0^2 + R^2 dOmega3^2 for |n0| << R)
vol = 2*np.pi**2*R**3 * 3.0   # n0 in {-1,0,1}: thickness ~ 3 slices of unit spacing in n0 (counting measure), crude
print(f"[4] crude local density near the waist: {slab_pts} points in |n0|<=1 vs 4-volume ~ {vol:.0f} -> rho ~ {slab_pts/vol:.3f} per unit 4-volume;"
      f" Siegel/Hardy-Littlewood predicts rho ~ singular series / (2 sqrt N) ~ O(1/sqrt N) = {1/(2*R):.3f} x S(N)")
