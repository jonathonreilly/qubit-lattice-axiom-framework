#!/usr/bin/env python3
"""Forming one record costs the energy held in the recorded site's bonds.

Setting (supplied, as in the landed dynamics-clause notes): the lattice's sites
carry a quantum state; a record at site x is formed by the compression update
with rank-one Kraus operators on x (a finite antipodal menu {n, -n}, or the
sphere menu, realised exactly by the octahedral 3-design). The mean energy
change over outcomes is Delta E = Tr rho (Phi*(h_x) - h_x), h_x = the terms of
H touching x.

Checks:

A. The identity on random nearest-neighbour chains, random states, antipodal
   and sphere menus.
B. Exact (sympy) singlet: a record costs 2J on either menu; an aligned record
   on an aligned product state costs 0.
C. Heisenberg dynamics-clause model on the open 2x2x2 and 2x2x3 blocks: the
   ground state is a singlet (site Bloch vector 0); every menu costs (2/3) of
   the site's bond energy; the cost is at least half the gap.
D. Gap bound: for random gapped chains the cost is at least
   gap * sum_a w_a (p_a - p_a^2), p_a = <P_a>, and the sphere menu costs at
   least gap * (3 - |r|^2)/6.
E. Walker sea (H = t sum_j sin k_j sigma_j, twisted boundaries, half filling):
   an occupation record costs exactly the energy of the site's bonds; Fock-space
   brute force equals the correlation-matrix formula in 1D, 2D and 3D, massless
   and with the staggered mass; the massless site is maximally mixed.
F. The cost of the massless sea is 2 <|s(k)|>_BZ t, converging to 2.387602 t;
   the massive sea's is 2 <s^2 / sqrt(s^2 + m^2)> t, tending to 3 t^2 / m.
G. Conical lemma: above a product (Fock-vacuum) ground state of a local,
   number-conserving quadratic H, the lowest one-particle band vanishes at
   least quadratically at its zeros: the gradient of v0^dag h(k) v0 vanishes.
H. A sharp record of a cube's total content costs (bonds crossing its surface)
   x (bond energy) = 2.39 R^2 t: coarse sharp records cost more.
I. A soft (Gaussian) record of a smooth region's content with resolution sigma
   costs sum over bonds |bond energy| (1 - exp(-(dw)^2 / (8 sigma^2))), about
   0.415 R / sigma^2 t for smooth weights of width R.
J. Physical tiers (external comparison inputs, reference only): the cost in
   joules at lattice energy scales 1 TeV, 10^10 GeV and the Planck energy, and
   the largest vacuum formation rate the critical density allows.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_INPUT_PATHS = (
    'docs/RECORD_FORMATION_A_SHARP_ONE_SITE_LOCK_COSTS_THE_ENERGY_OF_ITS_BONDS_IN_THE_WALKERS_SEA_ABOUT_TWO_POINT_FOUR_LATTICE_ENERGY_UNITS_PER_RECORD_BOUNDED_THEOREM_NOTE_2026-09-27.md',
    'docs/DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)
AUDIT_TIMEOUT_SEC = 600

import numpy as np
import scipy.sparse as sps
import scipy.sparse.linalg as spla
import sympy as sp
from sympy.physics.quantum import TensorProduct as TP

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260927)
I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]


def op_at(op, site, n):
    out = np.array([[1.0 + 0j]])
    for s in range(n):
        out = np.kron(out, op if s == site else I2)
    return out


def sparse_op_at(op, site, n):
    out = sps.identity(1, format='csr', dtype=complex)
    for s in range(n):
        out = sps.kron(out, sps.csr_matrix(op) if s == site else sps.identity(2, format='csr'), format='csr')
    return out


def proj(nvec):
    nvec = np.asarray(nvec, float)
    nvec = nvec / np.linalg.norm(nvec)
    return 0.5 * (I2 + sum(c * P for c, P in zip(nvec, PAULI)))


def menus_at(x, n, nvec):
    anti = [(1.0, op_at(proj(nvec), x, n)), (1.0, op_at(proj(-np.asarray(nvec)), x, n))]
    octa = [(1.0 / 3.0, op_at(proj(s * np.eye(3)[a]), x, n)) for a in range(3) for s in (1, -1)]
    return anti, octa


def cost_direct(rho, H, menu):
    post = sum(w * P @ rho @ P for w, P in menu)
    return np.real(np.trace(post @ H) - np.trace(rho @ H))


def cost_local(rho, hx, menu):
    dual = sum(w * P @ hx @ P for w, P in menu)
    return np.real(np.trace(rho @ (dual - hx)))


def random_chain(n, gapped_field=0.0):
    terms = []
    for i in range(n - 1):
        C = rng.normal(size=(3, 3))
        terms.append((i, i + 1, sum(C[a, b] * op_at(PAULI[a], i, n) @ op_at(PAULI[b], i + 1, n)
                                    for a in range(3) for b in range(3))))
    for i in range(n):
        hvec = rng.normal(size=3) + gapped_field * np.array([0, 0, 1.0])
        terms.append((i, i, sum(hvec[a] * op_at(PAULI[a], i, n) for a in range(3))))
    return terms


# ---------------------------------------------------------------- A
worst = 0.0
for trial in range(60):
    n = 4
    terms = random_chain(n)
    H = sum(t for _, _, t in terms)
    v = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
    v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())
    x = trial % n
    anti, octa = menus_at(x, n, rng.normal(size=3))
    hx = sum(t for i, j, t in terms if x in (i, j))
    for menu in (anti, octa):
        worst = max(worst, abs(cost_direct(rho, H, menu) - cost_local(rho, hx, menu)))
check("A: the mean energy change of a record equals Tr rho(Phi*(h_x) - h_x), only terms touching x",
      worst < 1e-12, f"60 random 4-site chains, antipodal and sphere menus; max deviation {worst:.1e}")

# ---------------------------------------------------------------- B
J = sp.Symbol('J', positive=True)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
Hs = J * (TP(sx, sx) + TP(sy, sy) + TP(sz, sz))
singlet = sp.Matrix([0, 1, -1, 0]) / sp.sqrt(2)
E0s = sp.simplify((singlet.H * Hs * singlet)[0])
Pz = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])]
cost_anti = sp.simplify(sum((singlet.H * TP(P, sp.eye(2)) * Hs * TP(P, sp.eye(2)) * singlet)[0] for P in Pz) - E0s)
octa_P = []
for s_mat in (sx, sy, sz):
    for sg in (1, -1):
        octa_P.append((sp.eye(2) + sg * s_mat) / 2)
cost_octa = sp.simplify(sum(sp.Rational(1, 3) * (singlet.H * TP(P, sp.eye(2)) * Hs * TP(P, sp.eye(2)) * singlet)[0]
                            for P in octa_P) - E0s)
up_up = sp.Matrix([1, 0, 0, 0])
Hfm = -Hs
cost_aligned = sp.simplify(sum((up_up.H * TP(P, sp.eye(2)) * Hfm * TP(P, sp.eye(2)) * up_up)[0] for P in Pz)
                           - (up_up.H * Hfm * up_up)[0])
check("B: singlet (E0 = -3J): a record costs exactly 2J on the antipodal and on the sphere menu",
      E0s == -3 * J and cost_anti == 2 * J and cost_octa == 2 * J, f"E0={E0s}, costs {cost_anti}, {cost_octa}")
check("B: an aligned record on the aligned ferromagnetic product state costs exactly 0",
      cost_aligned == 0, f"cost {cost_aligned}")


# ---------------------------------------------------------------- C
def heis_block(dims, Jv=1.0):
    sites = list(itertools.product(*[range(d) for d in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    bonds = []
    for s in sites:
        for a in range(3):
            t = list(s); t[a] += 1; t = tuple(t)
            if t in idx:
                bonds.append((idx[s], idx[t]))
    ops = {(i, a): sparse_op_at(PAULI[a], i, n) for i in range(n) for a in range(3)}
    H = sum(Jv * ops[(i, a)] @ ops[(j, a)] for i, j in bonds for a in range(3))
    return sites, n, bonds, ops, H.tocsr()


heis_rows = []
for dims in [(2, 2, 2), (2, 2, 3)]:
    sites, n, bonds, ops, H = heis_block(dims)
    vals, vecs = spla.eigsh(H, k=6, which='SA')
    o = np.argsort(vals); vals = vals[o]; vecs = vecs[:, o]
    g = vecs[:, 0]; E0 = vals[0]; gap = vals[1] - vals[0]
    Id = sps.identity(2**n, format='csr')
    Stot2 = sum((sum(ops[(i, a)] for i in range(n)) @ sum(ops[(i, a)] for i in range(n))) for a in range(3))
    s2 = np.real(g.conj() @ (Stot2 @ g))
    for x in sorted({0, [i for i, s in enumerate(sites) if s == (0, 0, 1)][0] if dims[2] > 2 else n - 1}):
        nb = [j for i, j in bonds if i == x] + [i for i, j in bonds if j == x]
        bond_e = sum(np.real(g.conj() @ (ops[(x, a)] @ (ops[(y, a)] @ g))) for y in nb for a in range(3))
        rx = np.array([np.real(g.conj() @ (ops[(x, a)] @ g)) for a in range(3)])
        costs = []
        for nvec in (np.array([0, 0, 1.0]), rng.normal(size=3), rng.normal(size=3)):
            nvec = nvec / np.linalg.norm(nvec)
            ns = sum(c * ops[(x, a)] for a, c in enumerate(nvec))
            costs.append(sum(np.real(((0.5 * (Id + sg * ns)) @ g).conj() @ (H @ ((0.5 * (Id + sg * ns)) @ g)))
                             for sg in (1, -1)) - E0)
        c_oct = sum((1 / 3) * np.real(((0.5 * (Id + sg * ops[(x, a)])) @ g).conj()
                                      @ (H @ ((0.5 * (Id + sg * ops[(x, a)])) @ g)))
                    for a in range(3) for sg in (1, -1)) - E0
        costs.append(c_oct)
        heis_rows.append((dims, x, len(nb), E0, gap, s2, np.linalg.norm(rx), costs, -2 / 3 * bond_e))
ok = all(abs(s2) < 1e-8 and nr < 1e-8 and max(abs(c - tb) for c in costs) < 1e-8 and min(costs) >= gap / 2 - 1e-9
         for dims, x, deg, E0, gap, s2, nr, costs, tb in heis_rows)
check("C: Heisenberg blocks: singlet ground state, every menu costs (2/3)|site bond energy| >= gap/2",
      ok, "; ".join(f"{d} site {x} (deg {deg}): cost {tb:.6f}, gap/2 {gap/2:.6f}"
                    for d, x, deg, E0, gap, s2, nr, costs, tb in heis_rows))

# ---------------------------------------------------------------- D
worst_margin = np.inf
sphere_margin = np.inf
for trial in range(40):
    n = 4
    terms = random_chain(n, gapped_field=3.0)
    H = sum(t for _, _, t in terms)
    w, V = np.linalg.eigh(H)
    g = V[:, 0]; gap = w[1] - w[0]
    rho = np.outer(g, g.conj())
    x = trial % n
    anti, octa = menus_at(x, n, rng.normal(size=3))
    for menu in (anti, octa):
        c = cost_direct(rho, H, menu)
        bound = gap * sum(wt * (np.real(g.conj() @ P @ g) - np.real(g.conj() @ P @ g)**2) for wt, P in menu)
        worst_margin = min(worst_margin, c - bound)
    rvec = np.array([np.real(g.conj() @ op_at(PAULI[a], x, n) @ g) for a in range(3)])
    sphere_margin = min(sphere_margin, cost_direct(rho, H, octa) - gap * (3 - rvec @ rvec) / 6)
check("D: cost >= gap * sum_a w_a (p_a - p_a^2) (antipodal and sphere menus)", worst_margin > -1e-10,
      f"40 random gapped chains; smallest margin {worst_margin:.3e}")
check("D: sphere menu cost >= gap * (3 - |r|^2)/6 >= gap/3, even at a pure site", sphere_margin > -1e-10,
      f"smallest margin {sphere_margin:.3e}")


# ---------------------------------------------------------------- E, F (walker sea)
def one_body_H(L, dim, anti=True, m=0.0):
    sites = list(itertools.product(range(L), repeat=dim))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((2 * N, 2 * N), complex)
    for s in sites:
        i = idx[s]
        for j in range(dim):
            t = list(s); t[j] += 1
            phase = 1.0
            if t[j] == L:
                t[j] = 0
                phase = -1.0 if anti else 1.0
            k = idx[tuple(t)]
            A = PAULI[j] / (2j) * phase
            h[2*i:2*i+2, 2*k:2*k+2] += A
            h[2*k:2*k+2, 2*i:2*i+2] += A.conj().T
        h[2*i:2*i+2, 2*i:2*i+2] += m * (-1) ** sum(s) * np.eye(2)
    return h, sites, idx


def corr_ground(h):
    w, V = np.linalg.eigh(h)
    occ = V[:, w < 0]
    return occ.conj() @ occ.T


def cut_cost(h, C, cut_mask):
    return -np.real(np.sum(np.where(cut_mask, h, 0) * C))


def site_mask(M, i):
    mask = np.zeros((M, M), bool)
    a = [2 * i, 2 * i + 1]
    for p in a:
        for q in range(M):
            if q not in a:
                mask[p, q] = mask[q, p] = True
    return mask


def fock_ops(M):
    Z = sps.csr_matrix(np.diag([1, -1]).astype(complex))
    Idm = sps.identity(2, format='csr', dtype=complex)
    a = sps.csr_matrix(np.array([[0, 1], [0, 0]], complex))
    ops = []
    for p in range(M):
        out = sps.identity(1, format='csr', dtype=complex)
        for q in range(M):
            out = sps.kron(out, Z if q < p else (a if q == p else Idm), format='csr')
        ops.append(out)
    return ops


def fock_cost(L, dim, m=0.0, site=0):
    h, sites, idx = one_body_H(L, dim, m=m)
    M = h.shape[0]
    c = fock_ops(M)
    cd = [x.conj().T.tocsr() for x in c]
    H = sps.csr_matrix((2**M, 2**M), dtype=complex)
    for p in range(M):
        for q in range(M):
            if abs(h[p, q]) > 0:
                H = H + h[p, q] * (cd[p] @ c[q])
    Nop = sum(cd[p] @ c[p] for p in range(M))
    Id = sps.identity(2**M, format='csr')
    Hpen = H + 5.0 * (Nop - (M // 2) * Id) @ (Nop - (M // 2) * Id)
    vals, vecs = spla.eigsh(Hpen.tocsr(), k=3, which='SA')
    o = np.argsort(vals); vals = vals[o]; vecs = vecs[:, o]
    g = vecs[:, 0]
    E0 = np.real(g.conj() @ (H @ g))
    na, nb = cd[2 * site] @ c[2 * site], cd[2 * site + 1] @ c[2 * site + 1]
    projs = [na @ nb, na @ (Id - nb), (Id - na) @ nb, (Id - na) @ (Id - nb)]
    dE = sum(np.real((P @ g).conj() @ (H @ (P @ g))) for P in projs) - E0
    C = corr_ground(h)
    return dE, cut_cost(h, C, site_mask(M, site)), vals[1] - vals[0]


rows = []
for (L, dim, m) in [(2, 3, 0.0), (2, 2, 0.0), (6, 1, 0.0), (8, 1, 0.0), (2, 3, 0.7), (6, 1, 0.4)]:
    dE, dC, gp = fock_cost(L, dim, m)
    rows.append((L, dim, m, dE, dC, gp))
check("E: Fock-space brute force equals the correlation-matrix bond formula (1D, 2D, 3D; massless and massive)",
      all(abs(dE - dC) < 1e-9 and gp > 1e-6 for L, dim, m, dE, dC, gp in rows),
      "; ".join(f"L={L} d={dim} m={m}: {dE:.10f}" for L, dim, m, dE, dC, gp in rows))


def mean_s(L, f):
    ks = 2 * np.pi * (np.arange(L) + 0.5) / L
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    return np.mean(f(np.sin(KX)**2 + np.sin(KY)**2 + np.sin(KZ)**2))


L = 8
h8, sites8, idx8 = one_body_H(L, 3)
C8 = corr_ground(h8)
cost_rs = cut_cost(h8, C8, site_mask(h8.shape[0], 0))
cost_cf = 2 * mean_s(L, np.sqrt)
blk = C8[0:2, 0:2]
check("E: massless sea, L = 8: real-space record cost = 2<|s|> (closed form); site one-body state = 1/2 (maximally mixed)",
      abs(cost_rs - cost_cf) < 1e-10 and np.max(np.abs(blk - 0.5 * np.eye(2))) < 1e-10,
      f"cost {cost_rs:.10f}; site block {np.real(np.diag(blk))}")
seq = [2 * mean_s(Lk, np.sqrt) for Lk in (64, 128, 256)]
check("F: massless sea cost 2<|s(k)|>_BZ t converges to 2.387602 t", abs(seq[-1] - seq[-2]) < 1e-6
      and abs(seq[-1] - 2.387602) < 1e-6, f"L = 64, 128, 256: {seq[0]:.9f}, {seq[1]:.9f}, {seq[2]:.9f}")
mrows = []
for m in (0.5, 3.0, 100.0):
    hm, _, _ = one_body_H(8, 3, m=m)
    Cm = corr_ground(hm)
    rs = cut_cost(hm, Cm, site_mask(hm.shape[0], 0))
    cf = 2 * mean_s(8, lambda s2: s2 / np.sqrt(s2 + m * m))
    inf = 2 * mean_s(96, lambda s2: s2 / np.sqrt(s2 + m * m))
    mrows.append((m, rs, cf, inf))
check("F: massive sea: cost 2<s^2/sqrt(s^2+m^2)> t (closed form = real space); tends to 3 t^2/m",
      all(abs(rs - cf) < 1e-10 for m, rs, cf, inf in mrows) and abs(mrows[-1][3] * 100 / 3 - 1) < 1e-3,
      "; ".join(f"m={m}: {inf:.6f}" for m, rs, cf, inf in mrows))

# ---------------------------------------------------------------- G conical lemma
from scipy.optimize import minimize
max_ratio_dev = 0.0
grid = np.linspace(0, 2 * np.pi, 16, endpoint=False)
for trial in range(30):
    A = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(3)]
    B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); B = B + B.conj().T

    def lam(k, A=A, B=B):
        out = B.copy()
        for j in range(3):
            out = out + A[j] * np.exp(1j * k[j]) + A[j].conj().T * np.exp(-1j * k[j])
        return np.linalg.eigvalsh(out)[0]
    best = min(((lam(np.array(kk)), np.array(kk)) for kk in itertools.product(grid, repeat=3)), key=lambda t: t[0])
    res = minimize(lam, best[1], method='Nelder-Mead', options=dict(xatol=1e-12, fatol=1e-15, maxiter=20000))
    kmin, emin = res.x, res.fun
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    e1 = lam(kmin + 1e-3 * u) - emin
    e2 = lam(kmin + 2e-3 * u) - emin
    max_ratio_dev = max(max_ratio_dev, abs(e2 / e1 - 4))   # conical: 2, quadratic: 4
check("G: lowest band of a local Bloch Hamiltonian rises quadratically from its global minimum (never conically)",
      max_ratio_dev < 0.05, f"30 random range-one 2x2 Bloch families; max |e(2d)/e(d) - 4| = {max_ratio_dev:.3e}")

# ---------------------------------------------------------------- K per-outcome costs (no odds can lower the mean)
def per_outcome_costs(L, dim, nvec):
    h, sites, idx = one_body_H(L, dim)
    M = h.shape[0]
    c = fock_ops(M)
    cd = [x.conj().T.tocsr() for x in c]
    H = sps.csr_matrix((2**M, 2**M), dtype=complex)
    for p in range(M):
        for q in range(M):
            if abs(h[p, q]) > 0:
                H = H + h[p, q] * (cd[p] @ c[q])
    Nop = sum(cd[p] @ c[p] for p in range(M))
    Id = sps.identity(2**M, format='csr')
    vals, vecs = spla.eigsh((H + 5.0 * (Nop - (M // 2) * Id) @ (Nop - (M // 2) * Id)).tocsr(), k=2, which='SA')
    g = vecs[:, np.argmin(vals)]
    E0 = np.real(g.conj() @ (H @ g))
    th, ph = np.arccos(nvec[2]), np.arctan2(nvec[1], nvec[0])
    u = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    v = np.array([-np.exp(-1j * ph) * np.sin(th / 2), np.cos(th / 2)])
    an = u.conj()[0] * c[0] + u.conj()[1] * c[1]
    bn = v.conj()[0] * c[0] + v.conj()[1] * c[1]
    nA, nB = an.conj().T @ an, bn.conj().T @ bn
    out = []
    for P in (nA @ nB, nA @ (Id - nB), (Id - nA) @ nB, (Id - nA) @ (Id - nB)):
        v2 = P @ g
        pr = np.real(v2.conj() @ v2)
        out.append((pr, np.real(v2.conj() @ (H @ v2)) / pr - E0))
    return out


krows = []
for (L, dim) in [(2, 3), (8, 1)]:
    for nvec in (np.array([0, 0, 1.0]), np.array([1, 1, 1]) / np.sqrt(3)):
        oc = per_outcome_costs(L, dim, nvec)
        krows.append((L, dim, [round(float(cst), 9) for pr, cst in oc], [round(float(pr), 6) for pr, cst in oc]))
check("K: in the massless sea every outcome of a site record costs the same (so no choice of odds lowers the cost)",
      all(max(cs) - min(cs) < 1e-8 for L, dim, cs, ps in krows),
      "; ".join(f"L={L} d={dim}: costs {cs[0]:.6f}, odds {ps}" for L, dim, cs, ps in krows))

# ---------------------------------------------------------------- L stored vs radiable; M parity of the lock
lrows = []
for Ls in (8, 12):
    hL, _, _ = one_body_H(Ls, 3)
    wL = np.linalg.eigvalsh(hL)
    E0L = wL[wL < 0].sum()
    NpL = int((wL < 0).sum())
    keep = list(range(2, hL.shape[0]))
    wr = np.sort(np.linalg.eigvalsh(hL[np.ix_(keep, keep)]))
    stored = [wr[:NpL - nx].sum() - E0L for nx in (0, 1, 2)]
    lrows.append((Ls, stored, 2 * np.mean(np.abs(wL))))
check("L: after the record the rest cannot relax below E0 + 2.30 t (L = 12): about 96 % of the injected energy is the "
      "permanent record's own, at most about 4 % can radiate",
      all(max(st) - min(st) < 1e-9 and 0.95 < st[0] / inj < 0.98 for Ls, st, inj in lrows),
      "; ".join(f"L={Ls}: stored {st[0]:.6f} of injected {inj:.6f} ({100*st[0]/inj:.1f} %)" for Ls, st, inj in lrows))


def fock_menu_cost(L, dim, menu_vecs):
    """Record on site 0 with a rank-one menu given as 4-vectors on the site's Fock basis (|0>, |u>, |d>, |ud>)."""
    h, sites, idx = one_body_H(L, dim)
    M = h.shape[0]
    c = fock_ops(M)
    cd = [x.conj().T.tocsr() for x in c]
    H = sps.csr_matrix((2**M, 2**M), dtype=complex)
    for p_ in range(M):
        for q_ in range(M):
            if abs(h[p_, q_]) > 0:
                H = H + h[p_, q_] * (cd[p_] @ c[q_])
    Nop = sum(cd[p_] @ c[p_] for p_ in range(M))
    Id = sps.identity(2**M, format='csr')
    vals, vecs = spla.eigsh((H + 5.0 * (Nop - (M // 2) * Id) @ (Nop - (M // 2) * Id)).tocsr(), k=2, which='SA')
    g = vecs[:, np.argmin(vals)]
    E0 = np.real(g.conj() @ (H @ g))
    # site Fock basis operators: |0><0| etc. built from c_0, c_1 (modes u, d of site 0)
    n_u, n_d = cd[0] @ c[0], cd[1] @ c[1]
    basis_ops = {}
    P0 = (Id - n_u) @ (Id - n_d)
    # |a><b| on the site: |u> = c_u^dag|0>, |d> = c_d^dag|0>, |ud> = c_u^dag c_d^dag |0>
    raise_ = [Id, cd[0], cd[1], cd[0] @ cd[1]]
    lower_ = [Id, c[0], c[1], c[1] @ c[0]]
    def ket_bra(i, j):
        return raise_[i] @ P0 @ lower_[j]
    Eafter = 0.0
    for v in menu_vecs:
        v = np.asarray(v, complex); v = v / np.linalg.norm(v)
        Pm = sum(v[i] * np.conj(v[j]) * ket_bra(i, j) for i in range(4) for j in range(4))
        x_ = Pm @ g
        Eafter += np.real(x_.conj() @ (H @ x_))
    return Eafter - E0


r2 = 1 / np.sqrt(2)
even_menu = [[r2, 0, 0, r2], [r2, 0, 0, -r2], [0, 1, 0, 0], [0, 0, 1, 0]]
odd_menu = [[r2, r2, 0, 0], [r2, -r2, 0, 0], [0, 0, r2, r2], [0, 0, r2, -r2]]
occ_menu = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
ce, co, cc = (fock_menu_cost(2, 3, m_) for m_ in (even_menu, odd_menu, occ_menu))
check("M: every parity-definite rank-one menu costs the full bond energy (a hop out of the site flips its parity); "
      "a parity-violating menu, forbidden by fermion superselection, would cost 3/4 of it",
      abs(ce - cc) < 1e-9 and abs(co - 0.75 * cc) < 1e-9,
      f"occupation menu {cc:.9f}, parity-definite superposition menu {ce:.9f}, parity-violating menu {co:.9f}")

# ---------------------------------------------------------------- N a record that is a particle at one site
nrows = []
for Ls in (8, 12):
    hN, _, _ = one_body_H(Ls, 3)
    wN, VN = np.linalg.eigh(hN)
    upN, wu = VN[:, wN > 0], wN[wN > 0]
    for a_ in (0, 1):
        amp = upN[a_, :]
        n2 = np.sum(np.abs(amp) ** 2)
        nrows.append((Ls, a_, n2, np.sum(np.abs(amp) ** 2 * wu) / n2, np.mean(np.abs(wN))))
check("N: moving-records reading: a particle added at one site of the sea (only empty states can take it) carries "
      "<|s|> = 1.19 t above the vacuum, half the sharp-lock cost and still the lattice scale",
      all(abs(n2 - 0.5) < 1e-9 and abs(e_ - ms) < 1e-9 for Ls, a_, n2, e_, ms in nrows),
      "; ".join(f"L={Ls} coin {a_}: weight {n2:.3f}, energy {e_:.6f} t" for Ls, a_, n2, e_, ms in nrows))

# ---------------------------------------------------------------- H, I: coarse records
L = 12
h12, sites12, idx12 = one_body_H(L, 3)
C12 = corr_ground(h12)
M12 = h12.shape[0]
site_cost12 = cut_cost(h12, C12, site_mask(M12, 0))


def weighted_cost(wts, sigma=None):
    wm = np.repeat(wts, 2)
    dW = wm[:, None] - wm[None, :]
    fac = (np.abs(dW) > 0).astype(float) if sigma is None else 1 - np.exp(-dW**2 / (8 * sigma**2))
    return -np.real(np.sum(h12 * fac * C12))


hrows = []
for R in (1, 2, 3, 4):
    wts = np.array([1.0 if all(c < R for c in s) else 0.0 for s in sites12])
    hrows.append((R, weighted_cost(wts), 6 * R * R * site_cost12 / 6))
check("H: a sharp record of a cube's total content costs (surface bonds) x (bond energy) = 2.39 R^2 t",
      all(abs(a - b) < 1e-9 for R, a, b in hrows),
      "; ".join(f"R={R}: {a:.6f}" for R, a, b in hrows))
irows = []
c0 = np.array([L / 2] * 3)
for Rs in (2.0, 3.0):
    wts = np.array([np.exp(-np.sum((np.array(s) - c0)**2) / (2 * Rs**2)) for s in sites12])
    for sig in (1.0, 4.0):
        exact = weighted_cost(wts, sig)
        approx = (site_cost12 / 6) * (1.5 * np.pi**1.5 * Rs) / (8 * sig**2)
        irows.append((Rs, sig, exact, approx))
check("I: a soft Gaussian record of a smooth region (width R, resolution sigma) costs about 0.415 R/sigma^2 t",
      all(abs(ex / ap - 1) < 0.15 for Rs, sig, ex, ap in irows if sig >= 1.0),
      "; ".join(f"R={Rs},sigma={sig}: {ex:.4f} (approx {ap:.4f})" for Rs, sig, ex, ap in irows))

# ---------------------------------------------------------------- J physical tiers (external inputs, reference only)
eV = 1.602176634e-19          # J (exact SI)
hbar_c = 1.973269804e-7       # eV m
cost_coeff = seq[-1]          # 2.387602 (units of t = hbar c / a)
rho_crit_energy = 7.7e-10     # J m^-3, reference only (critical density x c^2, h ~ 0.68)
t_universe = 4.35e17          # s, reference only
tiers = [("1 TeV (collider-safe floor)", 1e12), ("1e10 GeV (quadratic-LIV order, reference)", 1e19),
         ("Planck energy (framework open gate)", 1.22089e28)]
lines = []
ok = True
for name, E_L_eV in tiers:
    a = hbar_c / E_L_eV
    cost_J = cost_coeff * E_L_eV * eV
    tau = a / 2.99792458e8
    gamma_max = rho_crit_energy / (cost_J / a**3 * t_universe)   # per site per second
    lines.append(f"{name}: a = {a:.2e} m, record cost {cost_coeff*E_L_eV:.2e} eV = {cost_J:.2e} J, "
                 f"vacuum rate < {gamma_max:.1e}/site/s = {gamma_max*tau:.1e}/site/tick")
    ok = ok and cost_coeff * E_L_eV > 1e12 and gamma_max * tau < 1e-60
check("J: physical tiers: every tier puts a single-site record above 1 TeV and the vacuum formation rate "
      "below 1e-60 per site per tick", ok, " | ".join(lines))

print('per_element: the cost identity and the menus are checked on explicit Kraus operators.')
print('per_site: single-site records in singlet, product, random and free-fermion states are computed.')
print('per_mode: the sea costs are Brillouin-zone sums, checked against real-space and Fock-space evaluations.')
print('per_block: sharp block records and soft Gaussian records are evaluated on the 12^3 torus.')
print('lattice_wide: checked and not executed - no interacting-vacuum theorem beyond the stated models is certified.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
