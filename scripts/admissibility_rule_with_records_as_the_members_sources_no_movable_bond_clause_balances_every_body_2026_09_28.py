#!/usr/bin/env python3
"""Exact checks: block 60's curvature member solved self-consistently with records as its sources (harvest of probe HIT #9366, a
Claude Opus worker, refereed by Claude Sonnet). Records sit one per site on the interior of a held box and cross to empty interior
neighbours at block 110's factor kappa = sqrt(w_x w_y)/(chi_x chi_y); the supplied clause is H = m sum_(x in C) w_x + sum over the movable
bonds (one end occupied) of g(kappa). (T1) e_z = m w_z n_z + sum g'(kappa) kappa/2 and tau_z = sum g'(kappa) kappa/2 over the movable bonds
at z; the field's-change clause (mu/2)(kappa - 1) has block 171's activity clause's (e, tau). (T2) At weak field, eps = 1/(8K),
P - Q = 2 g'(1) B eps + eps^2 [-4 m g''(1) S - 2 m^2 n.Gn] + O(eps^3), the bracket for g'(1) = 0, with G the Dirichlet Green function,
B the number of movable bonds and S = sum over movable bonds of (Gn)_x + (Gn)_y; G > 0 entrywise, so every clause with g'(1) = 0 and
g''(1) >= 0, and every jammed body, has P < Q at order eps^2. (T3) Balance at order eps^2 needs g''(1) = -m n.Gn/(2S), which differs
between bodies: on the 5^3 box -11/162, -145/1762, -23/222, -353/2546 (times m) for single records at the centre, a face, an edge and a
corner, and -3739/36462, -103877/1011162, -690875/6664644 under the uniform law for N = 1, 2, 3; for the centre record tuned at eps^2
the eps^3 term is m^2 (472392 g3 - 73777 m)/280908 with g3 the third derivative. (T4) The same clause on every bond touching a record
has the same form with its own B and S; it narrows the body dependence (a corner 2x2x2 cube needs -5941/59232 m against -5941/23586 m)
but does not remove it.

A (premises): landed block 110's site equations and P - Q.
B (T1): the clause's derivatives.
C (T2): the exact self-consistent series on the 5^3 box against the formula; positivity of G.
D (T3): the tuned values; the eps^3 term.
F (T4): the local variant.
Exact (Fractions, sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WITH_RECORDS_AS_THE_MEMBERS_SOURCES_NO_MOVABLE_BOND_CLAUSE_FIXED_ONCE_BALANCES_THE_TWO_CHARGES_OF_EVERY_BODY_AT_WEAK_FIELD_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_with_records_as_the_members_sources_no_movable_bond_clause_fixed_once_balances_the_two_charges_of_every_body_at_weak_field_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "Records form.",
    "A site never carries more than one record; records are permanent.",
    "Admissibility is not a dynamics axiom.",
)
LANDED110 = (
    "`(Δχ)_z = −e_z/(8K w_z χ_z)`",
    "`(ΔN)_z = (e_z + 2τ_z)/(8Kχ_z)`",
    "`P − Q = (1/8K) Σ_z [2τ_z − e_z(1 − w_z)/w_z]/χ_z`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "clause_derivative_forged": "B",
    "bracket_forged": "C",
    "tuned_value_forged": "D",
    "local_forged": "F",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()

# ============================================================================================ the member's weak-field series (exact)
ORD = 3


class Ser:
    __slots__ = ("c",)

    def __init__(self, c):
        c = list(c) + [Fr(0)] * (ORD + 1)
        self.c = [Fr(x) for x in c[:ORD + 1]]

    def __add__(a, b):
        b = b if isinstance(b, Ser) else Ser([b])
        return Ser([x + y for x, y in zip(a.c, b.c)])

    __radd__ = __add__

    def __sub__(a, b):
        b = b if isinstance(b, Ser) else Ser([b])
        return Ser([x - y for x, y in zip(a.c, b.c)])

    def __rsub__(a, b):
        return Ser([b]) - a

    def __neg__(a):
        return Ser([-x for x in a.c])

    def __mul__(a, b):
        if not isinstance(b, Ser):
            return Ser([x * b for x in a.c])
        r = [Fr(0)] * (ORD + 1)
        for i, x in enumerate(a.c):
            if x == 0:
                continue
            for j in range(ORD + 1 - i):
                r[i + j] += x * b.c[j]
        return Ser(r)

    __rmul__ = __mul__

    def inv(a):
        assert a.c[0] != 0
        r = [Fr(0)] * (ORD + 1)
        r[0] = 1 / a.c[0]
        for n in range(1, ORD + 1):
            r[n] = -sum(a.c[k] * r[n - k] for k in range(1, n + 1)) / a.c[0]
        return Ser(r)

    def __truediv__(a, b):
        if not isinstance(b, Ser):
            return Ser([x / b for x in a.c])
        return a * b.inv()

    def sqrt(a):
        assert a.c[0] == 1
        r = [Fr(0)] * (ORD + 1)
        r[0] = Fr(1)
        for n in range(1, ORD + 1):
            r[n] = (a.c[n] - sum(r[k] * r[n - k] for k in range(1, n))) / 2
        return Ser(r)

    def shift(a):
        """multiply by eps"""
        return Ser([Fr(0)] + a.c[:ORD])


L = 5
INT = [x for x in itertools.product(range(1, L - 1), repeat=3)]
IDX = {x: i for i, x in enumerate(INT)}
NI = len(INT)
NBR = {x: [tuple(x[k] + (d if k == a else 0) for k in range(3)) for a in range(3) for d in (-1, 1)] for x in INT}
BONDS = sorted({tuple(sorted((x, y))) for x in INT for y in NBR[x] if y in IDX})


def green():
    """Dirichlet Green matrix (-Delta)^-1 on the interior, exact"""

    A = sp.zeros(NI, NI)
    for x in INT:
        A[IDX[x], IDX[x]] = 6
        for y in NBR[x]:
            if y in IDX:
                A[IDX[x], IDX[y]] = -1
    Ai = A.inv()
    return [[Fr(int(sp.fraction(Ai[i, j])[0]), int(sp.fraction(Ai[i, j])[1])) for j in range(NI)] for i in range(NI)]


G = green()


def solve(occ, m, g1, g2, g3, local=False):
    """fixed-point series iteration of chi - 1 = eps G[e/(w chi)], 1 - N = eps G[(e + 2 tau)/chi]"""
    n = [1 if x in occ else 0 for x in INT]
    if local:
        cbonds = [b for b in BONDS if (b[0] in occ) or (b[1] in occ)]
    else:
        cbonds = [b for b in BONDS if (b[0] in occ) != (b[1] in occ)]
    chi = [Ser([1]) for _ in INT]
    N = [Ser([1]) for _ in INT]
    for _ in range(ORD + 2):
        w = [N[i] / chi[i] for i in range(NI)]
        e = [w[i] * (m * n[i]) for i in range(NI)]
        tau = [Ser([0]) for _ in INT]
        for (x, y) in cbonds:
            i, j = IDX[x], IDX[y]
            kap = (w[i] * w[j]).sqrt() / (chi[i] * chi[j])
            dk = kap - 1
            gp = Ser([g1]) + dk * g2 + dk * dk * (g3 / 2)
            t = gp * kap / 2
            for k in (i, j):
                e[k] = e[k] + t
                tau[k] = tau[k] + t
        s1 = [e[i] / (w[i] * chi[i]) for i in range(NI)]
        s2 = [(e[i] + tau[i] * 2) / chi[i] for i in range(NI)]
        chi = [Ser([1]) + sum((s1[j] * G[i][j] for j in range(NI) if G[i][j] != 0), Ser([0])).shift() for i in range(NI)]
        N = [Ser([1]) - sum((s2[j] * G[i][j] for j in range(NI) if G[i][j] != 0), Ser([0])).shift() for i in range(NI)]
    w = [N[i] / chi[i] for i in range(NI)]
    e = [w[i] * (m * n[i]) for i in range(NI)]
    tau = [Ser([0]) for _ in INT]
    for (x, y) in cbonds:
        i, j = IDX[x], IDX[y]
        kap = (w[i] * w[j]).sqrt() / (chi[i] * chi[j])
        dk = kap - 1
        gp = Ser([g1]) + dk * g2 + dk * dk * (g3 / 2)
        t = gp * kap / 2
        for k in (i, j):
            e[k] = e[k] + t
            tau[k] = tau[k] + t
    pq = sum(((tau[i] * 2 - e[i] * (Ser([1]) - w[i]) / w[i]) / chi[i] for i in range(NI)), Ser([0])).shift()
    return pq, n, cbonds


def formula(occ, local=False):
    n = [1 if x in occ else 0 for x in INT]
    Gn = [sum(G[i][j] * n[j] for j in range(NI)) for i in range(NI)]
    nGn = sum(n[i] * Gn[i] for i in range(NI))
    if local:
        cb = [b for b in BONDS if (b[0] in occ) or (b[1] in occ)]
    else:
        cb = [b for b in BONDS if (b[0] in occ) != (b[1] in occ)]
    S = sum(Gn[IDX[x]] + Gn[IDX[y]] for (x, y) in cb)
    return nGn, S, len(cb)




# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t110 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(normalize_text(n) in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: records form, at most one per site and permanent; Admissibility is not a dynamics axiom (the member and the clause are supplied)")
    q = list(LANDED110)
    if mut("landed_quote_forged"):
        q[2] = q[2].replace("2τ_z", "τ_z")
    checks.check("A3", all(x in t110 for x in q), "landed block 110: the site equations and P - Q for any content")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ux, uy, lx, ly, mu, kk = sp.symbols("u_x u_y lambda_x lambda_y mu k", real=True)
    g = sp.Function("g")
    kap = sp.exp((ux + uy) / 2 - (lx + ly) / 2)
    e_x = sp.diff(g(kap), ux)
    tau_x = -sp.diff(g(kap), lx)
    want = sp.diff(g(kk), kk).subs(kk, kap) * kap / 2
    if mut("clause_derivative_forged"):
        want = want * 2
    ok1 = sp.simplify(e_x - want) == 0 and sp.simplify(tau_x - want) == 0
    act = mu * kap / 2
    chg = mu * (kap - 1) / 2
    ok2 = all(sp.simplify(sp.diff(act, v) - sp.diff(chg, v)) == 0 for v in (ux, uy, lx, ly))
    checks.check("B1", ok1 and ok2, "a bond term g(kappa), kappa = exp((u_x + u_y - lambda_x - lambda_y)/2), gives e_x = tau_x = g'(kappa) kappa/2 at each end; the field's-change clause (mu/2)(kappa - 1) has the activity clause mu kappa/2's (e, tau)")


# ============================================================================================ family C (T2)
CONFIGS = [{(2, 2, 2)}, {(1, 1, 1)}, {(1, 2, 2), (2, 2, 2)}, {(1, 1, 1), (3, 3, 3)}, {(1, 1, 2), (2, 2, 2), (3, 1, 3)}]


def family_c(checks: Checks) -> None:
    m, g2, g3 = Fr(3, 2), Fr(-2, 3), Fr(5, 7)
    ok = True
    rows = []
    for occ in CONFIGS:
        nGn, S, B = formula(occ)
        for g1 in (Fr(0), Fr(1, 5)):
            pq, _, _ = solve(occ, m, g1, g2, g3)
            f1 = 2 * g1 * B
            f2 = -4 * m * g2 * S - 2 * m * m * nGn
            if mut("bracket_forged"):
                f2 = -2 * m * g2 * S - 2 * m * m * nGn
            ok = ok and pq.c[0] == 0 and pq.c[1] == f1 and (g1 != 0 or pq.c[2] == f2)
            rows.append(f"{sorted(occ)} g'(1)={g1}: eps {pq.c[1]}, eps^2 {pq.c[2]}")
    for r in rows:
        print("   " + r)
    pos = all(G[i][j] > 0 for i in range(NI) for j in range(NI))
    checks.check("C1", ok, "the exact self-consistent series on the 5^3 box (five configurations, m = 3/2, g'' = -2/3, third derivative 5/7): the eps term is 2 g'(1) B and, for g'(1) = 0, the eps^2 term is -4 m g''(1) S - 2 m^2 n.Gn")
    checks.check("C2", pos, "the Dirichlet Green matrix of the 3^3 interior is entrywise positive: n.Gn > 0 and S > 0, so g'(1) = 0 with g''(1) >= 0, or a jammed body (S = 0), gives P < Q at order eps^2")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    singles = {"centre": (2, 2, 2), "face": (1, 2, 2), "edge": (1, 1, 2), "corner": (1, 1, 1)}
    tuned = {}
    for name, x in singles.items():
        nGn, S, B = formula({x})
        tuned[name] = -nGn / (2 * S)
    want = {"centre": Fr(-11, 162), "face": Fr(-145, 1762), "edge": Fr(-23, 222), "corner": Fr(-353, 2546)}
    if mut("tuned_value_forged"):
        want["corner"] = want["centre"]
    ok1 = tuned == want and len(set(tuned.values())) == 4
    law = {}
    for N in (1, 2, 3):
        tn, ts = Fr(0), Fr(0)
        for occ in itertools.combinations(INT, N):
            nGn, S, B = formula(set(occ))
            tn += nGn
            ts += S
        law[N] = -tn / (2 * ts)
    ok2 = law == {1: Fr(-3739, 36462), 2: Fr(-103877, 1011162), 3: Fr(-690875, 6664644)}
    ok3 = True
    for mm, g3 in ((Fr(1), Fr(5, 7)), (Fr(2), Fr(-1, 3))):
        nGn, S, B = formula({(2, 2, 2)})
        pq, _, _ = solve({(2, 2, 2)}, mm, Fr(0), -mm * nGn / (2 * S), g3)
        ok3 = ok3 and pq.c[2] == 0 and pq.c[3] == mm * mm * (472392 * g3 - 73777 * mm) / 280908
    checks.check("D1", ok1, f"balance at order eps^2 needs g''(1) = -m n.Gn/(2S): single records {dict((k, str(v)) for k, v in tuned.items())} (times m), four different values")
    checks.check("D2", ok2, f"under the uniform law on the 5^3 box the tuned values are {dict((k, str(v)) for k, v in law.items())} (times m) for N = 1, 2, 3 records")
    checks.check("D3", ok3, "for the centre record tuned at eps^2, the eps^3 term is m^2 (472392 g3 - 73777 m)/280908 (g3 the third derivative): each order needs its own tuning")


# ============================================================================================ family F (T4)
def family_f(checks: Checks) -> None:
    m, g2, g3 = Fr(3, 2), Fr(-2, 3), Fr(5, 7)
    ok = True
    for occ in ({(1, 2, 2), (2, 2, 2)}, {(1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)}):
        pq, _, _ = solve(occ, m, Fr(0), g2, g3, local=True)
        nGn, S, B = formula(occ, local=True)
        ok = ok and pq.c[2] == -4 * m * g2 * S - 2 * m * m * nGn
    cube = {x for x in itertools.product((1, 2), repeat=3)}
    a1, S1, _ = formula(cube)
    a2, S2, _ = formula(cube, local=True)
    ac, Sc, _ = formula({(1, 1, 1)})
    mov, loc, single = -a1 / (2 * S1), -a2 / (2 * S2), -ac / (2 * Sc)
    if mut("local_forged"):
        loc = single
    ok = ok and mov == Fr(-5941, 23586) and loc == Fr(-5941, 59232) and loc != single and abs(loc - single) < abs(mov - single)
    checks.check("F1", ok, f"the clause on every bond touching a record has the same eps^2 form with its own S (series check on two configurations); a corner 2x2x2 cube needs {loc} m (local) against {mov} m (movable bonds), the lone corner record {single} m: the spread narrows but stays")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the tuned clause."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Watson", "Tolman", "Komar", "Kirchhoff")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Tolman) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the clause's derivatives; the equality of the activity and field's-change clauses",
    "per_site: executed - the exact self-consistent series on the 5^3 box for five configurations, through eps^2 (and eps^3 for the centre)",
    "per_mode: executed - the tuned values for single records at four site classes and under the uniform law for N = 1, 2, 3",
    "per_block: executed - entrywise positivity of the inverse of -Delta with held walls; the local variant's form and its narrower spread on 5^3",
    "lattice_wide: checked and not executed - larger boxes (floating point in the probe and the referee); the clocked law W != 1; finite field",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: at weak field, with records as the member's sources, P - Q = 2 g'(1) B eps + eps^2[-4 m g''(1) S - 2 m^2 n.Gn]; balance needs a concave clause tuned to the body, so no movable-bond clause fixed once balances every body; a clause on all bonds touching a record narrows the spread; a harvest of probe #9366, refereed by Claude Sonnet (same family); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
