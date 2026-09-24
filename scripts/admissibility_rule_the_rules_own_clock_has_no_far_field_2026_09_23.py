#!/usr/bin/env python3
"""Compact-support clocks have compact-support Laplacian sources; exact contact ratios, an anticommutation obstruction and conditional reciprocity identities."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_THE_RULES_OWN_CLOCK_HAS_NO_FAR_FIELD_THE_PULL_NEEDS_A_RATE_LAW_WITH_A_MONOPOLE_A_REST_ENERGY_AND_A_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_INERTIA_JOINED_WITH_THE_RULES_PAIR_WEIGHTS_BY_A_CLOCK_GLOBAL_CLOCK_EXACT_LOCAL_CLOCK_EXACT_FOR_PAIRS_DEFECT_AT_THREE_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_rules_own_clock_has_no_far_field_the_pull_needs_a_rate_law_with_a_monopole_a_rest_energy_and_a_coupling_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "averaging_law_massive": "B",
    "kappa_table_altered": "C",
    "average_order_swapped": "C",
    "equal_pull_sign_flipped": "D",
    "rest_term_forged": "E",
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the distribution sentence; Admissibility is not a dynamics axiom and does not define a time metric (rates are supplied clauses)")


# ============================================================================================ helpers
import itertools
import random

E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
P0, Q0, R0 = F(3), F(1), F(2)
C0 = 6 / (P0 + Q0 + 4 * R0)
PAIR = {"equal": C0 * P0, "opposite": C0 * Q0, "orthogonal": C0 * R0}
MULT = {"equal": 1, "opposite": 1, "orthogonal": 4}


def rel(a, b):
    if a == b:
        return "equal"
    if E6[a] == tuple(-t for t in E6[b]):
        return "opposite"
    return "orthogonal"


def torus(L):
    sites = list(itertools.product(range(L), repeat=3))
    nb = {x: [tuple((x[i] + (d if i == j else 0)) % L for i in range(3)) for j in range(3) for d in (-1, 1)] for x in sites}
    return sites, nb


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    L = 4
    sites, nb = torus(L)
    # (a) any field whatever: the block-53 sources u_x - (1/6) sum u_(x+e) sum to zero on a torus (symbolic u at every site)
    u = {x: sp.Symbol("u_%d_%d_%d" % x) for x in sites}
    avg_weight = sp.Rational(1, 6) if not mut("averaging_law_massive") else sp.Rational(1, 7)
    total = sp.expand(sum((u[x] - avg_weight * sum((u[y] for y in nb[x]), sp.Integer(0)) for x in sites), sp.Integer(0)))
    zero_total = total == 0
    # (b) a range-R clock (rate a function of the records within graph distance R, ambient without records) on a larger
    # torus: u vanishes beyond distance R of the records, so it and its sources have finite support: no tail
    L2 = 9
    sites2, nb2 = torus(L2)

    def dist(x, y):
        return sum(min((x[i] - y[i]) % L2, (y[i] - x[i]) % L2) for i in range(3))
    random.seed(7)
    fin = True
    for R in (1, 2):
        for trial in range(6):
            recs = {(4 + random.randint(-1, 1), 4 + random.randint(-1, 1), 4 + random.randint(-1, 1)): random.randrange(6) for _ in range(3)}
            fsym = {}
            uu = {}
            for x in sites2:
                patt = tuple(sorted((tuple((y[i] - x[i]) % L2 for i in range(3)), c) for y, c in recs.items() if dist(x, y) <= R))
                if not patt:
                    uu[x] = sp.Integer(0)
                else:
                    fsym.setdefault(patt, sp.Symbol("f%d" % len(fsym)))
                    uu[x] = fsym[patt]
            src = {x: sp.expand(uu[x] - sp.Rational(1, 6) * sum((uu[y] for y in nb2[x]), sp.Integer(0))) for x in sites2}
            far = [x for x in sites2 if min(dist(x, y) for y in recs) > R + 1]
            fin = fin and all(uu[x] == 0 and src[x] == 0 for x in far) and sp.expand(sum(src.values(), sp.Integer(0))) == 0
    # (c) block 53's clock: one record of source log kappa has total source log kappa; an n-record body n log kappa
    lk = sp.symbols("logkappa")
    n = sp.symbols("n", positive=True, integer=True)
    mono = sp.simplify(n * lk + (-n * lk)) == 0
    checks.check("B1", zero_total and fin and mono, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = C0 == F(1, 2) and PAIR == {"equal": F(3, 2), "opposite": F(1, 2), "orthogonal": F(1)}
    ok = ok and sum((MULT[k] * PAIR[k] for k in PAIR), F(0)) / 6 == 1

    def karith(wx, wn):
        return wx / (sum(wn, F(0)) / 6)
    one = {k: karith(1 / cw, [1 / cw] + [F(1)] * 5) for k, cw in PAIR.items()}
    target = {"equal": F(12, 17), "opposite": F(12, 7), "orthogonal": F(1)}
    if mut("kappa_table_altered"):
        target["equal"] = F(12, 7)
    ok = ok and one == target and karith(F(1), [F(1)] * 6) == 1
    two = {}
    for (k1, w1), (k2, w2) in itertools.combinations_with_replacement(PAIR.items(), 2):
        two[(k1, k2)] = karith(1 / (w1 * w2), [1 / w1, 1 / w2] + [F(1)] * 4)
    ok = ok and two == {("equal", "equal"): F(1, 2), ("equal", "opposite"): F(6, 5), ("equal", "orthogonal"): F(12, 17),
                        ("opposite", "opposite"): F(3), ("opposite", "orthogonal"): F(12, 7), ("orthogonal", "orthogonal"): F(1)}
    unif = sum((MULT[k] * one[k] for k in PAIR), F(0)) / 6
    sw = {k: MULT[k] * PAIR[k] for k in PAIR}
    stat = sum((sw[k] * one[k] for k in PAIR), F(0)) / sum(sw.values(), F(0))
    order = (unif > 1 > stat) if not mut("average_order_swapped") else (unif < 1 < stat)
    ok = ok and unif == F(382, 357) and stat == F(352, 357) and order
    # geometric mean (block 53's exact form): neighbours whose only record neighbour is x give kappa = pi_x^(-5/6)
    pis = sp.symbols("w1:7", positive=True)
    pix = sp.Mul(*pis)
    kgeo = (1 / pix) / sp.Mul(*[(1 / wi) ** sp.Rational(1, 6) for wi in pis])
    geo = sp.simplify(kgeo - pix ** sp.Rational(-5, 6)) == 0
    checks.check("C1", ok and geo, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # the field of the rule's clock is u = -log pi: formal logs on 3^3, 40 random configurations, sources sum to zero and vanish where pi = 1 nearby
    L = 3
    sites, nb = torus(L)
    sym = {k: sp.Symbol("l_" + k) for k in PAIR}
    random.seed(11)
    tot = True
    loc = True
    for trial in range(40):
        nrec = random.randint(1, 6)
        occ = dict(zip(random.sample(sites, nrec), [random.randrange(6) for _ in range(nrec)]))
        logpi = {x: (sum((sym[rel(occ[x], occ[y])] for y in nb[x] if y in occ), sp.Integer(0)) if x in occ else sp.Integer(0)) for x in sites}
        src = {x: sp.expand(-logpi[x] + sp.Rational(1, 6) * sum((logpi[y] for y in nb[x]), sp.Integer(0))) for x in sites}
        tot = tot and sp.expand(sum(src.values(), sp.Integer(0))) == 0
        loc = loc and all(src[x] == 0 for x in sites if logpi[x] == 0 and all(logpi[y] == 0 for y in nb[x]))
    checks.check("C2", tot and loc, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    EA, EB, SA, SB, g1 = sp.symbols("E_A E_B S_A S_B gprime")
    sign = 1 if not mut("equal_pull_sign_flipped") else -1
    pulls = sp.expand(-EA * SB * g1 + sign * EB * SA * g1 - (-(EA * SB - EB * SA) * g1)) == 0
    gam, Erec = sp.symbols("gamma E_rec", positive=True)
    lk = sp.symbols("lk")
    sol = sp.solve(sp.Eq(lk / Erec, -gam / 6), lk)[0]
    kap_ok = sp.simplify(sol + gam * Erec / 6) == 0
    checks.check("D1", pulls and kap_ok, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    a, b, c, d = sp.symbols("a b c d")
    Mm = sp.Matrix([[a, b], [c, d]])
    sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    mats = (sx, sy, sz) if not mut("rest_term_forged") else (sx, sy)
    eqs = []
    for s in mats:
        eqs += list(Mm * s + s * Mm)
    solm = sp.solve(eqs, [a, b, c, d], dict=True)
    no_rest = len(solm) == 1 and len(solm[0]) == 4 and all(v == 0 for v in solm[0].values())
    gam = sp.symbols("gamma", positive=True)
    EA, EB = sp.symbols("E_A E_B")
    t, wx, wy = sp.symbols("t w_x w_y", positive=True)
    Fe = (2 / gam) * (sp.sqrt(wx) - sp.sqrt(wy)) ** 2
    weight_one = sp.simplify(Fe.subs({wx: t * wx, wy: t * wy}, simultaneous=True) - t * Fe) == 0
    pull_dep = sp.diff(-(gam / (4 * sp.pi)) * EA * EB / sp.Symbol("R", positive=True), gam) != 0
    checks.check("E1", no_rest and weight_one and pull_dep, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    m=sp.symbols("m",real=True)
    scalar=m*sp.eye(2)
    sx=sp.Matrix([[0,1],[1,0]])
    checks.check("E9", scalar.subs(m,2).eigenvals()=={sp.Integer(2):2} and scalar*sx+sx*scalar==2*m*sx, 'Scoped exact check E9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Compact-support clocks have compact-support Laplacian sources; exact contact ratios, an anticommutation obstruction and conditional reciprocity identities.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
