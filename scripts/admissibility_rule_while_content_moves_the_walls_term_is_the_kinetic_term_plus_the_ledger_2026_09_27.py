#!/usr/bin/env python3
"""Exact checks: while content moves, the walls' term of block 60's box equals the lengths' kinetic term plus the ledger at
every label time, and moves only by the content's explicit dependence on the label: for supplied content at rest, by the
work the supply does; for a walker, by the commutator of its generator with its ledger (a harvest of probe #8757, confirmed
by an other-family referee in #9344). Block 60 as landed: weight one, T1(c), the bond form, the kinetic instance.

A (premises): landed block 60's T1(c), the curvature member's bond form, the kinetic instance and its comparator values.
B (T1): on the 2^3 box with its 24 walls, exactly at a rational point with the walls at 1: sum_all u-derivatives of the ledger is
   the ledger (weight one) and of the kinetic term minus itself (weight -1); the walls' term is 8K times the flux of chi;
   h - Wt = -sum_I dL/du for rest content and for a two-component walker.
C (T2): the energy function h = sum lamdot dL/dlamdot - L has dh/dt = sum lamdot(EL_lambda) - sum udot dL/du - dL/dt (symbolic).
D (T3): on the 3^3 interior (K = 1/2, c_k = -6K): g_cc = 11/51, g_face = 145/714; the changes +3/952 and -61/2856; for the smooth
   step 3t^2 - 2t^3, d/dt Wt^(2) = sum w_1 rhodot as a polynomial identity, with Wt^(2) = -(rho.g rho + 3 rhodot.g^2 rhodot)/(8K).
E (T4): for i psidot = G psi at fixed fields, d<H>/dt = i<[G, H]>, zero for G = H.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WHILE_CONTENT_MOVES_THE_WALLS_TERM_IS_THE_KINETIC_TERM_PLUS_THE_LEDGER_AND_MOVES_ONLY_BY_THE_WORK_OF_WHAT_DRIVES_THE_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_while_content_moves_the_walls_term_is_the_kinetic_term_plus_the_ledger_and_moves_only_by_the_work_of_what_drives_the_content_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED60 = (
    "(c) If the rates of a set `W` of sites are held and `𝓔` is stationary in every other `u_x`, then `𝓔 = Σ_{x∈W} ∂𝓔/∂u_x`.",
    "the local instance `Σ_x c_k ℓ_x^s (dλ_x/dt)²/w_x`",
    "The comparator's values are `s = 3` (the volume) and `c_k = −6K`.",
    "`F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "kinetic_weight_forged": "B",
    "energy_function_forged": "C",
    "green_value_forged": "D",
    "commutator_sign_forged": "E",
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
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, the kinetic term, the content and its motion are supplied)")
    needles = list(LANDED60)
    if mut("landed_quote_forged"):
        needles[2] = "The comparator's values are `s = 3` (the volume) and `c_k = −8K`."
    checks.check("A3", all(n in landed for n in needles), "landed block 60: T1(c) (held walls: the ledger is the walls' term), the kinetic instance sum c_k l^s lamdot^2/w with the comparator's s = 3 and c_k = -6K, and the curvature member's bond form")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    interior = [(i, j, k) for i in (1, 2) for j in (1, 2) for k in (1, 2)]
    Iset = set(interior)
    walls = sorted({add(x, d) for x in interior for d in DIRS} - Iset)
    sites = interior + walls
    bonds = sorted({tuple(sorted((x, add(x, d)))) for x in interior for d in DIRS})
    K = sp.Rational(1, 2)
    ck = -6 * K
    phi = {x: sp.Symbol("phi_%d%d%d" % x, positive=True) for x in sites}          # w = phi^2
    chi = {x: sp.Symbol("chi_%d%d%d" % x, positive=True) for x in sites}
    lamdot = {x: sp.Rational(random.Random(3).randint(1, 9) + i, 7) for i, x in enumerate(interior)}
    w = {x: phi[x] ** 2 for x in sites}
    Nf = {x: w[x] * chi[x] for x in sites}
    F = -8 * K * sum((Nf[b[1]] - Nf[b[0]]) * (chi[b[1]] - chi[b[0]]) for b in bonds)
    rho = {x: sp.Rational(i + 2, 5) for i, x in enumerate(interior)}
    H_rest = sum(w[x] * rho[x] for x in interior)
    s_exp = 3
    Kin = sum(ck * chi[x] ** (2 * s_exp) * lamdot[x] ** 2 / w[x] for x in interior)
    du = lambda E, x: phi[x] * sp.diff(E, phi[x]) / 2                              # d/du = w d/dw = (phi/2) d/dphi
    rng = random.Random(60)
    point = {}
    for x in sites:
        if x in Iset:
            point[phi[x]] = sp.Rational(rng.randint(5, 12), 9)
            point[chi[x]] = sp.Rational(rng.randint(9, 15), 11)
        else:
            point[phi[x]] = 1
            point[chi[x]] = 1
    ok = True
    Ledger = H_rest + F
    sumE = sum(du(Ledger, x) for x in sites)
    sumK = sum(du(Kin, x) for x in sites)
    wantK = -Kin if not mut("kinetic_weight_forged") else Kin
    ok = ok and sp.simplify((sumE - Ledger).subs(point)) == 0 and sp.simplify((sumK - wantK).subs(point)) == 0
    Wt = sum(du(Ledger, x) for x in walls).subs(point)
    lap = {x: sum(chi[add(x, d)] - chi[x] for d in DIRS if tuple(sorted((x, add(x, d)))) in set(bonds)) for x in sites}
    flux = 8 * K * sum(lap[x] for x in walls).subs(point)
    ok = ok and sp.simplify(Wt - flux) == 0 and sp.simplify(sum(lap[x] for x in sites)) == 0
    h = (Kin + Ledger).subs(point)
    L = Kin - Ledger
    ok = ok and sp.simplify(h - Wt + sum(du(L, x) for x in interior).subs(point)) == 0
    # a two-component walker on the interior: <H> = psi^dag A H A psi, A = phi/chi, H = sum_j sigma_j S_j restricted to I
    SX = sp.Matrix([[0, 1], [1, 0]])
    SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    SZ = sp.Matrix([[1, 0], [0, -1]])
    sig = (SX, SY, SZ)
    idx = {x: i for i, x in enumerate(interior)}
    n = len(interior)
    Hm = sp.zeros(2 * n, 2 * n)
    for j in range(3):
        e = [0, 0, 0]
        e[j] = 1
        e = tuple(e)
        for x in interior:
            y = add(x, e)
            if y in Iset:
                blk = sig[j] / (2 * sp.I)
                Hm[2 * idx[x]:2 * idx[x] + 2, 2 * idx[y]:2 * idx[y] + 2] += blk
                Hm[2 * idx[y]:2 * idx[y] + 2, 2 * idx[x]:2 * idx[x] + 2] += -blk
    A = sp.diag(*[phi[x] / chi[x] for x in interior for _ in range(2)])
    psi = sp.Matrix([sp.Rational(rng.randint(-5, 5), 7) + sp.I * sp.Rational(rng.randint(-5, 5), 7) for _ in range(2 * n)])
    Hw = sp.expand((psi.H * A * Hm * A * psi)[0])
    Ledger_w = Hw + F
    sumEw = sum(du(Ledger_w, x) for x in sites)
    ok_w = sp.simplify((sumEw - Ledger_w).subs(point)) == 0
    Lw = Kin - Ledger_w
    Wtw = sum(du(Ledger_w, x) for x in walls).subs(point)
    ok_w = ok_w and sp.simplify((Kin + Ledger_w).subs(point) - Wtw + sum(du(Lw, x) for x in interior).subs(point)) == 0 and sp.simplify(Wtw - flux) == 0
    checks.check("B1", ok and ok_w, "the 2^3 box with its 24 walls, exactly at a rational point with the walls at w = chi = 1: sum over all sites of d/du of the ledger is the ledger and of the kinetic term sum c_k chi^6 lamdot^2/w is minus itself; the walls' term equals 8K times the flux of chi into the walls; h - Wt = -sum_I dL/du for supplied content at rest and for a two-component walker crossing bonds at sqrt(w_x w_y)/(chi_x chi_y)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    t = sp.Symbol("t")
    l1, l2, d1, d2, u1, u2 = sp.symbols("l1 l2 d1 d2 u1 u2")
    rho = t ** 3 + 2 * t                                     # an explicit label dependence of the content
    c1 = 1 + l1 ** 2 + u1 * u2
    c2 = 2 + l2 * u1
    c3 = l1 - u2
    E = u1 * l1 ** 2 + u2 * l2 + (1 + l1) * rho + l1 * l2 * u1 * rho
    L = c1 * d1 ** 2 + c2 * d2 ** 2 + c3 * d1 * d2 - E       # quadratic in the lengths' rates, no rate of change of a rate
    path = {l1: 1 + t ** 2, l2: t - t ** 3 / 3, u1: 2 + t, u2: 1 - t ** 2}
    path[d1] = sp.diff(path[l1], t)
    path[d2] = sp.diff(path[l2], t)
    on = lambda ex: sp.expand(ex.subs(path, simultaneous=True))
    p1, p2 = sp.diff(L, d1), sp.diff(L, d2)
    h = d1 * p1 + d2 * p2 - L
    dh = sp.diff(on(h), t)
    EL1 = sp.diff(on(p1), t) - on(sp.diff(L, l1))
    EL2 = sp.diff(on(p2), t) - on(sp.diff(L, l2))
    udot_terms = sp.diff(path[u1], t) * on(sp.diff(L, u1)) + sp.diff(path[u2], t) * on(sp.diff(L, u2))
    dLdt = on(sp.diff(L, t))
    rhs = path[d1] * EL1 + path[d2] * EL2 - udot_terms - dLdt
    if mut("energy_function_forged"):
        rhs = rhs + udot_terms
    ok = sp.expand(dh - rhs) == 0 and sp.expand(on(h) - on(c1 * d1 ** 2 + c2 * d2 ** 2 + c3 * d1 * d2 + E)) == 0
    checks.check("C1", ok, "for L = (a form quadratic in the lengths' rates, coefficients depending on lengths and rates) - (a ledger with an explicit label dependence), along arbitrary polynomial paths: h = sum lamdot dL/dlamdot - L equals the kinetic term plus the ledger, and dh/dt = sum lamdot (d/dt dL/dlamdot - dL/dlambda) - sum udot dL/du - dL/dt exactly; on solutions dh/dt = -dL/dt, the content's explicit label derivative")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    interior = [(i, j, k) for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)]
    idx = {x: i for i, x in enumerate(interior)}
    n = len(interior)
    Lap = sp.zeros(n, n)
    for x in interior:
        Lap[idx[x], idx[x]] = 6
        for d in DIRS:
            y = add(x, d)
            if y in idx:
                Lap[idx[x], idx[y]] = -1
    g = Lap.inv()                                            # the inverse of -Delta on the interior with zero walls
    c, f, fo = (2, 2, 2), (2, 2, 1), (2, 2, 3)
    gcc, gff = g[idx[c], idx[c]], g[idx[f], idx[f]]
    want_face = sp.Rational(145, 714) if not mut("green_value_forged") else sp.Rational(145, 713)
    K = sp.Rational(1, 2)
    ok = gcc == sp.Rational(11, 51) and gff == want_face
    ok = ok and (gcc - gff) / (8 * K) == sp.Rational(3, 952)
    # a second body carried from the opposite face onto the centre beside a body fixed on a face
    before = g[idx[f], idx[f]] + g[idx[fo], idx[fo]] + 2 * g[idx[f], idx[fo]]
    after = g[idx[f], idx[f]] + g[idx[c], idx[c]] + 2 * g[idx[f], idx[c]]
    ok = ok and -(after - before) / (8 * K) == -sp.Rational(61, 2856)
    # the smooth step: d/dt Wt^(2) = sum w_1 rhodot as a polynomial identity in t
    t = sp.Symbol("t")
    ck = -6 * K
    sgm = 3 * t ** 2 - 2 * t ** 3
    rho = sp.zeros(n, 1)
    rho[idx[c]] = 1 - sgm
    rho[idx[f]] = sgm
    chi1 = g * rho / (8 * K)
    chi1dd = chi1.diff(t, 2)
    w1 = -2 * chi1 + (ck / K) * g * chi1dd
    lam1dot = 2 * chi1.diff(t)
    Wt2 = -(rho.T * g * rho)[0] / (8 * K) + ck * (lam1dot.T * lam1dot)[0]
    closed = -((rho.T * g * rho)[0] + 3 * (rho.diff(t).T * g * g * rho.diff(t))[0]) / (8 * K)
    ok = ok and sp.expand(Wt2 - closed) == 0
    ok = ok and sp.expand(sp.diff(Wt2, t) - (w1.T * rho.diff(t))[0]) == 0
    flux_one = sum(g[idx[x], idx[c]] * sum(1 for d in DIRS if add(x, d) not in idx) for x in interior)
    ok = ok and flux_one == 1
    checks.check("D1", ok, "the 3^3 interior with zero walls, K = 1/2, c_k = -6K: g_cc = 11/51 and g_face = 145/714; a body carried from the centre to a face raises Wt^(2) by 3/952, and one carried from the opposite face onto the centre beside a fixed face body lowers it by 61/2856; along the smooth step 3t^2 - 2t^3, Wt^(2) = -(rho.g rho + 3 rhodot.g^2 rhodot)/(8K) and dWt^(2)/dt = sum w_1 rhodot exactly, with w_1 = -2chi_1 + (c_k/K) g chi_1'' and chi_1 = g rho/(8K); a unit source sends flux 1 into the walls")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    rng = random.Random(8757)
    n = 4

    def herm():
        M = sp.zeros(n, n)
        for i in range(n):
            M[i, i] = sp.Rational(rng.randint(-5, 5), 3)
            for j in range(i + 1, n):
                z = sp.Rational(rng.randint(-5, 5), 3) + sp.I * sp.Rational(rng.randint(-5, 5), 3)
                M[i, j] = z
                M[j, i] = sp.conjugate(z)
        return M

    H = herm()
    G = herm()
    psi = sp.Matrix([sp.Rational(rng.randint(-4, 4), 5) + sp.I * sp.Rational(rng.randint(-4, 4), 5) for _ in range(n)])
    psidot = -sp.I * G * psi
    dH = sp.expand((psidot.H * H * psi)[0] + (psi.H * H * psidot)[0])
    sgn = 1 if not mut("commutator_sign_forged") else -1
    comm = sp.expand(sgn * sp.I * (psi.H * (G * H - H * G) * psi)[0])
    same = sp.expand(((-sp.I * H * psi).H * H * psi)[0] + (psi.H * H * (-sp.I * H * psi))[0])
    checks.check("E1", sp.simplify(dH - comm) == 0 and same == 0, "for i psidot = G psi at fixed fields, d<psi|H|psi>/dt = i<psi|[G, H]|psi> (random Hermitian 4x4, exact), and it is zero for G = H: a walker moved by its own ledger's generator keeps the ledger, and so the walls' term, while one moved by another generator changes it at i<[G, H_eff]>")


# ============================================================================================ family F
FENCES = (
    "This note works within block 60 as landed on main (the walled box, the ledger of weight one, the curvature member and the lengths' kinetic term) and asks what the walls' term does while content moves; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at c_k = -6K."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Arnowitt", "Misner",
                   "Komar", "Tolman", "Legendre", "Jacobi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Noether) —", 1)
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
    "per_element: executed - the weights of the ledger and the kinetic term under scaling of every rate",
    "per_site: executed - the walls' term as the flux of chi on the 2^3 box, for rest content and a walker",
    "per_mode: executed - the energy function's derivative for a generic quadratic kinetic term",
    "per_block: executed - the 3^3 interior's Green values, the two moves, and the smooth step's rate as a polynomial identity",
    "lattice_wide: checked and not executed - existence of slaved branches for walker content and with the kinetic term; the strong-field motion",
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
    print(f"scope: block 60's walled box: the walls' term equals the kinetic term plus the ledger at every label time on solutions and moves only by the content's explicit label dependence; for supplied rest content by the supply's work sum w rhodot; at weak field Wt = sum rho - (rho.g rho + 3 rhodot.g^2 rhodot)/(8K); for a walker by i<[G, H_eff]>; harvest of #8757 (confirmed by #9344); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
