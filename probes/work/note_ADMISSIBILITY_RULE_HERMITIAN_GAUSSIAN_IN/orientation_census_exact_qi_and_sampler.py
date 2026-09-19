#!/usr/bin/env python3
"""Probe: ADMISSIBILITY_RULE_HERMITIAN_GAUSSIAN_INSTANCE_FORMATION_PRECISION_LDL_BOUNDED_THEOREM_NOTE_2026-09-07.

Machinery disjoint from the runner (sympy on declared orders): a self-written
exact Gaussian-rational class (pairs of Fractions), own elimination; the
formation law built literally as the sequential product of the rule's
conditionals; recorded-set classes enumerated as acyclic orientations of the
window graph (each order induces one: every edge points from the earlier to
the later site, A_k = in-neighbours); a Monte Carlo sampler of the formation
law itself.

 K1  G1/G2 on ALL 720 orders of 2x3 (runner: two orders + the monotone class,
     snake, mirror): the sequential quadratic form equals L^H D L, det = prod P_kk,
     P_sigma constant on recorded-set classes; class counts = acyclic
     orientations (plaquette 14, as the note states).
 K2  G3 on every acyclic orientation of 1x3, 2x2, 2x3, 1x6, 2x4, 3x3 (exact
     L^H D L) and 3x4 (exact sparse formula), both declared instances:
     P_sigma = P + diag(c) + F, never P; support kept iff every |A_k| <= 1
     (the forward half proved; the converse the note's executed statement on
     the declared grid instances), fill-in only on distance-two pairs.
 K3  the literal numbers: path corrections [5/48, 5/48, 0]; 2x3 monotone
     corrections [5/24, 5/24, 5/48, 5/48, 5/48, 0] and fill-in pairs
     ((0,1),(1,0)), ((0,2),(1,1)); row-1 diagonal 149/48, 149/48, 3; the three
     C6 witnesses; the C7 one-edge example; E3's herm(Q^-1) != (herm Q)^-1.
 K4  G4 (Hadamard) on every window above; G5 three read-slice covariances on
     2x3 (and, beyond, 2x4 and 3x3 with the last row read).
 K5  sampler: 2,000,000 sequential draws from the rule along the monotone
     order of 2x3; empirical covariance against P_sigma^-1 and P^-1.

Prints SUMMARY: lines; HIT: only when a falsifier of the note fires.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


# ---------------------------------------------------------------------------
# exact Gaussian rationals
# ---------------------------------------------------------------------------
class G:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = Fr(r)
        self.i = Fr(i)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.r + o.r, s.i + o.i)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.r - o.r, s.i - o.i)

    def __rsub__(s, o):
        return G(o) - s

    def __neg__(s):
        return G(-s.r, -s.i)

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__

    def conj(s):
        return G(s.r, -s.i)

    def abs2(s):
        return s.r * s.r + s.i * s.i

    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        d = o.abs2()
        n = s * o.conj()
        return G(n.r / d, n.i / d)

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.r == o.r and s.i == o.i

    def __hash__(s):
        return hash((s.r, s.i))

    def iszero(s):
        return s.r == 0 and s.i == 0

    def __repr__(s):
        if s.i == 0:
            return str(s.r)
        return f"({s.r}{'+' if s.i >= 0 else '-'}{abs(s.i)}i)"


ZERO = G(0)


def mat_zero(n):
    return [[G(0) for _ in range(n)] for _ in range(n)]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def det_and_inv(A):
    n = len(A)
    M = [[A[i][j] for j in range(n)] + [G(1) if i == j else G(0) for j in range(n)] for i in range(n)]
    det = G(1)
    for c in range(n):
        p = next(r for r in range(c, n) if not M[r][c].iszero())
        if p != c:
            M[c], M[p] = M[p], M[c]
            det = -det
        piv = M[c][c]
        det = det * piv
        M[c] = [v / piv for v in M[c]]
        for r in range(n):
            if r != c and not M[r][c].iszero():
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return det, [row[n:] for row in M]


# ---------------------------------------------------------------------------
# windows and instances
# ---------------------------------------------------------------------------
def window(rows, cols):
    sites = [(i, j) for i in range(rows) for j in range(cols)]
    edges = []
    for (i, j) in sites:
        if j + 1 < cols:
            edges.append(((i, j), (i, j + 1), "h"))
        if i + 1 < rows:
            edges.append(((i, j), (i + 1, j), "v"))
    return sites, edges


def precision(sites, edges, inst):
    n = len(sites)
    idx = {s: t for t, s in enumerate(sites)}
    P = mat_zero(n)
    for t in range(n):
        P[t][t] = G(3)
    for a, b, kind in edges:
        if inst == "declared":
            val = G(Fr(1, 4), Fr(2, 4)) if kind == "h" else G(Fr(2, 4), Fr(-1, 4))
        else:
            val = G(Fr(1, 2))
        P[idx[a]][idx[b]] = val            # a left of / above b
        P[idx[b]][idx[a]] = val.conj()
    return P


def nbrs(n, P):
    return [[y for y in range(n) if y != x and not P[x][y].iszero()] for x in range(n)]


def sequential_form(P, order):
    """quadratic form of the product of the rule's conditionals along the order:
    sum_k P_kk |z_k + sum_{y in A_k} (P_ky/P_kk) z_y|^2 as a Hermitian matrix"""
    n = len(P)
    pos = {x: t for t, x in enumerate(order)}
    NB = nbrs(n, P)
    Qf = mat_zero(n)
    for x in order:
        A = [y for y in NB[x] if pos[y] < pos[x]]
        coef = {x: G(1)}
        for y in A:
            coef[y] = P[x][y] / P[x][x]
        for u, cu in coef.items():
            for v, cv in coef.items():
                Qf[u][v] = Qf[u][v] + P[x][x] * cu.conj() * cv
    return Qf


def recorded_sets(P, order):
    n = len(P)
    pos = {x: t for t, x in enumerate(order)}
    NB = nbrs(n, P)
    return tuple(frozenset(y for y in NB[x] if pos[y] < pos[x]) for x in range(n))


def form_from_sets(P, A):
    """P + diag(c) + F from recorded sets (the note's G3 formula)"""
    n = len(P)
    M = [[P[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for x in A[k]:
            M[x][x] = M[x][x] + P[k][x].abs2() / P[k][k].r
        for x in A[k]:
            for y in A[k]:
                if x != y:
                    M[x][y] = M[x][y] + P[x][k] * P[k][y] / P[k][k]
    return M


def acyclic_orientations(n, edge_list):
    """all acyclic orientations as tuples of in-neighbour sets"""
    out = []
    m = len(edge_list)
    for mask in range(1 << m):
        inn = [set() for _ in range(n)]
        for b, (u, v) in enumerate(edge_list):
            if mask >> b & 1:
                inn[v].add(u)
            else:
                inn[u].add(v)
        # acyclicity by Kahn
        indeg = [len(s) for s in inn]
        outs = [[] for _ in range(n)]
        for v in range(n):
            for u in inn[v]:
                outs[u].append(v)
        stack = [v for v in range(n) if indeg[v] == 0]
        seen = 0
        while stack:
            u = stack.pop()
            seen += 1
            for v in outs[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    stack.append(v)
        if seen == n:
            out.append(tuple(frozenset(s) for s in inn))
    return out


# ---------------------------------------------------------------------------
def run_K1():
    print("=" * 78)
    print("K1  all 720 orders of 2x3 (and all orders of the path and plaquette)")
    res = {}
    for (r, c) in ((1, 3), (2, 2), (2, 3)):
        sites, edges = window(r, c)
        n = len(sites)
        for inst in ("declared", "real"):
            P = precision(sites, edges, inst)
            classes = {}
            bad_form = bad_det = bad_class = 0
            prodP = G(1)
            for t in range(n):
                prodP = prodP * P[t][t]
            for order in itertools.permutations(range(n)):
                Qf = sequential_form(P, order)
                A = recorded_sets(P, order)
                M = form_from_sets(P, A)
                if not mat_eq(Qf, M):
                    bad_form += 1
                key = A
                if key in classes:
                    if not mat_eq(classes[key], Qf):
                        bad_class += 1
                else:
                    classes[key] = Qf
                    d, _ = det_and_inv(Qf)
                    if not d == prodP:
                        bad_det += 1
            distinct = len({tuple(tuple((v.r, v.i) for v in row) for row in M) for M in classes.values()})
            res[(r, c, inst)] = (len(classes), distinct, bad_form, bad_det, bad_class)
            print(f"  {r}x{c} {inst:8s}: {sum(1 for _ in itertools.permutations(range(n)))} orders, recorded-set "
                  f"classes {len(classes)}, distinct laws {distinct}; failures: sequential form vs formula {bad_form}, "
                  f"det vs prod P_kk {bad_det}, law not constant on a class {bad_class}")
            if bad_form or bad_det or bad_class:
                hit(f"G1/G2 fails on {r}x{c} {inst}")
    if res[(2, 2, "declared")][0] != 14:
        hit(f"plaquette class count {res[(2, 2, 'declared')][0]} != 14")
    return res


def run_K2():
    print("=" * 78)
    print("K2  G3 on every acyclic orientation (= recorded-set class)")
    out = []
    for (r, c) in ((1, 3), (2, 2), (2, 3), (1, 6), (2, 4), (3, 3), (3, 4)):
        sites, edges = window(r, c)
        n = len(sites)
        idx = {s: t for t, s in enumerate(sites)}
        elist = [(idx[a], idx[b]) for a, b, _ in edges]
        orients = acyclic_orientations(n, elist)
        edge_set = {frozenset(e) for e in elist}
        full = (r * c) <= 9
        for inst in ("declared", "real"):
            P = precision(sites, edges, inst)
            never_P = True
            fwd_bad = conv_bad = off2 = 0
            two_count = 0
            ldl_bad = 0
            for A in orients:
                M = form_from_sets(P, A)
                if full:
                    # a linear extension: topological order of the orientation
                    order = topo(n, A)
                    Qf = sequential_form(P, order)
                    if not mat_eq(Qf, M):
                        ldl_bad += 1
                if mat_eq(M, P):
                    never_P = False
                support_same = all((M[x][y].iszero()) == (P[x][y].iszero()) for x in range(n) for y in range(n) if x != y)
                some_two = any(len(a) >= 2 for a in A)
                two_count += some_two
                if not some_two and not support_same:
                    fwd_bad += 1
                if some_two and support_same:
                    conv_bad += 1
                for x in range(n):
                    for y in range(n):
                        if x != y and P[x][y].iszero() and not M[x][y].iszero():
                            (xi, xj), (yi, yj) = sites[x], sites[y]
                            if abs(xi - yi) + abs(xj - yj) != 2:
                                off2 += 1
            out.append((r, c, inst, len(orients), two_count, never_P, fwd_bad, conv_bad, off2, ldl_bad if full else None))
            print(f"  {r}x{c} {inst:8s}: acyclic orientations {len(orients)} ({two_count} with a site recording two); "
                  f"P_sigma = P for none: {never_P}; support changed with all |A|<=1: {fwd_bad}; support kept with a "
                  f"site recording two: {conv_bad}; fill-in off distance two: {off2}"
                  + (f"; sequential form != formula: {ldl_bad}" if full else " (formula only)"))
            if not never_P or fwd_bad or ldl_bad:
                hit(f"G3 (proved part) fails on {r}x{c} {inst}")
            if conv_bad and (r, c) in ((1, 3), (2, 2), (2, 3)):
                hit(f"declared grid instance {r}x{c} {inst}: support kept although a site records two neighbours")
            if off2:
                hit(f"{r}x{c} {inst}: fill-in at a pair not at distance two on the grid")
    return out


def topo(n, A):
    indeg = [len(a) for a in A]
    outs = [[] for _ in range(n)]
    for v in range(n):
        for u in A[v]:
            outs[u].append(v)
    stack = sorted([v for v in range(n) if indeg[v] == 0], reverse=True)
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in outs[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    return order


def run_K3():
    print("=" * 78)
    print("K3  literal numbers of the note")
    ok = True
    # path end-to-end
    sites, edges = window(1, 3)
    P = precision(sites, edges, "declared")
    A = recorded_sets(P, (0, 1, 2))
    M = form_from_sets(P, A)
    corr = [M[t][t] - P[t][t] for t in range(3)]
    print(f"  path end-to-end corrections {corr} (note [5/48, 5/48, 0])")
    ok &= corr == [G(Fr(5, 48)), G(Fr(5, 48)), G(0)]
    A2 = recorded_sets(P, (0, 2, 1))
    M2 = form_from_sets(P, A2)
    print(f"  path endpoints-first: fill-in at the end pair {M2[0][2]} (nonzero)")
    ok &= not M2[0][2].iszero()
    # 2x3 monotone class
    sites, edges = window(2, 3)
    P = precision(sites, edges, "declared")
    mono = (0, 1, 2, 3, 4, 5)       # row-major (0,0),(0,1),(0,2),(1,0),(1,1),(1,2)
    A = recorded_sets(P, mono)
    M = form_from_sets(P, A)
    corr = [M[t][t] - P[t][t] for t in range(6)]
    fill = sorted((sites[x], sites[y]) for x in range(6) for y in range(6)
                  if x < y and P[x][y].iszero() and not M[x][y].iszero())
    print(f"  2x3 monotone corrections {corr}; fill-in pairs {fill}")
    ok &= corr == [G(Fr(5, 24)), G(Fr(5, 24)), G(Fr(5, 48)), G(Fr(5, 48)), G(Fr(5, 48)), G(0)]
    ok &= fill == [((0, 1), (1, 0)), ((0, 2), (1, 1))]
    diag1 = [M[t][t] for t in (3, 4, 5)]
    print(f"  formation row-1 diagonal {diag1} (note 149/48, 149/48, 3)")
    ok &= diag1 == [G(Fr(149, 48)), G(Fr(149, 48)), G(3)]
    # the other monotone orders give the same law; snake and mirror differ
    monos = [o for o in itertools.permutations(range(6))
             if all(recorded_sets(P, o)[x] == A[x] for x in range(6))]
    snake = (0, 1, 2, 5, 4, 3)
    mirror = (2, 1, 0, 5, 4, 3)
    Ms = form_from_sets(P, recorded_sets(P, snake))
    Mm = form_from_sets(P, recorded_sets(P, mirror))
    print(f"  orders with the monotone recorded sets: {len(monos)} (note 5); snake equal: {mat_eq(Ms, M)}, mirror equal: "
          f"{mat_eq(Mm, M)}")
    ok &= len(monos) == 5 and not mat_eq(Ms, M) and not mat_eq(Mm, M)
    # C6 witnesses
    # plaquette a=(0,0),b=(0,1),c=(1,0),d=(1,1): 1/2 everywhere except P_cd = -1/2, order (a,d,b,c)
    sites, edges = window(2, 2)
    Pw = precision(sites, edges, "real")
    Pw[2][3] = G(Fr(-1, 2))
    Pw[3][2] = G(Fr(-1, 2))
    Aw = recorded_sets(Pw, (0, 3, 1, 2))
    Mw = form_from_sets(Pw, Aw)
    two = sum(1 for a in Aw if len(a) >= 2)
    kept = all(Mw[x][y].iszero() == Pw[x][y].iszero() for x in range(4) for y in range(4) if x != y)
    print(f"  C6 plaquette witness: sites recording two = {two}, support kept = {kept}, fill (a,d) = {Mw[0][3]}")
    ok &= two == 2 and kept
    # triangle K3, 1/2 on every edge: last site records the other two -> fill-in on an edge
    T = [[G(3), G(Fr(1, 2)), G(Fr(1, 2))], [G(Fr(1, 2)), G(3), G(Fr(1, 2))], [G(Fr(1, 2)), G(Fr(1, 2)), G(3)]]
    MT = form_from_sets(T, recorded_sets(T, (0, 1, 2)))
    print(f"  C6 K3 witness: P_sigma(0,1) = {MT[0][1]} vs P(0,1) = {T[0][1]} (fill-in on an edge)")
    ok &= not (MT[0][1] == T[0][1])
    T2 = [[G(3), G(Fr(1, 4)), G(Fr(1, 2))], [G(Fr(1, 4)), G(3), G(Fr(-3, 2))], [G(Fr(1, 2)), G(Fr(-3, 2)), G(3)]]
    MT2 = form_from_sets(T2, recorded_sets(T2, (0, 1, 2)))
    print(f"  C6 lost-entry witness: P_sigma(0,1) = {MT2[0][1]} (P(0,1) = 1/4)")
    ok &= MT2[0][1].iszero()
    # C7 one-edge example
    E = [[G(2), G(-1)], [G(-1), G(2)]]
    ME = form_from_sets(E, recorded_sets(E, (0, 1)))
    _, cov_s = det_and_inv(E)
    _, cov_f = det_and_inv(ME)
    print(f"  C7: P_sigma = {ME}; static cov {cov_s}; records-only cov {cov_f}")
    ok &= mat_eq(ME, [[G(Fr(5, 2)), G(-1)], [G(-1), G(2)]])
    ok &= mat_eq(cov_s, [[G(Fr(2, 3)), G(Fr(1, 3))], [G(Fr(1, 3)), G(Fr(2, 3))]])
    ok &= mat_eq(cov_f, [[G(Fr(1, 2)), G(Fr(1, 4))], [G(Fr(1, 4)), G(Fr(5, 8))]])
    # E3
    Qm = [[G(1), G(1)], [G(-1), G(1)]]
    _, Qi = det_and_inv(Qm)
    hermQi = [[(Qi[i][j] + Qi[j][i].conj()) / 2 for j in range(2)] for i in range(2)]
    hermQ = [[(Qm[i][j] + Qm[j][i].conj()) / 2 for j in range(2)] for i in range(2)]
    _, inv_hermQ = det_and_inv(hermQ)
    print(f"  E3: herm(Q^-1) = {hermQi}, (herm Q)^-1 = {inv_hermQ}")
    ok &= not mat_eq(hermQi, inv_hermQ)
    if not ok:
        hit("a literal number of the note differs")
    return ok, corr, fill, diag1


def read_slice_covs(r, c, inst):
    sites, edges = window(r, c)
    n = len(sites)
    P = precision(sites, edges, inst)
    A = recorded_sets(P, tuple(range(n)))       # row-major = monotone
    M = form_from_sets(P, A)
    last = [t for t, s in enumerate(sites) if s[0] == r - 1]
    _, Pinv = det_and_inv(P)
    _, Minv = det_and_inv(M)
    static = [[Pinv[a][b] for b in last] for a in last]
    formation = [[Minv[a][b] for b in last] for a in last]
    blk = [[P[a][b] for b in last] for a in last]
    _, pinned = det_and_inv(blk)
    return static, pinned, formation, P, M


def run_K4():
    print("=" * 78)
    print("K4  Hadamard (G4) and the read-slice covariances (G5)")
    had = []
    for (r, c) in ((1, 3), (2, 2), (2, 3), (1, 6), (2, 4), (3, 3)):
        sites, edges = window(r, c)
        for inst in ("declared", "real"):
            P = precision(sites, edges, inst)
            d, _ = det_and_inv(P)
            prod = Fr(1)
            for t in range(len(P)):
                prod *= P[t][t].r
            had.append((r, c, inst, d, prod))
            if not (d.i == 0 and 0 < d.r < prod):
                hit(f"Hadamard fails on {r}x{c} {inst}: det P = {d}")
    ratio = max(float(d.r / p) for _, _, _, d, p in had)
    print(f"  det P / prod P_kk on 12 (window, instance) cases: max {ratio:.6f} (< 1), all real positive")
    rows = []
    for (r, c) in ((2, 3), (2, 4), (3, 3)):
        for inst in ("declared", "real"):
            s, p, f, P, M = read_slice_covs(r, c, inst)
            eq_sp, eq_sf, eq_pf = mat_eq(s, p), mat_eq(s, f), mat_eq(p, f)
            rows.append((r, c, inst, eq_sp, eq_sf, eq_pf))
            print(f"  {r}x{c} {inst:8s} last-row read slice: static==pinned {eq_sp}, static==formation {eq_sf}, "
                  f"pinned==formation {eq_pf}; formation diag {[str(f[t][t]) for t in range(len(f))]}")
            if (r, c) == (2, 3) and (eq_sp or eq_sf or eq_pf):
                hit(f"2x3 {inst}: two read-slice covariances coincide")
    return ratio, rows


def run_K5(N=2_000_000, seed=20260919):
    print("=" * 78)
    print("K5  sampler of the formation law (monotone order of 2x3, declared instance)")
    sites, edges = window(2, 3)
    n = len(sites)
    P = precision(sites, edges, "declared")
    Pc = np.array([[complex(float(v.r), float(v.i)) for v in row] for row in P])
    A = recorded_sets(P, tuple(range(n)))
    rng = np.random.default_rng(seed)
    Z = np.zeros((N, n), dtype=complex)
    for k in range(n):
        mean = np.zeros(N, dtype=complex)
        for y in A[k]:
            mean -= (Pc[k, y] / Pc[k, k]) * Z[:, y]
        sd = np.sqrt(1.0 / (2 * Pc[k, k].real))
        Z[:, k] = mean + sd * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
    emp = (Z.T @ Z.conj()) / N              # E[z z^H]
    M = form_from_sets(P, A)
    Mc = np.array([[complex(float(v.r), float(v.i)) for v in row] for row in M])
    cov_f = np.linalg.inv(Mc)
    cov_s = np.linalg.inv(Pc)
    df = np.max(np.abs(emp - cov_f))
    ds = np.max(np.abs(emp - cov_s))
    gap = np.max(np.abs(cov_f - cov_s))
    se = np.max(np.abs(cov_f)) / np.sqrt(N)
    print(f"  N={N}: max |emp - P_sigma^-1| = {df:.2e}; max |emp - P^-1| = {ds:.2e}; max |P_sigma^-1 - P^-1| = "
          f"{gap:.2e}; statistical scale ~ {se:.1e}")
    if df > 10 * se * 3 or ds < df:
        hit(f"sampled formation law does not match the Gaussian with precision P_sigma (dev {df:.2e} vs static {ds:.2e})")
    return df, ds, gap, se


def main():
    t0 = time.time()
    k1 = run_K1()
    summary("K1 all orders, exact Q(i): " + "; ".join(
        f"{r}x{c} {inst}: classes {cl}, distinct laws {dl}, failures {bf + bd + bc}"
        for (r, c, inst), (cl, dl, bf, bd, bc) in k1.items()))
    k2 = run_K2()
    summary("K2 acyclic-orientation census (G3): " + "; ".join(
        f"{r}x{c} {inst}: {no} classes ({tw} with a site recording two), never P {nP}, support-kept-with-two {cb}, "
        f"fill-off-distance-2 {o2}" for r, c, inst, no, tw, nP, fb, cb, o2, lb in k2))
    ok, corr, fill, diag1 = run_K3()
    summary(f"K3 literals: path [5/48,5/48,0], 2x3 corrections {corr}, fill-in {fill}, row-1 diagonal {diag1}, "
            f"5 monotone orders one law, snake/mirror differ, C6 witnesses and C7/E3 reproduce: {ok}")
    ratio, rows = run_K4()
    summary(f"K4 Hadamard det P/prod P_kk max {ratio:.6f} on 12 cases; read slices pairwise different: " + "; ".join(
        f"{r}x{c} {inst}: {not (a or b or c2)}" for r, c, inst, a, b, c2 in rows))
    df, ds, gap, se = run_K5()
    summary(f"K5 sampler 2e6 draws: |emp - P_sigma^-1| {df:.1e}, |emp - P^-1| {ds:.1e} (gap {gap:.1e}, scale {se:.0e})")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
