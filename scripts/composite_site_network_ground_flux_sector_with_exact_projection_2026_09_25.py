#!/usr/bin/env python3
"""The ground-state flux sector of the supplied composite-site network's spin model, with the projection onto physical states exact.

Setting (all supplied, none adopted): the colored periodic network of composite sites of the landed note
docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md
(its explicit site and flavour rules, reproduced below), bonds J_lam (tau^lam tau^lam)(sigma.sigma) with flavour lam, and the
three-site odd term of strength kappa in this runner's sign convention. In the six-Majorana representation the bond variables
u = i b b are conserved and, in each sector {u}, the model is three identical copies of one free-Majorana hopping problem: the
lowest free energy of a sector is -(3/2) times the sum of the positive levels of iA({u}). The projection onto physical states
(every local constraint D_i = 1) is exact here: the product of all D_i on a sector's free ground state is (-i)^N times a
Majorana-reordering sign times (-i)^(number of bonds) times the product of the bond variables times (det Q i^(N/2))^3, where Q is
the orthogonal matrix that brings the hopping matrix to canonical form; when that product is -1 the sector's lowest physical
state carries one excitation, at the lowest level. Checks: (1) the reduction's gauge invariance and the cluster structure;
(2) the projection rule against exact diagonalization of the full 16-qubit spin model on 8 sites; (3) every gauge-inequivalent
sector of the 32-site cluster (131072), physical energies, kappa = 0, isotropic and anisotropic couplings; (4) annealing over all
bond configurations on 64- and 256-site clusters, kappa = 0 and 0.3; (5) every sector of the 32-site cluster at kappa = +-0.3,
the exception. Finite clusters only: no thermodynamic-limit flux theorem, phase or physical identification. Prints
TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

from scipy.linalg import schur
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 1200

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


import itertools
import numpy as np
from collections import deque

AX = {"x": 0, "y": 1, "z": 2}


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


def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0:
        return "z"
    lo = p if sum(d) > 0 else q
    m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"


def neighbours(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q):
                out.append(q)
    return out


def cluster(Ls):
    """Multigraph on the torus: bond keys (a, b, R) with a on sublattice A, R the wrap vector from p's image to q's."""
    sites = [p for p in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])) if is_site(p)]
    idx = {p: n for n, p in enumerate(sites)}
    Aset = {n for n, p in enumerate(sites) if sum(p) % 2 == 0}
    bonds = {}
    for p in sites:
        if sum(p) % 2:
            continue
        for q in neighbours(p):
            qf = tuple(q[b] % Ls[b] for b in range(3))
            R = tuple((q[b] - qf[b]) // Ls[b] for b in range(3))
            bonds[(idx[p], idx[qf], R)] = flavour(p, q)
    return sites, idx, Aset, bonds


def key_of(p, q, Ls, idx):
    """Bond key of the infinite-lattice bond p-q."""
    if sum(p) % 2:
        p, q = q, p
    pf = tuple(p[b] % Ls[b] for b in range(3))
    shift = tuple((p[b] - pf[b]) for b in range(3))
    q0 = tuple(q[b] - shift[b] for b in range(3))                 # translate so that p sits in the fundamental domain
    qf = tuple(q0[b] % Ls[b] for b in range(3))
    R = tuple((q0[b] - qf[b]) // Ls[b] for b in range(3))
    return (idx[pf], idx[qf], R)


def ten_loops(Ls, idx, sites):
    """Every 10-cycle of the infinite graph with a vertex in the fundamental domain, as a frozenset of bond keys (deduplicated)."""
    out = set()
    for p0 in sites:
        stack = [(p0, [p0])]
        while stack:
            v, path = stack.pop()
            if len(path) == 11:
                continue
            for w in neighbours(v):
                if w == p0 and len(path) == 10:
                    cyc = path + [p0]
                    out.add(frozenset(key_of(cyc[i], cyc[i + 1], Ls, idx) for i in range(10)))
                elif w not in path and len(path) < 10:
                    stack.append((w, path + [w]))
    return [l for l in out if len(l) == 10]


def spanning_tree(n, bonds):
    adj = {i: [] for i in range(n)}
    for k in bonds:
        a, b, R = k
        adj[a].append((b, k)); adj[b].append((a, k))
    seen, tree, q = {0}, set(), deque([0])
    while q:
        v = q.popleft()
        for w, k in adj[v]:
            if w not in seen:
                seen.add(w); q.append(w); tree.add(k)
    return tree


def matrix(n, Aset, bonds, u, J, kappa, sites, Ls, idx):
    M = np.zeros((n, n))
    for k, fl in bonds.items():
        a, b, R = k
        M[a, b] += 2 * J[AX[fl]] * u[k]
        M[b, a] -= 2 * J[AX[fl]] * u[k]
    if kappa:
        for p in sites:
            nb = {flavour(p, q): q for q in neighbours(p)}
            for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
                q1, q2 = nb[l], nb[m]
                g = u[key_of(p, q1, Ls, idx)] * u[key_of(p, q2, Ls, idx)]
                a1 = idx[tuple(q1[b] % Ls[b] for b in range(3))]; a2 = idx[tuple(q2[b] % Ls[b] for b in range(3))]
                M[a1, a2] += 2 * kappa * g
                M[a2, a1] -= 2 * kappa * g
    return M


def energy(M):
    ev = np.linalg.eigvalsh(1j * M)
    return -1.5 * ev[ev > 0].sum()


def windings(n, bonds, tree, sites, Ls):
    """Fundamental cycles of the cotree bonds with nonzero total wrap: their bond lists and wrap vectors."""
    adj = {i: [] for i in range(n)}
    for k in tree:
        a, b, R = k
        adj[a].append((b, k, R)); adj[b].append((a, k, tuple(-r for r in R)))
    parent = {0: None}; wrap = {0: (0, 0, 0)}; q = deque([0])
    while q:
        v = q.popleft()
        for w, k, R in adj[v]:
            if w not in parent:
                parent[w] = (v, k); wrap[w] = tuple(wrap[v][i] + R[i] for i in range(3)); q.append(w)
    def path_to_root(v):
        ks = []
        while parent[v] is not None:
            v0, k = parent[v]; ks.append(k); v = v0
        return ks
    out = []
    for k in bonds:
        if k in tree:
            continue
        a, b, R = k
        tot = tuple(wrap[a][i] + R[i] - wrap[b][i] for i in range(3))
        if any(tot):
            ks = set(path_to_root(a)) ^ set(path_to_root(b))
            out.append((ks | {k}, tot))
    return out




def schur_det(M):
    """det of the orthogonal Q with Q^T M Q = blocks [[0, e],[-e, 0]], e > 0, and the smallest level e."""
    T, Z = schur(M, output="real")
    Z = Z.copy(); m = M.shape[0]; eps = []
    i = 0
    while i < m:
        if i + 1 < m and abs(T[i + 1, i]) > 1e-12:
            e = T[i, i + 1]
            if e < 0:
                Z[:, [i, i + 1]] = Z[:, [i + 1, i]]
                e = -e
            eps.append(e); i += 2
        else:
            eps.append(0.0); i += 1
    return float(np.linalg.det(Z)), float(min(eps))


def perm_sign(seq):
    seq = list(seq); sgn = 1
    for i in range(len(seq)):
        while seq[i] != i:
            j = seq[i]; seq[i], seq[j] = seq[j], seq[i]; sgn = -sgn
    return sgn


def parity_sign(n, bonds):
    """Reordering sign taking the site-ordered product of all 6N Majoranas (b^x b^y b^z c^x c^y c^z per site) to the bond-paired b's
    followed by the flavour-grouped c's."""
    target = []
    for (a, b, R), lam in bonds.items():
        target += [6 * a + AX[lam], 6 * b + AX[lam]]
    for al in range(3):
        target += [6 * i + 3 + al for i in range(n)]
    return perm_sign(target)


