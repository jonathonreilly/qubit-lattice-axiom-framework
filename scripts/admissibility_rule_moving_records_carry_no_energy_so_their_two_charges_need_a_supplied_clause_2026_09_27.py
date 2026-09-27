#!/usr/bin/env python3
"""Exact checks: records that move carry no energy of their own, so block 110's two charges need a supplied clause for a
record's (e, tau); two admissible clauses give P - Q of opposite signs, records crossing at the member's factor are blind
to the fields, and under the activity clause P/Q stays above 1 at weak field whenever a record can move (a harvest of
probe #9122, confirmed by an other-family referee in #9336). Block 110's charges as landed, block 95's rates as landed.

A (premises): landed block 110's charge difference, crossing factor and derivatives; landed block 95 T1; the axioms.
B (T1): at the crossing factor sqrt(w_x w_y)/(chi_x chi_y) with block 95's heat-bath factor, pi ~ W balances every move for
   fixed fields; timed by the leaving site, W/prod w; for configuration-following even kernels the first order agrees.
C (T2): on records {0, 1, 3} of 3^3, rest only gives P - Q = -117/3280 and the activity clause +3893397/2555120; both have
   block 110 T2(e)'s homogeneity.
D (T3): at weak field P/Q = 1 + mu <B>/(m N + mu <B>/2); the uniform law has <B> = 6N(V - N)/(V - 1), so 251/101 and 121/49;
   the clocked gas at q = 3/2 (exact) stays above 1 and below the uniform ratios.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_MOVING_RECORDS_CARRY_NO_ENERGY_SO_THEIR_TWO_CHARGES_NEED_A_SUPPLIED_CLAUSE_AND_UNDER_THE_ACTIVITY_CLAUSE_THEY_NEVER_BALANCE_AT_WEAK_FIELD_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_moving_records_carry_no_energy_so_their_two_charges_need_a_supplied_clause_and_under_the_activity_clause_they_never_balance_at_weak_field_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED110 = (
    "P − Q = (1/8K) Σ [2τ − e(1 − w)/w]/χ",
    "a bond from `x` to `y` is crossed at `√(w_x w_y)/(χ_x χ_y)`",
    "These are `e_x = ∂⟨H⟩/∂u_x = r_x + τ_x` and `∂⟨H⟩/∂λ_x = −τ_x`",
    "At weak field `P/Q = 1 + 2Στ/Σe`",
)
LANDED95 = ("For a configuration-independent positive field w, pi(C) is proportional to W(C) product_{z in C}w_z^(1-2a).",)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "crossing_factor_forged": "B",
    "clause_values_forged": "C",
    "bond_count_forged": "D",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()


class Torus3:
    def __init__(self, L: int) -> None:
        self.L = L
        self.S = list(itertools.product(range(L), repeat=3))
        self.ix = {x: i for i, x in enumerate(self.S)}
        self.N = len(self.S)
        self.nb = [[self.ix[tuple((x[k] + d * (k == a)) % L for k in range(3))] for a in range(3) for d in (1, -1)] for x in self.S]
        lap = sp.zeros(self.N, self.N)
        for i in range(self.N):
            lap[i, i] = 6
            for j in self.nb[i]:
                lap[i, j] -= 1
        ginv = (lap + sp.ones(self.N, self.N) / self.N).inv() - sp.ones(self.N, self.N) / self.N
        self.G = [[Fr(int(sp.Rational(ginv[i, j]).p), int(sp.Rational(ginv[i, j]).q)) for j in range(self.N)] for i in range(self.N)]


def moves(t: Torus3, C):
    occ = set(C)
    for x in C:
        for y in t.nb[x]:
            if y not in occ:
                yield x, y, tuple(sorted((occ - {x}) | {y}))


def bond_count(t: Torus3, C) -> int:
    occ = set(C)
    return sum(1 for x in C for y in t.nb[x] if y not in occ)


T3 = None


def torus() -> Torus3:
    global T3
    if T3 is None:
        T3 = Torus3(3)
    return T3


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed110, landed95 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the records' motion, their energy clause, the member and the fields are supplied)")
    needles = list(LANDED110)
    if mut("landed_quote_forged"):
        needles[0] = "P − Q = (1/8K) Σ [2τ + e(1 − w)/w]/χ"
    checks.check("A3", all(n in landed110 for n in needles) and all(n in landed95 for n in LANDED95),
                 "landed block 110: P - Q = (1/8K) sum [2 tau - e(1 - w)/w]/chi; the crossing factor sqrt(w_x w_y)/(chi_x chi_y); e = dH/du = r + tau, dH/dlambda = -tau; P/Q = 1 + 2 sum tau/sum e at weak field; landed block 95 T1: pi ~ W prod w^(1-2a) for fixed fields")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    t = torus()
    rng = random.Random(9924)
    s_ = [Fr(rng.randint(3, 9), 5) for _ in range(t.N)]
    chi = [Fr(rng.randint(5, 11), 7) for _ in range(t.N)]
    w = [v * v for v in s_]
    omega = {}
    for d in itertools.product(range(3), repeat=3):
        md = tuple((-c) % 3 for c in d)
        if md in omega:
            omega[d] = omega[md]
        else:
            omega[d] = Fr(rng.randint(1, 9), 4)

    def W(C):
        r = Fr(1)
        for a, b in itertools.combinations(C, 2):
            xa, xb = t.S[a], t.S[b]
            r *= omega[tuple((xa[k] - xb[k]) % 3 for k in range(3))]
        return r

    def kappa(x, y):
        if mut("crossing_factor_forged"):
            return w[x] * s_[y] / (chi[x] * chi[y])
        return s_[x] * s_[y] / (chi[x] * chi[y])

    ok_cross = ok_site = True
    confs = list(itertools.combinations(range(t.N), 3))
    for C in confs[:600]:
        for x, y, Cp in moves(t, C):
            h_f = W(Cp) / (W(C) + W(Cp))
            h_b = W(C) / (W(C) + W(Cp))
            ok_cross = ok_cross and W(C) * kappa(x, y) * h_f == W(Cp) * kappa(y, x) * h_b
            pi_c = W(C) / (w[C[0]] * w[C[1]] * w[C[2]])
            pi_p = W(Cp) / (w[Cp[0]] * w[Cp[1]] * w[Cp[2]])
            ok_site = ok_site and pi_c * w[x] * h_f == pi_p * w[y] * h_b
    checks.check("B1", ok_cross and ok_site, "3 records on 3^3 with random rational clocks w = s^2, lengths chi and an even pair weight W (600 configurations, every move, exact): crossing at the member's factor sqrt(w_x w_y)/(chi_x chi_y) with block 95's heat-bath factor balances pi ~ W for fixed fields, so the fields drop out; timed by the leaving site the law is W/prod w instead")
    # B2: configuration-following fields with even kernels, first order: the forward and backward log-rates agree
    Uk = t.G[0]
    Fk = [Fr(2, 3 + sum(min(c, 3 - c) ** 2 for c in t.S[j])) for j in range(t.N)]

    def kern(Kv, a, b):
        xa, xb = t.S[a], t.S[b]
        return Kv[t.ix[tuple((xb[k] - xa[k]) % 3 for k in range(3))]]

    def fields(C, z):
        return sum((kern(Uk, z, r) for r in C), Fr(0)), sum((kern(Fk, z, r) for r in C), Fr(0))

    ok_f = True
    for C in confs[:300]:
        for x, y, Cp in moves(t, C):
            ux, px = fields(C, x)
            uy, py = fields(C, y)
            uy2, py2 = fields(Cp, y)
            ux2, px2 = fields(Cp, x)
            ok_f = ok_f and (ux + uy) / 2 - (px + py) == (uy2 + ux2) / 2 - (py2 + px2)
    checks.check("B2", ok_f, "fields that follow the records, u = sum G(z - r) (the mean-zero torus kernel) and phi = sum Phi(z - r) with an even Phi: at first order log kappa_xy(C) = log kappa_yx(C') for every move (300 configurations), so pi ~ W stays stationary and no clump binds")


# ============================================================================================ family C (T2)
def charges(t: Torus3, C, wv, cv, m, mu, K=Fr(1)):
    occ = set(C)
    tau = [Fr(0)] * t.N
    for x in range(t.N):
        for y in t.nb[x]:
            if (x in occ) != (y in occ):
                sq = wv[x] * wv[y]
                root = Fr(sp.sqrt(sp.Rational(sq.numerator, sq.denominator)).p, sp.sqrt(sp.Rational(sq.numerator, sq.denominator)).q)
                tau[x] += mu * Fr(1, 4) * root / (cv[x] * cv[y])
    e = [(m * wv[x] if x in occ else Fr(0)) + tau[x] for x in range(t.N)]
    P = sum(((e[x] + 2 * tau[x]) / (8 * K * cv[x]) for x in range(t.N)), Fr(0))
    Q = sum((e[x] / (8 * K * wv[x] * cv[x]) for x in range(t.N)), Fr(0))
    return P, Q


def family_c(checks: Checks) -> None:
    t = torus()
    C0 = (0, 1, 3)
    eps = Fr(1, 20)
    wv = [Fr(1)] * t.N
    cv = [Fr(1)] * t.N
    for z in C0:
        wv[z] = (1 - eps) ** 2
        cv[z] = 1 + eps / 2
    PR, QR = charges(t, C0, wv, cv, Fr(1), Fr(0))
    PA, QA = charges(t, C0, wv, cv, Fr(1), Fr(1))
    want_R, want_A = Fr(-117, 3280), Fr(3893397, 2555120)
    if mut("clause_values_forged"):
        want_A = -want_A
    lam_, s2, wx, wy, cx, cy = sp.symbols("lam s w_x w_y c_x c_y", positive=True)
    kap = sp.sqrt(wx * wy) / (cx * cy)
    hom = sp.simplify(kap.subs({wx: lam_ * wx, wy: lam_ * wy}) - lam_ * kap) == 0 and sp.simplify(kap.subs({cx: s2 * cx, cy: s2 * cy}) - kap / s2 ** 2) == 0
    checks.check("C1", PR - QR == want_R and PA - QA == want_A and hom, f"on records {{0, 1, 3}} of 3^3 with clocks (19/20)^2 and lengths 41/40 at the records (8K = 8): rest only H_R = sum m w gives P - Q = {PR - QR}, the activity clause H_A = H_R + mu sum (1/2) sqrt(w_x w_y)/(chi_x chi_y) over occupied-empty bonds gives P - Q = {PA - QA}; the crossing factor has degree 1 in the rates and -2 in the lengths, as block 110 T2(e) needs")


# ============================================================================================ family D (T3)
def weak_ratio(meanB, n, m=Fr(1), mu=Fr(1)):
    stau = mu * meanB / 2
    return 1 + 2 * stau / (m * n + stau)


def family_d(checks: Checks) -> None:
    t = torus()
    ok_u = True
    uni = {}
    for n in (2, 3):
        cs = list(itertools.combinations(range(t.N), n))
        mB = Fr(sum(bond_count(t, C) for C in cs), len(cs))
        want = Fr(6 * n * (t.N - n), t.N - 1)
        if mut("bond_count_forged"):
            want = Fr(6 * n * (t.N - n), t.N)
        ok_u = ok_u and mB == want
        uni[n] = weak_ratio(mB, n)
    ok_u = ok_u and uni[2] == Fr(251, 101) and uni[3] == Fr(121, 49)
    den = 1
    for i in range(t.N):
        for j in range(t.N):
            den = sp.ilcm(den, t.G[i][j].denominator)
    q = Fr(3, 2)
    gas = {}
    for n in (2, 3):
        cs = list(itertools.combinations(range(t.N), n))
        num = Fr(0)
        Z = Fr(0)
        for C in cs:
            ex = sum(int(t.G[a][b] * den) for a, b in itertools.combinations(C, 2))
            wt = q ** ex
            Z += wt
            num += wt * bond_count(t, C)
        gas[n] = (num / Z, weak_ratio(num / Z, n))
    ok_g = den == 486 and all(1 < gas[n][1] < uni[n] for n in (2, 3)) and all(gas[n][0] < Fr(6 * n * (t.N - n), t.N - 1) for n in (2, 3))
    checks.check("D1", ok_u and ok_g, f"weak field, activity clause (m = mu = 1): P/Q = 1 + mu <B>/(m N + mu <B>/2) with B the occupied-empty bonds; the uniform law on 3^3 has <B> = 6N(V - N)/(V - 1), so P/Q = {uni[2]} and {uni[3]} for N = 2, 3; the clocked gas's law q^(486 sum G), q = 3/2 (G's common denominator 486), gives P/Q = {gas[2][1]} and {gas[3][1]}, above 1 and below the uniform values")
    ok_r = weak_ratio(Fr(0), 2) == 1 and weak_ratio(Fr(6), 2, Fr(1), Fr(0)) == 1
    checks.check("D2", ok_r, "P/Q = 1 at weak field exactly when the hop energy vanishes with the field (sum tau/sum e -> 0): the rest-only clause, or a jammed gas with <B> = 0")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 110 and 95 as landed on main (the curvature member's two charges, and the rates at which records move) and asks what a record that moves contributes to the charges; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at P = Q."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Kolmogorov", "Metropolis",
                   "Glauber", "Komar", "Tolman", "Buchdahl", "Arnowitt", "Misner")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Kolmogorov) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the crossing factor's symmetry and homogeneity",
    "per_site: executed - the charges e, tau at every site of 3^3 under both clauses",
    "per_mode: executed - detailed balance for 600 configurations with every move, fixed fields and first-order following fields",
    "per_block: executed - the weak-field ratio under the uniform law and the clocked gas's law, exactly",
    "lattice_wide: checked and not executed - the self-consistent member at finite field; following fields beyond first order; which clause is the record's energy",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: blocks 110 and 95 as landed: records carry no energy, so the charges need a supplied clause; rest only and the activity clause give P - Q of opposite signs; crossing at the member's factor is blind to the fields; under the activity clause P/Q > 1 at weak field whenever a record can move; harvest of #9122 (confirmed by #9336); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
