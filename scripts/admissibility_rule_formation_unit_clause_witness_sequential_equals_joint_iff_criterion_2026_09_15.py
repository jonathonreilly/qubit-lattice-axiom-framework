#!/usr/bin/env python3
"""Exact finite checks of the unit identities and declared witnesses.
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
    "docs/ADMISSIBILITY_RULE_FORMATION_UNIT_CONDITIONAL_IDENTITIES_AND_FINITE_WITNESSES_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
    "docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_formation_unit_conditional_identities_and_finite_witnesses_bounded_theorem_note_2026-09-15"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "Theorem B"
CENSUS_CLAIM_ID = "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13"
CENSUS_FRAGMENT = "joint formation"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "reconstruction_wrong": "B",
    "normalizer_lemma_wrong": "B",
    "criterion_mismatch_isolated": "C",
    "criterion_mismatch_environment": "C",
    "star_separates_in_isolation_claimed": "D",
    "star_class_tv_forged": "D",
    "plaquette_order_equals_joint_claimed": "D",
    "class_ratios_not_monotone_claimed": "D",
    "environment_unit_agrees_claimed": "E",
    "single_site_differs_claimed": "E",
    "claim_unit_clause_adopted": "F",
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


def dec(x: Fraction, n: int = 5) -> str:
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


def seq_law(U, vO, order) -> dict:
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


def tv(a: dict, b: dict) -> Fraction:
    return sum((abs(a[v] - b[v]) for v in a), F(0)) / 2


def violates(U, vO, order) -> bool:
    """the criterion's failure: some site records an inside neighbour together with a second recorded neighbour"""
    Uset = set(U)
    S: set = set()
    for x in order:
        inside = [y for y in nbrs(x) if y in Uset and y in S]
        outside = [y for y in nbrs(x) if y in vO]
        if inside and len(inside) + len(outside) >= 2:
            return True
        S.add(x)
    return False


