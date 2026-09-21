#!/usr/bin/env python3
"""Exact checks: a formation event in the curvature member (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 58 and 60): block 60's ledger linear in the rates with the curvature member, walls held at w = l = 1, and its exact strong
field for bodies at rest: chi = 1 + sum Q_x g(., x), Q_x chi_x = m_x/(8K); N = w chi = 1 - sum P_x g(., x), P_x = Q_x w_x; ledger = 8K sum Q_x.
Block 58's question: a spread amplitude at rest, bodies m_x = m p_x on several sites (p_x = |a_x|^2), is replaced by ONE record at a site y.
T1 (the ledger can always be kept): the ledger is kept iff the record's charge is Q' = sum Q_x, that is iff its bare energy is
   m' = 8K Q'(1 + Q' g_yy); this exists for EVERY amplitude (block 58's law had a threshold); m' - m = 8K sum_xx' Q_x Q_x' (g_yy - g_xx').  If instead the
   bare energy is kept the ledger changes.
T2 (what the walls see of the lengths): for every discrete-harmonic h, sum over wall bonds of (chi_inside - 1) h(wall) = sum_x Q_x h(x).  With the
   ledger kept the monopole does not jump and the dipole jumps by Q'(y - Xbar), Xbar the centre of the CHARGES Q_x, proportional to p_x/chi_x.  Over
   ANY odds the mean jump is Q'(sum odds_y y - Xbar): zero for odds proportional to p_x/chi_x, not for p_x or p_x/chi_x^2.  (No odds are assumed.)
T3 (what the walls see of the clocks): the clocks' monopole sum P_x = sum Q_x w_x is NOT kept when the ledger is: it jumps by an amount of second
   order in the charges, -2 [Q'^2 g_yy - sum_xx' Q_x Q_x' g_xx'] + ..., that is -(m' - m)/(4K) + ...; no record keeps both far-field coefficients.
Exact arithmetic only (integers, Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_FORMATION_EVENT_IN_THE_CURVATURE_MEMBER_THE_LEDGER_CAN_ALWAYS_BE_KEPT_AND_THEN_THE_CLOCKS_FAR_FIELD_JUMPS_AT_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_formation_event_in_the_curvature_member_the_ledger_can_always_be_kept_and_then_the_clocks_far_field_jumps_at_second_order_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "record_keeps_the_bare_energy_and_the_ledger": "B",
    "ledger_has_a_threshold": "B",
    "outside_sees_the_formation_in_the_monopole": "C",
    "probability_odds_hold_the_centre": "C",
    "clocks_far_field_is_kept": "D",
    "jump_is_of_first_order": "D",
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
ZERO = F(0)
ONE = F(1)
E6 = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SIDE = 7                                                     # sites 0..6; walls at 0 and 6; 125 interior sites
ALL_SITES = list(product(range(SIDE), repeat=3))
INTERIOR = [s for s in product(range(1, SIDE - 1), repeat=3)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
K = F(3, 4)                                                  # the field energy's one number; 8K = 6


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


def add(s, e):
    return (s[0] + e[0], s[1] + e[1], s[2] + e[2])


def solve_multi(a, rhs_list):
    """Solve a x = b exactly for several right-hand sides at once; the matrix must be non-singular."""
    n = len(a)
    k = len(rhs_list)
    rows = [[F(c) for c in a[i]] + [F(r[i]) for r in rhs_list] for i in range(n)]
    for col in range(n):
        piv = next((i for i in range(col, n) if rows[i][col] != 0), None)
        if piv is None:
            raise ValueError("singular")
        rows[col], rows[piv] = rows[piv], rows[col]
        pv = rows[col][col]
        rows[col] = [c / pv for c in rows[col]]
        for i in range(n):
            if i != col and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[col])]
    return [[rows[i][n + j] for i in range(n)] for j in range(k)]


def green_columns(sources):
    """Columns of the inverse of minus the lattice Laplacian on the interior (walls held): g(., s) for each source s."""
    n = len(INTERIOR)
    a = [[ZERO] * n for _ in range(n)]
    for s in INTERIOR:
        i = INDEX[s]
        a[i][i] = F(6)
        for e in E6:
            t = add(s, e)
            if t in INDEX:
                a[i][INDEX[t]] -= 1
    rhs = []
    for s in sources:
        col = [ZERO] * n
        col[INDEX[s]] = ONE
        rhs.append(col)
    sols = solve_multi(a, rhs)
    return {s: {t: sols[j][INDEX[t]] for t in INTERIOR} for j, s in enumerate(sources)}


def val(field, t, wall=ONE):
    return field[t] if t in field else wall


def lap(field, s, wall=ONE):
    """Lattice Laplacian at s over the bonds that stay inside the box; outside the interior the field is the wall value."""
    tot = ZERO
    for e in E6:
        t = add(s, e)
        if min(t) < 0 or max(t) >= SIDE:
            continue
        tot += val(field, t, wall) - val(field, s, wall)
    return tot


def bond_form(nfield, chi):
    """-8K sum over bonds with an interior end of (N_y - N_x)(chi_y - chi_x)."""
    tot = ZERO
    for s in ALL_SITES:
        for e in E3:
            t = add(s, e)
            if max(t) >= SIDE or (s not in INDEX and t not in INDEX):
                continue
            tot += (val(nfield, t) - val(nfield, s)) * (val(chi, t) - val(chi, s))
    return -8 * K * tot


def rational_field(seed, lo=F(1, 2), spread=F(1)):
    """A deterministic positive rational field on the interior."""
    out = {}
    for s in INTERIOR:
        h = (seed * 7919 + 31 * s[0] + 57 * s[1] * s[1] + 101 * s[2] * s[0] + 13 * s[1] * s[2] * seed) % 17
        out[s] = lo + spread * F(h, 17)
    return out


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ the configurations
SPREAD = {(3, 3, 3): F(1, 2), (4, 3, 3): F(1, 3), (3, 4, 3): F(1, 5), (2, 3, 3): F(1, 4), (3, 3, 2): F(1, 6)}       # the charges Q_x of the spread amplitude
RECORD_SITE = (3, 3, 3)
WALL_SITES = [s for s in ALL_SITES if s not in INDEX]


def fields(charges, g):
    """chi, N and the rates for bodies at rest with the given charges (block 60 T4): returns chi, N, w at the bodies, P, bare energies."""
    sites = list(charges)
    chi = {s: 1 + sum((charges[b] * g[b][s] for b in sites), ZERO) for s in INTERIOR}
    masses = {b: 8 * K * charges[b] * chi[b] for b in sites}
    mat = [[(ONE if i == j else ZERO) + charges[bi] / chi[bi] * g[bj][bi] for j, bj in enumerate(sites)] for i, bi in enumerate(sites)]
    ps = solve_multi(mat, [[charges[b] / chi[b] for b in sites]])[0]
    p = {b: ps[i] for i, b in enumerate(sites)}
    nf = {s: 1 - sum((p[b] * g[b][s] for b in sites), ZERO) for s in INTERIOR}
    return chi, nf, p, masses


def stationary(chi, nf, masses):
    ok = True
    for s in INTERIOR:
        lc = lap(chi, s)
        ok = ok and masses.get(s, ZERO) + 8 * K * chi[s] * lc == 0
        ok = ok and nf[s] / chi[s] * lc + lap(nf, s) == 0
    return ok


def wall_moment(field_minus_wall, h):
    """sum over wall bonds (wall site s, interior site t) of (field_t - 1) h(s)."""
    tot = ZERO
    for s in WALL_SITES:
        for e in E6:
            t = add(s, e)
            if t in INDEX:
                tot += (field_minus_wall[t] - 1) * h(s)
    return tot


def family_b(checks: Checks):
    g = green_columns(list(SPREAD) + [(5, 3, 3)])
    chi, nf, p, masses = fields(SPREAD, g)
    q_tot = sum(SPREAD.values(), ZERO)
    m_tot = sum(masses.values(), ZERO)
    ledger_before = sum((masses[b] * nf[b] / chi[b] for b in SPREAD), ZERO) + bond_form(nf, chi)
    ok_before = stationary(chi, nf, masses) and ledger_before == 8 * K * q_tot
    y = RECORD_SITE
    rec = {y: q_tot}
    chi2, nf2, p2, masses2 = fields(rec, g)
    m_rec = masses2[y]
    ledger_after = m_rec * nf2[y] / chi2[y] + bond_form(nf2, chi2)
    extra = 8 * K * sum((SPREAD[a] * SPREAD[b] * (g[y][y] - g[a][b]) for a in SPREAD for b in SPREAD), ZERO)
    kept = ledger_after == ledger_before and stationary(chi2, nf2, masses2) and m_rec == 8 * K * q_tot * (1 + q_tot * g[y][y]) and m_rec - m_tot == extra
    if mut("record_keeps_the_bare_energy_and_the_ledger"):
        kept = kept and m_rec == m_tot
    checks.check("B1", ok_before and kept and extra > 0, f"T1: a spread amplitude at rest on five sites (charges 1/2, 1/3, 1/5, 1/4, 1/6; bare energy {about(m_tot)}; ledger 8K sum Q = {about(ledger_before)}) and the record at the centre that KEEPS the ledger: both are exact stationary points at all 125 sites; the record's charge is sum Q and its bare energy 8K Q'(1 + Q' g_yy) = {about(m_rec)}, more than the amplitude's by 8K sum Q_x Q_x' (g_yy - g_xx') = {about(extra)}")

    big = F(1000)
    m_big = 8 * K * big * (1 + big * g[y][y])
    f_at = q_tot * (1 + q_tot * g[y][y]) - m_tot / (8 * K)                                          # the record with the amplitude's bare energy has Q'' with Q''(1 + Q'' g) = m/(8K); the left side is increasing
    threshold = (m_big > 0 and f_at > 0) if not mut("ledger_has_a_threshold") else (m_big <= 0)
    checks.check("B2", threshold, f"T1: the ledger can be kept for EVERY amplitude: for sum Q = 1000 the record's bare energy is {about(m_big)}, finite (block 58's law had a threshold); if instead the record keeps the amplitude's bare energy its charge is below sum Q (the increasing function Q(1 + Q g_yy) - m/(8K) is {about(f_at)} > 0 at sum Q): the ledger falls")
    return g, chi, nf, p, chi2, nf2, p2, q_tot, m_tot, m_rec


# ============================================================================================ family C
def family_c(checks: Checks, state) -> None:
    g, chi, nf, p, chi2, nf2, p2, q_tot, m_tot, m_rec = state
    y = RECORD_SITE
    hs = [lambda s: ONE, lambda s: F(s[0]), lambda s: F(s[1]), lambda s: F(s[2])]
    before = [wall_moment(chi, h) for h in hs]
    after = [wall_moment(chi2, h) for h in hs]
    charges_moment = [sum((SPREAD[b] * h(b) for b in SPREAD), ZERO) for h in hs]
    identity = before == charges_moment and after == [q_tot * h(y) for h in hs]
    centre = [charges_moment[i] / q_tot for i in (1, 2, 3)]
    jump = [after[i] - before[i] for i in range(4)]
    monopole_still = (jump[0] == 0) if not mut("outside_sees_the_formation_in_the_monopole") else (jump[0] != 0)
    dipole_ok = all(jump[i + 1] == q_tot * (y[i] - centre[i]) for i in range(3)) and any(j != 0 for j in jump[1:])
    checks.check("C1", identity and monopole_still and dipole_ok, f"T2: for the discrete-harmonic functions 1, x, y, z the sum over wall bonds of (chi_inside - 1) h(wall) equals sum Q_x h(x) exactly, before and after; with the ledger kept the monopole does not jump and the dipole jumps by Q'(y - Xbar) = ({', '.join(about(j) for j in jump[1:])}), Xbar = ({', '.join(about(c) for c in centre)}) the centre of the charges")

    sites = list(SPREAD)
    probs = {b: SPREAD[b] * chi[b] for b in sites}                                                   # p_x is proportional to the bare energy m_x = 8K Q_x chi_x
    norm = sum(probs.values(), ZERO)
    probs = {b: v / norm for b, v in probs.items()}

    def mean_jump(odds):
        tot = sum(odds.values(), ZERO)
        return [q_tot * (sum((odds[b] * b[i] for b in sites), ZERO) / tot - centre[i]) for i in range(3)]

    charge_odds = {b: probs[b] / chi[b] for b in sites}
    prob_odds = dict(probs)
    square_odds = {b: probs[b] / chi[b] ** 2 for b in sites}
    zero = all(v == 0 for v in mean_jump(charge_odds))
    if mut("probability_odds_hold_the_centre"):
        holds = all(v == 0 for v in mean_jump(prob_odds))
    else:
        holds = any(v != 0 for v in mean_jump(prob_odds)) and any(v != 0 for v in mean_jump(square_odds))
    checks.check("C2", zero and holds, f"T2: over ANY odds of where the record forms (none is assumed) the mean jump of the dipole is Q'(sum odds_y y - Xbar): it vanishes for odds proportional to p_x/chi_x, the charge density, and not for odds proportional to p_x (mean jump {', '.join(about(v) for v in mean_jump(prob_odds))}) or to p_x/chi_x^2; at weak field p/chi and block 58's p sqrt(w) are the same density, p(1 - lam/2)")


# ============================================================================================ family D
def family_d(checks: Checks, state) -> None:
    g, chi, nf, p, chi2, nf2, p2, q_tot, m_tot, m_rec = state
    y = RECORD_SITE
    clocks_before = sum(p.values(), ZERO)
    clocks_after = p2[y]
    flux_before = wall_moment({s: 2 - nf[s] for s in INTERIOR}, lambda s: ONE)                          # sum over wall bonds of (1 - N_inside) = sum P_x
    jump = clocks_after - clocks_before
    kept = (jump != 0) if not mut("clocks_far_field_is_kept") else (jump == 0)
    increasing = p2[y] == q_tot / (1 + 2 * q_tot * g[y][y])
    checks.check("D1", flux_before == clocks_before and kept and increasing and all(p[b] == SPREAD[b] * nf[b] / chi[b] for b in SPREAD), f"T3: what the walls see of the CLOCKS is sum P_x = sum Q_x w_x (the flux of 1 - N): {about(clocks_before)} before and {about(clocks_after)} after, with the ledger kept: it jumps by {about(jump)}; since P' = Q'/(1 + 2Q' g_yy) is increasing in Q', the record that keeps the clocks' monopole has another charge than the one that keeps the ledger: no record keeps both")

    t = F(1, 1000)
    small = {b: t * q for b, q in SPREAD.items()}
    chi_s, nf_s, p_s, masses_s = fields(small, g)
    qs = t * q_tot
    rec_p = qs / (1 + 2 * qs * g[y][y])
    jump_s = rec_p - sum(p_s.values(), ZERO)
    second = -2 * (qs * qs * g[y][y] - sum((small[a] * small[b] * g[a][b] for a in small for b in small), ZERO))
    m_rec_s = 8 * K * qs * (1 + qs * g[y][y])
    energy_form = -(m_rec_s - sum(masses_s.values(), ZERO)) / (4 * K)
    close = abs(jump_s - second) < abs(second) / 100 and second == energy_form
    first_order = (abs(jump_s) < qs / 100) if not mut("jump_is_of_first_order") else (abs(jump_s) > qs / 100)
    checks.check("D2", close and first_order, f"T3: with every charge scaled by 1/1000 the jump of the clocks' monopole is within one per cent of -2[Q'^2 g_yy - sum Q_x Q_x' g_xx'] = -(m' - m)/(4K) (an exact identity between the two forms), and below one hundredth of the charge: a second-order effect, which vanishes at first order, where the two far-field coefficients agree (block 60 T4)")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for lengths of weight zero and for a ledger linear in the rates with the curvature member; it reports what the replacement of a spread amplitude at rest by one record does to the ledger and to what the walls see, of the lengths and of the clocks; no rule of formation is assumed; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
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
    "per_element: executed — the exact fields of a five-site amplitude at rest and of the record that keeps the ledger, in a 7x7x7 box with walls at w = l = 1: both stationarity conditions at all 125 sites",
    "per_site: executed — the record's bare energy against the amplitude's; the ledger for a charge of 1000; the sign that decides what happens when the bare energy is kept",
    "per_mode: executed — the wall moments of chi - 1 against sum Q_x h(x) for the four discrete-harmonic functions 1, x, y, z, before and after; the flux of 1 - N against sum P_x",
    "per_block: executed — the dipole's jump against Q'(y - Xbar); the mean jump for three odds; the clocks' monopole before and after; the second-order formula with all charges scaled by 1/1000",
    "lattice_wide: T1 and T2 hold for every amplitude at rest and every site of formation in every box with walls held at w = l = 1, for the curvature member with isotropic stretching; the statement about odds is about ANY odds and assumes none; T3 exactly for the stated configuration, the second-order formula for every configuration; whether an amplitude that has formed no record sources anything, whether a formation event keeps the ledger, and where records form are not decided; bodies at rest are supplied; nothing moves in this note",
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
    state = family_b(checks)
    family_c(checks, state)
    family_d(checks, state)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: a formation event under the curvature member's exact strong field — the ledger can be kept for every amplitude, by a record of charge sum Q and bare energy 8K Q'(1 + Q' g_yy); the lengths' monopole then does not jump and the dipole jumps by Q'(y - Xbar), its mean over any odds vanishing for odds proportional to the charge density p/chi; the clocks' monopole jumps at second order in the charges, so no record keeps both far-field coefficients")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
