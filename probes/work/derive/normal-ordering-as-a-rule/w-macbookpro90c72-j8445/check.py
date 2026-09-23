#!/usr/bin/env python3
"""J:derive:normal-ordering-as-a-rule:a2 - checks for ATTEMPT.md (same directory).

Block 76's filled sea (open PR #8611): E_sea[w] = sum of the negative eigenvalues of H_w = phi H phi, H = sum_j sigma_j D_j
(block 54's walk), phi = sqrt(w) = e^{u/2}; c0 = E_sea[1]/N. Counter-terms: site T_site = c0 sum_x w_x, bond T_bond =
(c0/3) sum_bonds sqrt(w_x w_y). Exact finite-torus identities are checked on TWISTED tori (equal boundary phases on the three
axes, so that no k-point sits at a zero-energy point and the axes stay equivalent; the twist changes no statement), by dense diagonalisation
(float64, machine precision); infinite-volume numbers by large momentum sums (FLOAT, extrapolated, labelled).
"""
import sys
from itertools import product

import mpmath as mp
import numpy as np

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
TW = np.array([0.61, 0.61, 0.61])  # equal boundary phases: the grid keeps the permutations of the axes, no k at a zero


def ham(L, tw=TW):
    N = L ** 3
    H = np.zeros((2 * N, 2 * N), complex)
    idx = lambda x: np.ravel_multi_index(tuple(v % L for v in x), (L, L, L))
    for x in product(range(L), repeat=3):
        for j in range(3):
            y = list(x); y[j] += 1
            ph = np.exp(1j * tw[j]) if y[j] == L else 1.0
            a, b = idx(x), idx(y)
            blk = SIG[j] / (2j) * ph  # the overall sign of H does not change E_sea (its spectrum is symmetric)
            H[2 * b:2 * b + 2, 2 * a:2 * a + 2] += blk
            H[2 * a:2 * a + 2, 2 * b:2 * b + 2] += blk.conj().T
    return H


def esea(H, u):
    ph = np.repeat(np.exp(u / 2), 2)
    ev = np.linalg.eigvalsh((ph[:, None] * H) * ph[None, :])
    return ev[ev < 0].sum()


def kgrid(L, tw=TW, mid=False):
    n = np.arange(L) + (0.5 if mid else 0.0)
    ks = [2 * np.pi * n / L + tw[j] / L for j in range(3)]
    K = np.meshgrid(*ks, indexing="ij")
    return np.stack(K)  # (3, L, L, L)


def formula_parts(L, qn, tw=TW, mid=False):
    """c0, the bond part (c0/12) sum(2 + 2 cos q) and the bubble B(q) on the (twisted) grid; q = 2 pi qn / L."""
    K = kgrid(L, tw, mid)
    d = np.sin(K); e = np.sqrt((d * d).sum(0))
    c0 = -e.mean()
    dq = np.sin(K + (2 * np.pi * np.array(qn) / L)[:, None, None, None])
    eq = np.sqrt((dq * dq).sum(0))
    cosang = (d * dq).sum(0) / (e * eq)
    B = -((eq - e) ** 2 * (1 - cosang) / (e + eq)).mean() / 4
    q = 2 * np.pi * np.array(qn) / L
    bond = c0 / 12 * np.sum(2 + 2 * np.cos(q))
    return c0, bond, B


# ------------------------------------------------------------------ A: exact identities on twisted tori
L = 6
N = L ** 3
H = ham(L)
X = np.array(list(product(range(L), repeat=3)))
u0 = np.zeros(N)
E0 = esea(H, u0)
c0 = E0 / N
rng = np.random.default_rng(76)
ur = rng.normal(0, 0.4, N)
s = 1.7
weight = abs(esea(H, ur + np.log(s)) - s * esea(H, ur)) < 1e-11 * abs(E0)
cb = (-1.0) ** X.sum(1)
chess = [abs(esea(H, e * cb) - E0) < 1e-11 * abs(E0) for e in (0.5, 1.0)]
Tsite = lambda u: c0 * np.exp(u).sum()
bonds = [(i, np.ravel_multi_index(tuple((X[i] + np.eye(3, dtype=int)[j]) % L), (L, L, L))) for i in range(N) for j in range(3)]
Tbond = lambda u: c0 / 3 * sum(np.exp((u[a] + u[b]) / 2) for a, b in bonds)
member = lambda u, gam: (2 / gam) * sum((np.exp(u[a] / 2) - np.exp(u[b] / 2)) ** 2 for a, b in bonds)
gam_ind = 12 / abs(c0)
Rs = lambda u: esea(H, u) - Tsite(u)
Rb = lambda u: esea(H, u) - Tbond(u)
cb_ok = all(abs(Rs(e * cb) - N * abs(c0) * (np.cosh(e) - 1)) < 1e-10 * N and abs(Rs(e * cb) - member(e * cb, gam_ind)) < 1e-10 * N
            and abs(Rb(e * cb)) < 1e-10 * N for e in (0.5, 1.0))