CENTER = (0, 0, 0)
LEAVES = nbrs(CENTER)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, b01, census = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, block 01 and the census note, both on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f01, fc = normalize_text(b01), normalize_text(census).lower()
    checks.check("A3", BLOCK01_CLAIM_ID in f01 and BLOCK01_FRAGMENT in f01 and CENSUS_CLAIM_ID in fc and CENSUS_FRAGMENT in fc,
                 "the parents' claim ids, block 01's Theorem B and the census note's mention of joint formation are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    random.seed(20260915)
    n = 3
    pats = list(product(range(M), repeat=n))
    w = {v: F(random.randint(1, 50), random.randint(1, 50)) for v in pats}
    Z = sum(w.values())
    mu = {v: w[v] / Z for v in pats}
    def conditional(v, i, s):
        base = list(v)
        tot = F(0)
        for u in range(M):
            base[i] = u
            tot += mu[tuple(base)]
        base[i] = s
        return mu[tuple(base)] / tot
    ref = pats[0]
    rec = {}
    for v in pats:
        ratio = F(1)
        cur = list(ref)
        for i in range(n):
            before = tuple(cur)
            cur[i] = v[i]
            after = tuple(cur)
            ratio *= conditional(after, i, v[i]) / conditional(before, i, ref[i])
        rec[v] = ratio
    tot = sum(rec.values())
    rec = {v: rec[v] / tot for v in pats}
    if mut("reconstruction_wrong"):
        rec[ref] += F(1, 10 ** 6)
    checks.check("B1", all(rec[v] == mu[v] for v in pats), "U1: a pseudo-random positive law on three sites (216 patterns) is reconstructed exactly from its one-site conditionals by the telescoping ratio argument")
    pp, qq, rr, kk = sp.symbols("p q r k", positive=True)
    ok = True
    for k in range(2, 7):
        ZZ = pp + qq + 4 * rr
        Kb = [pp / ZZ, qq / ZZ, rr / ZZ, rr / ZZ, rr / ZZ, rr / ZZ]  # K(b, s) for s = b, -b, c, -c, d, -d
        Kmb = [qq / ZZ, pp / ZZ, rr / ZZ, rr / ZZ, rr / ZZ, rr / ZZ]
        Kc = [rr / ZZ, rr / ZZ, pp / ZZ, qq / ZZ, rr / ZZ, rr / ZZ]
        same = sum(Kb[s] ** k for s in range(6))
        anti = sum(Kmb[s] * Kb[s] ** (k - 1) for s in range(6))
        orth = sum(Kc[s] * Kb[s] ** (k - 1) for s in range(6))
        pred_anti = (pp - qq) / ZZ * ((pp / ZZ) ** (k - 1) - (qq / ZZ) ** (k - 1))
        pred_orth = ((pp - rr) * (pp ** (k - 1) - rr ** (k - 1)) + (qq - rr) * (qq ** (k - 1) - rr ** (k - 1))) / ZZ ** k
        if mut("normalizer_lemma_wrong"):
            pred_anti = pred_anti * (k + 1) / k
        ok = ok and sp.simplify(same - anti - pred_anti) == 0 and sp.simplify(same - orth - pred_orth) == 0
        num = same.subs({pp: P_, qq: Q_, rr: R_}) - anti.subs({pp: P_, qq: Q_, rr: R_})
        ok = ok and num > 0
    checks.check("B2", ok, "U2 lemma: K_k(b..b) - K_k(-b,b..b) = ((p-q)/Z_1)[(p/Z_1)^(k-1) - (q/Z_1)^(k-1)] and the orthogonal form, symbolically for k = 2..6; positive at (3,1,2)")


# ============================================================================================ family C
def family_c(checks: Checks, report: dict) -> None:
    ok_iso = True
    star_U, star_O = make_unit([CENTER] + LEAVES)
    Jstar = joint_law(star_U, {})
    star_tv = {}
    for k in (0, 1, 2, 3, 6):
        order = LEAVES[:k] + [CENTER] + LEAVES[k:]
        L = seq_law(star_U, {}, order)
        star_tv[k] = tv(L, Jstar)
        ok_iso = ok_iso and ((star_tv[k] == 0) == (not violates(star_U, {}, order)))
    report["star"] = (star_U, star_O, Jstar, star_tv)
    for sites in ([(0, 0, 0), (1, 0, 0)], [(0, 0, 0), (1, 0, 0), (2, 0, 0)], [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]):
        U, O = make_unit(sites)
        J = joint_law(U, {})
        for order in permutations(U):
            eq = tv(seq_law(U, {}, order), J) == 0
            ok_iso = ok_iso and (eq == (not violates(U, {}, order)))
        if len(sites) == 4:
            report["plq"] = (U, O, J)
    if mut("criterion_mismatch_isolated"):
        ok_iso = False
    checks.check("C1", ok_iso, "finite isolated comparisons: exact equality with the joint law holds iff the criterion holds, on every order of the domino (2), the path (6), the plaquette (24) and the star's classes k = 0, 1, 2, 3, 6")
    random.seed(5)
    ok_env = True
    env_res = {}
    for name, sites in (("domino", [(0, 0, 0), (1, 0, 0)]), ("path3", [(0, 0, 0), (1, 0, 0), (2, 0, 0)]), ("single", [(0, 0, 0)])):
        U, O = make_unit(sites)
        vO = {y: random.randrange(M) for y in O}
        J = joint_law(U, vO)
        res = []
        for order in permutations(U):
            eq = tv(seq_law(U, vO, order), J) == 0
            res.append((eq, violates(U, vO, order)))
            ok_env = ok_env and (eq == (not res[-1][1]))
        env_res[name] = res
    report["env_small"] = env_res
    if mut("criterion_mismatch_environment"):
        ok_env = False
    checks.check("C2", ok_env, "finite fixed-environment comparisons: on the domino, the path and a single site with pseudo-random outside records, equality holds iff the criterion holds, on every order")
    vO_allx = {y: 0 for y in star_O}
    random.seed(3)
    vO_mixed = {y: random.randrange(M) for y in star_O}
    env_star = {}
    ok_star = True
    for ename, vO in (("all+x", vO_allx), ("mixed", vO_mixed)):
        Je = joint_law(star_U, vO)
        for k in ((0, 6) if ename == "all+x" else (0, 1, 6)):
            order = LEAVES[:k] + [CENTER] + LEAVES[k:]
            d = tv(seq_law(star_U, vO, order), Je)
            env_star[(ename, k)] = d
            ok_star = ok_star and d > 0 and violates(star_U, vO, order)
    report["env_star"] = (env_star, vO_mixed)
    checks.check("C3", ok_star, "finite fixed-environment comparisons: the star's center-first and leaves-first orders in all-+x, and center-first, one-leaf-first and leaves-first in the mixed environment all violate the criterion and all differ from the joint law: " + ", ".join(f"{e}/k={k}: {dec(d)}" for (e, k), d in env_star.items()))


# ============================================================================================ family D
def family_d(checks: Checks, report: dict) -> None:
    star_U, star_O, Jstar, star_tv = report["star"]
    expected = {0: F(0), 1: F(0), 2: F(1, 72), 3: F(5, 144), 6: F(103375, 1492992)}
    d1 = all(star_tv[k] == expected[k] for k in expected)
    if mut("star_separates_in_isolation_claimed"):
        d1 = all(star_tv[k] > 0 for k in expected)
    if mut("star_class_tv_forged"):
        d1 = star_tv[2] == F(1, 73)
    checks.check("D1", d1, "U3: isolated star — sequential equals joint for k = 0, 1 leaves before the center and differs for k = 2, 3, 6 with TV 1/72, 5/144, 103375/1492992")
    U, O, J = report["plq"]
    dists = {}
    for order in permutations(U):
        d = tv(seq_law(U, {}, order), J)
        dists[d] = dists.get(d, 0) + 1
    plq_ok = dists == {F(455, 31176): 16, F(37, 1299): 8}
    if mut("plaquette_order_equals_joint_claimed"):
        plq_ok = F(0) in dists
    # class ratios monotone in the diagonal normalizer
    idx = {x: i for i, x in enumerate(U)}
    def prodK(v):
        x_ = F(1)
        for i, x in enumerate(U):
            for y in nbrs(x):
                if y in idx and idx[y] > i:
                    x_ *= F(PHI[v[i]][v[idx[y]]], Z1)
        return x_
    P1, P3, P4 = (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 2, 2)  # d_same, d_anti, d_orth
    def K2(a, b):
        return sum((F(PHI[u][a] * PHI[u][b], Z1 * Z1) for u in range(M)), F(0))
    dvals = [(1 / K2(0, 0), P1), (1 / K2(0, 2), P4), (1 / K2(0, 1), P3)]
    dvals.sort()
    mono = True
    seen = set()
    for order in permutations(U):
        L = seq_law(U, {}, order)
        key = tuple(L[pat] / prodK(pat) for _, pat in dvals)
        if key in seen:
            continue
        seen.add(key)
        mono = mono and key[0] < key[1] < key[2]
    if mut("class_ratios_not_monotone_claimed"):
        mono = not mono
    checks.check("D2", plq_ok and mono and len(seen) == 2, "U3: isolated plaquette — every order differs from the joint law (16 at 455/31176, 8 at 37/1299) and the two class ratios to prod K are strictly increasing in the diagonal normalizer d_same < d_orth < d_anti")


# ============================================================================================ family E
def family_e(checks: Checks, report: dict) -> None:
    env_res = report["env_small"]
    multi = all(not eq and viol for name in ("domino", "path3") for (eq, viol) in env_res[name])
    env_star, _ = report["env_star"]
    multi = multi and all(d > 0 for d in env_star.values())
    if mut("environment_unit_agrees_claimed"):
        multi = any(eq for name in ("domino", "path3") for (eq, viol) in env_res[name])
    checks.check("E1", multi, "U4: in a full environment the domino and the path (every order) and the star (two all-+x orders and three mixed-environment orders) all differ from their joint law")
    single = all(eq and not viol for (eq, viol) in env_res["single"])
    if mut("single_site_differs_claimed"):
        single = not single
    checks.check("E2", single, "U4: a single site in a full environment agrees with its joint law (its only formation records outside neighbours only)")


# ============================================================================================ family F
FENCES = ('This note proves conditional identities and a sufficient agreement condition and reports finite unit witnesses; arbitrary fixed-environment necessity and universal multi-site exclusions are deferred; no unit, order, rule or coupling is selected as physical, and no clause is adopted.', 'No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The menu, weights and formation conventions are declared mathematical inputs, not empirical or axiom-selected values.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical unit", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "the unit clause is adopted", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_unit_clause_adopted": "Hence the unit clause is adopted and selects the physical unit."}
CLASSICAL_NAMES = ("Brook", "Besag", "Hammersley", "Clifford", "Toom", "Peierls", "Fourier", "Dobrushin", "Gillespie", "Eden")
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
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem U1"):
            body = body + " (the Brook ratio)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the normalizer lemma for k = 2..6 symbolically; the three-site reconstruction on 216 patterns",
    "per_site: executed — every pattern of each unit (6^7 for the star, 6^4 for the plaquette, 6^3, 6^2, 6)",
    "per_mode: executed — every order of the domino, the path and the plaquette; the star's classes k = 0, 1, 2, 3, 6; two star orders in all-+x and three in the mixed environment",
    "per_block: executed — five units, isolated and in pseudo-random or all-+x environments",
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
    print("scope: unit identities and declared finite witnesses; broad negative certification deferred; no clause adopted")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts)
    family_b(checks)
    family_c(checks, report)
    family_d(checks, report)
    family_e(checks, report)
    family_f(checks, texts[0])
    family_g(checks)
    if exact:
        env_star, vO_mixed = report["env_star"]
        print("exact star TVs in environments:", {f"{e}/k={k}": str(d) for (e, k), d in env_star.items()})
        print("mixed environment of the star (site -> value index):", sorted(vO_mixed.items()))
        print("exact isolated star TVs:", {k: str(v) for k, v in report["star"][3].items()})
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
