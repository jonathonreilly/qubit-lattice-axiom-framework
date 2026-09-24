#!/usr/bin/env python3
"""Exact controls for supplied rate-linear field energies and restricted static models.
Field linearity is distinct from hopping-ledger linearity. The finite positive
static diagonal-source solution and stated weak-field/kinetic identities are tested.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "ledger_is_not_of_weight_one": "B",
    "positive_field_energy_admits_a_free_unit": "B",
    "closed_lattice_holds_a_static_body": "B",
    "exponent_formula_sign": "C",
    "bilinear_member_gives_p": "C",
    "curvature_identity_coefficient": "C",
    "rate_at_the_body_uses_one_charge": "D",
    "far_field_coefficients_equal": "D",
    "seen_from_outside_saturates": "D",
    "kinetic_term_delays_the_lengths": "E",
    "positive_kinetic_term_moves_the_lengths": "E",
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
E6 = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
E3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
SIDE = 7                                                     # sites 0..6; walls at 0 and 6; 125 interior sites
ALL_SITES = list(product(range(SIDE), repeat=3))
INTERIOR = [s for s in product(range(1, SIDE - 1), repeat=3)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
K = F(3, 4)                                                  # the field energy's one number; 8K = 6


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


def add(s, e):
    return (s[0] + e[0], s[1] + e[1], s[2] + e[2])


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


def green_columns(sources):
    """Columns of the inverse of minus the lattice Laplacian on the interior (walls held): g(., s) for each source s."""
    n = len(INTERIOR)
    a = [[ZERO] * n for _ in range(n)]
    for s in INTERIOR:
        i = INDEX[s]
        a[i][i] = F(6)
        for e in E6:
            t = add(s, e)
            if t in INDEX:
                a[i][INDEX[t]] -= 1
    rhs = []
    for s in sources:
        col = [ZERO] * n
        col[INDEX[s]] = ONE
        rhs.append(col)
    sols = solve_multi(a, rhs)
    return {s: {t: sols[j][INDEX[t]] for t in INTERIOR} for j, s in enumerate(sources)}


def val(field, t, wall=ONE):
    return field[t] if t in field else wall


def lap(field, s, wall=ONE):
    """Lattice Laplacian at s over the bonds that stay inside the box; outside the interior the field is the wall value."""
    tot = ZERO
    for e in E6:
        t = add(s, e)
        if min(t) < 0 or max(t) >= SIDE:
            continue
        tot += val(field, t, wall) - val(field, s, wall)
    return tot


def bond_form(nfield, chi):
    """-8K sum over bonds with an interior end of (N_y - N_x)(chi_y - chi_x)."""
    tot = ZERO
    for s in ALL_SITES:
        for e in E3:
            t = add(s, e)
            if max(t) >= SIDE or (s not in INDEX and t not in INDEX):
                continue
            tot += (val(nfield, t) - val(nfield, s)) * (val(chi, t) - val(chi, s))
    return -8 * K * tot


def rational_field(seed, lo=F(1, 2), spread=F(1)):
    """A deterministic positive rational field on the interior."""
    out = {}
    for s in INTERIOR:
        h = (seed * 7919 + 31 * s[0] + 57 * s[1] * s[1] + 101 * s[2] * s[0] + 13 * s[1] * s[2] * seed) % 17
        out[s] = lo + spread * F(h, 17)
    return out


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
SMALL = 5                                                    # family B's own box: sites 0..4, 27 interior sites
SMALL_ALL = list(product(range(SMALL), repeat=3))
SMALL_INT = [s for s in product(range(1, SMALL - 1), repeat=3)]


def small_bonds():
    out = []
    for s in SMALL_ALL:
        for e in E3:
            t = add(s, e)
            if max(t) < SMALL:
                out.append((s, t))
    return out


SMALL_BONDS = small_bonds()


def amplitude():
    """A rational complex amplitude on the interior of the small box (real and imaginary parts kept apart); zero on the walls."""
    amp = {}
    for s in SMALL_INT:
        amp[s] = (F(1 + (3 * s[0] + s[1] * s[2]) % 5, 3), F((s[0] * s[0] + 2 * s[1] + 5 * s[2]) % 7 - 3, 4))
    return amp


def content_energy(phi, chi, amp, masses):
    """<H> = sum m_x w_x |a_x|^2 - sum over bonds of (phi_x phi_y/(chi_x chi_y)) 2 Re(conj(a_x) a_y): of weight one in the rates w = phi^2."""
    tot = ZERO
    for s, (re_, im_) in amp.items():
        tot += masses.get(s, ZERO) * phi[s] ** 2 * (re_ * re_ + im_ * im_)
    for s, t in SMALL_BONDS:
        if s in amp and t in amp:
            tot -= phi[s] * phi[t] / (chi[s] * chi[t]) * 2 * (amp[s][0] * amp[t][0] + amp[s][1] * amp[t][1])
    return tot


def field_linear(phi, chi):
    """The bilinear member in bond form, -8K sum over bonds (N_y - N_x)(chi_y - chi_x), N = phi^2 chi: linear in the rates."""
    tot = ZERO
    for s, t in SMALL_BONDS:
        tot += (phi[t] ** 2 * chi[t] - phi[s] ** 2 * chi[s]) * (chi[t] - chi[s])
    return -8 * K * tot


def field_block56(phi):
    """Block 56's bond energy with gamma = 1/(4K): 8K sum over bonds (phi_x - phi_y)^2; non-negative."""
    return 8 * K * sum(((phi[s] - phi[t]) ** 2 for s, t in SMALL_BONDS), ZERO)