unif = all(abs(Rs(np.full(N, t))) < 1e-10 * N and abs(Rb(np.full(N, t))) < 1e-10 * N for t in (-0.7, 0.4))
dec = abs(Rs(ur) - (member(ur, gam_ind) + Rb(ur))) < 1e-9 * N
h = 1e-4
fv = [(esea(H, h * np.eye(N)[i]) - esea(H, -h * np.eye(N)[i])) / (2 * h) for i in (0, 37, 111)]
first = all(abs(v - c0) < 1e-6 for v in fv)
ok("A1", weight and all(chess) and cb_ok and unif and dec and first,
   f"twisted 6^3 torus, dense spectra: E_sea has weight one; c0 = {c0:.6f} per site; a chessboard of clocks leaves E_sea "
   "exactly unchanged (amplitudes 0.5, 1); dE_sea/du_x = c0 at uniform rates (sites 0, 37, 111); R_site = E_sea - c0 sum w "
   "and R_bond = E_sea - (c0/3) sum_bonds sqrt(w_x w_y) vanish on uniform rates; on the chessboard R_site = N|c0|(cosh e - 1) "
   "= block 56's member with gamma = 12/|c0| exactly, R_bond = 0; and R_site = member(12/|c0|) + R_bond identically")


def second_var(fun, qn, eps=1e-2):
    q = 2 * np.pi * np.array(qn) / L
    mode = np.cos(X @ q)
    f = lambda e: fun(e * mode)
    # five-point second derivative, per site; E(eps) - E(0) = N M eps^2 / 4 for a cos mode
    d2 = (-f(2 * eps) + 16 * f(eps) - 30 * f(0) + 16 * f(-eps) - f(-2 * eps)) / (12 * eps ** 2)
    return 2 * d2 / N


modes = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 2, 1)]
rows, good = [], True
for qn in modes:
    Mfd = second_var(lambda u: esea(H, u), qn)
    c0f, bond, B = formula_parts(L, qn)
    Mb = second_var(Tbond, qn)
    good &= abs(Mfd - (bond + B)) < 1e-7 and abs(Mb - bond) < 1e-8 and B <= 0 and abs(c0f - c0) < 1e-12
    rows.append(f"{qn}: {Mfd:+.9f} = {bond:+.9f} + ({B:+.2e})")
ok("A2", good, "the sea's second variation along cos(q.x) modes, per site (finite differences of dense spectra = the "
   "closed form (c0/12) sum_j (2 + 2 cos q_j) + B(q), B = -(1/4N) sum_k (e_k+q - e_k)^2 (1 - dhat_k.dhat_k+q)/(e_k + "
   "e_k+q) <= 0): " + "; ".join(rows) + "; the bond counter-term's second variation is exactly the first part")

# ------------------------------------------------------------------ B: infinite volume (FLOAT, momentum sums)
def slab_sum(L, qx, mid=True):
    """c0 and B(q) for q = (qx, 0, 0) on a midpoint grid, summed in slabs of k_x (memory-light)."""
    n = (np.arange(L) + (0.5 if mid else 0.0)) * 2 * np.pi / L
    KY, KZ = np.meshgrid(n, n, indexing="ij")
    sy2, sz2 = np.sin(KY) ** 2, np.sin(KZ) ** 2
    esum, bsum = 0.0, 0.0
    for kx in n:
        a, b = np.sin(kx), np.sin(kx + qx)
        e = np.sqrt(a * a + sy2 + sz2); eq = np.sqrt(b * b + sy2 + sz2)
        cosang = (a * b + sy2 + sz2) / (e * eq)
        esum += e.sum()
        bsum += ((eq - e) ** 2 * (1 - cosang) / (e + eq)).sum()
    return -esum / L ** 3, -bsum / (4 * L ** 3)


c0s = {Lm: slab_sum(Lm, 0.0)[0] for Lm in (32, 64, 128, 256)}
rate = (c0s[64] - c0s[32]) / (c0s[128] - c0s[64]), (c0s[128] - c0s[64]) / (c0s[256] - c0s[128])
p_ord = np.log2(rate[1])
c0inf = c0s[256] + (c0s[256] - c0s[128]) / (2 ** p_ord - 1)
ok("B1", abs(c0s[256] - c0s[128]) < 1e-6 and rate[1] > 4,
   f"c0 = -<|sin k|> over the zone on midpoint grids 32, 64, 128, 256: {c0s[32]:.9f}, {c0s[64]:.9f}, {c0s[128]:.9f}, "
   f"{c0s[256]:.9f} (differences shrink {rate[0]:.1f}x, {rate[1]:.1f}x per doubling) -> c0 = {c0inf:.9f}; so kappa = "
   f"|c0|/12 = {abs(c0inf) / 12:.7f}, gamma_ind = 12/|c0| = {12 / abs(c0inf):.6f}")

Lb = 256
bq = []
for n in (4, 8, 16, 32, 64):
    q = 2 * np.pi * n / Lb
    B = slab_sum(Lb, q)[1]
    bq.append((q, B / (2 - 2 * np.cos(q))))
