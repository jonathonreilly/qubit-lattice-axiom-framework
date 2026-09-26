#!/usr/bin/env python3
"""Exact checks: when the clock field relaxes towards the records at a finite rate, block 95's pair law survives at first order
with log kappa -> gamma log kappa, gamma = 2 Gamma/(2 Gamma + 1), the separation of two records still jumps as a simple random
walk, and no stationary law is of product form (a harvest of probe #9158, confirmed by an other-family referee in #9325).
Block 95's law as landed (rates exp[a u_x + (1 - a) u_y] h/q, W = 1, h = 1/2), with the supplied relaxation clause
du_z/dt = Gamma w_z ((M u)_z + lambda (n_z - nbar)), M = Adj/q - I, on finite tori.

A (premises): landed block 95's slaved law, its clock-only rate and its exclusion of delayed clocks; the axioms.
B (T1): the invariant sum_z 1/w_z; the slaved equilibrium M u* = -lambda (n - nbar); the energy E_C decreases along the flow.
C (T2): the separation's jump chain: D -> D - e (e != D) and D -> D + e (e != -D) each reach every nonzero neighbour of D once.
D (T3): the first-order moment system is solved by m(C) = pi0 gamma phi*(C), gamma = Gamma/(Gamma + r0 q) = 2 Gamma/(2 Gamma + 1),
   uniquely; both wrong gammas fail; the O(lambda) record law is block 95's at coupling gamma lambda; ring-6 pair weights.
E (T4): on the line u = u_rho + c 1 the drift is Gamma lambda e^c w_rho (n_C - rho); a common multiple forces n_C = rho.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_CLOCK_THAT_FOLLOWS_THE_RECORDS_LATE_KEEPS_THEIR_PAIR_LAW_AT_FIRST_ORDER_WITH_THE_COUPLING_SCALED_BY_TWO_GAMMA_OVER_TWO_GAMMA_PLUS_ONE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_with_the_coupling_scaled_by_two_gamma_over_two_gamma_plus_one_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    "pi(C) is proportional to W(C) exp[6lambda(1-2a) sum_{unordered pairs}G(r-s)]",
    "At a=1 every allowed hop of a record at x has rate w_x/12",
    "Formation and delayed clocks are absent.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "invariant_forged": "B",
    "separation_forged": "C",
    "gamma_forged": "D",
    "line_drift_forged": "E",
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


class Torus:
    """(Z/L)^d with its sites, unit steps, M = Adj/q - I and the mean-zero G: Delta G = delta_0 - 1/V"""

    def __init__(self, L: int, d: int) -> None:
        self.L, self.d = L, d
        self.sites = list(itertools.product(range(L), repeat=d))
        self.index = {s: i for i, s in enumerate(self.sites)}
        self.V = len(self.sites)
        self.q = 2 * d
        self.steps = []
        for k in range(d):
            for sg in (1, -1):
                e = [0] * d
                e[k] = sg
                self.steps.append(tuple(e))
        adj = sp.zeros(self.V, self.V)
        for s in self.sites:
            for e in self.steps:
                adj[self.index[s], self.index[self.add(s, e)]] += 1
        self.adj = adj
        self.M = adj / self.q - sp.eye(self.V)
        lap = self.q * sp.eye(self.V) - adj
        rhs = sp.Matrix([(1 if i == 0 else 0) - sp.Rational(1, self.V) for i in range(self.V)])
        g = (lap + sp.ones(self.V, self.V) / self.V).LUsolve(rhs)
        self.G = {s: g[self.index[s]] for s in self.sites}

    def add(self, s, e):
        return tuple((a + b) % self.L for a, b in zip(s, e))

    def sub(self, s, e):
        return tuple((a - b) % self.L for a, b in zip(s, e))

    def Gd(self, x, r):
        return self.G[self.sub(x, r)]


def configs(T: Torus, N: int):
    return [frozenset(c) for c in itertools.combinations(T.sites, N)]


def moves(T: Torus, C):
    """(x, y, C') for every record at x and empty neighbour y"""
    out = []
    for x in sorted(C):
        for e in T.steps:
            y = T.add(x, e)
            if y not in C:
                out.append((x, y, (C - {x}) | {y}))
    return out


def phistar(T: Torus, C):
    return sp.Matrix([T.q * sum(T.Gd(z, r) for r in C) for z in T.sites])


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the records' rates, the field and its relaxation are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[0] = "pi(C) is proportional to W(C) exp[6lambda(1+2a) sum_{unordered pairs}G(r-s)]"
    checks.check("A3", all(n in landed for n in needles), "landed block 95: the slaved law pi ~ W exp[6 lambda (1 - 2a) sum_pairs G]; at a = 1 every allowed hop has rate w_x/12; delayed clocks are absent there")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    T = Torus(5, 1)
    us = sp.symbols("u0:5", real=True)
    lam, Gam = sp.symbols("lambda Gamma", real=True)
    C = frozenset({(0,), (2,)})
    n = sp.Matrix([1 if s in C else 0 for s in T.sites])
    nbar = sp.Rational(len(C), T.V)
    u = sp.Matrix(us)
    Mu = T.M * u
    udot = [Gam * sp.exp(us[z]) * (Mu[z] + lam * (n[z] - nbar)) for z in range(T.V)]
    sgn = 1 if not mut("invariant_forged") else -1
    dS = sp.simplify(sum(-sp.exp(-sgn * us[z]) * udot[z] for z in range(T.V)))
    checks.check("B1", dS == 0, "the invariant: along the flow d/dt sum_z e^(-u_z) = -Gamma [sum_z (M u)_z + lambda sum_z (n_z - nbar)] = 0 (ring 5, symbolic u), and jumps do not move u")
    ok2 = True
    for (L, d, N) in ((6, 1, 2), (3, 2, 2), (4, 2, 3)):
        Tt = Torus(L, d)
        for Cc in configs(Tt, N)[:6]:
            nn = sp.Matrix([1 if s in Cc else 0 for s in Tt.sites])
            ok2 = ok2 and sp.simplify(Tt.M * phistar(Tt, Cc) + (nn - sp.Rational(N, Tt.V) * sp.ones(Tt.V, 1))) == sp.zeros(Tt.V, 1)
    checks.check("B2", ok2, "the slaved field: M phi*(C) = -(n_C - nbar) for phi*(C) = q sum_(r in C) G(. - r) (ring 6, 3x3, 4x4), so u*(C) = lambda phi*(C) + const is the fixed-configuration equilibrium")
    ustar = sp.Matrix(sp.symbols("s0:5", real=True))
    dvec = u - ustar
    E = (dvec.T * (-T.M) * dvec)[0] / 2
    flow = [Gam * sp.exp(us[z]) * (T.M * dvec)[z] for z in range(T.V)]
    dE = sum(sp.diff(E, us[z]) * flow[z] for z in range(T.V))
    target = -Gam * sum(sp.exp(us[z]) * (T.M * dvec)[z] ** 2 for z in range(T.V))
    checks.check("B3", sp.simplify(dE - target) == 0, "for fixed C the flow is Gamma w (x) M(u - u*), and E_C = (1/2)<u - u*, -M(u - u*)> has dE_C/dt = -Gamma sum_z w_z ((M(u - u*))_z)^2 <= 0 (ring 5, symbolic)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    ok = True
    cases = ((3, 1), (4, 1), (5, 1), (6, 1), (3, 2), (4, 2), (3, 3))
    for L, d in cases:
        T = Torus(L, d)
        zero = tuple([0] * d)
        for D in T.sites:
            if D == zero:
                continue
            nbrs = [T.add(D, e) for e in T.steps]
            target = sorted(x for x in nbrs if x != zero)
            first = sorted(T.sub(D, e) for e in T.steps if T.add(zero, e) != D)
            second = sorted(T.add(D, e) for e in T.steps if T.add(zero, e) != T.sub(zero, D))
            if mut("separation_forged"):
                second = sorted(T.add(D, e) for e in T.steps)
            ok = ok and first == target and second == target
    checks.check("C1", ok, "two records (a = 1, W = 1): a hop of record 1 by e != D sends D to D - e, a hop of record 2 by e != -D sends D to D + e, and each map reaches every nonzero neighbour of D exactly once (rings 3-6, 3x3, 4x4, 3^3), so the separation's jump chain is the simple random walk on the torus minus the origin at every Gamma and lambda")


# ============================================================================================ family D (T3)
def moment_residual(T: Torus, N: int, Gam, gam):
    cs = configs(T, N)
    pi0 = sp.Rational(1, len(cs))
    r0 = sp.Rational(1, 2 * T.q)
    nbar = sp.Rational(N, T.V)
    m = {C: pi0 * gam * phistar(T, C) for C in cs}
    worst = sp.Integer(0)
    for C0 in cs:
        n = sp.Matrix([1 if s in C0 else 0 for s in T.sites])
        lhs = Gam * (T.M * m[C0] + pi0 * (n - nbar * sp.ones(T.V, 1)))
        for (_, _, C1) in moves(T, C0):
            lhs += r0 * (m[C1] - m[C0])
        if any(v != 0 for v in lhs):
            worst = sp.Integer(1)
    return worst


def family_d(checks: Checks) -> None:
    ok1 = True
    ctrl = 0
    ctrl_fail = 0
    for (L, d, N) in ((5, 1, 1), (5, 1, 2), (6, 1, 2), (3, 2, 2)):
        T = Torus(L, d)
        for Gam in (sp.Rational(1, 3), sp.Integer(1), sp.Rational(5, 2)):
            r0q = sp.Rational(1, 2)
            gam = Gam / (Gam + r0q)
            if mut("gamma_forged"):
                gam = Gam / (Gam + 1)
            ok1 = ok1 and moment_residual(T, N, Gam, gam) == 0
            for bad in (sp.Integer(1), Gam / (Gam + 1)):
                ctrl += 1
                ctrl_fail += moment_residual(T, N, Gam, bad) != 0
    checks.check("D1", ok1 and ctrl_fail == ctrl, f"the first-order moment system Gamma[M m(C0) + pi0(n_C0 - nbar)] + r0 sum_(C ~ C0)(m(C) - m(C0)) = 0 is solved exactly by m(C) = pi0 gamma phi*(C), gamma = Gamma/(Gamma + r0 q) = 2 Gamma/(2 Gamma + 1) (rings 5, 6 and 3x3, N = 1, 2, Gamma = 1/3, 1, 5/2); both controls gamma = 1 and Gamma/(Gamma + 1) fail in all {ctrl} cases")
    # D2: uniqueness, the kernel of Gamma M (x) I + I (x) Q0 is the constants
    ok2 = True
    for (L, d, N) in ((5, 1, 2), (6, 1, 2)):
        T = Torus(L, d)
        cs = configs(T, N)
        idx = {C: i for i, C in enumerate(cs)}
        r0 = sp.Rational(1, 2 * T.q)
        dim = len(cs) * T.V
        Op = sp.zeros(dim, dim)
        for C0 in cs:
            i0 = idx[C0]
            for z in range(T.V):
                row = i0 * T.V + z
                for zz in range(T.V):
                    Op[row, i0 * T.V + zz] += T.M[z, zz]
                for (_, _, C1) in moves(T, C0):
                    Op[row, idx[C1] * T.V + z] += r0
                    Op[row, i0 * T.V + z] -= r0
        ok2 = ok2 and DomainMatrix.from_Matrix(Op).convert_to(QQ).rank() == dim - 1 and Op * sp.ones(dim, 1) == sp.zeros(dim, 1)
    checks.check("D2", ok2, "uniqueness: the operator M (x) I + I (x) Q0 (Gamma = 1) has rank dim - 1 with the constants as its kernel (ring 5, N = 2: 49/50; ring 6, N = 2: 89/90), and the zero sum of phi fixes the solution")
    Gs = sp.Symbol("Gamma", positive=True)
    g_expr = 2 * Gs / (2 * Gs + 1)
    ser = sp.series(g_expr.subs(Gs, 1 / sp.Symbol("e", positive=True)), sp.Symbol("e", positive=True), 0, 3).removeO()
    ok3 = sp.simplify(Gs / (Gs + sp.Rational(1, 2)) - g_expr) == 0 and sp.expand(ser - (1 - sp.Symbol("e", positive=True) / 2 + sp.Symbol("e", positive=True) ** 2 / 4)) == 0
    # D4: the O(lambda) record law is block 95's at coupling gamma lambda, for a in {1, 1/2, 0}
    T = Torus(6, 1)
    cs = configs(T, 2)
    pi0 = sp.Rational(1, len(cs))
    r0 = sp.Rational(1, 2 * T.q)
    Gam = sp.Rational(3, 2)
    gam = Gam / (Gam + sp.Rational(1, 2))
    m = {C: pi0 * gam * phistar(T, C) for C in cs}
    P = {C: sum(T.Gd(x, y) for x, y in itertools.combinations(sorted(C), 2)) for C in cs}
    Pbar = sum(P.values()) / len(cs)
    for a in (sp.Integer(1), sp.Rational(1, 2), sp.Integer(0)):
        pi1 = {C: pi0 * T.q * gam * (1 - 2 * a) * (P[C] - Pbar) for C in cs}
        for C0 in cs:
            inflow = sp.Integer(0)
            for C1 in cs:
                for (x, y, C2) in moves(T, C1):
                    if C2 == C0:
                        inflow += r0 * pi1[C1] + r0 * (a * m[C1][T.index[x]] + (1 - a) * m[C1][T.index[y]])
            outflow = sp.Integer(0)
            for (x, y, _) in moves(T, C0):
                outflow += r0 * pi1[C0] + r0 * (a * m[C0][T.index[x]] + (1 - a) * m[C0][T.index[y]])
            ok3 = ok3 and sp.simplify(inflow - outflow) == 0
    # ring-6 pair weights at a = 1: pi1/pi0 = -q gamma (G(D) - Pbar) per unit lambda
    wts = [sp.simplify(-T.q * (T.G[(D,)] - Pbar)) for D in (1, 2, 3)]
    ok3 = ok3 and wts == [-sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 3)]
    checks.check("D3", ok3, "gamma = 2 Gamma/(2 Gamma + 1) = 1 - 1/(2 Gamma) + 1/(4 Gamma^2) - ...; the O(lambda) master equation with the exact m is solved by pi0 (1 + q gamma lambda (1 - 2a)(P(C) - Pbar)), block 95's law at coupling gamma lambda (ring 6, N = 2, a = 1, 1/2, 0); at a = 1 the ring-6 pair weights are -1/3, 1/6, 1/3 times gamma lambda at D = 1, 2, 3")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    T = Torus(5, 1)
    lam, Gam, c = sp.symbols("lambda Gamma c", real=True)
    rho = sp.Matrix(sp.symbols("rho0:5", real=True))
    urho = sp.Matrix(sp.symbols("v0:5", real=True))
    C = frozenset({(1,), (3,)})
    n = sp.Matrix([1 if s in C else 0 for s in T.sites])
    nbar = sp.Rational(2, 5)
    # impose M u_rho = -lambda (rho - nbar) by substituting M u_rho
    u = urho + c * sp.ones(T.V, 1)
    Mu = T.M * u
    ok1 = sp.simplify(Mu - T.M * urho) == sp.zeros(T.V, 1)
    Mu_line = -lam * (rho - nbar * sp.ones(T.V, 1))
    drift = [Gam * sp.exp(u[z]) * (Mu_line[z] + lam * (n[z] - nbar)) for z in range(T.V)]
    sgn = 1 if not mut("line_drift_forged") else -1
    want = [Gam * lam * sp.exp(c) * sp.exp(urho[z]) * (n[z] - sgn * rho[z]) for z in range(T.V)]
    ok1 = ok1 and all(sp.simplify(drift[z] - want[z]) == 0 for z in range(T.V))
    beta_ = sp.Symbol("beta_")
    ws = sp.symbols("w0:5", positive=True)
    # w (n - rho) = beta 1 with sum(n - rho) = 0 forces beta = 0
    diffs = [beta_ / ws[z] for z in range(T.V)]
    sol = sp.solve(sp.Eq(sum(diffs), 0), beta_)
    ok1 = ok1 and sol == [0]
    checks.check("E1", ok1, "on the line u = u_rho + c 1 (M u_rho = -lambda(rho - nbar)) the drift of configuration C is Gamma lambda e^c w_rho (n_C - rho); w_rho (n_C - rho) = beta 1 with sum(n_C - rho) = 0 forces beta = 0 and n_C = rho, so a product law would sit on one configuration, which the positive escape rate forbids")


# ============================================================================================ family F
FENCES = (
    "This note works within block 95 as landed on main (records moving on their own clocks, with the slaved clock field) and adds the supplied clause that the clock field relaxes towards the records at a finite rate; it reports what survives of block 95's pair law and what the delay changes; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at Gamma = 1/2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Dynkin", "LaSalle",
                   "Markov", "Kolmogorov", "Kelvin")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Dynkin) —", 1)
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
    "per_element: executed - the invariant and the energy's decrease along the flow (symbolic)",
    "per_site: executed - the slaved equilibrium on three tori; the separation maps on seven tori",
    "per_mode: executed - the first-order moment system and its two controls on four tori at three Gammas; the rank of its operator",
    "per_block: executed - the O(lambda) record law against block 95 at coupling gamma lambda for three timings; the ring-6 pair weights; the drift on the line",
    "lattice_wide: checked and not executed - well-posedness (A0) and differentiability (A1); orders beyond the first in lambda; the direct simulation",
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
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 95's records with a clock field relaxing at rate Gamma (supplied clause), finite tori, W = 1: the invariant sum 1/w; the separation jumps as a simple random walk; at first order in lambda (given A1) the pair law is block 95's with lambda -> gamma lambda, gamma = 2 Gamma/(2 Gamma + 1); no stationary product law (given A0); harvest of #9158 (confirmed by #9325); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
