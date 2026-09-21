#!/usr/bin/env python3
"""Exact checks: the strong field of block 55's simplest clock law, for bodies at rest (supplied clauses on Z^3; not adopted).

SETTING (blocks 53-55, open PRs; supplied): rates w_x = phi_x^2; the ledger <H_w> + F with the simplest bond energy of weight one,
F = (2/gamma) sum over bonds (phi_x - phi_y)^2; a body at rest at x with bare rest energy m_x has the energy density e_x = m_x w_x (block 55);
a box whose walls are held at the ambient rate phi = 1 (the unit of rate), the rates inside free.
T1 (linear): the law (12/gamma) phi_x (phi_x - average of phi) = -m_x phi_x^2 is, after division by phi_x > 0, the LINEAR problem
   ((1 - A) + (gamma/12) M) phi = 0 inside, phi = 1 on the walls: one solution, 0 < phi <= 1, decreasing in every m.
   Linearity does not need rest: for ANY fixed amplitude e_x = phi_x (K phi)_x with K_xy = Re chi_x^dagger H_xy chi_y independent of the rates,
   so the law is ((12/gamma)(1 - A) + K) phi = 0; rest gives K = diag(m) >= 0 and with it the bounds.
T2 (ledger): the ledger of a static arrangement is sum_i m_i phi_i exactly (not the sum of the bare energies, not the sum of the energies
   m_i phi_i^2 the bodies have in the field), and it equals the surface term sum over wall sites of dF/du_x: what the outside sees is the ledger.
T3 (saturation): one body: phi_0 = 1/(1 + x), x = (gamma/12) g_0 m, g_0 the potential of (1 - A) at the body; its ledger m/(1 + x) stays below
   12/(gamma g_0) however large m; the energy it has in the field, m/(1 + x)^2, is largest at x = 1; its clock stops only in the limit.
   Any arrangement on a set B: the ledger increases with every m and stays below (12/gamma) Cap(B), Cap(B) = 1^T G_B^-1 1.
T4 (two bodies): closed form; the ledger of a pair is less than the sum of the ledgers of its members alone, by more the closer they are.
T5 (what picks the bond energy; a supplied principle): block 54's clause makes the amplitudes' energy bilinear in the root rates with
   rate-independent coefficients.  If the field's own energy is timed the same way, F = sum phi_x J_xy phi_y, then nearest-neighbour range,
   covariance and 'uniform rates solve the empty-space law' leave one family, c sum over bonds (phi_x - phi_y)^2: the simplest bond energy.
   The second bond energy of the refuting pass is not of this form (it fails the parallelogram identity of quadratic forms).
Exact arithmetic only (integers and Fractions); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_strong_field_exactly_bodies_at_rest_make_the_clock_law_linear_in_the_root_of_the_rate_the_ledger_is_a_surface_term_bounded_by_a_capacity_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "body_energy_not_timed_by_its_clock": "B",
    "raising_an_energy_raises_the_rates": "B",
    "amplitude_energy_not_timed_by_its_clock": "B",
    "ledger_is_the_sum_of_energies_in_the_field": "C",
    "outside_sees_the_bare_energies": "C",
    "ledger_grows_without_bound": "D",
    "energy_in_the_field_is_monotone": "D",
    "capacity_bound_is_the_single_site_bound": "D",
    "pair_ledger_exceeds_the_members": "E",
    "every_weight_one_energy_is_bilinear": "E",
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
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SIDE = 7                                                     # sites 0..6; walls at 0 and 6; 125 interior sites
INTERIOR = [s for s in product(range(1, SIDE - 1), repeat=3)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
GAMMA = F(3, 5)


def about(v) -> str:
    """A rational to three decimal places, by integer rounding (descriptive only; every comparison in this runner is exact)."""
    k = round(v * 1000)
    sign = "-" if k < 0 else ""
    k = abs(k)
    return f"{sign}{k // 1000}.{k % 1000:03d}"


def solve_multi(a, rhs_list):
    """Solve a x = b exactly for several right-hand sides at once; the matrix must be non-singular."""
    n = len(a)
    k = len(rhs_list)
    rows = [[F(c) for c in a[i]] + [F(r[i]) for r in rhs_list] for i in range(n)]
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
    return [[rows[i][n + j] for i in range(n)] for j in range(k)]


def operator(masses):
    """Matrix of (1 - A) + (gamma/12) M on the interior, and the right-hand side from walls held at phi = 1."""
    n = len(INTERIOR)
    a = [[ZERO] * n for _ in range(n)]
    b = [ZERO] * n
    for s in INTERIOR:
        i = INDEX[s]
        a[i][i] = ONE + GAMMA / 12 * masses.get(s, ZERO)
        for e in E6:
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if t in INDEX:
                a[i][INDEX[t]] -= F(1, 6)
            else:
                b[i] += F(1, 6)
    return a, b


def rates(masses):
    a, b = operator(masses)
    sol = solve_multi(a, [b])[0]
    return {s: sol[INDEX[s]] for s in INTERIOR}


def value(phi, t):
    return phi[t] if t in phi else ONE                       # walls at the ambient rate


def ledger_parts(phi, masses):
    matter = sum((m * phi[s] ** 2 for s, m in masses.items()), ZERO)
    bonds = ZERO
    for s in product(range(SIDE), repeat=3):
        for e in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if max(t) >= SIDE:
                continue
            bonds += (value(phi, s) - value(phi, t)) ** 2
    return matter, 2 / GAMMA * bonds


def wall_term(phi):
    """sum over wall sites of dF/du_x = (2/gamma) phi_x sum_y (phi_x - phi_y), phi = 1 on the walls."""
    tot = ZERO
    for s in product(range(SIDE), repeat=3):
        if s in INDEX:
            continue
        for e in E6:
            t = (s[0] + e[0], s[1] + e[1], s[2] + e[2])
            if t in INDEX:
                tot += ONE - phi[t]
    return 2 / GAMMA * tot


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
BODIES = {(2, 3, 3): F(2), (4, 3, 2): F(5), (3, 5, 4): F(3, 2)}


def family_b(checks: Checks):
    phi = rates(BODIES)
    ok_law = True
    for s in INTERIOR:
        avg = sum((value(phi, (s[0] + e[0], s[1] + e[1], s[2] + e[2])) for e in E6), ZERO) / 6
        m = BODIES.get(s, ZERO)
        energy = m * phi[s] ** 2 if not mut("body_energy_not_timed_by_its_clock") else m
        ok_law = ok_law and 12 / GAMMA * phi[s] * (phi[s] - avg) == -energy
    inside = all(ZERO < v < ONE for v in phi.values())
    checks.check("B1", ok_law and inside, f"T1: three bodies at rest (bare energies 2, 5, 3/2; gamma = 3/5) in a 7x7x7 box with walls at the ambient rate: the solution of the LINEAR problem ((1 - A) + (gamma/12) M) phi = 0 satisfies the clock law (12/gamma) phi_x (phi_x - average) = -m_x phi_x^2 at all 125 interior sites, with 0 < phi < 1 everywhere (lowest: about {about(min(phi.values()))}, at the heaviest body)")
    raised = dict(BODIES)
    raised[(2, 3, 3)] = F(3)
    phi2 = rates(raised)
    if mut("raising_an_energy_raises_the_rates"):
        monotone = all(phi2[s] > phi[s] for s in INTERIOR)
    else:
        monotone = all(phi2[s] < phi[s] for s in INTERIOR)
    checks.check("B2", monotone, "T1: raising one body's bare energy from 2 to 3 lowers phi at every one of the 125 interior sites: more energy anywhere slows every clock, and the (non-singular) linear problem has one solution")
    # B3: linearity does not need rest.  A real amplitude spread over interior sites, a real symmetric nearest-neighbour generator
    # (on-site energy 2, hopping -1/2): e_x[phi] = chi_x (phi H phi chi)_x = phi_x (K phi)_x with K_xy = chi_x H_xy chi_y.
    support = {(2, 2, 2): F(1, 2), (3, 2, 2): F(2, 3), (3, 3, 2): -F(1, 3), (3, 3, 3): F(3, 4), (4, 3, 3): F(1, 5), (2, 3, 3): F(1, 4)}
    kmat = {}
    for x, cx in support.items():
        kmat[(x, x)] = 2 * cx * cx
        for e in E6:
            y = (x[0] + e[0], x[1] + e[1], x[2] + e[2])
            if y in support:
                kmat[(x, y)] = -F(1, 2) * cx * support[y]
    n = len(INTERIOR)
    a_mat, b_vec = operator({})
    for (x, y), v in kmat.items():
        a_mat[INDEX[x]][INDEX[y]] += GAMMA / 12 * v
    sol = solve_multi(a_mat, [b_vec])[0]
    phi_amp = {s: sol[INDEX[s]] for s in INTERIOR}
    ok_amp = all(v > 0 for v in phi_amp.values())
    for s in INTERIOR:
        avg = sum((value(phi_amp, (s[0] + e[0], s[1] + e[1], s[2] + e[2])) for e in E6), ZERO) / 6
        clocked = phi_amp if not mut("amplitude_energy_not_timed_by_its_clock") else {t: ONE for t in INTERIOR}
        energy = ZERO
        if s in support:
            energy = clocked[s] * sum((kmat[(s, y)] * clocked[y] for y in support if (s, y) in kmat), ZERO)
        ok_amp = ok_amp and 12 / GAMMA * phi_amp[s] * (phi_amp[s] - avg) == -energy
    off_diagonal = sum(1 for (x, y) in kmat if x != y)
    both_signs = any(v > 0 for (x, y), v in kmat.items() if x != y) and any(v < 0 for (x, y), v in kmat.items() if x != y)
    checks.check("B3", ok_amp and off_diagonal > 0 and both_signs, f"T1: linearity does not need rest: for an amplitude spread over six sites with a hopping generator, e_x = phi_x (K phi)_x with K independent of the rates ({off_diagonal} bond entries, of both signs), and the solution of the linear problem ((12/gamma)(1 - A) + K) phi = 0 satisfies the clock law with the amplitude's own energy density at all 125 interior sites; what rest adds is K = diag(m) >= 0, and with it uniqueness, the bounds and monotonicity")
    return phi


# ============================================================================================ family C
def family_c(checks: Checks, phi) -> None:
    matter, field = ledger_parts(phi, BODIES)
    ledger = sum((m * phi[s] for s, m in BODIES.items()), ZERO)
    want = ledger if not mut("ledger_is_the_sum_of_energies_in_the_field") else matter
    checks.check("C1", matter + field == want, f"T2: energies in the field sum m phi^2 (about {about(matter)}) plus the field energy (2/gamma) sum (phi_x - phi_y)^2 (about {about(field)}) equal sum m phi (about {about(ledger)}) exactly: less than the bare energies' sum {sum(BODIES.values())} by a defect of about {about(sum(BODIES.values()) - ledger)}")
    seen = wall_term(phi)
    want = ledger if not mut("outside_sees_the_bare_energies") else sum(BODIES.values(), ZERO)
    checks.check("C2", seen == want, "T2: the sum over wall sites of dF/du_x equals the ledger exactly: the ledger is a surface term, so what the rates at the walls (and anything outside) respond to is the ledger of the arrangement, not the bare energies and not the energies in the field")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    centre = (3, 3, 3)
    a, _ = operator({})
    cross = [centre] + [(3 + e[0], 3 + e[1], 3 + e[2]) for e in E6]
    rhs = []
    for s in cross:
        r = [ZERO] * len(INTERIOR)
        r[INDEX[s]] = ONE
        rhs.append(r)
    sols = solve_multi(a, rhs)
    g = [[sols[j][INDEX[cross[i]]] for j in range(7)] for i in range(7)]          # potential of (1 - A) with grounded walls, on the cross
    g0 = g[0][0]
    bound = 12 / (GAMMA * g0)
    ok = True
    ledgers = []
    for m in (F(1), F(20), F(10) ** 8):
        phi = rates({centre: m})
        x = GAMMA / 12 * g0 * m
        ok = ok and phi[centre] == 1 / (1 + x)
        ledgers.append(m * phi[centre])
    below = all(v < bound for v in ledgers) if not mut("ledger_grows_without_bound") else ledgers[-1] > bound
    checks.check("D1", ok and below and ledgers[0] < ledgers[1] < ledgers[2] and bound - ledgers[2] < bound / 10 ** 5, f"T3: one body at the centre: phi_0 = 1/(1 + x), x = (gamma/12) g_0 m, with the box's g_0 = {g0}; its ledger m/(1 + x) rises with m and stays below 12/(gamma g_0) = {bound} (within a part in 10^5 of it at m = 10^8): a site's energy seen from outside is bounded however much is put there")
    field_energy = []
    for x in (F(1, 2), F(1), F(2)):
        m = 12 * x / (GAMMA * g0)
        phi = rates({centre: m})
        field_energy.append(m * phi[centre] ** 2)
    peak = field_energy[1] > field_energy[0] and field_energy[1] > field_energy[2]
    if mut("energy_in_the_field_is_monotone"):
        peak = field_energy[0] < field_energy[1] < field_energy[2]
    checks.check("D2", peak and field_energy[1] == 3 / (GAMMA * g0), f"T3: the energy the body has in the field, m phi_0^2 = m/(1 + x)^2, is {field_energy[0]}, {field_energy[1]}, {field_energy[2]} at x = 1/2, 1, 2: largest at x = 1, where it is 3/(gamma g_0); beyond that, adding bare energy lowers it, the body's clock running at 1/(1 + x)^2 of the ambient rate")
    # capacity of the seven-site cross
    ones = solve_multi(g, [[ONE] * 7])[0]
    cap = sum(ones, ZERO)
    if mut("capacity_bound_is_the_single_site_bound"):
        cap = 1 / g0
    vals = []
    for m in (F(1), F(100), F(10) ** 8):
        masses = {s: m for s in cross}
        phi = rates(masses)
        vals.append(sum((m * phi[s] for s in cross), ZERO))
    limit = 12 / GAMMA * cap
    checks.check("D3", vals[0] < vals[1] < vals[2] < limit and limit - vals[2] < limit / 10 ** 6, f"T3: seven bodies on a site and its six neighbours: the ledger rises with the bare energies (about {about(vals[0])} at 1 each, {about(vals[1])} at 100 each, and within a part in 10^6 of the limit at 10^8 each) and stays below (12/gamma) Cap = {limit}, Cap = 1^T G^-1 1 = {cap} the capacity of the set for the operator 1 - A: a region's energy seen from outside is bounded by its capacity")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    a, _ = operator({})
    m1, m2 = F(4), F(7)
    defects = []
    ok_closed = True
    for s1, s2 in (((1, 3, 3), (5, 3, 3)), ((2, 3, 3), (4, 3, 3)), ((3, 3, 3), (4, 3, 3))):
        rhs = []
        for s in (s1, s2):
            r = [ZERO] * len(INTERIOR)
            r[INDEX[s]] = ONE
            rhs.append(r)
        sols = solve_multi(a, rhs)
        ga, gb, gc = sols[0][INDEX[s1]], sols[1][INDEX[s2]], sols[0][INDEX[s2]]
        d1, d2 = GAMMA / 12 * m1, GAMMA / 12 * m2
        det = (1 + d1 * ga) * (1 + d2 * gb) - d1 * d2 * gc * gc
        p1, p2 = (1 + d2 * gb - d2 * gc) / det, (1 + d1 * ga - d1 * gc) / det
        phi = rates({s1: m1, s2: m2})
        ok_closed = ok_closed and phi[s1] == p1 and phi[s2] == p2
        alone = m1 / (1 + d1 * ga) + m2 / (1 + d2 * gb)
        defects.append(alone - (m1 * phi[s1] + m2 * phi[s2]))
    order = ZERO < defects[0] < defects[1] < defects[2]
    if mut("pair_ledger_exceeds_the_members"):
        order = defects[0] < ZERO
    checks.check("E1", ok_closed and order, f"T4: two bodies (bare energies 4 and 7): phi at each equals the closed form from the 2x2 problem (1 + G D) phi = 1; the pair's ledger is below the sum of the members' ledgers alone by about {about(defects[0])}, {about(defects[1])}, {about(defects[2])} at separations 4, 2, 1: the defect is positive and grows as they approach, so the static ledger is one function whose slope pulls each towards the other, at any field strength")

    # T5: nearest-neighbour energies bilinear in the root rates, F = alpha sum phi_x^2 + sum over directions beta_e sum phi_x phi_(x+e)
    # unknowns (alpha, beta_1, beta_2, beta_3); covariance: beta_1 = beta_2 = beta_3; uniform rates solve the empty-space law: 2 alpha + 2 sum beta_e = 0
    rows = [[ZERO, ONE, -ONE, ZERO], [ZERO, ZERO, ONE, -ONE], [F(2), F(2), F(2), F(2)]]
    # rank by elimination
    mat = [r[:] for r in rows]
    rk = 0
    for col in range(4):
        piv = next((i for i in range(rk, len(mat)) if mat[i][col] != 0), None)
        if piv is None:
            continue
        mat[rk], mat[piv] = mat[piv], mat[rk]
        mat[rk] = [v / mat[rk][col] for v in mat[rk]]
        for i in range(len(mat)):
            if i != rk and mat[i][col] != 0:
                fac = mat[i][col]
                mat[i] = [x - fac * y for x, y in zip(mat[i], mat[rk])]
        rk += 1
    side = 3
    sites = list(product(range(side), repeat=3))
    bonds = [(x, tuple((x[i] + (1 if i == j else 0)) % side for i in range(3))) for x in sites for j in range(3)]
    pa = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in sites}
    pb = {x: F(1, 5) + F((2 * x[0] + x[1] + 4 * x[2]) % 7, 9) for x in sites}

    def f_one(p):
        return sum(((p[x] - p[y]) ** 2 for x, y in bonds), ZERO)

    def f_two(p):
        return sum(((p[x] ** 2 - p[y] ** 2) ** 2 / (p[x] ** 2 + p[y] ** 2) for x, y in bonds), ZERO)

    beta = F(-7, 3)
    family = -3 * beta * sum((pa[x] ** 2 for x in sites), ZERO) + beta * sum((pa[x] * pa[y] for x, y in bonds), ZERO)
    plus = {x: pa[x] + pb[x] for x in sites}
    minus = {x: pa[x] - pb[x] for x in sites}

    def parallelogram(fn):
        return fn(plus) + fn(minus) == 2 * fn(pa) + 2 * fn(pb)

    second_is_bilinear = parallelogram(f_two)
    if mut("every_weight_one_energy_is_bilinear"):
        second_is_bilinear = not second_is_bilinear
    checks.check("E2", rk == 3 and family == -beta / 2 * f_one(pa) and parallelogram(f_one) and not second_is_bilinear and all(v > 0 for v in minus.values()), "T5: nearest-neighbour energies bilinear in the root rates, covariant, with uniform rates solving the empty-space law, form a one-dimensional family (rank 3 of 4 conditions on (alpha, beta_1, beta_2, beta_3)), and alpha = -3 beta makes it -(beta/2) sum over bonds (phi_x - phi_y)^2 (checked on the 3x3x3 torus): the simplest bond energy; it satisfies the parallelogram identity of quadratic forms and the refuting pass's second bond energy does not: if the local clock times the field's own energy as it times an amplitude, the bond energy is not a choice")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a kept ledger, with the simplest bond energy of weight one; it reports the exact static law for bodies at rest; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "event horizon", "horizon",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Hellmann", "Feynman", "Dirichlet", "Watson", "Lowner", "Stieltjes", "Kelvin", "Buchdahl", "Abraham")
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
    "per_element: executed — the clock law at each of the 125 interior sites of a 7x7x7 box for three bodies; the sign of the change of phi at each site when one bare energy is raised",
    "per_site: executed — one body at the centre for three bare energies against 1/(1 + x); the energy in the field at x = 1/2, 1, 2",
    "per_mode: executed — the capacity of the seven-site cross from the exact 7x7 potential matrix, and the ledgers of seven bodies for three bare energies",
    "per_block: executed — the ledger identity and the surface term for three bodies; the closed form and the defect for a pair at separations 4, 2, 1; the clock law for an amplitude spread over six sites; the one-dimensional family of bilinear nearest-neighbour energies and the parallelogram identity on the 3x3x3 torus",
    "lattice_wide: T1 to T4 hold for any finite set of bodies at rest in any box with walls at the ambient rate, for the simplest bond energy of weight one; that the ledger is a surface term holds for every bond energy of weight one; for other bond energies the static law is not linear and the strong-field statements are not established; that the bond energy is bilinear in the root rates is a supplied principle (T5), not a consequence of blocks 53 to 55; bodies at rest with a rest energy are supplied (one walker has none); motion, delay and the number gamma are not addressed",
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
    phi = family_b(checks)
    family_c(checks, phi)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: the strong field of the simplest clock law — for bodies at rest the law is linear in phi = sqrt(w); the ledger is sum m phi and is a surface term; a body's ledger saturates and its clock stops only in the limit; a region's ledger is bounded by its capacity; a pair's ledger has a defect that grows as the bodies approach")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