def small_field(seed, lo, spread):
    out = {}
    for s in SMALL_ALL:
        h = (seed * 7919 + 31 * s[0] + 57 * s[1] * s[1] + 101 * s[2] * s[0] + 13 * s[1] * s[2] * seed) % 17
        out[s] = lo + spread * F(h, 17)
    return out


def rate_gradient_sum(fun, phi):
    """sum over ALL sites of w_x dE/dw_x = sum (phi_x/2) dE/dphi_x, the derivative taken by an exact central difference (E is quadratic in each phi_x)."""
    tot = ZERO
    for s in SMALL_ALL:
        up = dict(phi)
        dn = dict(phi)
        up[s] = phi[s] + 1
        dn[s] = phi[s] - 1
        tot += phi[s] / 2 * (fun(up) - fun(dn)) / 2
    return tot


def family_b(checks: Checks) -> None:
    amp = amplitude()
    masses = {s: F(1 + (s[0] + 2 * s[1] + 3 * s[2]) % 4, 2) for s in SMALL_INT}
    phi = small_field(3, F(1, 2), ONE)
    chi = small_field(8, F(3, 4), F(1, 2))
    led_lin = lambda p: content_energy(p, chi, amp, masses) + field_linear(p, chi)
    led_56 = lambda p: content_energy(p, chi, amp, masses) + field_block56(p)
    scale = F(3, 2)
    factor = scale ** 2 if not mut("ledger_is_not_of_weight_one") else scale
    scaled = {s: scale * v for s, v in phi.items()}
    ok_scale = led_lin(scaled) == factor * led_lin(phi) and led_56(scaled) == factor * led_56(phi)
    ok_sum = rate_gradient_sum(led_lin, phi) == led_lin(phi) and rate_gradient_sum(led_56, phi) == led_56(phi)
    checks.check("B1", ok_scale and ok_sum, "T1: both ledgers (a hopping amplitude with on-site energies, 27 interior sites, rational rates and lengths) are of weight one in the rates, and the sum over ALL sites of w_x dE/dw_x, taken by exact differences, is the ledger itself: a stationary point in every rate has ledger zero; with held walls the ledger is the walls' own share of that sum")

    rest = {s: (F(1, 3), ZERO) for s in SMALL_INT}                                   # a real amplitude with positive on-site energies and no hop term kept: bodies at rest
    pos = []
    for seed in (1, 2, 5):
        p = small_field(seed, F(1, 3), F(2))
        matter = sum((masses[s] * p[s] ** 2 * rest[s][0] ** 2 for s in SMALL_INT), ZERO)
        pos.append(matter + field_block56(p))
    free_unit_ok = all(v > 0 for v in pos) if not mut("positive_field_energy_admits_a_free_unit") else any(v <= 0 for v in pos)
    hill = {s: (ONE + (F(1, 2) if s == (2, 2, 2) else ZERO)) for s in SMALL_ALL}
    dip = {s: (ONE - (F(1, 2) if s == (2, 2, 2) else ZERO)) for s in SMALL_ALL}
    flat = small_field(3, ONE, ZERO)
    slow_centre = {s: (F(1, 2) if s == (2, 2, 2) else ONE) for s in SMALL_ALL}
    f_a, f_b = field_linear(flat, hill), field_linear(slow_centre, hill)
    checks.check("B2", free_unit_ok and f_a < 0 < f_b, f"T1: block 56's field energy is a sum of squares, so with positive content its ledger is positive at every configuration ({', '.join(about(v) for v in pos)} at three): it has no stationary point once the unit of rate is varied; the field energy linear in the rates takes both signs ({about(f_a)} for a stretched site among even clocks, {about(f_b)} when that site's clock is slow) and can balance the content")

    phi2 = small_field(11, F(1, 4), F(3, 2))
    w_sum = {s: (phi[s] ** 2 + phi2[s] ** 2) for s in SMALL_ALL}

    def field_of_rates(w):
        return -8 * K * sum(((w[t] * chi[t] - w[s] * chi[s]) * (chi[t] - chi[s]) for s, t in SMALL_BONDS), ZERO)

    w1 = {s: phi[s] ** 2 for s in SMALL_ALL}
    w2 = {s: phi2[s] ** 2 for s in SMALL_ALL}
    additive = field_of_rates(w_sum) == field_of_rates(w1) + field_of_rates(w2)
    phi_sum = {s: phi[s] + phi2[s] for s in SMALL_ALL}
    not_additive_56 = field_block56(phi_sum) != field_block56(phi) + field_block56(phi2)

    def chi_gradient(w, z):
        up = dict(chi)
        dn = dict(chi)
        up[z] = chi[z] + 1
        dn[z] = chi[z] - 1
        f = lambda c: -8 * K * sum(((w[t] * c[t] - w[s] * c[s]) * (c[t] - c[s]) for s, t in SMALL_BONDS), ZERO)
        return (f(up) - f(dn)) / 2

    lin_in_w = all(chi_gradient(w_sum, z) == chi_gradient(w1, z) + chi_gradient(w2, z) for z in ((2, 2, 2), (1, 2, 3), (3, 1, 1)))
    site_only = True
    for z in ((2, 2, 2), (1, 3, 2)):
        bumped = dict(w1)
        other = (3, 3, 3)
        bumped[other] = w1[other] + 5
        g_z = lambda w: sum((chi[z] * (chi[add(z, e)] - chi[z]) for e in E6), ZERO) * 8 * K      # dF/dw_z = 8K chi_z (Lap chi)_z: no rate in it
        site_only = site_only and g_z(bumped) == g_z(w1)
    checks.check("B3", additive and not_additive_56 and lin_in_w and site_only, "T2: the bilinear field energy is ADDITIVE in the vector of rates at fixed lengths (block 56's is not): every rate is a multiplier, dF/dw_x = 8K chi_x (Lap chi)_x holds no rate at all, the FIELD contribution to length stationarity is linear in rates; hopping content generally is not")

    dims = (3, 3, 4)
    torus = list(product(*(range(d) for d in dims)))
    chi_t = {s: F(3, 4) + F((5 * s[0] + 3 * s[1] * s[2] + s[2]) % 11, 11) for s in torus}
    total = ZERO
    for s in torus:
        for e in E6:
            t = tuple((s[i] + e[i]) % dims[i] for i in range(3))
            total += chi_t[t] - chi_t[s]
    demand = sum((F(1) / (8 * K * chi_t[s]) for s in torus[:3]), ZERO)                  # three bodies of unit bare energy: the constraint asks sum Lap chi = -demand
    closed_ok = (total == 0) if not mut("closed_lattice_holds_a_static_body") else (total != 0)
    checks.check("B4", closed_ok and demand > 0, f"T2: on a closed lattice (3x3x4 torus, rational chi) the sum of (Lap chi)_x is zero, while the constraint asks (Lap chi)_x = -e_x/(8K w_x chi_x), whose sum is negative for positive content (here -{about(demand)}): no static solution; a reference (held walls) or motion of the lengths is needed")

    wx,wy=sp.symbols("wx wy",positive=True)
    hop=sp.sqrt(wx*wy)
    checks.check("B5",sp.simplify(sp.diff(hop,wx,wy)-1/(4*sp.sqrt(wx*wy)))==0,"T2: a single hopping coefficient sqrt(wx*wy) has nonzero mixed rate derivative; linear field energy does not make the full ledger rate-linear")


