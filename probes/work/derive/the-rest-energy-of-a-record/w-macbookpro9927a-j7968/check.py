#!/usr/bin/env python3
"""The rest energy of a record: checks for ATTEMPT.md (attempt 1 of 2), worker w-macbookpro9927a-j7968 (claude-opus-5-5).

Objects: block 56's box (interior 5^3, walls held at phi = 1), A the six-neighbour average, G = (1 - A)^-1 on the interior,
g_y = G(y, y); block 55's ledger <H_w> + F, F = (2/gamma) sum_bonds (phi_x - phi_y)^2; block 58's formation event with the
ledger kept; block 53's record clause w_y = kappa M(neighbours) with block 56's mean M_1/2 = (average of sqrt w)^2; block 95's
records on their own clocks on the 4^3 torus. Everything is exact: Fractions, sympy DomainMatrix over QQ, sympy series.
"""
from __future__ import annotations

import itertools
import json
import random
import subprocess
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


NOTES = {
    "58": ("e526d22c18", "docs/ADMISSIBILITY_RULE_WHAT_A_FORMATION_EVENT_DOES_TO_THE_LEDGER_AND_TO_THE_FAR_FIELD_THE_MONOPOLE_NEVER_JUMPS_"
           "THE_DIPOLE_DOES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
           ["E' = m'/(1 + (γ/12) g_y m')", "such an `m' > 0` exists iff `E < 12/(γ g_y)`",
            "**The record.** One body at rest at `y` with bare energy `m'`"]),
    "56": ("d6c6e2572d", "docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_"
           "RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
           ["A positive rate field is a static solution iff `φ` solves `((1 − A) + D) φ = 0` at every interior site with `φ = 1` on the walls.",
            "For the simplest bond energy the ledger is `Σ_i m_i φ_i`"]),
    "55": ("525c6500c5", "docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_"
           "PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
           ["block 53's power mean of order `1/2`", "`log κ = −(γ/6) E/w̄`"]),
    "53": ("c4e6a23f6c", "docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_"
           "LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
           ["**Record clause.** At a record, `w_x = κ F̃(neighbours)` with `F̃` of the same class",
            "`κ` may depend on the record's content and on its occupied neighbours"]),
    "95": ("f9b34475df", "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_"
           "ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md",
           ["A move `x → y` runs at the rate `w_x^a w_y^(1−a) · h / 6`", "`6G(d) − Σ_e G(d + e) = [d = 0] − 1/N`"]),
    "104": ("705d466f49", "docs/ADMISSIBILITY_RULE_THE_RULES_OWN_CLOCK_HAS_NO_FAR_FIELD_THE_PULL_NEEDS_A_RATE_LAW_WITH_A_MONOPOLE_A_REST_"
            "ENERGY_AND_A_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-23.md",
            ["With block 55's packet, `S/E = −γ/6`, so a record needs `log κ = −(γ/6)E_rec`."]),
}
TASK_Q = ["(a) Under block 58's formation event (an amplitude's energy converted into a record's, the ledger kept), what rest energy "
          "does a record carry, and does it depend on its content?"]


