#!/usr/bin/env python3
"""Record fields keep the carved Majoranas sublattice-symmetric; a gapless start plus a time-reversal-odd term gives a Chern number.

Open PR 9054 carved exactly solvable three-dimensional Kitaev networks: at
the compass point of the fully soldered clause, with records as fields,
every unrecorded site keeps at most one bond per axis, and its content rule
makes records orthogonal to kept axes, so record fields sit on dangling
axes only. Open PR 9088 found no covariant time-reversal-odd star term that
keeps a carving's Majoranas free. This runner asks what record fields do to
chirality (supplied models, finite diagnostics, no physical reading):

1. Sublattice symmetry: give each c Majorana the parity of its site and
   each dangling b Majorana the opposite parity. Under the content rule
   every coupling joins opposite classes, so S = diag(+-1) anticommutes with
   the Bloch Hamiltonian (4x4x4 cells, an even period) in every gauge sector
   and for any field values.
2. So every weak Chern number of the lowest sector's negative bands vanishes
   on the planes k_a = 0 and pi (both networks carry flat zero bands, 2 and 4
   per cell; with particle-hole symmetry S forces zero on those planes).
3. Outside the content rule, a leaf (a site with one kept bond, axis c) could
   carry a field along c and stay solvable, since sigma^c_j = -i b^a_j b^b_j
   on the physical space; that couples two same-class Majoranas and breaks
   S. On a two-site leaf pair the free-Majorana spectrum in one parity
   sector equals the exact spin spectrum.
4. Kitaev's pattern s^a_i s^b_m s^c_k on every bond pair (Majorana image
   -i eps_abc u_im u_mk c_i c_k, a same-class hopping) breaks S. Two exact zero
   bands per cell stay at zero, the refined gap above them stays open at
   kappa = 0.05, 0.2, 1, 4 (growing from zero in the 16-site network, where
   kappa splits two of its four flat bands), and every weak Chern number
   stays 0.
5. A gapless start changes this: the 20-site network with its dangling
   Majoranas decoupled (zero dangling fields) is gapless, and Kitaev's
   pattern at kappa = 0.3 gaps it (0.0528) with weak Chern numbers (1, 0, 0).
   Its records cannot all be chosen with zero fields (7 touch unrecorded
   sites along all three axes).
6. Zero dangling fields are realizable on other three-direction networks: a
   SAT search finds 16 on 4x4x4 in which no record touches unrecorded sites
   along all three axes; 8 of them have gapless dispersive Majorana bands.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 600

import numpy as np
from pysat.card import CardEnc, EncType
from pysat.solvers import Glucose4
from scipy.optimize import minimize

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


# ------------------------------------------------ the networks of open PR 9054 (compass point, generic records)
L3 = (4, 4, 4)
# generic record contents: the fixed direction (1, sqrt 2, sqrt 3) projected
# orthogonal to each record's constrained axes; its components are positive,
# so the two records on a dangling axis never cancel
V_GENERIC = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)]) / np.sqrt(6.0)
N20 = [(0, 0, 0), (0, 0, 3), (0, 1, 0), (0, 2, 1), (0, 2, 2), (0, 3, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
       (1, 1, 1), (1, 2, 1), (2, 0, 1), (2, 0, 2), (2, 1, 1), (2, 1, 2), (3, 0, 0), (3, 1, 2), (3, 2, 2),
       (3, 3, 0), (3, 3, 1)]
N16 = [(0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 1, 2), (1, 1, 3), (2, 0, 3), (2, 1, 0),
       (2, 1, 3), (2, 2, 0), (3, 0, 2), (3, 0, 3), (3, 2, 0), (3, 2, 1), (3, 3, 1), (3, 3, 2)]


def nbr(s, ax, d, Ls=L3):
    t = list(s)
    t[ax] = (t[ax] + d) % Ls[ax]
    return tuple(t)


def winding_rank(comp, Ls=L3):
    comp = set(comp)
    s0 = min(comp)
    pos = {s0: (0, 0, 0)}
    stack = [s0]
    wind = set()
    while stack:
        v = stack.pop()
        for ax in range(3):
            for d in (1, -1):
                t = list(v)
                t[ax] += d
                off = [0, 0, 0]
                if t[ax] == Ls[ax]:
                    t[ax], off[ax] = 0, 1
                if t[ax] == -1:
                    t[ax], off[ax] = Ls[ax] - 1, -1
                w = tuple(t)
                if w not in comp:
                    continue
                pw = tuple(pos[v][i] + off[i] for i in range(3))
                if w in pos:
                    if pos[w] != pw:
                        wind.add(tuple(pw[i] - pos[w][i] for i in range(3)))
                else:
                    pos[w] = pw
                    stack.append(w)
    rank = int(np.linalg.matrix_rank(np.array(sorted(wind)))) if wind else 0
    return len(pos) == len(comp), rank


def build(comp, Ls=L3):
    comp = sorted(comp)
    ix = {s: i for i, s in enumerate(comp)}
    cs = set(comp)
    bonds = []
    for s in comp:
        for ax in range(3):
            t = list(s)
            t[ax] += 1
            off = [0, 0, 0]
            if t[ax] == Ls[ax]:
                t[ax], off[ax] = 0, 1
            t = tuple(t)
            if t in cs:
                bonds.append((ix[s], ix[t], ax, tuple(off)))
    contents, cons_ok = {}, True
    for r in itertools.product(*[range(l) for l in Ls]):
        if r in cs:
            continue
        cons = set()
        for ax in range(3):
            for d in (1, -1):
                u = nbr(r, ax, d, Ls)
                if u in cs and nbr(u, ax, d, Ls) in cs:
                    cons.add(ax)
        if len(cons) > 2:
            cons_ok = False
            continue
        q = V_GENERIC.copy()
        for a in cons:
            q[a] = 0.0
        contents[r] = q / np.linalg.norm(q)
    kept_field, dfield = 0.0, {}
    for s in comp:
        for ax in range(3):
            for d in (1, -1):
                r = nbr(s, ax, d, Ls)
                if r in cs:
                    continue
                f = contents[r][ax] if r in contents else 0.0
                if nbr(s, ax, -d, Ls) in cs:
                    kept_field = max(kept_field, abs(f))
                else:
                    dfield[(ix[s], ax)] = dfield.get((ix[s], ax), 0.0) + f
    live = [key for key, v in dfield.items() if abs(v) > 0]
    uf = list(range(len(comp)))

    def fnd(a):
        while uf[a] != a:
            uf[a] = uf[uf[a]]
            a = uf[a]
        return a

    tree, non = [], []
    for b in bonds:
        ra, rb = fnd(b[0]), fnd(b[1])
        if ra != rb:
            uf[ra] = rb
            tree.append(b)
        else:
            non.append(b)
    per_axis = all(sum(nbr(s, ax, d, Ls) in cs for d in (1, -1)) <= 1 for s in comp for ax in range(3))
    return dict(comp=comp, ix=ix, n=len(comp), bonds=bonds, dfield=dfield, live=live, tree=tree, non=non,
                cons_ok=cons_ok, kept_field=kept_field, per_axis=per_axis,
                ndangling=sum(1 for s in comp for ax in range(3)
                              if nbr(s, ax, 1, Ls) not in cs and nbr(s, ax, -1, Ls) not in cs))


def majorana_matrix(G, u_all, k=None):
    n = G["n"]
    N = n + len(G["live"])
    A = np.zeros((N, N), dtype=complex)
    for (j, kk, ax, off), ub in zip(G["bonds"], u_all):
        t = -2 * ub * (np.exp(1j * np.dot(k, off)) if k is not None else 1.0)
        A[j, kk] += t
        A[kk, j] -= np.conj(t)
    for pos, (j, ax) in enumerate(G["live"]):
        h = G["dfield"][(j, ax)]
        A[n + pos, j] += 2 * h
        A[j, n + pos] -= 2 * h
    return A


def u_from_non(G, u_non):
    uu = {b: 1 for b in G["tree"]}
    uu.update({b: v for b, v in zip(G["non"], u_non)})
    return [uu[b] for b in G["bonds"]]


def bloch(G, u_non, k):
    return np.linalg.eigvalsh(1j * majorana_matrix(G, u_from_non(G, u_non), np.array(k, dtype=float)))



def S_diag(G):
    par = [sum(G["comp"][j]) % 2 for j in range(G["n"])]
    return np.array([(-1) ** p for p in par] + [-(-1) ** par[j] for (j, ax) in G["live"]], dtype=float)


def kitaev_pattern(G, u_all):
    """Majorana image of s^a_i s^b_m s^c_k over every site m and pair of its bonds (a, c the bond axes, b the third)."""
    inc = {}
    for (j, k, ax, off), ub in zip(G["bonds"], u_all):
        inc.setdefault(j, []).append((k, ax, np.array(off), ub))
        inc.setdefault(k, []).append((j, ax, -np.array(off), -ub))
    out = []
    for m, lst in inc.items():
        for (i, a, off_mi, u_mi), (k, c, off_mk, u_mk) in itertools.combinations(lst, 2):
            if a == c:
                continue
            b = 3 - a - c
            cyc = 1 if (a, b, c) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1
            out.append((i, k, cyc * (-u_mi) * u_mk, off_mk - off_mi))     # = -i cyc u_im u_mk c_i c_k
    return out


def H_bloch(G, u_all, k, kappa=0.0):
    A = majorana_matrix(G, u_all, k)
    if kappa:
        for (i, kk, coef, off) in kitaev_pattern(G, u_all):
            t = -2 * kappa * coef * np.exp(1j * np.dot(k, off))
            A[i, kk] += t
            A[kk, i] -= np.conj(t)
    return 1j * A


def chern(G, u_all, plane, kfix, N=20, kappa=0.0):
    a1, a2 = [a for a in range(3) if a != plane]
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    vec, top = {}, -9.0
    for i1, k1 in enumerate(ks):
        for i2, k2 in enumerate(ks):
            k = np.zeros(3)
            k[a1], k[a2], k[plane] = k1, k2, kfix
            w, v = np.linalg.eigh(H_bloch(G, u_all, k, kappa))
            neg = w < -1e-7
            vec[(i1, i2)] = v[:, neg]
            top = max(top, w[neg].max())
    nb = {x.shape[1] for x in vec.values()}
    if len(nb) != 1:
        return None, top
    tot = 0.0
    for i1 in range(N):
        for i2 in range(N):
            p = [vec[(i1, i2)], vec[((i1 + 1) % N, i2)], vec[((i1 + 1) % N, (i2 + 1) % N)], vec[(i1, (i2 + 1) % N)]]
            tot += np.angle(np.prod([np.linalg.det(p[j].conj().T @ p[(j + 1) % 4]) for j in range(4)]))
    return tot / (2 * np.pi), top


def lowest_sector(G):
    ks = [np.array(kk) * 2 * np.pi / 4 for kk in itertools.product(range(4), repeat=3)]
    best = None
    for u in itertools.product((1, -1), repeat=len(G["non"])):
        E = sum(-0.5 * ev[ev > 0].sum() for ev in (bloch(G, u, kk) for kk in ks)) / len(ks)
        if best is None or E < best[0]:
            best = (E, u)
    return u_from_non(G, best[1])


def lowest_k(G, kappa):
    ks = [np.array(kk) * 2 * np.pi / 4 for kk in itertools.product(range(4), repeat=3)]
    best = None
    for u in itertools.product((1, -1), repeat=len(G["non"])):
        E = sum(-0.5 * ev[ev > 0].sum() for ev in (np.linalg.eigvalsh(H_bloch(G, u_from_non(G, u), kk, kappa)) for kk in ks)) / len(ks)
        if best is None or E < best[0] - 1e-12:
            best = (E, u)
    return u_from_non(G, best[1])


def refined_gap(G, u, kappa, g=10, nseed=8):
    f = lambda k: np.min(np.abs(np.linalg.eigvalsh(H_bloch(G, u, np.array(k), kappa))))
    seeds = sorted((f(np.array(kk) * 2 * np.pi / g), kk) for kk in itertools.product(range(g), repeat=3))[:nseed]
    return min(minimize(f, np.array(kk) * 2 * np.pi / g, method="Nelder-Mead",
                        options={"xatol": 1e-8, "fatol": 1e-12, "maxiter": 3000}).fun for _, kk in seeds)



rng = np.random.default_rng(20260924)
NETS = {"20-site": build(N20), "16-site": build(N16)}

# ------------------------------------------------ 1. sublattice symmetry
viol, nsec = 0.0, 0
for name, G in NETS.items():
    S = np.diag(S_diag(G))
    for u in itertools.product((1, -1), repeat=len(G["non"])):
        nsec += 1
        G2 = dict(G, dfield={key_: rng.normal() for key_ in G["dfield"]})
        for _ in range(3):
            k = rng.uniform(0, 2 * np.pi, 3)
            H = H_bloch(G2, u_from_non(G2, u), k)
            viol = max(viol, np.linalg.norm(S @ H @ S + H))
check("sublattice symmetry: every bond and every dangling-axis field joins opposite classes, so S H(k) S = -H(k)",
      viol < 1e-12 and nsec == 24,
      f"both networks, all {nsec} gauge sectors, random record fields, random momenta: largest |S H S + H| {viol:.0e}")

# ------------------------------------------------ 2. every weak Chern number vanishes
LOW = {name: lowest_sector(G) for name, G in NETS.items()}
cherns, tops, flats = [], {}, {}
for name, G in NETS.items():
    tops[name] = -9.0
    for plane in range(3):
        for kf in (0.0, np.pi):
            c, top = chern(G, LOW[name], plane, kf)
            cherns.append(c)
            tops[name] = max(tops[name], top)
    flats[name] = min(int(np.sum(np.abs(np.linalg.eigvalsh(H_bloch(G, LOW[name], np.array(kk) * 2 * np.pi / 4))) < 1e-9))
                      for kk in itertools.product(range(4), repeat=3))
check("so every weak Chern number of the lowest sector's negative bands vanishes",
      all(c is not None and abs(c) < 1e-6 for c in cherns) and max(tops.values()) < -0.1,
      f"planes k_a = 0, pi for each axis, both networks: largest |Chern number| {max(abs(c) for c in cherns):.0e}; "
      f"top of the negative bands {tops['20-site']:.3f} (20-site), {tops['16-site']:.3f} (16-site); "
      f"flat zero bands per cell {flats['20-site']} and {flats['16-site']}")

# ------------------------------------------------ 3. the leaf exception
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]])
PZ = np.diag([1.0 + 0j, -1.0])
I2 = np.eye(2)
worst_leaf, sviol = 0.0, 0.0
for _ in range(20):
    h = rng.normal(size=(2, 3))
    Hs = np.kron(PZ, PZ) + sum(np.kron(*[(h[0][a] * P) if s == 0 else I2 for s in range(2)]) +
                               np.kron(*[I2 if s == 0 else (h[1][a] * P) for s in range(2)])
                               for a, P in enumerate((PX, PY, PZ)))
    spin = np.sort(np.linalg.eigvalsh(Hs))
    # Majoranas [c1, c2, bx1, by1, bx2, by2]; the z bond carries u = +1
    A = np.zeros((6, 6))
    A[0, 1] = -2.0
    for j, (c, bx, by) in enumerate(((0, 2, 3), (1, 4, 5))):
        A[bx, c] += 2 * h[j][0]
        A[by, c] += 2 * h[j][1]
        A[bx, by] += -2 * h[j][2]                       # sigma^z_j = -i b^x_j b^y_j on the physical space
    A = A - A.T
    eps = np.sort(np.linalg.eigvalsh(1j * A))[3:]
    levels = {0: [], 1: []}
    for occ in itertools.product((0, 1), repeat=3):
        levels[sum(occ) % 2].append(-0.5 * eps.sum() + np.dot(occ, eps))
    worst_leaf = max(worst_leaf, min(np.max(np.abs(np.sort(levels[p]) - spin)) for p in (0, 1)))
    Sl = np.diag([1.0, -1.0, -1.0, -1.0, 1.0, 1.0])
    sviol = max(sviol, np.linalg.norm(Sl @ (1j * A) @ Sl + 1j * A))
check("outside the content rule, a leaf's kept-axis field stays free-Majorana solvable and breaks the sublattice symmetry",
      worst_leaf < 1e-12 and sviol > 0.1,
      f"two-site leaf pair, 20 random field sets: spin spectrum = one parity sector of the Majorana spectrum to {worst_leaf:.0e}; "
      f"|S H S + H| up to {sviol:.2f}")

# ------------------------------------------------ 4. gapped networks stay non-chiral under time-reversal-odd terms
def gap_above_flat(G, u, kappa):
    """Number of exact zero modes per cell, and the refined smallest |E| of the remaining bands."""
    grid = [np.array(kk) * 2 * np.pi / 6 for kk in itertools.product(range(6), repeat=3)]
    nz = min(int(np.sum(np.abs(np.linalg.eigvalsh(H_bloch(G, u, k, kappa))) < 1e-9)) for k in grid)
    f = lambda k: np.sort(np.abs(np.linalg.eigvalsh(H_bloch(G, u, np.array(k), kappa))))[nz]
    seeds = sorted((f(k), tuple(k)) for k in grid)[:6]
    return nz, min(minimize(f, np.array(k0), method="Nelder-Mead", options={"xatol": 1e-8, "fatol": 1e-12,
                                                                                 "maxiter": 3000}).fun for _, k0 in seeds)


rows, ok4 = [], True
for name, G in NETS.items():
    S = np.diag(S_diag(G))
    for kappa in (0.05, 0.2, 1.0, 4.0):
        sv = max(np.linalg.norm(S @ H_bloch(G, LOW[name], k, kappa) @ S + H_bloch(G, LOW[name], k, kappa))
                 for k in [rng.uniform(0, 2 * np.pi, 3) for _ in range(3)])
        nz, gmin = gap_above_flat(G, LOW[name], kappa)
        cs = [chern(G, LOW[name], p, 0.0, N=16, kappa=kappa)[0] for p in range(3)]
        ok4 &= sv > 0.1 and gmin > 0.01 and nz == 2 and all(c is not None and abs(c) < 1e-6 for c in cs)
        rows.append(f"{name} kappa {kappa}: gap {gmin:.4f}")
check("Kitaev's pattern breaks S, yet with two flat zero bands per cell kept, the gap stays open and every weak Chern number stays 0",
      ok4, "; ".join(rows) + "; two exact zero bands per cell at every kappa; Chern numbers 0 on the three k = 0 planes throughout")

# ------------------------------------------------ 5. a gapless start plus Kitaev's pattern gives a Chern number
G20z = dict(NETS["20-site"], live=[], dfield={})          # the 20-site network with its dangling Majoranas decoupled
cs20 = set(N20)
three_axis = sum(1 for r in itertools.product(range(4), repeat=3) if r not in cs20 and
                 len({ax for ax in range(3) for d in (1, -1) if nbr(r, ax, d) in cs20}) == 3)


gap0 = refined_gap(G20z, lowest_k(G20z, 0.0), 0.0)
u3 = lowest_k(G20z, 0.3)
gap3 = refined_gap(G20z, u3, 0.3)
c5 = {(p, kf): chern(G20z, u3, p, kf, N=32, kappa=0.3)[0] for p in range(3) for kf in (0.4, 1.9, 3.5)}
weak = [sorted({round(abs(c5[(p, kf)]), 6) * np.sign(round(c5[(p, kf)], 6)) + 0.0 for kf in (0.4, 1.9, 3.5)}) for p in range(3)]
check("a gapless start plus Kitaev's pattern gives a Chern number: the 20-site network with decoupled dangling Majoranas",
      gap0 < 1e-9 and gap3 > 0.04 and weak == [[1.0], [0.0], [0.0]] and three_axis == 7,
      f"gap at kappa 0 {gap0:.0e}; at kappa 0.3 {gap3:.4f}; weak Chern numbers on planes normal to x, y, z "
      f"{[int(round(float(w[0]))) for w in weak]} (three planes each); "
      f"but {three_axis} of its records touch unrecorded sites along all three axes, so zero dangling fields are not realizable there")

# ------------------------------------------------ 6. where zero dangling fields are realizable
def search_zero_field(Ls, maxsol):
    """Relaxed carvings in which no record touches unrecorded sites along all three axes, so every record can avoid them."""
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx_s = {s: i + 1 for i, s in enumerate(sites)}
    cls, top = [], len(sites)
    for s in sites:
        u = idx_s[s]
        for ax in range(3):
            cls.append([-u, -idx_s[nbr(s, ax, 1, Ls)], -idx_s[nbr(s, ax, -1, Ls)]])
        for sx, sy, sz in itertools.product((1, -1), repeat=3):
            cls.append([u, -idx_s[nbr(s, 0, sx, Ls)], -idx_s[nbr(s, 1, sy, Ls)], -idx_s[nbr(s, 2, sz, Ls)]])
        enc = CardEnc.atleast(lits=[idx_s[nbr(s, ax, d, Ls)] for ax in range(3) for d in (1, -1)], bound=2,
                              top_id=top, encoding=EncType.seqcounter)
        top = max(top, enc.nv)
        for c in enc.clauses:
            cls.append([-u] + c)
    cls.append([idx_s[(0, 0, 0)]])
    g = Glucose4(bootstrap_with=cls)
    out = []
    while len(out) < maxsol and g.solve():
        m = g.get_model()
        U = frozenset(s for s in sites if m[idx_s[s] - 1] > 0)
        out.append(U)
        g.add_clause([-idx_s[s] if s in U else idx_s[s] for s in sites])
    g.delete()
    return out


def comps(U):
    Uset, seen, out = set(U), set(), []
    for s in sorted(U):
        if s in seen:
            continue
        comp, stack = {s}, [s]
        while stack:
            v = stack.pop()
            for ax in range(3):
                for d in (1, -1):
                    w = nbr(v, ax, d)
                    if w in Uset and w not in comp:
                        comp.add(w)
                        stack.append(w)
        seen |= comp
        out.append(frozenset(comp))
    return out


zf = set()
for U in search_zero_field(L3, 3000):
    for c in comps(U):
        if len(c) >= 8 and winding_rank(c)[1] == 3:
            zf.add(c)
zstats = []
for c in sorted(zf, key=lambda x: (len(x), sorted(x))):
    Gz = dict(build(c), live=[], dfield={})
    ok_zero = all(len({ax for ax in range(3) for d in (1, -1) if nbr(r, ax, d) in c}) <= 2
                  for r in itertools.product(range(4), repeat=3) if r not in c)
    u = lowest_k(Gz, 0.0)
    ev = np.array([np.sort(np.abs(np.linalg.eigvalsh(H_bloch(Gz, u, np.array(kk) * 2 * np.pi / 8))))
                   for kk in itertools.product(range(8), repeat=3)])
    nflat = int(np.sum(ev.max(axis=0) < 1e-8))
    zstats.append((len(c), ok_zero, float(ev[:, nflat:].min())))
ngapless = sum(1 for z in zstats if z[2] < 1e-6)
check("zero dangling fields are realizable on other three-direction networks, and half of them are gapless",
      len(zf) >= 10 and all(z[1] for z in zstats) and ngapless >= 4,
      f"{len(zf)} distinct networks in 3000 solutions on 4x4x4, every record touching at most two axes; "
      f"{ngapless} have gapless dispersive Majorana bands on an 8^3 grid, sizes {sorted({z[0] for z in zstats if z[2] < 1e-6})}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
