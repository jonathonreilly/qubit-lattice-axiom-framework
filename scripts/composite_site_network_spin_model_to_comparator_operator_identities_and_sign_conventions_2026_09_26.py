#!/usr/bin/env python3
"""The composite-site network: local operator identities from the positive-J spin model to the quadratic Majorana comparator, and the
equality of projected sector energies across hopping-sign conventions.

Setting (all supplied, none adopted): the spin model of the landed network notes, bonds J_l (tau_i^l tau_j^l)(sigma_i . sigma_j) with
flavour l and odd paths kappa tau_q1^l tau_p^nu tau_q2^m (sigma_q1 . sigma_q2) for cyclic (l, m, nu), and the supplied quadratic
comparator H = sum_a (i/4) c^a A c^a of the landed notes (A_ij = 2 J u_ij on bonds, u_ij = i b_i b_j with i on sublattice A, and
2 kappa u u on odd hops), with the six-Majorana representation and constraints D_i = -i b^x b^y b^z c^x c^y c^z = 1. The landed review
of the flux-sector note found that equality to the positive-J spin model is not established in the comparator's sign convention.

Checks: (1) on the constrained space, sigma^a = -(i/2) eps c c and tau^l = -(i/2) eps b b obey the two-qubit Pauli algebra and
sigma^a tau^l = +i b^l c^a; (2) each
positive-J spin bond equals the comparator bond with the opposite hopping sign, as an operator identity on the constrained space of two
sites; (3) each odd path equals the comparator's odd hop with one sign, on three sites, for every colour pair and either sublattice
of the middle site; (4) the four sign conventions (bond, odd) give the same projected sector energies for random sectors on 32 to 128
sites, as the Pfaffian and sublattice-sign arguments require when N/2 is even, which holds for every admissible torus.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time
from collections import deque
from functools import reduce as freduce

import numpy as np
from scipy.linalg import schur

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


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

# ---------------------------------------------------------------- the constrained Clifford spaces of one to three sites
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2)


def majoranas(nq):
    """2 nq Majorana operators on nq qubits (Jordan-Wigner)."""
    out = []
    for k in range(nq):
        for Pm in (X, Y):
            out.append(freduce(np.kron, [Z] * k + [Pm] + [I2] * (nq - k - 1)))
    return out


def site(g, s):
    """(b, c): the six Majoranas b^x, b^y, b^z, c^x, c^y, c^z of site s."""
    return {"x": g[6 * s], "y": g[6 * s + 1], "z": g[6 * s + 2]}, {"x": g[6 * s + 3], "y": g[6 * s + 4], "z": g[6 * s + 5]}


def spins(b, c):
    """sigma^a = -(i/2) eps^{abc} c^b c^c, tau^l = -(i/2) eps^{lmn} b^m b^n."""
    return ({"x": -1j * c["y"] @ c["z"], "y": -1j * c["z"] @ c["x"], "z": -1j * c["x"] @ c["y"]},
            {"x": -1j * b["y"] @ b["z"], "y": -1j * b["z"] @ b["x"], "z": -1j * b["x"] @ b["y"]})


def Dop(b, c):
    return -1j * b["x"] @ b["y"] @ b["z"] @ c["x"] @ c["y"] @ c["z"]


g3 = majoranas(9)
dim3 = g3[0].shape[0]
S3 = [site(g3, s) for s in range(3)]
P3 = freduce(lambda a, b: a @ b, [(np.eye(dim3) + Dop(*S3[s])) / 2 for s in range(3)])
SPN = [spins(*S3[s]) for s in range(3)]
CYC = {("x", "y"): "z", ("y", "z"): "x", ("z", "x"): "y"}
res = lambda A: float(np.abs(P3 @ A @ P3).max())

# 1. local algebra
sig, tau = SPN[0]
b0, c0 = S3[0]
alg = max(res(sig["x"] @ sig["y"] - 1j * sig["z"]), res(tau["x"] @ tau["y"] - 1j * tau["z"]), res(sig["x"] @ tau["y"] - tau["y"] @ sig["x"]),
          res(sig["z"] @ sig["z"] - np.eye(dim3)), res(tau["z"] @ tau["z"] - np.eye(dim3)))
rep_p = max(res(sig[a] @ tau[l] - 1j * b0[l] @ c0[a]) for a in "xyz" for l in "xyz")
rep_m = max(res(sig[a] @ tau[l] + 1j * b0[l] @ c0[a]) for a in "xyz" for l in "xyz")
rank = int(round(np.trace(P3).real))
check("on the constrained space D_i = 1 (rank 4 per site), sigma^a = -(i/2) eps c c and tau^l = -(i/2) eps b b satisfy the two-qubit Pauli "
      "algebra, and sigma^a tau^l = +i b^l c^a", alg < 1e-12 and rep_p < 1e-12 and rep_m > 0.5 and rank == 64,
      f"three sites: rank {rank}; algebra residual {alg:.1e}; sigma tau = +i b c residual {rep_p:.1e} (-i b c: {rep_m:.1f}); {time.time() - T0:.0f} s")

# 2. the bond identity: J (tau^l tau^l)(sigma . sigma) = (i/2) s_b 2J u_ij sum_a c_i^a c_j^a, u_ij = i b_i^l b_j^l, i on sublattice A
rows2, sb = [], {}
for lam in "xyz":
    s0, t0 = SPN[0]; s1, t1 = SPN[1]
    Hs = t0[lam] @ t1[lam] @ sum(s0[a] @ s1[a] for a in "xyz")
    u01 = 1j * S3[0][0][lam] @ S3[1][0][lam]
    r = {s: res(Hs - sum(0.5j * s * 2 * u01 @ S3[0][1][a] @ S3[1][1][a] for a in "xyz")) for s in (+1, -1)}
    sb[lam] = min(r, key=r.get)
    rows2.append(f"{lam}: residual {r[1]:.1e} (+), {r[-1]:.1e} (-)")
ok2 = all(v == -1 for v in sb.values())
check("each positive-J spin bond equals, on the constrained space, the comparator bond with hopping -2J u_ij (u_ij = i b_i b_j, i on "
      "sublattice A): the comparator's +2J u_ij is the opposite sign", ok2, "; ".join(rows2) + f"; {time.time() - T0:.0f} s")

# 3. the odd path q1 -(l)- p -(m)- q2, cyclic (l, m, nu): kappa tau_q1^l tau_p^nu tau_q2^m (sigma_q1 . sigma_q2)
rows3, so = [], {}
for (l, m), nu in CYC.items():
    q1, p, q2 = 0, 1, 2
    Hs = SPN[q1][1][l] @ SPN[p][1][nu] @ SPN[q2][1][m] @ sum(SPN[q1][0][a] @ SPN[q2][0][a] for a in "xyz")
    for mid in ("A", "B"):
        if mid == "A":
            u1 = 1j * S3[p][0][l] @ S3[q1][0][l]; u2 = 1j * S3[p][0][m] @ S3[q2][0][m]
        else:
            u1 = 1j * S3[q1][0][l] @ S3[p][0][l]; u2 = 1j * S3[q2][0][m] @ S3[p][0][m]
        r = {s: res(Hs - sum(0.5j * s * 2 * u1 @ u2 @ S3[q1][1][a] @ S3[q2][1][a] for a in "xyz")) for s in (+1, -1)}
        so[((l, m), mid)] = min(r, key=r.get) if min(r.values()) < 1e-12 else 0
        rows3.append(f"({l},{m}) middle on {mid}: {r[1]:.1e} (+), {r[-1]:.1e} (-)")
vals = set(so.values())
ok3 = 0 not in vals and len(vals) == 1
check("each odd path of the spin model equals, on the constrained space, the comparator's odd hop between the two outer sites with one "
      "sign for every colour pair and for the middle site on either sublattice", ok3,
      f"sign {vals}; " + "; ".join(rows3) + f"; {time.time() - T0:.0f} s")
S_ODD = list(vals)[0] if ok3 else 0

# 4. the four sign conventions give the same projected sector energies on every admissible torus
#    (bond sign -1 and odd sign -1 together are A -> -A, the positive-J spin model; either sign alone is a sublattice flip of c)
rows4, dmax = [], 0.0
rng = np.random.default_rng(4)
for Ls in ([(4, 4, 4)] if DRY else [(4, 4, 4), (8, 4, 4), (8, 8, 4)]):
    sites, idx, Aset, bonds = cluster(Ls)
    n = len(sites); psg = parity_sign(n, bonds)
    keys = list(bonds)
    for trial in range(4 if DRY else 12):
        u = {k: (1 if trial == 0 else (-1 if rng.random() < 0.5 else 1)) for k in keys}
        es = [physical_energy(matrix(n, Aset, bonds, u, (sbd, sbd, sbd), sod * 0.3, sites, Ls, idx), n, bonds, u, psg)[0]
              for sbd in (1.0, -1.0) for sod in (1.0, -1.0)]
        dmax = max(dmax, max(es) - min(es))
    rows4.append(f"{n} sites (N/2 = {n // 2})")
check("for random bond sectors on the 32-, 64- and 128-site tori at kappa = 0.3, the four sign conventions (bond +-, odd +-) give the same "
      "projected sector energy; admissible tori have N = Lx Ly Lz / 2 = 8abc sites, so N/2 is even", dmax < 1e-9,
      ", ".join(rows4) + f"; max spread over conventions {dmax:.1e}; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
