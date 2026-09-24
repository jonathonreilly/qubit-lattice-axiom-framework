#!/usr/bin/env python3
"""Exact checks: the binding scale pinned at the neutral value.

Scope (conditional on the moving-records reading of block 39 and on the proposal c = c_0; nothing adopted).  For the six-axis rule with
weights omega = (p, q, r), one-neighbour probability K_1(b | a) = omega(a, b)/(p + q + 4r), and the law with vacancies (a bond between
two records weighs c omega, a bond with an empty end weighs 1, a record weighs z):
T1: c_0 = 6/(p + q + 4r) is the only scale at which (i) the pair weight is the rule's likelihood ratio against the uniform law,
W = K_1/(1/6); (ii) an empty site's row of the bond kernel is the average of the six record rows, so the vector (-6, 1, ..., 1) is
annihilated; (iii) the formation rate next to one record equals the rate in empty space.  T2: at c_0, on a window without a cycle, the
occupancy is independent from site to site with density 6z/(1 + 6z), the contents given the occupancy follow the rule's tree law, and
every occupied forest weighs (6z)^n.  T3: a fully occupied cycle of length n weighs (6z)^n (1 + 3 l_1^n + 2 l_2^n), l_1 = (p - q)/(p + q + 4r),
l_2 = (p + q - 2r)/(p + q + 4r): all binding at c_0 comes from cycles and is fixed by the rule's own eigenvalues.  T4: at any other
scale, on a window without a cycle, the occupancy is the lattice gas with bond activity c/c_0: that ratio is the content-blind glue.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_BINDING_SCALE_PINNED_AT_THE_NEUTRAL_VALUE_PAIR_WEIGHT_IS_THE_RULES_LIKELIHOOD_RATIO_NO_BINDING_WITHOUT_A_CYCLE_ALL_BINDING_IS_AGREEMENT_AROUND_LOOPS_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_binding_scale_pinned_at_the_neutral_value_pair_weight_is_the_rules_likelihood_ratio_no_binding_without_a_cycle_all_binding_is_agreement_around_loops_bounded_theorem_note_2026-09-20"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "A site with no record cannot be read.",
)

MUTATION_GATE = {
    "scale_wrong": "B",
    "null_vector_wrong": "B",
    "tree_independence_at_wrong_scale": "C",
    "forest_weight_wrong": "C",
    "loop_factor_wrong": "D",
    "activity_wrong": "E",
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


M6 = range(6)
TRIPLES = ((3, 1, 2), (5, 2, 4), (12, 1, 2))


def shape(p, q, r):
    return [[Fraction(p) if a == b else Fraction(q) if a == (b ^ 1) else Fraction(r) for b in M6] for a in M6]


def neutral(p, q, r) -> Fraction:
    return Fraction(6, p + q + 4 * r)


def occupancy_law(n_sites, edges, W, z):
    """exact law of the occupied set: sum over contents of prod z prod W, by enumeration"""
    out = {}
    for cfg in product([None] + list(M6), repeat=n_sites):
        w = Fraction(1)
        for v in cfg:
            if v is not None:
                w *= z
        for a, b in edges:
            if cfg[a] is not None and cfg[b] is not None:
                w *= W[cfg[a]][cfg[b]]
        occ = tuple(v is not None for v in cfg)
        out[occ] = out.get(occ, Fraction(0)) + w
    return out


def is_forest(occ, edges) -> bool:
    nodes = [i for i, o in enumerate(occ) if o]
    parent = {i: i for i in nodes}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for a, b in edges:
        if occ[a] and occ[b]:
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[ra] = rb
    return True


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    norm = normalize_text(axioms)
    checks.check("A2", all(n in norm for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used: no possibility is privileged; the distribution sentence; a site with no record cannot be read")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in normalize_text(block01), "block 01 on main carries its claim id and the static law of a product rule")


# ============================================================================================ family B (T1: the characterizations)
def family_b(checks: Checks) -> None:
    ok = True
    uniq = True
    for (p, q, r) in TRIPLES:
        om = shape(p, q, r)
        c0 = Fraction(1) if mut("scale_wrong") else neutral(p, q, r)
        z1 = p + q + 4 * r
        W = [[c0 * om[a][b] for b in M6] for a in M6]
        ok = ok and all(W[a][b] == Fraction(om[a][b], z1) / Fraction(1, 6) for a in M6 for b in M6)       # likelihood ratio against the uniform law
        ok = ok and all(sum(W[a]) / 6 == 1 for a in M6)                                                   # an empty bond = the average record bond
        ok = ok and all(sum(W[a][b] for a in M6) / 6 == 1 for b in M6)                                     # formation next to one record at the empty-space rate
        for c in (Fraction(1, 4), Fraction(1), 2 * neutral(p, q, r)):
            if c != neutral(p, q, r) and sum(c * om[0][b] for b in M6) / 6 == 1:
                uniq = False
    checks.check("B1", ok and uniq, "T1: at c_0 = 6/(p + q + 4r), and at no other scale, the pair weight is the rule's one-neighbour probability divided by 1/6, its rows average to 1, and an empty site next to one record forms at the empty-space rate; at (3,1,2), (5,2,4), (12,1,2)")
    ok2 = True
    for (p, q, r) in TRIPLES:
        c0 = neutral(p, q, r)
        om = shape(p, q, r)
        B = [[Fraction(1)] * 7] + [[Fraction(1)] + [c0 * om[a][b] for b in M6] for a in M6]
        v = [Fraction(-6 if not mut("null_vector_wrong") else -5)] + [Fraction(1)] * 6
        ok2 = ok2 and all(sum(B[i][j] * v[j] for j in range(7)) == 0 for i in range(7))
        ok2 = ok2 and all(B[0][j] == sum(B[i][j] for i in range(1, 7)) / 6 for j in range(7))
    checks.check("B2", ok2, "T1: at c_0 the empty row of the 7 x 7 bond kernel is the average of the six record rows, so the vector (-6, 1, 1, 1, 1, 1, 1) is annihilated: bond by bond an empty site acts as a record of uniformly random content (companion T5: RP boundary only when p>=q and p+q>=2r)")
    # the formation rate as a likelihood ratio of the neighbourhood
    p, q, r = 3, 1, 2
    c0 = neutral(p, q, r)
    om = shape(p, q, r)
    k1 = [[Fraction(om[a][b], p + q + 4 * r) for b in M6] for a in M6]
    ok3 = True
    for past in product(M6, repeat=2):
        zx_over_6 = sum(c0 * om[a][past[0]] * c0 * om[a][past[1]] for a in M6) / 6
        bayes = sum(Fraction(1, 6) * k1[a][past[0]] * k1[a][past[1]] for a in M6) / (Fraction(1, 6) ** 2)
        ok3 = ok3 and zx_over_6 == bayes
    checks.check("B3", ok3, "T1: at c_0 the formation rate over its empty-space value, Z_x/6, equals the likelihood ratio of the neighbours' contents under a common uniformly drawn cause against independent uniform draws, for all 36 pairs of neighbours")


# ============================================================================================ family C (T2: no binding without a cycle)
TREES = {
    "path of 3": (3, [(0, 1), (1, 2)]),
    "star of 4": (4, [(0, 1), (0, 2), (0, 3)]),
    "path of 4": (4, [(0, 1), (1, 2), (2, 3)]),
    "tree of 5": (5, [(0, 1), (1, 2), (1, 3), (3, 4)]),
}


def family_c(checks: Checks) -> None:
    ok = True
    for (p, q, r) in TRIPLES[:2]:
        om = shape(p, q, r)
        c = Fraction(1) if mut("tree_independence_at_wrong_scale") else neutral(p, q, r)
        W = [[c * om[a][b] for b in M6] for a in M6]
        for z in (Fraction(1, 12), Fraction(2, 3)):
            rho = 6 * z / (1 + 6 * z)
            for name, (n, edges) in TREES.items():
                law = occupancy_law(n, edges, W, z)
                tot = sum(law.values())
                for occ, w in law.items():
                    want = Fraction(1)
                    for o in occ:
                        want *= rho if o else 1 - rho
                    if w / tot != want:
                        ok = False
    checks.check("C1", ok, "T2: at c_0, on the path of 3, the star of 4, the path of 4 and a tree of 5 sites, the occupancy is exactly independent from site to site with density 6z/(1 + 6z); two weight triples, two fugacities")
    # every occupied forest of the 2x3 window weighs (6z)^n; and the contents of a fully occupied tree follow the rule's tree law
    ok2 = True
    p, q, r = 3, 1, 2
    om = shape(p, q, r)
    c0 = neutral(p, q, r)
    W = [[c0 * om[a][b] for b in M6] for a in M6]
    z = Fraction(1, 5)
    edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
    law = occupancy_law(6, edges, W, z)
    forests = 0
    for occ, w in law.items():
        if is_forest(occ, edges):
            forests += 1
            n = sum(occ)
            want = (6 * z) ** n if not mut("forest_weight_wrong") else (6 * z) ** n * 2
            if w != want:
                ok2 = False
    n, tedges = TREES["tree of 5"]
    for cfg in list(product(M6, repeat=n))[::97]:
        w = Fraction(1)
        for a, b in tedges:
            w *= W[cfg[a]][cfg[b]]
        rule = Fraction(1, 6)
        for a, b in tedges:
            rule *= Fraction(om[cfg[a]][cfg[b]], p + q + 4 * r)
        if w / 6 ** n != rule:
            ok2 = False
    checks.check("C2", ok2 and forests==57, f"T2: on the 2x3 window every occupied set without a cycle ({forests} of the 64) weighs exactly (6z)^n; on a fully occupied tree the contents have the rule's tree law (uniform root, the one-neighbour probability along each edge)")


# ============================================================================================ family D (T3: binding is agreement around loops)
def family_d(checks: Checks) -> None:
    ok = True
    vals = []
    for (p, q, r) in TRIPLES:
        om = shape(p, q, r)
        c0 = neutral(p, q, r)
        W = [[c0 * om[a][b] for b in M6] for a in M6]
        z1 = p + q + 4 * r
        l1, l2 = Fraction(p - q, z1), Fraction(p + q - 2 * r, z1)
        for n in (4, 6):
            tot = Fraction(0)
            for cfg in product(M6, repeat=n):
                w = Fraction(1)
                for i in range(n):
                    w *= W[cfg[i]][cfg[(i + 1) % n]]
                tot += w
            factor = tot / 6 ** n
            want = Fraction(1) if mut("loop_factor_wrong") else 1 + 3 * l1 ** n + 2 * l2 ** n
            if factor != want:
                ok = False
            if n == 4:
                vals.append(f"({p},{q},{r}): {factor}")
    checks.check("D1", ok, "T3: a fully occupied cycle of length n = 4, 6 weighs (6z)^n (1 + 3 l_1^n + 2 l_2^n) with l_1 = (p - q)/(p + q + 4r), l_2 = (p + q - 2r)/(p + q + 4r), the two non-trivial eigenvalues of the rule's one-neighbour probability; plaquette factors " + "; ".join(vals))
    p, q, r = 3, 1, 2
    om = shape(p, q, r)
    W = [[neutral(p, q, r) * om[a][b] for b in M6] for a in M6]
    law = occupancy_law(4, [(0, 1), (1, 2), (2, 3), (3, 0)], W, Fraction(1, 12))
    tot = sum(law.values())
    d0 = sum(w for occ, w in law.items() if occ[0]) / tot
    d01 = sum(w for occ, w in law.items() if occ[0] and occ[1]) / tot
    checks.check("D2", d01 - d0 * d0 == Fraction(15552,1224510049), f"T3: on the plaquette at c_0 neighbouring occupancies are positively correlated, by the loop factor alone (covariance {d01 - d0 * d0} at (3,1,2), z = 1/12)")


# ============================================================================================ family E (T4: the glue is c/c_0)
def family_e(checks: Checks) -> None:
    ok = True
    p, q, r = 3, 1, 2
    om = shape(p, q, r)
    c0 = neutral(p, q, r)
    z = Fraction(1, 12)
    for c in (Fraction(1, 4), Fraction(1), Fraction(3)):
        W = [[c * om[a][b] for b in M6] for a in M6]
        for name, (n, edges) in TREES.items():
            law = occupancy_law(n, edges, W, z)
            for occ, w in law.items():
                bonds = sum(1 for a, b in edges if occ[a] and occ[b])
                expo = sum(occ) if mut("activity_wrong") else bonds
                if w != (6 * z) ** sum(occ) * (c / c0) ** expo:
                    ok = False
    checks.check("E1", ok, "T4: at any scale c, on a window without a cycle, the occupied set weighs (6z)^n (c/c_0)^(occupied bonds): the content-less lattice gas with bond activity c/c_0; the glue beyond the rule is exactly the ratio c/c_0 (c = 1/4, 1, 3 at (3,1,2))")


# ============================================================================================ family F
FENCES = (
    "This note works under the moving-records reading of block 39 and proposes the value c = c_0 for the binding scale; neither the reading nor the value is in the axioms memo, and neither is adopted or registered here.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 10."}
CLASSICAL_NAMES = ("Bayes", "Gibbs", "Boltzmann", "Ising", "Potts", "Kawasaki", "Markov", "Bernoulli", "Shannon")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Bayes)", 1)
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
    "per_element: executed — the pair weight as the rule's likelihood ratio; the averaged empty row and the annihilated vector; the formation rate as a likelihood ratio, all 36 neighbour pairs",
    "per_site: executed — exact occupancy laws on four windows without a cycle at two triples and two fugacities; all 64 occupied sets of the 2x3 window",
    "per_mode: executed — the loop factor 1 + 3 l_1^n + 2 l_2^n for n = 4, 6 at three triples, by enumeration of the contents",
    "per_block: executed — the lattice-gas form (6z)^n (c/c_0)^bonds away from the neutral scale on windows without a cycle",
    "lattice_wide: T1-T4 hold for every finite window and every positive six-axis triple; the value c = c_0 is a proposal, not adopted and not registered; historical clumping reports are not fresh evidence or an infinite-volume theorem",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
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
    print("scope: the binding scale at the neutral value — the pair weight is the rule's likelihood ratio; an empty site is a record of unknown content; no binding without a cycle; the loop factor from the rule's eigenvalues; the glue c/c_0 away from it; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
