#!/usr/bin/env python3
"""Exact checks: the books admit one rest energy - with block 77's staggered mass the averaged energy still flows exactly as
the carried two-step momentum and both momentum laws keep their stresses, so massive content is exact content for the member
iff alpha = K/4; among the eight site terms 1, eps, sigma_a, eps sigma_a only the staggered mass keeps the energy law with the
two-step momentum; a constant offset breaks the books for every local placement (the supervisor's own derivation; blocks 54,
73, 77 and 119 as landed or placed; blocks 136 and 137 placed; not adopted).

B (T1): the staggered mass keeps the books (6^3 and 10^3).
C (T2): the eight site terms.
D (T3): the mechanism, and the offset.
E (T4): massive content and the member.
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
    "docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "coin_mass_in_place": "B",
    "offset_admitted_forged": "C",
    "coin_mass_current_forged": "D",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its rest energy, the currents and their placements, the member and the source link are supplied; the memo does not define a time metric)")


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

    def site_term(self, fn):
        """a site-local term: sum_x |x><x| (x) V(x), V(x) a 2x2 coin matrix given as a dict {(c, d): value}"""
        M = SM()
        for x in self.sites:
            for (c, d), v in fn(x).items():
                if v != GZ:
                    M.add_entry(2 * self.n(x) + c, 2 * self.n(x) + d, v)
        return M

    def energy_with(self, Hm, x):
        pr = self.pos_op([(x, x, gq(1))])
        return (pr * Hm + Hm * pr).scale(gq(Fr(1, 2)))

    def energy_with_avg(self, Hm, x):
        out = SM()
        for sg in product((1, -1), repeat=3):
            out = out + self.energy_with(Hm, (x[0] + sg[0], x[1] + sg[1], x[2] + sg[2]))
        return out.scale(gq(Fr(1, 8)))

    def energy_defect(self, M, x):
        """i[H + M, e'_{H+M}(x)] + sum_j dbar_j P''_j(x)"""
        Hm = self.H + M
        e = self.energy_with_avg(Hm, x)
        lhs = (Hm * e - e * Hm).scale(gq(0, 1))
        return lhs + self.div_bond(lambda j, y: self.mom_bond(j, y), x)

    def radius(self, m):
        L = self.L
        best = 0
        for r, row in m.d.items():
            for idx in [r] + list(row):
                nn = idx // 2
                x = (nn % L, (nn // L) % L, nn // (L * L))
                best = max(best, max(min(v, L - v) for v in x))
        return best










def eps_site(x):
    return (-1) ** sum(x)


ID2 = {(0, 0): gq(1), (1, 1): gq(1)}


def coin_scaled(coin, s):
    return {k: gmul(v, s) for k, v in coin.items()}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the staggered rest energy keeps the books exactly - same momentum, same stress."""
    ok = True
    radii = []
    for L, ms in ((6, (Fr(3, 4), Fr(5, 2))), (10, (Fr(3, 4),))):
        tor = Torus(L)
        x = (0, 0, 0)
        for m in ms:
            coin = SIGC[2] if mut("coin_mass_in_place") else ID2
            M = tor.site_term(lambda y: coin_scaled(coin, gq(m * eps_site(y))))
            Hm = tor.H + M
            d_e = tor.energy_defect(M, x)
            ok = ok and d_e.is_zero()
            for j in range(3):
                dp = (Hm * tor.mom_bond(j, x) - tor.mom_bond(j, x) * Hm).scale(gq(0, 1))
                ok = ok and (dp + tor.div_bond(lambda i, y: tor.theta_two_step(i, j, y), x)).is_zero()
                dq = (Hm * tor.q_avg(j, x) - tor.q_avg(j, x) * Hm).scale(gq(0, 1))
                ok = ok and (dq + tor.div_bond(lambda i, y: tor.theta_two_step(j, i, y), x)).is_zero()
            if L == 10:
                e_avg = tor.energy_with_avg(Hm, x)
                lhs = (Hm * e_avg - e_avg * Hm).scale(gq(0, 1))
                radii = [tor.radius(lhs)]
    checks.check("B1", ok and radii and radii[0] <= 4,
                 "T1: with block 77's staggered rest energy m eps (m = 3/4 and 5/2 on 6^3, m = 3/4 on 10^3), as exact operators over Q(i): i[H + m eps, e'_m] = - sum_j dbar_j P''_j with e'_m = C_1 C_2 C_3 Re psi^dag (H + m eps) psi and the same carried two-step momentum P''; i[H + m eps, P''_j] = - sum_i dbar_i Theta_ij and i[H + m eps, Q_j] = - sum_i dbar_i Theta_ji with the same stress; support radius at most 4 on 10^3 (side > 8), so the massive walker keeps the books on Z^3")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: among the eight site terms 1, eps, sigma_a, eps sigma_a, only the staggered mass keeps the energy law."""
    tor = Torus(6)
    x = (0, 0, 0)
    basis = [("1", lambda y: ID2), ("eps", lambda y: coin_scaled(ID2, gq(eps_site(y))))]
    for a in range(3):
        basis.append(("sigma_%d" % (a + 1), (lambda aa: (lambda y: SIGC[aa]))(a)))
        basis.append(("eps sigma_%d" % (a + 1), (lambda aa: (lambda y: coin_scaled(SIGC[aa], gq(eps_site(y)))))(a)))
    defects = {}
    for name, fn in basis:
        defects[name] = tor.energy_defect(tor.site_term(fn), x)
    zero = [name for name, dmat in defects.items() if dmat.is_zero()]
    # the seven nonzero defects are linearly independent over Q(i): rank of their entry vectors
    names = [n for n in defects if n != "eps"]
    keys = sorted({(r, c) for n in names for r, row in defects[n].d.items() for c in row})
    rows = []
    for n in names:
        rows.append([sp.Rational(defects[n].d.get(r, {}).get(c, GZ)[0]) + sp.I * sp.Rational(defects[n].d.get(r, {}).get(c, GZ)[1]) for (r, c) in keys[:200]])
    rank = sp.Matrix(rows).rank()
    want_zero = ["eps"] if not mut("offset_admitted_forged") else ["eps", "1"]
    checks.check("C1", zero == want_zero and rank == 7,
                 "T2: on 6^3 the energy law's defect i[H + M, e'_{H+M}] + div P'' is linear in a site term M (the term commutes with its own density); for the eight terms 1, eps, sigma_a, eps sigma_a it vanishes only for eps, and the other seven defects are linearly independent (rank 7 over Q(i) on 200 entries): with the carried two-step momentum (block 73: the only covariant conserved one of reach two), the books admit exactly one site rest energy, the staggered mass; a constant offset, a uniform coin mass and a staggered coin mass each break them")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the mechanism - (H + m eps)^2 = H^2 + m^2, so E dE/dk_j = sin k_j cos k_j, the two-step momentum, at every k."""
    tor = Torus(6)
    m = Fr(3, 4)
    M = tor.site_term(lambda y: coin_scaled(ID2, gq(m * eps_site(y))))
    Hm = tor.H + M
    anti = (tor.H * M + M * tor.H).is_zero()
    sq = (Hm * Hm - tor.H * tor.H - tor.site_term(lambda y: coin_scaled(ID2, gq(m * m)))).is_zero()
    k1, k2, k3, mm = sp.symbols("k1 k2 k3 m", real=True)
    ks = (k1, k2, k3)
    E2 = sum(sp.sin(k) ** 2 for k in ks) + mm ** 2
    ok_sym = all(sp.simplify(sp.diff(E2, ks[j]) / 2 - sp.sin(ks[j]) * sp.cos(ks[j])) == 0 for j in range(3))
    E2c = sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + (sp.sin(k3) + mm) ** 2
    if mut("coin_mass_current_forged"):
        E2c = E2
    ok_coin = sp.simplify(sp.diff(E2c, k3) / 2 - sp.sin(k3) * sp.cos(k3)) != 0
    sv = sp.Matrix([[sp.sin(k3), sp.sin(k1) - sp.I * sp.sin(k2)], [sp.sin(k1) + sp.I * sp.sin(k2), -sp.sin(k3)]])
    vel = sp.Matrix([[0, 1], [1, 0]]) * sp.cos(k1)
    ok_vel = sp.simplify(sv * vel - vel * sv) != sp.zeros(2, 2)
    checks.check("D1", anti and sq and ok_sym and ok_coin and ok_vel,
                 "T3: m eps anticommutes with H, so (H + m eps)^2 = H^2 + m^2 exactly (6^3), the dispersion E^2 = |sin k|^2 + m^2, and each wave's energy current E dE/dk_j = sin k_j cos k_j is its two-step momentum at every k, as for the massless walker; a uniform coin mass m sigma_3 shifts sin k_3 to sin k_3 + m and its current (sin k_3 + m) cos k_3 is not the two-step momentum; a constant offset V adds V times the velocity sigma_j cos k_j to the total current, and the velocity does not commute with sigma.s, so by block 137 T3 no local placement keeps the books with an offset: the energy that sources the member is measured from the middle of the spectrum")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: massive content is exact content for the member iff alpha = K/4 (block 136's constraints)."""
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
    c_z = el(nz)
    phidot = sp.solve(c_z, phi.diff(t))[0]
    cond3 = sp.simplify(e.diff(t) - 2 * kk * wb * p ** 2 * phidot)
    ok3 = sp.simplify(cond3 - (e.diff(t) - kk * wb ** 2 / (4 * al) * p * pm[2])) == 0
    cone = sp.solve(sp.Eq(kk * wb ** 2 / (4 * al), wb ** 2), al)
    want = [kk / 2] if mut("light_cone_forged") else [kk / 4]
    checks.check("E1", ok3 and cone == want,
                 "T4: block 136's member with a bond shift at beta = -alpha keeps its clock constraint iff e' = (K wbar^2/(4 alpha)) p P_z; by T1 the massive walker's averaged energy flows as wbar^2 times the same momentum, so massive content is exact content for the member iff alpha = K/4: the rest energy does not move the light cone; the massive walker's waves are slower than wbar, but its books carry the coefficient wbar^2")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 73 and 77 as landed on main (the walk, the two-step momentum and the staggered rest energy), with blocks 119, 136 and 137 placed; it reports which rest energies keep the books that the member needs; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the energy and momentum laws with the staggered mass as exact matrices over Q(i) on 6^3 (two masses) and 10^3, support radius at most 4",
    "per_site: executed - the energy-law defect for each of the eight site terms on 6^3, and their rank",
    "per_mode: executed - (H + m eps)^2 = H^2 + m^2; the plane-wave currents with the staggered and the coin mass; the velocity against sigma.s",
    "per_block: executed - the member's clock constraint with a bond shift and the solve",
    "lattice_wide: exact on Z^3 for every state at uniform rates; site terms only; the walk, rest energy, currents, member and link supplied",
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
    print("scope: the books admit one rest energy - the staggered mass keeps them exactly, so massive content meets the member iff alpha = K/4; other site terms and offsets break them; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
