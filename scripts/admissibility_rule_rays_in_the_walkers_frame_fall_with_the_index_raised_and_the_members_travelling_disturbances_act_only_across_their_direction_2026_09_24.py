#!/usr/bin/env python3
"""Exact checks: rays in the walker's frame - the fall has its index raised by the inverse metric, block 60's field read
as a frame bends rays twice as much as it makes bodies fall, the member's travelling transverse disturbances act on a ray
only across their direction of travel, and a uniform rest energy fits only a frame of rank two while the staggered one
fits every frame (a harvest block from a Grok-refereed probes attempt; blocks 59, 60, 62 and 77 as landed; the ray limit
declared; not adopted).

B (T1): the ray equations and the fall.
C (T2): block 60's field as a frame.
D (T3): rays in a travelling transverse disturbance.
E (T4): rest energy and the frame.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_RAYS_IN_THE_WALKERS_FRAME_FALL_WITH_THE_INDEX_RAISED_AND_THE_MEMBERS_TRAVELLING_DISTURBANCES_ACT_ONLY_ACROSS_THEIR_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_rays_in_the_walkers_frame_fall_with_the_index_raised_and_the_members_travelling_disturbances_act_only_across_their_direction_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "fall_index_forged": "B",
    "bending_ratio_forged": "C",
    "ray_row_forged": "D",
    "stagger_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged (no coin axis carries a preferred rest energy); no site is privileged (the staggered sign breaks one-site translation, as block 77 notes); Admissibility is not a dynamics axiom (the frame, the rates and the ray limit are supplied)")


# ============================================================================================ rays of the walker's symbol in a frame
X3 = sp.symbols("x1:4", real=True)
K3 = sp.symbols("k1:4", real=True)
MM = sp.symbols("m", positive=True)


def ray_energy(afun, wfun, ginv):
    s = [sp.sin(k) for k in K3]
    return sp.sqrt(afun ** 2 * MM ** 2 + wfun ** 2 * sum(ginv[i, j] * s[i] * s[j] for i in range(3) for j in range(3)))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the ray equations with the full inverse metric, and the fall with the index raised."""
    afun = sp.Function("a", positive=True)(*X3)
    wfun = sp.Function("w", positive=True)(*X3)
    gfun = [[sp.Function(f"g{min(i, j)}{max(i, j)}")(*X3) for j in range(3)] for i in range(3)]
    ginv = sp.Matrix(3, 3, lambda i, j: gfun[i][j])
    en = ray_energy(afun, wfun, ginv)
    s = [sp.sin(k) for k in K3]
    ok_v = True
    for i in range(3):
        want = wfun ** 2 * sum(ginv[i, j] * s[j] for j in range(3)) * sp.cos(K3[i]) / en
        ok_v = ok_v and sp.simplify(sp.diff(en, K3[i]) - want) == 0
    ok_fall = True
    at0 = {K3[0]: 0, K3[1]: 0, K3[2]: 0}
    for i in range(3):
        acc = sum(sp.diff(sp.diff(en, K3[i]), K3[l]).subs(at0) * (-sp.diff(en, X3[l])).subs(at0) for l in range(3))
        want = -(wfun ** 2 / afun) * sum(ginv[i, l] * sp.diff(afun, X3[l]) for l in range(3))
        if mut("fall_index_forged"):
            want = -(wfun ** 2 / afun) * sp.diff(afun, X3[i])
        ok_fall = ok_fall and sp.simplify(acc - want) == 0
    checks.check("B1", ok_v and ok_fall,
                 "T1: for E^2 = a^2 m^2 + w^2 g^{ij} sin k_i sin k_j with a, w and the six g^{ij} general functions of position, the group velocity is exactly v_i = w^2 g^{ij} sin k_j cos k_i / E, and a slow body at k = 0 accelerates as dv_i/dt = -(w^2/a) g^{il} d_l a: the fall is block 59's with the index raised by the inverse metric")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: block 60's field read as a frame - bending twice the fall, and the strong-field ratio."""
    w, wbar, pp, qq, g = sp.symbols("w wbar P Q g", positive=True)
    ell = wbar / w
    c = w / ell
    a = w
    ratio = sp.simplify(sp.diff(sp.log(c), w) / sp.diff(sp.log(a), w))
    want = 2
    if mut("bending_ratio_forged"):
        want = 3
    ok_weak = ratio == want
    chi = 1 + qq * g
    nn = 1 - pp * g
    c_s = nn / chi ** 3
    a_s = nn / chi
    lc = sp.series(sp.log(c_s), g, 0, 2).removeO()
    la = sp.series(sp.log(a_s), g, 0, 2).removeO()
    ok_strong = sp.simplify(lc + (pp + 3 * qq) * g) == 0 and sp.simplify(la + (pp + qq) * g) == 0
    checks.check("C1", ok_weak and ok_strong,
                 "T2: block 60's weak field as the frame E = (1/l) 1 with l = wbar/w and the rest energy timed by a = w gives the light speed c = w/l = w^2/wbar, so d log c/d log a = 2 exactly (the stipulated local axial transverse-acceleration ratio, not integrated deflection); in block 60's strong field (l = chi^2, w = N/chi) the far-field logarithms are log c = -(P + 3Q) g and log a = -(P + Q) g at first order, ratio (P + 3Q)/(P + Q)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the member's travelling disturbances act on rays only across their direction."""
    ap, ax, q, t, z0 = sp.symbols("A_plus A_times q t z0", real=True)
    om = sp.symbols("Omega", positive=True)
    eps = sp.symbols("epsilon")
    ph = q * X3[2] - om * t
    h = sp.Matrix([[ap * sp.cos(ph), ax * sp.cos(ph), 0], [ax * sp.cos(ph), -ap * sp.cos(ph), 0], [0, 0, 0]])
    ginv = sp.eye(3) - eps * h
    s = [sp.sin(k) for k in K3]
    en = sp.sqrt(sum(ginv[i, j] * s[i] * s[j] for i in range(3) for j in range(3)))
    kap = sp.pi / 3
    along1 = {K3[0]: kap, K3[1]: 0, K3[2]: 0}
    v = [sp.series(sp.diff(en, K3[i]).subs(along1), eps, 0, 2).removeO() for i in range(3)]
    kdot = [sp.series((-sp.diff(en, X3[i])).subs(along1), eps, 0, 2).removeO() for i in range(3)]
    want_v = [sp.cos(kap) * (1 - eps * h[0, 0] / 2), -eps * h[0, 1], 0]
    want_k = [0, 0, eps * sp.sin(kap) / 2 * sp.diff(h[0, 0], X3[2])]
    if mut("ray_row_forged"):
        want_v[1] = -eps * h[0, 1] / 2
    ok_row = all(sp.simplify(v[i] - want_v[i]) == 0 for i in range(3)) and all(sp.simplify(kdot[i] - want_k[i]) == 0 for i in range(3))
    along3 = {K3[0]: 0, K3[1]: 0, K3[2]: kap}
    v3 = [sp.series(sp.diff(en, K3[i]).subs(along3), eps, 0, 2).removeO() for i in range(3)]
    k3 = [sp.series((-sp.diff(en, X3[i])).subs(along3), eps, 0, 2).removeO() for i in range(3)]
    ok_along = sp.simplify(v3[2] - sp.cos(kap)) == 0 and all(sp.simplify(v3[i]) == 0 for i in range(2)) and all(sp.simplify(k3[i]) == 0 for i in range(3))
    tt = sp.symbols("T", positive=True)
    drift = sp.integrate((-ax * sp.cos(q * z0 - om * t)), (t, 0, tt))
    ok_bound = sp.simplify(drift - (-ax * (sp.sin(q * z0) - sp.sin(q * z0 - om * tt)) / om)) == 0
    checks.check("D1", ok_row and ok_along and ok_bound,
                 "T3: for a travelling transverse traceless disturbance h = (A+ (e1e1 - e2e2) + Ax (e1e2 + e2e1)) cos(q x3 - Omega t), g^{ij} = delta - h at first order, a ray along axis 1 at k = pi/3 has v1 = cos k (1 - h11/2), v2 = -h12, v3 = 0 only at exactly axial momentum; induced k3 changes v3 at first order, kdot2 = 0 and kdot3 = (sin k/2) d3 h11 (delayed by h11, turned towards its gradient, drifted by h12), and a ray along the wave vector feels nothing at first order; along the unperturbed ray the drift integrates to -Ax (sin q z0 - sin(q z0 - Omega T))/Omega, bounded by 2|Ax|/Omega")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: a uniform rest energy needs a frame of rank at most two; the staggered one fits every frame."""
    s1, s2, s3 = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    m0, m1, m2, m3 = sp.symbols("m0:4")
    mat = m0 * sp.eye(2) + m1 * s1 + m2 * s2 + m3 * s3
    eqs = []
    for sb in (s1, s2, s3):
        eqs += list(mat * sb + sb * mat)
    sol = sp.solve(eqs, [m0, m1, m2, m3], dict=True)
    ok_none = sol == [{m0: 0, m1: 0, m2: 0, m3: 0}]
    e1, e2, e3 = sp.symbols("E1 E2 E3")
    frame_vec = e1 * s1 + e2 * s2 + e3 * s3
    ok_reduced = sp.simplify(s1 * frame_vec + frame_vec * s1 - 2 * e1 * sp.eye(2)) == sp.zeros(2, 2)
    ll = 4
    idx = {}
    for x in product(range(ll), repeat=3):
        for cc in range(2):
            idx[(x, cc)] = len(idx)
    dim = len(idx)
    sig = (s1, s2, s3)
    hmat = {}
    seed = 7
    frame = {}
    for x in product(range(ll), repeat=3):
        for j in range(3):
            vec = []
            for a in range(3):
                seed = (seed * 1103515245 + 12345) % 2147483648
                vec.append((seed >> 16) % 5 - 2)
            frame[(x, j)] = vec
    for x in product(range(ll), repeat=3):
        for j in range(3):
            y = list(x)
            y[j] = (y[j] + 1) % ll
            y = tuple(y)
            ev = frame[(x, j)]
            ev_y = frame[(y, j)]
            for cc in range(2):
                for d in range(2):
                    amp_x = sum(ev[a] * sig[a][cc, d] for a in range(3))
                    amp_y = sum(ev_y[a] * sig[a][cc, d] for a in range(3))
                    val = (amp_x + amp_y) / (4 * sp.I)
                    if val != 0:
                        k1_, k2_ = (idx[(x, cc)], idx[(y, d)]), (idx[(y, d)], idx[(x, cc)])
                        hmat[k1_] = hmat.get(k1_, 0) + val
                        hmat[k2_] = hmat.get(k2_, 0) + sp.conjugate(val)
    hh = sp.SparseMatrix(dim, dim, hmat)
    epsm = sp.SparseMatrix(dim, dim, {(idx[(x, cc)], idx[(x, cc)]): (-1) ** sum(x) for x in product(range(ll), repeat=3) for cc in range(2)})
    ok_anti = (epsm * hh + hh * epsm).applyfunc(sp.expand).is_zero_matrix
    if mut("stagger_forged"):
        ok_anti = ok_anti and False
    ok_sq = (((hh + MM * epsm) ** 2) - hh ** 2 - MM ** 2 * sp.SparseMatrix(sp.eye(dim))).applyfunc(sp.expand).is_zero_matrix
    ok_herm = (hh - hh.H).applyfunc(sp.expand).is_zero_matrix
    checks.check("E1", ok_none and ok_reduced and ok_anti and ok_sq and ok_herm,
                 "T4: M = m0 + m.sigma anticommutes with sigma_1, sigma_2, sigma_3 only if M = 0, and {sigma_1, E.sigma} = 2 E_1, a uniform anticommuting mass requires the global actual bond-vector span to have rank at most two; the pointwise varying-frame rank is not the criterion (the reduced walk's m sigma_1 needs E_1^j = 0); on the 4^3 torus with a varying integer frame field (symmetrised bond hops), the staggered sign anticommutes with the walk and (H + m eps)^2 = H^2 + m^2 exactly: the staggered rest energy fits every frame")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 59, 60, 62 and 77 as landed on main (rays and rates, the curvature member's field, the coin's frame and its disturbances, and the staggered sign), with the ray limit declared; it reports how rays move in a frame, what the member's travelling disturbances do to them, and which rest energy a frame admits; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Hamilton", "Jacobi", "Berry", "Fermat", "Snell", "Eddington", "Shapiro", "Einstein", "Dirac", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the group velocity and the fall with a, w and the six inverse-metric components general functions of position",
    "per_site: executed - the light speed and rest-energy timing of block 60's weak and strong fields read as a frame",
    "per_mode: executed - a ray along an axis and along the wave vector in a travelling transverse traceless disturbance, at first order; the integrated drift",
    "per_block: executed - the anticommutation of a uniform rest energy with the coin matrices; the staggered sign against a varying integer frame on the 4^3 torus",
    "lattice_wide: T1-T3 in the ray limit (declared) and at first order in the disturbance for T3; T4 exact on every even torus; no packet control; the frame, rates and disturbances supplied",
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
    print('scope: Local supplied-ray accelerations; induced longitudinal drift corrected; global bond-span mass criterion. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
