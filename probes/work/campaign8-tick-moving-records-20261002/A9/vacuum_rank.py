"""A9 task 2/5: can a local effect F >= 0 annihilate a candidate vacuum?

F_x >= 0 with <vac|F_x|vac> = 0 exists (F != 0) iff the vacuum's marginal on the
support of F (the star: site + 6 neighbours) is rank-deficient. The minimal
vacuum ("dark") rate of a rank-r effect is the sum of the r smallest eigenvalues
of that marginal (Ky Fan). Supplied candidate vacua, nothing adopted:

 (a) half-filled staggered (Kogut-Susskind) fermion sea on an L^3 torus with
     antiperiodic boundaries, massless and with staggered mass m; star marginal
     from the restricted correlation matrix C_A (Gaussian state).
 (b) spin-1/2 antiferromagnetic Heisenberg ground states: 1D ring N=16 (3-site
     star) and 2D 4x4 torus (5-site star); exact diagonalisation.
 (c) Klein-type valence-bond check: P_{7/2}(star) on a superposition of
     nearest-neighbour singlet coverings around the star (14 qubits).
 (d) permanent floor: symmetric-subspace weight of 7-qubit product states.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import itertools
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

rng = np.random.default_rng(7)


# ---------------- (a) staggered sea ----------------
def staggered_sea_star(L, m=0.0):
    N = L ** 3
    idx = lambda x1, x2, x3: ((x1 % L) * L + (x2 % L)) * L + (x3 % L)
    h = np.zeros((N, N), complex)
    for x1 in range(L):
        for x2 in range(L):
            for x3 in range(L):
                i = idx(x1, x2, x3)
                eta = (1, (-1) ** x1, (-1) ** (x1 + x2))
                h[i, i] += m * (-1) ** (x1 + x2 + x3)
                for mu, step in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    y = (x1 + step[0], x2 + step[1], x3 + step[2])
                    wrap = (y[mu] == L)
                    s = -1.0 if wrap else 1.0  # antiperiodic boundary
                    j = idx(*y)
                    amp = 0.5j * eta[mu] * s
                    h[j, i] += amp
                    h[i, j] += np.conj(amp)
    e, v = np.linalg.eigh(h)
    occ = v[:, e < 0]
    nz = np.min(np.abs(e))
    c0 = (L // 2, L // 2, L // 2)
    star = [idx(*c0)] + [idx(c0[0] + d[0], c0[1] + d[1], c0[2] + d[2]) for d in
                         ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
    CA = occ[star] @ occ[star].conj().T
    nu = np.linalg.eigvalsh(CA)
    return occ.shape[1], nz, nu


def gaussian_spectrum(nu):
    vals = []
    for bits in itertools.product((0, 1), repeat=len(nu)):
        vals.append(np.prod([n if b else 1 - n for n, b in zip(nu, bits)]))
    return np.sort(np.array(vals))


def star_C_kspace(L, m=0.0):
    """C_A = (1 - (H + m eps) |H_m|^{-1})/2 on the star, using (H + m eps)^2 = sum sin^2 k + m^2.
    |H_m|^{-1} kernel G(r) = L^-3 sum_k e^{ik.r} / sqrt(m^2 + sum_mu sin^2 k_mu), APBC momenta."""
    k1 = np.pi * (2 * np.arange(L) + 1) / L
    s2 = np.sin(k1) ** 2
    E = np.sqrt(m * m + s2[:, None, None] + s2[None, :, None] + s2[None, None, :])
    def G(r):
        ph = (np.exp(1j * k1 * r[0])[:, None, None] * np.exp(1j * k1 * r[1])[None, :, None]
              * np.exp(1j * k1 * r[2])[None, None, :])
        return np.real(np.sum(ph / E)) / L ** 3
    c0 = np.array([L // 2] * 3)
    dirs = [np.array(d) for d in ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
    star = [c0 + d for d in dirs]
    eta = lambda x, mu: (1, (-1) ** x[0], (-1) ** (x[0] + x[1]))[mu]
    eps = lambda x: (-1) ** int(x.sum())
    unit = [np.array(u) for u in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    # (H f)(x) = (i/2) sum_mu eta_mu(x) [f(x - mu) - f(x + mu)]; f = G(. - y)
    A = np.zeros((7, 7), complex)
    for a, x in enumerate(star):
        for b, y in enumerate(star):
            val = m * eps(x) * G(x - y)
            for mu in range(3):
                val += 0.5j * eta(x, mu) * (G(x - unit[mu] - y) - G(x + unit[mu] - y))
            A[a, b] = val
    C = (np.eye(7) - A) / 2
    return np.linalg.eigvalsh((C + C.conj().T) / 2)


print("(a) half-filled staggered sea, 7-site star, antiperiodic L^3 torus")
for m in (0.0, 0.5):
    for L in (6, 8):
        nocc, gap, nu = staggered_sea_star(L, m)
        nuk = star_C_kspace(L, m)
        print(f"  dense vs k-space m={m:3.1f} L={L}: filled={nocc}/{L**3}, min|E|={gap:.3f}, "
              f"max|nu_dense - nu_k| = {np.max(np.abs(np.sort(nu) - np.sort(nuk))):.2e}")
    for L in (8, 12, 16, 24, 32, 48):
        nu = star_C_kspace(L, m)
        spec = gaussian_spectrum(nu)
        print(f"  m={m:3.1f} L={L:2d} nu=[{', '.join(f'{x:.4f}' for x in nu)}] "
              f"min eig rho_A={spec[0]:.3e} sum8={spec[:8].sum():.3e} sum32={spec[:32].sum():.3e} "
              f"sum96={spec[:96].sum():.3e} tr={spec.sum():.6f}")


# ---------------- (b) Heisenberg antiferromagnet ----------------
def heisenberg(nsites, bonds, J=1.0):
    dim = 2 ** nsites
    s = np.arange(dim)
    diag = np.zeros(dim)
    rows, cols, vals = [], [], []
    for i, j in bonds:
        bi = (s >> i) & 1
        bj = (s >> j) & 1
        diag += J * 0.25 * (1 - 2 * bi) * (1 - 2 * bj)
        flip = bi != bj
        rows.append(s[flip]); cols.append(s[flip] ^ ((1 << i) | (1 << j)))
        vals.append(np.full(flip.sum(), 0.5 * J))
    rows = np.concatenate(rows + [s]); cols = np.concatenate(cols + [s])
    vals = np.concatenate(vals + [diag])
    return sp.csr_matrix((vals, (rows, cols)), shape=(dim, dim))


def reduced(psi, nsites, keep):
    t = psi.reshape([2] * nsites)  # axis k <-> bit (nsites-1-k)
    axes = [nsites - 1 - q for q in keep]
    rest = [a for a in range(nsites) if a not in axes]
    m = np.transpose(t, axes + rest).reshape(2 ** len(keep), -1)
    return m @ m.conj().T


print("(b) antiferromagnetic Heisenberg ground states")
N1 = 16
bonds1 = [(i, (i + 1) % N1) for i in range(N1)]
H1 = heisenberg(N1, bonds1)
e1, v1 = eigsh(H1, k=2, which="SA")
g1 = v1[:, np.argmin(e1)]
r1 = reduced(g1, N1, [0, 1, N1 - 1])
w1 = np.linalg.eigvalsh(r1)
print(f"  1D ring N=16: E0/N={e1.min()/N1:.6f} gap={abs(e1[1]-e1[0]):.4f}; 3-site star marginal eigenvalues "
      f"min={w1.min():.4e} max={w1.max():.4e}")
Lx = 4
site = lambda a, b: (a % Lx) * Lx + (b % Lx)
bonds2 = []
for a in range(Lx):
    for b in range(Lx):
        bonds2.append((site(a, b), site(a + 1, b)))
        bonds2.append((site(a, b), site(a, b + 1)))
H2 = heisenberg(16, bonds2)
e2, v2 = eigsh(H2, k=2, which="SA")
g2 = v2[:, np.argmin(e2)]
star2 = [site(1, 1), site(2, 1), site(0, 1), site(1, 2), site(1, 0)]
r2 = reduced(g2, 16, star2)
w2 = np.linalg.eigvalsh(r2)
# total-spin-5/2 weight of the star (fully symmetric sector)
Sx = np.array([[0, 1], [1, 0]]) / 2; Sy = np.array([[0, -1j], [1j, 0]]) / 2; Sz = np.diag([0.5, -0.5])
def total_S2(n):
    tot = [np.zeros((2 ** n, 2 ** n), complex) for _ in range(3)]
    for k in range(n):
        for c, S in enumerate((Sx, Sy, Sz)):
            op = np.array([[1.0]])
            for q in range(n):
                op = np.kron(op, S if q == k else np.eye(2))
            tot[c] += op
    return sum(t @ t for t in tot)
S2_5 = total_S2(5)
lam, vec = np.linalg.eigh(S2_5)
Pmax5 = vec[:, np.isclose(lam, 2.5 * 3.5)] @ vec[:, np.isclose(lam, 2.5 * 3.5)].conj().T
print(f"  2D 4x4 torus: E0/N={e2.min()/16:.6f} gap={abs(e2[1]-e2[0]):.4f}; 5-site star marginal eigenvalues "
      f"min={w2.min():.4e} max={w2.max():.4e}; weight in star spin 5/2 = {np.trace(Pmax5 @ r2).real:.4e}")


# ---------------- (c) Klein-type check ----------------
# qubits: 0 = centre x, 1..6 = neighbours, 7..12 = outside partners o_1..o_6, 13 = extra site z.
# covering_j: singlet(x, n_j); singlet(n_i, o_i) for i != j; singlet(o_j, z). Each is a global singlet.
def singlet_pairs_state(pairs, free, n=14):
    psi = np.zeros(2 ** n, complex)
    sing = {(0, 1): 1 / np.sqrt(2), (1, 0): -1 / np.sqrt(2)}
    for choice in itertools.product(sing.items(), repeat=len(pairs)):
        bits = [0] * n
        amp = 1.0
        for (a, b), ((u, w), c) in zip(pairs, choice):
            bits[a], bits[b] = u, w
            amp *= c
        for f in free:
            bits[f] = 0
        k = sum(bq << q for q, bq in enumerate(bits))  # qubit q <-> bit q (same as heisenberg())
        psi[k] += amp
    return psi

coverings = []
for j in range(1, 7):
    pairs = [(0, j)] + [(i, 6 + i) for i in range(1, 7) if i != j] + [(6 + j, 13)]
    coverings.append(singlet_pairs_state(pairs, free=[]))
amps = rng.normal(size=6) + 1j * rng.normal(size=6)
sup = sum(a * c for a, c in zip(amps, coverings))
sup /= np.linalg.norm(sup)
S2_7 = total_S2(7)
lam7, vec7 = np.linalg.eigh(S2_7)
sel = np.isclose(lam7, 3.5 * 4.5)
P72 = vec7[:, sel] @ vec7[:, sel].conj().T
print(f"(c) Klein check: dim S=7/2 sector = {sel.sum()} (expect 8)")
for k, c in enumerate(coverings, 1):
    rs = reduced(c / np.linalg.norm(c), 14, list(range(7)))
    if k in (1, 6):
        print(f"  covering x-n{k}: <P_7/2(star)> = {np.trace(P72 @ rs).real:.2e}")
rs = reduced(sup, 14, list(range(7)))
print(f"  random superposition of the 6 coverings: <P_7/2(star)> = {np.trace(P72 @ rs).real:.2e}; "
      f"single-site marginal of x = {np.round(reduced(sup, 14, [0]).real, 6).tolist()}")


# ---------------- (d) permanent floor for product states ----------------
def sym_weight(vecs):
    psi = np.array([1.0 + 0j])
    for v in vecs:
        psi = np.kron(psi, v)
    return float(np.real(np.vdot(psi, P72 @ psi)))

def bloch(th, ph):
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])

best = 1.0
for _ in range(20000):
    th = np.arccos(rng.uniform(-1, 1, 7)); ph = rng.uniform(0, 2 * np.pi, 7)
    best = min(best, sym_weight([bloch(a, b) for a, b in zip(th, ph)]))
from scipy.optimize import minimize
fun = lambda z: sym_weight([bloch(a, b) for a, b in zip(z[:7], z[7:])])
opt = min((minimize(fun, np.concatenate([np.arccos(rng.uniform(-1, 1, 7)), rng.uniform(0, 2 * np.pi, 7)]),
                    method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-12})
           for _ in range(12)), key=lambda r: r.fun)
ud = sym_weight([bloch(0, 0)] * 4 + [bloch(np.pi, 0)] * 3)
print(f"(d) 7-qubit product states: min symmetric weight, random search = {best:.4e}; "
      f"local optimisation = {opt.fun:.4e}; 4 up + 3 down = {ud:.4e} (1/35 = {1/35:.4e}); "
      f"Marcus floor 1/7! = {1/5040:.4e}")
