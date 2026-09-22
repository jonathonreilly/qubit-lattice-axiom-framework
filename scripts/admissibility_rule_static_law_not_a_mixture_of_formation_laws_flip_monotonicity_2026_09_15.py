#!/usr/bin/env python3
"""Exact finite checks of the flip identities and declared witnesses.
The paired note defines the scope; broad negative certification is deferred.
Historical runner and mutation basenames remain recovery identifiers.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from functools import reduce
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_FLIP_IDENTITIES_AND_FINITE_MIXTURE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_formation_law_flip_identities_and_finite_mixture_witnesses_bounded_theorem_note_2026-09-15"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "Theorem B"
CENSUS_CLAIM_ID = "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13"
CENSUS_FRAGMENT = "372254646387017/12790481418000000"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "flip_inequality_wrong": "B",
    "strictness_criterion_wrong": "B",
    "normalizer_lemma_wrong": "B",
    "qualifying_mixture_not_static_claimed": "C",
    "mixture_equals_static_claimed": "C",
    "census_value_mismatch": "C",
    "cycle_lemma_wrong": "C",
    "environment_mixture_equals_joint_claimed": "D",
    "claim_static_law_derived": "F",
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
M = 6
P_, Q_, R_ = 3, 1, 2


def dec(x: Fraction, n: int = 6) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


def orbit_type(s: int, u: int) -> str:
    if s == u:
        return "p"
    if s // 2 == u // 2:
        return "q"
    return "r"


WEIGHTS = {"p": P_, "q": Q_, "r": R_}
PHI = [[WEIGHTS[orbit_type(s, t)] for t in range(M)] for s in range(M)]
Z1 = sum(PHI[0])
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
_KK: dict = {}


def Kk(vals: tuple) -> Fraction:
    if vals not in _KK:
        _KK[vals] = sum((reduce(lambda a, b: a * b, [F(PHI[s][a], Z1) for a in vals], F(1)) for s in range(M)), F(0)) if vals else F(1)
    return _KK[vals]


_COND: dict = {}


def cond(rec: tuple, s: int) -> Fraction:
    key = (rec, s)
    if key not in _COND:
        if not rec:
            _COND[key] = F(1, M)
        else:
            num = reduce(lambda a, b: a * b, [PHI[s][a] for a in rec], 1)
            den = sum(reduce(lambda a, b: a * b, [PHI[u][a] for a in rec], 1) for u in range(M))
            _COND[key] = F(num, den)
    return _COND[key]


def window(pos: dict):
    sites = sorted(pos)
    edges = [(i, j) for i in sites for j in sites if i < j and sum(abs(pos[i][k] - pos[j][k]) for k in range(3)) == 1]
    nb = {i: [j for j in sites if (min(i, j), max(i, j)) in edges] for i in sites}
    return sites, edges, nb


WINDOWS = {
    "plaquette": {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)},
    "2x3": {i: (i // 3, i % 3, 0) for i in range(6)},
    "cube": {i: (i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)},
    "path3": {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)},
    "star4": {0: (0, 0, 0), 1: (1, 0, 0), 2: (-1, 0, 0), 3: (0, 1, 0), 4: (0, -1, 0)},
    "domino": {0: (0, 0, 0), 1: (1, 0, 0)},
}


def recorded_sets(order, nb):
    S: set = set()
    out = {}
    for x in order:
        out[x] = tuple(y for y in nb[x] if y in S)
        S.add(x)
    return out


def weight(order, nb, v) -> Fraction:
    w = F(1)
    for x, A in recorded_sets(order, nb).items():
        if not A:
            w /= M
        else:
            w /= Kk(tuple(sorted(v[y] for y in A)))
    return w


def bad_union(order, nb) -> set:
    bad: set = set()
    for x, A in recorded_sets(order, nb).items():
        if len(A) >= 2:
            bad |= set(A)
    return bad


def multiset_key(order, nb):
    return tuple(sorted(A for A in (tuple(sorted(a)) for a in recorded_sets(order, nb).values()) if len(A) >= 2))


def static_law(sites, edges) -> dict:
    w = {}
    for v in product(range(M), repeat=len(sites)):
        x = 1
        for (i, j) in edges:
            x *= PHI[v[i]][v[j]]
        w[v] = x
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}


def seq_law(order, nb, sites) -> dict:
    law = {}
    for v in product(range(M), repeat=len(sites)):
        S: set = set()
        pr = F(1)
        for x in order:
            rec = tuple(sorted(v[y] for y in nb[x] if y in S))
            pr *= cond(rec, v[x])
            S.add(x)
        law[v] = pr
    return law


def tv(a: dict, b: dict) -> Fraction:
    return sum((abs(a[v] - b[v]) for v in a), F(0)) / 2


# ------------------------------------------------------------------ units in an environment (block 15's objects)
def nbrs(p):
    return [tuple(p[k] + d[k] for k in range(3)) for d in STEPS]


def make_unit(sites):
    U = list(sites)
    Uset = set(U)
    O = sorted({y for x in U for y in nbrs(x) if y not in Uset})
    return U, O


def joint_law(U, vO) -> dict:
    Uset = set(U)
    idx = {x: i for i, x in enumerate(U)}
    w = {}
    for v in product(range(M), repeat=len(U)):
        x_ = 1
        for i, x in enumerate(U):
            for y in nbrs(x):
                if y in Uset:
                    if idx[y] > i:
                        x_ *= PHI[v[i]][v[idx[y]]]
                elif y in vO:
                    x_ *= PHI[v[i]][vO[y]]
        w[v] = x_
    Z = sum(w.values())
    return {v: F(x_, Z) for v, x_ in w.items()}


def seq_law_env(U, vO, order) -> dict:
    Uset = set(U)
    idx = {x: i for i, x in enumerate(U)}
    law = {}
    for v in product(range(M), repeat=len(U)):
        S: set = set()
        pr = F(1)
        for x in order:
            rec = []
            for y in nbrs(x):
                if y in Uset and y in S:
                    rec.append(v[idx[y]])
                elif y in vO:
                    rec.append(vO[y])
            pr *= cond(tuple(sorted(rec)), v[idx[x]])
            S.add(x)
        law[v] = pr
    return law


def violates(U, vO, order) -> bool:
    Uset = set(U)
    S: set = set()
    for x in order:
        inside = [y for y in nbrs(x) if y in Uset and y in S]
        outside = [y for y in nbrs(x) if y in vO]
        if inside and len(inside) + len(outside) >= 2:
            return True
        S.add(x)
    return False


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, b01, census = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, block 01 and the census note, both on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f01, fc = normalize_text(b01), normalize_text(census)
    checks.check("A3", BLOCK01_CLAIM_ID in f01 and BLOCK01_FRAGMENT in f01 and CENSUS_CLAIM_ID in fc and CENSUS_FRAGMENT in fc,
                 "the parents' claim ids, block 01's Theorem B and the census note's Theorem 3 rational are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    ok = True
    strict_total = 0
    counts = {}
    for name in ("plaquette", "2x3", "cube"):
        sites, edges, nb = window(WINDOWS[name])
        n = len(sites)
        reps = {}
        for order in permutations(sites):
            key = multiset_key(order, nb)
            if key not in reps:
                reps[key] = order
        pairs = 0
        strict = 0
        orders_iter = reps.values() if name == "cube" else list(permutations(sites))
        for order in orders_iter:
            v = tuple([0] * n)
            w0 = weight(order, nb, v)
            bad = bad_union(order, nb)
            for z in sites:
                v2 = list(v)
                v2[z] = 1
                w1 = weight(order, nb, tuple(v2))
                pairs += 1
                if mut("flip_inequality_wrong") and name == "plaquette" and z == 0:
                    w1 = w0 - F(1, 10 ** 6)
                pred = z in bad
                if mut("strictness_criterion_wrong"):
                    pred = z not in bad
                ok = ok and (w1 >= w0) and ((w1 > w0) == pred)
                strict += int(w1 > w0)
        counts[name] = (pairs, strict, len(reps))
        strict_total += strict
        report.setdefault("classes", {})[name] = reps
    checks.check("B1", ok, "X1: the flip raises every order's weight ratio, strictly iff the site lies in a recorded set of size >= 2: " + "; ".join(f"{n}: {c[0]} pairs ({c[2]} classes), {c[1]} strict" for n, c in counts.items()))
    pp, qq, rr = sp.symbols("p q r", positive=True)
    lem = True
    for k in range(2, 7):
        ZZ = pp + qq + 4 * rr
        Kb = [pp / ZZ, qq / ZZ, rr / ZZ, rr / ZZ, rr / ZZ, rr / ZZ]
        Kmb = [qq / ZZ, pp / ZZ, rr / ZZ, rr / ZZ, rr / ZZ, rr / ZZ]
        Kc = [rr / ZZ, rr / ZZ, pp / ZZ, qq / ZZ, rr / ZZ, rr / ZZ]
        same = sum(Kb[s] ** k for s in range(6))
        anti = sum(Kmb[s] * Kb[s] ** (k - 1) for s in range(6))
        orth = sum(Kc[s] * Kb[s] ** (k - 1) for s in range(6))
        pred_anti = (pp - qq) / ZZ * ((pp / ZZ) ** (k - 1) - (qq / ZZ) ** (k - 1))
        pred_orth = ((pp - rr) * (pp ** (k - 1) - rr ** (k - 1)) + (qq - rr) * (qq ** (k - 1) - rr ** (k - 1))) / ZZ ** k
        if mut("normalizer_lemma_wrong"):
            pred_anti = pred_anti * (k + 1) / k
        lem = lem and sp.simplify(same - anti - pred_anti) == 0 and sp.simplify(same - orth - pred_orth) == 0
    checks.check("B2", lem, "the normalizer lemma: K_k(b..b) - K_k(-b,b..b) = ((p-q)/Z_1)[(p/Z_1)^(k-1) - (q/Z_1)^(k-1)] and the orthogonal form, symbolically for k = 2..6")


# ============================================================================================ family C
def family_c(checks: Checks, report: dict, exact: bool) -> None:
    random.seed(20260915)
    ok_q, ok_bad = True, True
    details = []
    for name in ("path3", "star4"):
        sites, edges, nb = window(WINDOWS[name])
        st = static_law(sites, edges)
        orders = list(permutations(sites))
        good = [o for o in orders if not bad_union(o, nb)]
        laws = {}
        for o in orders:
            key = multiset_key(o, nb)
            if key not in laws:
                laws[key] = seq_law(o, nb, sites)
        mix_good = {v: sum((laws[multiset_key(o, nb)][v] for o in good), F(0)) / len(good) for v in st}
        wts = {o: F(random.randint(1, 9)) for o in good}
        tot = sum(wts.values())
        mix_good2 = {v: sum((wts[o] * laws[multiset_key(o, nb)][v] for o in good), F(0)) / tot for v in st}
        eq = tv(mix_good, st) == 0 and tv(mix_good2, st) == 0
        if mut("qualifying_mixture_not_static_claimed"):
            eq = not eq
        ok_q = ok_q and eq
        diffs = []
        for _ in range(3):
            w2 = {o: F(random.randint(1, 9)) for o in orders}
            t2 = sum(w2.values())
            mix = {v: sum((w2[o] * laws[multiset_key(o, nb)][v] for o in orders), F(0)) / t2 for v in st}
            diffs.append(tv(mix, st))
        ok_bad = ok_bad and all(d > 0 for d in diffs)
        details.append(f"{name}: {len(good)}/{len(orders)} qualifying")
    checks.check("C1", ok_q, "X2 (if): on the path and the four-leaf star, the uniform and a pseudo-random mixture over qualifying orders equal the static law exactly: " + "; ".join(details))
    if mut("mixture_equals_static_claimed"):
        ok_bad = False
    checks.check("C2", ok_bad, "X2 finite samples: three pseudo-random mixtures charging non-qualifying orders differ from the static law on the path and the star")
    sites, edges, nb = window(WINDOWS["2x3"])
    st6 = static_law(sites, edges)
    reps = report["classes"]["2x3"]
    laws6 = {key: seq_law(o, nb, sites) for key, o in reps.items()}
    counts = {}
    for o in permutations(sites):
        key = multiset_key(o, nb)
        counts[key] = counts.get(key, 0) + 1
    uni = {v: sum((F(counts[k], 720) * laws6[k][v] for k in laws6), F(0)) for v in st6}
    d_uni = tv(uni, st6)
    census = F(372254646387017, 12790481418000000)
    c3 = d_uni == census
    if mut("census_value_mismatch"):
        c3 = d_uni == census * F(1001, 1000)
    rnd = []
    for _ in range(2):
        w2 = {k: F(random.randint(1, 9)) for k in laws6}
        t2 = sum(w2.values())
        mix = {v: sum((w2[k] * laws6[k][v] for k in laws6), F(0)) / t2 for v in st6}
        rnd.append(tv(mix, st6))
    sites4, edges4, nb4 = window(WINDOWS["plaquette"])
    st4 = static_law(sites4, edges4)
    laws4 = {key: seq_law(o, nb4, sites4) for key, o in report["classes"]["plaquette"].items()}
    w4 = {k: F(random.randint(1, 9)) for k in laws4}
    t4 = sum(w4.values())
    mix4 = {v: sum((w4[k] * laws4[k][v] for k in laws4), F(0)) / t4 for v in st4}
    checks.check("C3", c3 and all(d > 0 for d in rnd) and tv(mix4, st4) > 0, f"X2: on 2x3 the uniform mixture over 720 orders (28 classes) is at the census note's distance {d_uni} from the static law; two pseudo-random class mixtures and a plaquette mixture differ (TV " + ", ".join(dec(d) for d in rnd) + f", {dec(tv(mix4, st4))})")
    cyc = True
    for name in ("plaquette", "2x3", "cube"):
        keys = report["classes"][name].keys()
        cyc = cyc and all(len(k) >= 1 for k in keys)
    if mut("cycle_lemma_wrong"):
        cyc = not cyc
    checks.check("C4", cyc, "X2 (cycle lemma): every multiset class of the plaquette, 2x3 and the cube contains a recorded set of size >= 2, so no order qualifies")
    if exact:
        print("exact random mixture TVs on 2x3:", [str(d) for d in rnd])


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    random.seed(7)
    ok_env, ok_iso = True, True
    for name in ("domino", "path3"):
        U, O = make_unit(list(WINDOWS[name].values()))
        vO = {y: 0 for y in O}
        J = joint_law(U, vO)
        orders = list(permutations(U))
        laws = {o: seq_law_env(U, vO, o) for o in orders}
        allviol = all(violates(U, vO, o) for o in orders)
        w2 = {o: F(random.randint(1, 9)) for o in orders}
        t2 = sum(w2.values())
        mix = {v: sum((w2[o] * laws[o][v] for o in orders), F(0)) / t2 for v in J}
        ok_env = ok_env and allviol and tv(mix, J) > 0 and all(tv(laws[o], J) > 0 for o in orders)
        Ji = joint_law(U, {})
        lawsi = {o: seq_law_env(U, {}, o) for o in orders}
        good = [o for o in orders if not violates(U, {}, o)]
        mixi = {v: sum((lawsi[o][v] for o in good), F(0)) / len(good) for v in Ji}
        ok_iso = ok_iso and tv(mixi, Ji) == 0 and len(good) >= 1
    if mut("environment_mixture_equals_joint_claimed"):
        ok_env = False
    checks.check("D1", ok_env, "X3: the domino and the path in the all-+x environment — every order violates the criterion, every order and a pseudo-random mixture differ from the joint law")
    checks.check("D2", ok_iso, "X3 (isolated): the uniform mixture over the qualifying orders of the domino and the path equals the joint law")


# ============================================================================================ family F
FENCES = ('This note proves flip identities and a sufficient static-mixture construction and reports finite mixture witnesses; universal mixture necessity and cycle or environment exclusions are deferred; no order, mixture, rule or coupling is selected as physical, and no clause is adopted.', 'No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The menu, weights and mixture conventions are declared mathematical inputs, not empirical or axiom-selected values.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical mixture", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "the static law is derived", "the formation reading is refuted", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_static_law_derived": "Hence the static law is derived from the formation reading."}
CLASSICAL_NAMES = ("Brook", "Besag", "Toom", "Peierls", "Fourier", "Dobrushin", "Gillespie", "Eden", "Hammersley")
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
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem X2"):
            body = body + " (a Dobrushin-type comparison)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the normalizer lemma for k = 2..6 symbolically; the flip on every order-site pair of the plaquette (96) and 2x3 (4320) and every class-site pair of the cube (4336)",
    "per_site: executed — every pattern of the path, the star, the plaquette and 2x3 in the mixture checks; every pattern of the domino and the path in the environment checks",
    "per_mode: executed — every order class of the plaquette (4), 2x3 (28) and the cube (542); every order of the path, the star, the domino",
    "per_block: executed — six windows, two environments",
    "lattice_wide: checked and not executed — written conditional identities and sufficient constructions; no infinite-lattice execution; broad negative certification deferred",
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
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: flip identities and declared finite witnesses; broad negative certification deferred; no clause adopted")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts)
    family_b(checks, report)
    family_c(checks, report, exact)
    family_d(checks)
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
