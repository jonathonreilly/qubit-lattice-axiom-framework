#!/usr/bin/env python3
"""Readability of a covariant nearest-neighbour rule from finished-window
records on the continuum Bloch alphabet: exact Fisher rank at the uniform
base point, finite-alphabet controls, and the order of the formation order.

Objects (all exact, Fractions only):
  * windows 2x3 (6 sites, 7 edges) and 2x2x2 (8 sites, 12 edges) of Z^3;
  * letters = unit Bloch vectors v_x in S^2 (continuum alphabet), with the
    binary {+-e_z} and six-axis {+-e_i} alphabets as controls;
  * covariant polynomial rule families in the invariants v_x.v_y (unsoldered
    SO(3)), (v_x.e)(v_y.e) with e the edge direction (soldered), and the
    cubic site term sum_i v_i^4 - 3/5 (soldered);
  * finished-window law mu_theta(v) = W_theta(v)/Z(theta) with
    W_theta = prod_edges (1 + sum_{a=1}^5 theta_a f_a) prod_sites (1 + theta_H H),
    and formation-order laws mu_sigma built from conditional rules
    r_theta(p | recorded neighbours) composed along a total order sigma;
  * Fisher information at theta = 0 equals the covariance, under the product
    uniform measure, of the tangent functions T_a = d W/d theta_a |_0;
    E[monomial] is the product over sites of the normalised sphere moment
    E[x^a y^b z^c] = (a-1)!!(b-1)!!(c-1)!!/(a+b+c+1)!! (all even), else 0.
Prints TOTAL: PASS=N FAIL=0 on success; stdout stays under 6000 characters.
"""
from fractions import Fraction as Fr
from itertools import permutations, combinations
import sys
import time

AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_READABILITY_CONTINUUM_ALPHABET_FISHER_RANK_AND_FORMATION_ORDER_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md', 'docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md', 'docs/A_READABLE_MATTER_LAW_EXISTS_ON_THE_5X5X5_WINDOW_THE_DESIGNED_LAWS_RECORD_TABLE_COMPLETED_BY_A_COVARIANT_PARITY_RULE_HAS_EVERY_MENU_NONEMPTY_IS_READ_FROM_PARTIAL_BLOCKS_AND_KEEPS_THE_FERMION_BOUNDED_NOTE_2026-09-04.md')

T0 = time.time()
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f" | {detail}" if detail else ""))


# ----------------------------------------------------------------- windows
def make_window(shape):
    sites = [(i, j, k) for i in range(shape[0]) for j in range(shape[1])
             for k in range(shape[2])]
    idx = {s: n for n, s in enumerate(sites)}
    edges = []  # (x, y, direction)
    for s in sites:
        for d in range(3):
            t = list(s)
            t[d] += 1
            t = tuple(t)
            if t in idx:
                edges.append((idx[s], idx[t], d))
    nbrs = {n: [] for n in range(len(sites))}
    for x, y, _ in edges:
        nbrs[x].append(y)
        nbrs[y].append(x)
    return {"name": "x".join(str(k) for k in shape if k > 1),
        "shape": tuple(shape), "sites": sites, "idx": idx,
            "edges": edges, "nbrs": nbrs, "n": len(sites)}


# ------------------------------------------------- polynomials (monomial dicts)
def padd(p, q):
    r = dict(p)
    for m, c in q.items():
        v = r.get(m, 0) + c
        if v:
            r[m] = v
        elif m in r:
            del r[m]
    return r


def pscale(p, c):
    return {m: c * v for m, v in p.items()} if c else {}


def pmul(p, q):
    r = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            v = r.get(m, 0) + c1 * c2
            if v:
                r[m] = v
            elif m in r:
                del r[m]
    return r


def pconst(c, nv):
    return {(0,) * nv: Fr(c)} if c else {}


def pvar(site, coord, nv):
    m = [0] * nv
    m[3 * site + coord] = 1
    return {tuple(m): Fr(1)}


def pdot(x, y, nv):
    r = {}
    for i in range(3):
        r = padd(r, pmul(pvar(x, i, nv), pvar(y, i, nv)))
    return r


