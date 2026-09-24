#!/usr/bin/env python3
"""Exact quadratic three-length model controls on product boxes and periodic lattices.
Static source examples, continuum quadratic identities and the normalized dispersion
polynomial are checked. Source universality, nonlinear stability and strict fronts
are not consequences of these tests.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.calculus.euler import euler_equations

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THREE_LENGTHS_PER_SITE_A_BODY_AT_REST_STRETCHES_THEM_ALIKE_HOP_ENERGY_DRIVES_WHOLE_COLUMNS_AND_THE_DELAYS_SPEED_DEPENDS_ON_DIRECTION_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_and_the_delays_speed_depends_on_direction_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "second_order_form_has_a_self_term": "B",
    "kinetic_density_sign": "B",
    "body_at_rest_stretches_unequally": "C",
    "static_equations_leave_a_freedom": "C",
    "hop_energy_response_is_local": "D",
    "tent_height_ignores_the_box": "D",
    "equal_lengths_law_survives_hop_energy": "D",
    "body_diagonal_speed_is_one": "E",
    "speeds_are_direction_free": "E",
    "some_kinetic_term_is_isotropic": "E",
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
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
K = F(3, 4)                                                  # the field energy's one number; the ambient rate is 1


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


def add(s, e, sign=1):
    return (s[0] + sign * e[0], s[1] + sign * e[1], s[2] + sign * e[2])


def solve_multi(a, rhs_list):
    """Solve a x = b exactly for several right-hand sides at once; raises if the matrix is singular."""
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


class Box:
    """Interior sites 1..n of a box with walls at 0 and n + 1 where every field is held at zero."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.sites = list(product(range(1, n + 1), repeat=3))
        self.index = {s: i for i, s in enumerate(self.sites)}

    def d2(self, field, s, axis):
        """Second difference along one axis; the field is zero outside the interior."""
        e = AXES[axis]
        return field.get(add(s, e), ZERO) + field.get(add(s, e, -1), ZERO) - 2 * field.get(s, ZERO)

    def lap(self, field, s):
        return sum((self.d2(field, s, ax) for ax in range(3)), ZERO)

    def tent(self, z, z0):
        """The inverse of the one-dimensional second difference with zero walls, column z0: -min(z, z0)(n + 1 - max(z, z0))/(n + 1)."""
        lo, hi = min(z, z0), max(z, z0)
        return -F(lo * (self.n + 1 - hi), self.n + 1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    x, y, z, eps = sp.symbols("x y z epsilon", real=True)
    coords = (x, y, z)
    lam = [sp.Function(f"lam{j}")(x, y, z) for j in range(3)]
    g = sp.diag(*[sp.exp(2 * eps * lam[j]) for j in range(3)])
    ginv = g.inv()
    gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], coords[k]) + sp.diff(g[l, k], coords[j]) - sp.diff(g[j, k], coords[l])) for l in range(3)) / 2 for k in range(3)] for j in range(3)] for i in range(3)]
    ric = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            ric[j, k] = sum(sp.diff(gam[i][j][k], coords[i]) - sp.diff(gam[i][j][i], coords[k]) + sum(gam[i][i][l] * gam[l][j][k] - gam[i][k][l] * gam[l][j][i] for l in range(3)) for i in range(3))
    scalar = sum(ginv[j, k] * ric[j, k] for j in range(3) for k in range(3))
    dens = sp.exp(eps * sum(lam)) * scalar
    ser = sp.series(dens, eps, 0, 3).removeO()
    first = sp.expand(ser.coeff(eps, 1))
    second = sp.expand(ser.coeff(eps, 2))
    first_expected = -2 * sum(sp.diff(lam[j], coords[i], 2) for j in range(3) for i in range(3) if i != j)
    pairs = ((0, 1, 2), (0, 2, 1), (1, 2, 0))                                                   # (i, m, k): the two lengths and the third axis
    cand = 2 * sum(sp.diff(lam[i], coords[k]) * sp.diff(lam[m], coords[k]) for i, m, k in pairs)
    if mut("second_order_form_has_a_self_term"):
        cand = cand + sp.diff(lam[0], coords[1]) ** 2

    def el(lagrangian):
        return [sp.expand(e.lhs) for e in euler_equations(lagrangian, lam, coords)]

    same = all(sp.simplify(p - q) == 0 for p, q in zip(el(second), el(cand)))
    checks.check("B1", sp.simplify(first - first_expected) == 0 and same, "T1: for the metric diag(l_1^2, l_2^2, l_3^2), volume density x scalar curvature is -2 sum_j sum_{i != j} d_i^2 lam_j at first order, and at second order it has the same variational derivatives as 2 (d_3 lam_1 d_3 lam_2 + d_2 lam_1 d_2 lam_3 + d_1 lam_2 d_1 lam_3): each pair of lengths is coupled through differences along the third axis, and no length has a term of its own (exact symbolic algebra)")

    one = sp.Function("lam")(x, y, z)
    sub = {lam[j]: one for j in range(3)}
    first_equal = sp.simplify(first.subs(sub).doit() + 4 * sum(sp.diff(one, c, 2) for c in coords))
    second_equal = sp.simplify(cand.subs(sub).doit() - 2 * sum(sp.diff(one, c) ** 2 for c in coords)) if not mut("second_order_form_has_a_self_term") else sp.Integer(0)
    t = sp.symbols("t", real=True)
    w = sp.symbols("w", positive=True)
    lt = [sp.Function(f"l{j}")(t) for j in range(3)]
    kmix = [-sp.diff(sp.exp(2 * lt[j]), t) / (2 * w) * sp.exp(-2 * lt[j]) for j in range(3)]      # the mixed components -(dlam_j/dt)/w
    kin = sum(k ** 2 for k in kmix) - sum(kmix) ** 2
    sign = -2 if not mut("kinetic_density_sign") else 2
    kin_expected = sign * sum(sp.diff(lt[i], t) * sp.diff(lt[m], t) for i in range(3) for m in range(i + 1, 3)) / w ** 2
    equal_kin = sp.simplify(kin.subs({lt[1]: lt[0], lt[2]: lt[0]}).doit() + 6 * sp.diff(lt[0], t) ** 2 / w ** 2)
    checks.check("B2", first_equal == 0 and second_equal == 0 and sp.simplify(kin - kin_expected) == 0 and equal_kin == 0, "T1: with equal lengths the two orders are -4 Lap lam and 2 |grad lam|^2, block 60's member; the kinetic density of lengths that change in the label, with no sliding of sites, is -2 sum_{i<m} (dlam_i/dt)(dlam_m/dt)/w^2, which is -6 (dlam/dt)^2/w^2 for equal lengths (block 60's c_k = -6K, s = 3)")