def physical_energy(M, n, bonds, u, psign):
    """Lowest energy of the sector's physical states: the free ground energy, plus the lowest level when the product of the local
    constraints is -1 on the free ground state (validated against exact diagonalization in check 2)."""
    ev = np.linalg.eigvalsh(1j * M)
    Ef = -1.5 * ev[ev > 1e-12].sum()
    detQ, emin = schur_det(M)
    if emin < 1e-9:
        return Ef, Ef, emin, 0
    prod_u = int(np.prod([u[k] for k in bonds]))
    v = ((-1j) ** n) * psign * ((-1j) ** len(bonds)) * prod_u * (detQ * (1j) ** (n // 2)) ** 3
    ok = abs(v - 1) < 1e-6
    return Ef + (0.0 if ok else emin), Ef, emin, (1 if ok else -1)


def fluxes(u, loops):
    return np.array([int(np.prod([u[k] for k in l])) for l in loops])


def winding_sectors(bonds, E):
    u0 = {k: 1 for k in bonds}
    cuts = [[k for k in bonds if k[2][d] != 0] for d in range(3)]
    out = []
    for w in range(8):
        u = dict(u0)
        for d in range(3):
            if (w >> d) & 1:
                for k in cuts[d]:
                    u[k] = -u[k]
        out.append((E(u), w, u))
    out.sort(key=lambda x: x[0])
    return out


def anneal(keys, E, u_start, steps, rng):
    u = dict(u_start); e = E(u); best = (e, dict(u))
    for s in range(steps):
        Tm = 0.5 * (0.002 / 0.5) ** (s / max(1, steps - 1))
        k = keys[rng.integers(len(keys))]
        u[k] = -u[k]
        e2 = E(u)
        if e2 <= e or rng.random() < np.exp(-(e2 - e) / Tm):
            e = e2
            if e < best[0]:
                best = (e, dict(u))
        else:
            u[k] = -u[k]
    return best


def setup(Ls, J, kappa):
    sites, idx, Aset, bonds = cluster(Ls)
    n = len(sites)
    E = lambda u: energy(matrix(n, Aset, bonds, u, J, kappa, sites, Ls, idx))
    return sites, idx, Aset, bonds, n, E, ten_loops(Ls, idx, sites)


DRY = "--dry" in sys.argv
rng = np.random.default_rng(2509)

# ---------------------------------------------------------------- 1. the reduction and the clusters
rows1, ok1 = [], True
for Ls in ((4, 4, 4), (8, 4, 4)) if not DRY else ((4, 4, 4),):
    sites, idx, Aset, bonds, n, E, loops = setup(Ls, (1.0, 1.0, 1.0), 0.3)
    u = {k: (-1 if rng.random() < 0.5 else 1) for k in bonds}
    e1 = E(u)
    g = {s: (-1 if rng.random() < 0.5 else 1) for s in range(n)}                       # a gauge transformation at every site
    ug = {k: u[k] * g[k[0]] * g[k[1]] for k in bonds}
    same_flux = np.array_equal(fluxes(u, loops), fluxes(ug, loops))
    ok1 &= len(bonds) == 3 * n // 2 and len(loops) == n and same_flux and abs(E(ug) - e1) < 1e-9
    rows1.append(f"{Ls}: {n} sites, {len(bonds)} bonds, {len(loops)} 10-loops; a random gauge transformation keeps the fluxes and the energy "
                 f"({e1:.6f} vs {E(ug):.6f})")
check("the free-Majorana reduction per sector: trivalent multigraphs on the tori, one 10-loop per site, and sector energies that depend only on the "
      "fluxes (gauge invariance, with the odd term on)", ok1, "; ".join(rows1))

# ---------------------------------------------------------------- 2. the projection rule against exact diagonalization of the spin model
sites8, idx8, Aset8, bonds8 = cluster((2, 2, 4))
n8 = len(sites8)
psign8 = parity_sign(n8, bonds8)
nq = 2 * n8
dim = 1 << nq
st = np.arange(dim, dtype=np.int64)
def pauli_term(ops):
    xm = zm = 0; ny = 0
    for q, pp in ops:
        if pp in "xy":
            xm |= 1 << q
        if pp in "yz":
            zm |= 1 << q
        if pp == "y":
            ny += 1
    par = np.zeros(dim, dtype=np.int64); t = st & zm
    while np.any(t):
        par ^= t & 1; t = t >> 1
    return st ^ xm, (1j ** ny) * (1 - 2 * par)
tree8 = spanning_tree(n8, bonds8)
cot8 = [k for k in bonds8 if k not in tree8]
rows2, ok2 = [], True
for J in ((1.0, 1.0, 2.5), (0.4, 1.0, 1.6), (1.0, 1.0, 0.3)) if not DRY else ((1.0, 1.0, 2.5),):
    rr, cc, vv = [], [], []
    for (a, b, R), lam in bonds8.items():
        for al in ("x", "y", "z"):
            r_, v_ = pauli_term([(2 * a, lam), (2 * b, lam), (2 * a + 1, al), (2 * b + 1, al)])
            rr.append(r_); cc.append(st); vv.append(J[AX[lam]] * v_)
    H = coo_matrix((np.concatenate(vv), (np.concatenate(rr), np.concatenate(cc))), shape=(dim, dim)).tocsr()
    lev = np.sort(eigsh(H, k=120, which="SA", return_eigenvectors=False))
    phys = []
    for bitsv in range(1 << len(cot8)):
        u = {k: 1 for k in bonds8}
        for i, k in enumerate(cot8):
            if (bitsv >> i) & 1:
                u[k] = -1
        phys.append(physical_energy(matrix(n8, Aset8, bonds8, u, J, 0.0, sites8, (2, 2, 4), idx8), n8, bonds8, u, psign8)[0])
    inside = [e for e in phys if e < lev[-1] - 1e-6]
    found = sum(np.min(np.abs(lev - e)) < 1e-7 for e in inside)
    ok2 &= found == len(inside) and len(inside) > 0 and abs(min(phys) - lev[0]) < 1e-8
    rows2.append(f"J = {J}: {found} of {len(inside)} sectors' lowest physical levels found among the lowest 120 exact levels; ground {min(phys):.6f} vs exact {lev[0]:.6f}")
check("the projection rule against exact diagonalization of the full 16-qubit spin model on the 8-site cluster: every sector's lowest physical level, "
      "as the rule assigns it, is an exact eigenvalue, and the lowest is the exact ground energy", ok2, "; ".join(rows2) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3. every sector of the 32-site cluster, kappa = 0, physical energies
rows3x, ok3x, gap_iso = [], True, None
for J in ((1.0, 1.0, 1.0), (1.0, 1.0, 2.5)) if not DRY else ((1.0, 1.0, 1.0),):
    Ls = (4, 4, 4)
    sites, idx, Aset, bonds, n, E, loops = setup(Ls, J, 0.0)
    tree = spanning_tree(n, bonds)
    cotree = [k for k in bonds if k not in tree]
    u0 = {k: 1 for k in bonds}
    best_ff, best_fl, count = np.inf, np.inf, 0
    psg = parity_sign(n, bonds)
    for bitsv in range(1 << len(cotree)) if not DRY else range(1 << 8):
        u = dict(u0)
        for i, k in enumerate(cotree):
            if (bitsv >> i) & 1:
                u[k] = -1
        e = physical_energy(matrix(n, Aset, bonds, u, J, 0.0, sites, Ls, idx), n, bonds, u, psg)[0]; count += 1
        if np.all(fluxes(u, loops) == 1):
            best_ff = min(best_ff, e)
        else:
            best_fl = min(best_fl, e)
    ok3x &= best_ff < best_fl
    if J == (1.0, 1.0, 1.0):
        gap_iso = best_fl - best_ff
    rows3x.append(f"J = {J}: {count} sectors; lowest locally flux-free {best_ff:.5f}, lowest with any 10-loop at flux -1 {best_fl:.5f}, physical flux gap {best_fl - best_ff:.5f}")
check("every gauge-inequivalent sector of the 32-site cluster at kappa = 0, physical energies: the spin model's ground state is locally flux-free "
      "(all 32 ten-loops at flux +1) for isotropic and for gapped anisotropic couplings", ok3x, "; ".join(rows3x) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 4. annealing on 64 and 256 sites
PLAN = [((8, 4, 4), 0.0, 1500, 3), ((8, 4, 4), 0.3, 1500, 3), ((8, 8, 8), 0.0, 1200, 2), ((8, 8, 8), 0.3, 1200, 2)]
if DRY:
    PLAN = [((8, 4, 4), 0.3, 100, 1)]
rows3, ok3, ground = [], True, {}
for Ls, kappa, steps, runs in PLAN:
    sites, idx, Aset, bonds, n, E, loops = setup(Ls, (1.0, 1.0, 1.0), kappa)
    ws = winding_sectors(bonds, E)
    Ef, _, uf = ws[0]
    keys = list(bonds)
    flips = sorted(E({**uf, k: -uf[k]}) - Ef for k in keys[:: max(1, len(keys) // 48)])
    mins = [anneal(keys, E, uf if r == 0 else {k: (-1 if rng.random() < 0.5 else 1) for k in keys}, steps, rng) for r in range(runs)]
    low = min(m[0] for m in mins)
    psg = parity_sign(n, bonds)
    phys_ff = min(physical_energy(matrix(n, Aset, bonds, uw, (1.0, 1.0, 1.0), kappa, sites, Ls, idx), n, bonds, uw, psg)[0] for _, _, uw in ws)
    fl_free_min = min(Ef + flips[0], min(m[0] for m in mins if int((fluxes(m[1], loops) == -1).sum()) > 0) if any(int((fluxes(m[1], loops) == -1).sum()) > 0 for m in mins) else np.inf)
    ok3 &= low >= Ef - 1e-9 and flips[0] > 0 and phys_ff < fl_free_min
    ground[(Ls, kappa)] = (Ef, uf, n, sites, idx, Aset, bonds)
    rows3.append(f"{Ls} kappa {kappa}: flux-free ground {Ef:.5f} ({Ef / n:.5f} per site), physical {phys_ff:.5f}; lowest fluxed free energy found "
                 f"{fl_free_min:.5f} (a lower bound on its physical energy), margin {fl_free_min - phys_ff:+.4f}; single-bond flips cost {flips[0]:.4f}-{flips[-1]:.4f}; "
                 f"annealed minima " + ", ".join(f"{m[0] - Ef:+.4f} ({int((fluxes(m[1], loops) == -1).sum())} loops at -1)" for m in mins))
check("annealing over every bond configuration on the 64- and 256-site clusters, kappa = 0 and 0.3: no sector below the locally flux-free one is "
      "found, every single-bond flip costs energy, and the physical flux-free energy lies below every fluxed sector found", ok3, "; ".join(rows3) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 5. every sector of the 32-site cluster at kappa = +-0.3: the exception
sites, idx, Aset, bonds = cluster((4, 4, 4))
n = len(sites)
loops = ten_loops((4, 4, 4), idx, sites)
tree = spanning_tree(n, bonds)
cotree = [k for k in bonds if k not in tree]
psg = parity_sign(n, bonds)
nsec = (1 << len(cotree)) if not DRY else (1 << 8)
tab = {}
for kappa in (0.3, -0.3):
    Ep_all = np.empty(nsec)
    best = {}
    for bitsv in range(nsec):
        u = {k: 1 for k in bonds}
        for i, k in enumerate(cotree):
            if (bitsv >> i) & 1:
                u[k] = -1
        Ep, Ef, emin, par = physical_energy(matrix(n, Aset, bonds, u, (1.0, 1.0, 1.0), kappa, sites, (4, 4, 4), idx), n, bonds, u, psg)
        Ep_all[bitsv] = Ep
        nf = int((fluxes(u, loops) == -1).sum())
        cls = "ff" if nf == 0 else "fl"
        if cls not in best or Ep < best[cls][0]:
            best[cls] = (Ep, nf, par)
    tab[kappa] = (Ep_all, best)
even = float(np.max(np.abs(tab[0.3][0] - tab[-0.3][0])))
b = tab[0.3][1]
ok5 = even < 1e-8 and b["fl"][0] < b["ff"][0]
check("every sector of the 32-site cluster at kappa = +-0.3, physical energies: the exception, a fluxed sector below the locally flux-free one, "
      "with every sector's physical energy even in kappa", ok5,
      f"{nsec} sectors per sign; lowest flux-free {b['ff'][0]:.5f} (product {b['ff'][2]:+d}); lowest fluxed {b['fl'][0]:.5f} with {b['fl'][1]} of "
      f"{len(loops)} loops at -1 (product {b['fl'][2]:+d}), {b['fl'][0] - b['ff'][0]:+.5f}; max |E(+kappa) - E(-kappa)| over sectors {even:.1e}; "
      f"{time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
