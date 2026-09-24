#!/usr/bin/env python3
"""Exact checks: two structure theorems on how records form.

Scope.  T1 (the hull): for the six-axis rule with positive, not all equal weights and any finite window whose graph has a cycle, every
adapted formation scheme S (the next site may depend on the records so far; clocks with value-dependent rates included) gives the
constant patterns less weight than the static law: mu_S(v^b) <= p^|E| / D_min < p^|E| / Z = mu_stat(v^b), D_min the least over orders of
prod_x N_{k_x}, N_0 = 6, N_k = p^k + q^k + 4 r^k; so the static law lies outside the closed convex hull of the adapted formation laws.
T2 (causal structures): on a finite predecessor structure (a directed acyclic graph; a site forms only after all its predecessors and
reads exactly them) every readiness-gated adapted scheme, every clock law on the ready sites and every joint formation of an antichain
gives the same law, the product of the rule's kernels; a scheme that lets a site form before a neighbour it would read changes the law.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import ast
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_HOW_RECORDS_FORM_STATIC_LAW_OUTSIDE_THE_HULL_OF_ADAPTED_FORMATION_LAWS_AND_CLAUSE_INDEPENDENCE_ON_A_CAUSAL_PREDECESSOR_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_how_records_form_static_law_outside_the_hull_of_adapted_formation_laws_and_clause_independence_on_a_causal_predecessor_structure_bounded_theorem_note_2026-09-20"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "inequality_direction_wrong": "B",
    "tree_window_strict_injected": "B",
    "adapted_bound_wrong": "B",
    "causal_gate_removed": "C",
    "noncausal_control_equal_injected": "C",
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


# ============================================================================================ the rule, windows, exact laws
M6 = range(6)
TRIPLES = ((3, 1, 2), (5, 2, 4), (7, 3, 5))


def weight(p, q, r):
    return [[Fraction(p) if a == b else Fraction(q) if a == (b ^ 1) else Fraction(r) for b in M6] for a in M6]


def n_k(p, q, r, k: int) -> Fraction:
    return Fraction(6) if k == 0 else Fraction(p) ** k + Fraction(q) ** k + 4 * Fraction(r) ** k


WINDOWS = {
    "plaquette": (list(range(4)), [(0, 1), (1, 2), (2, 3), (3, 0)]),
    "rectangle 2x3": (list(range(6)), [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]),
    "cube": (list(range(8)), [(a, b) for a in range(8) for b in range(a + 1, 8) if bin(a ^ b).count("1") == 1]),
    "path of 3": (list(range(3)), [(0, 1), (1, 2)]),
    "star of 4": (list(range(4)), [(0, 1), (0, 2), (0, 3)]),
}


def neighbours(sites, edges):
    nb = {x: set() for x in sites}
    for a, b in edges:
        nb[a].add(b)
        nb[b].add(a)
    return nb


def partition_function(sites, edges, W) -> Fraction:
    """exact Z by eliminating one site at a time"""
    tables = [((a, b), {(va, vb): W[va][vb] for va in M6 for vb in M6}) for a, b in edges]
    for x in sites:
        inv = [t for t in tables if x in t[0]]
        rest = [t for t in tables if x not in t[0]]
        scope = tuple(sorted(set().union(*[set(t[0]) for t in inv]) - {x})) if inv else ()
        new = {}
        for vals in product(M6, repeat=len(scope)):
            asg = dict(zip(scope, vals))
            tot = Fraction(0)
            for vx in M6:
                asg[x] = vx
                w = Fraction(1)
                for key, tab in inv:
                    w *= tab[tuple(asg[k] for k in key)]
                tot += w
            new[vals] = tot
        tables = rest + [(scope, new)]
    out = Fraction(1)
    for key, tab in tables:
        out *= tab[()]
    return out


def d_extreme(sites, edges, p, q, r, largest: bool = False) -> Fraction:
    nb = neighbours(sites, edges)
    n = len(sites)
    best = {0: Fraction(1)}
    for mask in range(1 << n):
        if mask not in best:
            continue
        for i, x in enumerate(sites):
            if mask >> i & 1:
                continue
            k = sum(1 for y in nb[x] if mask >> sites.index(y) & 1)
            v = best[mask] * n_k(p, q, r, k)
            m2 = mask | (1 << i)
            if m2 not in best or (v > best[m2] if largest else v < best[m2]):
                best[m2] = v
    return best[(1 << n) - 1]


def one_site_law(W, past_values):
    raw = []
    for a in M6:
        t = Fraction(1)
        for b in past_values:
            t *= W[a][b]
        raw.append(t)
    z = sum(raw)
    return [t / z for t in raw]


def scheme_law(sites, read, ready, W, pick, patterns):
    """exact law of an adapted scheme: state = (tuple of formed sites in order is irrelevant; the formed set and its records).
    read(x, formed) = the sites whose records x reads when it forms; ready(x, formed) = whether x may form now;
    pick(formed_records) = a dict {site: probability} over the sites allowed now.  Returns {pattern: probability} on `patterns`."""
    out = {}
    start = {(): Fraction(1)}          # key: tuple of (site, value) sorted by site
    frontier = start
    n = len(sites)
    for _ in range(n):
        nxt = {}
        for key, prob in frontier.items():
            rec = dict(key)
            allowed = [x for x in sites if x not in rec and ready(x, rec)]
            dist = pick(rec, allowed)
            for x, px in dist.items():
                if px == 0:
                    continue
                law = one_site_law(W, [rec[y] for y in read(x, rec)])
                for a in M6:
                    k2 = tuple(sorted(list(key) + [(x, a)]))
                    nxt[k2] = nxt.get(k2, Fraction(0)) + prob * px * law[a]
        frontier = nxt
    for key, prob in frontier.items():
        out[tuple(v for _, v in key)] = prob
    return out


def random_pick(rng):
    cache = {}

    def pick(rec, allowed):
        key = (tuple(sorted(rec.items())), tuple(allowed))
        if key not in cache:
            ws = [rng.randrange(0, 5) for _ in allowed]
            if sum(ws) == 0:
                ws[rng.randrange(len(ws))] = 1
            cache[key] = {x: Fraction(w, sum(ws)) for x, w in zip(allowed, ws)}
        return cache[key]

    return pick


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    norm = normalize_text(axioms)
    checks.check("A2", all(n in norm for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in normalize_text(block01), "block 01 on main carries its claim id and the static law of a product rule")


# ============================================================================================ family B (the hull)
def family_b(checks: Checks) -> None:
    ok = True
    eq_ok = True
    for (p, q, r) in TRIPLES + ((2, 2, 1),):
        W = weight(p, q, r)
        for k in (2, 3, 4):
            nk = n_k(p, q, r, k)
            for tup in product(M6, repeat=k):
                s = sum(_prod(W[a][b] for b in tup) for a in M6)
                bad = (s < nk) if mut("inequality_direction_wrong") else (s > nk)
                if bad:
                    ok = False
                same = len(set(tup)) == 1
                antipodal = len({t >> 1 for t in tup}) == 1
                expect_equal = same or (p == q and antipodal)
                if (s == nk) != expect_equal:
                    eq_ok = False
    checks.check("B1", ok and eq_ok, "T1: for k = 2, 3, 4 and every tuple of recorded neighbours, sum_s prod_i phi(s, a_i) <= N_k, with equality exactly when the a_i are equal (or, only when p = q, lie in one antipodal pair); at (3,1,2), (5,2,4), (7,3,5) and (2,2,1)")
    ok2 = True
    rows = []
    for (p, q, r) in TRIPLES:
        W = weight(p, q, r)
        for name, (sites, edges) in WINDOWS.items():
            Z = partition_function(sites, edges, W)
            D = d_extreme(sites, edges, p, q, r)
            cyclic = name in ("plaquette", "rectangle 2x3", "cube")
            if mut("tree_window_strict_injected"):
                cyclic = True
            if cyclic and not Z < D:
                ok2 = False
            if not cyclic and Z != D:
                ok2 = False
            if (p, q, r) == (3, 1, 2):
                expected = {"plaquette":(20784,22464),"rectangle 2x3":(6000000,7008768),"cube":(6982520832,10933678080),"path of 3":(864,864),"star of 4":(10368,10368)}
                if name in expected:
                    ok2 = ok2 and (Z,D)==expected[name]
                rows.append(f"{name}: Z = {Z}, D_min = {D}")
    checks.check("B2", ok2, "T1: Z < D_min on the plaquette, the 2x3 rectangle and the cube, and Z = D_min on the path and the star (no cycle), at the three weight triples; at (3,1,2): " + "; ".join(rows))
    # every order on the plaquette and the rectangle: mu_sigma(constant) = p^|E| / D_sigma
    ok3 = True
    for (p, q, r) in TRIPLES[:2]:
        W = weight(p, q, r)
        for name in ("plaquette", "rectangle 2x3"):
            sites, edges = WINDOWS[name]
            nb = neighbours(sites, edges)
            Z = partition_function(sites, edges, W)
            stat = Fraction(p) ** len(edges) / Z
            for order in permutations(sites):
                formed = []
                prob = Fraction(1)
                dsig = Fraction(1)
                for x in order:
                    k = sum(1 for y in nb[x] if y in formed)
                    prob *= one_site_law(W, [0] * k)[0]
                    dsig *= n_k(p, q, r, k)
                    formed.append(x)
                if prob != Fraction(p) ** len(edges) / dsig or not prob < stat:
                    ok3 = False
    checks.check("B3", ok3, "T1: for every order of the plaquette (24) and of the 2x3 rectangle (720) the constant pattern has formation weight p^|E| / D_sigma, strictly below its static weight; at (3,1,2) and (5,2,4)")
    # adapted schemes on the plaquette: exact laws of 60 random value-dependent schemes
    ok4 = True
    norm_ok = True
    p, q, r = 3, 1, 2
    W = weight(p, q, r)
    sites, edges = WINDOWS["plaquette"]
    nb = neighbours(sites, edges)
    Z = partition_function(sites, edges, W)
    bound = Fraction(p) ** len(edges) / (d_extreme(sites, edges, p, q, r, largest=True) if mut("adapted_bound_wrong") else d_extreme(sites, edges, p, q, r))
    rng = random.Random(38)
    worst = Fraction(0)
    for trial in range(60):
        law = scheme_law(sites, lambda x, rec: [y for y in nb[x] if y in rec], lambda x, rec: True, W, random_pick(rng), None)
        if sum(law.values()) != 1:
            norm_ok = False
        for b in M6:
            val = law[(b,) * 4]
            worst = max(worst, val)
            if val > bound:
                ok4 = False
    checks.check("B4", ok4 and norm_ok and bound < Fraction(p) ** len(edges) / Z, f"T1: 60 random adapted schemes on the plaquette at (3,1,2) (the next site drawn with probabilities depending on the records so far), exact laws: every constant pattern has weight at most p^4/D_min = {bound} < p^4/Z = {Fraction(p) ** 4 / Z} (largest found {worst})")


def _prod(it):
    out = Fraction(1)
    for t in it:
        out *= t
    return out


# ============================================================================================ family C (causal structures)
def family_c(checks: Checks) -> None:
    p, q, r = 3, 1, 2
    W = weight(p, q, r)
    # the diamond: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3 (the 2x2 level-ordered square); the V: 0 -> 2 <- 1
    structures = {"diamond": ([0, 1, 2, 3], {0: [], 1: [0], 2: [0], 3: [1, 2]}), "V": ([0, 1, 2], {0: [], 1: [], 2: [0, 1]})}
    ok = True
    for name, (sites, parents) in structures.items():
        target = {}
        for pat in product(M6, repeat=len(sites)):
            w = Fraction(1)
            for x in sites:
                w *= one_site_law(W, [pat[y] for y in parents[x]])[pat[x]]
            target[pat] = w
        rng = random.Random(3800 + len(sites))
        for trial in range(12):
            if mut("causal_gate_removed"):
                ready = lambda x, rec: True
                read = lambda x, rec, parents=parents: [y for y in parents[x] if y in rec]
            else:
                ready = lambda x, rec, parents=parents: all(y in rec for y in parents[x])
                read = lambda x, rec, parents=parents: parents[x]
            law = scheme_law(sites, read, ready, W, random_pick(rng), None)
            if law != target:
                ok = False
    checks.check("C1", ok, "T2: on the diamond and the V, 12 random readiness-gated adapted schemes each (the next ready site drawn with value-dependent probabilities, which includes every clock law on the ready sites) give exactly the product of the rule's kernels, on all patterns")
    # joint formation of an antichain: the rule-consistent joint law of {1, 2} given site 0 is the product of the one-site kernels
    ok2 = True
    for v0 in M6:
        joint = {(a, b): W[a][v0] * W[b][v0] for a in M6 for b in M6}
        zj = sum(joint.values())
        for (a, b), w in joint.items():
            if w / zj != one_site_law(W, [v0])[a] * one_site_law(W, [v0])[b]:
                ok2 = False
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    ok2 = ok2 and all(sum((e[i][c] - e[j][c]) ** 2 for c in range(3)) == 2 for i in range(3) for j in range(3) if i != j)
    checks.check("C2", ok2, "T2: an antichain formed jointly has the product law (no bond inside it); on level-ordered Z^3 same-level displacement has coordinate sum zero, so the sites cannot be nearest neighbours")
    # negative control: the path of 3 read as an undirected window: middle first against middle last (a site formed before a neighbour it would read)
    def path_law(order):
        law = {}
        nb = {0: [1], 1: [0, 2], 2: [1]}
        for pat in product(M6, repeat=3):
            formed = []
            w = Fraction(1)
            for x in order:
                w *= one_site_law(W, [pat[y] for y in nb[x] if y in formed])[pat[x]]
                formed.append(x)
            law[pat] = w
        return law
    a, b = path_law((1, 0, 2)), path_law((0, 2, 1))
    tv = sum(abs(a[k] - b[k]) for k in a) / 2
    checks.check("C3", (tv == 0) if mut("noncausal_control_equal_injected") else (tv == Fraction(1,72)), f"T2 (control): on the undirected path of 3 the order that forms the middle site last reads two neighbours where the other reads one at a time, and the laws differ: total variation {tv} at (3,1,2)")


# ============================================================================================ family F
FENCES = (
    "For the supplied six-axis positive pair weights (not all equal), the static law lies outside the closed convex hull of adapted single-site formation laws on a finite window with a cycle. On a fixed causal predecessor structure, readiness-gated adapted schedules give the product law; joint ready-antichain draws must use the explicitly factorized kernel. Arbitrary correlated joint draws are excluded. No predecessor structure is selected by this result.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the plaquette."}
CLASSICAL_NAMES = ("Hölder", "Holder", "Gibbs", "Markov", "Bayes", "Toom", "Dobrushin", "Glauber")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T2", phrase + "\n\n## Theorem T2", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Hölder)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [x for x in nodes if isinstance(x,ast.Constant) and isinstance(x.value,float)]
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
    "per_element: executed — the inequality sum_s prod phi(s, a_i) <= N_k with its equality cases for every tuple, k <= 4, four weight triples",
    "per_site: executed — every order of the plaquette and the 2x3 rectangle: the constant pattern's weight p^|E|/D_sigma against the static weight",
    "per_mode: No spectral-mode theorem is asserted; this certificate concerns the explicitly declared finite discrete model. Not applicable — finite windows",
    "per_block: executed — Z and D_min exactly on five windows at three triples; exact laws of 60 random adapted schemes on the plaquette and of 24 readiness-gated schemes on two causal structures",
    "lattice_wide: T1 holds for every finite window with a cycle and every positive not-all-equal triple; T2 for every finite predecessor structure; which structure the axioms intend is not decided here",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: how records form — the static law outside the hull of adapted formation laws on windows with a cycle; one law for every readiness-gated clause on a causal predecessor structure; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
