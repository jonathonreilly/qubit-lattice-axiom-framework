#!/usr/bin/env python3
"""Exact checks: the unit budget of the explanation-tree route is false.

Scope.  For the one-sided two-level majority automaton in level time on Z^3 (blocks 25, 30) and the counted family of marked
explanation trees of block 32 (budget E <= 3(|S| - 1) + c|A|), the realization from the ten marks
M = {000, 001, 010, 100, 021, 102, 210, 113, 131, 311} has one seed, nine amplified and 27 processed one-sites, all in [0,3]^3, and at
its top site 333: every tree of the family has E - |A| >= 1, the minimum of E - (10/9)|A| is 0, so the family constant there is 10/9
exactly; the three 1-predecessors of 333 are processed with rooted value 0.  Hence block 32's conjecture c* = 1, block 33's
tight-sibling lemma and its hypothesis (H) are false.  The minimum is computed by an exact dynamic program over the subsets of each
level (the single-seed case: no forks), and the optimal trees are verified edge by edge.  Exact arithmetic only (integers and
Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SIX_AXIS_FORMATION_THRESHOLD_THE_UNIT_BUDGET_IS_FALSE_ONE_SEED_WITNESS_WITH_FAMILY_CONSTANT_TEN_NINTHS_TIGHT_SIBLING_LEMMA_REFUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_six_axis_formation_threshold_the_unit_budget_is_false_one_seed_witness_with_family_constant_ten_ninths_tight_sibling_lemma_refuted_bounded_theorem_note_2026-09-20"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "Records form.",
)

MUTATION_GATE = {
    "marks_wrong": "B",
    "rule_check_wrong": "B",
    "unit_budget_holds_injected": "C",
    "constant_wrong": "C",
    "predecessors_not_tight": "C",
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


# ============================================================================================ the automaton and the family
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
MARKS = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 2, 1), (1, 0, 2), (2, 1, 0), (1, 1, 3), (1, 3, 1), (3, 1, 1)]
TOP = (3, 3, 3)


def level(z):
    return z[0] + z[1] + z[2]


def preds(z):
    return [tuple(z[i] - e[i] for i in range(3)) for e in E3]


def run_automaton(lo: int, hi: int, marks):
    """the one-sided two-level majority automaton: a site is 1 if at least two predecessors are 1, otherwise iff it is marked"""
    mk = set(marks)
    eta = {}
    for z in sorted(product(range(lo, hi + 1), repeat=3), key=level):
        eta[z] = 1 if (sum(eta.get(p, 0) for p in preds(z)) >= 2 or z in mk) else 0
    return eta


def kinds(eta):
    ones = {z for z, v in eta.items() if v == 1}
    npred = {z: [p for p in preds(z) if p in ones] for z in ones}
    kind = {z: ("seed" if len(npred[z]) == 0 else "amp" if len(npred[z]) == 1 else "proc") for z in ones}
    return ones, npred, kind


def cost_of(kind_z: str, c: Fraction) -> Fraction:
    return Fraction(1) if kind_z == "proc" else -c if kind_z == "amp" else Fraction(0)


def single_seed_min(ones, npred, kind, root, c: Fraction, cap: int | None = None):
    """exact minimum of E - c|A| over the trees of the family containing the root, when there is one seed (then |S| = 1 and no forks):
    a tree is a set of one-sites containing the root and the seed in which every non-seed node has a 1-predecessor in the set.
    Dynamic program over the subsets of each level, from the top level down.  cap: only nodes at levels <= cap (the rooted value)."""
    seeds = [z for z in ones if kind[z] == "seed"]
    assert len(seeds) == 1
    seed = seeds[0]
    at: dict[int, list] = {}
    for z in ones:
        if cap is None or level(z) <= cap:
            at.setdefault(level(z), []).append(z)
    top_level, seed_level, root_level = max(at), level(seed), level(root)
    nodes = sorted(at[top_level])
    states = {}
    for mask in range(1 << len(nodes)):
        X = frozenset(nodes[i] for i in range(len(nodes)) if mask >> i & 1)
        if top_level == root_level and root not in X:
            continue
        states[X] = (sum((cost_of(kind[z], c) for z in X), Fraction(0)), None)
    history = []
    for lev in range(top_level, seed_level, -1):
        below = sorted(at.get(lev - 1, []))
        nxt = {}
        for X, (val, _) in states.items():
            need = [z for z in X if kind[z] != "seed"]
            for mask in range(1 << len(below)):
                Y = frozenset(below[i] for i in range(len(below)) if mask >> i & 1)
                if lev - 1 == root_level and root not in Y:
                    continue
                if any(not any(p in Y for p in npred[z]) for z in need):
                    continue
                v2 = val + sum((cost_of(kind[z], c) for z in Y), Fraction(0))
                if Y not in nxt or v2 < nxt[Y][0]:
                    nxt[Y] = (v2, X)
        history.append(states)
        states = nxt
    best, back = states[frozenset([seed])]
    chain = [frozenset([seed])]
    X = back
    i = len(history) - 1
    while X is not None and i >= 0:
        chain.append(X)
        X = history[i][X][1]
        i -= 1
    return best, set().union(*chain)


def is_tree_of_family(nodes, ones, npred, kind, root) -> tuple[bool, int, int]:
    """one seed: choose for every non-seed node one arrow to a 1-predecessor inside the set; the result is a tree (it descends to the seed)"""
    ns = set(nodes)
    if root not in ns or not ns <= ones:
        return False, 0, 0
    arrows = 0
    for z in ns:
        if kind[z] == "seed":
            continue
        inside = [p for p in npred[z] if p in ns]
        if not inside:
            return False, 0, 0
        arrows += 1
    seeds = sum(1 for z in ns if kind[z] == "seed")
    ok = seeds == 1 and arrows == len(ns) - 1
    return ok, sum(1 for z in ns if kind[z] == "proc"), sum(1 for z in ns if kind[z] == "amp")


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    norm = normalize_text(axioms)
    checks.check("A2", all(n in norm for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in normalize_text(block01), "block 01 on main carries its claim id and the static law of a product rule")


# ============================================================================================ family B (the realization)
def family_b(checks: Checks):
    marks = list(MARKS)
    if mut("marks_wrong"):
        marks[-1] = (3, 1, 2)
    small = run_automaton(0, 3, marks)
    large = run_automaton(-2, 6, marks)
    ones_s = {z for z, v in small.items() if v}
    ones_l = {z for z, v in large.items() if v}
    ones, npred, kind = kinds(large)
    sizes = [sum(1 for z in ones if level(z) == l) for l in range(10)]
    ok = ones_s == ones_l and len(ones) == 37 and sizes == [1, 3, 3, 4, 3, 6, 7, 6, 3, 1]
    ok = ok and sorted(kind.values()).count("seed") == 1 and sorted(kind.values()).count("amp") == 9 and sorted(kind.values()).count("proc") == 27
    ok = ok and kind.get(TOP) == "proc" and sorted(npred.get(TOP, [])) == [(2, 3, 3), (3, 2, 3), (3, 3, 2)] and all(kind[p] == "proc" for p in npred.get(TOP, []))
    checks.check("B1", ok, "T1: from the ten marks the automaton has 37 one-sites, all in [0,3]^3 (the boxes [0,3]^3 and [-2,6]^3 agree), level sizes 1,3,3,4,3,6,7,6,3,1, one seed (000), nine amplified, 27 processed; the top site 333 is processed and its three predecessors are processed one-sites")
    # the defining rule at every site of [-1,4]^3, and outside the marks' box nothing can turn on
    ok2 = True
    mk = set(marks)
    for z in product(range(-1, 5), repeat=3):
        want = 1 if (sum(large.get(p, 0) for p in preds(z)) >= 2 or z in mk) else 0
        if mut("rule_check_wrong"):
            want = 1 if (sum(large.get(p, 0) for p in preds(z)) >= 1 or z in mk) else 0
        if large[z] != want:
            ok2 = False
    cyc = lambda z: (z[2], z[0], z[1])
    ok2 = ok2 and {cyc(z) for z in mk} == mk and {cyc(z) for z in ones} == ones
    checks.check("B2", ok2, "T1: the defining rule holds at every site of [-1,4]^3; the marks and the one-set are invariant under the cyclic shift (a,b,c) -> (c,a,b)")
    return ones, npred, kind


# ============================================================================================ family C (the values)
def family_c(checks: Checks, ones, npred, kind) -> None:
    root = (2, 3, 3) if mut("unit_budget_holds_injected") else TOP
    one = Fraction(1)
    v1, nodes1 = single_seed_min(ones, npred, kind, root, one, cap=level(root))
    ok_tree, e1, a1 = is_tree_of_family(nodes1, ones, npred, kind, root)
    checks.check("C1", v1 == 1 and ok_tree and e1 - a1 == 1, f"T2: at the unit budget every tree of the family at 333 has E - |A| >= 1 (exact minimum {v1}, attained by a verified tree with E = {e1}, |A| = {a1}): no tree satisfies E <= 3(|S| - 1) + |A|")
    cstar = Fraction(1) if mut("constant_wrong") else Fraction(10, 9)
    v2, nodes2 = single_seed_min(ones, npred, kind, TOP, cstar)
    ok2, e2, a2 = is_tree_of_family(nodes2, ones, npred, kind, TOP)
    below = [Fraction(11, 10), Fraction(109, 99), Fraction(1)]
    pos = all(single_seed_min(ones, npred, kind, TOP, c)[0] > 0 for c in below)
    checks.check("C2", v2 == 0 and ok2 and Fraction(e2, a2) == Fraction(10, 9) and pos, f"T2: the minimum of E - c|A| at 333 is 0 at c = 10/9 (a verified tree with E = {e2}, |A| = {a2}) and positive at c = 1, 11/10, 109/99: the family constant at this realization is exactly 10/9")
    vals = []
    for u in sorted(npred[TOP]):
        vu, nu = single_seed_min(ones, npred, kind, u, one, cap=level(u))
        oku, eu, au = is_tree_of_family(nu, ones, npred, kind, u)
        vals.append((vu, oku))
    if mut("predecessors_not_tight"):
        vals[0] = (Fraction(-1), True)
    checks.check("C3", all(v == 0 and ok for v, ok in vals), "T3: each of the three 1-predecessors of 333 is processed with rooted value exactly 0 (tight), so the hypothesis of the tight-sibling lemma holds at 333 and its conclusion (a rooted tree of cost at most 0) fails")
    worst = max(single_seed_min(ones, npred, kind, z, one, cap=level(z))[0] for z in ones if z != TOP)
    checks.check("C4", worst <= 0, f"T3: 333 is the only one-site of the realization with positive rooted value (the largest rooted value among the other 36 is {worst})")


# ============================================================================================ family F
FENCES = (
    "This note proves that the unit budget of the explanation-tree route is false: at the realization from ten marks in `[0,3]³` the family constant at the site `333` is exactly `10/9`, so block 32's conjecture `c* = 1`, block 33's tight-sibling lemma and its hypothesis (H) fail; it proves nothing about the formation law's ordering threshold itself.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "optimal constant", "cannot be improved", "best possible",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 488."}
CLASSICAL_NAMES = ("Toom", "Berman", "Simon", "Gács", "Mermin", "Wagner", "Bramson", "Gray", "Krylov", "Peierls", "Dobrushin", "Dinkelbach")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Toom)", 1)
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
    "per_element: executed — the automaton's rule at every site of [-1,4]^3; the kinds of the 37 one-sites",
    "per_site: executed — the exact minimum of E - c|A| at 333 for c = 1, 109/99, 11/10, 10/9 and the rooted value of every one-site at c = 1",
    "per_mode: not applicable — a finite combinatorial witness",
    "per_block: executed — the optimal trees verified node by node (every non-seed node with a 1-predecessor inside; one seed; E and |A| counted)",
    "lattice_wide: one realization on Z^3 refutes the unit budget, the tight-sibling lemma and (H); the family constant is at least 10/9; no upper bound on it and no statement about the formation law's ordering threshold is made",
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
    ones, npred, kind = kinds(run_automaton(-2, 6, MARKS))      # family C works on the declared marks, whatever family B was given
    family_c(checks, ones, npred, kind)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: the unit budget of the explanation-tree route is false — a one-seed realization with family constant exactly 10/9 at its top site; the tight-sibling lemma and (H) fail there; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
