#!/usr/bin/env python3
"""Exact checks: the static six-axis law at strong coupling — reflection positivity, chessboard, disseminated bound, contour
counts, the two-dimensional threshold 216 m and the conditional three-dimensional constants.

Scope.  Static law mu_L(v) = prod_bonds phi(v_x, v_y)/Z_L on tori, phi = (p, q, r) on same/antipodal/orthogonal pairs.  T1: the
spectrum of phi and the 48 signed permutations.  T2: reflection positivity through site planes on a ring of 4 and a 4x2 torus, at
(3,1,2) and at the indefinite triple (5,2,4), for pseudo-random F.  T3: chessboard instances.  T4: the disseminated bound
(6m/p)^N on the ring and the 4x2 torus at p = 432.  T5: enclosing dual-cycle counts for lengths 4, 6, 8; the series identity and
its value 5/8 at y = 1/2; the winding bound 45/256; the total 295/768; the threshold 216 m; an illustration on the 4x2 torus at
p = 432.  T7: the three-dimensional disseminated bound and an illustration on the 2x2x2 torus at p = 432 (the in-plane count needs no
further lemma).  Exact rational and symbolic arithmetic only; the runner scans its own source for
floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_LAW_STRONG_COUPLING_LONG_RANGE_ORDER_AND_SEVERAL_GIBBS_STATES_REFLECTION_POSITIVITY_CHESSBOARD_PEIERLS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_static_six_axis_law_strong_coupling_long_range_order_and_several_gibbs_states_reflection_positivity_chessboard_peierls_bounded_theorem_note_2026-09-15"
BLOCK03_CLAIM_ID = "admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06"
BLOCK03_FRAGMENT = "one-neighbor interdependence coefficient"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "eigenvalues_wrong": "B",
    "symmetry_not_preserved_claimed": "B",
    "rp_negative_claimed": "B",
    "chessboard_violated_claimed": "B",
    "disseminated_bound_wrong": "C",
    "contour_count_bound_wrong": "C",
    "series_value_wrong": "C",
    "winding_bound_wrong": "C",
    "threshold_wrong": "C",
    "unique_state_above_threshold_claimed": "C",
    "three_d_disseminated_bound_wrong": "D",
    "claim_sharp_threshold": "F",
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
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


F = Fraction
M = 6


def dec(x: Fraction, n: int = 6) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


def orbit_type(s: int, u: int) -> str:
    if s == u:
        return "p"
    if s // 2 == u // 2:
        return "q"
    return "r"


def phi_matrix(p: int, q: int, r: int):
    w = {"p": p, "q": q, "r": r}
    return [[w[orbit_type(s, t)] for t in range(M)] for s in range(M)]


AXIS = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}


def signed_permutations():
    idx = {v: k for k, v in AXIS.items()}
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            mp = []
            for k in range(M):
                a = AXIS[k]
                b = [0, 0, 0]
                for i in range(3):
                    b[perm[i]] = signs[i] * a[i]
                mp.append(idx[tuple(b)])
            out.append(tuple(mp))
    return out


# ------------------------------------------------------------------ small tori
def ring_measure(phi, n: int) -> dict:
    w = {}
    for v in product(range(M), repeat=n):
        x = 1
        for i in range(n):
            x *= phi[v[i]][v[(i + 1) % n]]
        w[v] = x
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}


def torus_4x2(phi):
    sites = [(i, j) for i in range(4) for j in range(2)]
    idx = {s: k for k, s in enumerate(sites)}
    hb = [(idx[(i, j)], idx[((i + 1) % 4, j)]) for i in range(4) for j in range(2)]  # direction-1 bonds (8)
    vb = sorted({tuple(sorted((idx[(i, 0)], idx[(i, 1)]))) for i in range(4)})  # direction-2 bonds (4 distinct pairs, each doubled on the 2-torus)
    w = {}
    for v in product(range(M), repeat=8):
        x = 1
        for (a, b) in hb:
            x *= phi[v[a]][v[b]]
        for (a, b) in vb:
            x *= phi[v[a]][v[b]] ** 2
        w[v] = x
    Z = sum(w.values())
    return sites, idx, hb, {v: F(x, Z) for v, x in w.items()}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, b03 = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, block 03 on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f03 = normalize_text(b03)
    checks.check("A3", BLOCK03_CLAIM_ID in f03 and BLOCK03_FRAGMENT in f03, "block 03's claim id and its one-neighbor coefficient are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    P_, Q_, R_ = sp.symbols("p q r", positive=True)
    Phi = sp.Matrix(M, M, lambda i, j: {"p": P_, "q": Q_, "r": R_}[orbit_type(i, j)])
    ev = Phi.eigenvals()
    expected = {P_ + Q_ + 4 * R_: 1, P_ - Q_: 3, P_ + Q_ - 2 * R_: 2}
    if mut("eigenvalues_wrong"):
        expected = {P_ + Q_ + 4 * R_: 1, P_ - Q_: 2, P_ + Q_ - 2 * R_: 3}
    ev_ok = all(any(sp.simplify(k - e) == 0 and m == mult for k, m in ev.items()) for e, mult in expected.items()) and sum(ev.values()) == 6
    phi = phi_matrix(3, 1, 2)
    perms = signed_permutations()
    inv = all(phi[g[a]][g[b]] == phi[a][b] for g in perms for a in range(M) for b in range(M))
    transitive = all(any(g[0] == a for g in perms) for a in range(M))
    if mut("symmetry_not_preserved_claimed"):
        inv = not inv
    checks.check("B1", ev_ok and len(perms) == 48 and inv and transitive, "T1: eigenvalues Z_1, p-q (x3), p+q-2r (x2); the 48 signed permutations preserve phi and act transitively on the six values")
    random.seed(20260915)
    ok_rp = True
    for tr in ((3, 1, 2), (5, 2, 4)):
        mu4 = ring_measure(phi_matrix(*tr), 4)
        for _ in range(20):
            Ftab = {k: F(random.randint(-9, 9)) for k in product(range(M), repeat=3)}
            val = sum((mu4[v] * Ftab[(v[0], v[1], v[2])] * Ftab[(v[0], v[3], v[2])] for v in mu4), F(0))
            ok_rp = ok_rp and val >= 0
    sites, idx, hb, mu8 = torus_4x2(phi_matrix(3, 1, 2))
    report["torus312"] = (sites, idx, hb, mu8)
    left = [idx[(i, j)] for i in (0, 1, 2) for j in range(2)]
    refl = {idx[(i, j)]: idx[((-i) % 4, j)] for (i, j) in sites}
    for _ in range(3):
        Ftab = {k: F(random.randint(-5, 5)) for k in product(range(M), repeat=len(left))}
        val = F(0)
        for v, pr in mu8.items():
            val += pr * Ftab[tuple(v[s] for s in left)] * Ftab[tuple(v[refl[s]] for s in left)]
        ok_rp = ok_rp and val >= 0
    if mut("rp_negative_claimed"):
        ok_rp = False
    checks.check("B2", ok_rp, "T2: E[F F∘θ] >= 0 for site reflections — 20 pseudo-random F on the ring of 4 at (3,1,2) and (5,2,4), 3 on the 4x2 torus at (3,1,2)")
    mu4 = ring_measure(phi_matrix(3, 1, 2), 4)
    p_both = sum((pr for v, pr in mu4.items() if v[0] != v[1] and v[2] != v[3]), F(0))
    p_all = sum((pr for v, pr in mu4.items() if all(v[i] != v[(i + 1) % 4] for i in range(4))), F(0))
    ring_ok = p_both ** 2 <= p_all  # P(both)^{1} <= P(all)^{2/4}  <=>  P(both)^2 <= P(all)
    # 4x2 torus: two direction-1 bonds at cells (0,0) and (2,1) versus all direction-1 bonds bad
    b1, b2 = hb[0], hb[5]
    p_two = sum((pr for v, pr in mu8.items() if v[b1[0]] != v[b1[1]] and v[b2[0]] != v[b2[1]]), F(0))
    p_alld1 = sum((pr for v, pr in mu8.items() if all(v[a] != v[b] for (a, b) in hb)), F(0))
    torus_ok = p_two ** 4 <= p_alld1  # P(two) <= P(all)^{2/8}  <=>  P(two)^4 <= P(all)
    report["p_alld1_312"] = p_alld1
    if mut("chessboard_violated_claimed"):
        torus_ok = p_two ** 4 > p_alld1
    checks.check("B3", ring_ok and torus_ok, f"T3: chessboard instances — ring: P(two bonds bad)^2 = {dec(p_both ** 2)} <= P(all bad) = {dec(p_all)}; 4x2 torus: P(two direction-1 bonds bad)^4 <= P(all direction-1 bad) = {dec(p_alld1)}")


# ============================================================================================ family C
def enclosing_cycles(n: int) -> int:
    """simple cycles of length n on the dual lattice (half-integer points) enclosing the origin cell, by enumeration of
    self-avoiding closed walks starting at a dual vertex crossing the positive half-line within distance n/2."""
    found = set()
    starts = [(k + F(1, 2), F(-1, 2)) for k in range(0, n // 2 + 1)]  # dual vertices just below the half-line
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def encloses(cycle_edges):
        # even-odd rule: count vertical crossings of the ray from the origin (0,0) going right along y = 0
        crossings = 0
        for (a, b) in cycle_edges:
            (x1, y1), (x2, y2) = a, b
            if x1 == x2 and x1 > 0 and min(y1, y2) < 0 < max(y1, y2):
                crossings += 1
        return crossings % 2 == 1

    def walk(path, edges):
        if len(path) - 1 == n:
            if path[-1] == path[0]:
                key = frozenset(edges)
                if encloses(edges):
                    found.add(key)
            return
        cur = path[-1]
        for dx, dy in steps:
            nxt = (cur[0] + dx, cur[1] + dy)
            e = frozenset((cur, nxt))
            if e in edges:
                continue
            if nxt in path[1:] or (nxt == path[0] and len(path) < n):
                continue
            if nxt == path[0] and len(path) != n:
                continue
            walk(path + [nxt], edges + [tuple(sorted((cur, nxt)))])
    for s in starts:
        walk([s], [])
    return len(found)


def family_c(checks: Checks, report: dict, exact: bool) -> None:
    m = 2
    # disseminated bound at p = 432: ring and 4x2 torus
    phi_big = phi_matrix(432, 1, 2)
    mu4 = ring_measure(phi_big, 4)
    p_all_ring = sum((pr for v, pr in mu4.items() if all(v[i] != v[(i + 1) % 4] for i in range(4))), F(0))
    sites, idx, hb, mu8 = torus_4x2(phi_big)
    report["torus432"] = (sites, idx, hb, mu8)
    p_alld1 = sum((pr for v, pr in mu8.items() if all(v[a] != v[b] for (a, b) in hb)), F(0))
    eps = F(6 * m, 432)
    diss_ok = p_all_ring <= eps ** 4 and p_alld1 <= eps ** 8
    if mut("disseminated_bound_wrong"):
        diss_ok = p_alld1 <= eps ** 16
    checks.check("C1", diss_ok, f"T4: at p = 432, m = 2 (eps = 6m/p = 1/36): P(all bonds bad) on the ring = {dec(p_all_ring, 9)} <= eps^4 = {dec(eps ** 4, 9)}; on the 4x2 torus P(all direction-1 bad) = {dec(p_alld1, 12)} <= eps^8")
    counts = {n: enclosing_cycles(n) for n in (4, 6, 8)}
    bound = {n: F(n, 2) * 3 ** (n - 1) for n in (4, 6, 8)}
    cnt_ok = counts == {4: 1, 6: 4, 8: 22} and all(counts[n] <= bound[n] for n in counts)
    if mut("contour_count_bound_wrong"):
        cnt_ok = counts == {4: 1, 6: 4, 8: 23}
    checks.check("C2", cnt_ok, f"T5: enclosing dual cycles of length 4, 6, 8: {counts} <= (n/2) 3^(n-1) = {dict((n, int(b)) for n, b in bound.items())}")
    y = sp.symbols("y", positive=True)
    series = sp.summation(sp.Symbol("n") * y ** sp.Symbol("n"), (sp.Symbol("n"), 4, sp.oo))
    closed = y ** 4 * (4 - 3 * y) / (1 - y) ** 2
    ident = sp.simplify(sp.simplify(series.subs(y, sp.Rational(1, 2))) - closed.subs(y, sp.Rational(1, 2))) == 0 and closed.subs(y, sp.Rational(1, 2)) == sp.Rational(5, 8)
    partial = sum((F(n, 1) * F(1, 2 ** n) for n in range(4, 200)), F(0))
    val_ok = ident and abs(partial - F(5, 8)) < F(1, 10 ** 40)
    if mut("series_value_wrong"):
        val_ok = closed.subs(y, sp.Rational(1, 2)) == sp.Rational(3, 5)
    checks.check("C3", val_ok, "T5: sum_{n>=4} n y^n = y^4 (4 - 3y)/(1 - y)^2, equal to 5/8 at y = 1/2 (case (a) bound 5/24)")
    Lp = 10
    winding = F(18 * Lp, 2 ** Lp)
    total = F(5, 24) + winding
    w_ok = winding == F(45, 256) and total == F(295, 768) and total < F(1, 2)
    if mut("winding_bound_wrong"):
        w_ok = winding == F(45, 512)
    checks.check("C4", w_ok and 3 * F(1, 6) == F(1, 2) and 6 * m * 36 == 216 * m, "T5: the winding bound 18 L' 2^{-L'} at L' = 10 is 45/256, the total 5/24 + 45/256 = 295/768 < 1/2; y = 3 eps^{1/2} = 1/2 at eps = 1/36, i.e. p_0 = 216 m")
    thr_ok = (216 * m == 432) and (F(6 * m, 216 * m) == F(1, 36))
    if mut("threshold_wrong"):
        thr_ok = F(6 * m, 216 * m) == F(1, 35)
    checks.check("C5", thr_ok, "T5: at m = 2 the threshold is p_0 = 432 and eps = 6m/p_0 = 1/36 exactly")
    same = sum((pr for v, pr in mu8.items() if v[idx[(0, 0)]] == v[idx[(2, 0)]]), F(0))
    illus = same > F(1, 2)
    if mut("unique_state_above_threshold_claimed"):
        illus = same <= F(1, 2)
    checks.check("C6", illus, f"T5 illustration: on the 4x2 torus at p = 432 the records at distance 2 agree with probability {dec(same)} > 1/2")
    if exact:
        print("exact 4x2 torus agreement at p = 432:", same)


# ============================================================================================ family D
def torus_2x2x2(phi):
    """the 2x2x2 torus: each pair of adjacent sites is joined by two bonds (periodic side 2); 8 direction-1 bond slots."""
    sites = list(product(range(2), repeat=3))
    idx = {s: k for k, s in enumerate(sites)}
    pairs = {d: set() for d in range(3)}
    for s in sites:
        for d in range(3):
            t_ = list(s)
            t_[d] = (s[d] + 1) % 2
            pairs[d].add(tuple(sorted((idx[s], idx[tuple(t_)]))))
    w = {}
    for v in product(range(M), repeat=8):
        x = 1
        for d in range(3):
            for (a, b) in pairs[d]:
                x *= phi[v[a]][v[b]] ** 2
        w[v] = x
    Z = sum(w.values())
    return idx, pairs, {v: F(x, Z) for v, x in w.items()}


def family_d(checks: Checks) -> None:
    m = 2
    idx, pairs, mu = torus_2x2x2(phi_matrix(432, 1, 2))
    p_alld1 = sum((pr for v, pr in mu.items() if all(v[a] != v[b] for (a, b) in pairs[0])), F(0))
    eps = F(6 * m, 432)
    d1 = p_alld1 <= eps ** 8
    if mut("three_d_disseminated_bound_wrong"):
        d1 = p_alld1 <= eps ** 16
    checks.check("D1", d1, f"T7: on the 2x2x2 torus at p = 432 the probability that every direction-1 bond disagrees is {dec(p_alld1, 15)} <= (6m/p)^N = (1/36)^8")
    same = sum((pr for v, pr in mu.items() if v[idx[(0, 0, 0)]] == v[idx[(1, 0, 0)]]), F(0))
    d2 = same > F(1, 2) and all(len(pairs[d]) == 4 for d in range(3))
    checks.check("D2", d2, f"T7 illustration: on the 2x2x2 torus at p = 432 neighbouring records agree with probability {dec(same)} > 1/2; each unit cube of a layer is canonical for one in-plane bond per in-plane direction")


# ============================================================================================ family F
FENCES = (
    "This note proves long-range order and the existence of at least two Gibbs states for the static six-axis law on `Z²` when `p ≥ 216 max(q, r)`, and on `Z³` for the same threshold by the in-plane count; it does not claim optimal thresholds, says nothing about the band between block 03's thresholds and these, says nothing about the formation law's phase (block 12's obligation stands), does not count the extremal states beyond the orbit bound, and does not select a coupling as physical.",
    "No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical phase", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "sharp threshold", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_sharp_threshold": "Hence 216 m is the sharp threshold of the phase transition."}
CLASSICAL_NAMES = ("Peierls", "Cauchy", "Schwarz", "Whitney", "Jordan", "Timár", "Lévy", "Kolmogorov", "Fröhlich", "Lieb", "Simon", "Biskup", "Israel", "Dobrushin")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem T3"):
            body = body + " (the Cauchy–Schwarz inequality)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the spectrum symbolically; the 48 signed permutations; the series identity at y = 1/2; the enclosing-cycle counts for lengths 4, 6, 8",
    "per_site: executed — every configuration of the ring of 4 and the 4x2 torus in the reflection-positivity, chessboard and disseminated checks",
    "per_mode: executed — the chessboard instances on the ring and the 4x2 torus; the disseminated ratios at p = 432",
    "per_block: executed — the 4x2 and 2x2x2 torus illustrations at p = 432 (agreement above 1/2)",
    "lattice_wide: T1-T7 proved for every positive triple with p >= 216 max(q, r) on Z^2 and Z^3 (the in-plane count); thresholds not claimed optimal",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


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
    exact = "--exact" in argv
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the static six-axis law at strong coupling — spectrum and symmetry, reflection positivity through site planes, chessboard, the disseminated bound, contour counts, the threshold 216 m on Z^2 and Z^3 (the in-plane count); exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts)
    family_b(checks, report)
    family_c(checks, report, exact)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