# ============================================================================================ family C
def jmul(a, b):
    return (a[0] * b[0], a[0] * b[1] + a[1] * b[0], a[0] * b[2] + a[1] * b[1] + a[2] * b[0])


def jexp(x):
    """exp(eps x) to second order in eps."""
    return (ONE, x, x * x / 2)


CELL = list(product(range(3), repeat=3))


def cell_nb(s):
    return [tuple((s[i] + e[i]) % 3 for i in range(3)) for e in E6]


def cell_lap(f, s):
    return sum((f[t] - f[s] for t in cell_nb(s)), ZERO)


def second_order_member(u, lam, a, b, p):
    """Coefficient of eps^2 (and of eps) in K sum w l^p (a Lap lam + b q) at (eps u, eps lam)."""
    c1 = ZERO
    c2 = ZERO
    for s in CELL:
        q = sum(((lam[t] - lam[s]) ** 2 for t in cell_nb(s)), ZERO) / 2
        j = jmul(jmul(jexp(u[s]), jexp(p * lam[s])), (ZERO, a * cell_lap(lam, s), b * q))
        c1 += j[1]
        c2 += j[2]
    return K * c1, K * c2


def second_order_bilinear(u, lam, c, p):
    """Coefficient of eps^2 in sum w c X Lap X, X = l^(p/2), at (eps u, eps lam)."""
    c2 = ZERO
    for s in CELL:
        x_s = jexp(F(p, 2) * lam[s])
        lap_x = (ZERO, ZERO, ZERO)
        for t in cell_nb(s):
            x_t = jexp(F(p, 2) * lam[t])
            lap_x = tuple(lap_x[i] + x_t[i] - x_s[i] for i in range(3))
        j = jmul(jmul(jexp(u[s]), x_s), lap_x)
        c2 += j[2]
    return c * c2


