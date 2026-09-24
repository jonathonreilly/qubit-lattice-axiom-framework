#!/usr/bin/env python3
"""Exact checks: no master clock (a supplied clause for local tick rates on Z^3; not adopted).

CLAUSE: every site has a positive tick rate w_x; the rate at a site is determined by the rates at its six nearest neighbours by one rule,
covariant under translations and proper cubic rotations, and SCALE COVARIANT: multiplying every rate by t multiplies the answer by t, because
without a master clock only ratios of rates mean anything.
T1 (linear laws): a linear nearest-neighbour law for u = log w that is covariant and admits the shift u -> u + const is
   c_0 (u_x - (1/6) sum of the six neighbours) = s_x: the lattice Laplace equation (the 24 rotations are transitive on the six directions and
   fix only the constant coefficient vector).
T2 (any law): a symmetric function F of the six neighbouring rates, homogeneous of degree one, with F(1,...,1) = 1 (uniform empty space is a
   solution), has all six first derivatives equal to 1/6 at the uniform point: every such law linearizes to T1.  The second order is not universal.
   The geometric mean is exactly linear in u.  The product of the six rates (degree six) is not scale covariant, and its symbol 1 - 2 sum cos k_i
   changes sign.
T3 (zero mode): on a torus the Laplace operator has rank L^3 - 1; a source is admissible iff it sums to zero, and u is fixed up to a constant.
T4 (records): a clause that pins a record's rate at an absolute value is not scale covariant; the selected geometric-mean clause uses fixed ratio kappa and gives additive log sources; general homogeneous rules need not be log-linear.
T5 (a test record): if a record's symmetric hops are timed by the clock of the site it sits on, its stationary law is proportional to 1/w.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "covariance_under_one_axis_only": "B",
    "shift_not_required": "B",
    "product_law_is_scale_covariant": "C",
    "second_order_is_universal": "C",
    "torus_law_has_full_rank": "D",
    "pinned_rate_is_scale_covariant": "E",
    "sources_do_not_add": "E",
    "hops_timed_by_the_bond": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


F = Fraction
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def proper_rotations():
    """The 24 signed permutation matrices of determinant +1, as maps on integer vectors."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            parity = 1
            p = list(perm)
            for i in range(3):
                for j in range(i + 1, 3):
                    if p[i] > p[j]:
                        parity = -parity
            if parity * signs[0] * signs[1] * signs[2] == 1:
                out.append((perm, signs))
    return out


def rotate(g, v):
    perm, signs = g
    return tuple(signs[i] * v[perm[i]] for i in range(3))


def rank(rows):
    rows = [[F(c) for c in r] for r in rows]
    rk = 0
    ncols = len(rows[0]) if rows else 0
    for col in range(ncols):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][col]
        rows[rk] = [c / pv for c in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [a - fac * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def solve(a, b):
    """Solve a x = b exactly; returns one solution or None (free variables set to zero)."""
    n, m = len(a), len(a[0])
    rows = [[F(c) for c in a[i]] + [F(b[i])] for i in range(n)]
    pivots = []
    rk = 0
    for col in range(m):
        piv = next((i for i in range(rk, n) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][col]
        rows[rk] = [c / pv for c in rows[rk]]
        for i in range(n):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[rk])]
        pivots.append(col)
        rk += 1
    if any(all(c == 0 for c in r[:-1]) and r[-1] != 0 for r in rows):
        return None
    x = [F(0)] * m
    for i, col in enumerate(pivots):
        x[col] = rows[i][-1]
    return x


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the covariance sentence and says that Admissibility does not define a time metric")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    rots = proper_rotations()
    if mut("covariance_under_one_axis_only"):
        rots = [g for g in rots if rotate(g, (0, 0, 1)) == (0, 0, 1)]
    orbit = {rotate(g, E[0]) for g in rots}
    # coefficient vectors on the six directions that every rotation leaves unchanged: the null space of the stacked (P_g - 1)
    rows = []
    for g in rots:
        for j, e in enumerate(E):
            row = [0] * 6
            row[E.index(rotate(g, e))] += 1
            row[j] -= 1
            rows.append(row)
    fixed_dim = 6 - rank(rows)
    checks.check("B1", len(proper_rotations()) == 24 and len(orbit) == 6 and fixed_dim == 1, f"T1: the 24 proper rotations of the cube are transitive on the six nearest-neighbour directions (orbit of one direction: {len(orbit)}) and leave a {fixed_dim}-dimensional space of coefficient vectors unchanged: a covariant linear nearest-neighbour law has one coefficient c_1 for all six neighbours")
    # shift symmetry: constants solve the homogeneous law c_0 u_x + c_1 sum u_y = 0 iff c_0 + 6 c_1 = 0
    ok = True
    for c0 in (F(1), F(-3, 2), F(7, 5)):
        c1 = -c0 / 6
        if mut("shift_not_required"):
            c1 = -c0 / 5
        ok = ok and c0 + 6 * c1 == 0
        # then the law is c_0 (u_x - (1/6) sum u_y): check on a random field at one site
        u = {e: F(k + 2, 3) for k, e in enumerate(E)}
        ux = F(5, 7)
        ok = ok and c0 * ux + c1 * sum(u.values()) == c0 * (ux - sum(u.values()) / 6)
    checks.check("B2", ok, "T1: such a law admits the shift u -> u + const iff c_0 + 6 c_1 = 0, and then it is c_0 (u_x - (1/6) sum over the six neighbours) = s_x: minus c_0/6 times the lattice Laplace operator")


# ============================================================================================ family C (T2)
class Dual:
    """a + b eps with eps^2 = 0 over the rationals: exact first derivatives."""

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, Dual) else Dual(o)
        return Dual(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __mul__(self, o):
        o = o if isinstance(o, Dual) else Dual(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, Dual) else Dual(o)
        return Dual(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))

    def __rtruediv__(self, o):
        return Dual(o) / self


