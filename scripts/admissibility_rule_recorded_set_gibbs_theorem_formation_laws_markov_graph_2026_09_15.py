#!/usr/bin/env python3
"""Exact checks: the recorded-set Gibbs theorem — every formation law's Markov graph is the recorded-set graph.

Scope.  The six Bloch-axis menu with the covariant positive product rule (p, q, r), the records-only reading, finite windows
and total formation orders.  T1: the product form (1/6)^{n_0} prod_edges K / prod_{|A_x|>=2} K_{|A_x|}(v_{A_x}), checked
against the product of conditionals on every order of the plaquette and of the star.  T3: the k-th mixed differences of
log K_k are nonzero for k = 2..6 at (3,1,2) and (5,2,4) (exact ratios) and vanish at the constant rule.  T6: the canonical
(vacuum-normalized) potential of the plaquette law with its last site recording two neighbors has a nonzero term on the
co-recorded non-adjacent pair and a zero term on the other non-edge on all 1296 configurations; the star with its center
last has a nonzero three-body term on the leaves; a direct Markov-property test (conditional dependence on the non-edge
partner) agrees.  Exact rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, permutations, product
from math import prod
from pathlib import Path

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RECORDED_SET_GIBBS_THEOREM_FORMATION_LAWS_MARKOV_GRAPH_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
)
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]
BLOCK01_PATH = ROOT / AUDIT_INPUT_PATHS[2]
BLOCK08_PATH = ROOT / AUDIT_INPUT_PATHS[3]
CLAIM_ID = "admissibility_rule_recorded_set_gibbs_theorem_formation_laws_markov_graph_bounded_theorem_note_2026-09-15"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "at most one recorded neighbor"
BLOCK08_CLAIM_ID = "admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15"
BLOCK08_FRAGMENT = "witnessed three-body irreducibility"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "product_form_wrong": "B",
    "mixed_difference_forged": "B",
    "constant_rule_difference_claimed": "B",
    "recorded_pairs_adjacent_claimed": "B",
    "plaquette_nonedge_term_claimed": "C",
    "plaquette_diagonal_term_denied": "C",
    "star_three_body_denied": "C",
    "markov_test_disagrees": "C",
    "claim_physical_order": "F",
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
AXES = ("+x", "-x", "+y", "-y", "+z", "-z")
M = 6


def orbit_type(s: int, t: int) -> str:
    if s == t:
        return "p"
    if s // 2 == t // 2:
        return "q"
    return "r"


class Rule:
    def __init__(self, tr) -> None:
        p, q, r = tr
        w = {"p": p, "q": q, "r": r}
        self.tr = tr
        self.phi = [[w[orbit_type(s, t)] for t in range(M)] for s in range(M)]
        self.Z1 = sum(self.phi[0])
        self.K = [[F(self.phi[s][a], self.Z1) for s in range(M)] for a in range(M)]

    def Zk(self, vals) -> int:
        return sum(prod(self.phi[s][a] for a in vals) for s in range(M))

    def Kk(self, vals) -> Fraction:
        return F(self.Zk(vals), self.Z1 ** len(vals))

    def cond(self, rec: tuple) -> list:
        if not rec:
            return [F(1, M)] * M
        Z = self.Zk(rec)
        return [F(prod(self.phi[s][a] for a in rec), Z) for s in range(M)]


# ------------------------------------------------------------------ windows, orders, laws
PLAQUETTE = {"sites": ["a", "b", "c", "d"], "edges": [("a", "b"), ("a", "c"), ("b", "d"), ("c", "d")]}
STAR = {"sites": ["l1", "l2", "l3", "x"], "edges": [("x", "l1"), ("x", "l2"), ("x", "l3")]}


def neighbors(win, s):
    return [b if a == s else a for a, b in win["edges"] if s in (a, b)]


def recorded_sets(win, order):
    pos = {s: t for t, s in enumerate(order)}
    return {s: tuple(y for y in neighbors(win, s) if pos[y] < pos[s]) for s in win["sites"]}


def law_conditionals(rule: Rule, win, order, v: dict) -> Fraction:
    rec = recorded_sets(win, order)
    return prod(rule.cond(tuple(v[y] for y in rec[s]))[v[s]] for s in win["sites"])


def law_product_form(rule: Rule, win, order, v: dict) -> Fraction:
    rec = recorded_sets(win, order)
    n0 = sum(1 for s in win["sites"] if not rec[s])
    w = F(1, M) ** n0
    for a, b in win["edges"]:
        w *= rule.K[v[a]][v[b]]
    for s in win["sites"]:
        if len(rec[s]) >= 2:
            w /= rule.Kk(tuple(v[y] for y in rec[s]))
    return w


def mixed_ratio(rule: Rule, vals) -> Fraction:
    """exp of the k-th mixed difference of log Z_k at vals with vacuum 0 (= +x): a ratio of products of Z_k values."""
    k = len(vals)
    num, den = 1, 1
    for mask in range(1 << k):
        arg = tuple(vals[i] if (mask >> i) & 1 else 0 for i in range(k))
        z = rule.Zk(arg)
        if (k - bin(mask).count("1")) % 2 == 0:
            num *= z
        else:
            den *= z
    return F(num, den)


def canonical_ratio(law, sites, S, v: dict) -> Fraction:
    """exp(Phi_S(v_S)) for the vacuum-normalized potential of the positive law on the window: Möbius inversion."""
    num, den = F(1), F(1)
    for r in range(len(S) + 1):
        for T in combinations(S, r):
            w = {s: 0 for s in sites}
            for s in T:
                w[s] = v[s]
            val = law(w)
            if (len(S) - r) % 2 == 0:
                num *= val
            else:
                den *= val
    return num / den


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b01: str, b08: str) -> None:
    checks.check("A1", all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, block 01, block 08)")
    flat_ax = normalize_text(axiom_text)
    checks.check("A2", all(n in flat_ax for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f01, f08 = normalize_text(b01).lower(), normalize_text(b08).lower()
    checks.check("A3", BLOCK01_CLAIM_ID in f01 and BLOCK01_FRAGMENT in f01 and BLOCK08_CLAIM_ID in f08 and BLOCK08_FRAGMENT in f08,
                 "the parents' claim ids and the cited fragments (block 01's condition; block 08's three-body term) are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
RATIOS_312 = {2: F(169, 121), 3: F(169, 165), 4: F(25313305500289, 23811286661761), 5: F(2241861381895613, 2214449659543773)}
RATIOS_524 = {2: F(961, 784), 3: F(1291123, 1244800), 4: F(845934898201600, 806460091894081)}
WITNESS = {2: (1, 1), 3: (1, 1, 2), 4: (1, 1, 1, 1), 5: (1, 1, 1, 1, 2), 6: (1, 1, 1, 1, 1, 1)}


def family_b(checks: Checks, report: dict) -> None:
    rule = Rule((3, 1, 2))
    ok = True
    n_orders = 0
    for win in (PLAQUETTE, STAR):
        for order in permutations(win["sites"]):
            n_orders += 1
            for vals in product(range(M), repeat=4):
                v = dict(zip(win["sites"], vals))
                lhs = law_conditionals(rule, win, order, v)
                rhs = law_product_form(rule, win, order, v)
                if mut("product_form_wrong"):
                    rhs *= 2
                if lhs != rhs:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            break
    checks.check("B1", ok and n_orders == 48, f"T1: the product form equals the product of conditionals on all 1296 configurations for every one of the {n_orders} orders of the plaquette and the star at (3,1,2)")
    r312 = {k: mixed_ratio(rule, WITNESS[k]) for k in range(2, 7)}
    r524 = {k: mixed_ratio(Rule((5, 2, 4)), WITNESS[k]) for k in range(2, 7)}
    lit_ok = all(r312[k] == RATIOS_312[k] for k in RATIOS_312) and all(r524[k] == RATIOS_524[k] for k in RATIOS_524)
    nonzero = all(r312[k] != 1 for k in range(2, 7)) and all(r524[k] != 1 for k in range(2, 7))
    if mut("mixed_difference_forged"):
        nonzero = r312[6] == 1
    checks.check("B2", lit_ok and nonzero, "T3: exp of the k-th mixed difference of log Z_k at the witness assignments is not 1 for k = 2..6 at (3,1,2) and (5,2,4); the literals for k <= 5 (k <= 4) match")
    rc = Rule((2, 2, 2))
    const = all(mixed_ratio(rc, vals) == 1 for k in range(2, 7) for vals in product((1, 2), repeat=k))
    if mut("constant_rule_difference_claimed"):
        const = not const
    checks.check("B3", const, "T3 control: at the constant rule every mixed-difference ratio over the {-x, +y}-assignments is 1 for k = 2..6")
    # B4: co-recorded neighbors are never adjacent on Z^3 (bipartite): two neighbors of a site differ by an even vector
    nbrs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    adj = any(sum(abs(a - b) for a, b in zip(u, w)) == 1 for u in nbrs for w in nbrs if u != w)
    if mut("recorded_pairs_adjacent_claimed"):
        adj = True
    checks.check("B4", not adj, "T4: no two neighbors of a site of Z^3 are adjacent (their difference has even coordinate sum)")
    report["rule"] = rule


# ============================================================================================ family C
def family_c(checks: Checks, report: dict, exact: bool) -> None:
    rule = report["rule"]
    sites = PLAQUETTE["sites"]
    order = ("a", "b", "c", "d")
    law = lambda w: law_product_form(rule, PLAQUETTE, order, w)
    v = {"a": 1, "b": 2, "c": 4, "d": 3}
    bc = canonical_ratio(law, sites, ("b", "c"), v)
    ad_all_one = all(canonical_ratio(law, sites, ("a", "d"), dict(zip(sites, vals))) == 1 for vals in product(range(M), repeat=4))
    bc_some = any(canonical_ratio(law, sites, ("b", "c"), dict(zip(sites, vals))) != 1 for vals in product(range(M), repeat=4))
    if mut("plaquette_nonedge_term_claimed"):
        ad_all_one = False
    checks.check("C1", ad_all_one, "T6: the plaquette law (order a, b, c, d) has a zero canonical term on the never-co-recorded non-edge {a, d} on all 1296 configurations")
    if mut("plaquette_diagonal_term_denied"):
        bc_some = False
    checks.check("C2", bc_some and bc == F(12, 13), f"T6: the canonical term on the co-recorded non-adjacent pair {{b, c}} is nonzero; exp Phi_bc = {bc} at (a,b,c,d) = (-x,+y,+z,-y)")
    ab = canonical_ratio(law, sites, ("a", "b"), v)
    bd = canonical_ratio(law, sites, ("b", "d"), v)
    q4 = canonical_ratio(law, sites, tuple(sites), v)
    bcd = canonical_ratio(law, sites, ("b", "c", "d"), v)
    checks.check("C3", ab == 3 and bd == F(3, 4) and q4 == 1 and bcd == 1, f"T6: edge terms exp Phi_ab = {ab}, exp Phi_bd = {bd}; the four-body and the {{b,c,d}} terms are 1 at the witness")
    # C4: the star, center last: three-body term on the leaves
    ssites = STAR["sites"]
    sorder = ("l1", "l2", "l3", "x")
    slaw = lambda w: law_product_form(rule, STAR, sorder, w)
    tri = canonical_ratio(slaw, ssites, ("l1", "l2", "l3"), {"l1": 1, "l2": 1, "l3": 2, "x": 0})
    tri_some = tri != 1
    if mut("star_three_body_denied"):
        tri_some = False
    checks.check("C4", tri_some and tri == F(165, 169), f"T6: the star with its center last has a nonzero three-body term on the leaves: exp Phi = {tri} at (l1,l2,l3) = (-x,-x,+y)")
    # C5: direct Markov test on the plaquette: the conditional of b given the rest depends on c (non-edge partner) and not... (a, d are its neighbors)
    def cond_b(w):
        ws = []
        for s in range(M):
            ww = dict(w)
            ww["b"] = s
            ws.append(law(ww))
        Z = sum(ws)
        return [x / Z for x in ws]
    base = {"a": 0, "b": 0, "c": 0, "d": 0}
    dep_c = False
    for cval in range(M):
        w = dict(base)
        w["c"] = cval
        if cond_b(w) != cond_b(base):
            dep_c = True
            break
    # and the conditional of a does not depend on d (never co-recorded, non-adjacent)
    def cond_a(w):
        ws = []
        for s in range(M):
            ww = dict(w)
            ww["a"] = s
            ws.append(law(ww))
        Z = sum(ws)
        return [x / Z for x in ws]
    indep_d = all(cond_a({**dict(zip(sites, vals)), "d": dval}) == cond_a({**dict(zip(sites, vals)), "d": 0})
                  for vals in product(range(M), repeat=4) for dval in range(M) if vals[3] == 0)
    if mut("markov_test_disagrees"):
        dep_c = not dep_c
    checks.check("C5", dep_c and indep_d, "T2/T6 direct Markov test on the plaquette: the conditional of b depends on c (co-recorded with b by d) and the conditional of a never depends on d (all configurations)")
    if exact:
        print(f"exact plaquette terms at the witness: bc={bc} ab={ab} bd={bd}; star leaves={tri}")


# ============================================================================================ family F
FENCES = (
    "This note describes formation laws on finite windows for every order; it states nothing infinite-volume beyond citing blocks 08–09 for the monotone class, nothing about the static law beyond block 01's equality case, and selects no order as physical.",
    "No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "no value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the physical order", "for every coupling", "selects the", "fires wake condition", "the Bridge weights", "the Bridge conjecture",
    "certified", "phase transition", "several static laws", "washes out", "toward the plane", "the trend",
    "the static law of Z^3 is unique", "arrow of time is derived",
)
CLAIM_INJECTIONS = {"claim_physical_order": "The leaves-first order is the physical order."}
CLASSICAL_NAMES = ("Hammersley", "Clifford", "Grimmett", "Möbius", "Mobius", "Brook", "Dobrushin", "Kolmogorov", "Perron")
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
    nsimp = "nsimp" + "lify("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln or nsimp in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.splitlines()[0].strip()
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem T3"):
            body = body + " (Hammersley)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — every configuration of the plaquette and the star (1296 each) for every one of their 48 orders; the mixed-difference ratios at witness assignments for k = 2..6 at three triples",
    "per_site: executed — the recorded set of every site in every order; the conditional of b and of a on the plaquette against their non-edge partners",
    "per_mode: executed — the canonical terms on the edges, the two non-edges, the triple and the quadruple of the plaquette; the leaves' triple of the star",
    "per_block: executed — the two windows' full potentials at the witnesses; the plaquette's {a, d} term on all 1296 configurations",
    "lattice_wide: finite-window factorization, containing graph and potential identities; converse and excluded-graph certification deferred",
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
    texts = [(ROOT / p).read_text(encoding="utf-8") if (ROOT / p).is_file() else "" for p in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the recorded-set Gibbs theorem — product form for every order (plaquette, star), mixed differences k = 2..6, the plaquette and star canonical potentials and a direct Markov test; exact; no order selected")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts[0], texts[1], texts[2], texts[3])
    family_b(checks, report)
    family_c(checks, report, exact)
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
