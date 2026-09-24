#!/usr/bin/env python3
"""Exact checks: no local momentum falls with weight one on the lattice (the weight is the slope of its band value, zero zone mean); the walk's force is a bond
energy times a clock difference; no ledger that carries the rates can demand it at every wave number (probes workers' results, refereed
by a Grok model; blocks 54, 63, 64, 66, 72 supplied; not adopted).

B (T1): [X, T_n] = n T_n; the band identity; the weight of the fall is d pbar/dk, cos k and cos 2k, with zero zone mean.
C (T2): the exact bond form of the force; the energy-density part and remainder; a sublattice state with no energy density and a force.
D (T3): curl ledgers demand no force; a rate-carrying ledger exists; equal-content plane waves with different forces.
E (T4): reach three: the two-step bond form and the weight cos 2k.
Exact rational, Gaussian-rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_NO_LOCAL_MOMENTUM_FALLS_WITH_WEIGHT_ONE_ON_THE_LATTICE_THE_WALKS_FORCE_IS_A_BOND_ENERGY_TIMES_A_CLOCK_DIFFERENCE_AND_NO_LEDGER_CAN_DEMAND_IT_EXACTLY_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    note, axioms = texts
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
    """T1: what falls with weight one: any local momentum commuting with the walk falls with weight d pbar/dk, of zero zone mean."""
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
    checks.check("B1", xt and sym_ok and commute and band and weights and zero_mean, "T1: [X, T_n] = n T_n exactly, so the symbol of i[X, P] is -dP/dk; for a momentum P commuting with the walk, <chi|dP/dk|chi> = d pbar/dk on the band (exact at sin k = (3/5, 4/5, 0): -28/25); so in a uniform clock gradient a plane wave's P changes at first order by -E grad u . grad_k pbar: the weight of the fall is d pbar/dk_j - cos k_j for the one-step momentum, cos 2k_j for the two-step one, 1 - k^4/6 + ... for the fourth-order stencil (-5/3 at k = pi); each has zero mean over (-pi, pi], as does the derivative of any periodic band value (a random trigonometric polynomial; |sin k|): no local momentum that commutes with the walk falls with weight one at every wave number")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the exact lattice force is a bond energy times a clock difference, not a function of the energy density."""
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
    checks.check("C1", ok1 and ok2 and sub and par, f"T2: for every state and rate field (random Gaussian-rational states and rational rate roots on 4^3 and 5^3), block 66's force density is exactly f_j(x) = d_j phi(x) eps_j(x) + d_j phi(x - e_j) eps_j(x - e_j) with eps_b = (1/2) Re[psi_y^+ chi_x + psi_x^+ chi_y] the bond's cross energy, chi = H phi psi; and eps_b = (rho_x + rho_y)/2 - (1/2) Re[(d psi)^+ (d chi)]: the energy-density part plus an exact remainder; a state on one sublattice (4^3) has energy density zero at every site and a force at {nz} sites, so the force is no function of the energy density; the map (-1)^(x1+x2+x3) anticommutes with the clocked walk, flips the energy density and keeps the force (6^3)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: ledgers built from curls demand no force; a ledger that carries the rates demands one built from e and J, which cannot be the walk's."""
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
    checks.check("D1", curl_ok and carries and first and same and differ, "T3: every ledger built from block 64's curls with site-multiplier rates (a random linear-plus-quadratic member on 4^3) obeys sum_a [E_a^j(x) - E_a^j(x - e_a)] = 0 exactly, with no rate term: it demands no force; a ledger that carries the rates exists (the volume member with the upwind transport, exact at B = 0) and demands a force built from the energy density and current; but at first order in the rate gradient every plane wave's force is e cos k_j (u(x+e_j) - u(x-e_j))/2 (all 48 plane waves of energy +-1 on 4^3), and k = (pi/2,0,0), (0,pi/2,0) carry the same energy density 2 and zero current at every site with forces 0 and nonzero along e_1: no requirement built from e and J can match the walk's force at every wave number")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: reach three: the same structure with the two-step bond, weight cos 2k."""
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
    checks.check("E1", ok0 and ok1 and ok2 and nontrivial, "T4: with the two-step momentum (block 72, reach three), i[phi, P_j] = -(1/2) C2_j[d2_j phi] exactly; the force is (1/2)[d2_j phi(x) eps2(x) + d2_j phi(x - 2e_j) eps2(x - 2e_j)] with eps2 the two-step bond's cross energy (5^3, 6^3); at first order its plane-wave form is e cos 2k_j (u(x+2e_j) - u(x-2e_j))/4 (all 48 plane waves of energy +-1 on 8^3, where the two-step difference is not identically zero): the same obstruction with weight cos 2k_j")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied clauses of blocks 54, 63, 64, 66 and 72 (the clocked walk, its momenta, the relabelling ledger and its force); it reports, from probes workers' results refereed by another model family, what falls with weight one on the lattice and whether a ledger can demand it; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the shift commutator on a chain; the symbols, weights and zone means of the momenta; the band identity at a rational point",
    "per_site: executed - the force density at every site of 4^3, 5^3, 6^3 for random Gaussian-rational states and rational rates; a sublattice state; the parity map",
    "per_mode: executed - all 48 plane waves of energy +-1 at first order in the rate gradient (one step on 4^3, two steps on 8^3)",
    "per_block: executed - a random curl member and the volume member with the upwind transport on 4^3",
    "lattice_wide: T1 for every finite-reach momentum commuting with the walk; T2 for every state and rate field; T3 for every ledger of the stated classes at first order; blocks 54, 63, 64, 66, 72 supplied",
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
    print("scope: the fall on the lattice - the weight of any local conserved momentum is d pbar/dk with zero zone mean, so no local momentum falls with weight one; the force is a bond energy times a clock difference, not a function of the energy density; curl ledgers demand no force and rate-carrying ledgers cannot demand the walk's at every wave number; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
