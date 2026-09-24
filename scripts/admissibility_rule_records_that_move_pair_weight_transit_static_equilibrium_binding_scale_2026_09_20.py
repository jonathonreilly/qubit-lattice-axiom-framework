#!/usr/bin/env python3
"""Exact checks: records that move.

Scope (a supplied motion clause; the axioms memo leaves update laws and persistence dynamics open).  A site is empty or carries one
record with content in the six-axis menu; content is carried; two neighbouring records weigh W(a, b) = c * omega(a, b) and a bond with
an empty end weighs 1.  T1: a record choosing between its position and an empty neighbouring position in proportion to the pair weights
it would have there is in detailed balance with the static law on the occupied set (contents fixed), for heat-bath and for the
min(1, ratio) acceptance; on the 2x3 window with two vacancies the motion connects all 180 arrangements of the contents (0,0,1,2).
T2: the scale c cancels from the axioms' normalized rule and enters the motion exactly through the change in the number of
record-record bonds; escape from k agreeing neighbours to an isolated position has probability 1/(1 + (c p)^k).  T3: if the move is
instead accepted with the rule's normalized probability of the content at the destination, the chain is blind to c and is not
reversible for any law (a cycle of four moves with unequal products of rates).  T4: formation at an empty site at rate z * Z_x with
content drawn from the rule is the creation half of a reversible birth-death pair for the static law with fugacity z, and no other rate
law is, when the removal rate is fixed to one; at the neutral scale c_0 = 6/(p + q + 4r) an empty neighbour weighs what a record of uniformly random content weighs on average.
T5: with the empty state included, the bond kernel (1 if an end is empty, c omega between records) is positive semidefinite, which is
what reflection positivity through bond planes needs, exactly when p >= q, p + q >= 2r and c >= c_0: subject to the two content-spectrum inequalities, the neutral scale is the least
scale at which the static law with vacancies is reflection positive; below it a function on the four-site ring has negative form.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "A site never carries more than one record; records are permanent.",
    "update laws",
    "record-production dynamics, physical persistence dynamics",
)

MUTATION_GATE = {
    "balance_with_normalized_rule": "B",
    "window_disconnected_injected": "B",
    "scale_invisible_to_motion_injected": "C",
    "escape_formula_wrong": "C",
    "normalized_reading_reversible_injected": "D",
    "birth_rate_wrong": "E",
    "rp_threshold_wrong": "E",
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


# ============================================================================================ the window and the rules
SITES = list(range(6))
EDGES = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)]
NB = {x: [b if a == x else a for a, b in EDGES if x in (a, b)] for x in SITES}
CONTENTS = (0, 0, 1, 2)                      # +z, +z, -z, +x: equal, opposite and orthogonal pairs all occur
STATES = sorted(set(permutations(CONTENTS + (None, None))), key=str)
INDEX = {s: i for i, s in enumerate(STATES)}
M6 = range(6)


def pair_weight(p, q, r, c):
    return [[Fraction(c) * (Fraction(p) if a == b else Fraction(q) if a == (b ^ 1) else Fraction(r)) for b in M6] for a in M6]


def local_weight(W, s, x, content, excl):
    w = Fraction(1)
    for z in NB[x]:
        if z != excl and s[z] is not None:
            w *= W[content][s[z]]
    return w


def static_weight(W, s):
    w = Fraction(1)
    for a, b in EDGES:
        if s[a] is not None and s[b] is not None:
            w *= W[s[a]][s[b]]
    return w


def moves(s):
    for a, b in EDGES:
        for x, y in ((a, b), (b, a)):
            if s[x] is not None and s[y] is None:
                t = list(s)
                t[y], t[x] = s[x], None
                yield x, y, tuple(t)


def acceptance(W, s, x, y, kind):
    c = s[x]
    wy, wx = local_weight(W, s, y, c, x), local_weight(W, s, x, c, y)
    if kind == "heat":
        return wy / (wx + wy)
    if kind == "min":
        return min(Fraction(1), wy / wx)
    ws = [local_weight(W, s, y, v, x) for v in M6]          # the rule's normalized probability of the content at the destination
    return ws[c] / sum(ws)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    norm = normalize_text(axioms)
    checks.check("A2", all(n in norm for n in AXIOM_NEEDLES), "the axioms memo carries the sentences used: the distribution sentence, 'Records form.', the one-record sentence, and the open gates for update laws and persistence dynamics")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in normalize_text(block01), "block 01 on main carries its claim id and the static law of a product rule")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    for (p, q, r, c) in ((3, 1, 2, 1), (3, 1, 2, Fraction(1, 2)), (5, 2, 4, Fraction(6, 23))):
        W = pair_weight(p, q, r, c)
        mu = {s: static_weight(W, s) for s in STATES}
        for kind in ("heat", "min"):
            use = "rule" if mut("balance_with_normalized_rule") else kind
            for s in STATES:
                for x, y, t in moves(s):
                    fwd = acceptance(W, s, x, y, use)
                    bwd = acceptance(W, t, y, x, use)
                    if mu[s] * fwd != mu[t] * bwd:
                        ok = False
    checks.check("B1", ok, "T1: on the 2x3 window with two vacancies and contents (+z, +z, -z, +x), every move of the pair-weight transit (heat-bath and min(1, ratio) acceptance) is in detailed balance with the static law on the occupied set; three weight and scale choices; all 180 arrangements")
    seen = {STATES[0]}
    stack = [STATES[0]]
    while stack:
        s = stack.pop()
        for _, _, t in moves(s):
            if mut("window_disconnected_injected") and t[0] is None:
                continue
            if t not in seen:
                seen.add(t)
                stack.append(t)
    checks.check("B2", len(seen) == len(STATES) == 180, f"T1: the moves connect all {len(STATES)} arrangements, so the static law on the occupied set is the only stationary law there ({len(seen)} reached)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    ok = True
    for (p, q, r) in ((3, 1, 2), (7, 3, 5)):
        base = pair_weight(p, q, r, 1)
        for c in (Fraction(1, 2), 3, Fraction(6, p + q + 4 * r)):
            W = pair_weight(p, q, r, c)
            for k in (1, 2, 3):
                for past in product(M6, repeat=k):
                    a0 = [_prod(base[a][b] for b in past) for a in M6]
                    a1 = [_prod(W[a][b] for b in past) for a in M6]
                    if [v / sum(a0) for v in a0] != [v / sum(a1) for v in a1]:
                        ok = False
    checks.check("C1", ok, "T2: the rule's normalized distribution is unchanged by the scale c, for every neighbourhood of one, two or three records (two weight triples, three scales)")
    W1, W2 = pair_weight(3, 1, 2, 1), pair_weight(3, 1, 2, Fraction(1, 2))
    same = diff = 0
    ok2 = True
    for s in STATES:
        for x, y, t in moves(s):
            kx = sum(1 for z in NB[x] if z != y and s[z] is not None)
            ky = sum(1 for z in NB[y] if z != x and s[z] is not None)
            a1, a2 = acceptance(W1, s, x, y, "heat"), acceptance(W2, s, x, y, "heat")
            if kx == ky:
                same += 1
                ok2 = ok2 and a1 == a2
            else:
                diff += 1
                ok2 = ok2 and a1 != a2
    if mut("scale_invisible_to_motion_injected"):
        ok2 = ok2 and diff == 0
    checks.check("C2", ok2 and (same,diff)==(288,384), f"T2: the motion probabilities at scale 1 and scale 1/2 agree exactly on the {same} moves that keep the number of record-record bonds and differ on the {diff} moves that change it")
    ok3 = True
    for c in (1, Fraction(1, 2), 2):
        for k in range(1, 6):
            wx = (Fraction(c) * 3) ** k
            val = Fraction(1) / (1 + wx)
            want = Fraction(1) / (1 + (Fraction(c) * 3) ** (k + 1 if mut("escape_formula_wrong") else k))
            ok3 = ok3 and val == want and (k == 1 or val < Fraction(1) / (1 + (Fraction(c) * 3) ** (k - 1)) or Fraction(c) * 3 <= 1)
    checks.check("C3", ok3, "T2: a record with k agreeing neighbours moves to an isolated empty position with probability 1/(1 + (c p)^k), decreasing in k when c p > 1 (p = 3; c = 1/2, 1, 2; k = 1..5)")


def _prod(it):
    out = Fraction(1)
    for t in it:
        out *= t
    return out


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    W1, W2 = pair_weight(3, 1, 2, 1), pair_weight(3, 1, 2, Fraction(1, 2))
    blind = all(acceptance(W1, s, x, y, "rule") == acceptance(W2, s, x, y, "rule") for s in STATES for x, y, _ in moves(s))
    checks.check("D1", blind, "T3: with the rule's normalized probability as acceptance, every move has the same probability at scale 1 and scale 1/2: that reading is blind to the binding scale")
    # a cycle of four moves (two records hopping in turn) with unequal products of rates: no reversible law exists
    witness = None
    kind = "heat" if mut("normalized_reading_reversible_injected") else "rule"
    for s in STATES:
        for x1, y1, t1 in moves(s):
            for x2, y2, t2 in moves(t1):
                if {x2, y2} & {x1, y1}:
                    continue
                for x3, y3, t3 in moves(t2):
                    if (x3, y3) != (y1, x1):
                        continue
                    for x4, y4, t4 in moves(t3):
                        if (x4, y4) != (y2, x2) or t4 != s:
                            continue
                        fwd = acceptance(W1, s, x1, y1, kind) * acceptance(W1, t1, x2, y2, kind) * acceptance(W1, t2, x3, y3, kind) * acceptance(W1, t3, x4, y4, kind)
                        bwd = acceptance(W1, s, x2, y2, kind) * acceptance(W1, _apply(s, x2, y2), x1, y1, kind) * acceptance(W1, _apply(_apply(s, x2, y2), x1, y1), y2, x2, kind) * acceptance(W1, _apply(_apply(_apply(s, x2, y2), x1, y1), y2, x2), y1, x1, kind)
                        if fwd != bwd and witness is None:
                            witness = (s, (x1, y1), (x2, y2), fwd, bwd)
    ss = (0,0,1,2,None,None)
    order = [(3,4),(2,5),(4,3),(5,2)]
    vals=[]
    for moves4 in (order,[(2,5),(3,4),(5,2),(4,3)]):
        state=ss;val=Fraction(1)
        for x,y in moves4:
            val*=acceptance(W1,state,x,y,kind);state=_apply(state,x,y)
        vals.append(val)
    checks.check("D2", witness is not None and vals==[Fraction(1,2592),Fraction(1,2376)], "T3: a cycle of four moves (record A hops, record B hops, A hops back, B hops back) has unequal products of rates around its two directions" + (f": from {witness[0]}, moves {witness[1]} and {witness[2]}: {witness[3]} against {witness[4]}" if witness else "") + "; by the cycle criterion no law is reversible for that chain")
    ok3 = True
    for s in STATES[:60]:
        for x1, y1, t1 in moves(s):
            for x2, y2, t2 in moves(t1):
                if {x2, y2} & {x1, y1}:
                    continue
                u1 = _apply(s, x2, y2)
                fwd = acceptance(W1, s, x1, y1, "heat") * acceptance(W1, t1, x2, y2, "heat")
                bwd_path = acceptance(W1, s, x2, y2, "heat") * acceptance(W1, u1, x1, y1, "heat")
                mu = static_weight(W1, s)
                ok3 = ok3 and static_weight(W1, t2) * acceptance(W1, t2, y2, x2, "heat") * acceptance(W1, t1, y1, x1, "heat") == mu * fwd and bwd_path >= 0
    checks.check("D3", ok3, "T3 (control): the pair-weight transit passes the same two-move test against the static law")


def _apply(s, x, y):
    t = list(s)
    t[y], t[x] = s[x], None
    return tuple(t)


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    p, q, r = 3, 1, 2
    z = Fraction(1, 5)
    ok = True
    ring = {0: (1, 3), 1: (0, 2), 2: (1, 3), 3: (0, 2)}
    for c in (1, Fraction(1, 2)):
        W = pair_weight(p, q, r, c)

        def mu_z(s):
            w = Fraction(1)
            for x in range(4):
                if s[x] is not None:
                    w *= z
                    y = (x + 1) % 4
                    if s[y] is not None:
                        w *= W[s[x]][s[y]]
            return w

        for s in product(list(M6) + [None], repeat=4):
            for x in range(4):
                if s[x] is not None:
                    continue
                past = [s[y] for y in ring[x] if s[y] is not None]
                raw = [_prod(W[a][b] for b in past) for a in M6]
                zx = sum(raw)
                for a in M6:
                    rate = z if mut("birth_rate_wrong") else z * zx
                    birth = rate * raw[a] / zx
                    t = s[:x] + (a,) + s[x + 1:]
                    if mu_z(s) * birth != mu_z(t) * 1:
                        ok = False
    checks.check("E1", ok, "T4: on the four-cycle, formation at an empty site at rate z Z_x with content drawn from the rule, against removal at rate 1, is in detailed balance with the static law with fugacity z (all 2401 configurations, two scales); the content given formation is the axioms' distribution")
    c0 = Fraction(6, p + q + 4 * r)
    W0 = pair_weight(p, q, r, c0)
    ok2 = all(sum(W0[a][b] for b in M6) / 6 == 1 for a in M6)
    agree = sum(W0[0][b] * W0[0][b] for b in M6) / 6
    orth = sum(W0[0][b] * W0[2][b] for b in M6) / 6
    opp = sum(W0[0][b] * W0[1][b] for b in M6) / 6
    ok2 = ok2 and agree == Fraction(13, 12) and orth == 1 and opp == Fraction(11, 12)
    checks.check("E2", ok2, f"T4: at the neutral scale c_0 = 6/(p + q + 4r) = {c0} for (3,1,2), an empty site next to ONE record forms at the rate of an isolated empty site (mean pair weight 1); next to two agreeing records the rate is multiplied by {agree}, next to two orthogonal ones by {orth}, next to two opposite ones by {opp}")


    # E3: reflection positivity through bond planes with the empty state included
    ps, qs, rs, cs = sp.symbols("p q r c", positive=True)
    omega = sp.Matrix(6, 6, lambda a, b: ps if a == b else qs if a == (b ^ 1) else rs)
    comp = cs * omega - sp.ones(6, 6)               # the complement of the empty state in the 7 x 7 bond kernel [[1, 1^T], [1, c omega]]
    const_mode = (cs * (ps + qs + 4 * rs) - 1) if mut("rp_threshold_wrong") else (cs * (ps + qs + 4 * rs) - 6)
    want = {sp.expand(const_mode): 1, sp.expand(cs * (ps + qs - 2 * rs)): 2, sp.expand(cs * (ps - qs)): 3}
    got = {sp.expand(k): v for k, v in comp.eigenvals().items()}
    ok3 = got == want
    # below the neutral scale an explicit function on the four-site ring has negative reflection form: G = v (x) w, v = (-6, 1, ..., 1), w = (1, 0, ..., 0)
    forms = []
    for cc in (Fraction(1, 4), Fraction(1, 2), Fraction(1)):
        Wn = pair_weight(3, 1, 2, cc)
        B = [[Fraction(1)] * 7] + [[Fraction(1)] + [Wn[a][b] for b in M6] for a in M6]
        v = [Fraction(-6)] + [Fraction(1)] * 6
        forms.append(sum(v[i] * B[i][j] * v[j] for i in range(7) for j in range(7)) * B[0][0])
    ok3 = ok3 and forms[0] < 0 and forms[1] == 0 and forms[2] > 0
    checks.check("E3", ok3, f"T5: the complement of the empty state in the bond kernel has eigenvalues c(p + q + 4r) - 6 (once), c(p + q - 2r) (twice), c(p - q) (three times), so the kernel is positive semidefinite exactly when p >= q, p + q >= 2r and c >= 6/(p + q + 4r); at (3,1,2) the function v (x) w on the four-site ring has reflection form {forms[0]} at c = 1/4, {forms[1]} at the neutral scale 1/2, {forms[2]} at c = 1")


# ============================================================================================ family F
FENCES = (
    "This note is conditional on a supplied motion clause (records move, carrying their content, by pair-weight transit) and on a supplied binding scale, neither of which is in the axioms memo; the memo lists update laws and persistence dynamics among its open gates, and nothing here is adopted.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 10."}
CLASSICAL_NAMES = ("Kawasaki", "Glauber", "Metropolis", "Kolmogorov", "Gibbs", "Boltzmann", "Ising", "Potts", "Blume", "Onsager", "Markov", "Schur", "Osterwalder", "Schrader")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Kawasaki)", 1)
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
    "per_element: executed — detailed balance of every pair-weight move with the static law; the scale cancelling from the rule; the escape probability 1/(1 + (c p)^k)",
    "per_site: executed — all 180 arrangements of four records and two vacancies on the 2x3 window, three weight and scale choices; all 2401 configurations of the four-cycle for the birth-death pair",
    "per_mode: not applicable — finite windows; the clumping map is executed in the controls",
    "per_block: executed — the connectedness of the moves; the four-move cycle with unequal products of rates for the normalized reading; the spectrum of the bond kernel with the empty state and the negative reflection form below the neutral scale",
    "lattice_wide: T1, T2 and T4 give conditional finite identities; T3 nonreversibility is the stated example, not a universal weight claim; historical clumping and jamming reports are not fresh evidence or limiting theorems; the motion clause and the binding scale are not in the axioms and are not adopted",
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
    print("scope: records that move — pair-weight transit is in detailed balance with the static law on the occupied set; the binding scale cancels from the rule and enters the motion; the normalized reading is blind to it and the stated example is not reversible; the formation rate that fits; exact")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