def legendre(d, t, nv):
    """P_d(t) for a polynomial t, by the three-term recursion."""
    p0, p1 = pconst(1, nv), t
    if d == 0:
        return p0
    for k in range(1, d):
        p2 = padd(pscale(pmul(t, p1), Fr(2 * k + 1, k + 1)),
                  pscale(p0, Fr(-k, k + 1)))
        p0, p1 = p1, p2
    return p1


def pequal(p, q):
    return {m: c for m, c in p.items() if c} == {m: c for m, c in q.items() if c}


# --------------------------------------------------------------- moments
def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


def moment_sphere(a, b, c):
    if a % 2 or b % 2 or c % 2:
        return Fr(0)
    return Fr(dfact(a - 1) * dfact(b - 1) * dfact(c - 1), dfact(a + b + c + 1))


def moment_binary_z(a, b, c):
    if a or b:
        return Fr(0)
    return Fr(1) if c % 2 == 0 else Fr(0)


def moment_six_axis(a, b, c):
    pos = [e for e in (a, b, c) if e > 0]
    if not pos:
        return Fr(1)
    if len(pos) > 1:
        return Fr(0)
    return Fr(1, 3) if pos[0] % 2 == 0 else Fr(0)


ALPHABETS = {"continuum": moment_sphere, "binary_z": moment_binary_z,
             "six_axis": moment_six_axis}


def expect(p, n, moment):
    tot = Fr(0)
    for m, c in p.items():
        val = c
        for s in range(n):
            val *= moment(m[3 * s], m[3 * s + 1], m[3 * s + 2])
            if not val:
                break
        tot += val
    return tot


