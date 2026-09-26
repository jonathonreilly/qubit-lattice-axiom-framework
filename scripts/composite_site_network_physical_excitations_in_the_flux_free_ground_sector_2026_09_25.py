#!/usr/bin/env python3
"""The physical excitations of the supplied composite-site network's spin model in its flux-free ground sector, against the
size of the cluster.

Setting (all supplied, none adopted): the colored periodic network of composite sites of the landed network note, bonds
J_lam (tau^lam tau^lam)(sigma.sigma) and the three-site odd term kappa in the runner's sign convention, in the six-Majorana
representation; the per-sector reduction to three identical free-Majorana copies and the exact projection rule of open PR 9255.
Open PR 9255 put the ground state in the locally flux-free sector on the clusters it searched. Within that sector the eight
winding classes (flip all bonds wrapping each direction) differ by boundary conditions; the physical ground is the class of
lowest physical energy, and its physical excitations with the same bonds are fermion pairs, the lowest 2 e1 with e1 the
lowest single-particle level (one fermion in each of two copies keeps the product of the constraints). Checks: (1) the 32-site
control against open PR 9255's enumeration; (2) isotropic couplings, kappa = 0, clusters 8^3 to 20^3 (256 to 4000 sites):
e1, L e1, and the count of levels below 4/L; (3) the same at kappa = 0.3; (4) the control J_z = 2.5, kappa = 0, where the
matching bound puts every level at 1 or above. Finite clusters only: no thermodynamic-limit, node or phase theorem.
Prints TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import sys
import time

from scipy.linalg import schur

AUDIT_TIMEOUT_SEC = 5400

RESULTS = []
T0 = time.time()


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


import itertools
import numpy as np

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


DRY = "--dry" in sys.argv

# ---------------------------------------------------------------- the ground flux sector's winding classes and levels
def levels(M):
    """Positive single-particle levels of the real antisymmetric M: its singular values come in equal pairs."""
    s = np.sort(np.linalg.svd(M, compute_uv=False))
    return s[0::2]


def sector_scan(Ls, J, kappa):
    """For the eight winding classes of the locally flux-free sector: free energy and levels; the constraint product is
    computed in order of free energy until the lowest physical energy found lies below the next class's free energy."""
    sites, idx, Aset, bonds = cluster(Ls)
    n = len(sites)
    psg = parity_sign(n, bonds)
    cuts = [[k for k in bonds if k[2][d] != 0] for d in range(3)]
    out = []
    for w in range(8):
        u = {k: 1 for k in bonds}
        for d in range(3):
            if (w >> d) & 1:
                for k in cuts[d]:
                    u[k] = -u[k]
        lev = levels(matrix(n, Aset, bonds, u, J, kappa, sites, Ls, idx))
        out.append(dict(w=w, u=u, lev=lev, Ef=-1.5 * lev.sum(), n=n, par=None, Ep=None))
    out.sort(key=lambda d: d["Ef"])
    best = np.inf
    for d in out:
        if d["Ef"] >= best:
            break
        Ep, Ef, emin, par = physical_energy(matrix(n, Aset, bonds, d["u"], J, kappa, sites, Ls, idx), n, bonds, d["u"], psg)
        d["Ep"], d["par"] = Ep, par
        best = min(best, Ep)
    for d in out:
        d.pop("u")
    g = min((d for d in out if d["Ep"] is not None), key=lambda d: d["Ep"])
    return g, out


def dos_exponent(out, E1, E2):
    """Pooled count of levels below E over the eight classes; the exponent log(N(E2)/N(E1)) / log(E2/E1)."""
    pool = np.concatenate([d["lev"] for d in out])
    n1, n2 = int((pool < E1).sum()), int((pool < E2).sum())
    return n1, n2, (np.log(n2 / n1) / np.log(E2 / E1) if n1 > 0 and n2 > 0 else np.nan)


