#!/usr/bin/env python3
"""Exact checks: the two-step content's books in the member's placement - the energy averaged over the body diagonals
flows exactly as the two-step momentum carried to the bonds; that momentum is conserved with block 120's stress; the coin-energy
current of the bonds is conserved with the transposed stress and has the same divergence; so the symmetric momentum
P^B = (P'' + Q)/2 is conserved with the symmetric stress the member sees, and a bond shift coupled to it keeps every constraint
of the member iff alpha = K/4 (the supervisor's own derivation; blocks 54, 62, 69, 73, 74 and 101 as landed; blocks 120, 124
and 135 placed; not adopted).

B (T1): the energy law on the 5^3, 6^3 and 9^3 tori, carried to Z^3 by its support radius.
C (T2): the momentum laws and the symmetric books.
D (T3): what fails.
E (T4): the member with a lapse and a bond shift.
Exact rational and Gaussian-rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THREE_RESPONSES_EIGHT_SPECIES_THE_FRAMES_SITE_STRESS_HAS_THE_WRONG_SIGN_IN_SHEAR_FOR_SIX_SPECIES_ONLY_THE_TWO_STEP_CURRENT_SERVES_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_two_step_content_keeps_symmetric_books_where_the_member_keeps_its_fields_and_a_bond_shift_keeps_every_constraint_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "energy_current_halved": "B",
    "symmetrized_momentum_dropped": "C",
    "control_passes_forged": "D",
    "light_cone_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its currents and their placements, the member, its kinetic term and the source link are supplied; the memo does not define a time metric)")


# ============================================================================================ exact Gaussian-rational sparse operators on the L^3 torus
GZ = (Fr(0), Fr(0))


def gq(re, im=0):
    return (Fr(re), Fr(im))


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


class SM:
    """sparse matrix over Q(i): dict row -> dict col -> (re, im)"""

    def __init__(self, d=None):
        self.d = d if d is not None else {}

    def add_entry(self, r, c, v):
        row = self.d.setdefault(r, {})
        nv = gadd(row.get(c, GZ), v)
        if nv == GZ:
            row.pop(c, None)
            if not row:
                self.d.pop(r)
        else:
            row[c] = nv

    def __add__(self, o):
        out = SM({r: dict(row) for r, row in self.d.items()})
        for r, row in o.d.items():
            for c, v in row.items():
                out.add_entry(r, c, v)
        return out

    def scale(self, s):
        return SM({r: {c: gmul(s, v) for c, v in row.items()} for r, row in self.d.items()})

    def __sub__(self, o):
        return self + o.scale(gq(-1))

    def __mul__(self, o):
        out = SM()
        for r, row in self.d.items():
            acc = {}
            for k, v in row.items():
                orow = o.d.get(k)
                if not orow:
                    continue
                for c, w in orow.items():
                    acc[c] = gadd(acc.get(c, GZ), gmul(v, w))
            acc = {c: v for c, v in acc.items() if v != GZ}
            if acc:
                out.d[r] = acc
        return out

    def dag(self):
        out = SM()
        for r, row in self.d.items():
            for c, v in row.items():
                out.add_entry(c, r, (v[0], -v[1]))
        return out

    def is_zero(self):
        return not self.d


SIGC = ({(0, 1): gq(1), (1, 0): gq(1)}, {(0, 1): gq(0, -1), (1, 0): gq(0, 1)}, {(0, 0): gq(1), (1, 1): gq(-1)})


class Torus:
    """block 54's walk H = sum_a sigma_a S_a on the L^3 torus, with S_a = (T_a - T_a^-1)/(2i), C_a = (T_a + T_a^-1)/2 and
    block 69's two-step momentum P_j = S_j C_j; state index 2 n(x) + coin."""

    def __init__(self, L):
        self.L = L
        self.sites = list(product(range(L), repeat=3))
        self.T = [self.pos_op([(x, self.sh(x, a), gq(1)) for x in self.sites]) for a in range(3)]
        self.S = [(self.T[a] - self.T[a].dag()).scale(gq(0, Fr(-1, 2))) for a in range(3)]
        self.C = [(self.T[a] + self.T[a].dag()).scale(gq(Fr(1, 2))) for a in range(3)]
        self.H = SM()
        for a in range(3):
            for x in self.sites:
                for d_ in (1, -1):
                    self.H = self.H + self.coin_op(SIGC[a], x, self.sh(x, a, d_), gq(0, Fr(-d_, 2)))
        self.P = [self.S[j] * self.C[j] for j in range(3)]
        self.kc = {}

    def n(self, x):
        L = self.L
        return (x[0] % L) + L * (x[1] % L) + L * L * (x[2] % L)

    @staticmethod
    def sh(x, a, s=1):
        y = list(x)
        y[a] += s
        return tuple(y)

    def pos_op(self, entries):
        m = SM()
        for x, y, cf in entries:
            for c in (0, 1):
                m.add_entry(2 * self.n(x) + c, 2 * self.n(y) + c, cf)
        return m

    def coin_op(self, coin, x, y, cf=None):
        cf = cf if cf is not None else gq(1)
        m = SM()
        for (c, d), v in coin.items():
            m.add_entry(2 * self.n(x) + c, 2 * self.n(y) + d, gmul(cf, v))
        return m

    def energy(self, x):
        """e(x) = Re psi^dag(x) (H psi)(x)"""
        pr = self.pos_op([(x, x, gq(1))])
        return (pr * self.H + self.H * pr).scale(gq(Fr(1, 2)))

    def energy_avg(self, x):
        """e'(x) = (C_1 C_2 C_3 e)(x): the energy density averaged over the eight body-diagonal neighbours"""
        out = SM()
        for sg in product((1, -1), repeat=3):
            out = out + self.energy((x[0] + sg[0], x[1] + sg[1], x[2] + sg[2]))
        return out.scale(gq(Fr(1, 8)))

    def kcur(self, a, j, x):
        """block 69's reach-three current on the bond x -> x + e_a: K_a^j = (1/2) Re[psi^dag(x+e_a) sigma_a (P_j psi)(x) + (P_j psi)^dag(x+e_a) sigma_a psi(x)]"""
        key = (a, j, tuple(v % self.L for v in x))
        if key not in self.kc:
            A = self.coin_op(SIGC[a], self.sh(x, a), x)
            Ad = A.dag()
            self.kc[key] = (A * self.P[j] + self.P[j] * A + self.P[j] * Ad + Ad * self.P[j]).scale(gq(Fr(1, 4)))
        return self.kc[key]

    def theta_two_step(self, i, j, y, transverse=True):
        """block 120's phi-realisation read as a source: Theta_ij(y) = (phi_j^T K_i^j)(y), phi_j^T = (1/2)(1 + T_j) prod_{l != j} C_l"""
        out = SM()
        ls = [l for l in range(3) if l != j]
        shifts = list(product((1, -1), repeat=2)) if transverse else [None]
        for s12 in shifts:
            yy = y if s12 is None else self.sh(self.sh(y, ls[0], s12[0]), ls[1], s12[1])
            out = out + self.kcur(i, j, yy) + self.kcur(i, j, self.sh(yy, j))
        return out.scale(gq(Fr(1, 8) if transverse else Fr(1, 2)))

    def theta_site(self, i, j, y):
        """block 62's site stress Theta_i^j(y) = Re psi^dag(y) sigma_i (S_j psi)(y)"""
        pr = self.coin_op(SIGC[i], y, y)
        return (pr * self.S[j] + self.S[j] * pr.dag()).scale(gq(Fr(1, 2)))

    def ddiv(self, thfun, x):
        """sum_ij dbar_i dbar_j Theta_ij (x), dbar_i f(x) = f(x) - f(x - e_i): the member's double divergence in site convention"""
        out = SM()
        for i in range(3):
            for j in range(3):
                xi = self.sh(x, i, -1)
                xj = self.sh(x, j, -1)
                out = out + thfun(i, j, x) - thfun(i, j, xi) - thfun(i, j, xj) + thfun(i, j, self.sh(xi, j, -1))
        return out

    def second_derivative(self, op):
        """d^2/dt^2 of <op> = -[H, [H, op]]"""
        c1 = self.H * op - op * self.H
        return (self.H * c1 - c1 * self.H).scale(gq(-1))

    def ddt(self, op):
        """d/dt of <op> = <i[H, op]>"""
        return (self.H * op - op * self.H).scale(gq(0, 1))

    def mom_site(self, j, y, one_step=False):
        """pi_j(y) = Re psi^dag(y) (P_j psi)(y) (two-step), or Re psi^dag(y) (S_j psi)(y) (one-step)"""
        pr = self.pos_op([(y, y, gq(1))])
        mom = self.S[j] if one_step else self.P[j]
        return (pr * mom + mom * pr).scale(gq(Fr(1, 2)))

    def mom_bond(self, j, y, averaged=True, one_step=False):
        """P''_j(y) = (phi_j^T pi_j)(y): the momentum carried to the bond y -> y + e_j by block 120's average"""
        if not averaged:
            return self.mom_site(j, y, one_step)
        out = SM()
        ls = [l for l in range(3) if l != j]
        for s12 in product((1, -1), repeat=2):
            yy = self.sh(self.sh(y, ls[0], s12[0]), ls[1], s12[1])
            out = out + self.mom_site(j, yy, one_step) + self.mom_site(j, self.sh(yy, j), one_step)
        return out.scale(gq(Fr(1, 8)))

    def div_bond(self, fun, x):
        """sum_j dbar_j F_j (x) for a bond field F_j"""
        out = SM()
        for j in range(3):
            out = out + fun(j, x) - fun(j, self.sh(x, j, -1))
        return out

    def q_bond(self, j, x):
        """Q^b_j(x) = (1/2) Re[psi^dag(x+e_j) sigma_j (H psi)(x) + (H psi)^dag(x+e_j) sigma_j psi(x)] on the bond x -> x + e_j"""
        A = self.coin_op(SIGC[j], self.sh(x, j), x)
        Ad = A.dag()
        return (A * self.H + self.H * A + self.H * Ad + Ad * self.H).scale(gq(Fr(1, 4)))

    def q_avg(self, j, x):
        """Q_j = C_1 C_2 C_3 Q^b_j: the coin-energy current of the bond, averaged over the eight body diagonals"""
        out = SM()
        for sg in product((1, -1), repeat=3):
            out = out + self.q_bond(j, (x[0] + sg[0], x[1] + sg[1], x[2] + sg[2]))
        return out.scale(gq(Fr(1, 8)))

    def mom_sym(self, j, x):
        """P^B_j = (P''_j + Q_j)/2"""
        return (self.mom_bond(j, x) + self.q_avg(j, x)).scale(gq(Fr(1, 2)))

    def theta_sym(self, i, j, y):
        return (self.theta_two_step(i, j, y) + self.theta_two_step(j, i, y)).scale(gq(Fr(1, 2)))

    def radius(self, m):
        L = self.L
        best = 0
        for r, row in m.d.items():
            for idx in [r] + list(row):
                nn = idx // 2
                x = (nn % L, (nn // L) % L, nn // (L * L))
                best = max(best, max(min(v, L - v) for v in x))
        return best






# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the energy law de'/dt = - sum_j dbar_j P''_j, exactly, for every state."""
    ok = True
    radii = []
    for L, xs in ((5, ((0, 0, 0), (2, 1, 3))), (6, ((0, 0, 0),)), (9, ((0, 0, 0),))):
        tor = Torus(L)
        for x in xs:
            lhs = tor.ddt(tor.energy_avg(x))
            factor = gq(Fr(-1, 2)) if mut("energy_current_halved") else gq(-1)
            rhs = tor.div_bond(lambda j, y: tor.mom_bond(j, y), x).scale(factor)
            ok = ok and (lhs - rhs).is_zero() and not lhs.is_zero()
            if L == 9:
                radii = [tor.radius(lhs), tor.radius(rhs)]
    ok_transfer = len(radii) == 2 and max(radii) <= 4
    checks.check("B1", ok and ok_transfer,
                 "T1: on the 5^3, 6^3 and 9^3 tori, as exact operators over Q(i), i[H, e'(x)] = - sum_j dbar_j P''_j(x), with e' = C_1 C_2 C_3 e and P''_j = phi_j^T pi_j the two-step momentum density pi_j = Re psi^dag P_j psi carried to the bond x -> x + e_j by block 120's average; both sides nonzero, support radius %s <= 4 on 9^3, so the law holds on Z^3: the energy current is exactly the two-step momentum (wbar^2 times it at a rate wbar)" % max(radii or [0]))


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the momentum laws, and the symmetric books P^B = (P'' + Q)/2 with the symmetric stress."""
    ok = True
    radii = []
    for L, xs in ((5, ((0, 0, 0), (2, 1, 3))), (6, ((0, 0, 0),)), (9, ((0, 0, 0),))):
        tor = Torus(L)
        for x in xs:
            for j in range(3):
                d_p = tor.ddt(tor.mom_bond(j, x))
                ok = ok and (d_p + tor.div_bond(lambda i, y: tor.theta_two_step(i, j, y), x)).is_zero()
                d_q = tor.ddt(tor.q_avg(j, x))
                ok = ok and (d_q + tor.div_bond(lambda i, y: tor.theta_two_step(j, i, y), x)).is_zero()
                mom = tor.mom_bond(j, x) if mut("symmetrized_momentum_dropped") else tor.mom_sym(j, x)
                d_b = tor.ddt(mom)
                rhs_b = tor.div_bond(lambda i, y: tor.theta_sym(i, j, y), x).scale(gq(-1))
                ok = ok and (d_b - rhs_b).is_zero() and not d_b.is_zero()
                if L == 9:
                    radii += [tor.radius(d_b), tor.radius(rhs_b)]
            dq = tor.div_bond(lambda j, y: tor.q_avg(j, y), x)
            dp = tor.div_bond(lambda j, y: tor.mom_bond(j, y), x)
            ok = ok and (dq - dp).is_zero() and not all((tor.q_avg(j, x) - tor.mom_bond(j, x)).is_zero() for j in range(3))
    ok_transfer = len(radii) == 6 and max(radii) <= 4
    checks.check("C1", ok and ok_transfer,
                 "T2: on the same tori, for j = 1, 2, 3: i[H, P''_j] = - sum_i dbar_i Theta_ij (block 69's law carried by block 120's average), and the bond's coin-energy current Q_j = C_1 C_2 C_3 (1/2) Re[psi^dag(x+e_j) sigma_j (H psi)(x) + (H psi)^dag(x+e_j) sigma_j psi(x)] obeys i[H, Q_j] = - sum_i dbar_i Theta_ji with sum_j dbar_j Q_j = sum_j dbar_j P''_j but Q != P''; so P^B = (P'' + Q)/2 obeys i[H, P^B_j] = - sum_i dbar_i Theta^sym_ij with the symmetric stress the member sees, and e' still has current P^B; support radius %s <= 4 on 9^3, so the laws hold on Z^3" % max(radii or [0]))


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: what fails."""
    tor = Torus(5)
    x = (0, 0, 0)
    de_avg = tor.ddt(tor.energy_avg(x))
    de_site = tor.ddt(tor.energy(x))
    fails = []
    fails.append(not (de_site + tor.div_bond(lambda j, y: tor.mom_bond(j, y), x)).is_zero())
    fails.append(not (de_avg + tor.div_bond(lambda j, y: tor.mom_bond(j, y, averaged=False), x)).is_zero())
    fails.append(not (de_avg + tor.div_bond(lambda j, y: tor.mom_bond(j, y, one_step=True), x)).is_zero())
    for j in range(3):
        dp = tor.ddt(tor.mom_bond(j, x))
        fails.append(not (dp + tor.div_bond(lambda i, y: tor.theta_sym(i, j, y), x)).is_zero())
        fails.append(not (dp + tor.div_bond(lambda i, y: tor.theta_site(i, j, y), x)).is_zero())
    if mut("control_passes_forged"):
        fails[0] = (de_site + tor.div_bond(lambda j, y: tor.mom_bond(j, y), x)).is_zero()
    checks.check("D1", all(fails) and len(fails) == 9,
                 "T3: on the 5^3 torus the energy law fails with the site energy e, with the unaveraged two-step density, and with the one-step momentum carried by the same average; for each j the canonical momentum P''_j is not conserved with the symmetric stress (the antisymmetric part, the torque on the coin, has a nonzero divergence), nor with block 62's site stress (operators nonzero)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: with a bond shift coupled to P^B, the member's lapse and shift constraints are kept iff alpha = K/4."""
    t = sp.symbols("t")
    al, kk, wb, p = sp.symbols("alpha K wbar p", positive=True)
    phi, a, b, cx, cy, xi, u, nx, ny, nz = [sp.Function(nm)(t) for nm in ("phi", "a", "b", "cx", "cy", "xi", "u", "Nx", "Ny", "Nz")]
    e = sp.Function("e")(t)
    pm = [sp.Function("P%d" % (i + 1))(t) for i in range(3)]
    th = sp.Matrix(3, 3, lambda i, j: sp.Function("Theta_%d%d" % (min(i, j) + 1, max(i, j) + 1))(t))
    h = sp.Matrix([[phi + a, b, cx], [b, phi - a, cy], [cx, cy, 2 * xi]])
    pv = sp.Matrix([0, 0, p])
    nv = sp.Matrix([nx, ny, nz])
    hd = h.diff(t) - (pv * nv.T + nv * pv.T)
    kin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) - al * hd.trace() ** 2) / wb
    hp = h * pv
    r1 = p ** 2 * h.trace() - (pv.T * h * pv)[0]
    r2 = -p ** 2 * (h.T * h).trace() / 4 + hp.dot(hp) / 2 - (pv.T * h * pv)[0] * h.trace() / 2 + p ** 2 * h.trace() ** 2 / 4
    lag = kin + kk * wb * (u * r1 + r2) - e * u - sum(nv[i] * pm[i] for i in range(3)) + sum(th[i, j] * h[i, j] for i in range(3) for j in range(3)) / 2

    def el(f):
        return sp.expand(sp.diff(lag, f) - sp.diff(sp.diff(lag, f.diff(t)), t))
    c_u = el(u)
    c_z = el(nz)
    c_x = el(nx)
    ok_constraints = sp.simplify(c_u - (2 * kk * wb * p ** 2 * phi - e)) == 0 and sp.simplify(c_z - (8 * al * p * phi.diff(t) / wb - pm[2])) == 0
    phidot = sp.solve(c_z, phi.diff(t))[0]
    cond1 = sp.simplify(el(xi).subs(phi.diff(t, 2), sp.diff(phidot, t)))
    ok1 = sp.simplify(cond1 - (pm[2].diff(t) / p + th[2, 2])) == 0
    cxdot = sp.solve(c_x, cx.diff(t))[0]
    cond2 = sp.simplify(el(cx).subs(cx.diff(t, 2), sp.diff(cxdot, t)).doit())
    ok2 = sp.simplify(cond2 - (pm[0].diff(t) / p + th[0, 2])) == 0
    cond3 = sp.simplify(e.diff(t) - 2 * kk * wb * p ** 2 * phidot)
    ok3 = sp.simplify(cond3 - (e.diff(t) - kk * wb ** 2 / (4 * al) * p * pm[2])) == 0
    # Check both transverse components and all three source-variation coefficients.
    cydot = sp.solve(el(ny), cy.diff(t))[0]
    condy = sp.simplify(el(cy).subs(cy.diff(t, 2), sp.diff(cydot, t)).doit())
    oky = sp.simplify(condy - (pm[1].diff(t) / p + th[1, 2])) == 0
    okx = sp.simplify(c_x - (4*al*p*(p*nx-cx.diff(t))/wb-pm[0])) == 0
    gauge = [sp.Function('g%d' % j)(t) for j in range(3)]
    gv = sp.Matrix(gauge)
    dh = pv*gv.T+gv*pv.T
    dn = gv.diff(t)
    okkin = hd.subs({}) is not None and (dh.diff(t)-(pv*dn.T+dn*pv.T)) == sp.zeros(3)
    variation = -sum(dn[j]*pm[j] for j in range(3))+sum(th[i,j]*dh[i,j] for i in range(3) for j in range(3))/2
    integrated = sp.expand(variation+sp.diff(sum(gauge[j]*pm[j] for j in range(3)),t))
    okg = sp.expand(integrated-sum(gauge[j]*(pm[j].diff(t)+p*th[j,2]) for j in range(3))) == 0
    cone = sp.solve(sp.Eq(kk * wb ** 2 / (4 * al), wb ** 2), al)
    want = [kk / 2] if mut("light_cone_forged") else [kk / 4]
    checks.check("E1", ok_constraints and ok1 and ok2 and ok3 and okx and oky and okkin and okg and cone == want,
                 "T4: give block 101's member at beta = -alpha a bond vector N_j entering as h' -> h' - (p N^T + N p^T) and coupled as -N.P (supplied, not adopted); along p = p z its lapse and shift constraints are 2K wbar p^2 phi = e and 8 alpha p phi'/wbar = P_z (with 4 alpha p (p N_x - c_x')/wbar = P_x across), and the evolution keeps them iff P_z' = -p Theta_zz, P_x' = -p Theta_xz with the symmetric stress, and e' = (K wbar^2/(4 alpha)) p P_z; with P = P^B, T1-T2 give the first two for every state and the energy current wbar^2 P^B, so initially satisfied nonzero-mode lapse and shift constraints are preserved for all free-walk sources iff alpha = K/4, and the prescribed conserved-source quadratic action is invariant under time-dependent relabellings up to a boundary term")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 62, 69, 73, 74 and 101 as landed on main (the walk, the frame's stress coupling, the two-step momentum and its current, and the member's quadratic action), with blocks 120, 124 and 135 placed; it reports the two-step content's conservation laws in the member's placement and what a bond shift coupled to its momentum would keep; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the energy and momentum laws as exact matrices over Q(i) on the 5^3, 6^3 and 9^3 tori, both sides nonzero, support radius at most 4",
    "per_site: executed - the laws at two sites of 5^3 and at the origin of 6^3 and 9^3, for every momentum component",
    "per_mode: executed - the member with a lapse and a bond shift along one axis: constraints, their preservation, and the three conditions",
    "per_block: executed - nine failing variants: site energy, unaveraged and one-step momenta, the canonical momentum with the symmetric stress, the site stress",
    "lattice_wide: the laws are exact on Z^3 for every state (support radius at most 4 < 9/2); first order in the member's fields; the walk, currents, placements, member, shift and link supplied",
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
    print('scope: Conservation identities and preservation of initially satisfied nonzero-mode constraints; no general solvability or nonlinear gauge theory. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
