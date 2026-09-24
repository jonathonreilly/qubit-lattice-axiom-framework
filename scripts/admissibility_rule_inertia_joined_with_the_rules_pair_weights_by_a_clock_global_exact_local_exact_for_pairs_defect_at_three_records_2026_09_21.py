#!/usr/bin/env python3
"""Exact checks: inertia joined with the rule's pair weights by a clock (six-axis menu, 3x3x3 torus; clauses supplied, not adopted).

The law with vacancies of block 39 gives a configuration the weight pi(C) = product over adjacent occupied pairs of c omega(a, b), omega = p for
equal contents, q for opposite, r for orthogonal.  Block 44's streaming: the record at x with content s has the target x + e_s; an empty target
is entered, an occupied target exchanges contents with the record.  Every record of a configuration has exactly one such event and exactly one
predecessor through such an event, so the unit-clock dynamics keeps the uniform measure.
T1 GLOBAL clock: if every event of C runs at the rate 1/pi(C), pi is stationary (a change of time), whatever the weights and the density.
T2 LOCAL clock: if the event of the record at x runs at the rate 1/pi_x(C), pi_x the product of the pair weights of site x, then
out(C) - in(C) = sum over records whose site behind is occupied of W_0 [A_b(u) - A_x(u)], u the content behind, A the weight of u among the
other neighbours of the two sites, W_0 the pairs that touch neither site: zero for two records, not zero for three (3168 of 70200).
T3: in the two-record sector the stationary law is the rule's pair law; at the neutral scale c_0 = 6/(p + q + 4r) the mean pair weight is one.
T4: re-drawing a bond's contents on its momentum class with probabilities proportional to pi satisfies detailed balance and conserves momentum.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_INERTIA_JOINED_WITH_THE_RULES_PAIR_WEIGHTS_BY_A_CLOCK_GLOBAL_CLOCK_EXACT_LOCAL_CLOCK_EXACT_FOR_PAIRS_DEFECT_AT_THREE_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_inertia_joined_with_the_rules_pair_weights_by_a_clock_global_clock_exact_local_clock_exact_for_pairs_defect_at_three_records_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = ("A site never carries more than one record; records are permanent.",)

MUTATION_GATE = {
    "blocked_record_waits": "B",
    "global_clock_uses_arrival_weight": "B",
    "local_clock_claimed_exact_at_three": "C",
    "defect_identity_wrong_site": "C",
    "neutral_scale_wrong": "D",
    "redraw_uniform_with_weights": "D",
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
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]      # content d and d ^ 1 are opposite
SIDE = 3
SITES = list(product(range(SIDE), repeat=3))
ORIGIN = (0, 0, 0)


def shift(x, d, sign=1):
    return tuple((x[i] + sign * E[d][i]) % SIDE for i in range(3))


NEIGHBOURS = {x: [shift(x, d) for d in range(6)] for x in SITES}


def omega(a, b, w):
    if a == b:
        return w[0]
    if a == (b ^ 1):
        return w[1]
    return w[2]


def site_weight(conf, x, w, skip=None):
    val = 1
    for y in NEIGHBOURS[x]:
        if y in conf and y != skip:
            val = val * omega(conf[x], conf[y], w)
    return val


def weight(conf, w):
    val = 1
    items = list(conf.items())
    for i, (x, a) in enumerate(items):
        for y, b in items[i + 1:]:
            if y in NEIGHBOURS[x]:
                val = val * omega(a, b, w)
    return val


def predecessor(conf, x):
    """The unique configuration from which the record now at x arrived by its own event; returns (configuration, site of the active record)."""
    s = conf[x]
    b = shift(x, s, -1)
    pred = dict(conf)
    if b not in conf:
        del pred[x]
        pred[b] = s
    else:
        pred[b], pred[x] = s, conf[b]
    return pred, b


def sector(nrec):
    others = [s for s in SITES if s != ORIGIN]
    for pos in combinations(others, nrec - 1):
        for contents in product(range(6), repeat=nrec):
            conf = {ORIGIN: contents[0]}
            for k, xk in enumerate(pos):
                conf[xk] = contents[k + 1]
            yield conf


def successor(conf, x):
    s = conf[x]
    y = shift(x, s)
    nxt = dict(conf)
    if y not in conf:
        del nxt[x]
        nxt[y] = s
    else:
        nxt[x], nxt[y] = conf[y], s
    return nxt


def key(conf):
    return tuple(sorted(conf.items()))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", bool(note) and CLAIM_ID in note, "the note exists and carries its claim id")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the sentence used")


# ============================================================================================ family B (T1)
def family_b(checks: Checks, scan) -> None:
    # the unit-clock event graph: every record has one event and one predecessor event, and they are inverse to one another
    ok = True
    count = 0
    for conf in sector(2):
        for x in conf:
            nxt = successor(conf, x)
            if mut("blocked_record_waits") and shift(x, conf[x]) in conf:
                nxt = dict(conf)                                        # a blocked attempt that does nothing
            y = shift(x, conf[x])
            back, _ = predecessor(nxt, y)
            ok = ok and key(back) == key(conf) and sum(E[c][i] for c in nxt.values() for i in range(3)) == sum(E[c][i] for c in conf.values() for i in range(3)) and sorted(nxt.values()) == sorted(conf.values())
            count += 1
    checks.check("B1", ok, f"T1: every record of a configuration has exactly one streaming event (enter the empty target, or exchange contents with the occupied one) and the predecessor map inverts it ({count} events of the two-record sector); events keep the number of records and their contents, hence the momentum: the unit-clock dynamics has as many ways into a configuration as out of it")
    w = (3, 1, 2)
    bad2 = sum(1 for conf in sector(2) if global_defect(conf, w) != 0)
    bad3 = scan["global_bad"]
    checks.check("B2", bad2 == 0 and bad3 == 0 and scan["n2"]==936 and scan["n3"]==70200, f"T1: with every event of C running at the rate 1/pi(C), the flow of pi into a configuration equals the flow out of it at all {scan['n2']} two-record and {scan['n3']} three-record configurations (weights 3, 1, 2): pi is stationary under the global clock")


def global_defect(conf, w):
    pi_c = weight(conf, w)
    out = F(0)
    inn = F(0)
    for x in conf:
        out += F(pi_c, pi_c)
        pred, _ = predecessor(conf, x)
        pi_p = weight(pred, w)
        rate_weight = weight(conf, w) if mut("global_clock_uses_arrival_weight") else pi_p
        inn += F(pi_p, rate_weight)
    return out - inn


# ============================================================================================ family C (T2)
def local_defect(conf, w):
    pi_c = weight(conf, w)
    total = F(0)
    for x in conf:
        total += F(pi_c, site_weight(conf, x, w))
        pred, active = predecessor(conf, x)
        total -= F(weight(pred, w), site_weight(pred, active, w))
    return total


def identity_defect(conf, w):
    """sum over records whose site behind is occupied of W_0 [A_b(u) - A_x(u)]."""
    total = F(0)
    for x, s in conf.items():
        b = shift(x, s, -1)
        if b not in conf:
            continue
        u = conf[b]
        rest = {z: c for z, c in conf.items() if z not in (x, b)}
        w0 = weight(rest, w)
        a_b = 1
        for y in NEIGHBOURS[b]:
            if y in rest:
                a_b *= omega(u, rest[y], w)
        a_x = 1
        for y in NEIGHBOURS[x]:
            if y in rest:
                a_x *= omega(u, rest[y], w)
        if mut("defect_identity_wrong_site"):
            a_x = 1
        total += w0 * (a_b - a_x)
    return total


def three_record_scan():
    w = (3, 1, 2)
    res = {"n2": sum(1 for _ in sector(2)), "n3": 0, "global_bad": 0, "local_bad": 0, "identity_bad": 0, "largest": F(0), "witness": None, "clean_but_bad": 0}
    for conf in sector(3):
        res["n3"] += 1
        if global_defect(conf, w) != 0:
            res["global_bad"] += 1
        d = local_defect(conf, w)
        if d != identity_defect(conf, w):
            res["identity_bad"] += 1
        if d != 0:
            res["local_bad"] += 1
            if abs(d) > abs(res["largest"]):
                res["largest"], res["witness"] = d, dict(conf)
            crowded = False
            for x, s in conf.items():
                b = shift(x, s, -1)
                if b in conf and any(z in NEIGHBOURS[x] or z in NEIGHBOURS[b] for z in conf if z not in (x, b)):
                    crowded = True
            if not crowded:
                res["clean_but_bad"] += 1
    return res


def family_c(checks: Checks, scan) -> None:
    ok = True
    for w in ((3, 1, 2), (5, 2, 4), (F(3, 2), F(1, 2), F(1))):
        ok = ok and all(local_defect(conf, w) == 0 for conf in sector(2))
    checks.check("C1", ok, f"T2: with the event of the record at x running at the rate 1/pi_x(C), pi is stationary at all {scan['n2']} two-record configurations, for the weights (3, 1, 2), (5, 2, 4) and (3, 1, 2) at the neutral scale 1/2")
    bad = 0 if mut("local_clock_claimed_exact_at_three") else 3168
    checks.check("C2", scan["local_bad"] == bad and scan["largest"] == 3 and scan["witness"] is not None, f"T2: at three records the local clock fails at {scan['local_bad']} of {scan['n3']} configurations; the largest defect is {scan['largest']}, at {sorted(scan['witness'].items()) if scan['witness'] else None} (contents 0..5 = +x, -x, +y, -y, +z, -z)")
    checks.check("C3", scan["identity_bad"] == 0 and scan["clean_but_bad"] == 0, f"T2: at every three-record configuration out - in = sum over records whose site behind is occupied of W_0 [A_b(u) - A_x(u)]; it vanishes whenever no such pair of sites has a third record next to it ({scan['n3']} configurations)")


# ============================================================================================ family D (T3, T4)
def family_d(checks: Checks) -> None:
    ok = True
    shown = []
    for p, q, r in ((3, 1, 2), (5, 2, 4), (12, 1, 2)):
        c0 = F(6, p + q + 4 * r)
        if mut("neutral_scale_wrong"):
            c0 = F(6, p + q + r)
        mean = (c0 * p + c0 * q + 4 * c0 * r) / 6
        ok = ok and mean == 1
        shown.append(f"({p},{q},{r}): c_0 = {c0}")
    # the two-record stationary law under either clock is pi itself: adjacent pairs carry c omega(a, b), others 1
    w = (3, 1, 2)
    adj = {weight(conf, w) for conf in sector(2) if any(y in conf for y in NEIGHBOURS[ORIGIN])}
    far = {weight(conf, w) for conf in sector(2) if not any(y in conf for y in NEIGHBOURS[ORIGIN])}
    ok = ok and adj == {1, 2, 3} and far == {1}
    checks.check("D1", ok, "T3: in the two-record sector the stationary law is the rule's pair law (weights p, q, r for adjacent equal, opposite and orthogonal contents, 1 otherwise); at the neutral scale the mean pair weight over the partner's content is one: " + "; ".join(shown))
    # heat-bath re-draw of a bond's two contents on its momentum class, in the presence of a third record
    ok = True
    classes = 0
    for third_content in range(6):
        for a, b in product(range(6), repeat=2):
            base = {(0, 0, 0): a, (1, 0, 0): b, (0, 1, 0): third_content}
            mom = tuple(E[a][i] + E[b][i] for i in range(3))
            cls = [(a2, b2) for a2, b2 in product(range(6), repeat=2) if tuple(E[a2][i] + E[b2][i] for i in range(3)) == mom]
            weights = []
            for a2, b2 in cls:
                conf = dict(base)
                conf[(0, 0, 0)], conf[(1, 0, 0)] = a2, b2
                weights.append(F(weight(conf, w)))
            tot = sum(weights)
            probs = [F(1, len(cls)) for _ in cls] if mut("redraw_uniform_with_weights") else [wt / tot for wt in weights]
            for i in range(len(cls)):
                for j in range(len(cls)):
                    ok = ok and weights[i] * probs[j] == weights[j] * probs[i]
            ok = ok and (len(cls) in (1, 2, 6))
            classes += 1
    checks.check("D2", ok, f"T4: re-drawing the two contents of a bond on their momentum class (classes of 1, 2 or 6 ordered pairs) with probabilities proportional to pi satisfies detailed balance with respect to pi and conserves the pair's momentum, also next to a third record ({classes} cases)")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied inertial clause of block 44 and the supplied law with vacancies of block 39; it reports which clocks let streaming keep that law stationary; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Navier", "Stokes", "Bernoulli", "Boltzmann", "Gibbs", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Markov", "Metropolis", "Glauber", "Kawasaki", "Krauth", "Diaconis", "Schutz", "Spitzer", "Liggett", "Kolmogorov")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Metropolis)", 1)
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
    "per_element: executed — every event of the two-record sector and its inverse; the momentum classes of a bond (1, 2 or 6 ordered pairs)",
    "per_site: executed — the local-clock balance at all 936 two-record configurations for three weight sets; the defect identity at all 70200 three-record configurations",
    "per_mode: not applicable — the retained finite identities concern local rates and integrated flux, not a mode spectrum",
    "per_block: executed — the global-clock balance in both sectors; the count 3168 and the largest defect 3 with its configuration; the neutral scale for three weight triples; detailed balance of the weighted re-draw next to a third record",
    "lattice_wide: T1 is a change of time and holds for any weights, density and window once the unit-clock dynamics keeps the uniform measure (block 44); T2's identity is proved for any number of records and checked at two and three; whether some local clock is exact at all densities is open",
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
    scan = three_record_scan()
    family_a(checks, texts)
    family_b(checks, scan)
    family_c(checks, scan)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: inertial streaming with the rule's pair weights — a global clock 1/pi keeps the law with vacancies stationary at any density; a local clock 1/pi_x is exact for two records and fails at three with an exact defect identity; the pair law and the neutral scale; weighted re-drawing of contents")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
