#!/usr/bin/env python3
"""Exact checks: the strong-coupling side of the three-dimensional monotone formation law.

Scope.  The six Bloch-axis menu with the covariant positive product rule (p, q, r), the records-only reading, the monotone
class on Z^3 in level time.  S0: the predecessors of a site project to the north-east-center offsets.  S1: the closed
forms of the kernel at the unanimous, 2:1-orthogonal, 2:1-antipodal and tie patterns, verified symbolically; the values at
(p,1,2) for five couplings; the majority-preference condition p > max(q, r) and p**2*q > r**3.  S2: the noiseless majority rule on levels is
an eroder: random islands, a line and a triangle die within M_1 + M_2 + M_3 - t_0 + 1 levels.  S3: epsilon(p) as the exact
maximum over all 216 triples with at least two entries +x.  S4: the 2x2 orbit quotient's contraction after n steps rises
with p; the constant plane is nearly absorbing at p = 10^6.  S5: the row eigenvalue (p - q)/Z_1 < 1.  Exact rational and
symbolic arithmetic only; the runner scans its own source for floating-point literals.  No ordered phase is claimed.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from math import lcm
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_STRONG_COUPLING_FORMATION_LAW_LEVEL_AUTOMATON_ERODER_METASTABILITY_ORDERED_PHASE_OBLIGATION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_MONOTONE_FORMATION_LAW_PLANE_CHAIN_COUPLING_REGION_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_MARKOV_GRAPH_EIGHT_CORNER_LAWS_SWEEP_IMPRINT_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/ADMISSIBILITY_RULE_MONOTONE_ORDER_FORMATION_LAW_ROWS_COLUMNS_CHAINS_CORNER_LAW_BOUNDED_THEOREM_NOTE_2026-09-07.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_strong_coupling_formation_law_level_automaton_eroder_metastability_ordered_phase_obligation_bounded_theorem_note_2026-09-15"
BLOCK08_CLAIM_ID = "admissibility_rule_three_dimensional_monotone_formation_law_plane_chain_coupling_region_bounded_theorem_note_2026-09-15"
BLOCK08_FRAGMENT = "strong coupling"
BLOCK09_CLAIM_ID = "admissibility_rule_three_dimensional_formation_law_markov_graph_eight_corner_laws_sweep_imprint_bounded_theorem_note_2026-09-15"
BLOCK05_CLAIM_ID = "admissibility_rule_monotone_order_formation_law_rows_columns_chains_corner_law_bounded_theorem_note_2026-09-07"
BLOCK05_FRAGMENT = "every row and every column"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "projection_offsets_wrong": "B",
    "closed_form_forged": "B",
    "noise_values_off": "B",
    "majority_preference_wrong": "B",
    "epsilon_max_wrong": "B",
    "eroder_bound_violated_claimed": "C",
    "island_survives_claimed": "C",
    "memory_table_forged": "D",
    "contraction_table_forged": "D",
    "absorbing_limit_denied": "D",
    "two_d_eigenvalue_ge_one_claimed": "D",
    "claim_ordered_phase_proved": "F",
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


def dec(x: Fraction, n: int = 8) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


def orbit_type(s: int, u: int) -> str:
    if s == u:
        return "p"
    if s // 2 == u // 2:
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
        self.Z2 = {(a, b): sum(self.phi[s][a] * self.phi[s][b] for s in range(M)) for a in range(M) for b in range(M)}
        self.Z3 = {(a, b, c): sum(self.phi[s][a] * self.phi[s][b] * self.phi[s][c] for s in range(M)) for a in range(M) for b in range(M) for c in range(M)}
        self.K2 = {k: F(v, self.Z1 ** 2) for k, v in self.Z2.items()}
        self.K3 = {k: F(v, self.Z1 ** 3) for k, v in self.Z3.items()}
        self._cond: dict = {}

    def cond(self, rec: tuple) -> list:
        if rec in self._cond:
            return self._cond[rec]
        k = len(rec)
        if k == 0:
            out = [F(1, M)] * M
        elif k == 1:
            out = [self.K[rec[0]][s] for s in range(M)]
        elif k == 2:
            out = [F(self.phi[s][rec[0]] * self.phi[s][rec[1]], self.Z2[rec]) for s in range(M)]
        else:
            out = [F(self.phi[s][rec[0]] * self.phi[s][rec[1]] * self.phi[s][rec[2]], self.Z3[rec]) for s in range(M)]
        self._cond[rec] = out
        return out


# ------------------------------------------------------------------ the 2x2 plane transfer and orbits (block 08's machinery)
def plane_transfer(rule: Rule, w, v) -> Fraction:
    w00, w01, w10, w11 = w
    v00, v01, v10, v11 = v
    K, K2, K3 = rule.K, rule.K2, rule.K3
    return (K[w00][v00] * K[w01][v01] * K[v00][v01] / K2[(w01, v00)] * K[w10][v10] * K[v00][v10] / K2[(w10, v00)]
            * K[w11][v11] * K[v01][v11] * K[v10][v11] / K3[(w11, v01, v10)])


def group48():
    axes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    idx = {a: i for i, a in enumerate(axes)}
    elems = set()
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            mp = []
            for a in axes:
                b = [0, 0, 0]
                for i in range(3):
                    b[perm[i]] = signs[i] * a[i]
                mp.append(idx[tuple(b)])
            elems.add(tuple(mp))
    return sorted(elems)


def orbits_2x2():
    states = list(product(range(M), repeat=4))
    G = group48()
    orbit_of, reps = {}, []
    for s in states:
        if s in orbit_of:
            continue
        o = len(reps)
        reps.append(s)
        orbit_of[s] = o
        stack = [s]
        while stack:
            u = stack.pop()
            for g in G:
                gu = tuple(g[x] for x in u)
                for cand in (gu, (gu[0], gu[2], gu[1], gu[3])):
                    if cand not in orbit_of:
                        orbit_of[cand] = o
                        stack.append(cand)
    return states, orbit_of, reps


def contraction_table(rule: Rule, steps=(1, 2, 4, 8)):
    states, orbit_of, reps = orbits_2x2()
    n = len(reps)
    Q = [[F(0)] * n for _ in range(n)]
    for o, w in enumerate(reps):
        for v in states:
            Q[o][orbit_of[v]] += plane_transfer(rule, w, v)
    Qn = [row[:] for row in Q]
    out = {}
    for k in range(1, max(steps) + 1):
        if k in steps:
            out[k] = max(sum(abs(Qn[o1][o] - Qn[o2][o]) for o in range(n)) / 2 for o1 in range(n) for o2 in range(n))
        Qn = [[sum(Qn[i][kk] * Q[kk][j] for kk in range(n)) for j in range(n)] for i in range(n)]
    return out


# ------------------------------------------------------------------ the eroder
def evolve_majority(island: set) -> int:
    cur = set(island)
    t = 0
    while cur:
        cand = set()
        for (a, b, c) in cur:
            cand |= {(a + 1, b, c), (a, b + 1, c), (a, b, c + 1)}
        nxt = set()
        for (a, b, c) in cand:
            n1 = ((a - 1, b, c) in cur) + ((a, b - 1, c) in cur) + ((a, b, c - 1) in cur)
            if n1 >= 2:
                nxt.add((a, b, c))
        cur = nxt
        t += 1
        if t > 10 ** 5:
            return -1
    return t


def island_bound(island: set, t0: int) -> int:
    return max(s[0] for s in island) + max(s[1] for s in island) + max(s[2] for s in island) - t0 + 1


# ============================================================================================ family A
def family_a(checks: Checks, note_text: str, axiom_text: str, b08: str, b09: str, b05: str) -> None:
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 5,
                 "the five declared inputs exist (this note, axiom memo, plane-chain and DLR notes, actual rectangle premise)")
    checks.check("A2", all(n in normalize_text(axiom_text) for n in AXIOM_NEEDLES), "the four axiom sentences used are present verbatim in the axiom memo")
    f08, f09 = normalize_text(b08).lower(), normalize_text(b09).lower()
    checks.check("A3", BLOCK08_CLAIM_ID in f08 and BLOCK08_FRAGMENT in f08 and BLOCK09_CLAIM_ID in f09 and BLOCK05_CLAIM_ID in b05 and BLOCK05_FRAGMENT in normalize_text(b05).lower(),
                 "actual parent claim ids, strong-coupling context and rectangle row/column proof identity are present")
    flat = normalize_text(note_text)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
x, mx, y, my, z, mz = 0, 1, 2, 3, 4, 5
EPS_312 = {3: F(35, 44), 10: F(21, 71), 30: F(71, 971), 100: F(211, 10211), 1000: F(2011, 1002011)}


def family_b(checks: Checks, report: dict) -> None:
    # B1: the projection of the predecessors
    ok = True
    random.seed(20260915)
    for _ in range(50):
        pt = tuple(random.randint(-20, 20) for _ in range(3))
        preds = [tuple(pt[i] - (1 if j == i else 0) for i in range(3)) for j in range(3)]
        proj = [(p_[1], p_[2]) for p_ in preds]
        exp = [(pt[1], pt[2]), (pt[1] - 1, pt[2]), (pt[1], pt[2] - 1)]
        if mut("projection_offsets_wrong"):
            exp = [(pt[1], pt[2]), (pt[1] + 1, pt[2]), (pt[1], pt[2] - 1)]
        ok = ok and proj == exp and all(sum(p_) == sum(pt) - 1 for p_ in preds)
    checks.check("B1", ok, "S0: the three predecessors lie on the previous level and project to the offsets (0,0), (-1,0), (0,-1)")
    # B2: closed forms, symbolically
    P, Q, R = sp.symbols("p q r", positive=True)
    w = {"p": P, "q": Q, "r": R}

    def cond_sym(rec, s):
        num = sp.prod([w[orbit_type(s, a)] for a in rec])
        den = sum(sp.prod([w[orbit_type(u, a)] for a in rec]) for u in range(M))
        return sp.cancel(num / den)
    forms = [
        (cond_sym((x, x, x), x), P**3 / (P**3 + Q**3 + 4 * R**3)),
        (cond_sym((x, x, y), x), P**2 * R / (R * (P**2 + Q**2) + R**2 * (P + Q) + 2 * R**3)),
        (cond_sym((x, x, mx), x), P**2 * Q / (P * Q * (P + Q) + 4 * R**3)),
        (cond_sym((x, y, z), x), P / (3 * (P + Q))),
        (cond_sym((x, y, z), mx), Q / (3 * (P + Q))),
    ]
    closed_ok = all(sp.simplify(a - b) == 0 for a, b in forms)
    if mut("closed_form_forged"):
        closed_ok = False
    checks.check("B2", closed_ok, "S1: the five closed forms (unanimous, 2:1 orthogonal, 2:1 antipodal, tie majority, tie antipode) agree with the definition symbolically")
    # B3: values at (p,1,2)
    vals = {}
    for p in (3, 10, 30, 100, 1000):
        rule = Rule((p, 1, 2))
        vals[p] = (rule.cond((x, x, x))[x], rule.cond((x, x, y))[x], rule.cond((x, x, mx))[x], rule.cond((x, y, z))[x])
    v10 = vals[10]
    lit_ok = v10 == (F(1000, 1033), F(200, 262), F(100, 142), F(10, 33))
    if mut("noise_values_off"):
        lit_ok = False
    checks.check("B3", lit_ok, "S1: at (10,1,2) the four probabilities are 1000/1033, 100/131, 50/71, 10/33; " + "; ".join(f"p={p}: dev(aaa)={dec(1-vals[p][0])}, dev(aab)={dec(1-vals[p][1])}, dev(aa-a)={dec(1-vals[p][2])}" for p in (3, 100, 1000)))
    # B4: strict majority for both patterns needs both exact inequalities.
    def majority_most_likely(tr):
        rule = Rule(tr)
        c1 = rule.cond((x, x, y))
        c2 = rule.cond((x, x, mx))
        return c1[x] > max(c1[s] for s in range(M) if s != x) and c2[x] > max(c2[s] for s in range(M) if s != x)
    preference_triples = ((3, 1, 2), (2, 1, 3), (1, 2, 1), (2, 2, 1),
                          (3, F(1, 100), 2), (2, 2, 2), (4, F(1, 2), 2))
    pref = all(majority_most_likely((p, q, r)) ==
               (p > max(q, r) and p*p*q > r*r*r)
               for p, q, r in preference_triples)
    if mut("majority_preference_wrong"):
        pref = majority_most_likely((3, F(1, 100), 2))
    checks.check("B4", pref, "S1: strict majority across both 2:1 patterns iff p > max(q,r) and p^2*q > r^3; exact samples include the small-q counterexample and equality boundaries")
    # B5: epsilon(p) as the exact maximum over the 216 triples with >= 2 entries +x
    eps = {}
    arg = {}
    for p in (3, 10, 30, 100, 1000):
        rule = Rule((p, 1, 2))
        best, best_t = F(0), None
        for tr in product(range(M), repeat=3):
            if sum(1 for a in tr if a == x) >= 2:
                d = 1 - rule.cond(tr)[x]
                if d > best:
                    best, best_t = d, tr
        eps[p] = best
        arg[p] = best_t
    eps_ok = all(eps[p] == EPS_312[p] for p in eps)
    if mut("epsilon_max_wrong"):
        eps_ok = False
    checks.check("B5", eps_ok, "S3: epsilon(p) over all 216 triples at (p,1,2): " + "; ".join(f"p={p}: {eps[p]} = {dec(eps[p])} at {tuple(('+x','-x','+y','-y','+z','-z')[a] for a in arg[p])}" for p in (3, 10, 100)))
    report["eps"] = eps


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    random.seed(20260915)
    ok = True
    worst = 0
    for _ in range(300):
        t0 = random.randint(3, 12)
        pts = [(a, b, t0 - a - b) for a in range(t0 + 1) for b in range(t0 + 1 - a)]
        k = random.randint(1, min(12, len(pts)))
        isl = set(random.sample(pts, k))
        T = evolve_majority(isl)
        bound = island_bound(isl, t0)
        if mut("eroder_bound_violated_claimed"):
            bound = bound - 1
        ok = ok and 0 <= T <= bound
        worst = max(worst, T)
    checks.check("C1", ok, f"S2: 300 random islands (levels 3..12, up to 12 sites) all die within M_1+M_2+M_3-t_0+1 levels (longest life {worst})")
    line = {(0, b, 10 - b) for b in range(6)}
    tri = {(a, b, 12 - a - b) for a in range(5) for b in range(5 - a)}
    tl, tt = evolve_majority(line), evolve_majority(tri)
    exact = (tl == island_bound(line, 10) == 6) and (tt == island_bound(tri, 12) == 9)
    if mut("island_survives_claimed"):
        exact = tl < 0
    checks.check("C2", exact, f"S2: a line of six dies in exactly {tl} levels and a filled triangle of fifteen in exactly {tt}, both equal to the bound")


# ============================================================================================ family D
# integer decimals: floor(10^6 x); the memory table is the full 1296-state chain (TV between the rows of the all-+x and the
# all--x planes after n steps); the contraction table is the 48-fold orbit quotient, which identifies the six constant planes
MEMORY = {3: {1: 428390, 2: 82771, 4: 2940, 8: 3}, 10: {1: 798539, 2: 509619, 4: 154437, 8: 10129},
          30: {1: 929565, 2: 795932, 4: 505143, 8: 165879}, 100: {1: 976919, 2: 927316, 4: 795151, 8: 549286}}
CONTRACTION = {3: {1: 72029, 2: 2008, 4: 1, 8: 0}, 10: {1: 393104, 2: 113234, 4: 7298, 8: 21},
               30: {1: 653361, 2: 320619, 4: 66726, 8: 1813}, 100: {1: 734878, 2: 413945, 4: 110339, 8: 5940}}


def micro(x: Fraction) -> int:
    return x.numerator * 10 ** 6 // x.denominator


def full_chain_memory(rule: Rule, steps=(1, 2, 4, 8)):
    """TV between the n-step laws started from the all-+x and the all--x planes on the full 2x2 chain, exactly, by integer
    numerators over a common denominator D (each row of the transfer sums to D)."""
    phi, Z1, Z2, Z3 = rule.phi, rule.Z1, rule.Z2, rule.Z3
    L2 = 1
    for v in set(Z2.values()):
        L2 = lcm(L2, v)
    L3 = 1
    for v in set(Z3.values()):
        L3 = lcm(L3, v)
    D = Z1 * L2 * L2 * L3
    states = list(product(range(M), repeat=4))
    Pint = []
    for (w00, w01, w10, w11) in states:
        row = []
        for (v00, v01, v10, v11) in states:
            num = phi[v00][w00] * phi[v01][w01] * phi[v01][v00] * phi[v10][w10] * phi[v10][v00] * phi[v11][w11] * phi[v11][v01] * phi[v11][v10]
            den = Z1 * Z2[(w01, v00)] * Z2[(w10, v00)] * Z3[(w11, v01, v10)]
            row.append(num * (D // den))
        assert sum(row) == D
        Pint.append(row)
    idx = {s: i for i, s in enumerate(states)}
    d = [u - v for u, v in zip(Pint[idx[(x, x, x, x)]], Pint[idx[(mx, mx, mx, mx)]])]
    cols = list(zip(*Pint))
    out, scale, n = {}, D, 1
    if 1 in steps:
        out[1] = F(sum(abs(t) for t in d), 2 * scale)
    while n < max(steps):
        d = [sum(di * pij for di, pij in zip(d, col)) for col in cols]
        scale *= D
        n += 1
        if n in steps:
            out[n] = F(sum(abs(t) for t in d), 2 * scale)
    return out


def family_d(checks: Checks, report: dict, exact: bool) -> None:
    mem = {p: full_chain_memory(Rule((p, 1, 2))) for p in (3, 10, 30, 100)}
    mem_ok = all(micro(mem[p][k]) == MEMORY[p][k] for p in mem for k in (1, 2, 4, 8))
    mem_mono = all(mem[3][k] < mem[10][k] < mem[30][k] < mem[100][k] for k in (1, 2, 4, 8)) and all(mem[p][k] < 1 for p in mem for k in (1, 2, 4, 8))
    if mut("memory_table_forged"):
        mem_ok = False
    checks.check("D1", mem_ok and mem_mono, "S4: full 2x2 chain, TV between the n-step laws from the all-+x and the all--x planes at (p,1,2) matches the memory table, is below one, and increases with p for n = 1, 2, 4, 8: "
                 + "; ".join(f"p={p}: " + ",".join(dec(mem[p][k], 6) for k in (1, 2, 4, 8)) for p in (3, 100)))
    table = {p: contraction_table(Rule((p, 1, 2))) for p in (3, 10, 30, 100)}
    tab_ok = all(micro(table[p][k]) == CONTRACTION[p][k] for p in table for k in (1, 2, 4, 8))
    mono = all(table[3][k] < table[10][k] < table[30][k] < table[100][k] for k in (1, 2, 4, 8))
    quotient_below = all(table[p][k] < mem[p][k] for p in table for k in (1, 2, 4, 8))
    if mut("contraction_table_forged"):
        tab_ok = False
    checks.check("D1b", tab_ok and mono and quotient_below, "S4: the 48-fold orbit quotient (the six constant planes identified) contracts at every coupling; its n-step max row TV matches the table, increases with p, and lies below the full chain's memory at every (p, n)")
    rule = Rule((10 ** 6, 1, 2))
    const = (x, x, x, x)
    stay = plane_transfer(rule, const, const)
    absorbing = stay >= 1 - F(1, 10 ** 5)
    if mut("absorbing_limit_denied"):
        absorbing = stay <= F(1, 2)
    checks.check("D2", absorbing, f"S4: at p = 10^6 the constant plane maps to itself with probability {dec(stay, 8)} (>= 1 - 10^-5): absorbing in the limit")
    P, Q, R = sp.symbols("p q r", positive=True)
    Z1 = P + Q + 4 * R
    ev_ok = all(F(p - 1, p + 9) < 1 for p in (3, 10, 30, 100, 1000)) and sp.simplify(Z1 - (P - Q) - (2 * Q + 4 * R)) == 0 and sp.simplify(Z1 - (P + Q - 2 * R) - 6 * R) == 0
    if mut("two_d_eigenvalue_ge_one_claimed"):
        ev_ok = False
    checks.check("D3", ev_ok, "S5: the row eigenvalues (p-q)/Z_1 and (p+q-2r)/Z_1 are below one at every positive triple (Z_1 - (p-q) = 2q+4r > 0, Z_1 - (p+q-2r) = 6r > 0); at (1000,1,2) the first is " + dec(F(999, 1009)))
    if exact:
        for p in table:
            print(f"exact quotient contraction at p={p}: " + ", ".join(f"n={k}: {table[p][k]}" for k in (1, 2)))
            print(f"exact full-chain memory at p={p}: " + ", ".join(f"n={k}: {mem[p][k]}" for k in (1,)))


# ============================================================================================ family F
FENCES = (
    "This note structures the strong-coupling side of the three-dimensional monotone formation law and reduces its ordered phase to one exact obligation; it does not prove an ordered phase, does not select an order, corner or coupling as physical, states nothing about the static law's ordered phase, and gives no numeric threshold.",
    "No plane, bridge, Born or gravity statement enters this note; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "the probability and spectral results listed under Imports are mathematical inputs, not physical premises.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "phase transition is proved", "ordered phase exists", "we prove the ordered phase",
    "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_ordered_phase_proved": "Hence the ordered phase exists for large p."}
CLASSICAL_NAMES = ("Toom", "Peierls", "Perron", "Dobrushin", "Kolmogorov", "Gács", "Gray", "Bramson")
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
    for sec in sections:
        title = sec.splitlines()[0].strip() if sec.startswith(("Theorem", "S", "Result", "Machine", "Premises", "Prior", "Exact", "No-Go", "Falsifiers", "Boundaries", "Imports", "Review", "Verification")) else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem S2"):
            body = body + " (Toom's eroder)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the five closed forms against the definition; the 216 triples for epsilon(p) at five couplings; the preference condition at four triples",
    "per_site: executed — the projected predecessors of 50 random sites; the constant plane's self-transition at p = 10^6",
    "per_mode: executed — the 2x2 orbit quotient's contraction after 1, 2, 4, 8 steps at four couplings; the row eigenvalues",
    "per_block: executed — 300 random islands, a line and a filled triangle under the eroder bound",
    "lattice_wide: S0, S2, S3, S5 proved for every positive triple; S4 proved for every finite cross-section; the three-dimensional ordered phase is an obligation (S6), not claimed",
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
    print("scope: the strong-coupling side of the 3D monotone law — the level automaton, the exact noise map, the eroder bound, epsilon(p), the 2x2 metastability table, the 2D eigenvalue; exact; no ordered phase claimed")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts[0], texts[1], texts[2], texts[3], texts[4])
    family_b(checks, report)
    family_c(checks)
    family_d(checks, report, exact)
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