# ============================================================================================ family C
def static_system(box: Box):
    """Rows (each divided by 2K): D_3 lam_2 + D_2 lam_3 + (D_2 + D_3) u = tau_1/(2K) and its rotations; sum_j (Lap - D_j) lam_j = -e/(2K)."""
    n = len(box.sites)
    a = [[ZERO] * (4 * n) for _ in range(4 * n)]

    def put(row, block, s, axis, coef):
        """Add coef x (second difference along axis) of the field in the given block, evaluated at site s, to the row."""
        e = AXES[axis]
        a[row][block * n + box.index[s]] += -2 * coef
        for sign in (1, -1):
            nb = add(s, e, sign)
            if nb in box.index:
                a[row][block * n + box.index[nb]] += coef

    for s in box.sites:
        i = box.index[s]
        for j in range(3):
            others = [ax for ax in range(3) if ax != j]
            p, q = others                                           # equation of lam_j: D_q lam_p + D_p lam_q + (D_p + D_q) u
            put(j * n + i, p, s, q, ONE)
            put(j * n + i, q, s, p, ONE)
            put(j * n + i, 3, s, p, ONE)
            put(j * n + i, 3, s, q, ONE)
            put(3 * n + i, j, s, p, ONE)                             # constraint: (D_p + D_q) lam_j
            put(3 * n + i, j, s, q, ONE)
    return a


