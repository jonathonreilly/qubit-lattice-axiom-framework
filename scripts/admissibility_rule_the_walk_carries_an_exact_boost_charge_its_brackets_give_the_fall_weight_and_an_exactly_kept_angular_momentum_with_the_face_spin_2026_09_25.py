#!/usr/bin/env python3
"""Exact checks: the walk carries an exact boost charge - the energy centroid moves with the two-step momentum, so
K = D - tP is kept; the boost-momentum bracket carries cos 2k, block 106's fall weight; the boost-boost bracket is an exactly
kept, mass-independent angular momentum, the two-step orbital part plus the coin's spin on the faces (block 138); the
angular momentum turns the momentum with the same factor; every factor tends to 1 at long wavelength (the supervisor's own
derivation; blocks 54, 73, 77 and 106 as landed or placed; blocks 136, 138 and 139 placed; not adopted).

B (T1): i[H, D_i] = P_i (symbolic and exact vectors, massless and massive).
C (T2): i[D_i, P_j] = - delta_ij cos(2k_j) H.
D (T3): i[D_i, D_j] = eps_ijl J_l, [H, J] = 0.
E (T4): [J_l, P_m] = i eps_lmn cos(2k_m) P_n; the long-wave limit; each species' spin.
Exact rational, Gaussian-rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_WALK_CARRIES_AN_EXACT_BOOST_CHARGE_ITS_BRACKETS_GIVE_THE_FALL_WEIGHT_AND_AN_EXACTLY_KEPT_ANGULAR_MOMENTUM_WITH_THE_FACE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_NO_LOCAL_MOMENTUM_FALLS_WITH_WEIGHT_ONE_ON_THE_LATTICE_THE_WALKS_FORCE_IS_A_BOND_ENERGY_TIMES_A_CLOCK_DIFFERENCE_AND_NO_LEDGER_CAN_DEMAND_IT_EXACTLY_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_walk_carries_an_exact_boost_charge_its_brackets_give_the_fall_weight_and_an_exactly_kept_angular_momentum_with_the_face_spin_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "centroid_momentum_one_step": "B",
    "fall_weight_forged": "C",
    "spin_unaveraged": "D",
    "rotation_weight_forged": "E",
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


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its rest energy and its momenta are supplied; the memo does not define a time metric)")


# ============================================================================================ exact real-space vectors over Q(i) on the open lattice
def gadd(a, b): return (a[0] + b[0], a[1] + b[1])
def gmul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
Z = (Fr(0), Fr(0))
SIG = ({(0, 1): (Fr(1), Fr(0)), (1, 0): (Fr(1), Fr(0))}, {(0, 1): (Fr(0), Fr(-1)), (1, 0): (Fr(0), Fr(1))}, {(0, 0): (Fr(1), Fr(0)), (1, 1): (Fr(-1), Fr(0))})
def vadd(v, key, a):
    nv = gadd(v.get(key, Z), a)
    if nv == Z: v.pop(key, None)
    else: v[key] = nv
def lin(*terms):
    out = {}
    for coef, v in terms:
        for key, a in v.items(): vadd(out, key, gmul(coef, a))
    return out
ONE = (Fr(1), Fr(0)); MONE = (Fr(-1), Fr(0)); I = (Fr(0), Fr(1)); MI = (Fr(0), Fr(-1))
def eps(x): return (-1) ** sum(x)
def shift(x, a, s):
    y = list(x); y[a] += s; return tuple(y)
def H(v, weight=None, M=Fr(0)):
    """(H + M eps) v; weight(t, s) multiplies each hop (for the dipole)"""
    out = {}
    for (x, c), amp in v.items():
        for a in range(3):
            for sg in (1, -1):
                y = shift(x, a, -sg)
                for (d, c2), sv in SIG[a].items():
                    if c2 != c: continue
                    w = gmul((Fr(0), Fr(-sg, 2)), sv)
                    if weight is not None:
                        w = gmul(w, weight(y, x))
                    vadd(out, (y, d), gmul(amp, w))
        if M:
            w = (M * eps(x), Fr(0))
            if weight is not None:
                w = gmul(w, weight(x, x))
            vadd(out, (x, c), gmul(amp, w))
    return out
def Tsh(v, a, s):
    """(T_a^s psi)(x) = psi(x + s e_a): moves amplitude at x to x - s e_a"""
    return {(shift(x, a, -s), c): amp for (x, c), amp in v.items()}
def Pm(v, j):
    """P_j = S_j C_j = (T_j^2 - T_j^-2)/(4i)"""
    return lin((gmul((Fr(1, 4), Fr(0)), MI), Tsh(v, j, 2)), (gmul((Fr(-1, 4), Fr(0)), MI), Tsh(v, j, -2)))
def C(v, j):
    return lin(((Fr(1, 2), Fr(0)), Tsh(v, j, 1)), ((Fr(1, 2), Fr(0)), Tsh(v, j, -1)))
def C2(v, j):
    return lin(((Fr(1, 2), Fr(0)), Tsh(v, j, 2)), ((Fr(1, 2), Fr(0)), Tsh(v, j, -2)))
def X(v, i):
    return {(x, c): gmul(amp, (Fr(x[i]), Fr(0))) for (x, c), amp in v.items() if x[i] != 0}
def D(v, i, M=Fr(0)):
    return H(v, lambda t, s: (Fr(t[i] + s[i], 2), Fr(0)), M)
def sig(v, l):
    out = {}
    for (x, c), amp in v.items():
        for (d, c2), sv in SIG[l].items():
            if c2 == c: vadd(out, (x, d), gmul(amp, sv))
    return out
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
def J(v, l, averaged=True):
    i, j = [m for m in range(3) if m != l]
    e = (Fr(EPS[(i, j, l)]), Fr(0))
    orb = lin((ONE, X(Pm(v, j), i)), (MONE, X(Pm(v, i), j)))
    spin = lin(((Fr(1, 2), Fr(0)), C(C(sig(v, l), i), j) if averaged else sig(v, l)))
    return lin((e, orb), (ONE, spin))
def comm(A, B, v): return lin((ONE, A(B(v))), (MONE, B(A(v))))


def rs_tests():
    out = []
    for c in (0, 1):
        out.append({((0, 0, 0), c): ONE})
        out.append({((1, 2, -1), c): ONE, ((0, 1, 1), 1 - c): (Fr(1, 3), Fr(2, 5))})
    return out


MASSES = (Fr(0), Fr(3, 4))


# ============================================================================================ symbolic operators on spinor functions of k
KS = sp.symbols("k1:4", real=True)
FPSI = sp.Matrix([sp.Function("f1")(*KS), sp.Function("f2")(*KS)])
SGM = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
HK = sum((SGM[a] * sp.sin(KS[a]) for a in range(3)), sp.zeros(2, 2))


def s_H(v):
    return HK * v


def s_X(i, v):
    return sp.I * v.diff(KS[i])


def s_D(i, v):
    return (s_X(i, s_H(v)) + s_H(s_X(i, v))) / 2


def s_P(j, v, one_step=False):
    return v * sp.sin(KS[j]) if one_step else v * sp.sin(KS[j]) * sp.cos(KS[j])


def s_J(l, v, averaged=True):
    i, j = [m for m in range(3) if m != l]
    e = EPS[(i, j, l)]
    orb = e * (s_X(i, s_P(j, v)) - s_X(j, s_P(i, v)))
    w = sp.cos(KS[i]) * sp.cos(KS[j]) if averaged else 1
    return orb + w * SGM[l] * v / 2


def s_comm(A, B, v):
    return (A(B(v)) - B(A(v))).applyfunc(sp.expand)


def s_zero(expr):
    return all(sp.simplify(x) == 0 for x in expr)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the energy centroid moves with the two-step momentum: i[H, D_i] = P_i, so K = D - tP is kept."""
    one = mut("centroid_momentum_one_step")
    ok_s = all(s_zero(sp.I * s_comm(s_H, lambda w: s_D(i, w), FPSI) - s_P(i, FPSI, one)) for i in range(3))
    ok_r = True
    for M in MASSES:
        for v in rs_tests():
            for i in range(3):
                pv = Pm(v, i) if not one else lin((MI, lin(((Fr(1, 2), Fr(0)), Tsh(v, i, 1)), ((Fr(-1, 2), Fr(0)), Tsh(v, i, -1)))))
                r = lin((I, comm(lambda w: H(w, None, M), lambda w: D(w, i, M), v)), (MONE, pv))
                ok_r = ok_r and not r
    checks.check("B1", ok_s and ok_r,
                 "T1: i[H, D_i] = P_i for the energy dipole D_i = (X_i H + H X_i)/2 (the first moment of the averaged energy e') and the two-step momentum P_i = S_i C_i: symbolically on spinor functions of k, and as exact vectors over Q(i) on the open lattice for the massless walk and with the staggered mass m = 3/4 (both H + m eps and its dipole); so the boost charge K_i = D_i - t P_i is kept, on the stated common operator domain")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the boost-momentum bracket is deformed by cos 2k_j, block 106's fall weight."""
    forged = mut("fall_weight_forged")
    ok_s = True
    for i in range(3):
        for j in range(3):
            lhs = sp.I * s_comm(lambda w: s_D(i, w), lambda w: s_P(j, w), FPSI)
            if i == j:
                w8 = sp.cos(KS[j]) if forged else sp.cos(2 * KS[j])
                lhs = lhs + w8 * HK * FPSI
            ok_s = ok_s and s_zero(lhs)
    ok_r = True
    for M in MASSES:
        for v in rs_tests():
            for i in range(3):
                for j in range(3):
                    r = lin((I, comm(lambda w: D(w, i, M), lambda w: Pm(w, j), v)))
                    if i == j:
                        r = lin((ONE, r), (ONE, C2(H(v, None, M), j)))
                    ok_r = ok_r and not r
    checks.check("C1", ok_s and ok_r,
                 "T2: i[D_i, P_j] = - delta_ij cos(2 k_j) H (on the lattice, C2_j H with C2_j = (T_j^2 + T_j^-2)/2), symbolically and as exact vectors, massless and massive: the boost-momentum bracket carries the factor cos 2k, which is block 106's fall weight of the two-step momentum; at every species corner cos 2(pi n + kappa) = cos 2 kappa")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the boost-boost bracket is an exactly kept angular momentum: orbital two-step part plus the face spin."""
    averaged = not mut("spin_unaveraged")
    ok_s = True
    for (i, j) in ((0, 1), (1, 2), (2, 0)):
        l = 3 - i - j
        lhs = sp.I * s_comm(lambda w: s_D(i, w), lambda w: s_D(j, w), FPSI) - EPS[(i, j, l)] * s_J(l, FPSI, averaged)
        ok_s = ok_s and s_zero(lhs)
    ok_k = all(s_zero(s_comm(s_H, lambda w: s_J(l, w), FPSI)) for l in range(3))
    ok_r = True
    for M in MASSES:
        for v in rs_tests():
            for (i, j) in ((0, 1), (1, 2), (2, 0)):
                l = 3 - i - j
                r = lin((I, comm(lambda w: D(w, i, M), lambda w: D(w, j, M), v)), (MONE, J(v, l, averaged)))
                ok_r = ok_r and not r
            for l in range(3):
                ok_r = ok_r and not comm(lambda w: H(w, None, M), lambda w: J(w, l), v)
    checks.check("D1", ok_s and ok_k and ok_r,
                 "T3: i[D_i, D_j] = eps_ijl J_l with J_l = (X x P)_l + (1/2) C_i C_j sigma_l ({i, j} the directions other than l): the orbital angular momentum of the two-step momentum plus the coin's spin sigma/2 carried on the faces (block 138's face spin, summed); [H, J_l] = 0 exactly; symbolically, and as exact vectors for the massless walk and with the staggered mass, where J is the same: the boost charges' bracket is an exactly kept, mass-independent angular momentum")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the rest of the algebra, its long-wave limit, and each species' own spin."""
    forged = mut("rotation_weight_forged")
    ok_jp = True
    for l in range(3):
        for m in range(3):
            lhs = s_comm(lambda w: s_J(l, w), lambda w: s_P(m, w), FPSI)
            for n in range(3):
                e = EPS.get((l, m, n), 0)
                if e:
                    w8 = sp.cos(2 * KS[n]) if forged else sp.cos(2 * KS[m])
                    lhs = lhs - sp.I * e * w8 * s_P(n, FPSI)
            ok_jp = ok_jp and s_zero(lhs)
    t = sp.symbols("tau", positive=True)
    kap = sp.symbols("kappa1:4", real=True)
    lim = sp.series(sp.cos(2 * t * kap[0]), t, 0, 3).removeO()
    ok_lim = sp.expand(lim - (1 - 2 * t ** 2 * kap[0] ** 2)) == 0
    ok_species = True
    for n in product((0, 1), repeat=3):
        for (i, j) in ((0, 1), (1, 2), (2, 0)):
            wt = sp.cos(sp.pi * n[i] + t * kap[i]) * sp.cos(sp.pi * n[j] + t * kap[j])
            lead = sp.limit(wt, t, 0)
            ok_species = ok_species and lead == (-1) ** (n[i] + n[j])
    checks.check("E1", ok_jp and ok_lim and ok_species,
                 "T4: [J_l, P_m] = i eps_lmn cos(2 k_m) P_n (symbolically): the angular momentum turns the two-step momentum with the same factor cos 2k; every factor tends to 1 at long wavelength (cos 2 tau kappa = 1 - 2 tau^2 kappa^2 + ...), where the brackets become the comparator's kinematic ones with J = L + sigma/2; at the species corner pi n the spin weight cos k_i cos k_j tends to (-1)^(n_i + n_j), each species' own spin for its reflected frame")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 73, 77 and 106 as landed on main (the walk, the two-step momentum, the staggered rest energy and the fall weight), with blocks 136, 138 and 139 placed; it reports the brackets of the walk's energy dipole with the energy, the momentum and itself; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
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
    "per_element: executed - i[H, D] = P, the boost-momentum and boost-boost brackets and [H, J] = 0 as exact vectors over Q(i) on the open lattice, massless and with m = 3/4",
    "per_site: executed - four test states per mass, every component",
    "per_mode: executed - all brackets symbolically on spinor functions of k: i[H, D_i], i[D_i, P_j], i[D_i, D_j], [H, J_l], [J_l, P_m]",
    "per_block: executed - the long-wave series of the factors and the species' spin signs at all eight corners",
    "lattice_wide: identities of operators on the whole lattice (symbolic in k); the J-J bracket not claimed exact; the walk and its rest energy supplied",
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
    print('scope: Common-domain dipole/bracket identities; no full symmetry group or unproved self-bracket. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