def arithmetic(w):
    return sum(w, Dual(0)) / 6


def harmonic(w):
    return 6 / sum((1 / x for x in w), Dual(0))


def contraharmonic(w):
    return sum((x * x for x in w), Dual(0)) / sum(w, Dual(0))


def pair_ratio(w):
    e2 = Dual(0)
    for i in range(6):
        for j in range(i + 1, 6):
            e2 = e2 + w[i] * w[j]
    return F(2, 5) * e2 / sum(w, Dual(0))


def product_of_six(w):
    out = Dual(1)
    for x in w:
        out = out * x
    return out


MEANS = {"arithmetic": arithmetic, "harmonic": harmonic, "contraharmonic": contraharmonic, "pair ratio (2/5) e_2/e_1": pair_ratio}


def partials(f, point):
    out = []
    for i in range(6):
        w = [Dual(point[j], 1 if j == i else 0) for j in range(6)]
        out.append(f(w).b)
    return out


def family_c(checks: Checks) -> None:
    rots = proper_rotations()
    perms = []
    for g in rots:
        perms.append([E.index(rotate(g, e)) for e in E])
    uniform = [F(3, 2)] * 6
    generic = [F(1, 2), F(2), F(3, 4), F(5, 3), F(1), F(7, 6)]
    ok = True
    shown = []
    laws = dict(MEANS)
    if mut("product_law_is_scale_covariant"):
        laws["product of the six rates"] = product_of_six
    for name, f in laws.items():
        val = f([Dual(x) for x in generic]).a
        sym = all(f([Dual(generic[p[j]]) for j in range(6)]).a == val for p in perms)
        t = F(7, 3)
        hom = f([Dual(t * x) for x in generic]).a == t * val
        at_one = f([Dual(1)] * 6).a == 1
        d_uni = partials(f, uniform)
        d_gen = partials(f, generic)
        euler = sum(generic[i] * d_gen[i] for i in range(6)) == val
        ok = ok and sym and hom and at_one and euler and all(d == F(1, 6) for d in d_uni)
        shown.append(name)
    checks.check("C1", ok, "T2: for four rational laws (" + "; ".join(shown) + "): symmetric under the 24 rotations, homogeneous of degree one, equal to one on uniform rates; the sum of w_i dF/dw_i equals F at a generic rational point, and at the uniform point all six first derivatives equal 1/6: every such law linearizes to u_x = (1/6) sum over the six neighbours")
    # second order is not universal: one neighbour up by delta, the opposite one down by delta
    delta = F(1, 10)
    bumped = [1 + delta, 1 - delta, F(1), F(1), F(1), F(1)]
    second = {name: f([Dual(x) for x in bumped]).a - 1 for name, f in MEANS.items()}
    distinct = len(set(second.values())) == len(second) and second["arithmetic"] == 0
    if mut("second_order_is_universal"):
        distinct = len(set(second.values())) == 1
    checks.check("C2", distinct and list(second.values()) == [F(0),F(-1,298),F(1,300),F(-1,1500)], "T2: the second order is not universal: with one neighbour at 11/10 and the opposite one at 9/10 the laws give 1 + " + ", ".join(f"{v}" for v in second.values()) + ": the weak-field equation is forced, its non-linear completion is not")
    # the geometric mean on sixth powers: exact, multiplicative (that is, linear in u = log w)
    a = [2, 3, 1, 5, 2, 7]
    b = [3, 1, 4, 2, 5, 1]

    def geometric(v):
        prod = 1
        for x in v:
            prod *= x
        return prod                                                  # the sixth root of the product of sixth powers

    # the lists hold the sixth roots of the rates: multiplying every rate by t = 4^6 multiplies every root by 4 and the mean by 4^6 = t (degree one)
    ok = geometric([x * y for x, y in zip(a, b)]) == geometric(a) * geometric(b) and geometric([4 * x for x in a]) == 4 ** 6 * geometric(a) and geometric([3] * 6) == 3 ** 6
    # symbols: averaging law 1 - (1/3) sum cos k_i >= 0 with a zero only at k = 0; product law 1 - 2 sum cos k_i changes sign.  cos takes the values 1, 0, -1 on a torus of side 4
    avg_vals = {1 - F(1, 3) * sum(c) for c in product((1, 0, -1), repeat=3)}
    prod_vals = {1 - 2 * sum(c) for c in product((1, 0, -1), repeat=3)}
    ok = ok and min(avg_vals) == 0 and sum(1 for c in product((1, 0, -1), repeat=3) if 1 - F(1, 3) * sum(c) == 0) == 1 and min(prod_vals) < 0 < max(prod_vals)
    checks.check("C3", ok, f"T2: the geometric mean is multiplicative, that is exactly linear in u = log w; the symbol of the averaging law on a torus of side 4 is non-negative with a single zero at k = 0, while the product of the six rates (degree six, not scale covariant) has the symbol 1 - 2 sum cos k_i, from {min(prod_vals)} to {max(prod_vals)}: it changes sign")


