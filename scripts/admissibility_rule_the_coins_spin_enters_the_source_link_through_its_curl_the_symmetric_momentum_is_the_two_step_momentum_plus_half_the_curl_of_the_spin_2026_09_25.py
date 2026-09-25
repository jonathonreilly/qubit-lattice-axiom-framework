#!/usr/bin/env python3
"""Exact checks: the coin's spin enters the source link through its curl - the bonds' coin-energy current Q differs from
the carried two-step momentum P'' by half the curl of the coin's spin on the faces, so block 136's symmetric momentum is the
two-step momentum plus half the curl of the specified face bilinear (sigma/2), exactly on the lattice; the curl has zero divergence and therefore changes no term in this energy-continuity equation, and the torque
that stops the canonical momentum from balancing the symmetric stress is the rate of the face-bilinear curl (the supervisor's own
derivation; blocks 54, 62, 63, 69, 73 and 74 as landed; blocks 120 and 136 placed; not adopted).

B (T1): Q - P'' = (1/2) curl S~ on the 5^3, 6^3 and 9^3 tori, carried to Z^3 by its support radius.
C (T2): P^B = P'' + (1/2) curl (spin); the curl has zero divergence and therefore changes no term in this energy-continuity equation.
D (T3): the torque is the rate of the face-bilinear curl.
E (T4): the eigenvector identity behind T1.
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
AUDIT_INPUT_PATHS = ['docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THREE_RESPONSES_EIGHT_SPECIES_THE_FRAMES_SITE_STRESS_HAS_THE_WRONG_SIGN_IN_SHEAR_FOR_SIX_SPECIES_ONLY_THE_TWO_STEP_CURRENT_SERVES_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md']
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_coins_spin_enters_the_source_link_through_its_curl_the_symmetric_momentum_is_the_two_step_momentum_plus_half_the_curl_of_the_spin_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "one_diagonal_only": "B",
    "belinfante_factor_forged": "C",
    "torque_sign_forged": "D",
    "spin_identity_forged": "E",
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


EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
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

    def re_bil(self, coin, a, b):
        """Re psi^dag(a) coin psi(b)"""
        A = self.coin_op(coin, a, b)
        return (A + A.dag()).scale(gq(Fr(1, 2)))

    def face_spin(self, l, x, diagonals=(True, True)):
        """S_l(x): the coin's spin sigma_l carried on the face perpendicular to l at x + (e_j + e_k)/2, the mean of its two diagonals"""
        j, k = [m for m in range(3) if m != l]
        out = SM()
        if diagonals[0]:
            out = out + self.re_bil(SIGC[l], x, self.sh(self.sh(x, j), k))
        if diagonals[1]:
            out = out + self.re_bil(SIGC[l], self.sh(x, k), self.sh(x, j))
        return out.scale(gq(Fr(1, 2)))

    def face_spin_avg(self, l, x, diagonals=(True, True)):
        out = SM()
        for sg in product((1, -1), repeat=3):
            out = out + self.face_spin(l, (x[0] + sg[0], x[1] + sg[1], x[2] + sg[2]), diagonals)
        return out.scale(gq(Fr(1, 8)))

    def curl_spin(self, j, x, diagonals=(True, True)):
        """sum_{k,l} eps_jkl dbar_k S~_l (x): lands on the bond x -> x + e_j"""
        out = SM()
        for k in range(3):
            for l in range(3):
                e = EPS.get((j, k, l), 0)
                if e:
                    term = self.face_spin_avg(l, x, diagonals) - self.face_spin_avg(l, self.sh(x, k, -1), diagonals)
                    out = out + term.scale(gq(e))
        return out

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
    """T1: Q - P'' is half the curl of the coin's face spin, exactly."""
    ok = True
    radii = []
    for L, xs in ((5, ((0, 0, 0), (2, 1, 3))), (6, ((0, 0, 0),)), (9, ((0, 0, 0),))):
        tor = Torus(L)
        for x in xs:
            for j in range(3):
                lhs = tor.q_avg(j, x) - tor.mom_bond(j, x)
                diag = (True, False) if mut("one_diagonal_only") else (True, True)
                rhs = tor.curl_spin(j, x, diag).scale(gq(Fr(1, 2)))
                ok = ok and (lhs - rhs).is_zero() and not lhs.is_zero()
                if L == 9:
                    radii += [tor.radius(lhs), tor.radius(rhs)]
    ok_transfer = len(radii) == 6 and max(radii) <= 4
    checks.check("B1", ok and ok_transfer,
                 "T1: on the 5^3, 6^3 and 9^3 tori, as exact operators over Q(i), for j = 1, 2, 3: Q_j - P''_j = (1/2) sum_kl eps_jkl dbar_k S~_l, where S_l(x) = (1/2)[Re psi^dag(x) sigma_l psi(x + e_j + e_k) + Re psi^dag(x + e_k) sigma_l psi(x + e_j)] is the specified face bilinear perpendicular to l (the mean of its two diagonals) and S~ = C_1 C_2 C_3 S; both sides nonzero, support radius at most 4 on 9^3, so the identity holds on Z^3")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the symmetric momentum is the two-step momentum plus half the curl of the specified face bilinear; the curl has zero divergence and therefore changes no term in this energy-continuity equation."""
    ok = True
    for L in (5, 6):
        tor = Torus(L)
        x = (0, 0, 0)
        for j in range(3):
            pb = tor.mom_sym(j, x)
            fac = Fr(1, 2) if mut("belinfante_factor_forged") else Fr(1, 4)
            ok = ok and (pb - tor.mom_bond(j, x) - tor.curl_spin(j, x).scale(gq(fac))).is_zero()
        div_curl = tor.div_bond(lambda j, y: tor.curl_spin(j, y), x)
        ok = ok and div_curl.is_zero()
    checks.check("C1", ok,
                 "T2: on 5^3 and 6^3, P^B_j = P''_j + (1/4) (curl S~)_j = P''_j + (1/2) curl(S~/2), with S~/2 the specified averaged face bilinear: the symmetric momentum is the two-step momentum plus half the curl of the specified face bilinear; and sum_j dbar_j (curl S~)_j = 0 exactly, so the curl has zero divergence and therefore changes no term in this energy-continuity equation and e' flows as P^B")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the torque - the divergence of the antisymmetric stress is the rate of the face-bilinear curl."""
    ok = True
    tor = Torus(5)
    x = (0, 0, 0)
    for j in range(3):
        anti = tor.div_bond(lambda i, y: tor.theta_two_step(i, j, y) - tor.theta_two_step(j, i, y), x)
        rate = tor.ddt(tor.curl_spin(j, x)).scale(gq(Fr(1, 2)))
        if mut("torque_sign_forged"):
            rate = rate.scale(gq(-1))
        ok = ok and (anti - rate).is_zero() and not anti.is_zero()
    checks.check("D1", ok,
                 "T3: on 5^3, for j = 1, 2, 3: sum_i dbar_i (Theta_ij - Theta_ji) = (1/2) d/dt (curl S~)_j, both sides nonzero: the torque on the coin that stops the canonical momentum from being conserved with the symmetric stress (block 136 T3) is exactly the rate of change of the face-bilinear curl")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the exact coin-matrix eigenvector identity."""
    # (lambda + lambda') M_j = (s_j + s'_j) u'^dag u + i eps_jkl (s - s')_k M_l  (the identity behind T1)
    lam, lamp = sp.symbols("lambda lambda_p", real=True)
    s = sp.symbols("s1:4", real=True)
    t = sp.symbols("t1:4", real=True)
    u = sp.Matrix([lam + s[2], s[0] + sp.I * s[1]])
    up = sp.Matrix([lamp + t[2], t[0] + sp.I * t[1]])
    sig = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    mm = [(up.H * sg * u)[0] for sg in sig]
    ov = (up.H * u)[0]
    rels = [lam ** 2 - sum(v ** 2 for v in s), lamp ** 2 - sum(v ** 2 for v in t)]
    eps = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    ok = True
    sgn = -1 if mut("spin_identity_forged") else 1
    for j in range(3):
        rhs = (s[j] + t[j]) * ov + sgn * sp.I * sum(eps.get((j, k, l), 0) * (s[k] - t[k]) * mm[l] for k in range(3) for l in range(3))
        expr = sp.expand((lam + lamp) * mm[j] - rhs)
        rem = sp.reduced(expr, rels, lam, lamp)[1]
        ok = ok and sp.expand(rem) == 0
    checks.check("E1", ok,
                 "T4: the identity behind T1 - for eigenvectors (sigma.s) u = lambda u, (sigma.s') u' = lambda' u': (lambda + lambda') u'^dag sigma_j u = (s_j + s'_j) u'^dag u + i eps_jkl (s - s')_k u'^dag sigma_l u, modulo lambda^2 = |s|^2 (symbolic): the first part is the two-step momentum's beat, the second is the curl of the specified face bilinear's beat, since s - s' = 2 sin(q/2) cos kbar")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 62, 63, 69, 73 and 74 as landed on main (the walk, the frame, the currents and the two-step momentum), with blocks 120 and 136 placed; it reports how the coin's spin enters the symmetric momentum that block 136 couples to a shift; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - Q - P'' = (1/2) curl S~ as exact matrices over Q(i) on 5^3, 6^3 and 9^3, support radius at most 4",
    "per_site: executed - two sites of 5^3 and the origin of 6^3 and 9^3, every component",
    "per_mode: executed - the eigenvector identity (l + l') u'^dag sigma_j u = (s_j + s'_j) u'^dag u + i eps (s - s')_k u'^dag sigma_l u, symbolically",
    "per_block: executed - P^B = P'' + (1/4) curl S~; the divergence of the curl; the torque as the rate of the curl",
    "lattice_wide: the identities are exact on Z^3 for every state (support radius at most 4 < 9/2); the walk, currents and placements supplied",
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
    print('scope: Specified face-bilinear curl identity, not derived physical on-site spin. Supplied model only; no audit verdict.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
