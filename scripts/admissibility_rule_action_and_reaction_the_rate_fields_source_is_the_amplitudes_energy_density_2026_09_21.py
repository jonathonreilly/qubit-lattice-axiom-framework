#!/usr/bin/env python3
"""Exact controls for clocked energy derivatives, sufficient canonical ledger conservation,
a separately supplied reciprocal point-force model, and local zero-multiplier bond-law expansions.
No unique physical source or exact universal packet-force theorem is asserted.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)
PACKET_NEEDLE = "rho_psi(x) = |psi(x)|^2"

MUTATION_GATE = {
    "energy_density_without_the_clock": "B",
    "energy_does_not_have_weight_one": "B",
    "source_is_the_count": "C",
    "pulls_matched_for_any_source": "C",
    "field_energy_of_weight_two": "D",
    "second_order_depends_on_the_field_energy": "D",
    "fourth_order_is_universal_too": "D",
    "moving_body_sources_its_rest_energy": "E",
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
AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, G) else G(o)))

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


HALF_I = G(0, F(1, 2))
SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]


def solve(a, b):
    """Solve a x = b exactly (free variables set to zero); None if inconsistent."""
    n, m = len(a), len(a[0])
    rows = [[F(c) for c in a[i]] + [F(b[i])] for i in range(n)]
    pivots = []
    rk = 0
    for col in range(m):
        piv = next((i for i in range(rk, n) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][col]
        rows[rk] = [c / pv for c in rows[rk]]
        for i in range(n):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [x - fac * y for x, y in zip(rows[i], rows[rk])]
        pivots.append(col)
        rk += 1
    if any(all(c == 0 for c in r[:-1]) and r[-1] != 0 for r in rows):
        return None
    x = [ZERO] * m
    for i, col in enumerate(pivots):
        x[col] = rows[i][-1]
    return x


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, packet = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")
    checks.check("A3", PACKET_NEEDLE in packet, "weak-field packet on main: its second supplied piece is the source read off the amplitude as rho = |psi|^2")


# ============================================================================================ family B
def walk_on_torus(side, phi, rest=None):
    """Matrix of H_w = phi H phi on a torus; H = sum_j sigma_j D_j, plus an on-site rest-energy term m sigma_1 when `rest` is given
    (a generic Hermitian onsite perturbation here; not an anticommuting three-dimensional mass)."""
    sites = list(product(range(side), repeat=3))
    idx = {(x, s): 2 * i + s for i, x in enumerate(sites) for s in range(2)}
    n = 2 * len(sites)
    h = [[G(0)] * n for _ in range(n)]
    for x in sites:
        for j, e in enumerate(AXES):
            for sign in (+1, -1):
                tgt = tuple((x[i] + sign * e[i]) % side for i in range(3))
                for s in range(2):
                    for s2 in range(2):
                        h[idx[(tgt, s2)]][idx[(x, s)]] = h[idx[(tgt, s2)]][idx[(x, s)]] + SIG[j][s2][s] * HALF_I * (F(sign) * phi[x] * phi[tgt])
        if rest is not None:
            for s in range(2):
                for s2 in range(2):
                    h[idx[(x, s2)]][idx[(x, s)]] = h[idx[(x, s2)]][idx[(x, s)]] + SIG[0][s2][s] * (rest * phi[x] * phi[x])
    return sites, idx, n, h


def expectation(h, chi):
    n = len(chi)
    tot = G(0)
    for a in range(n):
        row = G(0)
        for b in range(n):
            row = row + h[a][b] * chi[b]
        tot = tot + chi[a].conj() * row
    return tot


def energy_density(h, chi, sites, idx):
    n = len(chi)
    hchi = [sum((h[a][b] * chi[b] for b in range(n)), G(0)) for a in range(n)]
    return {x: sum(((chi[idx[(x, s)]].conj() * hchi[idx[(x, s)]]).re for s in range(2)), ZERO) for x in sites}


def family_b(checks: Checks) -> None:
    side = 3
    phi = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in product(range(side), repeat=3)}
    sites, idx, n, h = walk_on_torus(side, phi, rest=F(2, 5))
    chi = [G(F((5 * a + 3) % 7 - 3, 4), F((3 * a + 1) % 5 - 2, 3)) for a in range(n)]
    total = expectation(h, chi)
    e = energy_density(h, chi, sites, idx)
    if mut("energy_does_not_have_weight_one"):
        e = {x: v * F(9, 10) for x, v in e.items()}
    checks.check("B1", total.im == 0 and sum(e.values(), ZERO) == total.re, f"T1: on the 3x3x3 torus with a rational rate field and a rational amplitude, e_x = Re chi_x^dagger (H_w chi)_x sums to <H_w> = {total.re}: the amplitude's energy has weight one in the rates, and e is its density")
    # e_x is the derivative of <H_w> with respect to u_x at fixed amplitude: <H_w> is a quadratic form in phi and d/du_x = (phi_x/2) d/dphi_x
    ok = True
    for x in sites[:9]:
        vals = []
        for shift in (+1, -1):
            phi2 = dict(phi)
            phi2[x] = phi[x] + shift
            vals.append(expectation(walk_on_torus(side, phi2, rest=F(2, 5))[3], chi).re)
        dq = (vals[0] - vals[1]) / 2                                          # exact for a quadratic form
        want = e[x] if not mut("energy_density_without_the_clock") else energy_density(walk_on_torus(side, {y: ONE for y in phi}, rest=F(2, 5))[3], chi, sites, idx)[x]
        ok = ok and phi[x] * dq / 2 == want
    checks.check("B2", ok, "T1: e_x = d<H_w>/du_x at fixed amplitude (exact: <H_w> is a quadratic form in phi = sqrt(w), and d/du_x = (phi_x/2) d/dphi_x), checked at nine sites: along the supplied canonical chi evolution d<H_w>/dt = sum_x e_x du_x/dt, the amplitude's own flow contributing nothing because H_w is hermitian")

    velocities=[F(2),F(-3),F(1)];density=[F(5),F(7),F(11)];source=[F(4),F(8),F(9)];mu=F(13)
    gradf=[-a+mu for a in source]
    actual=sum((a+b)*v for a,b,v in zip(density,gradf,velocities))
    predicted=sum((a-b)*v for a,b,v in zip(density,source,velocities))
    ledger_mu=(sum(density)+F(6))/3
    checks.check("B3",sum(velocities)==0 and actual==predicted==7 and ledger_mu-sum(density)/3==2,"T2: ledger defect equals sum(e-s)dotu; total-ledger multiplier exceeds mean amplitude energy by F/N in an explicit rational example")


# ============================================================================================ family C
def torus_potential(side, source):
    """Zero-mean solution of (u_x - average of the six neighbours) = source_x - mean(source) on a torus."""
    sites = list(product(range(side), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    n = len(sites)
    a = [[ZERO] * n for _ in range(n)]
    for x in sites:
        a[idx[x]][idx[x]] += 1
        for e in E6:
            y = tuple((x[i] + e[i]) % side for i in range(3))
            a[idx[x]][idx[y]] -= F(1, 6)
    mean = sum(source.get(x, ZERO) for x in sites) / n
    sol = solve(a, [source.get(x, ZERO) - mean for x in sites])
    m = sum(sol) / n
    return {x: sol[idx[x]] - m for x in sites}


def family_c(checks: Checks) -> None:
    side = 4
    bodies = [((0, 0, 0), F(2)), ((2, 1, 0), F(5)), ((1, 3, 2), F(3, 2))]          # positions and energies
    gamma = F(1, 10)

    def total_pull(strengths):
        fields = [torus_potential(side, {pos: -gamma * s}) for (pos, _), s in zip(bodies, strengths)]
        tot = [ZERO, ZERO, ZERO]
        for a, (pos_a, en_a) in enumerate(bodies):
            for b in range(len(bodies)):
                if a == b:
                    continue
                for j, ax in enumerate(AXES):
                    up = tuple((pos_a[i] + ax[i]) % side for i in range(3))
                    dn = tuple((pos_a[i] - ax[i]) % side for i in range(3))
                    tot[j] += -en_a * (fields[b][up] - fields[b][dn]) / 2
        return tot

    matched = total_pull([en * F(7, 3) for _, en in bodies])
    count = total_pull([ONE for _ in bodies])
    if mut("source_is_the_count"):
        matched = count
    if mut("pulls_matched_for_any_source"):
        count = [ZERO, ZERO, ZERO]
    checks.check("C1", matched == [ZERO, ZERO, ZERO] and count != [ZERO, ZERO, ZERO], f"T3: three bodies of energies 2, 5, 3/2 on the 4x4x4 torus, each pulled by -E grad u in the others' fields (central differences; fields from block 53's operator with the zero mode removed): with source strengths proportional to the energies the pulls sum to zero exactly; with every body sourcing alike (a count) they sum to {tuple(str(v) for v in count)}: this supplied point-force model has nonzero summed force for the specified count-source example")
    # the pair identity behind it: pull on A from B plus pull on B from A = -gamma (E_A S_B - E_B S_A) x (difference of the potential)
    (pa, ea), (pb, eb) = bodies[0], bodies[1]
    g0 = torus_potential(side, {pb: ONE})
    g0a = torus_potential(side, {pa: ONE})
    ok = True
    for sa, sb in ((F(2), F(5)), (F(1), F(1)), (F(3), F(1, 2))):
        for j, ax in enumerate(AXES):
            up_a = tuple((pa[i] + ax[i]) % side for i in range(3)); dn_a = tuple((pa[i] - ax[i]) % side for i in range(3))
            up_b = tuple((pb[i] + ax[i]) % side for i in range(3)); dn_b = tuple((pb[i] - ax[i]) % side for i in range(3))
            pull_a = -ea * (-gamma * sb) * (g0[up_a] - g0[dn_a]) / 2
            pull_b = -eb * (-gamma * sa) * (g0a[up_b] - g0a[dn_b]) / 2
            grad = (g0[up_a] - g0[dn_a]) / 2
            ok = ok and pull_a + pull_b == gamma * (ea * sb - eb * sa) * grad
    checks.check("C2", ok, "T3: for a pair, pull on A plus pull on B = gamma (E_A S_B - E_B S_A) x (the lattice potential's difference across A): it vanishes for every separation iff S_A/E_A = S_B/E_B, provided a separation with nonzero central gradient exists and both energies are nonzero")


# ============================================================================================ family D
class Series:
    """A power series in one variable, truncated after degree ORDER, with exact coefficients."""

    ORDER = 4

    def __init__(self, coeffs):
        c = [F(v) for v in coeffs][: Series.ORDER + 1]
        self.c = c + [ZERO] * (Series.ORDER + 1 - len(c))

    @staticmethod
    def const(v):
        return Series([v])

    def __add__(self, o):
        o = o if isinstance(o, Series) else Series.const(o)
        return Series([a + b for a, b in zip(self.c, o.c)])

    __radd__ = __add__

    def __neg__(self):
        return Series([-a for a in self.c])

    def __sub__(self, o):
        return self + (-(o if isinstance(o, Series) else Series.const(o)))

    def __rsub__(self, o):
        return (-self) + o

    def __mul__(self, o):
        o = o if isinstance(o, Series) else Series.const(o)
        out = [ZERO] * (Series.ORDER + 1)
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                if i + j <= Series.ORDER:
                    out[i + j] += a * b
        return Series(out)

    __rmul__ = __mul__

    def inverse(self):
        assert self.c[0] != 0
        out = [ONE / self.c[0]] + [ZERO] * Series.ORDER
        for k in range(1, Series.ORDER + 1):
            out[k] = -sum((self.c[i] * out[k - i] for i in range(1, k + 1)), ZERO) / self.c[0]
        return Series(out)

    def __truediv__(self, o):
        o = o if isinstance(o, Series) else Series.const(o)
        return self * o.inverse()


def law_first(px, neighbours):
    """d/d(phi_x) of F_1 = sum over bonds (phi_x - phi_y)^2, divided by 2."""
    return sum(((px - py) for py in neighbours), Series.const(0))


def law_second(px, neighbours):
    """d/dA of F_2 = sum over bonds (A - B)^2/(A + B), A = phi_x^2, B = phi_y^2: (A - B)(A + 3B)/(A + B)^2."""
    a = px * px
    tot = Series.const(0)
    for py in neighbours:
        b = py * py
        tot = tot + (a - b) * (a + 3 * b) / ((a + b) * (a + b))
    return tot


def solve_series(law, neighbours):
    """Solve law(phi_x, neighbours) = 0 for phi_x as a series in the bump.  The slope of the law at the uniform point is found exactly (the
    first-order coefficient of the law along phi_x = 1 + b with every neighbour at 1); each step with that slope fixes one more order exactly."""
    b = Series([0, 1])
    slope = law(Series.const(1) + b, [Series.const(1)] * len(neighbours)).c[1]
    px = Series.const(1)
    for _ in range(Series.ORDER + 2):
        px = px - law(px, neighbours) * (ONE / slope)
    assert all(c == 0 for c in law(px, neighbours).c)
    return px


def family_d(checks: Checks) -> None:
    side = 3
    phi = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in product(range(side), repeat=3)}
    sites = list(phi)
    bonds = [(x, tuple((x[i] + e[i]) % side for i in range(3))) for x in sites for e in AXES]

    def f_one(p):
        return sum(((p[x] - p[y]) ** 2 for x, y in bonds), ZERO)

    def f_two(p):
        return sum(((p[x] ** 2 - p[y] ** 2) ** 2 / (p[x] ** 2 + p[y] ** 2) for x, y in bonds), ZERO)

    def f_weight_two(p):
        return sum(((p[x] ** 2 - p[y] ** 2) ** 2 for x, y in bonds), ZERO)

    t, root_t = F(49, 9), F(7, 3)
    scaled = {x: root_t * v for x, v in phi.items()}
    functionals = [f_one, f_two] if not mut("field_energy_of_weight_two") else [f_one, f_weight_two]
    weight_one = all(fn(scaled) == t * fn(phi) for fn in functionals)
    checks.check("D1", weight_one, "T4: the bond energies sum (phi_x - phi_y)^2 and sum (w_x - w_y)^2/(w_x + w_y) have weight one under w -> t w, as the amplitude's energy has: a ledger made of them keeps its form when the unit of rate is changed (a field energy quadratic in u, or of weight two, does not)")
    # weight one means sum_x dF/du_x = F: by exact one-sided scaling of all phi (degree two in phi): F((1+s) phi) = (1+s)^2 F(phi)
    euler = all(fn({x: v * F(3, 2) for x, v in phi.items()}) == F(9, 4) * fn(phi) for fn in (f_one, f_two))
    checks.check("D2", euler and f_one(phi) > 0 and f_two(phi) > 0, "T4: both energies are homogeneous of degree two in phi, so sum_x dF/du_x = F, and the same holds for <H_w> (B1): sum_x d(ledger)/du_x = ledger.  With positive energies the ledger cannot be stationary in every u_x; the unit of rate is not a variable, the multiplier is mu = ledger per site, and the source enters as e_x - mu: the total-ledger multiplier differs from mean amplitude energy when field energy is nonzero")
    # the law in empty space, bump test: two opposite neighbours phi = 1 + a and 1/(1 + a) (u = +-2 log(1 + a)), the other four at 1
    a = Series([0, 1])
    neighbours = [Series.const(1) + a, (Series.const(1) + a).inverse()] + [Series.const(1)] * 4
    first = solve_series(law_first, neighbours)
    second = solve_series(law_second, neighbours)
    mean_phi = sum(neighbours, Series.const(0)) * F(1, 6)
    second_order = (first.c[2], second.c[2])
    if mut("second_order_depends_on_the_field_energy"):
        second_order = (first.c[2], second.c[2] + F(1, 100))
    fourth = (first.c[4], second.c[4])
    if mut("fourth_order_is_universal_too"):
        fourth = (first.c[4], first.c[4])
    ok = first.c[:5] == mean_phi.c[:5] and first.c[1] == 0 and second.c[1] == 0 and second_order == (F(1, 6), F(1, 6)) and first.c[3] == second.c[3] and fourth[0] != fourth[1]
    checks.check("D3", ok, f"T4: the empty-space law of the first energy is phi_x = average of phi over the neighbours exactly (the averaging law for sqrt(w): block 53's power mean of order 1/2); the second energy gives the same phi_x through the second order of the bump (coefficients {second.c[2]} and {second.c[3]} at the second and third order for both) and differs at the fourth ({first.c[4]} against {second.c[4]}): these selected local zero-multiplier homogeneous bond laws agree through second order and differ at fourth")
    # weak-field form of dF_1/du_x: (phi_x/2) * 2 * sum_y (phi_x - phi_y) -> wbar * (1/2) * sum_y (u_x - u_y) at first order, that is 3 wbar (u_x - average)
    eps = Series([0, 1])
    base = F(5, 3)
    ux = F(2, 7)
    uys = [F(1, 3), -F(1, 5), F(0), F(1, 2), -F(2, 3), F(1, 11)]
    px = base * (Series.const(1) + eps * (ux / 2))
    pys = [base * (Series.const(1) + eps * (uy / 2)) for uy in uys]
    grad = px * sum(((px - py) for py in pys), Series.const(0))
    want = base * base * 3 * (ux - sum(uys) / 6)
    checks.check("D4", grad.c[0] == 0 and grad.c[1] == want, "T4: at weak field dF_1/du_x = 3 wbar (u_x - average of u over the six neighbours): block 53's operator, with the ambient rate wbar multiplying it, so that the law reads (u_x - average) = -(gamma/(6*wbar))(e_x - mu) for the normalized F=(2/gamma)F_1: the coupling is a pure number and the source is the energy density counted in ambient ticks")


# ============================================================================================ family E
def ring_walk(length, phi, m):
    """The reduced walk of block 54 on a ring along the third axis: H = m sigma_1 + sigma_3 D, H_w = phi H phi."""
    ring = [(0, 0, z) for z in range(length)]
    ridx = {(x, s): 2 * i + s for i, x in enumerate(ring) for s in range(2)}
    hr = [[G(0)] * (2 * length) for _ in range(2 * length)]
    for x in ring:
        for sign in (+1, -1):
            tgt = (0, 0, (x[2] + sign) % length)
            for s in range(2):
                for s2 in range(2):
                    hr[ridx[(tgt, s2)]][ridx[(x, s)]] = hr[ridx[(tgt, s2)]][ridx[(x, s)]] + SIG[2][s2][s] * HALF_I * (F(sign) * phi[x] * phi[tgt])
        for s in range(2):
            for s2 in range(2):
                hr[ridx[(x, s2)]][ridx[(x, s)]] = hr[ridx[(x, s2)]][ridx[(x, s)]] + SIG[0][s2][s] * (m * phi[x] * phi[x])
    return ring, ridx, hr


def family_e(checks: Checks) -> None:
    # a body at rest on the reduced walk, in a rational rate field: a real envelope times the rest-energy content (1, 1)
    m = F(2, 5)
    length = 7
    phi = {(0, 0, z): ONE + F((3 * z * z + 2 * z) % 11, 13) for z in range(length)}
    ring, ridx, hr = ring_walk(length, phi, m)
    env = {x: ONE + F((2 * x[2] * x[2] + x[2]) % 5, 7) for x in ring}
    chi = [G(0)] * (2 * length)
    for x in ring:
        chi[ridx[(x, 0)]] = G(env[x])
        chi[ridx[(x, 1)]] = G(env[x])
    e = energy_density(hr, chi, ring, ridx)
    ok_rest = all(e[x] == m * phi[x] ** 2 * (2 * env[x] ** 2) for x in ring)
    checks.check("E1", ok_rest, "T2: for a body at rest on the reduced walk (a real envelope with the rest-energy content) e_x = m w_x |chi_x|^2 at every site of a ring with a rational rate field, exactly: the weak-field packet's density |psi|^2 is the energy density of a body at rest per unit rest energy and local rate")
    # a moving body: a plane wave of wave vector pi/2 on a ring of four sites, uniform rate; m = 3/4 so that eps = 5/4
    m2 = F(3, 4)
    ring, ridx, hr = ring_walk(4, {(0, 0, z): ONE for z in range(4)}, m2)
    # eigenvector of m sigma_1 + sigma_3 with eigenvalue 5/4: (m, 5/4 - 1) = (3/4, 1/4) ~ (3, 1); plane wave exp(i pi z / 2) = i^z
    powers = [G(1), G(0, 1), G(-1), G(0, -1)]
    chi_r = [G(0)] * 8
    for x in ring:
        chi_r[ridx[(x, 0)]] = powers[x[2]] * 3
        chi_r[ridx[(x, 1)]] = powers[x[2]] * 1
    er = energy_density(hr, chi_r, ring, ridx)
    ratio = {er[x] / 10 for x in ring}                                         # |chi_x|^2 = 10
    want = {F(5, 4)} if not mut("moving_body_sources_its_rest_energy") else {m2}
    checks.check("E2", ratio == want, f"T2: for a moving body (wave vector pi/2, rest energy 3/4, energy 5/4) e_x = (5/4) |chi_x|^2: the source is the energy, not the rest energy and not the probability ({sorted(ratio)[0]} per unit probability)")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates and canonical amplitudes; it proves energy-derivative identities and a sufficient variational conservation law, with a separately supplied reciprocal point-force model; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Rindler", "Bloch", "Berry", "Hesse", "Schrodinger", "Liouville", "Lorentz", "Hartree", "Hellmann", "Feynman", "Noether", "Lagrange", "Mach", "Bondi", "Penrose", "Diosi", "Moller", "Rosenfeld")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Newton)", 1)
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
    "per_element: executed — the energy density of a rational amplitude at each of the 27 sites of a torus, and its derivative with respect to the local rate at nine of them",
    "per_site: executed — an instantaneous real-envelope state at every site of a ring with a rational rate field: e_x = m w_x |chi_x|^2; a moving body on a ring of four sites: e_x = (5/4) |chi_x|^2",
    "per_mode: executed — the bump test of the empty-space law for two field energies of weight one, as exact power series through the fourth order",
    "per_block: executed — three bodies on the 4x4x4 torus with exact lattice potentials: total pull zero for sources proportional to the energies, non-zero for a count; the pair identity for three choices of strengths",
    "lattice_wide: T1 holds for every amplitude, generator and positive rate field; T2 for every static law and ledger of the stated form; T3 for point bodies in the weak field of block 53's operator on any torus; T4 for every nearest-neighbour field energy of weight one; that the pair keeps a ledger at all, the static form of the law, the coupling and the function f are not derived; whether records and amplitudes source alike is not settled here",
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
    print("scope: supplied canonical dynamics; clocked energy derivatives and sufficient constrained ledger conservation; conditional point-force reciprocity; distinct local zero-multiplier second-order bond-law expansion")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
