"""Cubical cochain complex of Z^4 (one cell of each type per site): d with forward-difference phases.
Checks: Hodge Laplacian = phat^2 * I on all 16 components; DK D = d - d^dag squares to -Delta;
cubical Maxwell nullity on the shell; P1 scalar on the Kuhn complex equals the NN Laplacian; staggered shell."""
import itertools, numpy as np, sys
sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
CELLS = [frozenset(c) for r in range(5) for c in itertools.combinations(range(4), r)]
IDX = {c: i for i, c in enumerate(CELLS)}
def dmat(p, hol_minus=False):
    # (d w)_{S u {mu}} = sum_mu sign * (z_mu - 1) w_S ,  z_mu = e^{i p_mu}
    z = np.exp(1j*np.asarray(p, complex))
    D = np.zeros((16, 16), complex)
    for S in CELLS:
        for mu in range(4):
            if mu in S: continue
            T = S | {mu}; sign = (-1)**sum(1 for a in S if a < mu)
            D[IDX[T], IDX[S]] += sign*(z[mu] - 1)
    return D
def dstar(p):   # holomorphic adjoint: conj -> p -> -p
    return dmat(-np.asarray(p, complex)).T
def phat2(p): return np.sum(4*np.sin(np.asarray(p, complex)/2)**2)
rng = np.random.default_rng(0)
e1 = e2 = e3 = 0
for _ in range(20):
    p = rng.standard_normal(4)*1.3 + 1j*rng.standard_normal(4)*0.4
    d, ds = dmat(p), dstar(p)
    Lap = d@ds + ds@d
    e1 = max(e1, np.abs(Lap - phat2(p)*np.eye(16)).max())
    Dk = d - ds
    e2 = max(e2, np.abs(Dk@Dk + Lap).max())
    e3 = max(e3, np.abs(d@d).max())
print(f"cubical: d^2 = 0 to {e3:.1e}; d d* + d* d = phat^2 I to {e1:.1e}; (d - d*)^2 = -Delta to {e2:.1e}  (20 complex momenta)")
# doublers: zeros of phat^2 on the real BZ
grid = np.linspace(-np.pi, np.pi, 9)
m = min(phat2(np.array(q)).real for q in itertools.product(grid, repeat=4) if np.linalg.norm(q) > 1e-9)
print(f"DK zero modes on the real BZ: only p=0; min phat^2 over nonzero grid points = {m:.3f}")
# cubical Maxwell: A on 1-cells, S = |dA|^2 -> d1* d1 (4x4 restricted to 1-forms)
ones = [IDX[frozenset([m_])] for m_ in range(4)]; twos = [i for i, c in enumerate(CELLS) if len(c) == 2]
def maxwell_cub(p):
    d = dmat(p); dm = dmat(-np.asarray(p, complex))
    d1 = d[np.ix_(twos, ones)]; d1m = dm[np.ix_(twos, ones)]
    return d1m.T @ d1
mx_on = 0; mx_off = 1
for n in [(1,0,0), (1,1,0), (1,1,1), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n)
    for km in (0.3, 1.0, 2.0):
        ks = km*n; p = np.array([*ks, R.lattice_kt(ks)])
        s = R.sv(maxwell_cub(p)); mx_on = max(mx_on, s[2])
        s2 = R.sv(maxwell_cub(np.array([*ks, 1.01*R.lattice_kt(ks)]))); mx_off = min(mx_off, s2[1])
print(f"cubical Maxwell on the shell: 3 null directions (gauge + 2), 3rd sv <= {mx_on:.1e}; off shell 2nd sv >= {mx_off:.1e}")
# P1 scalar on Kuhn complex == NN Laplacian?
e4 = 0
for _ in range(10):
    p = rng.standard_normal(4)*1.5 + 1j*rng.standard_normal(4)*0.3
    e4 = max(e4, abs(R.scalar(p, np.eye(4)) - phat2(p)))
print(f"P1 scalar on the Kuhn complex = sum 4 sin^2(p/2) to {e4:.1e}")
# staggered / naive: sum sin^2 p ; its shell at p equals the Hodge shell at 2p
for n in [(1,0,0), (1,1,1)]:
    n = np.array(n, float); n /= np.linalg.norm(n); k = 0.01
    # sum sin^2(k n_i) = sinh^2(w): w^2 = k^2(1 + alpha k^2)
    for kk in (0.02, 0.01):
        w = np.arcsinh(np.sqrt(np.sum(np.sin(kk*n)**2)))
    a = lambda kk: (np.arcsinh(np.sqrt(np.sum(np.sin(kk*n)**2)))**2/kk**2 - 1)/kk**2
    print(f"naive/staggered fine-lattice alpha {tuple(n.round(3))}: {(4*a(0.01)-a(0.02))/3:+.6f} vs Hodge {-(1+(n**4).sum())/12:+.6f} (ratio {((4*a(0.01)-a(0.02))/3)/(-(1+(n**4).sum())/12):.4f})")
