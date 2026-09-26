#!/usr/bin/env python3
"""Finite supplied-comparator flux-pattern repetition and retained annealing-minimum diagnostics.
No spin-Hamiltonian equivalence, complete sector classification or ground-sector theorem.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

from scipy.linalg import schur
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 4800
AUDIT_INPUT_PATHS = ['docs/COMPOSITE_SITE_NETWORK_THE_HALF_FLUXED_SECTORS_THAT_UNDERCUT_THE_FLUX_FREE_ONE_ON_32_AND_64_SITES_LOSE_WHEN_REPEATED_ONTO_LARGER_CLUSTERS_BOUNDED_THEOREM_NOTE_2026-09-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_SECTOR_LOWEST_PAIR_EXCITATION_FALLS_AS_ONE_OVER_L_TO_4000_SITES_AND_THE_ODD_TERM_THINS_THE_LOW_LEVELS_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md']

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
    detQ = float(np.linalg.det(Z))
    assert np.isfinite(detQ) and abs(abs(detQ)-1.0) < 1e-8
    return detQ, float(min(eps))


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
    constraints is -1 on the free ground state (conditional parity rule from the reviewed parent, not a spin-Hamiltonian validation)."""
    ev = np.linalg.eigvalsh(1j * M)
    Ef = -1.5 * ev[ev > 1e-12].sum()
    detQ, emin = schur_det(M)
    if emin < 1e-9:
        return Ef, Ef, emin, 0
    prod_u = int(np.prod([u[k] for k in bonds]))
    v = ((-1j) ** n) * psign * ((-1j) ** len(bonds)) * prod_u * (detQ * (1j) ** (n // 2)) ** 3
    assert min(abs(v-1), abs(v+1)) < 1e-6
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
rng = np.random.default_rng(2610)
JI = (1.0, 1.0, 1.0)


def tile(u_small, Ls_small, idx_small, Ls_big, sites_big, idx_big):
    """Repeat a bond pattern of a small torus periodically onto a larger one (bond keys through the infinite network)."""
    out = {}
    for p in sites_big:
        if sum(p) % 2:
            continue
        for q in neighbours(p):
            out[key_of(p, q, Ls_big, idx_big)] = u_small[key_of(p, q, Ls_small, idx_small)]
    return out


class Cl:
    def __init__(self, Ls, kappa):
        self.Ls, self.kappa = Ls, kappa
        self.sites, self.idx, self.Aset, self.bonds, self.n, self.E, self.loops = setup(Ls, JI, kappa)
        self.psg = parity_sign(self.n, self.bonds)
        self.cuts = [[k for k in self.bonds if k[2][d] != 0] for d in range(3)]
        self.ws = winding_sectors(self.bonds, self.E)
        self.ff = min(self.phys(uw) for _, _, uw in self.ws)

    def phys(self, u):
        return physical_energy(matrix(self.n, self.Aset, self.bonds, u, JI, self.kappa, self.sites, self.Ls, self.idx), self.n, self.bonds, u, self.psg)[0]

    def best_class(self, u):
        """Lowest projected comparator energy of the pattern over the eight chosen cut representatives (sign flips across the three cuts)."""
        best = np.inf
        for w in range(8):
            u2 = dict(u)
            for d in range(3):
                if (w >> d) & 1:
                    for k in self.cuts[d]:
                        u2[k] = -u2[k]
            best = min(best, self.phys(u2))
        return best

    def nflux(self, u):
        return int((fluxes(u, self.loops) == -1).sum())


BIG = [(8, 8, 4)] if DRY else [(8, 4, 4), (8, 8, 4), (8, 8, 8)]

# ---------------------------------------------------------------- 1. the 32-site exception, repeated onto larger clusters
c32 = Cl((4, 4, 4), 0.3)
tree = spanning_tree(c32.n, c32.bonds)
assert len(tree) == c32.n-1
cotree = [k for k in c32.bonds if k not in tree]
nsec = (1 << len(cotree)) if not DRY else (1 << 10)
best_fl = (np.inf, None)
for bitsv in range(nsec):
    u = {k: 1 for k in c32.bonds}
    for i, k in enumerate(cotree):
        if (bitsv >> i) & 1:
            u[k] = -1
    if c32.nflux(u) == 0:
        continue
    e = c32.phys(u)
    if e < best_fl[0]:
        best_fl = (e, u)
rows1 = [f"32 sites: flux-free {c32.ff:.5f}, lowest fluxed {best_fl[0]:.5f} ({c32.nflux(best_fl[1])} of {len(c32.loops)} loops at -1), {best_fl[0] - c32.ff:+.5f}"]
ok1 = best_fl[0] < c32.ff - 0.5
for Lb in BIG:
    cb = Cl(Lb, 0.3)
    e = cb.best_class(tile(best_fl[1], (4, 4, 4), c32.idx, Lb, cb.sites, cb.idx))
    ok1 &= e > cb.ff
    rows1.append(f"repeated onto {cb.n} sites: {e:.4f} vs flux-free {cb.ff:.4f} ({e - cb.ff:+.4f})")
check("32 sites, kappa = 0.3: all cotree assignments swept (only fluxed candidates evaluated), the exception reproduced; its bond pattern repeated onto the 64-, 128- and 256-site "
      "clusters (best of eight chosen cut representatives) lies above the flux-free projected comparator energy", ok1, "; ".join(rows1) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2. the 64-site minima at kappa = 0.45 and 0.6, repeated
rows2, ok2, small = [], True, {}
for kappa in (0.45, 0.6):
    c64 = Cl((8, 4, 4), kappa)
    Ef, _, uf = c64.ws[0]
    keys = list(c64.bonds)
    steps = 400 if DRY else 4000
    mins = [anneal(keys, c64.E, {k: (-1 if rng.random() < 0.5 else 1) for k in keys}, steps, rng) for r in range(2 if DRY else 6)]
    mins.append(anneal(keys, c64.E, uf, steps, rng))
    b = min(mins, key=lambda m: m[0])
    pb = c64.phys(b[1])
    small[kappa] = b[1]
    good = pb < c64.ff - 0.5
    row = f"kappa {kappa}, 64 sites: annealed {pb:.4f} ({c64.nflux(b[1])} of {len(c64.loops)} loops at -1) vs flux-free {c64.ff:.4f} ({pb - c64.ff:+.4f})"
    for Lb in BIG[1:] if not DRY else BIG:
        cb = Cl(Lb, kappa)
        e = cb.best_class(tile(b[1], (8, 4, 4), c64.idx, Lb, cb.sites, cb.idx))
        good &= e > cb.ff
        row += f"; repeated onto {cb.n}: {e - cb.ff:+.4f}"
    ok2 &= good
    rows2.append(row)
check("64 sites, kappa = 0.45 and 0.6: annealing finds half-fluxed sectors below the flux-free projected comparator energy, and the same patterns "
      "repeated onto 128 and 256 sites lie above it", ok2, "; ".join(rows2) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 3. annealing on 128 and 256 sites
rows3, ok3 = [], True
for kappa in (0.45, 0.6):
    for Lb, steps, nrand in ([((8, 8, 4), 600, 1)] if DRY else [((8, 8, 4), 6000, 2), ((8, 8, 8), 4000, 2)]):
        cb = Cl(Lb, kappa)
        keys = list(cb.bonds)
        Ef, _, uf = cb.ws[0]
        starts = [uf] + [{k: (-1 if rng.random() < 0.5 else 1) for k in keys} for _ in range(nrand)] + [tile(small[kappa], (8, 4, 4), Cl((8, 4, 4), kappa).idx, Lb, cb.sites, cb.idx)]
        found = [anneal(keys, cb.E, s, steps, rng) for s in starts]
        phys = [cb.phys(m[1]) for m in found]
        low = min(phys)
        ok3 &= low >= cb.ff - 1e-9
        rows3.append(f"kappa {kappa}, {cb.n} sites: flux-free {cb.ff:.4f}; annealed minima " + ", ".join(f"{p - cb.ff:+.4f} ({cb.nflux(m[1])} loops at -1)" for p, m in zip(phys, found)))
check("128 and 256 sites, kappa = 0.45 and 0.6: annealing from the flux-free sector, from random bonds and from the repeated 64-site "
      "minimum retains no free-energy minimum whose projected comparator energy lies below the flux-free one", ok3, "; ".join(rows3) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
