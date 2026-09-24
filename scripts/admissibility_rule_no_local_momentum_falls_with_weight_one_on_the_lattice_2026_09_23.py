#!/usr/bin/env python3
"""Formal first-order band derivatives, exact finite-lattice bond identities and a restricted leading-force representation obstruction."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_NO_LOCAL_MOMENTUM_FALLS_WITH_WEIGHT_ONE_ON_THE_LATTICE_THE_WALKS_FORCE_IS_A_BOND_ENERGY_TIMES_A_CLOCK_DIFFERENCE_AND_NO_LEDGER_CAN_DEMAND_IT_EXACTLY_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_FALL_IS_OWED_BY_THE_LEDGER_A_FIELD_ENERGY_PER_LOCAL_TICK_REQUIRES_THE_CONTENTS_STRESS_GRADIENT_TO_EQUAL_ITS_WEIGHT_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHICH_SPECIES_FALL_THE_LEDGER_OWES_UNDER_REACH_TWO_A_REFLECTED_SPECIES_HAS_MINUS_ITS_WEIGHT_UNDER_REACH_THREE_ALL_EIGHT_AGREE_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_the_walks_force_is_a_bond_energy_times_a_clock_difference_and_no_ledger_can_demand_it_exactly_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "weight_mean_forged": "B",
    "bond_form_shifted": "C",
    "equal_content_pair_forged": "D",
    "reach_three_factor_altered": "E",
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


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the walk, the clocks and the ledger are supplied clauses)")


# ============================================================================================ helpers (block 54's walk on tori, Gaussian rationals; ported from the probes worker w-macbookpro90c72-j152a)
import random

class Q:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, F) else F(r)
        self.i = i if isinstance(i, F) else F(i)

    def __add__(self, o):
        return Q(self.r + o.r, self.i + o.i)

    def __sub__(self, o):
        return Q(self.r - o.r, self.i - o.i)

    def __neg__(self):
        return Q(-self.r, -self.i)

    def __mul__(self, o):
        if isinstance(o, Q):
            return Q(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
        o = F(o)
        return Q(self.r * o, self.i * o)

    __rmul__ = __mul__

    def conj(self):
        return Q(self.r, -self.i)

    def __eq__(self, o):
        return self.r == o.r and self.i == o.i


QZ = Q(0, 0)
QONE = Q(1, 0)
QI = Q(0, 1)
SIG = [((QZ, QONE), (QONE, QZ)), ((QZ, -QI), (QI, QZ)), ((QONE, QZ), (QZ, -QONE))]


def sp_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sp_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def sp_scale(c, a):
    return (c * a[0], c * a[1])


def sp_mat(m, a):
    return (m[0][0] * a[0] + m[0][1] * a[1], m[1][0] * a[0] + m[1][1] * a[1])


def re_dot(a, b):
    """Re a^dagger b."""
    return a[0].r * b[0].r + a[0].i * b[0].i + a[1].r * b[1].r + a[1].i * b[1].i


class Torus:
    def __init__(self, L):
        self.L = L
        self.N = L ** 3
        self.sites = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
        self.idx = {s: n for n, s in enumerate(self.sites)}
        self.nb = {}
        for a in range(3):
            for st in (1, -1, 2, -2):
                self.nb[(a, st)] = [self.idx[tuple((s[t] + (st if t == a else 0)) % L for t in range(3))] for s in self.sites]

    def shift(self, v, a, st):
        nb = self.nb[(a, st)]
        return [v[nb[n]] for n in range(self.N)]

    def S(self, psi, a):  # (psi(x+e) - psi(x-e))/(2i) = -(i/2)(...)
        p, m = self.shift(psi, a, 1), self.shift(psi, a, -1)
        c = Q(0, F(-1, 2))
        return [sp_scale(c, sp_sub(p[n], m[n])) for n in range(self.N)]

    def H(self, psi):
        out = [(QZ, QZ)] * self.N
        for a in range(3):
            s = self.S(psi, a)
            out = [sp_add(out[n], sp_mat(SIG[a], s[n])) for n in range(self.N)]
        return out

    def mul(self, phi, psi):
        return [sp_scale(phi[n], psi[n]) for n in range(self.N)]

    def C(self, psi, a, v, step=1):
        p, m = self.shift(psi, a, step), self.shift(psi, a, -step)
        vm = self.shift(v, a, -step)
        h = F(1, 2)
        return [sp_add(sp_scale(h * v[n], p[n]), sp_scale(h * vm[n], m[n])) for n in range(self.N)]

    def d(self, phi, a, step=1):
        p = self.shift(phi, a, step)
        return [p[n] - phi[n] for n in range(self.N)]


def rand_q(rng, k=3):
    return Q(F(rng.randint(-k, k)), F(rng.randint(-k, k)))


def rand_state(T, rng, k=3):
    return [(rand_q(rng, k), rand_q(rng, k)) for _ in range(T.N)]


def rand_phi(T, rng):
    return [F(rng.randint(2, 9), rng.randint(2, 5)) for _ in range(T.N)]


def densities(T, psi, phi):
    chi = T.H(T.mul(phi, psi))
    e = [phi[n] * re_dot(psi[n], chi[n]) for n in range(T.N)]
    return chi, e


def force(T, psi, phi, chi, j, two=False):
    if two:
        v = T.d(phi, j, 2)
        Cpsi = T.C(psi, j, v, 2); Cchi = T.C(chi, j, v, 2)
        half = F(1, 2)
        return [half * (re_dot(Cpsi[n], chi[n]) + re_dot(psi[n], Cchi[n])) for n in range(T.N)]
    v = T.d(phi, j)
    Cpsi = T.C(psi, j, v); Cchi = T.C(chi, j, v)
    return [re_dot(Cpsi[n], chi[n]) + re_dot(psi[n], Cchi[n]) for n in range(T.N)]


def bond_eps(T, psi, chi, j, step=1):
    """epsilon_b = (1/2) Re[psi(y)^dagger chi(x) + psi(x)^dagger chi(y)] on the bond b = (x, y = x + step e_j), placed at x."""
    py, cy = T.shift(psi, j, step), T.shift(chi, j, step)
    return [F(1, 2) * (re_dot(py[n], chi[n]) + re_dot(psi[n], cy[n])) for n in range(T.N)]


def plane_waves():
    """energy +-1 plane waves of the 8-torus: one component of k in {pi/2, 3pi/2}, the others in {0, pi}; spinor eigenvectors."""
    out = []
    for pos in range(3):
        for q in (1, 3):
            for o1 in (0, 2):
                for o2 in (0, 2):
                    k = [0, 0, 0]; others = [t for t in range(3) if t != pos]
                    k[pos] = q; k[others[0]] = o1; k[others[1]] = o2       # k = (pi/2) * k
                    s = 1 if q == 1 else -1                               # sin k_pos = s
                    for E in (1, -1):
                        if pos == 0:
                            a = (QONE, Q(E * s))                            # s sigma_x a = E a
                        elif pos == 1:
                            a = (QONE, Q(0, E * s))                         # s sigma_y a = E a: (1, i s E)
                        else:
                            a = (QONE, QZ) if E * s == 1 else (QZ, QONE)       # s sigma_z a = E a
                        out.append((tuple(k), E, a))
    return out


PH = [QONE, QI, -QONE, -QI]   # e^{i (pi/2) m}
COS = {0: 1, 1: 0, 2: -1, 3: 0}


def curls(T, B):
    """F_ab^j(x) = d_a B_b^j(x) - d_b B_a^j(x), a < b; B[a][j] a site list (bond x -> x + e_a)."""
    out = []
    for (a, b) in ((0, 1), (0, 2), (1, 2)):
        for j in range(3):
            dab = T.d(B[b][j], a); dba = T.d(B[a][j], b)
            out.append([dab[n] - dba[n] for n in range(T.N)])
    return out




# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    k = sp.symbols("k", real=True)
    N = 9
    X = sp.diag(*range(N))

    def Tn(n):
        return sp.Matrix(N, N, lambda a, b: 1 if a - b == n else 0)
    xt = all((X * Tn(n) - Tn(n) * X) == n * Tn(n) for n in (-2, -1, 1, 2))

    def symbol(co):
        return sum((c * sp.exp(-sp.I * k * n) for n, c in co.items()), sp.Integer(0))
    S1 = {1: sp.I / 2, -1: -sp.I / 2}
    C1 = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}
    P2 = {}
    for n1, c1 in S1.items():
        for n2, c2 in C1.items():
            P2[n1 + n2] = P2.get(n1 + n2, 0) + c1 * c2
    P2 = {n: c for n, c in P2.items() if c != 0}
    sym_ok = True
    for co, pexpr in ((S1, sp.sin(k)), (P2, sp.sin(k) * sp.cos(k))):
        sym_ok = sym_ok and sp.simplify(sp.expand(symbol(co).rewrite(sp.cos)) - pexpr) == 0
        comm = sum((sp.I * n * c * sp.exp(-sp.I * k * n) for n, c in co.items()), sp.Integer(0))
        sym_ok = sym_ok and sp.simplify(sp.expand((comm + sp.diff(symbol(co), k)).rewrite(sp.cos))) == 0
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    s = sp.Matrix([sp.sin(k1), sp.sin(k2), sp.sin(k3)])
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    Hk = sum((s[i] * sig[i] for i in range(3)), sp.zeros(2))
    a_ = sp.cos(k1) + sp.cos(k2) * sp.cos(k3)
    c_ = 1 + sp.cos(k1 + k2)
    Pk = a_ * sp.eye(2) + c_ * Hk
    commute = sp.simplify(Pk * Hk - Hk * Pk) == sp.zeros(2)
    pt = {sp.sin(k1): sp.Rational(3, 5), sp.cos(k1): sp.Rational(4, 5), sp.sin(k2): sp.Rational(4, 5), sp.cos(k2): sp.Rational(3, 5), sp.sin(k3): 0, sp.cos(k3): 1}
    Hn = Hk.subs(pt)
    vecs = (Hn - sp.eye(2)).nullspace()
    chi = vecs[0] / sp.sqrt((vecs[0].H * vecs[0])[0])
    at = lambda e: sp.nsimplify(sp.simplify(sp.expand_trig(sp.expand(e)).subs(pt)))
    dP = sp.diff(Pk, k1)
    pbar = a_ + c_ * sp.sqrt(sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2)
    band = sp.simplify((chi.H * dP.applyfunc(at) * chi)[0] - at(sp.diff(pbar, k1))) == 0 and at(sp.diff(pbar, k1)) == sp.Rational(-28, 25)
    w_pi = sp.diff(sp.sin(k), k)
    w_P = sp.simplify(sp.diff(sp.sin(k) * sp.cos(k), k))
    w_4 = sp.diff(sp.Rational(4, 3) * sp.sin(k) - sp.Rational(1, 6) * sp.sin(2 * k), k)
    mean = sp.integrate(w_pi, (k, -sp.pi, sp.pi)) if not mut("weight_mean_forged") else 2 * sp.pi
    weights = (w_pi == sp.cos(k) and mean == 0 and sp.simplify(w_P - sp.cos(2 * k)) == 0 and sp.integrate(w_P, (k, -sp.pi, sp.pi)) == 0
               and sp.series(w_4, k, 0, 6).removeO() == 1 - k ** 4 / 6 and sp.integrate(w_4, (k, -sp.pi, sp.pi)) == 0
               and sp.simplify(w_4.subs(k, sp.pi)) == sp.Rational(-5, 3))
    rng = random.Random(3)
    ptrig = sum((rng.randint(-5, 5) * sp.sin(n * k) + rng.randint(-5, 5) * sp.cos(n * k) for n in range(1, 7)), sp.Integer(0))
    zero_mean = sp.integrate(sp.diff(ptrig, k), (k, -sp.pi, sp.pi)) == 0 and sp.integrate(sp.sign(sp.sin(k)) * sp.cos(k), (k, -sp.pi, sp.pi)) == 0
    checks.check("B1", xt and sym_ok and commute and band and weights and zero_mean, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    rng = random.Random(20260924)
    ok1 = ok2 = True
    for L in (4, 5):
        T = Torus(L)
        psi, phi = rand_state(T, rng), rand_phi(T, rng)
        chi, e = densities(T, psi, phi)
        rho = [re_dot(psi[n], chi[n]) for n in range(T.N)]
        for j in range(3):
            fj = force(T, psi, phi, chi, j)
            eps = bond_eps(T, psi, chi, j)
            dphi = T.d(phi, j)
            shift = -1 if not mut("bond_form_shifted") else 1
            epsm, dphim = T.shift(eps, j, shift), T.shift(dphi, j, shift)
            ok1 = ok1 and all(fj[n] == dphi[n] * eps[n] + dphim[n] * epsm[n] for n in range(T.N))
            dpsi = [sp_sub(a, b) for a, b in zip(T.shift(psi, j, 1), psi)]
            dchi = [sp_sub(a, b) for a, b in zip(T.shift(chi, j, 1), chi)]
            rhoy = T.shift(rho, j, 1)
            ok2 = ok2 and all(eps[n] == (rho[n] + rhoy[n]) / 2 - F(1, 2) * re_dot(dpsi[n], dchi[n]) for n in range(T.N))
    T = Torus(4)
    phi = rand_phi(T, rng)
    psi = [(rand_q(rng), rand_q(rng)) if sum(s) % 2 == 0 else (QZ, QZ) for s in T.sites]
    chi, e = densities(T, psi, phi)
    fx = force(T, psi, phi, chi, 0)
    nz = sum(1 for v in fx if v != 0)
    sub = all(v == 0 for v in e) and nz > 0
    T = Torus(6)
    psi, phi = rand_state(T, rng), rand_phi(T, rng)
    g = [(-1) ** (sum(s) % 2) for s in T.sites]
    gpsi = [sp_scale(g[n], psi[n]) for n in range(T.N)]
    Hwpsi = T.mul(phi, T.H(T.mul(phi, psi)))
    Hwg = T.mul(phi, T.H(T.mul(phi, gpsi)))
    par = all(Hwg[n] == sp_scale(-g[n], Hwpsi[n]) for n in range(T.N))
    chi, e = densities(T, psi, phi)
    chig, eg = densities(T, gpsi, phi)
    par = par and all(eg[n] == -e[n] for n in range(T.N))
    for j in range(3):
        f1, f2 = force(T, psi, phi, chi, j), force(T, gpsi, phi, chig, j)
        par = par and all(f2[n] == f1[n] for n in range(T.N))
    checks.check("C1", ok1 and ok2 and sub and par, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    rng = random.Random(64)
    T = Torus(4)
    w = [F(rng.randint(1, 9), rng.randint(1, 4)) for _ in range(T.N)]
    lin = [F(rng.randint(-3, 3)) for _ in range(9)]
    quad = [[F(rng.randint(-2, 2)) for _ in range(9)] for _ in range(9)]

    def Fval(B):
        c = curls(T, B)
        tot = F(0)
        for n in range(T.N):
            v = [c[p][n] for p in range(9)]
            D = sum((lin[p] * v[p] for p in range(9)), F(0)) + sum((quad[p][q] * v[p] * v[q] for p in range(9) for q in range(9)), F(0))
            tot += w[n] * D
        return tot
    B0 = [[[F(rng.randint(-2, 2)) for _ in range(T.N)] for _ in range(3)] for _ in range(3)]
    E = [[[F(0)] * T.N for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for j in range(3):
            for n in range(T.N):
                B0[a][j][n] += 1
                Fp = Fval(B0)
                B0[a][j][n] -= 2
                Fm = Fval(B0)
                B0[a][j][n] += 1
                E[a][j][n] = (Fp - Fm) / 2
    curl_ok = True
    for j in range(3):
        div = [sum((E[a][j][n] - E[a][j][T.nb[(a, -1)][n]] for a in range(3)), F(0)) for n in range(T.N)]
        curl_ok = curl_ok and all(v == 0 for v in div)
    c0 = F(3, 7)
    xi = [[F(rng.randint(-3, 3)) for _ in range(T.N)] for _ in range(3)]
    s1 = F(0)
    for a in range(3):
        dx = T.d(xi[a], a)
        s1 += sum((-c0 * w[n] * dx[n] for n in range(T.N)), F(0))
    s2 = F(0)
    for n in range(T.N):
        du = -sum((xi[a][n] * (1 - w[T.nb[(a, -1)][n]] / w[n]) for a in range(3)), F(0))
        s2 += c0 * w[n] * du
    carries = s1 + s2 == 0 and s1 != 0
    # first order in the rate gradient: the force of a plane wave is e cos k_j (centred difference of u)/2; two equal-content waves
    T = Torus(4)
    rng2 = random.Random(8)
    eta = [F(rng2.randint(-4, 4)) for _ in range(T.N)]
    COS4 = {0: 1, 1: 0, 2: -1, 3: 0}
    first = True
    pair = {}
    for kk, E_, a in plane_waves():
        psi = [sp_scale(PH[(kk[0] * s_[0] + kk[1] * s_[1] + kk[2] * s_[2]) % 4], a) for s_ in T.sites]
        Hpsi = T.H(psi)
        first = first and all(Hpsi[n] == sp_scale(E_, psi[n]) for n in range(T.N))
        e0 = E_ * re_dot(a, a)
        v = T.d(eta, 0)
        f1 = [re_dot(c, h) + re_dot(p, cc) for c, h, p, cc in zip(T.C(psi, 0, v), Hpsi, psi, T.C(Hpsi, 0, v))]
        ep, em = T.shift(eta, 0, 1), T.shift(eta, 0, -1)
        first = first and all(f1[n] == e0 * COS4[kk[0] % 4] * (ep[n] - em[n]) for n in range(T.N))
        if E_ == 1 and kk in ((1, 0, 0), (0, 1, 0)):
            dens = [re_dot(psi[n], Hpsi[n]) for n in range(T.N)]
            cur0 = True
            for jj in range(3):
                Sj = T.S(psi, jj)
                for aa in range(3):
                    up, Sup = T.shift(psi, aa, 1), T.shift(Sj, aa, 1)
                    cur0 = cur0 and all(re_dot(up[n], sp_mat(SIG[aa], Sj[n])) + re_dot(Sup[n], sp_mat(SIG[aa], psi[n])) == 0 for n in range(T.N))
            pair[kk] = (dens, cur0, f1)
    A, Bw = pair[(1, 0, 0)], pair[(0, 1, 0)]
    same = all(x == 2 for x in A[0]) and all(x == 2 for x in Bw[0]) and A[1] and Bw[1]
    if mut("equal_content_pair_forged"):
        same = same and A[0] != Bw[0]
    differ = all(v == 0 for v in A[2]) and any(v != 0 for v in Bw[2])
    checks.check("D1", curl_ok and carries and first and same and differ, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    rng = random.Random(69)
    ok0 = ok1 = True
    for L in (5, 6):
        T = Torus(L)
        psi, phi = rand_state(T, rng), rand_phi(T, rng)
        for j in range(3):
            ones = [F(1)] * T.N
            Pj = lambda v: T.S(T.C(v, j, ones), j)
            a = Pj(psi)
            b = Pj(T.mul(phi, psi))
            comm = [sp_scale(Q(0, 1), sp_sub(sp_scale(phi[n], a[n]), b[n])) for n in range(T.N)]
            rhs = T.C(psi, j, T.d(phi, j, 2), 2)
            ok0 = ok0 and all(comm[n] == sp_scale(F(-1, 2), rhs[n]) for n in range(T.N))
        chi, e = densities(T, psi, phi)
        for j in range(3):
            fp = force(T, psi, phi, chi, j, True)
            eps2 = bond_eps(T, psi, chi, j, 2)
            v2 = T.d(phi, j, 2)
            eps2m, v2m = T.shift(eps2, j, -2), T.shift(v2, j, -2)
            ok1 = ok1 and all(fp[n] == F(1, 2) * (v2[n] * eps2[n] + v2m[n] * eps2m[n]) for n in range(T.N))
    T = Torus(8)
    rng2 = random.Random(8)
    eta = [F(rng2.randint(-4, 4)) for _ in range(T.N)]
    COS4 = {0: 1, 1: 0, 2: -1, 3: 0}
    ok2 = True
    nontrivial = False
    for kk, E_, a in plane_waves():
        psi = [sp_scale(PH[(kk[0] * s_[0] + kk[1] * s_[1] + kk[2] * s_[2]) % 4], a) for s_ in T.sites]
        Hpsi = T.H(psi)
        e0 = E_ * re_dot(a, a)
        v2 = T.d(eta, 0, 2)
        p1 = [F(1, 2) * (re_dot(c, h) + re_dot(p, cc)) for c, h, p, cc in zip(T.C(psi, 0, v2, 2), Hpsi, psi, T.C(Hpsi, 0, v2, 2))]
        ep2, em2 = T.shift(eta, 0, 2), T.shift(eta, 0, -2)
        factor = COS4[(2 * kk[0]) % 4] if not mut("reach_three_factor_altered") else COS4[kk[0] % 4]
        ok2 = ok2 and all(p1[n] == F(1, 2) * e0 * factor * (ep2[n] - em2[n]) for n in range(T.N))
        nontrivial = nontrivial or any(v != 0 for v in p1)
    checks.check("E1", ok0 and ok1 and ok2 and nontrivial, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    T=Torus(3); psi=[(QZ,QZ)]*T.N; psi[0]=(QONE,QZ)
    g=[(-1)**sum(s) for s in T.sites]
    left=T.H([sp_scale(g[n],psi[n]) for n in range(T.N)])
    right=[sp_scale(-g[n],v) for n,v in enumerate(T.H(psi))]
    checks.check("C9", any(a!=b for a,b in zip(left,right)), 'Scoped exact check C9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Formal first-order band derivatives, exact finite-lattice bond identities and a restricted leading-force representation obstruction.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