ratios = [abs(b) / (q ** 2 * np.log(1 / q)) for q, b in bq if q < 0.5]
mono = all(abs(bq[i][1]) < abs(bq[i + 1][1]) for i in range(len(bq) - 1))
ok("B2", mono and abs(bq[0][1]) < 2e-4 and max(ratios) / min(ratios) < 3,
   "the bubble per |q|^2: " + ", ".join(f"q = {q:.3f}: {b:+.2e}" for q, b in bq) + ": it vanishes "
   "like q^2 log(1/q) (midpoint grid 256^3), so the long-wavelength stiffness of R_site is exactly |c0|/12 and that of "
   "R_bond exactly 0; block 76's 0.0952 at L = 12 is |c0|/12 + B(q)/|q|^2 at its finite q")

k76 = []
for qn in ((1, 0, 0), (2, 0, 0), (3, 0, 0), (1, 1, 0), (1, 1, 1), (2, 2, 0)):
    c0t, bond, B = formula_parts(12, qn, tw=TW)
    q = 2 * np.pi * np.array(qn) / 12
    q2 = np.sum(2 - 2 * np.cos(q))
    k76.append((bond + B - c0t) / q2)
ok("B3", all(0.088 < v < 0.100 for v in k76),
   f"block 76's six modes on a twisted 12^3 torus, (M(q) - c0)/|q|^2: {', '.join(f'{v:.4f}' for v in k76)} (block 76: "
   "0.0944-0.0960, kappa = 0.0952 +- 0.0016): its measured stiffness is the exact |c0|/12 lowered by the bubble")


# ------------------------------------------------------------------ C: the family and the strong field
mp.mp.dps = 30
g0 = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) * mp.gamma(mp.mpf(11) / 24)
g0i = mp.quad(lambda t: mp.exp(-t) * mp.besseli(0, t / 3) ** 3, [0, 1, 10, 100])
g0tail = mp.quad(lambda t: mp.exp(-t) * mp.besseli(0, t / 3) ** 3, [100, 1000, 10000]) + 2 * (mp.mpf(3) / (2 * mp.pi)) ** 1.5 / mp.sqrt(10000)
sat = abs(c0inf) / float(g0)
ok("C1", abs(g0 - (g0i + g0tail)) < 1e-4 and abs(float(g0) - 1.516386059151978) < 1e-12,
   f"Watson's g0 = G_(1-A)(0) = (sqrt6/32pi^3) Gamma(1/24)Gamma(5/24)Gamma(7/24)Gamma(11/24) = {mp.nstr(g0, 16)} (the "
   f"integral int e^-t I0(t/3)^3 dt agrees to {mp.nstr(abs(g0 - g0i - g0tail), 2)}); with gamma = 12/|c0| block 56's strong "
   f"field is phi0 = 1/(1 + g0 m/|c0|), ledger m/(1 + x) < 12/(gamma g0) = |c0|/g0 = {sat:.5f} (block 76's gamma = 10.51 "
   f"would give {12 / (10.51 * float(g0)):.5f}), field energy at most |c0|/(4 g0) = {sat / 4:.5f}; the family "
   "theta T_site + (1 - theta) T_bond has long-wavelength stiffness theta |c0|/12, gamma = 12/(theta |c0|): A and C fix "
   "only the uniform value")

print(f"SUMMARY: {'PARTIAL' if not FAILS else 'PARTIAL (failed checks: ' + ', '.join(FAILS) + ')'} normal ordering "
      "R_site = E_sea - c0 sum w has weight one, vanishes with its first variation on uniform rates, and its second "
      "variation is (|c0|/12)|q|^2_lat + B(q) with the interband bubble B = O(q^4 log q) <= 0: exactly block 56's member "
      f"with gamma = 12/|c0| = {12 / abs(c0inf):.4f} plus R_bond; the equally admissible bond subtraction leaves no "
      "long-wavelength stiffness, so A and C do not fix the counter-term: it is supplied (the unit's HIT condition fails)")
if not FAILS:
    print("HIT: the filled sea's second variation in the rates is exactly (c0/12) sum_j (2 + 2 cos q_j) + B(q), B(q) = "
          "-(1/4N) sum_k (eps_k+q - eps_k)^2 (1 - dhat_k.dhat_k+q)/(eps_k + eps_k+q) <= 0 and O(q^4 log(1/q)); hence the "
          "site-normal-ordered sea energy is block 56's member (2/gamma) sum_bonds (phi_x - phi_y)^2 with gamma = 12/|c0| "
          f"= {12 / abs(c0inf):.4f}, identically, plus the bond-normal-ordered energy R_bond, whose long-wavelength "
          "stiffness is exactly 0; so the induced coupling is 12/|c0| (block 76's 10.51 is a finite-q value), the "
          f"saturation |c0|/g0 = {sat:.4f}, and the counter-term is a supplied clause, not a consequence of clauses A and C")