def family_c(checks: Checks) -> None:
    box = Box(3)
    n = len(box.sites)
    a = static_system(box)
    centre = (2, 2, 2)
    energy = F(3, 10)
    rhs = [ZERO] * (4 * n)
    rhs[3 * n + box.index[centre]] = -energy / (2 * K)
    try:
        sol = solve_multi(a, [rhs])[0]
        solved = True
    except ValueError:
        sol = [ZERO] * (4 * n)
        solved = False
    l1, l2, l3, u = (sol[b * n:(b + 1) * n] for b in range(4))
    lap_matrix = [[ZERO] * n for _ in range(n)]
    for s in box.sites:
        i = box.index[s]
        lap_matrix[i][i] = F(-6)
        for e in AXES:
            for sign in (1, -1):
                nb = add(s, e, sign)
                if nb in box.index:
                    lap_matrix[i][box.index[nb]] += 1
    src = [ZERO] * n
    src[box.index[centre]] = -energy / (4 * K)
    lam_iso = solve_multi(lap_matrix, [src])[0]
    alike = (l1 == l2 == l3) if not mut("body_at_rest_stretches_unequally") else (l1 != l2)
    unique = solved if not mut("static_equations_leave_a_freedom") else (not solved)
    checks.check("C1", unique and alike and l1 == [-v for v in u] and l1 == lam_iso, f"T2: 5x5x5 box, walls held: the 108 static equations are non-singular (one solution); for a body at rest of energy 3/10 it has lam_1 = lam_2 = lam_3 = -u at all 27 sites, equal to the solution of block 60's law 4K Lap lam = -e (lam at the body {about(l1[box.index[centre]])})")

    minors_ok = True
    for size in (3, 5):
        m = sp.Matrix(size, size, lambda i, j: 2 if i == j else (-1 if abs(i - j) == 1 else 0))
        minors_ok = minors_ok and all(m[:k, :k].det() == k + 1 for k in range(1, size + 1))
    a_, b_, c_ = sp.symbols("a b c", positive=True)
    det3 = sp.Matrix([[0, c_, b_], [c_, 0, a_], [b_, a_, 0]]).det()
    checks.check("C2", minors_ok and sp.simplify(det3 - 2 * a_ * b_ * c_) == 0, "T2 (the proof's ingredients): minus the one-dimensional second difference with zero walls has leading minors 2, 3, ..., n + 1, so its eigenvalues a, b, c along the three axes are positive; in their common eigenbasis the equations for lam_j + u have determinant 2abc, never zero: lam_j = -u for content at rest, and then the constraint gives the law of block 60")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    box = Box(5)
    c0 = 3
    centre = (c0, c0, c0)
    quarter = 1 / (4 * K)

    def second_diff_of_delta(xx):
        return F(-2) if xx == c0 else (ONE if abs(xx - c0) == 1 else ZERO)

    a2 = {s: (box.tent(s[2], c0) * quarter if (s[0], s[1]) == (c0, c0) else ZERO) for s in box.sites}
    a3 = {s: (box.tent(s[1], c0) * quarter if (s[0], s[2]) == (c0, c0) else ZERO) for s in box.sites}
    a1 = {s: -second_diff_of_delta(s[0]) * box.tent(s[1], c0) * box.tent(s[2], c0) * quarter for s in box.sites}
    eq_ok = True
    for s in box.sites:
        tau = ONE if s == centre else ZERO
        eq_ok = eq_ok and 2 * K * (box.d2(a2, s, 2) + box.d2(a3, s, 1)) == tau
        eq_ok = eq_ok and box.d2(a1, s, 2) + box.d2(a3, s, 0) == 0
        eq_ok = eq_ok and box.d2(a1, s, 1) + box.d2(a2, s, 0) == 0
    column = [a2[(c0, c0, zz)] for zz in range(1, 6)]
    off_column = all(a2[s] == 0 for s in box.sites if (s[0], s[1]) != (c0, c0))
    reaches = all(v != 0 for v in column) if not mut("hop_energy_response_is_local") else (column[0] == 0)
    checks.check("D1", eq_ok and off_column and reaches, f"T3: 7x7x7 box, one unit of hop energy along axis 1 at the centre: a_2 = D_3^(-1) tau/(4K), a_3 = D_2^(-1) tau/(4K), a_1 = -D_1 D_2^(-1) D_3^(-1) tau/(4K) satisfy the three equations at all 125 sites exactly; a_2 = lam_2 + u is zero off the column through the source along axis 3 and is a tent on it, {', '.join(str(v) for v in column)}: it reaches the walls")

    heights = {nn: Box(nn).tent((nn + 1) // 2, (nn + 1) // 2) * quarter for nn in (3, 5, 13, 101)}
    grows = all(heights[nn] == -F(nn + 1, 16) / K for nn in heights) if not mut("tent_height_ignores_the_box") else (heights[3] == heights[5])
    checks.check("D2", grows, f"T3: the tent's height at the source is -(n + 1)/(16K) for n interior sites across: {', '.join(str(heights[nn]) for nn in heights)} for n = 3, 5, 13, 101; it grows with the distance to the walls: not a field that falls off")

    n = len(box.sites)
    lap_matrix = [[ZERO] * n for _ in range(n)]
    for s in box.sites:
        i = box.index[s]
        lap_matrix[i][i] = F(-6)
        for e in AXES:
            for sign in (1, -1):
                nb = add(s, e, sign)
                if nb in box.index:
                    lap_matrix[i][box.index[nb]] += 1
    fields = (a1, a2, a3)
    rhs_u = [sum(((box.lap(fields[j], s) - box.d2(fields[j], s, j)) for j in range(3)), ZERO) / 2 for s in box.sites]
    delta = [ONE if s == centre else ZERO for s in box.sites]
    u_list, green = solve_multi(lap_matrix, [rhs_u, delta])
    u = {s: u_list[box.index[s]] for s in box.sites}
    lam = [{s: fields[j][s] - u[s] for s in box.sites} for j in range(3)]
    constraint_ok = all(sum(((box.lap(lam[j], s) - box.d2(lam[j], s, j)) for j in range(3)), ZERO) == 0 for s in box.sites)
    end = (c0, c0, 1)
    third = F(1, 3)
    a1_equal = third * (a1[end] + box.tent(1, c0) * quarter)                       # tau_2 and tau_3 by rotation: tents along axes 3 and 2; only the first passes through this site
    iso = {s: green[box.index[s]] * quarter for s in box.sites}                     # block 60's equal-lengths law with hop energy: Lap (u + lam) = tau/(4K)
    beside = (c0 + 1, c0, c0)                                                       # at the source itself the equal-lengths law passes by symmetry; one site along axis 1 it does not
    residual = 2 * K * (box.d2(iso, beside, 1) + box.d2(iso, beside, 2))
    survives = (residual != 0) if not mut("equal_lengths_law_survives_hop_energy") else (residual == 0)
    rates_ok = all(u[s] == iso[s] for s in box.sites)                                # the rates obey Lap u = tau/(4K) exactly: block 60's law for the rates survives
    checks.check("D3", constraint_ok and rates_ok and a1_equal == F(1, 9) and survives, f"T3: with the rates from the constraint (an exact 125-site solve) all four sets of equations hold, and the rates are exactly those of block 60's law Lap u = tau/(4K): it is the lengths that leave it; EQUAL hop energies of 1/3 along the three axes still leave lam_1 + u = 1/9 at the end of a column, two sites from the source and next to the wall; and block 60's equal-lengths law Lap(u + lam) = tau/(4K) does not solve the wider equations (it passes at the source by symmetry and leaves a residual of {about(residual)} one site along axis 1, where there is no hop energy): these point-source examples cannot keep the three lengths equal; specially structured extended sources can")

    # Counterexample to the claim that every nonzero hop source breaks equality.
    same={z:F(sum(z)) for z in box.sites}
    tau=[{z:2*K*(box.lap(same,z)-box.d2(same,z,j)) for z in box.sites} for j in range(3)]
    equal_ok=any(v for field in tau for v in field.values())
    equal_ok=equal_ok and all(2*K*sum(box.d2(same,z,l) for l in range(3) if l!=j)==tau[j][z] for j in range(3) for z in box.sites)
    checks.check("D4",equal_ok,"T3 boundary: structured nonzero sources tau_j=2K(Delta-D_j)f admit equal a_j=f; the point-source failure is not universal")


# ============================================================================================ family E
def mode_matrix(xx, a, b, c, m1, m2):
    """Second derivatives of X T - V in (A_1, A_2, A_3, U), lengths in units with K = wbar = 1 and the kinetic numbers in units of K."""
    return sp.Matrix([
        [2 * m1 * xx, m2 * xx + 2 * c, m2 * xx + 2 * b, 2 * (b + c)],
        [m2 * xx + 2 * c, 2 * m1 * xx, m2 * xx + 2 * a, 2 * (a + c)],
        [m2 * xx + 2 * b, m2 * xx + 2 * a, 2 * m1 * xx, 2 * (a + b)],
        [2 * (b + c), 2 * (a + c), 2 * (a + b), 0],
    ])


def family_e(checks: Checks) -> None:
    xx, a, b, c, m1, m2 = sp.symbols("X a b c m1 m2", real=True)
    s = a + b + c
    sig = a * b + a * c + b * c
    pi = a * b * c
    det = sp.expand(mode_matrix(xx, a, b, c, m1, m2).det())
    formula = -16 * ((2 * m1 - m2) * (m1 * s ** 2 - (m1 + m2) * sig) * xx ** 2 - 2 * (m1 * s ** 3 - (2 * m1 + m2) * s * sig + 3 * (m1 + m2) * pi) * xx + 4 * pi * s)
    comparator = sp.expand(det.subs({m1: 0, m2: -2}) + 64 * (sig * xx ** 2 - (s * sig - 3 * pi) * xx + pi * s))
    checks.check("E1", sp.expand(det - formula) == 0 and comparator == 0, "T4: the determinant of the mode equations in (lam_1, lam_2, lam_3, u) is -16 [(2m_1 - m_2)(m_1 s^2 - (m_1 + m_2) sigma) X^2 - 2 (m_1 s^3 - (2m_1 + m_2) s sigma + 3 (m_1 + m_2) pi) X + 4 pi s] in the symmetric functions of a, b, c; for the comparator's kinetic term it is -64 [sigma X^2 - (s sigma - 3 pi) X + pi s]: a quadratic determinant identity; oscillatory mode counts require nondegenerate kinetic coefficients and positive roots")

    rho = sp.symbols("rho", positive=True)
    disc_ok = sp.expand((1 - 3 * rho) ** 2 - 4 * rho - (1 - rho) * (1 - 9 * rho)) == 0
    samples = ((F(1), F(2), F(3)), (F(1, 3), F(7, 2), F(4)), (F(2), F(2), F(2)), (F(1, 100), F(3), F(5, 7)))
    bound_ok = all(9 * p * q * r <= (p + q + r) * (p * q + p * r + q * r) for p, q, r in samples)
    diag_poly = sp.factor((sig * xx ** 2 - (s * sig - 3 * pi) * xx + pi * s).subs({b: a, c: a}))
    diag_root = sp.solve(sp.Eq(diag_poly, 0), xx)
    target = a if not mut("body_diagonal_speed_is_one") else 3 * a
    plane_poly = sp.factor((sig * xx ** 2 - (s * sig - 3 * pi) * xx + pi * s).subs(c, 0))
    checks.check("E2", disc_ok and bound_ok and diag_root == [target] and sp.expand(plane_poly - a * b * xx * (xx - a - b)) == 0,
                 "T4: with v = X/s and rho = pi/(s sigma): v_1 + v_2 = 1 - 3 rho, v_1 v_2 = rho, discriminant (1 - rho)(1 - 9 rho) >= 0 because 9 abc <= (a + b + c)(ab + ac + bc); in a coordinate plane the roots are X = a + b (v = 1) and X = 0; on a body diagonal X = a twice (v = 1/3): the normalized squared frequency depends on direction; sqrt(3) is the phase-speed ratio of these directions only in the long-wavelength limit")

    la, lb, lc = F(1), F(1), F(4)                                                                  # 4 sin^2(k/2) at k = pi/3, pi/3, pi
    roots = sp.solve(sp.Eq((la * lb + la * lc + lb * lc) * xx ** 2 - ((la + lb + lc) * (la * lb + la * lc + lb * lc) - 3 * la * lb * lc) * xx + la * lb * lc * (la + lb + lc), 0), xx)
    roots = sorted(F(int(sp.numer(r)), int(sp.denom(r))) for r in roots)
    dims = (6, 6, 2)
    cosine = {0: F(1), 1: F(1, 2), 2: F(-1, 2), 3: F(-1), 4: F(-1, 2), 5: F(1, 2)}
    torus = list(product(*(range(d) for d in dims)))
    wave = {p: (F(-1) if p[2] % 2 else F(1)) * cosine[(p[0] + p[1]) % 6] for p in torus}

    def d2t(field, p, axis):
        up = tuple((p[i] + (1 if i == axis else 0)) % dims[i] for i in range(3))
        dn = tuple((p[i] - (1 if i == axis else 0)) % dims[i] for i in range(3))
        return field[up] + field[dn] - 2 * field[p]

    lattice_ok = True
    for root in roots:
        null = mode_matrix(sp.Rational(root.numerator, root.denominator), 1, 1, 4, 0, -2).nullspace()
        lattice_ok = lattice_ok and len(null) == 1
        amp = [F(int(sp.numer(v)), int(sp.denom(v))) for v in null[0]]
        fields = [{p: amp[j] * wave[p] for p in torus} for j in range(4)]
        for p in torus:
            for j in range(3):
                pq = [ax for ax in range(3) if ax != j]
                lhs = root * (fields[pq[0]][p] + fields[pq[1]][p])                                 # comparator's kinetic term, K = wbar = 1: -X (-2)(A_p + A_q)/2
                rhs = -(d2t(fields[3], p, pq[0]) + d2t(fields[3], p, pq[1]) + d2t(fields[pq[0]], p, pq[1]) + d2t(fields[pq[1]], p, pq[0]))
                lattice_ok = lattice_ok and lhs == rhs
            lattice_ok = lattice_ok and sum((d2t(fields[j], p, ax) for j in range(3) for ax in range(3) if ax != j), ZERO) == 0
    speeds = [r / (la + lb + lc) for r in roots]
    free = (speeds[1] != 1) if not mut("speeds_are_direction_free") else (speeds[1] == 1)
    checks.check("E3", roots == [F(2, 3), F(4)] and lattice_ok and free, f"T4: on the 6x6x2 torus at the wave vector (pi/3, pi/3, pi), where (a, b, c) = (1, 1, 4), the two disturbances have X = 2/3 and 4; with their exact amplitudes the lattice equations of motion and the constraint hold at all 72 sites; normalized X/s values {speeds[0]} and {speeds[1]}, against 1 and 0 in a coordinate plane and 1/3 on a body diagonal")

    v0, sh, ph = sp.symbols("v0 sigma_hat pi_hat", real=True)
    reduced = sp.expand((2 * m1 - m2) * (m1 - (m1 + m2) * sh) * v0 ** 2 - 2 * (m1 - (2 * m1 + m2) * sh + 3 * (m1 + m2) * ph) * v0 + 4 * ph)
    scaled = sp.expand(formula.subs(xx, v0 * s) / (-16))
    consistent = sp.simplify(scaled - sp.expand(reduced.subs({sh: sig / s ** 2, ph: pi / s ** 3}) * s ** 4)) == 0
    poly = sp.Poly(reduced, sh, ph)
    conditions = [poly.coeff_monomial(mon) for mon in ((0, 0), (1, 0), (0, 1))]
    basis = sp.groebner(conditions, v0, m1, m2, order="lex")
    none = (list(basis.exprs) == [1]) if not mut("some_kinetic_term_is_isotropic") else (list(basis.exprs) != [1])
    checks.check("E4", consistent and none, "T4: a root X = v_0 s with v_0 the same in every direction would need the coefficients of 1, sigma/s^2 and pi/s^3 to vanish together; those three polynomials in (v_0, m_1, m_2) generate the whole ring (their reduced basis is 1): for NO kinetic term of the two-number family does any disturbance travel at a direction-free speed")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero, with one length for each axis at every site and one declared member of the ledger at second order; it reports what such lengths do at rest and in motion; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — the two orders of volume density x scalar curvature for three lengths and the kinetic density, by exact symbolic algebra; their restriction to equal lengths",
    "per_site: executed — the 108 static equations of a 5x5x5 box for a body at rest; the three equations for lam_j + u at all 125 sites of a 7x7x7 box for a point of hop energy; the constraint after an exact solve for the rates",
    "per_mode: executed — the mode determinant in symmetric functions; its roots in the coordinate planes and on the body diagonals; the two disturbances at (pi/3, pi/3, pi) with exact amplitudes, checked at all 72 sites of a 6x6x2 torus",
    "per_block: executed — the height of the tent against the size of the box; equal hop energies along the three axes; the failure of the equal-lengths law with hop energy; the reduced basis of the three isotropy conditions",
    "lattice_wide: T1 is a continuum identity for every metric diag(l_1^2, l_2^2, l_3^2); T2 holds for every box with held walls and every content at rest; T3 for every box and every distribution of hop energy, by linearity; T4 for every wave vector of a torus and every kinetic term M_1 sum (dlam_j/dt)^2 + M_2 sum (dlam_i/dt)(dlam_m/dt); all at second order in the fields, for the declared member only; that a site has three lengths, the member, K, M_1, M_2 and whether other variables (angles between bonds, sliding of sites) exist are not derived",
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
    print("scope: declared quadratic model; unique product-box static solution; point-source column response with structured-source exceptions; exact normalized dispersion polynomial and no constant normalized root for the stated onsite kinetic family")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
