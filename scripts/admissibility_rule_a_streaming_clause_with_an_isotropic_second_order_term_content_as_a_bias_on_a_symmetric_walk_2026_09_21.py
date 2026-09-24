#!/usr/bin/env python3
"""Exact checks: a streaming clause whose second-order term is isotropic (sphere menu; clauses supplied, not adopted).

BIASED WALK: a record of content s (a unit vector) hops to x + e, for each of the six lattice directions e, at the rate (alpha + c s.e)/2,
alpha >= c > 0.  Block 44's clause is c max(0, s.e): hops forward only.
T1: the biased walk has first moment c s and second moment alpha delta_kl whatever the content; for any non-negative axis-hop law with first
moment c s the second moment along axis k is at least c |s_k|, with equality only for forward hops; a content-independent second moment needs
alpha >= c.  T2: on fields of degree two its streaming operator is exactly -c s.grad + (alpha/2) Laplacian: the second-order term is isotropic,
the momentum equation gets (alpha/2) Laplacian g_i with no part of cubic symmetry, and a potential flow is damped by nothing.  T3: a site, and
any body, captures every content at the same rate: the captured records are a fair sample of the gas whatever its content law (block 48's
two-content witness: captured mean = gas mean).  T4: with exchange of contents on occupied targets the uniform measure is stationary and the
momentum is conserved event by event (two records on the 3x3x3 torus, three pairs of rational contents); not so if a blocked hop does nothing.
T5 the price: a record hops against its content a fraction (3 alpha - c |s|_1)/(6 alpha) of the time: between (3 - sqrt 3)/6 and 1/3 at alpha = c.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_STREAMING_CLAUSE_WITH_AN_ISOTROPIC_SECOND_ORDER_TERM_CONTENT_AS_A_BIAS_ON_A_SYMMETRIC_WALK_UNBIASED_CAPTURE_AND_ITS_PRICE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_unbiased_capture_and_its_price_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "second_moment_depends_on_content": "B",
    "forward_clause_not_minimal": "B",
    "operator_keeps_cubic_part": "C",
    "capture_weighted_by_content": "D",
    "blocked_hop_does_nothing": "E",
    "fraction_against_wrong": "E",
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
ALPHA, C = F(1, 3), F(1, 3)                                          # the control's values: probability (1 + s.e)/6 per attempt


def unit_contents():
    out = set()
    for d, length in (((1, 0, 0), 1), ((3, 4, 0), 5), ((1, 2, 2), 3), ((2, 3, 6), 7), ((1, 4, 8), 9)):
        for perm in set(product(range(3), repeat=3)):
            if sorted(perm) != [0, 1, 2]:
                continue
            for sg in product((1, -1), repeat=3):
                out.add(tuple(F(sg[i] * d[perm[i]], length) for i in range(3)))
    return sorted(out)


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def rate_biased(s, e, alpha=ALPHA, c=C):
    return (alpha + c * dot(s, e)) / 2


def rate_forward(s, e, c=C):
    return c * max(F(0), dot(s, e))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    for s in unit_contents():
        rates = [rate_biased(s, e) for e in E]
        ok = ok and all(r >= 0 for r in rates) and sum(rates) == 3 * ALPHA
        ok = ok and tuple(sum(rates[j] * E[j][i] for j in range(6)) for i in range(3)) == tuple(C * s[i] for i in range(3))
        for k in range(3):
            for l in range(3):
                m = sum(rates[j] * E[j][k] * E[j][l] for j in range(6))
                want = (ALPHA if k == l else F(0))
                if mut("second_moment_depends_on_content") and k == l:
                    want = C * abs(s[k])
                ok = ok and m == want
    checks.check("B1", ok, "T1: the biased walk (alpha + c s.e)/2 has non-negative rates, total rate 3 alpha, first moment c s and second moment alpha delta_kl for every one of 150 rational unit contents: the second moment does not depend on the content")
    ok = True
    rng = random.Random(52)
    for s in unit_contents():
        # any non-negative axis-hop law with first moment c s: a_plus - a_minus = c s_k on each axis, so a_plus + a_minus >= c |s_k|
        for _ in range(3):
            extra = [F(rng.randint(0, 5), 7) for _ in range(3)]
            for k in range(3):
                a_plus = C * max(F(0), s[k]) + extra[k]
                a_minus = C * max(F(0), -s[k]) + extra[k]
                ok = ok and a_plus - a_minus == C * s[k] and a_plus + a_minus >= C * abs(s[k]) and ((a_plus + a_minus == C * abs(s[k])) == (extra[k] == 0))
        fwd = [rate_forward(s, e) for e in E]
        for k in range(3):
            m = sum(fwd[j] * E[j][k] * E[j][k] for j in range(6))
            ok = ok and m == C * abs(s[k])
    # a content-independent second moment alpha must dominate c |s_k| for every content, hence alpha >= c (reached on the axes)
    least = max(C * abs(s[k]) for s in unit_contents() for k in range(3))
    if mut("forward_clause_not_minimal"):
        least = C / 2
    checks.check("B2", ok and least == C, f"T1: for any non-negative axis-hop law with first moment c s the second moment along an axis is at least c |s_k|, with equality only for block 44's forward hops; a second moment that does not depend on the content must therefore be at least c = {least}: the biased walk with alpha = c is the least diffusive such clause")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    rng = random.Random(152)
    ok = True
    for s in unit_contents():
        a0 = F(rng.randint(-5, 5))
        b = [F(rng.randint(-5, 5), rng.randint(1, 4)) for _ in range(3)]
        m = [[F(rng.randint(-4, 4), rng.randint(1, 3)) for _ in range(3)] for _ in range(3)]
        m = [[(m[i][j] + m[j][i]) / 2 for j in range(3)] for i in range(3)]

        def field(x):
            return a0 + sum(b[i] * x[i] for i in range(3)) + sum(m[i][j] * x[i] * x[j] for i in range(3) for j in range(3))

        x = tuple(F(rng.randint(-3, 3)) for _ in range(3))
        stream = sum(rate_biased(s, e) * (field(tuple(x[i] - e[i] for i in range(3))) - field(x)) for e in E)
        grad = [b[i] + 2 * sum(m[i][j] * x[j] for j in range(3)) for i in range(3)]
        lap = 2 * sum(m[k][k] for k in range(3))
        expansion = -C * dot(s, grad) + ALPHA / 2 * lap
        if mut("operator_keeps_cubic_part"):
            expansion = -C * dot(s, grad) + C / 2 * sum(abs(s[k]) * 2 * m[k][k] for k in range(3))
        ok = ok and stream == expansion
    checks.check("C1", ok, "T2: on a field of degree two the streaming operator of the biased walk is exactly -c s.grad + (alpha/2) Laplacian, the same second-order term for every content: in local equilibrium the momentum equation gets (alpha/2) Laplacian g_i and nothing of cubic symmetry, so a potential flow (whose Laplacian vanishes) meets no viscous stress at this order")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ok = True
    for s in unit_contents():
        site = sum(rate_biased(s, e) for e in E)                     # a record at the neighbour -e hops along e onto the site
        if mut("capture_weighted_by_content"):
            site = sum(rate_forward(s, e) for e in E)                 # the forward clause's capture weight c |s|_1
        ok = ok and site == 3 * ALPHA
    # bodies: a face with outward normal n is entered by hops along -n; opposite faces are equally many, so the content-dependent parts cancel
    bodies = {
        "cube": list(product(range(2), repeat=3)),
        "plate": [(x, y, 0) for x in range(2) for y in range(2)],
        "ball": [p for p in product(range(-3, 4), repeat=3) if sum(c * c for c in p) <= 9],
    }
    for body in bodies.values():
        bset = set(body)
        normals = [d for p in body for d in E if tuple(p[i] + d[i] for i in range(3)) not in bset]
        for s in unit_contents()[::7]:
            total = sum(rate_biased(s, tuple(-c for c in n)) for n in normals)
            ok = ok and total == ALPHA * len(normals) / 2
    # block 48's witness: contents (1,0,0) and (-3/5,-4/5,0), equally likely
    s_a, s_b = (F(1), F(0), F(0)), (F(-3, 5), F(-4, 5), F(0))
    w_a, w_b = sum(rate_biased(s_a, e) for e in E), sum(rate_biased(s_b, e) for e in E)
    cap = tuple((w_a * s_a[i] + w_b * s_b[i]) / (w_a + w_b) for i in range(3))
    ok = ok and cap == (F(1, 5), F(-2, 5), F(0))
    checks.check("D1", ok, "T3: a site captures every content at the rate 3 alpha, and a body of any shape (cube, 2x2x1 plate, ball of radius 3) with total weight alpha/2 times the exposed-face count, under a homogeneous product reservoir, because opposite faces are equally many: captured records are a fair sample of the gas (for block 48's two contents the captured mean is the gas mean (1/5, -2/5, 0), where the forward clause gave (1/15, -7/15, 0))")


# ============================================================================================ family E (T4, T5)
SIDE = 3
SITES = list(product(range(SIDE), repeat=3))


def family_e(checks: Checks) -> None:
    ok = True
    pairs = [((F(1, 3), F(2, 3), F(2, 3)), (F(-3, 5), F(0), F(4, 5))), ((F(1), F(0), F(0)), (F(-1), F(0), F(0))), ((F(2, 7), F(-3, 7), F(6, 7)), (F(2, 7), F(-3, 7), F(6, 7)))]
    states = 0
    for s1, s2 in pairs:
        inflow = {}
        outflow = {}
        for x1 in SITES:
            for x2 in SITES:
                if x1 == x2:
                    continue
                key = (x1, s1, x2, s2)
                for (xa, sa, xb, sb, first) in ((x1, s1, x2, s2, True), (x2, s2, x1, s1, False)):
                    for e in E:
                        r = rate_biased(sa, e)
                        target = tuple((xa[i] + e[i]) % SIDE for i in range(3))
                        if target == xb:
                            if mut("blocked_hop_does_nothing"):
                                continue
                            nxt = (xa, sb, xb, sa) if first else (xb, sa, xa, sb)     # contents exchanged, positions kept
                        else:
                            nxt = (target, sa, xb, sb) if first else (xb, sb, target, sa)
                        # canonical form: the record carrying s1 first when contents differ; for equal contents order by position
                        if nxt[1] != s1 or (s1 == s2 and nxt[0] > nxt[2]):
                            nxt = (nxt[2], nxt[3], nxt[0], nxt[1])
                        ckey = key if not (s1 == s2 and key[0] > key[2]) else (key[2], key[3], key[0], key[1])
                        inflow[nxt] = inflow.get(nxt, 0) + r
                        outflow[ckey] = outflow.get(ckey, 0) + r
        for k, v in outflow.items():
            ok = ok and inflow.get(k, 0) == v
        states += len(outflow)
    checks.check("E1", ok, f"T4: with exchange of contents on occupied targets the flow into every configuration of two records on the 3x3x3 torus equals the flow out of it ({states} configurations, three pairs of rational contents): the uniform measure is stationary; hops move contents or exchange them, so number and momentum are conserved")
    ok = True
    shown = []
    for s in ((F(1), F(0), F(0)), (F(3, 5), F(4, 5), F(0)), (F(1, 3), F(2, 3), F(2, 3)), (F(2, 7), F(3, 7), F(6, 7))):
        against = sum((rate_biased(s, e) for e in E if dot(s, e) < 0), F(0))      # start from a Fraction: an empty sum is the integer 0, and 0/2 is a float
        idle = sum((rate_biased(s, e) for e in E if dot(s, e) == 0), F(0))
        l1 = sum(abs(c) for c in s)
        want = (3 * ALPHA - C * l1) / 2 - idle / 2
        if mut("fraction_against_wrong"):
            want = F(0)
        ok = ok and against == want
        shown.append(f"|s|_1 = {l1}: against {against / (3 * ALPHA)}, across {idle / (3 * ALPHA)}")
    checks.check("E2", ok, "T5: the share of a record's hops that go against its content, and across it (at alpha = c): " + "; ".join(shown) + ": a record moving along an axis makes one hop in three forwards and two in three sideways; one along a body diagonal makes (3 - sqrt 3)/6 of its hops backwards")


# ============================================================================================ family F
FENCES = (
    "This note works within a supplied variant of the inertial clause of block 44; it reports a streaming clause whose second-order term is isotropic, what it restores and what it costs; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Knudsen", "Einstein", "Planck", "Fourier", "Taylor", "Reynolds", "Chapman", "Enskog",
                   "Frisch", "Hasslacher", "Pomeau", "Hardy", "Pazzis", "Peclet", "Courant", "Lax", "Godunov", "Friedrichs")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Courant)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
    float_hits += [x for x in nodes if isinstance(x,ast.Call) and
        ((isinstance(x.func,ast.Name) and x.func.id in ("float","N")) or
         (isinstance(x.func,ast.Attribute) and x.func.attr in ("evalf","N")))]
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
    "per_element: executed — rates, first and second moments of the biased walk for 150 rational unit contents; the lower bound c |s_k| on the second moment of any axis-hop law and its attainment by forward hops",
    "per_site: executed — capture at the rate 3 alpha by a site and alpha/2 per exposed face by a cube, a plate and a ball; the two-content witness",
    "per_mode: not applicable — the retained finite identities concern local rates and integrated flux, not a mode spectrum",
    "per_block: executed — the streaming operator on fields of degree two; the balance of flows at every two-record configuration of the 3x3x3 torus for three pairs of contents; the shares of hops against and across the content",
    "lattice_wide: T1 to T3 and T5 are exact for the clause; T4 is checked in the two-record sector and argued in general by the pairing of every hop with a predecessor of the same rate; the lattice's symmetry returns at fourth order in gradients, which the note does not compute; the wind by direction under the clause is an executed control, not a proof",
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
    print("scope: a streaming clause with an isotropic second-order term — content as a bias on a symmetric walk: content-independent second moment, least diffusion alpha = c, isotropic viscous term, unbiased capture by any body, stationary uniform measure, and the share of hops that go against or across the content")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
