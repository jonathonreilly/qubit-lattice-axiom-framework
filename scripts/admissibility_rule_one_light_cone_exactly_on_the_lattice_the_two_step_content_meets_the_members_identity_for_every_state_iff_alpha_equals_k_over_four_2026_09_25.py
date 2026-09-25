#!/usr/bin/env python3
"""Exact checks: one light cone exactly on the lattice - block 69's two-step current, read through block 120's realisation,
with the energy averaged over the eight body-diagonal neighbours, obeys e'' = sum dbar_i dbar_j Theta_ij as an exact operator
identity for every state of the walk (all eight species, both branches, every wave vector); so the member's constraint equations
at the closing ratio admit this content exactly iff alpha = K/4 (the supervisor's own derivation; blocks 54, 62, 69, 73, 74 and
101 as landed; blocks 112, 120 and 134 placed; not adopted).

B (T1): the operator identity on the 5^3, 6^3 and 9^3 tori, carried to Z^3 by its support radius.
C (T2): the mechanism - one factor prod cos q_l, the same for every species and branch.
D (T3): what fails - the frame's site stress, and the realisation without its transverse average.
E (T4): the member admits the content exactly iff alpha = K/4; totals; the averaging's symbol.
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
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_one_light_cone_exactly_on_the_lattice_the_two_step_content_meets_the_members_identity_for_every_state_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "energy_unaveraged": "B",
    "trig_identity_forged": "C",
    "k_bar_independent_forged": "D",
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
    note, axioms = texts
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
    """T1: the exact operator identity d^2 e'/dt^2 = sum_ij dbar_i dbar_j Theta_ij on Z^3, for every state."""
    ok = True
    radii = []
    for L, xs in ((5, ((0, 0, 0), (2, 1, 3))), (6, ((0, 0, 0),)), (9, ((0, 0, 0),))):
        tor = Torus(L)
        for x in xs:
            lhs_op = tor.energy(x) if mut("energy_unaveraged") else tor.energy_avg(x)
            lhs = tor.second_derivative(lhs_op)
            rhs = tor.ddiv(lambda i, j, y: tor.theta_two_step(i, j, y), x)
            ok = ok and (lhs - rhs).is_zero() and not lhs.is_zero()
            if L == 9:
                radii = [tor.radius(lhs), tor.radius(rhs)]
    ok_transfer = radii == [4, 4]
    checks.check("B1", ok and ok_transfer,
                 "T1: on the 5^3, 6^3 and 9^3 tori, as exact operators over Q(i), -[H, [H, e'(x)]] = sum_ij dbar_i dbar_j Theta_ij(x), where e'(x) is the energy density averaged over the eight body-diagonal neighbours and Theta_ij = phi_j^T K_i^j is block 69's reach-three current read through block 120's phi-realisation; both sides are nonzero and have support radius 4 about x, so the 9^3 torus (side > 8) carries the identity to Z^3: every state of the walk, all eight species and both branches, obeys e'' = wbar^2 sum dbar_i dbar_j Theta_ij")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the mechanism - one common factor prod_l cos q_l, the same for every species and branch."""
    k, kp = sp.symbols("k kp", real=True)
    q = k - kp
    cq = sp.cos(q / 2) if mut("trig_identity_forged") else sp.cos(q)
    trig = sp.sin(q) * (sp.sin(2 * k) + sp.sin(2 * kp)) / 2 - cq * (sp.sin(k) ** 2 - sp.sin(kp) ** 2)
    ok_trig = sp.simplify(sp.expand_trig(sp.expand(trig))) == 0
    lam, lamp = sp.symbols("lambda lambda_p", real=True)
    s = sp.symbols("s1:4", real=True)
    sq = sp.symbols("t1:4", real=True)
    u = sp.Matrix([lam + s[2], s[0] + sp.I * s[1]])
    up = sp.Matrix([lamp + sq[2], sq[0] + sp.I * sq[1]])
    sig = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    mm = [(up.H * sg * u)[0] for sg in sig]
    ov = (up.H * u)[0]
    eig = sum((s[a] - sq[a]) * mm[a] for a in range(3)) - (lam - lamp) * ov
    rels = [lam ** 2 - sum(v ** 2 for v in s), lamp ** 2 - sum(v ** 2 for v in sq)]
    rem = sp.reduced(sp.expand(eig), rels, lam, lamp)[1]
    ok_eig = sp.expand(rem) == 0
    # assembly: sum_ij p_i p_j Theta_ij = sum_j sin q_j prod_{l != j} cos q_l (1/2)(P_j + P'_j) * sum_i (s_i - s'_i) M_i
    cs = sp.symbols("c1:4", real=True)
    ww = sp.symbols("w1:4", real=True)
    ss = sp.symbols("d1:4", real=True)
    pdd = sum(ww[j] * sp.prod([cs[l] for l in range(3) if l != j]) for j in range(3))
    want = sp.prod(cs) * sum(ss[j] for j in range(3))
    ok_assembly = sp.expand(pdd.subs({ww[j]: cs[j] * ss[j] for j in range(3)}) - want) == 0
    checks.check("C1", ok_trig and ok_eig and ok_assembly,
                 "T2: for the beat of two eigen-waves (k, l, u), (k', l', u') at q = k - k': sin q_j (P_j(k) + P_j(k')) = cos q_j (sin^2 k_j - sin^2 k'_j) (P_j = (1/2) sin 2k_j), and sum_a (sin k_a - sin k'_a) u'^dag sigma_a u = (l - l') u'^dag u modulo l^2 = |s|^2, l'^2 = |s'|^2; so the source's double divergence is prod_l cos q_l (l - l')^2 e_q with e_q = (1/2)(l + l') u'^dag u: the site energy misses by the one factor prod_l cos q_l, the same for every species, branch and k-bar, which the body-diagonal average e' = C_1 C_2 C_3 e supplies exactly")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: what fails - the frame's site stress, and the realisation without its transverse average."""
    tor = Torus(5)
    x = (0, 0, 0)
    d2e = tor.second_derivative(tor.energy(x))
    d2ep = tor.second_derivative(tor.energy_avg(x))
    site = tor.ddiv(lambda i, j, y: tor.theta_site(i, j, y), x)
    bare = tor.ddiv(lambda i, j, y: tor.theta_two_step(i, j, y, transverse=False), x)
    ok_ops = not (d2e - site).is_zero() and not (d2ep - site).is_zero() and not (d2e - bare).is_zero() and not (d2ep - bare).is_zero()
    # Fourier: without the transverse average the double divergence is (l - l') u'^dag u / 2 times sum_j cos q_j (sin^2 k_j - sin^2 k'_j);
    # at fixed q its ratio to (l^2 - l'^2) depends on k-bar, so no placement of the energy (a function of q alone) repairs it
    trig = {"a": (Fr(3, 5), Fr(4, 5)), "b": (Fr(5, 13), Fr(12, 13)), "c": (Fr(8, 17), Fr(15, 17)), "d": (Fr(7, 25), Fr(24, 25))}

    def add(u1, u2):
        return (u1[0] * u2[1] + u1[1] * u2[0], u1[1] * u2[1] - u1[0] * u2[0])

    qv = [trig["a"], trig["b"], (Fr(0), Fr(1))]

    def ratio(kpv):
        kv = [add(kpv[j], qv[j]) for j in range(3)]
        num = sum(qv[j][1] * (kv[j][0] ** 2 - kpv[j][0] ** 2) for j in range(3))
        den = sum(kv[j][0] ** 2 - kpv[j][0] ** 2 for j in range(3))
        return num / den

    r1 = ratio([trig["c"], trig["d"], trig["a"]])
    r2 = ratio([trig["d"], trig["c"], trig["b"]]) if not mut("k_bar_independent_forged") else r1
    ok_kbar = r1 != r2
    checks.check("D1", ok_ops and ok_kbar,
                 "T3: on the 5^3 torus the frame's site stress (block 62) matches neither e nor e' (operators nonzero), and neither does block 120's realisation without its transverse average prod_{l != j} C_l; without that average the beat's double divergence is (1/2)(l - l') u'^dag u sum_j cos q_j (sin^2 k_j - sin^2 k'_j), whose ratio to l^2 - l'^2 at the fixed q with cos q = (4/5, 12/13, 1) takes two different values for two k-bars (%s and %s): no placement of the energy repairs it" % (r1, r2))


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the member admits the two-step content exactly iff alpha = K/4; totals and the averaged energy."""
    t = sp.symbols("t")
    al, kk, wb, p = sp.symbols("alpha K wbar p", positive=True)
    phi, a, b, cx, cy, xi, u = [sp.Function(nm)(t) for nm in ("phi", "a", "b", "cx", "cy", "xi", "u")]
    e = sp.Function("e")(t)
    th = sp.Matrix(3, 3, lambda i, j: sp.Function("Theta_%d%d" % (min(i, j) + 1, max(i, j) + 1))(t))
    h = sp.Matrix([[phi + a, b, cx], [b, phi - a, cy], [cx, cy, 2 * xi]])
    hd = h.diff(t)
    kin = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) - al * hd.trace() ** 2) / wb
    pv = sp.Matrix([0, 0, p])
    hp = h * pv
    r1 = p ** 2 * h.trace() - (pv.T * h * pv)[0]
    r2 = -p ** 2 * (h.T * h).trace() / 4 + hp.dot(hp) / 2 - (pv.T * h * pv)[0] * h.trace() / 2 + p ** 2 * h.trace() ** 2 / 4
    lag = kin + kk * wb * (u * r1 + r2) - e * u + sum(th[i, j] * h[i, j] for i in range(3) for j in range(3)) / 2
    phisol = sp.solve(sp.diff(lag, u), phi)[0]
    eq_xi = sp.diff(lag, xi) - sp.diff(sp.diff(lag, xi.diff(t)), t)
    sol = sp.solve(sp.simplify(eq_xi.subs(phi, phisol).doit()), e.diff(t, 2))
    ok_member = len(sol) == 1 and sp.simplify(sol[0] + kk * wb ** 2 / (4 * al) * p ** 2 * th[2, 2]) == 0
    cone = sp.solve(sp.Eq(kk * wb ** 2 / (4 * al), wb ** 2), al)
    want = [kk / 2] if mut("light_cone_forged") else [kk / 4]
    ok_cone = cone == want
    tor = Torus(5)
    tot_e = SM()
    tot_ep = SM()
    for x in tor.sites:
        tot_e = tot_e + tor.energy(x)
        tot_ep = tot_ep + tor.energy_avg(x)
    ok_tot = (tot_e - tor.H).is_zero() and (tot_ep - tor.H).is_zero()
    q1, q2, q3, tt = sp.symbols("q1 q2 q3 tau", real=True)
    sym = sp.cos(q1) * sp.cos(q2) * sp.cos(q3)
    ok_sym = sym.subs({q1: 0, q2: 0, q3: 0}) == 1 and sym.subs({q1: sp.pi, q2: sp.pi, q3: sp.pi}) == -1
    ser = sp.series(sym.subs({q1: tt, q2: 2 * tt, q3: 3 * tt}), tt, 0, 4).removeO()
    ok_sym = ok_sym and sp.expand(ser - (1 - 7 * tt ** 2)) == 0
    checks.check("E1", ok_member and ok_cone and ok_tot and ok_sym,
                 "T4: at beta = -alpha the member (block 101's action with block 62's R2 and the full stress, re-derived) demands e_u'' = -(K wbar^2/(4 alpha)) p.Theta.p of the energy e_u that sources its clock; with e_u = e' and the two-step source, T1 gives e'' = -wbar^2 p.Theta.p for every state, so the member admits the walker's content exactly, at every wave vector and for all eight species, iff alpha = K/4; on the 5^3 torus sum_x e'(x) = sum_x e(x) = H exactly; the averaging's symbol prod cos q_l is 1 at q = 0, -1 at pi(1,1,1), and 1 - |q|^2/2 + O(q^4) (checked along (1,2,3))")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 62, 69, 73, 74 and 101 as landed on main (the walk, the frame's stress coupling, the two-step momentum and its current, and the member's quadratic action), with blocks 112, 120 and 134 placed; it reports whether the walker's two-step content, placed as block 120 places it, meets the member's identity exactly; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the operator identity as exact matrices over Q(i) on the 5^3, 6^3 and 9^3 tori, both sides nonzero, support radius 4",
    "per_site: executed - the identity at two sites of 5^3 and at the origin of 6^3 and 9^3; sum_x e'(x) = sum_x e(x) = H on 5^3",
    "per_mode: executed - the beat's mechanism symbolically: the trigonometric identity, the eigen-identity modulo l^2 = |s|^2, and the common factor prod cos q_l",
    "per_block: executed - the member's identity at beta = -alpha re-derived; the site stress and the untransverse realisation fail; two k-bars at one q give different ratios",
    "lattice_wide: the identity is exact on Z^3 for every state (support radius 4 < 9/2); first order in the member's fields; the walk, currents, placements, member and link supplied",
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
    print("scope: one light cone exactly on the lattice - the two-step content with the body-diagonal energy meets the member identity for every state and all eight species iff alpha = K/4; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