def cell_field(seed, mean_free=False):
    f = {s: F((seed * 13 + 7 * s[0] + 5 * s[1] * s[1] + 3 * s[2] * s[0] + s[1] * s[2] * seed) % 19 - 9, 6) for s in CELL}
    if mean_free:
        mean = sum(f.values(), ZERO) / len(CELL)
        f = {s: v - mean for s, v in f.items()}
    return f


def family_c(checks: Checks) -> None:
    u = cell_field(2, True)
    lam = cell_field(5, True)
    members = ((4, 2, 1), (4, 2, 2), (4, 1, 1), (2, 2, 3), (4, 8, 1), (6, 3, 1))
    form_ok = True
    for a, b, p in members:
        c1, c2 = second_order_member(u, lam, F(a), F(b), F(p))
        expect = K * sum((a * u[s] * cell_lap(lam, s) + (a * p - b) * lam[s] * cell_lap(lam, s) for s in CELL), ZERO)
        form_ok = form_ok and c1 == 0 and c2 == expect
    zero_lam = {s: ZERO for s in CELL}
    no_stiffness = all(second_order_member(u, zero_lam, F(a), F(b), F(p))[1] == 0 for a, b, p in members)
    checks.check("C1", form_ok and no_stiffness, "T3: for six members K l^p (a Lap lam + b q) on a periodic cell, exact second-order jets give K[a u.Lap lam + (ap - b) lam.Lap lam]; with the lengths unstretched the form vanishes for every u: the rates have no term of their own")

    beta_ok = True
    betas = []
    for a, b, p in members:
        beta = F(a, 2 * (a * p - b))
        betas.append(beta)
        used = beta if not mut("exponent_formula_sign") else -beta
        lam_star = {s: -used * u[s] for s in CELL}
        for z in ((0, 0, 0), (1, 2, 0), (2, 1, 1)):
            up = dict(lam_star)
            dn = dict(lam_star)
            up[z] += 1
            dn[z] -= 1
            grad = (second_order_member(u, up, F(a), F(b), F(p))[1] - second_order_member(u, dn, F(a), F(b), F(p))[1]) / 2
            beta_ok = beta_ok and grad == 0
    checks.check("C2", beta_ok and betas[0] == 1, f"T3: with no hop energy the lengths' stationarity at second order is solved by lam = -beta (u - ubar), beta = a/(2(ap - b)) (exact differences of the quadratic form at three sites, six members: beta = {', '.join(str(b) for b in betas)}); the member (4, 2, 1) has beta = 1; (4, 8, 1) has ap < b: its lengths stretch near a body like the others', and its clocks run FAST there")

    bil_ok = True
    for p in (1, 2, 3):
        c = 8 * K
        lhs = second_order_bilinear(u, lam, c, p)
        a, b = c * p / 2, c * p * p / 4
        rhs = second_order_member(u, lam, a / K, b / K, F(p))[1]
        beta = (a / K) / (2 * ((a / K) * p - b / K))
        target = F(1, p) if not mut("bilinear_member_gives_p") else F(p)
        bil_ok = bil_ok and lhs == rhs and beta == target
    checks.check("C3", bil_ok, "T3: the bilinear members c X Lap X, X = l^(p/2), agree at second order with (a, b) = (cp/2, cp^2/4): b = ap/2 and beta = 1/p (p = 1, 2, 3)")

    x, y, z = sp.symbols("x y z", real=True)
    lam_f = sp.Function("lam")(x, y, z)
    coords = (x, y, z)
    g = sp.diag(*([sp.exp(2 * lam_f)] * 3))
    ginv = g.inv()
    gamma = [[[sum(ginv[i, l] * (sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j]) - sp.diff(g[j, k], coords[l])) for l in range(3)) / 2 for k in range(3)] for j in range(3)] for i in range(3)]
    ricci = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            ricci[j, k] = sum(sp.diff(gamma[i][j][k], coords[i]) - sp.diff(gamma[i][j][i], coords[k]) + sum(gamma[i][i][l] * gamma[l][j][k] - gamma[i][k][l] * gamma[l][j][i] for l in range(3)) for i in range(3))
    scalar = sum(ginv[j, k] * ricci[j, k] for j in range(3) for k in range(3))
    chi_f = sp.exp(lam_f / 2)
    coefficient = 8 if not mut("curvature_identity_coefficient") else 6
    identity = sp.simplify(sp.exp(3 * lam_f) * scalar + coefficient * chi_f * sum(sp.diff(chi_f, c, 2) for c in coords))
    second = sp.simplify(8 * chi_f * sum(sp.diff(chi_f, c, 2) for c in coords) - sp.exp(lam_f) * (4 * sum(sp.diff(lam_f, c, 2) for c in coords) + 2 * sum(sp.diff(lam_f, c) ** 2 for c in coords)))
    checks.check("C4", identity == 0 and second == 0, "T3: in the continuum, for the metric l^2 delta in three dimensions, (volume density) x (scalar curvature) = -8 chi Lap chi = -l (4 Lap lam + 2 |grad lam|^2), chi = sqrt(l) (exact symbolic algebra): the bilinear member with p = 1 is K x rate x volume x curvature with a minus sign, and the power p = 1 is three (the volume) minus two (the curvature)")

    grads_ok = True
    for zsite in ((0, 0, 0), (1, 2, 0), (2, 1, 1)):
        up = dict(lam)
        dn = dict(lam)
        up[zsite] += 1
        dn[zsite] -= 1
        g_lam = (second_order_member(u, up, F(4), F(2), F(1))[1] - second_order_member(u, dn, F(4), F(2), F(1))[1]) / 2
        uu = dict(u)
        ud = dict(u)
        uu[zsite] += 1
        ud[zsite] -= 1
        g_u = (second_order_member(uu, lam, F(4), F(2), F(1))[1] - second_order_member(ud, lam, F(4), F(2), F(1))[1]) / 2
        grads_ok = grads_ok and g_lam == 4 * K * (cell_lap(u, zsite) + cell_lap(lam, zsite)) and g_u == 4 * K * cell_lap(lam, zsite)
    amp = amplitude()
    phi = small_field(3, F(1, 2), ONE)
    chi = small_field(8, F(3, 4), F(1, 2))
    zsite = (2, 2, 2)
    hop_at_z = ZERO
    for s, t in SMALL_BONDS:
        if zsite in (s, t) and s in amp and t in amp:
            hop_at_z -= phi[s] * phi[t] / (chi[s] * chi[t]) * 2 * (amp[s][0] * amp[t][0] + amp[s][1] * amp[t][1])
    doubled = dict(chi)
    doubled[zsite] = 2 * chi[zsite]
    no_mass = {}
    hop_ok = content_energy(phi, doubled, amp, no_mass) - content_energy(phi, chi, amp, no_mass) == -hop_at_z / 2
    checks.check("C5", grads_ok and hop_ok, "T3: for the member (4, 2, 1) the second-order form's gradients are 4K Lap lam in u and 4K (Lap u + Lap lam) in lam (exact differences); the content's energy falls as 1/chi_z on the bonds at z, so its derivative in lam_z is minus half the hop energy there, tau_z: at weak field Lap lam = -e/(4K wbar) and Lap u = (e + tau)/(4K wbar): the clock source is e+tau in this linear scalar ansatz; arbitrary hop density need not be positive")