# ============================================================================================ family D (T3)
def torus_operator(side):
    sites = list(product(range(side), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    a = [[F(0)] * len(sites) for _ in sites]
    for x in sites:
        a[idx[x]][idx[x]] += 1
        for e in E:
            y = tuple((x[i] + e[i]) % side for i in range(3))
            a[idx[x]][idx[y]] -= F(1, 6)
    return sites, idx, a


def family_d(checks: Checks) -> None:
    sites, idx, a = torus_operator(3)
    rk = rank(a)
    want = len(sites) if mut("torus_law_has_full_rank") else len(sites) - 1
    s_bad = [F(0)] * len(sites)
    s_bad[idx[(0, 0, 0)]] = F(1)
    s_good = list(s_bad)
    s_good[idx[(1, 2, 0)]] = F(-1)
    sol_bad, sol_good = solve(a, s_bad), solve(a, s_good)
    ok = rk == want and sol_bad is None and sol_good is not None
    if sol_good is not None:
        shifted = [v + F(5, 3) for v in sol_good]
        resid = [sum(a[i][j] * shifted[j] for j in range(len(sites))) - s_good[i] for i in range(len(sites))]
        ok = ok and all(r == 0 for r in resid)
    checks.check("D1", ok, f"T3: on the 3x3x3 torus the operator u_x - (1/6) sum of neighbours has rank {rk} = 27 - 1; a source that sums to one has no solution, a source that sums to zero has one, and adding a constant to it gives another: only the part of the source with zero sum enters, and u is fixed up to the unobservable constant")


# ============================================================================================ family E (T4, T5)
def family_e(checks: Checks) -> None:
    # pins against ratios under w -> t w (u -> u + k)
    k = F(2, 3)
    u_nb = [F(1, 2), F(-1, 3), F(0), F(1, 4), F(2, 5), F(-1, 6)]
    avg = sum(u_nb) / 6
    log_kappa = F(-3, 10)
    ratio_law_before = (avg + log_kappa) - avg - log_kappa            # u_x - avg - log kappa with u_x = avg + log kappa
    ratio_law_after = (avg + log_kappa + k) - (avg + k) - log_kappa
    pinned_value = F(1, 7)
    pin_before = pinned_value - pinned_value
    pin_after = (pinned_value + k) - pinned_value
    pin_covariant = pin_after == 0
    if mut("pinned_rate_is_scale_covariant"):
        pin_covariant = True
    checks.check("E1", ratio_law_before == 0 and ratio_law_after == 0 and pin_before == 0 and not pin_covariant, "T4: the clause 'a record's rate is kappa times the mean of its neighbours' rates' is unchanged when every rate is multiplied by t; the clause 'a record's rate is a fixed number' is not: the tested relative clause is covariant; source log kappa is exact only for the selected geometric-mean/log-linear completion")
    # exact additivity on the 4x4x4 torus (sources projected to zero sum)
    sites, idx, a = torus_operator(4)
    n = len(sites)
    recs = [(0, 0, 0), (2, 1, 0), (1, 3, 2)]

    def potential(rec_list):
        s = [F(0)] * n
        for x in rec_list:
            s[idx[x]] += log_kappa
        mean = sum(s) / n
        s = [v - mean for v in s]
        sol = solve(a, s)
        m = sum(sol) / n
        return [v - m for v in sol]

    single = [potential([x]) for x in recs]
    together = potential(recs)
    summed = [sum(single[j][i] for j in range(len(recs))) for i in range(n)]
    if mut("sources_do_not_add"):
        summed = [v * F(9, 10) for v in summed]
    sym = single[0][idx[recs[1]]] == single[1][idx[recs[0]]]
    checks.check("E2", together == summed and sym and single[0][idx[recs[0]]] == F(-4551,12800), f"T4: on the 4x4x4 torus the field of three records is exactly the sum of their single fields, the field of one record at the site of another equals the converse (the pair term is symmetric), and with kappa < 1 the field is lowest at the record (u = {single[0][idx[recs[0]]]} there, mean zero): clocks run slow near records, and sources add whatever their arrangement")
    # a test record whose symmetric hops are timed by the clock of the site it sits on: stationary law proportional to 1/w
    w = {x: F(1) + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in product(range(3), repeat=3)}
    sites3 = list(w)
    stat = {x: 1 / w[x] for x in sites3}
    ok = True
    for x in sites3:
        out = stat[x] * w[x]
        inn = F(0)
        for e in E:
            y = tuple((x[i] + e[i]) % 3 for i in range(3))
            rate = w[y] if not mut("hops_timed_by_the_bond") else (w[x] + w[y]) / 2
            inn += stat[y] * rate / 6
        if mut("hops_timed_by_the_bond"):
            out = sum(stat[x] * (w[x] + w[tuple((x[i] + e[i]) % 3 for i in range(3))]) / 2 / 6 for e in E)
        ok = ok and inn == out
    checks.check("E3", ok, "T5: a test record that hops to each neighbour at the rate w_x/6, timed by the clock of the site it sits on, has the stationary law 1/w_x = exp(-u_x) (checked on the 3x3x3 torus with a rational rate field): it is found more often where clocks run slow; residence weights do not imply a local expected displacement")

    zero_drift=all(sum((F(e[j])*w[x]/6 for e in E),F(0))==0 for x in sites3 for j in range(3))
    checks.check("E4",zero_drift,"T5: every site's conditional displacement rate is exactly zero despite nonuniform stationary residence weights")


# ============================================================================================ family F
FENCES = (
    "This note works within a supplied clause for local tick rates; it reports what field equation, what zero mode and what kind of source the clause forces; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Poisson)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[n for n in nodes if isinstance(n,ast.Constant) and isinstance(n.value,float)]
    float_hits += [n for n in nodes if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id in ('float','N')) or (isinstance(n.func,ast.Attribute) and n.func.attr in ('evalf','N')))]
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the 24 rotations, their orbit on the six directions and the one-dimensional space of invariant coefficient vectors; first derivatives of four rational laws at the uniform point, with exact dual numbers",
    "per_site: executed — the clause for a record under a change of the unit of rate: ratio law unchanged, pinned law changed; the stationary law 1/w of a test record at the 27 sites of a torus",
    "per_mode: executed — the symbols of the averaging law and of the product law on a torus of side 4",
    "per_block: executed — rank 26 of the law on the 3x3x3 torus and the solvability condition; exact additivity and symmetry of the fields of three records on the 4x4x4 torus",
    "lattice_wide: T1 and T2 are statements about every nearest-neighbour, covariant, scale-covariant law, the second at linear order; T3 and T4 are exact for the linear law on tori, and on the infinite lattice the field of finitely many records is the sum of their lattice potentials; T5 is exact for one test record; the clause itself, the value of kappa, inertia and any delay of the field are not derived",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: no master clock — a nearest-neighbour, covariant, scale-covariant law for the local tick rate linearizes to the lattice Laplace equation; the zero mode is unobservable; fixed sources superpose only in the selected log-linear model with stated background; finite stationary residence weights are inverse rates, with zero local drift")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