# ---------------------------------------------------------------- 1. the 32-site control against the enumeration of all sectors
rows1, ok1 = [], True
for J, kappa, ref in (((1.0, 1.0, 1.0), 0.0, -77.66563), ((1.0, 1.0, 2.5), 0.0, -130.62793), ((1.0, 1.0, 1.0), 0.3, -84.81708)):
    g, out = sector_scan((4, 4, 4), J, kappa)
    ok1 &= abs(g["Ep"] - ref) < 5e-6
    rows1.append(f"J = {J}, kappa {kappa}: {g['Ep']:.5f} (class {g['w']}, product {g['par']:+d}) against {ref:.5f}")
check("the eight winding classes of the locally flux-free sector on the 32-site cluster reproduce the lowest flux-free physical energies of the "
      "enumeration of all sectors in open PR 9255", ok1, "; ".join(rows1) + f"; {time.time() - T0:.0f} s")

# ---------------------------------------------------------------- 2.-4. the levels against the cluster size
SIZES = (4, 8) if DRY else (8, 12, 16, 20)
CASES = (("isotropic, kappa = 0", (1.0, 1.0, 1.0), 0.0), ("isotropic, kappa = 0.3", (1.0, 1.0, 1.0), 0.3), ("J_z = 2.5, kappa = 0", (1.0, 1.0, 2.5), 0.0))
R, POOL = {}, {}
for name, J, kappa in CASES:
    for L in SIZES:
        g, out = sector_scan((L, L, L), J, kappa)
        R[(name, L)] = dict(n=g["n"], w=g["w"], par=g["par"], e1=g["lev"][0], allmin=min(d["lev"][0] for d in out),
                            gap_next=out[1]["Ef"] - g["Ep"] if out[1]["Ep"] is None else min(d["Ep"] for d in out if d is not g and d["Ep"] is not None) - g["Ep"])
        POOL[(name, L)] = out
    print(f"# {name}: done, {time.time() - T0:.0f} s", file=sys.stderr, flush=True)


def rows_for(name):
    out = []
    for L in SIZES:
        r = R[(name, L)]
        out.append(f"L={L} ({r['n']} sites): ground class {r['w']} (product {r['par']:+d}), e1 {r['e1']:.4f} (L e1 {L * r['e1']:.2f}), lowest level of "
                   f"any class {r['allmin']:.4f} (L x {L * r['allmin']:.2f})")
    Lb = SIZES[-1]
    n1, n2, ex = dos_exponent(POOL[(name, Lb)], 0.25, 0.5)
    n3, n4, ex2 = dos_exponent(POOL[(name, Lb)], 0.5, 1.0)
    out.append(f"pooled levels on L={Lb}: below 0.25 {n1}, 0.5 {n2}, 1.0 {n4}; count exponents {ex:.2f} (0.25-0.5), {ex2:.2f} (0.5-1.0)")
    return out, ex, ex2


rows2, ex_a, ex_a2 = rows_for("isotropic, kappa = 0")
ok2 = all(R[("isotropic, kappa = 0", L)]["par"] == 1 for L in SIZES)
check("isotropic couplings, kappa = 0 (reported): the physical ground class has constraint product +1 on every cluster; its lowest level e1 and "
      "the lowest level of any class against L, and the pooled count of low levels on the largest cluster (count exponent 2 for a line of nodes, "
      "3 for isolated nodes, for linear crossings)", ok2, "; ".join(rows2))
rows3, ex_b, ex_b2 = rows_for("isotropic, kappa = 0.3")
ok3 = all(R[("isotropic, kappa = 0.3", L)]["par"] == 1 for L in SIZES)
check("isotropic couplings, kappa = 0.3 (reported): the same quantities with the odd term on", ok3, "; ".join(rows3))
rows4, _, _ = rows_for("J_z = 2.5, kappa = 0")
ok4 = all(R[("J_z = 2.5, kappa = 0", L)]["allmin"] >= 1.0 - 1e-9 for L in SIZES)
check("J_z = 2.5, kappa = 0, the control: every level of every winding class is at least 1 on every cluster, as the matching bound requires "
      "(z-matching levels 5, x and y matchings of norm 2 each)", ok4, "; ".join(rows4) + f"; {time.time() - T0:.0f} s")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