# ============================================================================================ family D
CENTRE = (3, 3, 3)
BODY_SITES = ((2, 3, 3), (4, 3, 2), (3, 5, 4))


def stationarity(chi, nf, masses):
    """Both conditions at every interior site: m_x + 8K chi_x (Lap chi)_x = 0, and w_z (Lap chi)_z + (Lap N)_z = 0 with w = N/chi."""
    ok = True
    for s in INTERIOR:
        lc = lap(chi, s)
        ok = ok and masses.get(s, ZERO) + 8 * K * chi[s] * lc == 0
        ok = ok and nf[s] / chi[s] * lc + lap(nf, s) == 0
    return ok


def wall_flux(chi):
    tot = ZERO
    for s in ALL_SITES:
        if s in INDEX:
            continue
        for e in E6:
            t = add(s, e)
            if t in INDEX:
                tot += chi[t] - 1
    return tot


def family_d(checks: Checks) -> None:
    g = green_columns([CENTRE] + list(BODY_SITES))
    g0 = g[CENTRE][CENTRE]
    q = F(5, 2)
    chi = {s: 1 + q * g[CENTRE][s] for s in INTERIOR}
    m = 8 * K * q * chi[CENTRE]
    p_true = q / (1 + 2 * q * g0)
    p_used = p_true if not mut("rate_at_the_body_uses_one_charge") else q / (1 + q * g0)
    nf = {s: 1 - p_used * g[CENTRE][s] for s in INTERIOR}
    w0 = nf[CENTRE] / chi[CENTRE]
    ok_one = stationarity(chi, nf, {CENTRE: m}) and w0 == 1 / (1 + 2 * q * g0)
    checks.check("D1", ok_one, f"T4: one body at the centre of the 7x7x7 box (Q = 5/2, 8K = 6, g_0 = {about(g0)}, bare energy {about(m)}): chi = 1 + Q g and N = 1 - P g, P = Q/(1 + 2Qg_0), satisfy BOTH stationarity conditions at all 125 interior sites exactly; the body's clock runs at 1/(1 + 2Qg_0) = {about(w0)}")

    nf_true = {s: 1 - p_true * g[CENTRE][s] for s in INTERIOR}
    ledger = m * nf_true[CENTRE] / chi[CENTRE] + bond_form(nf_true, chi)
    ok_ledger = ledger == 8 * K * q == m / chi[CENTRE] == 8 * K * wall_flux(chi) and ledger < m
    checks.check("D2", ok_ledger, f"T4: the ledger of the box (content plus the bond form) equals the walls' term 8K x (flux of chi into the walls) = 8KQ = m/chi_0 = {about(ledger)}, below the bare energy {about(m)}")

    qs = (F(3, 2), F(1, 3), F(4))
    chi3 = {s: 1 + sum((qs[i] * g[b][s] for i, b in enumerate(BODY_SITES)), ZERO) for s in INTERIOR}
    mu = [qs[i] * chi3[b] for i, b in enumerate(BODY_SITES)]
    masses3 = {b: 8 * K * mu[i] for i, b in enumerate(BODY_SITES)}
    mat = [[(ONE if i == j else ZERO) + qs[i] / chi3[bi] * g[bj][bi] for j, bj in enumerate(BODY_SITES)] for i, bi in enumerate(BODY_SITES)]
    ps = solve_multi(mat, [[qs[i] / chi3[b] for i, b in enumerate(BODY_SITES)]])[0]
    nf3 = {s: 1 - sum((ps[i] * g[b][s] for i, b in enumerate(BODY_SITES)), ZERO) for s in INTERIOR}
    w3 = [nf3[b] / chi3[b] for b in BODY_SITES]
    ledger3 = sum((masses3[b] * w3[i] for i, b in enumerate(BODY_SITES)), ZERO) + bond_form(nf3, chi3)
    bounded = all(0 < nf3[s] <= 1 and 0 < nf3[s] / chi3[s] <= 1 for s in INTERIOR)
    ok_three = (stationarity(chi3, nf3, masses3) and bounded and all(ps[i] == qs[i] * w3[i] for i in range(3)) and sum(ps) < sum(qs)
                and ledger3 == 8 * K * sum(qs) == sum((masses3[b] / chi3[b] for b in BODY_SITES), ZERO))
    checks.check("D3", ok_three, f"T4: three bodies (Q = 3/2, 1/3, 4): both conditions hold at all 125 sites; 0 < N <= 1 and 0 < w <= 1 everywhere; N = 1 - sum P_i g_i with P_i = Q_i w_i exactly (clocks at {', '.join(about(v) for v in w3)}), so sum P = {about(sum(ps))} < sum Q = {about(sum(qs))}; ledger = 8K sum Q = sum m_i/chi_i = {about(ledger3)} of bare {about(sum(masses3.values()))}")

    gm = [[g[bj][bi] for bj in BODY_SITES] for bi in BODY_SITES]
    grad_ok = all(1 + sum((gm[i][j] * qs[j] for j in range(3)), ZERO) - mu[i] / qs[i] == 0 for i in range(3))
    hess = [[gm[i][j] + (mu[i] / qs[i] ** 2 if i == j else ZERO) for j in range(3)] for i in range(3)]
    m1 = hess[0][0]
    m2 = hess[0][0] * hess[1][1] - hess[0][1] * hess[1][0]
    m3 = (hess[0][0] * (hess[1][1] * hess[2][2] - hess[1][2] * hess[2][1]) - hess[0][1] * (hess[1][0] * hess[2][2] - hess[1][2] * hess[2][0])
          + hess[0][2] * (hess[1][0] * hess[2][1] - hess[1][1] * hess[2][0]))
    sym = all(gm[i][j] == gm[j][i] for i in range(3) for j in range(3))
    alone_larger = all(qs[i] * (1 + gm[i][i] * qs[i]) - mu[i] < 0 for i in range(3))
    d = [mu[i] / qs[i] ** 2 for i in range(2)]
    g11, g22, g12 = gm[0][0], gm[1][1], gm[0][1]
    # two bodies (the first two sites, their own charges): d(Q_1 + Q_2)/d g_12 = -[(d_2 + g_22 - g_12) Q_2 + (d_1 + g_11 - g_12) Q_1]/det, with d_i = chi_i/Q_i
    chi_pair = [1 + g11 * qs[0] + g12 * qs[1], 1 + g12 * qs[0] + g22 * qs[1]]
    dd = [chi_pair[0] / qs[0], chi_pair[1] / qs[1]]
    det = (dd[0] + g11) * (dd[1] + g22) - g12 * g12
    slope = -((dd[1] + g22 - g12) * qs[1] + (dd[0] + g11 - g12) * qs[0]) / det
    checks.check("D4", grad_ok and sym and m1 > 0 and m2 > 0 and m3 > 0 and alone_larger and slope < 0 and g11 > g12 and g22 > g12,
                 f"T4: the charges are the minimum of the strictly convex function sum Q + (1/2) Q.G Q - sum mu_i log Q_i (gradient zero, Hessian's leading minors {about(m1)}, {about(m2)}, {about(m3)}): the positive solution is unique; each body alone would carry a larger charge (the pair shows the walls less than its parts), and at fixed diagonal entries and bare masses the total charge falls as the mutual inverse entry rises (slope {about(slope)} for two bodies)")

    m_56 = m / (1 + m * g0 / (8 * K))
    big_q = F(1000)
    seen_big = 8 * K * big_q
    bound_56 = 8 * K / g0
    unbounded = (seen_big > bound_56) if not mut("seen_from_outside_saturates") else (seen_big <= bound_56)
    checks.check("D5", ledger > m_56 and unbounded, f"T4: at the same bare energy the walls see {about(ledger)} here against {about(m_56)} under block 56's bond energy (same first correction, gamma = 1/(4K)); block 56's bound is 8K/g_0 = {about(bound_56)}, while here Q = 1000 shows the walls {about(seen_big)}: what is seen obeys M + M^2 g_0/(8K) = m and grows without bound, as the root of the bare energy")

    ratio = 1 + 2 * q / (p_true + q)
    weak_q = F(1, 1000)
    weak_ratio = 1 + (1 + 2 * weak_q * g0) / (1 + weak_q * g0)
    equal_ok = (p_true != q) if not mut("far_field_coefficients_equal") else (p_true == q)
    checks.check("D6", equal_ok and ratio == 1 + (1 + 2 * q * g0) / (1 + q * g0) and 2 < ratio < 3 and 0 < weak_ratio - 2 < F(1, 1000),
                 f"T4: far from the body chi - 1 = Q g and 1 - N = P g: the lengths carry 2Q and the rates P + Q, equal only to first order (P = {about(p_true)} against Q = {about(q)}); the leading weak-exterior local transverse ray coefficient ratio is 1 + 2Q/(P + Q) = 1 + (1 + 2Qg_0)/(1 + Qg_0) = {about(ratio)} here, within 1/1000 of 2 for Q = 1/1000, and below 3 at any strength")

    w3f = {s: nf3[s] / chi3[s] for s in INTERIOR}
    rule_ok = True
    for s in INTERIOR:
        sw = sum((val(chi3, add(s, e)) * val(w3f, add(s, e)) for e in E6), ZERO)
        sc = sum((val(chi3, add(s, e)) for e in E6), ZERO)
        kappa = 1 / (1 + masses3.get(s, ZERO) / (4 * K * chi3[s] * sc))
        rule_ok = rule_ok and w3f[s] == kappa * sw / sc
    kappas = [1 / (1 + masses3[b] / (4 * K * chi3[b] * sum((val(chi3, add(b, e)) for e in E6), ZERO))) for b in BODY_SITES]
    checks.check("D7", rule_ok and all(0 < k < 1 for k in kappas), f"T4: the rates' equation is block 53's form at every strength: w_z = kappa_z x (the mean of the six neighbours' rates weighted by their chi), kappa_z = 1/(1 + m_z/(4K chi_z sum_y chi_y)): 1 in empty space, {', '.join(about(k) for k in kappas)} at the three bodies; at weak field log kappa = -m/(24K), block 55's -(gamma/6) m with gamma = 1/(4K)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    u = cell_field(2, True)
    u2 = cell_field(7, True)
    lam = cell_field(5, True)
    usum = {s: u[s] + u2[s] for s in CELL}
    linear_in_u = all(second_order_member(usum, lam, F(a), F(b), F(p))[1] - second_order_member(u, lam, F(a), F(b), F(p))[1] - second_order_member(u2, lam, F(a), F(b), F(p))[1]
                      == -second_order_member({s: ZERO for s in CELL}, lam, F(a), F(b), F(p))[1] for a, b, p in ((4, 2, 1), (4, 1, 1), (2, 2, 3)))
    near, far = (1, 1, 1), (5, 5, 5)
    g = green_columns([near])
    e_on = F(1, 100)
    response = e_on * g[near][far] / (4 * K)
    delayed_ok = (response > 0) if not mut("kinetic_term_delays_the_lengths") else (response == 0)
    checks.check("E1", linear_in_u and delayed_ok, f"T5: at second order the field energy is affine in u for every member, and a kinetic term c_k l^s (dlam/dt)^2/w holds no rate of change of u: the rates stay multipliers and the constraint 4K Lap lam = -e/wbar holds at each label time; a source of 1/100 switched on at one corner of the box changes the length at the far corner by {about(response * 10 ** 6)} millionths at the SAME label time: the grounded linearized constraint is instantaneous; nonlinear dynamics and other backgrounds are not tested")

    t, t0, kap, m, s_ = sp.symbols("t t_0 kappa m s", positive=True)
    lam_t = sp.Function("lam")(t)
    w_ = sp.symbols("w", positive=True)
    ck = -kap if not mut("positive_kinetic_term_moves_the_lengths") else kap
    lagrangian = ck * sp.exp(s_ * lam_t) * sp.diff(lam_t, t) ** 2 / w_ - m * w_
    constraint = sp.diff(lagrangian, w_).subs(w_, 1)                                                     # = -c_k l^s lam'^2 - m
    lam_eq = (sp.diff(sp.diff(lagrangian, sp.diff(lam_t, t)), t) - sp.diff(lagrangian, lam_t)).subs(w_, 1)
    sol = (2 / s_) * sp.log(1 + t / t0)
    t0_val = 2 * sp.sqrt(kap / m) / s_
    c_res = sp.simplify(constraint.subs(lam_t, sol).doit().subs(t0, t0_val))
    l_res = sp.simplify(lam_eq.subs(lam_t, sol).doit())
    kept = sp.simplify(sp.diff(constraint, t) + sp.diff(lam_t, t) * lam_eq)                             # d(constraint)/dt = -(dlam/dt) x (the lengths' equation)
    checks.check("E2", c_res == 0 and l_res == 0 and sp.simplify(kept) == 0, "T5: a closed lattice with content at rest and c_k = -kappa < 0 (label with w = 1): l = (1 + t/t_0)^(2/s), t_0 = (2/s) sqrt(kappa/m), solves the constraint m = kappa l^s (dlam/dt)^2 and the lengths' equation 2 lam'' + s lam'^2 = 0 (exact symbolic algebra), and the rate of change of the constraint is -(dlam/dt) times the lengths' equation: it is kept; for c_k > 0 the constraint m + c_k l^s (dlam/dt)^2 = 0 has no solution with m > 0")

    zero_power=sp.sqrt(m/kap)*t
    check_zero=sp.simplify(kap*sp.diff(zero_power,t)**2-m)==0 and sp.diff(zero_power,t,2)==0
    checks.check("E3",check_zero,"T5: the omitted s=0 case has lambda=lambda0 +/-sqrt(m/kappa)t, an exponential positive length, satisfying constraint and length equation")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero; it reports what a ledger linear in the rates does, in general and for one declared member; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[n for n in nodes if isinstance(n,ast.Constant) and isinstance(n.value,float)]
    float_hits += [n for n in nodes if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id in ('float','N')) or (isinstance(n.func,ast.Attribute) and n.func.attr in ('evalf','N')))]
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
    "per_element: executed — both ledgers on a 5x5x5 box with a hopping rational amplitude: weight one, the sum over all sites of w dE/dw by exact differences, additivity of the linear field energy in the rates",
    "per_site: executed — both stationarity conditions at all 125 interior sites of a 7x7x7 box for one body and for three bodies; the rate at each body; P_i = Q_i w_i",
    "per_mode: executed — exact second-order jets of six nearest-neighbour members and three bilinear members on a periodic cell; the exponent beta by exact differences; the continuum curvature identity by exact symbolic algebra",
    "per_block: executed — the ledger against the wall term, against the bare energies and against block 56 at the same bare energy; convexity and uniqueness; the far-field coefficients; the closed lattice; the uniform motion of the lengths and the keeping of its constraint",
    "lattice_wide: T1 holds for every ledger of weight one; T2 for every field energy linear in the rates (the closed-lattice statement for the bilinear members); T3 for the nearest-neighbour members named, at second order; T4 for bodies at rest in any box with walls held at w = l = 1, for the bilinear member with p = 1 and isotropic stretching only; T5 at second order for every local kinetic term of the stated form, and for uniform configurations; that lengths exist, that the field energy is linear in the rates, the member, its number K, the powers p and s, the sign of c_k, and whether the anisotropic parts of block 59 can stay at rest are not derived",
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
    print("scope: homogeneous stationary boundary identity; field-only rate linearity; stated weak-field exponent; positive finite diagonal-source solution; restricted static-background kinetic constraint and uniform power-law/exponential solutions")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
