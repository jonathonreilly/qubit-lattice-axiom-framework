"""C2: generic static-Z2-gauge Majorana model on a bipartite lattice (one Majorana per site, nn hopping u_ij = +-1).
Single-particle energy current B = [A^2, X] = A^2 o D (D_ij = min-image x displacement) -- derived in the report.
Checks (a) the honeycomb build of c2_kitaev_majorana agrees with A^2 o D up to a factor;
(b) 2D square and 3D cubic random-flux sectors: Drude ratio r (beta=0) and the chiral lemma <v|iB|v> = 0."""
import numpy as np
from c2_kitaev_majorana import build, drude_ratio
rng = np.random.default_rng(31)

def cubic(L, d, u_rand):
    N = L**d
    coords = np.array(np.unravel_index(np.arange(N), (L,)*d)).T
    A = np.zeros((N, N))
    for i in range(N):
        for ax in range(d):
            c = coords[i].copy(); c[ax] = (c[ax] + 1) % L
            j = np.ravel_multi_index(tuple(c), (L,)*d)
            s = (-1.0 if rng.random() < 0.5 else 1.0) if u_rand else 1.0
            A[i, j] += s; A[j, i] -= s
    dx = coords[None, :, 0] - coords[:, None, 0]
    dx = (dx + L//2) % L - L//2
    B = (A @ A) * dx
    return A, B

# (a) honeycomb cross-check of the current formula
s3 = np.sqrt(3.0)
L = 6
A, Bh, bonds = build(L)
# site x-positions
xs = np.zeros(2*L*L)
for x in range(L):
    for y in range(L):
        p = x*np.array([1, 0]) + y*np.array([0.5, s3/2])
        xs[2*(x*L+y)] = p[0]; xs[2*(x*L+y)+1] = p[0]
u = np.where(rng.random(len(bonds)) < 0.5, -1.0, 1.0)
A, Bh, _ = build(L, u=u)
A2 = A @ A
# min-image displacement along x for 2-step neighbours: use the explicit geometry via B structure
D = xs[None, :] - xs[:, None]
Lx = L*1.0
Bf = np.zeros_like(A2)
nz = np.abs(A2) > 1e-12
# choose displacement with |D| minimal modulo lattice periods a1*L, a2*L (x components L and L/2)
cands = np.stack([D + m*Lx + n*Lx/2 for m in (-1, 0, 1) for n in (-1, 0, 1)])
# pick the candidate consistent with 2-step distance (|dx| <= 1)
Dm = np.take_along_axis(cands, np.argmin(np.abs(cands), axis=0)[None], 0)[0]
Bf[nz] = (A2 * Dm)[nz]
ratio = np.sum(Bh*Bf)/np.sum(Bf*Bf)
print(f"(a) honeycomb L=6 random sector: B_build = {ratio:.6f} * (A^2 o D), residual {np.linalg.norm(Bh-ratio*Bf)/np.linalg.norm(Bh):.2e}")

for d, Ls in [(2, [6, 8, 12, 16, 20]), (3, [4, 6, 8, 10])]:
    for L in Ls:
        A, B = cubic(L, d, False)
        r0, c0 = drude_ratio(A, B, (0.0,))
        R = []; DG = []
        for s in range(4 if L**d <= 600 else 2):
            A, B = cubic(L, d, True)
            r, c = drude_ratio(A, B, (0.0,))
            w, V = np.linalg.eigh(1j*A)
            diag = np.real(np.einsum('in,ij,jn->n', V.conj(), 1j*B, V))
            gaps = np.diff(np.sort(w)); mingap = np.min(gaps)
            R.append(r[0]); DG.append(np.max(np.abs(diag))/np.linalg.norm(B)*np.sqrt(L**d))
        print(f"d={d} L={L:2d} N={L**d:5d}  uniform: r={r0[0]:.4f} comm={c0:.1e} | random u: r={np.mean(R):.2e} "
              f"max|<v|iB|v>| (rel)={np.max(DG):.1e}", flush=True)