# --------------------------------------------------- exact linear algebra
def rank_and_nullspace(M):
    """Row-reduce a rational matrix; return (rank, list of null vectors)."""
    rows = [list(r) for r in M]
    nrow, ncol = len(rows), len(rows[0])
    pivots = []
    r = 0
    for c in range(ncol):
        piv = next((i for i in range(r, nrow) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = 1 / rows[r][c]
        rows[r] = [v * inv for v in rows[r]]
        for i in range(nrow):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(ncol) if c not in pivots]
    null = []
    for fc in free:
        v = [Fr(0)] * ncol
        v[fc] = Fr(1)
        for i, pc in enumerate(pivots):
            v[pc] = -rows[i][fc]
        null.append(v)
    return r, null


def matvec(M, v):
    return [sum(a * b for a, b in zip(row, v)) for row in M]


def in_span(v, basis):
    """Is v a rational combination of the basis vectors?"""
    if not basis:
        return all(x == 0 for x in v)
    r0, _ = rank_and_nullspace([list(b) for b in basis])
    r1, _ = rank_and_nullspace([list(b) for b in basis] + [list(v)])
    return r0 == r1


# ------------------------------------------------- tangent functions / Fisher
PARAMS = ["P1", "P2", "P3", "P4", "S1", "H"]


def tangents(win):
    """Base-point tangent functions of the six-parameter covariant family."""
    n, nv = win["n"], 3 * win["n"]
    T = {p: {} for p in PARAMS}
    for x, y, d in win["edges"]:
        t = pdot(x, y, nv)
        for k in (1, 2, 3, 4):
            T[f"P{k}"] = padd(T[f"P{k}"], legendre(k, t, nv))
        T["S1"] = padd(T["S1"], pmul(pvar(x, d, nv), pvar(y, d, nv)))
    for s in range(n):
        h = pconst(Fr(-3, 5), nv)
        for i in range(3):
            v = pvar(s, i, nv)
            h = padd(h, pmul(pmul(v, v), pmul(v, v)))
        T["H"] = padd(T["H"], h)
    return T


def fisher(T, n, moment, names=PARAMS):
    means = {a: expect(T[a], n, moment) for a in names}
    M = []
    for a in names:
        row = []
        for b in names:
            row.append(expect(pmul(T[a], T[b]), n, moment) - means[a] * means[b])
        M.append(row)
    return M


def fmt(v):
    return "/".join(str(v).split("/")) if v.denominator != 1 else str(v.numerator)


def fmt_vec(v, names=PARAMS):
    parts = []
    for c, nme in zip(v, names):
        if c:
            parts.append(f"{'+' if c > 0 else '-'}{fmt(abs(c))}*{nme}")
    return " ".join(parts) if parts else "0"


# ================================================================ sections
def section_moments():
    print("== S1 moments and Grams ==")
    check("E[z^2]=1/3, E[z^4]=1/5, E[x^2y^2]=1/15, E[x^2y^2z^2]=1/105",
          moment_sphere(0, 0, 2) == Fr(1, 3) and moment_sphere(0, 0, 4) == Fr(1, 5)
          and moment_sphere(2, 2, 0) == Fr(1, 15)
          and moment_sphere(2, 2, 2) == Fr(1, 105))
    nv = 9
    t = pdot(0, 1, nv)
    P = {k: legendre(k, t, nv) for k in range(5)}
    ok = True
    for i in range(1, 5):
        for j in range(1, 5):
            want = Fr(1, 2 * i + 1) if i == j else Fr(0)
            ok &= expect(pmul(P[i], P[j]), 3, moment_sphere) == want
    check("one edge: E[P_i(v.w)P_j(v.w)] = delta_ij/(2i+1), i,j<=4", ok)
    ok = all(expect(P[i], 3, moment_sphere) == 0 for i in range(1, 5))
    check("E[P_d(v.w)] = 0 for d=1..4 (zero-mean tangents)", ok)
    t2 = pdot(1, 2, nv)
    ok = all(expect(pmul(P[i], legendre(j, t2, nv)), 3, moment_sphere) == 0
             for i in range(1, 5) for j in range(1, 5))
    check("wedge u-v-w: E[P_i(u.v)P_j(v.w)] = 0 for i,j=1..4", ok)
    s1 = pmul(pvar(0, 2, nv), pvar(1, 2, nv))
    g = [[expect(pmul(a, b), 3, moment_sphere) for b in (P[1], s1)] for a in (P[1], s1)]
    check("one edge soldered Gram [[1/3,1/9],[1/9,1/9]], det 2/81",
          g == [[Fr(1, 3), Fr(1, 9)], [Fr(1, 9), Fr(1, 9)]]
          and g[0][0] * g[1][1] - g[0][1] * g[1][0] == Fr(2, 81))
    h = pconst(Fr(-3, 5), nv)
    for i in range(3):
        v = pvar(0, i, nv)
        h = padd(h, pmul(pmul(v, v), pmul(v, v)))
    check("cubic site term: E[H]=0, E[H^2]=16/525",
          expect(h, 3, moment_sphere) == 0
          and expect(pmul(h, h), 3, moment_sphere) == Fr(16, 525))
    for nme, mom in (("binary_z", moment_binary_z), ("six_axis", moment_six_axis)):
        vals = sorted(set(fmt(expect(pmul(P[i], P[j]), 3, mom)) for i in (1, 2)
                          for j in (1, 2)))
        print(f"   {nme}: one-edge Gram entries over P1,P2: {vals}")


def predicted_continuum_fisher(win):
    E, n = len(win["edges"]), win["n"]
    M = [[Fr(0)] * 6 for _ in range(6)]
    for k, den in ((0, 3), (1, 5), (2, 7), (3, 9)):
        M[k][k] = Fr(E, den)
    M[4][4] = Fr(E, 9)
    M[0][4] = M[4][0] = Fr(E, 9)
    M[5][5] = Fr(16 * n, 525)
    return M


FISHER = {}   # (window, alphabet) -> matrix, filled by section_fisher


def section_fisher(wins):
    print("== S2 continuum Fisher ==")
    for win in wins:
        T = tangents(win)
        M = fisher(T, win["n"], moment_sphere)
        FISHER[(win["name"], "continuum")] = M
        pred = predicted_continuum_fisher(win)
        rank, null = rank_and_nullspace(M)
        E = len(win["edges"])
        print(f"   {win['name']}: |E|={E} diag={','.join(fmt(M[i][i]) for i in range(6))}"
              f" I[P1,S1]={fmt(M[0][4])} rank={rank}")
        check(f"{win['name']} continuum Fisher = analytic prediction", M == pred)
        check(f"{win['name']} continuum Fisher rank 6 of 6 (local tangent)", rank == 6
              and not null)
        means = [expect(T[a], win["n"], moment_sphere) for a in PARAMS]
        check(f"{win['name']} continuum: all six tangents have zero mean",
              all(m == 0 for m in means))


def section_finite(wins):
    print("== S3 finite Fisher/null directions ==")
    e = {p: [Fr(1) if q == p else Fr(0) for q in PARAMS] for p in PARAMS}

    def vsub(a, b, c=Fr(1)):
        return [x - c * y for x, y in zip(a, b)]
    expected = {
        ("2x3", "binary_z"): (1, [e["P2"], e["P4"], e["H"], vsub(e["P1"], e["P3"]),
                                  e["S1"]]),
        ("2x2x2", "binary_z"): (2, [e["P2"], e["P4"], e["H"], vsub(e["P1"], e["P3"])]),
        ("2x3", "six_axis"): (3, [e["H"], vsub(e["P1"], e["P3"]),
                                  vsub(e["P4"], e["P2"], Fr(5, 12))]),
        ("2x2x2", "six_axis"): (3, [e["H"], vsub(e["P1"], e["P3"]),
                                    vsub(e["P4"], e["P2"], Fr(5, 12))]),
    }
    for win in wins:
        T = tangents(win)
        for alph in ("binary_z", "six_axis"):
            mom = ALPHABETS[alph]
            M = fisher(T, win["n"], mom)
            FISHER[(win["name"], alph)] = M
            rank, null = rank_and_nullspace(M)
            want_rank, named = expected[(win["name"], alph)]
            zero = [Fr(0)] * 6
            annihilated = all(matvec(M, v) == zero for v in named)
            spans = len(named) == 6 - rank and all(in_span(v, null) for v in named)
            print(f"   {win['name']} {alph}: rank={rank}, "
                  f"null={{{', '.join(fmt_vec(v) for v in named)}}}")
            check(f"{win['name']} {alph} Fisher rank {want_rank}", rank == want_rank)
            check(f"{win['name']} {alph}: named null vectors annihilated and span the "
                  f"null space", annihilated and spans)
    # the algebraic relations behind the collapse, checked as polynomial identities
    nv = 6
    t = pdot(0, 1, nv)
    p1, p2, p3, p4 = (legendre(k, t, nv) for k in (1, 2, 3, 4))
    six_ok = (expect(pmul(padd(p3, pscale(p1, -1)), padd(p3, pscale(p1, -1))), 2,
                     moment_six_axis) == 0
              and expect(pmul(padd(p4, padd(pscale(p2, Fr(-5, 12)), pconst(Fr(-7, 12), nv))),
                              padd(p4, padd(pscale(p2, Fr(-5, 12)), pconst(Fr(-7, 12), nv)))),
                         2, moment_six_axis) == 0)
    bin_ok = (expect(pmul(padd(p3, pscale(p1, -1)), padd(p3, pscale(p1, -1))), 2,
                     moment_binary_z) == 0
              and expect(pmul(padd(p2, pconst(-1, nv)), padd(p2, pconst(-1, nv))), 2,
                         moment_binary_z) == 0)
    check("six-axis relations P3=P1, P4=7/12+(5/12)P2 hold in L2 (t in {-1,0,1})", six_ok)
    check("binary relations P3=P1, P2=1 hold in L2 (t in {-1,+1})", bin_ok)
    cont_ok = (expect(pmul(padd(p3, pscale(p1, -1)), padd(p3, pscale(p1, -1))), 2,
                      moment_sphere) == Fr(1, 7) + Fr(1, 3))
    check("continuum: ||P3-P1||^2 = 1/7+1/3 (no relation)", cont_ok)


# ------------------------------------------------------- formation orders
def expect_site(p, site, moment):
    """Partial expectation over one site; returns a polynomial in the rest."""
    out = {}
    for mono, c in p.items():
        m = moment(mono[3 * site], mono[3 * site + 1], mono[3 * site + 2])
        if m == 0:
            continue
        key = list(mono)
        key[3 * site:3 * site + 3] = [0, 0, 0]
        key = tuple(key)
        v = out.get(key, 0) + c * m
        if v:
            out[key] = v
        elif key in out:
            del out[key]
    return out


def linear_extensions(win):
    """Total orders in which every site follows its coordinatewise-smaller sites."""
    out = []

    def rec(prefix, remaining):
        if not remaining:
            out.append(tuple(prefix))
            return
        for s in remaining:
            minimal = all(not all(a <= b for a, b in zip(t, s))
                          for t in remaining if t != s)
            if minimal:
                rec(prefix + [win["idx"][s]], [t for t in remaining if t != s])
    rec([], list(win["sites"]))
    return out


def recorded_sets(win, order):
    pos = {s: i for i, s in enumerate(order)}
    return {x: frozenset(y for y in win["nbrs"][x] if pos[y] < pos[x])
            for x in range(win["n"])}


def wedge_list(win):
    """Apex-resolved wedges (x; q, q'), q<q' neighbours of x."""
    return [(x, q, qq) for x in range(win["n"])
            for q, qq in combinations(sorted(win["nbrs"][x]), 2)]


def iota(Q, W):
    return tuple(1 if (q in Q[x] and qq in Q[x]) else 0 for x, q, qq in W)


def k_multiset(Q):
    return tuple(sorted(tuple(sorted(s)) for s in Q.values() if len(s) >= 2))


def pair_vector(Q, PAIRS):
    cnt = {pr: 0 for pr in PAIRS}
    for s in Q.values():
        if len(s) >= 2:
            for pr in combinations(sorted(s), 2):
                cnt[pr] += 1
    return tuple(cnt[pr] for pr in PAIRS)


def series_mul(a, b):
    """Truncated (order 2) product of series [c0,c1,c2] of polynomials."""
    return [pmul(a[0], b[0]),
            padd(pmul(a[0], b[1]), pmul(a[1], b[0])),
            padd(padd(pmul(a[0], b[2]), pmul(a[1], b[1])), pmul(a[2], b[0]))]


def order_law_series(win, Q, product_class):
    """theta-series to second order of the finished-window law density
    (relative to the uniform product measure) formed along the order with
    recorded-neighbour sets Q, for the degree-1 kernel g(p,q) = p.q.
    product_class=True: r = prod_q (1+theta p.q)/Z_theta(Q);
    False: r = 1 + theta sum_q p.q (exactly normalised, no Z)."""
    nv = 3 * win["n"]
    L = [pconst(1, nv), {}, {}]
    for x, S in Q.items():
        S = sorted(S)
        if product_class:
            N = [pconst(1, nv), {}, {}]
            for q in S:
                N = series_mul(N, [pconst(1, nv), pdot(x, q, nv), {}])
            Z2 = expect_site(N[2], x, moment_sphere)
            Z1 = expect_site(N[1], x, moment_sphere)
            assert not Z1
            r = series_mul(N, [pconst(1, nv), {}, pscale(Z2, -1)])
        else:
            s1 = {}
            for q in S:
                s1 = padd(s1, pdot(x, q, nv))
            r = [pconst(1, nv), s1, {}]
        L = series_mul(L, r)
    return L


def norm2(poly, n):
    return expect(pmul(poly, poly), n, moment_sphere)


def section_orders(wins):
    print("== S4 first-order tangent ==")
    nv9 = 9
    t01, t02 = pdot(0, 1, nv9), pdot(0, 2, nv9)
    # E_p[P_d(p.q)] vanishes on the unit sphere |q|=1 (not as a free polynomial
    # for d>=2, where it is a multiple of |q|^2-1): check its L^2 norm over q.
    ok = all(not expect(pmul(expect_site(legendre(d, t01, nv9), 0, moment_sphere),
                            expect_site(legendre(d, t01, nv9), 0, moment_sphere)), 3, moment_sphere)
             for d in (1, 2, 3, 4))
    check("E_p[P_d(p.q)] = 0 on the sphere, d=1..4 (every conditional normalised)", ok)
    z2 = expect_site(pmul(t01, t02), 0, moment_sphere)
    check("E_p[(p.q)(p.q')] = (1/3) q.q' (product-class normaliser at second order)",
          pequal(z2, pscale(pdot(1, 2, nv9), Fr(1, 3))))
    data = {}
    for win, ds in ((wins[0], (1, 2)), (wins[1], (1,))):
        nv = 3 * win["n"]
        T = tangents(win)
        EP = {d: {} for d in ds}
        for x, y, _ in win["edges"]:
            for d in ds:
                EP[d][(x, y)] = EP[d][(y, x)] = legendre(d, pdot(x, y, nv), nv)
        W = wedge_list(win)
        PAIRS = sorted({(q, qq) for _, q, qq in W})
        orders = list(permutations(range(win["n"])))
        ok = True
        ksets, pvecs, ivecs = {}, {}, {}
        isum = [0] * len(W)
        for od in orders:
            Q = recorded_sets(win, od)
            for d in ds:
                S = {}
                for x, Sx in Q.items():
                    for q in Sx:
                        S = padd(S, EP[d][(x, q)])
                ok &= pequal(S, T[f"P{d}"])
            iv = iota(Q, W)
            isum = [a + b for a, b in zip(isum, iv)]
            ksets.setdefault(k_multiset(Q), od)
            pvecs.setdefault(pair_vector(Q, PAIRS), od)
            ivecs.setdefault(iv, od)
        check(f"{win['name']}: shared-kernel tangent sum = static T_d for all {len(orders)} orders,"
              f" d in {list(ds)}", ok)
        check(f"{win['name']}: apex-latest frequency 1/3 for every wedge over all orders",
              all(Fr(s, len(orders)) == Fr(1, 3) for s in isum))
        data[win["name"]] = dict(W=W, PAIRS=PAIRS, ksets=ksets, pvecs=pvecs,
                                 ivecs=ivecs, norders=len(orders))
    return data


# --------------------------------------------- second order in the kernel
def second_order_data(win):
    """Closed-form second-order objects for the degree-1 kernel g = P1:
    A = sum_{e<e'} g_e g_e' (static coefficient), apex-resolved wedge
    polynomials B'_w = (v_x.v_q)(v_x.v_q') (additive class), arm-pair
    polynomials F_{qq'} = v_q.v_q' (product class)."""
    nv = 3 * win["n"]
    g = [pdot(x, y, nv) for x, y, _ in win["edges"]]
    A = {}
    for i in range(len(g)):
        for j in range(i + 1, len(g)):
            A = padd(A, pmul(g[i], g[j]))
    W = wedge_list(win)
    Bp = [pmul(pdot(x, q, nv), pdot(x, qq, nv)) for x, q, qq in W]
    PAIRS = sorted({(q, qq) for _, q, qq in W})
    F = {pr: pdot(pr[0], pr[1], nv) for pr in PAIRS}
    return dict(A=A, W=W, Bp=Bp, PAIRS=PAIRS, F=F)


def c_add(Q, so):
    c = so["A"]
    for k, (x, q, qq) in enumerate(so["W"]):
        if q in Q[x] and qq in Q[x]:
            c = padd(c, pscale(so["Bp"][k], -1))
    return c


def c_prod(Q, so):
    c = so["A"]
    for x, q, qq in so["W"]:
        if q in Q[x] and qq in Q[x]:
            c = padd(c, pscale(so["F"][(q, qq)], Fr(-1, 3)))
    return c


def gram(polys, n):
    m = len(polys)
    G = [[Fr(0)] * m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            G[i][j] = G[j][i] = expect(pmul(polys[i], polys[j]), n, moment_sphere)
    return G


def qform(G, u, v):
    return sum(ui * sum(Gij * vj for Gij, vj in zip(Gi, v) if vj)
               for ui, Gi in zip(u, G) if ui)


def section_second_order(wins, data):
    print("== S5 second order: classes, Grams, separations ==")
    out = {}
    for win in wins:
        nm, n, d = win["name"], win["n"], data[win["name"]]
        so = second_order_data(win)
        W, PAIRS = so["W"], so["PAIRS"]
        check(f"{nm}: E[A] = 0 (static normaliser has no theta^2 term)",
              not expect(so["A"], n, moment_sphere))
        kexp = {"2x3": 28, "2x2x2": 542}[nm]
        check(f"{nm}: K-multiset classes {len(d['ksets'])} = formation-order census {kexp}",
              len(d["ksets"]) == kexp)
        print(f"  {nm}: wedges {len(W)}, arm pairs {len(PAIRS)}, classes: K {len(d['ksets'])},"
              f" pair-vector {len(d['pvecs'])}, apex-vector {len(d['ivecs'])}")
        Ga = gram(so["Bp"], n)
        ok, shared = True, 0
        for i, (x, q, qq) in enumerate(W):
            for j, (x2, q2, qq2) in enumerate(W):
                if i == j:
                    want = Fr(1, 9)
                elif (q, qq) == (q2, qq2):
                    want, shared = Fr(1, 27), shared + 1
                else:
                    want = Fr(0)
                ok &= Ga[i][j] == want
        check(f"{nm}: apex Gram = 1/9 diag, 1/27 on {shared} shared-arm-pair entries, else 0", ok)
        rk, _ = rank_and_nullspace([row[:] for row in Ga])
        check(f"{nm}: apex Gram rank {rk} = #wedges (additive coefficient map injective)",
              rk == len(W))
        Gp = gram([so["F"][pr] for pr in PAIRS], n)
        check(f"{nm}: arm-pair Gram = (1/3) identity on {len(PAIRS)} pairs",
              all(Gp[i][j] == (Fr(1, 3) if i == j else 0)
                  for i in range(len(PAIRS)) for j in range(len(PAIRS))))
        # product class: dist^2 = |dm|^2 / 27 over pair vectors
        pv = list(d["pvecs"])
        dp = [sum((a - b) ** 2 for a, b in zip(u, v)) for i, u in enumerate(pv)
              for v in pv[i + 1:]]
        nz = [x for x in dp if x]
        check(f"{nm}: product-class pair-vector classes {len(pv)} distinct", len(nz) == len(dp))
        print(f"  {nm}: product class min dist^2 = {min(nz)}/27, max = {max(nz)}/27 over {len(dp)} class pairs")
        # additive class: dist^2 = di^T Ga di over apex vectors
        iv = list(d["ivecs"])
        Gi = {u: [sum(Gij * uj for Gij, uj in zip(Gi_, u) if uj) for Gi_ in Ga] for u in iv}
        sq = {u: sum(a * b for a, b in zip(u, Gi[u])) for u in iv}
        if len(iv) <= 400:
            pairs = [(u, v) for i, u in enumerate(iv) for v in iv[i + 1:]]
            scope = "all pairs"
        else:
            ref = tuple(iota(recorded_sets(win, linear_extensions(win)[0]), W))
            pairs = [(ref, v) for v in iv if v != ref]
            scope = "monotone vs all"
        da = [sq[u] + sq[v] - 2 * sum(a * b for a, b in zip(u, Gi[v])) for u, v in pairs]
        check(f"{nm}: additive apex-vector classes {len(iv)} distinct ({scope})",
              all(x > 0 for x in da))
        print(f"  {nm}: additive min dist^2 = {min(da)}, max = {max(da)} over {len(da)} pairs ({scope})")
        out[nm] = dict(so=so, Ga=Ga)
    return out


def section_named(wins, data, so_out):
    print("== S6 named order laws ==")
    for win in wins:
        nm, n = win["name"], win["n"]
        so, Ga = so_out[nm]["so"], so_out[nm]["Ga"]
        W, PAIRS = so["W"], so["PAIRS"]
        T = tangents(win)
        lex = linear_extensions(win)
        Qs = [recorded_sets(win, od) for od in lex]
        check(f"{nm}: {len(lex)} linear extensions, one recorded map (monotone-box)",
              all(Q == Qs[0] for Q in Qs))
        Qm, Qr = Qs[0], recorded_sets(win, tuple(reversed(lex[0])))
        sites, idx = win["sites"], win["idx"]
        want_m = {idx[s]: frozenset(idx[tuple(s[i] - (i == dd) for i in range(3))]
                                    for dd in range(3) if s[dd] >= 1) for s in sites}
        want_r = {idx[s]: frozenset(idx[tuple(s[i] + (i == dd) for i in range(3))]
                                    for dd in range(3) if s[dd] + 1 < win["shape"][dd]) for s in sites}
        check(f"{nm}: monotone-box records x-e_d, reversed records x+e_d", Qm == want_m and Qr == want_r)
        cs = so["A"]
        cm_p, cr_p = c_prod(Qm, so), c_prod(Qr, so)
        cm_a, cr_a = c_add(Qm, so), c_add(Qr, so)
        cu_p = cs
        for x, q, qq in W:
            cu_p = padd(cu_p, pscale(so["F"][(q, qq)], Fr(-1, 9)))
        cu_a = cs
        for k in range(len(W)):
            cu_a = padd(cu_a, pscale(so["Bp"][k], Fr(-1, 3)))
        dist = lambda a, b: norm2(padd(a, pscale(b, -1)), n)
        named = {"static|uniform": (cs, cu_p, cs, cu_a), "static|monotone": (cs, cm_p, cs, cm_a),
                 "monotone|reversed": (cm_p, cr_p, cm_a, cr_a)}
        for lab, (a, b, c, e) in named.items():
            print(f"  {nm} {lab}: product dist^2 = {dist(a, b)}, additive dist^2 = {dist(c, e)}")
        # exact predictions
        mult = {}
        for x, q, qq in W:
            mult[(q, qq)] = mult.get((q, qq), 0) + 1
        pred_u = Fr(sum(m * m for m in mult.values()), 243)
        check(f"{nm}: static|uniform product dist^2 = sum(mult^2)/243 = {pred_u}", dist(cs, cu_p) == pred_u)
        pm = pair_vector(Qm, PAIRS); pr_ = pair_vector(Qr, PAIRS)
        check(f"{nm}: static|monotone product dist^2 = |m|^2/27 = {Fr(sum(v*v for v in pm), 27)}",
              dist(cs, cm_p) == Fr(sum(v * v for v in pm), 27))
        same_pairs = pm == pr_
        check(f"{nm}: monotone/reversed pair vectors {'equal' if same_pairs else 'differ'} <=> product dist^2 "
              f"{'= 0' if same_pairs else '> 0'}", (dist(cm_p, cr_p) == 0) == same_pairs)
        check(f"{nm}: monotone/reversed K-multisets differ {k_multiset(Qm) != k_multiset(Qr)}"
              if nm == "2x2x2" else f"{nm}: monotone/reversed K-multisets equal {k_multiset(Qm) == k_multiset(Qr)}",
              (k_multiset(Qm) != k_multiset(Qr)) if nm == "2x2x2" else (k_multiset(Qm) == k_multiset(Qr)))
        im, ir = iota(Qm, W), iota(Qr, W)
        di = [a - b for a, b in zip(im, ir)]
        check(f"{nm}: additive monotone|reversed dist^2 = apex Gram form {qform(Ga, di, di)}",
              dist(cm_a, cr_a) == qform(Ga, di, di) and qform(Ga, di, di) > 0)
        # truncated theta-series validation of both closed forms
        for lab, Q in (("monotone", Qm), ("reversed", Qr)):
            if nm == "2x2x2" and lab == "reversed":
                continue
            for pc, cf, cl in ((True, c_prod, "product"), (False, c_add, "additive")):
                L = order_law_series(win, Q, pc)
                ok = (pequal(L[0], pconst(1, 3 * n)) and pequal(L[1], T["P1"]) and pequal(L[2], cf(Q, so))
                      and not expect(L[1], n, moment_sphere) and not expect(L[2], n, moment_sphere))
                check(f"{nm} {lab} {cl}: series = [1, T_1, closed-form c], normalised", ok)


def main():
    wins = [make_window((2, 3, 1)), make_window((2, 2, 2))]
    section_moments()
    section_fisher(wins)
    section_finite(wins)
    data = section_orders(wins)
    so_out = section_second_order(wins, data)
    section_named(wins, data, so_out)
    npass = sum(1 for r in RESULTS if r)
    nfail = len(RESULTS) - npass
    print("scope per_element=exact moments; per_site=6/8; per_mode=3 alphabets,2 models; per_block=all-order tangents,named series; lattice_wide=unrun")
    print(f"elapsed {time.time() - T0:.1f}s")
    print(f"TOTAL: PASS={npass} FAIL={nfail}")
    sys.exit(1 if nfail else 0)


if __name__ == "__main__":
    main()
