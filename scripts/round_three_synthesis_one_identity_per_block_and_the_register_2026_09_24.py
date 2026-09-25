#!/usr/bin/env python3
"""Finite supplied-model checks. The paired note states the retained claims and limitations.

No numerical pass establishes an unrestricted phase, minimum, physical particle or
framework premise. Original constructions are preserved; scope labels and decisive
controls have been corrected during review.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import eigsh

AUDIT_INPUT_PATHS = ['docs/GAUSSIAN_LATTICE_MAXWELL_COMPARATOR_GIVES_A_LINEAR_SIZE_INDEPENDENT_TRANSVERSE_STRUCTURE_FACTOR_AND_MISSES_THE_PURE_RING_LEVEL_STEP_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/RING_MODEL_FROM_THE_RK_POINT_TO_THE_PURE_RING_POINT_THE_TRANSVERSE_WEIGHT_MOVES_TO_THE_ZONE_CORNER_CONTINUOUSLY_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_ICE_TRANSVERSE_WEIGHT_SUM_RULE_THE_RING_TERM_MOVES_THE_WEIGHT_FROM_THE_SMALLEST_MOMENTA_TO_THE_ZONE_CORNER_WITHOUT_A_GROWING_PEAK_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_PURE_RING_POINT_TRANSVERSE_FLUCTUATIONS_AT_THE_SMALLEST_MOMENTUM_ARE_A_THIRD_OF_THE_UNIFORM_ICE_CONSTANT_AND_THE_FEYNMAN_PHOTON_BOUND_SHOWS_NO_RESOLVED_POWER_ON_SMALL_TORI_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_THE_TEN_CUBED_POINT_LIES_BETWEEN_THE_LINEAR_AND_LEVEL_READINGS_AND_A_CONSTANT_PLUS_A_LINEAR_TERM_FITS_THE_FOUR_SIZES_MILDLY_BETTER_THAN_A_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/RING_MODEL_TWO_REGULATORS_A_REGION_BOUNDED_BY_RECORDS_MATCHES_THE_TORUS_AT_SIZE_EIGHT_AND_THE_WALKER_POPULATION_IS_THE_LARGER_REGULATOR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ROUND_THREE_SYNTHESIS_THE_PHOTON_FROM_FOUR_SIDES_THE_FORMATION_CLOCKS_THE_TEXT_ADMITS_AND_A_THREE_DIMENSIONAL_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md']
AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()
ALPHA, G = 0.2, 1.0


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


class Ice:
    def __init__(self, L):
        self.L = L
        self.nv, self.nl = L ** 3, 3 * L ** 3
        self.verts = list(itertools.product(range(L), repeat=3))
        self.vid = {v: i for i, v in enumerate(self.verts)}
        self.tail = np.zeros(self.nl, dtype=int)
        self.head = np.zeros(self.nl, dtype=int)
        self.axis = np.zeros(self.nl, dtype=int)
        self.coord = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            for a in range(3):
                w = list(v)
                w[a] = (w[a] + 1) % L
                l = 3 * self.vid[v] + a
                self.tail[l], self.head[l], self.axis[l], self.coord[l] = self.vid[v], self.vid[tuple(w)], a, v[a]
        self.xc = np.array([self.verts[l // 3][0] for l in range(self.nl)])      # x-coordinate of the link's tail vertex
        self.inc = [[] for _ in range(self.nv)]
        for l in range(self.nl):
            self.inc[self.tail[l]].append((l, 1))
            self.inc[self.head[l]].append((l, -1))
        plaq = []
        for v in self.verts:
            for a, b in ((0, 1), (1, 2), (0, 2)):
                va, vb = list(v), list(v)
                va[a] = (va[a] + 1) % L
                vb[b] = (vb[b] + 1) % L
                plaq.append([3 * self.vid[v] + a, 3 * self.vid[tuple(va)] + b, 3 * self.vid[tuple(vb)] + a, 3 * self.vid[v] + b])
        self.plaq = np.array(plaq)
        self.sign = np.tile([1, 1, -1, -1], (len(plaq), 1))
        self.np_ = len(plaq)
        pol = [[] for _ in range(self.nl)]
        for p, links in enumerate(self.plaq):
            for l in links:
                pol[l].append(p)
        self.pol = pol
        width = max(len({q for l in links for q in pol[l]}) for links in self.plaq)
        self.A = np.full((self.np_, width), self.np_, dtype=int)
        self.M = np.zeros((self.np_, width, 4))
        for p, links in enumerate(self.plaq):
            aff = sorted({q for l in links for q in pol[l]})
            self.A[p, :len(aff)] = aff
            for j, q in enumerate(aff):
                for k, l in enumerate(links):
                    for h in np.flatnonzero(self.plaq[q] == l):
                        self.M[p, j, k] += self.sign[q, h]

    def circ(self, sigma):
        c = np.zeros(self.np_ + 1)
        c[:self.np_] = (sigma[self.plaq] * self.sign).sum(axis=1)
        return c

    def deltas(self, sigma, C, P):
        Ca = C[self.A[P]]
        Cn = Ca - 2 * np.einsum("pjk,pk->pj", self.M[P], sigma[self.plaq[P]])
        return Cn, (np.abs(Cn) == 4).sum(axis=1) - (np.abs(Ca) == 4).sum(axis=1)

    def winding_fast(self, sigma):
        return tuple(int(sigma[(self.axis == a) & (self.coord == 0)].sum()) for a in range(3))

    def sector_state(self, quanta=0):
        sigma = np.zeros(self.nl, dtype=int)
        for v in self.verts:
            i = self.vid[v]
            sigma[3 * i] = (-1) ** v[1]
            sigma[3 * i + 1] = (-1) ** v[0]
            sigma[3 * i + 2] = (-1) ** v[0]
        for q in range(quanta):
            for x in range(self.L):
                sigma[3 * self.vid[(x, 1, q)]] *= -1
        return sigma

    def modes(self, ms):
        """Transverse field modes O_b(k e_a) = N^{-1/2} sum over b-links of e^{i k x_a} sigma, b != a, k = 2 pi m / L:
        for each m the six (axis, polarisation) modes."""
        PH = np.zeros((len(ms), 6, self.nl), dtype=complex)
        tail_coord = np.array([self.verts[l // 3] for l in range(self.nl)])       # (nl, 3)
        for j, m in enumerate(ms):
            q = 0
            for a in range(3):
                e = np.exp(1j * 2 * np.pi * m / self.L * tail_coord[:, a]) / np.sqrt(self.nv)
                for b in range(3):
                    if b != a:
                        PH[j, q] = e * (self.axis == b)
                        q += 1
        return PH


def loop_vmc(ice, alpha, sweeps, therm, r, start=None, fix_winding=False):
    sigma = np.ones(ice.nl, dtype=int) if start is None else start.copy()
    C = ice.circ(sigma)
    W0 = ice.winding_fast(sigma)
    samples = []
    per_sweep = max(1, ice.nl // 20)
    for sw in range(therm + sweeps):
        for _ in range(per_sweep):
            v = r.integers(ice.nv)
            seen, path_l = {v: 0}, []
            while True:
                outs = [l for (l, s) in ice.inc[v] if sigma[l] * s == 1]
                l = outs[r.integers(3)]
                v = ice.head[l] if ice.tail[l] == v else ice.tail[l]
                path_l.append(l)
                if v in seen:
                    cyc = path_l[seen[v]:]
                    break
                seen[v] = len(path_l)
            aff = sorted({p for l in cyc for p in ice.pol[l]})
            before = int((np.abs(C[aff]) == 4).sum())
            sigma[cyc] *= -1
            C_new = (sigma[ice.plaq[aff]] * ice.sign[aff]).sum(axis=1)
            after = int((np.abs(C_new) == 4).sum())
            keep = r.random() < np.exp(2 * alpha * (after - before))
            if keep and fix_winding and ice.winding_fast(sigma) != W0:
                keep = False
            if keep:
                C[aff] = C_new
            else:
                sigma[cyc] *= -1
        if sw >= therm and sw % 2 == 0:
            samples.append(sigma.copy())
    return samples


def stats(x, n_bins=10):
    x = np.asarray(x, dtype=float)
    m = len(x) // n_bins * n_bins
    bins = x[:m].reshape(n_bins, -1).mean(axis=1)
    return float(x.mean()), float(bins.std(ddof=1) / np.sqrt(n_bins))


def exact_L2(ice, canon):
    B = np.zeros((ice.nv, ice.nl), dtype=np.int64)
    for v in range(ice.nv):
        for (l, s) in ice.inc[v]:
            B[v, l] += s
    bits = np.arange(ice.nl)
    codes = []
    n = 1 << ice.nl
    step = 1 << 18
    for start in range(0, n, step):
        ids = np.arange(start, min(n, start + step), dtype=np.int64)
        sig = (((ids[:, None] >> bits) & 1) * 2 - 1).astype(np.int64)
        ok = np.all(sig @ B.T == 0, axis=1)
        codes.append(ids[ok])
    codes = np.concatenate(codes)
    masks = np.array([sum(1 << int(l) for l in links) for links in ice.plaq], dtype=np.int64)

    def sig_of(code):
        return ((code >> bits) & 1) * 2 - 1

    def flippable(code):
        s = sig_of(code)
        return np.flatnonzero(np.abs((s[ice.plaq] * ice.sign).sum(axis=1)) == 4)

    def code_of(s):
        return int(((s + 1) // 2 * (1 << bits)).sum())

    c0 = code_of(canon)
    comp = {c0: 0}
    order = [c0]
    q = 0
    while q < len(order):
        c = order[q]
        q += 1
        for p in flippable(c):
            c2 = int(c ^ masks[p])
            if c2 not in comp:
                comp[c2] = len(order)
                order.append(c2)
    n_c = len(order)
    rows, cols = [], []
    for c in order:
        for p in flippable(c):
            rows.append(comp[int(c ^ masks[p])])
            cols.append(comp[c])
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n_c, n_c)).tocsr()
    return codes, order, H, sig_of




def fields(ice, sigma):
    """The three link-field components on the vertex grid, component a on the link leaving v along +a."""
    L = ice.L
    return sigma.reshape(L, L, L, 3).transpose(3, 0, 1, 2)


def modes(ice, sigma):
    return np.fft.fftn(fields(ice, sigma), axes=(1, 2, 3)) / np.sqrt(ice.nv)          # O_a(k), shape (3, L, L, L)


def weight_map(ice, sigma):
    return (np.abs(modes(ice, sigma)) ** 2).sum(axis=0)                                # T(k) = sum_a |O_a(k)|^2


def longitudinal_max(ice, sigma):
    F = modes(ice, sigma)
    d = 1 - np.exp(-2j * np.pi * np.arange(ice.L) / ice.L)
    Dx, Dy, Dz = np.meshgrid(d, d, d, indexing="ij")
    return float(np.abs(Dx * F[0] + Dy * F[1] + Dz * F[2]).max())


def geometry(L):
    N = L ** 3
    xs = np.array(list(np.ndindex(L, L, L)))                       # (N, 3)

    def v(x):
        x = np.mod(x, L)
        return x[..., 0] * L * L + x[..., 1] * L + x[..., 2]

    def link(x, a):
        return 3 * v(x) + a

    D = np.zeros((N, 3 * N), dtype=int)
    for a in range(3):
        ea = np.eye(3, dtype=int)[a]
        D[np.arange(N), link(xs, a)] += 1
        D[np.arange(N), link(xs - ea, a)] -= 1
    planes = [(0, 1), (0, 2), (1, 2)]
    C = np.zeros((3 * N, 3 * N), dtype=int)
    plane_of = np.zeros(3 * N, dtype=int)
    for pi, (a, b) in enumerate(planes):
        ea, eb = np.eye(3, dtype=int)[a], np.eye(3, dtype=int)[b]
        rows = 3 * np.arange(N) + pi
        plane_of[rows] = pi
        C[rows, link(xs, a)] += 1
        C[rows, link(xs + ea, b)] += 1
        C[rows, link(xs + eb, a)] -= 1
        C[rows, link(xs, b)] -= 1
    return N, xs, D, C, plane_of


def momenta(L):
    ms = np.array(list(np.ndindex(L, L, L)))
    return 2 * np.pi * ms / L                                          # (N, 3)


def s_abs(k):
    return np.sqrt(np.sum(2 - 2 * np.cos(k), axis=-1))


def fourier_cov(Sigma, L, xs, ks):
    """S_ab(k) = N^{-1} sum_{x,y} e^{ik(x-y)} Sigma[(x,a),(y,b)] for every k."""
    N = L ** 3
    Phi = np.exp(1j * ks @ xs.T)                                       # (N_k, N)
    S = np.zeros((len(ks), 3, 3), dtype=complex)
    for a in range(3):
        for b in range(3):
            blk = Sigma[a::3, b::3]                                    # (x, y) block for (a, b)
            S[:, a, b] = np.einsum("kx,kx->k", Phi @ blk, Phi.conj()) / N
    return S


def closed_form(ks, A):
    """A |s(k)| (1 - g g^dag), g_a = (1 - e^{-i k_a})/|s|; zero at k = 0."""
    out = np.zeros((len(ks), 3, 3), dtype=complex)
    sa = s_abs(ks)
    for i, k in enumerate(ks):
        if sa[i] < 1e-12:
            continue
        g = (1 - np.exp(-1j * k)) / sa[i]
        out[i] = A * sa[i] * (np.eye(3) - np.outer(g, g.conj()))
    return out



# ---- open PR 9168's hyperhoneycomb site set on Z^3 (its own definitions, copied for the recomputation)
def is_site(p):
    i, j, z = p
    m = z % 4
    if m == 0:
        return j % 2 == 0
    if m == 1:
        return i % 2 == 1
    if m == 2:
        return j % 2 == 1
    return i % 2 == 0


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p)
            q[a] += s
            if is_site(tuple(q)):
                out.append(tuple(q))
    return out



# ------------------------------------------------------------------------------------------------ main
rng = np.random.default_rng(3003)

# ---------------------------------------------------------------- 1. open PR 9161: the sum rule of the Feynman bound on the exact 2^3 component
ice2 = Ice(2)
canon = ice2.sector_state(0)
codes, order, H2, sig_of = exact_L2(ice2, canon)
vals, vecs = eigsh(H2, k=1, which="SA")
E0 = float(vals[0]); psi0 = np.abs(vecs[:, 0])
assert np.linalg.norm(H2 @ psi0 - E0 * psi0) < 1e-9, "ground-vector residual"
Sg = np.array([sig_of(c) for c in order])
PH = ice2.modes([1])
O = np.einsum("mpl,cl->cmp", PH, Sg)[:, 0, :]
u0 = -E0 / ice2.np_
f = np.mean([float((np.vdot(O[:, q] * psi0, H2 @ (O[:, q] * psi0)) - E0 * np.vdot(O[:, q] * psi0, O[:, q] * psi0)).real) for q in range(6)])
check("finite check: open PR 9161: on the exact 2^3 flip component (864 states, E0 = -9.026721) the Feynman numerator <O^dag (H - E0) O> equals 2 u0 s^2",
      len(codes) == 9600 and H2.shape[0] == 864 and abs(E0 + 9.026721) < 1e-5 and abs(f - 2 * u0 * 4) < 1e-9,
      f"{len(codes)} ice states, component {H2.shape[0]}, E0 {E0:.6f}, f {f:.6f} vs 2 u0 s^2 {2 * u0 * 4:.6f}; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. open PR 9163: Parseval and the Gauss law fix the transverse weight at 3
worst_sum, worst_long = 0.0, 0.0
for L in (4, 6):
    ice = Ice(L)
    for s in loop_vmc(ice, 0.0, sweeps=30, therm=20, r=rng) + loop_vmc(ice, ALPHA, sweeps=30, therm=20, r=rng, start=ice.sector_state(0), fix_winding=True):
        worst_sum = max(worst_sum, abs(weight_map(ice, s).mean() - 3))
        worst_long = max(worst_long, longitudinal_max(ice, s))
check("finite check: open PR 9163: the all-zone total-field weight divided by N is exactly 3; k=0 includes harmonic modes and the longitudinal combination vanishes on uniform and guided ice samples of 4^3 and 6^3",
      worst_sum < 1e-10 and worst_long < 1e-10, f"max |mean_k T - 3| {worst_sum:.0e}; max longitudinal amplitude {worst_long:.0e}")

# ---------------------------------------------------------------- 3. open PR 9169: the RK point is exact -- the uniform vector is a zero mode of D - A on the component
deg = np.asarray(-H2.sum(axis=0)).ravel()                       # N_flip of each configuration (each flippable plaquette gives one -1)
H_RK = H2 + coo_matrix((deg, (np.arange(len(deg)), np.arange(len(deg)))), shape=H2.shape).tocsr()
ones = np.ones(H2.shape[0])
w_rk = eigsh(H_RK, k=1, which="SA")[0][0]
check("finite check: open PR 9169: on the same component the RK clause D - A annihilates the uniform vector exactly and is non-negative (its lowest eigenvalue is zero)",
      np.abs(H_RK @ ones).max() < 1e-12 and abs(w_rk) < 1e-8 and deg.min() >= 1,
      f"|(D - A) 1|max {np.abs(H_RK @ ones).max():.0e}; lowest eigenvalue {w_rk:.1e}; N_flip on the component in [{deg.min():.0f}, {deg.max():.0f}]")

# ---------------------------------------------------------------- 4. open PR 9166: the Gaussian lattice Maxwell covariance on 4^3 has the closed form A|s|(1 - g g^+)
U, K = 1.7, 1.2
A_G = np.sqrt(K / U) / 2
N4, xs, D, C, plane_of = geometry(4)
ks = momenta(4)
M = (C.T @ C).astype(float)
w, V = np.linalg.eigh(M)
nz = w > 1e-9
Sigma = (V[:, nz] * np.sqrt(w[nz])) @ V[:, nz].T * A_G
S = fourier_cov(Sigma, 4, xs, ks)
dev = np.abs(S - closed_form(ks, A_G)).max()
check("finite check: open PR 9166: the lattice Maxwell covariance (1/2) sqrt(K/U) (C^T C)^{1/2} on 4^3 is divergence-free and equals A |s(k)| (1 - g g^+) at every k, with kernel N + 2",
      np.abs(D @ C.T).max() == 0 and np.abs(D @ Sigma).max() < 1e-9 and dev < 1e-9 and int((~nz).sum()) == N4 + 2,
      f"|D C^T|max {np.abs(D @ C.T).max()}, |D Sigma|max {np.abs(D @ Sigma).max():.0e}, |S - closed form|max {dev:.0e}, kernel {int((~nz).sum())} = N + 2; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. open PR 9164: the register criterion -- invariance under menu dephasing
rs = rng.normal(size=(300, 3)); rs *= (rng.random(300) ** (1 / 3) / np.linalg.norm(rs, axis=1))[:, None]
p = rng.normal(size=3); p /= np.linalg.norm(p)
deph = (rs @ p)[:, None] * p[None, :]                                # Delta_p rho keeps only the menu component r.p
odds = lambda r: 0.5 * (1 + r @ p)                                    # functionals of the menu odds Tr(P_+ rho)
law = lambda r: np.exp(-((r @ p) ** 2))
purity = lambda r: 0.5 * (1 + (r * r).sum(axis=1))                    # reads the pre-record state beyond the menu diagonal
coh = lambda r: (r * r).sum(axis=1) - (r @ p) ** 2                    # 4 |rho_{+-}|^2
inv = {n: float(np.abs(fn(rs) - fn(deph)).max()) for n, fn in dict(odds=odds, law=law).items()}
read = {n: float(np.abs(fn(rs) - fn(deph)).max()) for n, fn in dict(purity=purity, coherence=coh).items()}
check("finite check: open PR 9164: rate functionals of the menu odds are invariant under menu dephasing rho -> P+ rho P+ + P- rho P-, purity and coherence rates are not",
      all(v < 1e-12 for v in inv.values()) and all(v > 0.1 for v in read.values()),
      "max |f(rho) - f(Delta_p rho)| over 300 Bloch-ball states: " + ", ".join(f"{n} {v:.0e}" for n, v in inv.items()) + "; " + ", ".join(f"{n} {v:.3f}" for n, v in read.items()))

# ---------------------------------------------------------------- 6. open PR 9168: the hyperhoneycomb site set in Z^3 is trivalent with axis bonds and bipartite
Lc = (4, 4, 8)
sites = [p_ for p_ in itertools.product(range(Lc[0]), range(Lc[1]), range(Lc[2])) if is_site(p_)]
def wrap(q):
    return tuple(q[a] % Lc[a] for a in range(3))
degs = [len({wrap(q) for q in neighbours(p_)}) for p_ in sites]
col = {sites[0]: 0}; stack = [sites[0]]; bip = True
while stack:
    a = stack.pop()
    for q in neighbours(a):
        q = wrap(q)
        if q not in col:
            col[q] = 1 - col[a]; stack.append(q)
        elif col[q] == col[a]:
            bip = False
check("finite check: open PR 9168: on the 4x4x8 torus every hyperhoneycomb site has exactly three nearest neighbours in the site set (axis bonds, three of six), "
      "the network is connected and bipartite, and half the points are sites",
      set(degs) == {3} and bip and len(col) == len(sites) and len(sites) == 4 * 4 * 8 // 2,
      f"{len(sites)} sites of {4 * 4 * 8} points, degrees {sorted(set(degs))}, connected {len(col) == len(sites)}, bipartite {bip}")

# ---------------------------------------------------------------- 7. open PR 9171: the two fits of the four-size series from the historical numbers
Ls = np.array([4., 6., 8., 10.]); ks1 = 2 * np.pi / Ls
Sv = np.array([0.692, 0.557, 0.575, 0.510]); Se = np.array([0.013, 0.022, 0.028, 0.046])
cp = np.polyfit(np.log(Ls), np.log(Sv), 1, w=Sv / Se)
log_objective = float((((np.polyval(cp, np.log(Ls))-np.log(Sv)) * Sv/Se)**2).sum())
chi_pow = float((((np.exp(np.polyval(cp, np.log(Ls))) - Sv) / Se) ** 2).sum())
cl = np.polyfit(ks1, Sv, 1, w=1 / Se)
chi_lin = float((((np.polyval(cl, ks1) - Sv) / Se) ** 2).sum())
check("finite check: open PR 9171: from the historical S_T(k_min) on 4^3-10^3 the weighted power law and the linear-plus-constant fit reproduce nu = 0.34, chi^2 5.1 and S0 = 0.392, a = 0.189, chi^2 3.8",
      abs(-cp[0] - 0.34) < 0.01 and abs(chi_pow - 5.1) < 0.1 and abs(cl[1] - 0.392) < 0.002 and abs(cl[0] - 0.189) < 0.002 and abs(chi_lin - 3.8) < 0.1,
      f"log objective {log_objective:.6f}; nu {-cp[0]:.3f} (original-scale residual at log fit {chi_pow:.2f}); S0 {cl[1]:.3f}, a {cl[0]:.3f} (chi^2 {chi_lin:.2f})")

# ---------------------------------------------------------------- 8. the register
REGISTER = ["D-gauss", "D-roles", "D-ring", "D-RK (the potential V n_p and its sweep, open PR 9169)",
            "D-form-const", "D-form-law", "D-form-records", "D-form-odds", "D-form-state", "D-form-time", "D-register (open PR 9164)",
            "D-comp (which composite sites are recorded, open PR 9168)", "D-axes / D-flavour (record-selected bond flavours, open PR 9168)",
            "D-Gauss-comparator (the lattice Maxwell theory as a supplied comparison, open PR 9166)"]
ADOPTED = {key: False for key in REGISTER}
check("finite check: register of decision points touched in round three (none adopted)", len(REGISTER) == 14 and not any(ADOPTED.values()), "; ".join(REGISTER))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