def family_q() -> None:
    miss = []
    for b, (sha, path, qs) in NOTES.items():
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"b{b}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:the-rest-energy-of-a-record:a1"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    n = sum(len(v[2]) for v in NOTES.values()) + len(TASK_Q)
    check("Q", not miss, f"blocks 53, 55, 56, 58, 95, 104 (PR heads) and the task quoted verbatim ({n} lines)"
          f"{'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ the box of block 56
NB = 5
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SITES = list(itertools.product(range(NB), repeat=3))
IDX = {s: i for i, s in enumerate(SITES)}
NS = len(SITES)


def add(s, e):
    return tuple(a + b for a, b in zip(s, e))


def fr(q) -> Fr:
    return Fr(int(q.numerator), int(q.denominator))


def solve_law(c: Fr, K: dict) -> list[Fr]:
    """c((1 - A)phi)_x + (K phi)_x = 0 at every interior x, phi = 1 on the walls (block 56 T1 and its remark)."""
    rows = [[QQ(0)] * NS for _ in range(NS)]
    rhs = [QQ(0)] * NS
    for s, i in IDX.items():
        rows[i][i] += QQ(c.numerator, c.denominator)
        for e in E6:
            t = add(s, e)
            if t in IDX:
                rows[i][IDX[t]] -= QQ(c.numerator, c.denominator * 6)
            else:
                rhs[i] += QQ(c.numerator, c.denominator * 6)
    for (i, j), v in K.items():
        rows[i][j] += QQ(v.numerator, v.denominator)
    M = DomainMatrix(rows, (NS, NS), QQ)
    b = DomainMatrix([[r] for r in rhs], (NS, 1), QQ)
    x = M.lu_solve(b)
    return [fr(x[i, 0].element) for i in range(NS)]


def avg_phi(phi, s) -> Fr:
    return sum((phi[IDX[add(s, e)]] if add(s, e) in IDX else Fr(1)) for e in E6) / 6


def bond_sum(phi) -> Fr:
    """sum over all bonds of the box of (phi_x - phi_y)^2, wall sites at phi = 1 (wall-wall bonds give 0)."""
    tot = Fr(0)
    for s, i in IDX.items():
        for e in E6[0::2]:
            t = add(s, e)
            tot += (phi[i] - (phi[IDX[t]] if t in IDX else 1)) ** 2
        for e in E6[1::2]:
            t = add(s, e)
            if t not in IDX:
                tot += (phi[i] - 1) ** 2
    return tot


def wall_flux(phi) -> Fr:
    return sum(1 - phi[i] for s, i in IDX.items() for e in E6 if add(s, e) not in IDX)


def green():
    rows = [[QQ(0)] * NS for _ in range(NS)]
    for s, i in IDX.items():
        rows[i][i] = QQ(1)
        for e in E6:
            t = add(s, e)
            if t in IDX:
                rows[i][IDX[t]] -= QQ(1, 6)
    Minv = DomainMatrix(rows, (NS, NS), QQ).inv()
    return lambda a, b: fr(Minv[IDX[a], IDX[b]].element)


# ------------------------------------------------------------------------------------------------ K: a body's kappa in block 56's law
def family_k(G) -> None:
    d = sp.Symbol("d", positive=True)
    phi_y, aphi = sp.symbols("phi_y Aphi", positive=True)
    sol = sp.solve(sp.Eq(phi_y - aphi + d * phi_y, 0), aphi)[0]
    ok_sym = sp.simplify((phi_y / sol) ** 2 - (1 + d) ** -2) == 0
    gam = Fr(1)
    bodies = {(2, 2, 2): Fr(3), (1, 2, 3): Fr(1, 2), (3, 3, 1): Fr(7, 5)}
    phi = solve_law(Fr(1), {(IDX[s], IDX[s]): gam / 12 * m for s, m in bodies.items()})
    ok = all(p > 0 for p in phi)
    for s, i in IDX.items():
        k = (phi[i] / avg_phi(phi, s)) ** 2
        ok &= k == ((1 + gam / 12 * bodies[s]) ** -2 if s in bodies else 1)
    # the geometric mean of block 53 T2: kappa_geo^6 = phi_y^12 / prod phi_nbr^2 is not a function of the body alone
    def kgeo6(conf, s):
        ph = solve_law(Fr(1), {(IDX[t], IDX[t]): gam / 12 * m for t, m in conf.items()})
        prod = Fr(1)
        for e in E6:
            t = add(s, e)
            prod *= (ph[IDX[t]] if t in IDX else 1) ** 2
        return ph[IDX[s]] ** 12 / prod
    k1 = kgeo6({(2, 2, 2): Fr(3)}, (2, 2, 2))
    k2 = kgeo6({(2, 2, 2): Fr(3), (2, 2, 3): Fr(3)}, (2, 2, 2))
    check("K", ok_sym and ok and k1 != k2,
          "block 56's law at a body site is (A phi)_y = (1 + (gamma/12) m) phi_y, so w_y = kappa M_1/2(neighbours) with kappa = "
          "(1 + gamma m/12)^-2 exactly, whatever else is in the box (3 bodies, all 125 sites; kappa = 1 at empty sites); in the geometric "
          f"mean kappa^6 changes with a neighbour ({float(k1):.4f} -> {float(k2):.4f}): the dictionary is block 56's mean's")


# ------------------------------------------------------------------------------------------------ F: the formation event, ledger kept
def ledger_three_ways(gam, K, phi):
    hw = sum(v * phi[i] * phi[j] for (i, j), v in K.items())
    return hw + 2 / gam * bond_sum(phi), 2 / gam * wall_flux(phi)


def form(G, gam, m, p, y):
    K = {(IDX[s], IDX[s]): m * w for s, w in p.items()}
    phi = solve_law(Fr(12) / gam, K)
    L = sum(m * w * phi[IDX[s]] for s, w in p.items())
    la, lb = ledger_three_ways(gam, K, phi)
    gy = G(y, y)
    mp = L / (1 - gam / 12 * gy * L)
    phr = solve_law(Fr(12) / gam, {(IDX[y], IDX[y]): mp})
    Lr = mp * phr[IDX[y]]
    kap = (1 + gam * mp / 12) ** -2
    kform = ((1 - gam / 12 * gy * L) / (1 - gam / 12 * (gy - 1) * L)) ** 2
    ok = (L == la == lb and Lr == L and phr[IDX[y]] == 1 - gam / 12 * gy * L and kap == kform
          and (phr[IDX[y]] / avg_phi(phr, y)) ** 2 == kap and L < 12 / (gam * gy) and all(v > 0 for v in phi + phr))
    return ok, L, mp, kap, gy


AMPS = {}


def family_f(G) -> dict:
    y = (2, 2, 2)
    x1 = (3, 2, 2)
    AMPS["point"] = {y: Fr(1)}
    AMPS["pair"] = {y: Fr(1, 2), x1: Fr(1, 2)}
    AMPS["cross"] = {y: Fr(1, 7), **{add(y, e): Fr(1, 7) for e in E6}}
    gam, m = Fr(1), Fr(1)
    res = {k: form(G, gam, m, p, y) for k, p in AMPS.items()}
    ok = all(r[0] for r in res.values())
    mps = [res[k][2] for k in ("point", "pair", "cross")]
    ok &= mps[0] == m and m < mps[1] < mps[2]
    kaps = [res[k][3] for k in ("point", "pair", "cross")]
    ok &= kaps[0] > kaps[1] > kaps[2]
    alt = form(G, gam, m, AMPS["pair"], x1)
    ok &= alt[0] and alt[2] != res["pair"][2] and alt[1] == res["pair"][1]
    check("F", ok,
          "one amplitude at rest (bare m = 1, gamma = 1) in the 5^3 box: its ledger sum m_x phi_x = <H_w> + F = (2/gamma) x wall flux; "
          "the record at the centre with m' = L/(1 - (gamma/12) g_y L) keeps it, phi_y = 1 - (gamma/12) g_y L, "
          "kappa = [(1 - (gamma/12)g_yL)/(1 - (gamma/12)(g_y - 1)L)]^2; "
          f"m' = 1, {float(mps[1]):.6f}, {float(mps[2]):.6f} for a point, a pair, a cross (g_y = {res['point'][4]}); "
          f"the pair's record one site over has m' = {float(alt[2]):.6f}")
    return res


# ------------------------------------------------------------------------------------------------ S: the series in gamma m
def Q(x: Fr) -> sp.Rational:
    return sp.Rational(x.numerator, x.denominator)


def family_s(G, res) -> None:
    t = sp.Symbol("t")
    y = (2, 2, 2)
    g = Q(G(y, y))
    ok = True
    for k in ("pair", "cross"):
        p = AMPS[k]
        S = list(p)
        n = len(S)
        GS = sp.Matrix(n, n, lambda i, j: Q(G(S[i], S[j])))
        pv = sp.Matrix([Q(p[s]) for s in S])
        M = sp.diag(*[1 / Q(p[s]) for s in S]) + t * GS
        # E/m = 1^T (P^-1 + t G_S)^-1 1 = det(M + 1 1^T)/det(M) - 1 (block 56 T3(b) with D = tP, t = gamma m/12)
        Em = sp.cancel(sp.expand((M + sp.ones(n, n)).det(method="berkowitz")) / sp.expand(M.det(method="berkowitz")) - 1)
        ok &= Em.subs(t, sp.Rational(1, 12)) == Q(res[k][1])      # the full 125-site law at gamma m = 1
        mean_g = (pv.T * GS * pv)[0, 0]
        s1 = sp.series(Em, t, 0, 2).removeO()
        s2 = sp.series(Em / (1 - t * g * Em), t, 0, 2).removeO()
        s3 = sp.series(-2 * sp.log(1 + t * s2), t, 0, 3).removeO()
        ok &= sp.expand(s1 - (1 - t * mean_g)) == 0
        ok &= sp.expand(s2 - (1 + t * (g - mean_g))) == 0
        ok &= sp.expand(s3 - (-2 * t - t ** 2 * (2 * (g - mean_g) - 1))) == 0
        ok &= g - mean_g > 0 and all(Q(G(s, s)) <= g for s in S)
    gam, gg, L = sp.symbols("gamma g L", positive=True)
    lk = 2 * sp.log(1 - gam * gg * L / 12) - 2 * sp.log(1 - gam * (gg - 1) * L / 12)
    ok &= sp.expand(sp.series(lk, gam, 0, 3).removeO() - (-gam * L / 6 - gam ** 2 * (2 * gg - 1) * L ** 2 / 144)) == 0
    check("S", ok, "E = m(1 - t<G>_p) + O(t^2), m' = m(1 + t(g_y - <G>_p)) + O(t^2), log kappa = -2t - t^2(2(g_y - <G>_p) - 1) + O(t^3), "
          "t = gamma m/12, for the pair and the cross (E(t) exact, equal to the 125-site law at t = 1/12; g_y the largest g on each support, "
          "g_y > <G>_p); in the ledger, log kappa = -(gamma/6)L - (gamma^2/144)(2g_y - 1)L^2 + O(gamma^3)")


# ------------------------------------------------------------------------------------------------ T: one kappa and a kept ledger
def family_t(G, res) -> None:
    gam, g, k0, m = sp.symbols("gamma g kappa0 m", positive=True)
    m0 = 12 / gam * (k0 ** sp.Rational(-1, 2) - 1)
    L0 = m0 / (1 + gam * g * m0 / 12)
    ok = sp.simplify((1 + gam * m0 / 12) ** -2 - k0) == 0
    Ls = sp.Symbol("L")
    mp = Ls / (1 - gam * g * Ls / 12)
    ok &= sp.simplify(sp.diff(mp, Ls) - 1 / (1 - gam * g * Ls / 12) ** 2) == 0
    ok &= sp.simplify(mp.subs(Ls, L0) - m0) == 0
    # kappa0 = the point record's kappa: only amplitudes of the point's ledger can form a kappa0 record at y with the books kept
    Lp = res["point"][1]
    ok &= res["pair"][1] != Lp and res["cross"][1] != Lp and res["point"][2] == 1
    # negative ledger: m' < 0, kappa > 1, the record's clock above ambient
    gy = res["point"][4]
    Ln = Fr(-1, 2)
    mpn = Ln / (1 - Fr(1, 12) * gy * Ln)
    phn = solve_law(Fr(12), {(IDX[(2, 2, 2)], IDX[(2, 2, 2)]): mpn})
    ok &= mpn < 0 and (1 + mpn / 12) ** -2 > 1 and mpn * phn[IDX[(2, 2, 2)]] == Ln and phn[IDX[(2, 2, 2)]] > 1
    check("T", ok, "kappa(m') = kappa0 iff m' = m0 = (12/gamma)(kappa0^-1/2 - 1) iff L = L0(y) = m0/(1 + (gamma/12) g_y m0) (m' is "
          "increasing in L); the pair's and the cross's ledgers differ from the point's, so with kappa0 the point's kappa they cannot form "
          "one at the centre with the ledger kept; a ledger L = -1/2 gives m' < 0, kappa > 1 and phi_y > 1")


# ------------------------------------------------------------------------------------------------ M: an amplitude with no on-site term
def family_m(G) -> None:
    y = (2, 2, 2)
    z = add(y, (0, 1, 0))
    chi = {y: sp.Matrix([0, sp.Rational(3, 5)]), z: sp.Matrix([sp.Rational(4, 5), 0])}
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    K = {}
    for s in chi:
        for j, e in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
            for sgn, t in ((1, add(s, e)), (-1, add(s, tuple(-a for a in e)))):
                if t in chi:            # H_{s,s+e_j} = sigma_j/(2i), H_{s,s-e_j} = -sigma_j/(2i): the symmetric difference, no site term
                    v = sp.re(sp.expand((chi[s].H * (sgn * sig[j] / (2 * sp.I)) * chi[t])[0, 0]))
                    if v != 0:
                        K[(IDX[s], IDX[t])] = Fr(int(sp.fraction(v)[0]), int(sp.fraction(v)[1]))
    gam = Fr(1)
    phi = solve_law(Fr(12) / gam, K)
    la, lb = ledger_three_ways(gam, K, phi)
    e_unclocked = sum(K.values())
    gy = G(y, y)
    mp = la / (1 - gam / 12 * gy * la)
    phr = solve_law(Fr(12) / gam, {(IDX[y], IDX[y]): mp})
    ok = (all(i != j for (i, j) in K) and e_unclocked == Fr(12, 25) and la == lb and la > 0 and all(v > 0 for v in phi)
          and mp > 0 and mp * phr[IDX[y]] == la)
    check("M", ok, "an amplitude on two sites with no on-site term (H the symmetric difference times sigma_j; energy 12/25 at uniform "
          f"rates): ledger <H_w> + F = (2/gamma) x wall flux = {float(la):.6f} > 0, and the record it forms under the clause has "
          f"bare energy m' = {float(mp):.6f} > 0 with the ledger kept")


# ------------------------------------------------------------------------------------------------ C: block 95's chain with one kappa per record
def torus_green() -> dict:
    c = [1, 0, -1, 0]
    G = {}
    for d in itertools.product(range(4), repeat=3):
        s = Fr(0)
        for n in itertools.product(range(4), repeat=3):
            if n != (0, 0, 0):
                s += Fr(c[sum(a * b for a, b in zip(n, d)) % 4]) / (1 - Fr(c[n[0]] + c[n[1]] + c[n[2]], 3))
        G[d] = s / (6 * 64)
    return G


def family_c() -> None:
    G = torus_green()
    md = lambda v: tuple(a % 4 for a in v)
    sub = lambda u, v: md(tuple(a - b for a, b in zip(u, v)))
    ok = G[(1, 0, 0)] == Fr(257, 7680) and G[(2, 0, 0)] == Fr(29, 7680) and sum(G.values()) == 0
    ok &= all(6 * G[d] - sum(G[md(add(d, e))] for e in E6) == (1 if d == (0, 0, 0) else 0) - Fr(1, 64) for d in G)
    l1, l2, a = sp.symbols("lambda1 lambda2 a")
    lam = {1: l1, 2: l2}

    def logw(z, conf):
        return 6 * sum(lam[r] * sp.Rational(G[sub(z, pos)].numerator, G[sub(z, pos)].denominator) for r, pos in conf.items())

    def lograte(conf, r, to):
        return a * logw(conf[r], conf) + (1 - a) * logw(to, conf)

    x, y, u, v = (0, 0, 0), (1, 0, 0), (2, 1, 0), (2, 0, 0)
    cyc = [({1: x, 2: u}, 1, y), ({1: y, 2: u}, 2, v), ({1: y, 2: v}, 1, x), ({1: x, 2: v}, 2, u)]
    fwd = sum(lograte(cf, r, to) for cf, r, to in cyc)
    bwd = 0
    for cf, r, to in cyc:
        new = dict(cf); new[r] = to
        bwd += lograte(new, r, cf[r])
    Dl = G[sub(x, u)] - G[sub(y, u)] + G[sub(y, v)] - G[sub(x, v)]
    ok &= sp.expand(fwd - bwd - 6 * (2 * a - 1) * (l2 - l1) * sp.Rational(Dl.numerator, Dl.denominator)) == 0 and Dl != 0
    # a = 1, two records: pi(x1, x2) = 1/(r1(d) + r2(d)) is stationary for ANY positive r1, r2 of d = x1 - x2 (joint chain, exclusion)
    rnd = random.Random(7)
    r1 = {d: Fr(rnd.randint(1, 9), rnd.randint(1, 9)) for d in G if d != (0, 0, 0)}
    r2 = {d: Fr(rnd.randint(1, 9), rnd.randint(1, 9)) for d in G if d != (0, 0, 0)}
    pi = lambda d: 1 / (r1[d] + r2[d])
    bal = True
    for x1 in itertools.product(range(4), repeat=3):
        for x2 in itertools.product(range(4), repeat=3):
            if x1 == x2:
                continue
            d = sub(x1, x2)
            out = pi(d) * (r1[d] * sum(1 for e in E6 if md(add(x1, e)) != x2) + r2[d] * sum(1 for e in E6 if md(add(x2, e)) != x1))
            inn = sum(pi(sub(md(add(x1, e)), x2)) * r1[sub(md(add(x1, e)), x2)] for e in E6 if md(add(x1, e)) != x2)
            inn += sum(pi(sub(x1, md(add(x2, e)))) * r2[sub(x1, md(add(x2, e)))] for e in E6 if md(add(x2, e)) != x1)
            bal &= out == inn
            if not bal:
                break
    ok &= bal
    # with r_i = the rate at record i's site: first order of log(r1 + r2) is the MEAN of the two sources
    s_, m1, m2 = sp.symbols("s mu1 mu2")
    G0 = sp.Rational(G[(0, 0, 0)].numerator, G[(0, 0, 0)].denominator)
    dd = (2, 1, 0)
    Gd = sp.Rational(G[dd].numerator, G[dd].denominator)
    rr = sp.exp(6 * s_ * m1 * G0 + 6 * s_ * m2 * Gd) + sp.exp(6 * s_ * m2 * G0 + 6 * s_ * m1 * Gd)
    ok &= sp.simplify(sp.series(sp.log(rr), s_, 0, 2).removeO() - (sp.log(2) + 3 * s_ * (m1 + m2) * (G0 + Gd))) == 0
    # a < 1: the two records' mean velocities at separation d do not cancel at first order
    aa = a
    def vel(me, other, lm, lo):
        v = [0, 0, 0]
        for e in E6:
            t = md(add(me, e))
            lw = 6 * s_ * (lm * sp.Rational(G[sub(t, me)].numerator, G[sub(t, me)].denominator)
                           + lo * sp.Rational(G[sub(t, other)].numerator, G[sub(t, other)].denominator))
            lw0 = 6 * s_ * (lm * G0 + lo * sp.Rational(G[sub(me, other)].numerator, G[sub(me, other)].denominator))
            for k in range(3):
                v[k] += sp.Rational(e[k], 12) * sp.exp(aa * lw0 + (1 - aa) * lw)
        return v
    p1, p2 = (2, 1, 0), (0, 0, 0)
    vs = [sp.series(v1 + v2, s_, 0, 2).removeO() for v1, v2 in zip(vel(p1, p2, m1, m2), vel(p2, p1, m2, m1))]
    grad = [sum(e[k] * G[md(add(sub(p1, p2), e))] for e in E6) for k in range(3)]
    ok &= all(sp.simplify(vs[k] - s_ * (1 - aa) / 2 * (m2 - m1) * sp.Rational(grad[k].numerator, grad[k].denominator)) == 0
              for k in range(3)) and any(gk != 0 for gk in grad)
    check("C", ok, "4^3 torus, block 95's G (257/7680, 29/7680, defining identity at all 64 offsets): the four-move cycle of two records "
          f"has log(forward/backward) = 6(2a - 1)(lambda2 - lambda1) Delta, Delta = {Dl} here; at a = 1, 1/(r1(d) + r2(d)) is stationary "
          "for any rates (4032 states), and its first order is 3(lambda1 + lambda2)(G(0) + G(d)); the two mean velocities at d = (2,1,0) "
          "sum to (1 - a)(lambda2 - lambda1)/2 sum_e e G(d + e) at first order, a symbolic")


def main() -> int:
    family_q()
    G = green()
    family_k(G)
    res = family_f(G)
    family_s(G, res)
    family_t(G, res)
    family_m(G)
    family_c()
    print("The rest energy of a record - checks; worker w-macbookpro9927a-j7968 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PARTIAL exact under the stated formation clause (block 58's event, the ledger kept, the record a body at rest of block 56): "
          "the record's bare energy is m' = L/(1 - (gamma/12) g_y L), L the ledger of the amplitude it came from (rest and motion alike), its "
          "clock phi_y = 1 - (gamma/12) g_y L, and in block 53's clause with block 56's mean kappa = (1 + gamma m'/12)^-2 = "
          "[(1 - (gamma/12)g_yL)/(1 - (gamma/12)(g_y - 1)L)]^2; the record's content enters none of these; kappa is one number for all "
          "records only if every formation converts the same L at sites of equal g_y; for one species at rest log kappa = -(gamma/6)m - "
          "(gamma m)^2 (2(g_y - <G>_p) - 1)/144 + O(gamma^3), so it depends on the amplitude's spread; block 95's chain with two kappas "
          "has a four-move cycle of log-ratio 6(2a - 1)(lambda2 - lambda1) Delta")
    print("HIT: under a stated formation clause (block 58's event with the ledger kept) a record's rest energy is set by the converted "
          "ledger L and the site alone: m' = L/(1 - (gamma/12) g_y L), kappa = (1 + gamma m'/12)^-2 exactly in block 56's law; it is "
          "content-blind, but one kappa for all records needs one L per formation, and block 95's pair law needs one kappa")
    return 0


if __name__ == "__main__":
    sys.exit(main())
