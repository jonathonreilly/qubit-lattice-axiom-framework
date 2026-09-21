#!/usr/bin/env python3
"""Exact checks: a delay for the rate field (supplied clauses on Z^3; not adopted).

SETTING (blocks 53-56, open PRs; supplied): rates w_x = phi_x^2 = exp(u_x); amplitudes timed by them; a kept ledger whose terms have weight one.
NO MASTER CLOCK, AT EVERY INSTANT: the parameter t along which motion is written is arbitrary.  Under t -> f(t) the rates go to w/f', so
u -> u - log f' and  du/dt -> (du/dt - f''/f')/f'.  Block 54's law and every ledger term of weight one are unchanged (L dt is invariant).
T1 (what a kinetic term may see): K dt is unchanged for every f iff K depends on the du_x/dt only through differences between sites (for a
   quadratic form (1/2) v^T M v: iff M 1 = 0) and has weight one.  The on-site term sum (du_x/dt)^2 / w_x is unchanged only for f'' = 0.
T2 (neighbours only): a nearest-neighbour, covariant quadratic form with M 1 = 0 is a multiple of the lattice operator Lam of sum over bonds
   (v_x - v_y)^2 -- the same operator as the weak-field bond energy.  So Lam [(kappa/wbar) d^2u/dt^2 + (wbar/gamma) u] = -P_0 s: every mode
   swings at the one frequency wbar/sqrt(gamma kappa), and the field of a source switched on is its STATIC profile times one function of time:
   it appears everywhere at once.  With longer finite range the band has a gap and no branch through zero: nothing travels at long wavelength.
T3 (a reference clock): referring every rate to one clock of the system (the clocks at the walls, or the lattice mean) gives a form with
   M 1 = 0 that is not of finite range; at weak field d^2u/dt^2 = c^2 wbar^2 Lap u - source: a front moving c sites per local tick.
T4 (a master parameter): the on-site term (1/(2 gamma c^2)) sum (du/dt)^2/w = (2/(gamma c^2)) sum (dpsi/dt)^2, psi = w^(-1/2), gives the same
   waves, and on a closed lattice a uniform mode that moves: d^2 psi_0/dt^2 = gamma c^2 (ledger's static part)/(2 N psi_0) > 0.
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_DELAY_FOR_THE_RATE_FIELD_NEIGHBOUR_REFERRED_MOTION_DOES_NOT_PROPAGATE_A_REFERENCE_TO_DISTANT_CLOCKS_DOES_AT_A_SPEED_SET_BY_THE_LOCAL_RATE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_delay_for_the_rate_field_neighbour_referred_motion_does_not_propagate_a_reference_to_distant_clocks_does_at_a_speed_set_by_the_local_rate_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "onsite_term_survives_any_change_of_parameter": "B",
    "neighbour_term_does_not_survive": "B",
    "neighbour_forms_are_a_two_parameter_family": "C",
    "neighbours_only_law_has_a_front": "C",
    "reference_law_acts_at_once": "D",
    "finite_range_gives_a_branch_through_zero": "D",
    "uniform_mode_is_inert_under_the_onsite_term": "E",
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
ZERO = F(0)
ONE = F(1)


def solve(a, b):
    """Solve a x = b exactly; the matrix must be non-singular."""
    n = len(a)
    rows = [[F(c) for c in a[i]] + [F(b[i])] for i in range(n)]
    for col in range(n):
        piv = next((i for i in range(col, n) if rows[i][col] != 0), None)
        if piv is None:
            raise ValueError("singular")
        rows[col], rows[piv] = rows[piv], rows[col]
        pv = rows[col][col]
        rows[col] = [c / pv for c in rows[col]]
        for i in range(n):
            if i != col and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[col])]
    return [rows[i][n] for i in range(n)]


def rank(rows):
    rows = [[F(c) for c in r] for r in rows]
    rk = 0
    for col in range(len(rows[0])):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        rows[rk] = [c / rows[rk][col] for c in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def ring_inverse_laplacian(n, source):
    """Zero-mean v with  2 v_z - v_(z+1) - v_(z-1) = source_z - mean(source)  on a ring."""
    mean = sum(source, ZERO) / n
    a = [[ZERO] * n for _ in range(n)]
    for z in range(n):
        a[z][z] += 2
        a[z][(z + 1) % n] -= 1
        a[z][(z - 1) % n] -= 1
    a[0] = [ONE] * n                                        # gauge row: zero mean (the dropped equation is implied by the others)
    rhs = [s - mean for s in source]
    rhs[0] = ZERO
    return solve(a, rhs)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    n = 6
    phi = [F(3, 2), F(5, 4), F(2), F(7, 5), F(9, 8), F(4, 3)]
    w = [p * p for p in phi]
    vel = [F(1, 3), -F(2, 5), F(1, 7), F(3, 4), -F(1, 2), F(2, 9)]
    bonds = [(z, (z + 1) % n) for z in range(n)]
    qdot = [F(2, 3), F(1, 5), -F(3, 7), F(1, 2), F(5, 6), -F(1, 4)]

    def k_site(v, w):
        return sum((v[z] ** 2 / w[z] for z in range(n)), ZERO)

    def k_bond(v, ph):
        return sum(((v[a] - v[b]) ** 2 / (ph[a] * ph[b]) for a, b in bonds), ZERO)

    def k_wall(v, w):                                        # every rate against the clock at site 0 (a wall)
        return sum(((v[z] - v[0]) ** 2 / w[z] for z in range(1, n)), ZERO)

    def k_mean(v, w):                                        # every rate against the weighted mean: min over b of sum (v - b)^2 / w
        b = sum((v[z] / w[z] for z in range(n)), ZERO) / sum((1 / w[z] for z in range(n)), ZERO)
        return sum(((v[z] - b) ** 2 / w[z] for z in range(n)), ZERO)

    def bond_energy(ph):
        return sum(((ph[a] - ph[b]) ** 2 for a, b in bonds), ZERO)

    results = {}
    for label, fdd in (("general", F(2, 7)), ("rescaling", ZERO)):
        fd, root_fd = F(9, 4), F(3, 2)                        # f' = 9/4 at this instant
        v2 = [(x - fdd / fd) / fd for x in vel]
        w2 = [x / fd for x in w]
        ph2 = [p / root_fd for p in phi]
        results[label] = {
            "site": k_site(v2, w2) * fd == k_site(vel, w),
            "bond": k_bond(v2, ph2) * fd == k_bond(vel, phi),
            "wall": k_wall(v2, w2) * fd == k_wall(vel, w),
            "mean": k_mean(v2, w2) * fd == k_mean(vel, w),
            "energy": bond_energy(ph2) * fd == bond_energy(phi),
            "other field": k_site([x / fd for x in qdot], w2) * fd == k_site(qdot, w),          # a field that is not a rate: dq/dt -> (dq/dt)/f', no shift
        }
    want_general = {"site": False, "bond": True, "wall": True, "mean": True, "energy": True, "other field": True}
    if mut("onsite_term_survives_any_change_of_parameter"):
        want_general["site"] = True
    if mut("neighbour_term_does_not_survive"):
        want_general["bond"] = False
    checks.check("B1", results["general"] == want_general and all(results["rescaling"].values()), "T1: under a change of parameter with f' = 9/4 and f'' = 2/7 at the instant, K dt is unchanged for the neighbour-difference term, for the term that refers every rate to a wall clock and for the term that refers it to the weighted mean, the bond energy times dt is unchanged (weight one), and so is the ON-SITE kinetic term of a field that is not a rate (T5: its velocity has no shift); the on-site term of the rates, sum (du/dt)^2/w changes, and is unchanged only when f'' = 0: it needs a parameter that is more than a label")
    # quadratic forms: invariant under a common shift of the velocities iff M 1 = 0
    m_site = [[(1 / w[a] if a == b else ZERO) for b in range(n)] for a in range(n)]
    m_bond = [[ZERO] * n for _ in range(n)]
    for a, b in bonds:
        c = 1 / (phi[a] * phi[b])
        m_bond[a][a] += c; m_bond[b][b] += c; m_bond[a][b] -= c; m_bond[b][a] -= c
    tot = sum((1 / x for x in w), ZERO)
    m_mean = [[(1 / w[a] if a == b else ZERO) - (1 / w[a]) * (1 / w[b]) / tot for b in range(n)] for a in range(n)]
    row_sums = [[sum(r, ZERO) for r in m] for m in (m_site, m_bond, m_mean)]
    checks.check("B2", any(v != 0 for v in row_sums[0]) and all(v == 0 for v in row_sums[1]) and all(v == 0 for v in row_sums[2]), "T1: for a quadratic form (1/2) v^T M v the change of parameter shifts every velocity by the same amount, so invariance is M 1 = 0: true for the neighbour-difference form and for the form referred to the weighted mean (which is not of finite range: every pair of sites is coupled), false for the on-site form")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    # nearest-neighbour, covariant, symmetric forms with M 1 = 0: unknowns (c_0, c_(+x), c_(-x), c_(+y), c_(-y), c_(+z), c_(-z))
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    rows = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            parity = 1
            for i in range(3):
                for j in range(i + 1, 3):
                    if perm[i] > perm[j]:
                        parity = -parity
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue                                                                        # proper rotations only, as the Admissibility axiom names
            for e in dirs:
                ge = tuple(signs[i] * e[perm[i]] for i in range(3))
                r = [ZERO] * 7
                r[1 + dirs.index(ge)] += 1
                r[1 + dirs.index(e)] -= 1
                rows.append(r)
    rows.append([ONE] * 7)                                                                      # M 1 = 0: c_0 + sum of the six c_e = 0
    dim = 7 - rank(rows)
    if mut("neighbour_forms_are_a_two_parameter_family"):
        dim = 2
    checks.check("C1", dim == 1, f"T2: nearest-neighbour, covariant forms with M 1 = 0 are a {dim}-parameter family: multiples of the lattice operator of sum over bonds (v_x - v_y)^2.  The kinetic form and the weak-field bond energy are then the SAME operator, so their ratio, the squared frequency wbar^2/(gamma kappa), is the same for every mode: a flat band")
    # leapfrog on a ring of 16: Lam[(kappa/wbar) a + (wbar/gamma) u] = -P_0 s  =>  a = -omega0^2 u - (wbar/kappa) Lam^+ P_0 s
    n, h = 16, F(1, 4)
    omega_sq, drive = F(1), F(1)
    source = [ZERO] * n; source[0] = ONE
    profile = ring_inverse_laplacian(n, source)               # Lam^+ P_0 s: the static profile up to a constant factor
    u_prev = [ZERO] * n
    u = [-h * h / 2 * drive * p for p in profile]             # first step from rest
    proportional = True
    far_moves_at_once = u[n // 2] != 0
    for _ in range(6):
        ratios = {u[z] / profile[z] for z in range(n) if profile[z] != 0}
        proportional = proportional and len(ratios) == 1
        acc = [-omega_sq * u[z] - drive * profile[z] for z in range(n)]
        u_prev, u = u, [2 * u[z] - u_prev[z] + h * h * acc[z] for z in range(n)]
    if mut("neighbours_only_law_has_a_front"):
        far_moves_at_once = not far_moves_at_once
    checks.check("C2", proportional and far_moves_at_once, "T2: a source switched on at one site of a ring of 16 under the neighbours-only law: after the FIRST step the field at the opposite site is already non-zero, and at every step the field is the static profile times one number: the whole profile appears at once and swings in place; nothing travels")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    # reference-clock law on a segment with walls: u'' = c^2 wbar^2 (u_(z+1) + u_(z-1) - 2 u_z) - s, leapfrog with c wbar h = 1/2
    n, mid, lam_sq = 25, 12, F(1, 4)
    u_prev = [ZERO] * n
    u = [ZERO] * n
    cone = True
    for step in range(1, 9):
        new = [ZERO] * n
        for z in range(1, n - 1):
            new[z] = 2 * u[z] - u_prev[z] + lam_sq * (u[z + 1] + u[z - 1] - 2 * u[z]) - (F(1, 16) if z == mid else ZERO)
        u_prev, u = u, new
        reach = step - 1                                     # the source acts at step 1 on its own site; each further step reaches one more site
        inside = all(u[z] != 0 for z in range(n) if abs(z - mid) <= reach and 0 < z < n - 1)
        outside = all(u[z] == 0 for z in range(n) if abs(z - mid) > reach)
        if mut("reference_law_acts_at_once"):
            outside = any(u[z] != 0 for z in range(n) if abs(z - mid) > reach)
        cone = cone and inside and outside
    checks.check("D1", cone, "T3: under the law referred to the wall clocks a source switched on at the middle of a segment reaches exactly one more site at every step (exact zeros beyond, non-zero values within, for eight steps): a front.  With the step fixed in local ticks (c wbar h = 1/2) the recursion does not contain the ambient rate: the front moves c sites per local tick")
    # symbols on a ring of 12: E = 2 - 2 cos k takes the rational values 0, 1, 2, 3, 4 at k = 0, pi/3, pi/2, 2pi/3, pi
    e_values = [F(1), F(2), F(3), F(4)]
    wbar, gamma, kappa1, kappa2, c = F(3, 2), F(3, 5), F(2), F(1, 3), F(1)
    near = {wbar * e / gamma / (kappa1 * e / wbar) for e in e_values}
    longer = [wbar * e / gamma / ((kappa1 * e + kappa2 * e * e) / wbar) for e in e_values]
    reference = [wbar * e / gamma * (gamma * c * c * wbar) for e in e_values]
    gap = min(longer)
    floor = wbar * wbar / (gamma * (kappa1 + 4 * kappa2))
    ok = len(near) == 1 and longer == sorted(longer, reverse=True) and gap == floor and gap > 0 and [r / e for r, e in zip(reference, e_values)] == [c * c * wbar * wbar] * 4
    if mut("finite_range_gives_a_branch_through_zero"):
        ok = ok and gap == 0
    checks.check("D2", ok, f"T2/T3: squared frequencies on a ring of 12 (E = 1, 2, 3, 4): neighbours only: {sorted(near)[0]} for every mode; a kinetic form of longer finite range, kappa_1 Lam + kappa_2 Lam^2: {', '.join(str(v) for v in longer)}, largest at long wavelength and never below wbar^2/(gamma (kappa_1 + 4 kappa_2)) = {floor}: a gap, no branch through zero; referred to a clock of the system: c^2 wbar^2 E, which goes to zero with E: waves at c wbar")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    psi, dpsi, ddpsi = F(7, 5), -F(2, 9), F(3, 11)
    w = 1 / (psi * psi)
    du = -2 * dpsi / psi
    ddu = -2 * ddpsi / psi + 2 * dpsi * dpsi / (psi * psi)
    gamma, c = F(3, 5), F(5, 4)
    same_kinetic = du * du / w / (2 * gamma * c * c) == 2 / (gamma * c * c) * dpsi * dpsi
    same_accel = ddu - du * du / 2 == -2 * ddpsi / psi
    # closed lattice, uniform mode under the on-site term: (N/(gamma c^2 w)) (u'' - u'^2/2) = -(static part of the ledger)
    n_sites, static_part = 64, F(17, 3)
    accel = gamma * c * c * static_part / (2 * n_sites * psi)
    balance = n_sites / (gamma * c * c * w) * (-2 * accel / psi) == -static_part
    moves = accel > 0
    if mut("uniform_mode_is_inert_under_the_onsite_term"):
        moves = accel == 0
    checks.check("E1", same_kinetic and same_accel and balance and moves, f"T4: with psi = w^(-1/2): (1/(2 gamma c^2)) (du/dt)^2/w = (2/(gamma c^2)) (dpsi/dt)^2 and d^2u/dt^2 - (du/dt)^2/2 = -2 (d^2psi/dt^2)/psi; on a closed lattice the uniform mode under the on-site term obeys d^2psi_0/dt^2 = gamma c^2 (static part of the ledger)/(2 N psi_0) = {accel} > 0 here: every clock slows together against the parameter, which only a master parameter could notice; under a form with M 1 = 0 the uniform mode has no momentum at all (B2)")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger; it reports which motions of the rate field survive an arbitrary change of the time parameter and whether they carry a delay; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Lagrange", "Mach", "Barbour", "Bertotti", "Jacobi", "Coulomb", "Maxwell", "Noether", "Courant", "Verlet", "Arnowitt", "Deser", "Misner")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Mach)", 1)
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
    "per_element: executed — the change of parameter applied to six rational rates and velocities: four kinetic terms and the bond energy, with and without f''; the row sums of three kinetic matrices",
    "per_site: executed — a source switched on at one site: the neighbours-only law on a ring of 16 (the opposite site after one step; proportionality to the static profile for six steps) and the wall-referred law on a segment of 25 (exact zeros beyond the front for eight steps)",
    "per_mode: executed — squared frequencies on a ring of 12 at the four rational values of the lattice symbol, for the neighbours-only form, a form of longer finite range and a form referred to a clock of the system",
    "per_block: executed — the one-parameter family of nearest-neighbour covariant forms with M 1 = 0 (rank of the covariance and row-sum conditions); the uniform mode's equation under the on-site term",
    "lattice_wide: T1 holds for every Lagrangian that depends on the first time derivatives of the rates; T2 for every nearest-neighbour covariant quadratic kinetic form at weak field, and in the form 'no branch through zero' for every finite range; T3 and T4 at weak field; the full non-linear motion referred to the wall clocks is executed only; which reference, if any, the framework would state is not decided; fields that are not rates are not treated",
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
    print("scope: a delay for the rate field — with no master clock at any instant a kinetic term may see only differences of rates between sites; referred to neighbours it is the same operator as the bond energy and nothing propagates; referred to a clock of the system it gives a front at c sites per local tick; the on-site term needs a master parameter and moves the uniform mode")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
