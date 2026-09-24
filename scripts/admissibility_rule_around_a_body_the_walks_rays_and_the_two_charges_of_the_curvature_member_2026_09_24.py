#!/usr/bin/env python3
"""Exact checks: around a body the walk's rays in the curvature member of block 60 are the comparator's at every order exactly
when the body's two charges agree, and the charges agree only when the content's hop energy balances its slowed clocks
(supervisor's derivation with a refereed probes result for the log-linear completion; all clauses supplied; not adopted).

B (T1): the exterior fields chi = 1 + a/r, N = 1 - p/r; long-wave rays of E = (w/l)|k| have the index chi^3/N and keep x x k.
C (T2): the two charges exactly on a box: Q = sum e/(8K w chi), P = sum (e + 2 tau)/(8K chi); P - Q; bodies at rest; hop content; balance.
D (T3): the capture threshold min_r (r + a)^3/(r(r - p)) and its growth with the charge ratio at a fixed first-order turn.
E (T4, T5): the turn at every order; the second-order coefficient; the log-linear completion's tree-function coefficients.
Exact arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_around_a_body_the_walks_rays_match_the_comparators_at_every_order_exactly_when_its_two_charges_agree_and_they_agree_only_when_hop_energy_balances_the_slowed_clocks_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "index_power_forged": "B",
    "hop_energy_counted_once": "C",
    "capture_root_sign_forged": "D",
    "second_order_ignores_the_square": "E",
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


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


def about_sym(x) -> str:
    """A real sympy number to three places, rounded by exact comparison (no floating point)."""
    n = int(sp.floor(sp.sympify(x) * 1000 + sp.Rational(1, 2)))
    return about(F(n, 1000))


def add(s, e):
    return (s[0] + e[0], s[1] + e[1], s[2] + e[2])


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the clocks, the lengths, the walk and the member are supplied clauses)")


# ============================================================================================ family B
RR, AA, PP, MM = sp.symbols("r a p M", positive=True)


def radial_laplacian(f, r):
    return sp.diff(r ** 2 * sp.diff(f, r), r) / r ** 2


def family_b(checks: Checks) -> None:
    """T1: the exterior of a spherical body in the curvature member, and the index its long-wave rays see."""
    r, a, p, m = RR, AA, PP, MM
    chi = 1 + a / r
    nf = 1 - p / r
    harmonic = sp.simplify(radial_laplacian(chi, r)) == 0 and sp.simplify(radial_laplacian(nf, r)) == 0
    rate = nf / chi
    length = chi ** 2
    index = sp.simplify(length / rate) if not mut("index_power_forged") else sp.simplify(chi ** 2 / nf)
    target = (r + a) ** 3 / (r ** 2 * (r - p))
    checks.check("B1", harmonic and sp.simplify(index - target) == 0,
                 "T1: outside a spherical body the curvature member's fields are chi = 1 + a/r and N = w chi = 1 - p/r (both harmonic, both 1 far away); with lengths l = chi^2 and rates w = N/chi a bond is crossed at w/l, so long-wave rays of E = (w/l)|k| see the index n = l/w = chi^3/N = (r + a)^3/(r^2 (r - p))")

    x = sp.symbols("x1:4", real=True)
    kk = sp.symbols("k1:4", real=True)
    c = sp.Function("c")
    rad = sp.sqrt(sum(xi ** 2 for xi in x))
    kn = sp.sqrt(sum(ki ** 2 for ki in kk))
    ham = c(rad) * kn
    xdot = [sp.diff(ham, ki) for ki in kk]
    kdot = [-sp.diff(ham, xi) for xi in x]
    lvec = [x[1] * kk[2] - x[2] * kk[1], x[2] * kk[0] - x[0] * kk[2], x[0] * kk[1] - x[1] * kk[0]]
    ldot = [sum(sp.diff(li, xi) * xd for xi, xd in zip(x, xdot)) + sum(sp.diff(li, ki) * kd for ki, kd in zip(kk, kdot)) for li in lvec]
    hdot = sum(sp.diff(ham, xi) * xd for xi, xd in zip(x, xdot)) + sum(sp.diff(ham, ki) * kd for ki, kd in zip(kk, kdot))
    parallel = all(sp.simplify(xdot[i] * kk[j] - xdot[j] * kk[i]) == 0 for i in range(3) for j in range(3))
    checks.check("B2", all(sp.simplify(v) == 0 for v in ldot) and sp.simplify(hdot) == 0 and parallel,
                 "T1: for H = c(|x|)|k| the ray moves along k, and E and x x k are kept exactly; with |k| = E n, n = 1/c, this is r n sin(phi) = b along every ray (the invariant of rays in a spherical index), b the impact parameter")

    s = sp.symbols("s", positive=True)
    ser = sp.series(target.subs(r, 1 / s), s, 0, 4).removeO()
    nu = [sp.expand(ser.coeff(s, j)) for j in range(4)]
    want = [1, 3 * a + p, 3 * a ** 2 + 3 * a * p + p ** 2, a ** 3 + 3 * a ** 2 * p + 3 * a * p ** 2 + p ** 3]
    comp = (1 + m / (2 * r)) ** 2 / ((1 - m / (2 * r)) / (1 + m / (2 * r)))
    same = sp.simplify(target.subs({a: m / 2, p: m / 2}) - comp) == 0
    checks.check("B3", all(sp.expand(nu[j] - want[j]) == 0 for j in range(4)) and same,
                 "T1: n = 1 + (3a + p)/r + (3a^2 + 3ap + p^2)/r^2 + (a + p)^3/r^3 + ...; at p = a = M/2 it is psi^2/alpha with psi = 1 + M/(2r) and alpha = (1 - M/(2r))/(1 + M/(2r)), the comparator's index in its isotropic form, identically")


# ============================================================================================ family C
K = F(3, 4)                                                  # the member's one number; 8K = 6
SIDE = 7                                                     # sites 0..6; walls at 0 and 6; 125 interior sites
ALL_SITES = list(product(range(SIDE), repeat=3))
INTERIOR = [s for s in product(range(1, SIDE - 1), repeat=3)]
INDEX = {s: i for i, s in enumerate(INTERIOR)}
SITE_X = (3, 3, 3)
SITE_Y = (4, 3, 3)


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


def lap(field, s):
    """Lattice Laplacian at s over the bonds that stay inside the box; outside the interior the field is the wall value 1."""
    tot = ZERO
    for e in E6:
        t = add(s, e)
        if min(t) < 0 or max(t) >= SIDE:
            continue
        tot += val(field, t) - val(field, s)
    return tot


def wall_flux(field):
    """Sum over the bonds joining an interior site to a wall of (field - 1) at the interior end."""
    tot = ZERO
    for s in ALL_SITES:
        if s in INDEX:
            continue
        for e in E6:
            t = add(s, e)
            if t in INDEX:
                tot += field[t] - 1
    return tot


def bond_form(nfield, chi):
    """The member's field energy: -8K times the sum over bonds with an interior end of (N_y - N_x)(chi_y - chi_x)."""
    tot = ZERO
    for s in ALL_SITES:
        for e in E3:
            t = add(s, e)
            if max(t) >= SIDE or (s not in INDEX and t not in INDEX):
                continue
            tot += (val(nfield, t) - val(nfield, s)) * (val(chi, t) - val(chi, s))
    return -8 * K * tot


def global_identities(chi, nf, e, tau):
    """Ledger 8KQ = H + F; 4K(P + Q) = H_rest + 2 H_hop; 4K(P - Q) = H_hop - F (homogeneity in the rates and in chi)."""
    pp, qq = -wall_flux(nf), wall_flux(chi)
    h_hop = sum(tau.values(), ZERO)
    h_rest = sum((e[s] - tau[s] for s in INTERIOR), ZERO)
    fld = bond_form(nf, chi)
    ok = (h_rest + h_hop + fld == 8 * K * qq and 4 * K * (pp + qq) == h_rest + 2 * h_hop and 4 * K * (pp - qq) == h_hop - fld)
    return ok, fld, h_hop, h_rest


def configuration(g, qx, qy, sx, sy):
    """chi and N from the charges at the two content sites; the content's derivatives e and tau read off the site equations."""
    chi = {s: 1 + qx * g[SITE_X][s] + qy * g[SITE_Y][s] for s in INTERIOR}
    nf = {s: 1 - sx * g[SITE_X][s] - sy * g[SITE_Y][s] for s in INTERIOR}
    w = {s: nf[s] / chi[s] for s in INTERIOR}
    q = {SITE_X: qx, SITE_Y: qy}
    sg = {SITE_X: sx, SITE_Y: sy}
    e = {s: 8 * K * w[s] * chi[s] * q.get(s, ZERO) for s in INTERIOR}
    tau = {s: (8 * K * chi[s] * sg.get(s, ZERO) - e[s]) / 2 for s in INTERIOR}
    return chi, nf, w, e, tau


def site_equations(chi, nf, w, e, tau, hop_factor=2):
    return all(lap(chi, s) == -e[s] / (8 * K * w[s] * chi[s]) and lap(nf, s) == (e[s] + hop_factor * tau[s]) / (8 * K * chi[s]) for s in INTERIOR)


def identity_rhs(chi, w, e, tau, hop_factor=2):
    return sum(((hop_factor * tau[s] - e[s] * (1 - w[s]) / w[s]) / chi[s] for s in INTERIOR), ZERO) / (8 * K)


def small_box_derivatives(hop_factor) -> bool:
    """On a box of side 4 (8 interior sites), differentiate the member's bond form and a walker's energy symbolically."""
    side = 4
    inner = list(product(range(1, side - 1), repeat=3))
    chi = {s: sp.Symbol(f"c{i}", positive=True) for i, s in enumerate(inner)}
    w = {s: sp.Symbol(f"w{i}", positive=True) for i, s in enumerate(inner)}
    kk = sp.Rational(3, 4)
    v = lambda f, t: f[t] if t in f else sp.Integer(1)
    bonds = []
    for s in product(range(side), repeat=3):
        for e in E3:
            t = add(s, e)
            if max(t) >= side or (s not in chi and t not in chi):
                continue
            bonds.append((s, t))
    nf = {s: w[s] * chi[s] for s in inner}
    field = -8 * kk * sum((v(nf, t) - v(nf, s)) * (v(chi, t) - v(chi, s)) for s, t in bonds)
    inner_bonds = [(s, t) for s, t in bonds if s in chi and t in chi]
    that = {b: sp.Symbol(f"t{i}", real=True) for i, b in enumerate(inner_bonds)}
    rhat = {s: sp.Symbol(f"r{i}", positive=True) for i, s in enumerate(inner)}
    hop = {b: sp.sqrt(w[b[0]] * w[b[1]]) / (chi[b[0]] * chi[b[1]]) * that[b] for b in inner_bonds}
    energy = sum(hop.values()) + sum(w[s] * rhat[s] for s in inner)

    def slap(f, s):
        tot = sp.Integer(0)
        for e in E6:
            t = add(s, e)
            if min(t) < 0 or max(t) >= side:
                continue
            tot += v(f, t) - v(f, s)
        return tot
    ok = True
    for s in inner:
        tau = sum(hop[b] for b in inner_bonds if s in b) / 2
        e_s = w[s] * rhat[s] + tau
        du = sp.simplify(w[s] * sp.diff(energy + field, w[s]) - (e_s + 8 * kk * w[s] * chi[s] * slap(chi, s)))
        dc = sp.simplify(sp.diff(energy + field, chi[s]) - (8 * kk * (w[s] * slap(chi, s) + slap(nf, s)) - hop_factor * tau / chi[s]))
        ok = ok and du == 0 and dc == 0
    return ok


def family_c(checks: Checks) -> None:
    """T2: the two charges, exactly, for any content with fixed-state derivatives e and tau."""
    hop_factor = 2 if not mut("hop_energy_counted_once") else 1
    checks.check("C1", small_box_derivatives(hop_factor),
                 "T2: on a box of side 4, symbolically: for the member's bond form F = -8K sum (N_y - N_x)(chi_y - chi_x) and a walker crossing each bond at sqrt(w_x w_y)/(chi_x chi_y), w_z d(<H> + F)/dw_z = e_z + 8K w_z chi_z (Lap chi)_z and d(<H> + F)/dchi_z = 8K(w_z (Lap chi)_z + (Lap N)_z) - 2 tau_z/chi_z, with e_z = r_z + tau_z and tau_z half the hop energies at z; so a static configuration has (Lap chi)_z = -e_z/(8K w_z chi_z) and (Lap N)_z = (e_z + 2 tau_z)/(8K chi_z) at every site")

    g = green_columns([SITE_X, SITE_Y])
    g0 = g[SITE_X][SITE_X]
    q = F(5, 2)
    chi, nf, w, e, tau = configuration(g, q, ZERO, q / (1 + 2 * q * g0), ZERO)
    w0 = w[SITE_X]
    pp = -wall_flux(nf)
    qq = wall_flux(chi)
    rest = site_equations(chi, nf, w, e, tau) and all(tau[s] == 0 for s in INTERIOR)
    checks.check("C2", rest and qq == q and pp == q * w0 and pp - qq == identity_rhs(chi, w, e, tau, hop_factor) and pp < qq,
                 f"T2: one body at rest (tau = 0, e = m w) in a 7x7x7 box, 8K = 6: every site equation holds at all 125 sites; the walls see Q = {about(qq)} from the lengths and P = Q w_0 = {about(pp)} from N (w_0 = {about(w0)}), and P - Q = (1/8K) sum [2 tau - e(1 - w)/w]/chi exactly: a body at rest has P < Q")

    sx_, sy_ = sp.symbols("sx sy")
    gxx, gxy, gyy = g[SITE_X][SITE_X], g[SITE_X][SITE_Y], g[SITE_Y][SITE_Y]

    def solve_for(qx, qy, extra):
        cx = 1 + qx * gxx + qy * gxy
        cy = 1 + qx * gxy + qy * gyy
        nx = 1 - sx_ * gxx - sy_ * gxy
        ny = 1 - sx_ * gxy - sy_ * gyy
        tx = (8 * K * cx * sx_ - 8 * K * nx * qx) / 2
        ty = (8 * K * cy * sy_ - 8 * K * ny * qy) / 2
        sol = sp.solve([sp.Eq(tx, ty), extra], [sx_, sy_], dict=True)[0]
        return F(str(sol[sx_])), F(str(sol[sy_]))

    qx, qy = F(2), F(1)
    sx, sy = solve_for(qx, qy, sp.Eq(sx_, sp.Rational(3, 2)))
    chi, nf, w, e, tau = configuration(g, qx, qy, sx, sy)
    pp, qq = -wall_flux(nf), wall_flux(chi)
    rpart = {s: e[s] - tau[s] for s in (SITE_X, SITE_Y)}
    ok3 = (site_equations(chi, nf, w, e, tau) and tau[SITE_X] == tau[SITE_Y] > 0 and all(v > 0 for v in rpart.values())
           and pp == sx + sy and qq == qx + qy and pp - qq == identity_rhs(chi, w, e, tau, hop_factor))
    checks.check("C3", ok3,
                 f"T2: content on one bond (rest parts {about(rpart[SITE_X])}, {about(rpart[SITE_Y])} and hop energy {about(2 * tau[SITE_X])} shared by its ends, clocks {about(w[SITE_X])}, {about(w[SITE_Y])}): every site equation holds; the walls see Q = {about(qq)} and P = {about(pp)}; P - Q = {about(pp - qq)} = (1/8K) sum [2 tau - e(1 - w)/w]/chi exactly")

    qx, qy = F(1), F(3, 4)
    sx, sy = solve_for(qx, qy, sp.Eq(sx_ + sy_, qx + qy))
    chi, nf, w, e, tau = configuration(g, qx, qy, sx, sy)
    pp, qq = -wall_flux(nf), wall_flux(chi)
    rpart = {s: e[s] - tau[s] for s in (SITE_X, SITE_Y)}
    balance = sum((2 * tau[s] / chi[s] for s in INTERIOR), ZERO) == sum((e[s] * (1 - w[s]) / (w[s] * chi[s]) for s in INTERIOR), ZERO)
    ok4 = site_equations(chi, nf, w, e, tau) and pp == qq and balance and tau[SITE_X] > 0 and all(v > 0 for v in rpart.values())
    big = F(2)
    sx2, sy2 = solve_for(big, big, sp.Eq(sx_ + sy_, 2 * big))
    chi2, nf2, w2, e2, tau2 = configuration(g, big, big, sx2, sy2)
    slow = all(w2[s] < F(1, 3) for s in (SITE_X, SITE_Y))
    negative_rest = any(e2[s] - tau2[s] < 0 for s in (SITE_X, SITE_Y))
    checks.check("C4", ok4 and slow and negative_rest and site_equations(chi2, nf2, w2, e2, tau2),
                 f"T2: equal charges with hop energy: charges (1, 3/4) with sum sigma = sum Q give P = Q = {about(qq)} exactly, with positive rest parts {about(rpart[SITE_X])}, {about(rpart[SITE_Y])}, hop energy {about(2 * tau[SITE_X])}, clocks {about(w[SITE_X])}, {about(w[SITE_Y])}, and the balance 2 sum tau/chi = sum e(1 - w)/(w chi); with charges (2, 2) the clocks run at {about(w2[SITE_X])}, {about(w2[SITE_Y])} < 1/3 and balance needs a negative rest part")

    e_, t_, w_ = sp.symbols("e tau w", positive=True)
    one_site = sp.solve(sp.Eq(2 * t_, e_ * (1 - w_) / w_), w_)
    massless = sp.solve(sp.Eq(2 * e_, e_ * (1 - w_) / w_), w_)
    r_ = sp.symbols("r", nonnegative=True)
    weak = sp.simplify((r_ + 3 * t_) / (r_ + t_))
    above_third = sp.simplify(e_ / (e_ + 2 * t_) - sp.Rational(1, 3) - 2 * (e_ - t_) / (3 * (e_ + 2 * t_))) == 0
    bound_ok = one_site == [e_ / (e_ + 2 * t_)] and above_third and massless == [sp.Rational(1, 3)] and sp.simplify(weak - 1 - 2 * t_ / (r_ + t_)) == 0
    checks.check("C5", bound_ok,
                 "T2: one content site has P = Q exactly when w = e/(e + 2 tau), which is at least 1/3 whenever 0 <= tau <= e (nonnegative rest part) and equals 1/3 for content with no rest energy; at weak field P/Q = sum (r + 3 tau)/sum (r + tau) = 1 + 2 sum tau/sum e, between 1 (content at rest) and 3 (no rest energy)")

    gids = []
    for cfg in (configuration(g, q, ZERO, q / (1 + 2 * q * g0), ZERO), configuration(g, F(2), F(1), *solve_for(F(2), F(1), sp.Eq(sx_, sp.Rational(3, 2)))),
                configuration(g, F(1), F(3, 4), *solve_for(F(1), F(3, 4), sp.Eq(sx_ + sy_, F(7, 4))))):
        gids.append(global_identities(cfg[0], cfg[1], cfg[3], cfg[4]))
    bal = gids[2]
    checks.check("C6", all(x[0] for x in gids) and bal[1] == bal[2],
                 f"T2(e): for all three configurations the ledger H + F = 8KQ, 4K(P + Q) = H_rest + 2 H_hop and 4K(P - Q) = H_hop - F hold exactly (field energies {', '.join(about(x[1]) for x in gids)}; hop energies {', '.join(about(x[2]) for x in gids)}): the charges agree exactly when the member's field energy equals the content's hop energy, as in the balanced content ({about(bal[1])} = {about(bal[2])})")


# ============================================================================================ family D
RHO = sp.symbols("rho", positive=True)


def family_d(checks: Checks) -> None:
    """T3: capture: the smallest value of r n(r) outside the body, and how it grows with the charge ratio."""
    r, a, p, m, rho = RR, AA, PP, MM, RHO
    fr = (r + a) ** 3 / (r * (r - p))
    root = sp.sqrt(a ** 2 + a * p + p ** 2)
    rstar = a + p + root if not mut("capture_root_sign_forged") else a + p - root
    crit = sp.simplify(sp.diff(fr, r).subs(r, rstar)) == 0
    ratio = sp.simplify(sp.numer(sp.together(sp.diff(sp.log(fr), r))) / (r ** 2 - 2 * (a + p) * r + a * p))
    quad = ratio.is_number and ratio != 0
    other_below = sp.expand(a ** 2 - root ** 2) == -a * p - p ** 2
    outside = sp.simplify(rstar - p - (a + root)) == 0
    checks.check("D1", crit and quad and other_below and outside,
                 "T3: f(r) = r n(r) = (r + a)^3/(r(r - p)) has f'/f = 3/(r + a) - 1/r - 1/(r - p), which vanishes exactly at the roots of r^2 - 2(a + p) r + ap; the larger, r* = a + p + sqrt(a^2 + ap + p^2) = p + a + sqrt(...), lies outside r = p and the smaller inside, so on r > p (where N > 0) f falls to its one minimum at r* and rises to infinity at both ends: a ray with b < f(r*) never turns and reaches the body if the body lies inside r*, b = f(r*) winds onto the circular ray r = r*, b > f(r*) escapes")

    bc = sp.simplify(fr.subs(r, rstar))
    comp_r = sp.simplify(rstar.subs({a: m / 2, p: m / 2}) / m)
    comp_b = sp.simplify(bc.subs({a: m / 2, p: m / 2}) / m)
    checks.check("D2", sp.simplify(comp_r - (2 + sp.sqrt(3)) / 2) == 0 and sp.simplify(comp_b - 3 * sp.sqrt(3)) == 0,
                 f"T3: at equal charges, a = p = M/2 (first-order turn 4M/b): the circular ray sits at r* = (2 + sqrt 3) M/2 and the capture threshold is b_c = 3 sqrt(3) M = {about_sym(comp_b)} M, the comparator's values")

    sub = {a: 2 * m / (3 + rho), p: 2 * m * rho / (3 + rho)}
    bcm = sp.simplify(bc.subs(sub) / m)
    s_ = sp.sqrt(rho ** 2 + rho + 1)
    closed = 2 * (rho + s_ + 2) ** 3 / ((rho + 3) * (s_ + 1) * (rho + s_ + 1))
    vals = {q: sp.nsimplify(sp.simplify(closed.subs(rho, q))) for q in (0, sp.Rational(1, 2), 1, 3)}
    want = {0: sp.Rational(9, 2), sp.Rational(1, 2): 4 * sp.sqrt(7) - sp.Rational(40, 7), 1: 3 * sp.sqrt(3), 3: (70 + 26 * sp.sqrt(13)) / 27}
    same_closed = all(sp.simplify(bcm.subs(rho, q) - closed.subs(rho, q)) == 0 for q in (sp.Rational(1, 3), 2, 5))
    envelope = sp.simplify(sp.diff(fr, a) * sp.diff(sub[a], rho) + sp.diff(fr, p) * sp.diff(sub[p], rho) - 6 * m * fr / (3 + rho) ** 2 * (1 / (r - p) - 1 / (r + a)))
    lim = sp.limit(closed, rho, sp.oo)
    checks.check("D3", all(sp.simplify(vals[q] - want[q]) == 0 for q in want) and same_closed and envelope == 0 and lim == 8,
                 f"T3: at a fixed first-order turn 4M/b (3a + p = 2M) and charge ratio rho = p/a = P/Q, b_c/M = 2(rho + s + 2)^3/((rho + 3)(s + 1)(rho + s + 1)), s = sqrt(rho^2 + rho + 1): 9/2 at rho = 0, 4 sqrt 7 - 40/7 = {about_sym(want[sp.Rational(1, 2)])} at 1/2, 3 sqrt 3 at 1, (70 + 26 sqrt 13)/27 = {about_sym(want[3])} at 3, tending to 8; its rho-derivative is (6M f/(3 + rho)^2)(1/(r* - p) - 1/(r* + a)) > 0 at r* (the minimum moves only through a and p): the threshold rises with the charge ratio")

    kk, amp = sp.symbols("k A", positive=True)
    fe = r * sp.exp(kk * amp / r)
    crit_e = sp.solve(sp.Eq(sp.diff(fe, r), 0), r)
    checks.check("D4", crit_e == [kk * amp] and sp.simplify(fe.subs(r, kk * amp) - sp.E * kk * amp) == 0,
                 "T5: for the log-linear completion, index e^(kA/r) (k = 1 + beta), r e^(kA/r) has its one minimum at r = kA, so the capture threshold is e k A (e A without lengths, as the probes attempt found; 2 e A with block 59's beta = 1, where the first-order turn is 4A/b)")


# ============================================================================================ family E
ZZ = sp.symbols("z", positive=True)


def moment(n):
    """int_0^1 y^n / sqrt(1 - y^2) dy in closed form."""
    return sp.sqrt(sp.pi) / 2 * sp.gamma(sp.Rational(n + 1, 2)) / sp.gamma(sp.Rational(n, 2) + 1)


def turn_coefficients(f_of_r, order):
    """Coefficients of 1/b^n in the turn chi(b) = 2 int_0^1 (D(b/y) - 1) dy/sqrt(1 - y^2), D = dlog r/dlog F, F = r n(r).

    r(F) is inverted order by order near F = infinity: with z = 1/F, r = (1/z)(1 + c_1 z + c_2 z^2 + ...), and
    D = -(z/r) dr/dz = 1 + sum d_n z^n; then chi_n = 2 d_n I_n."""
    z, r = ZZ, RR
    cs = sp.symbols(f"c1:{order + 2}")
    rr = (1 / z) * (1 + sum(cs[i] * z ** (i + 1) for i in range(order + 1)))
    expr = sp.expand(sp.series(f_of_r.subs(r, rr) * z - 1, z, 0, order + 2).removeO())
    sol = {}
    for i in range(1, order + 2):
        coeff = sp.expand(expr.coeff(z, i).subs(sol))
        sol[cs[i - 1]] = sp.solve(sp.Eq(coeff, 0), cs[i - 1])[0]
    rr = rr.subs(sol)
    dd = sp.expand(sp.series(-z * sp.diff(rr, z) / rr, z, 0, order + 1).removeO())
    return [sp.simplify(2 * dd.coeff(z, n) * moment(n)) for n in range(1, order + 1)]


def family_e(checks: Checks) -> None:
    """T4 and T5: the turn at every order, and the second order against the charge ratio."""
    y = sp.symbols("y", positive=True)
    moments_ok = all(sp.simplify(sp.integrate(y ** n / sp.sqrt(1 - y ** 2), (y, 0, 1)) - moment(n)) == 0 for n in range(0, 7))
    nu1, nu2, nu3 = sp.symbols("nu1 nu2 nu3", real=True)
    r = RR
    general = turn_coefficients(r + nu1 + nu2 / r + nu3 / r ** 2, 3)
    second = general[1] if not mut("second_order_ignores_the_square") else sp.pi * nu2
    ok1 = (moments_ok and sp.simplify(general[0] - 2 * nu1) == 0 and sp.simplify(second - sp.pi * (nu2 + nu1 ** 2 / 2)) == 0
           and sp.simplify(general[2] - sp.Rational(4, 3) * (nu1 ** 3 + 6 * nu1 * nu2 + 3 * nu3)) == 0)
    checks.check("E1", ok1,
                 "T4: with y = b/(r n(r)) along the outward branch the half-turn is int_0^1 (dlog r/dlog F) dy/sqrt(1 - y^2), F = r n; expanding dlog r/dlog F in 1/F and integrating term by term (the moments int_0^1 y^n/sqrt(1 - y^2) dy checked for n <= 6), an index n = 1 + nu1/r + nu2/r^2 + nu3/r^3 + ... turns a ray by 2 nu1/b + pi (nu2 + nu1^2/2)/b^2 + (4/3)(nu1^3 + 6 nu1 nu2 + 3 nu3)/b^3 + ...")

    a, p, m, rho = AA, PP, MM, RHO
    curv = turn_coefficients((r + a) ** 3 / (r * (r - p)), 4)
    want = [2 * (3 * a + p), sp.Rational(3, 2) * sp.pi * (5 * a ** 2 + 4 * a * p + p ** 2), sp.Rational(8, 3) * (42 * a ** 3 + 54 * a ** 2 * p + 27 * a * p ** 2 + 5 * p ** 3),
            sp.Rational(15, 8) * sp.pi * (99 * a ** 4 + 176 * a ** 3 * p + 132 * a ** 2 * p ** 2 + 48 * a * p ** 3 + 7 * p ** 4)]
    comp = [sp.simplify(c.subs({a: m / 2, p: m / 2})) for c in curv]
    comp_want = [4 * m, sp.Rational(15, 4) * sp.pi * m ** 2, sp.Rational(128, 3) * m ** 3, sp.Rational(3465, 64) * sp.pi * m ** 4]
    checks.check("E2", all(sp.simplify(curv[i] - want[i]) == 0 for i in range(4)) and all(sp.simplify(comp[i] - comp_want[i]) == 0 for i in range(4)),
                 "T4: for the curvature member's exterior the turn is 2(3a + p)/b + (3 pi/2)(5a^2 + 4ap + p^2)/b^2 + (8/3)(42a^3 + 54a^2 p + 27ap^2 + 5p^3)/b^3 + (15 pi/8)(99a^4 + ...)/b^4 + ...; at a = p = M/2: 4M/b + (15 pi/4)(M/b)^2 + (128/3)(M/b)^3 + (3465 pi/64)(M/b)^4, the comparator's series")

    sub = {a: 2 * m / (3 + rho), p: 2 * m * rho / (3 + rho)}
    c2 = sp.simplify(curv[1].subs(sub) / (sp.pi * m ** 2))
    closed = 6 * (5 + 4 * rho + rho ** 2) / (3 + rho) ** 2
    slope = sp.simplify(sp.diff(closed, rho) - 12 * (1 + rho) / (3 + rho) ** 3)
    vals = [sp.simplify(closed.subs(rho, q)) for q in (0, 1, 3)]
    checks.check("E3", sp.simplify(c2 - closed) == 0 and slope == 0 and vals == [sp.Rational(10, 3), sp.Rational(15, 4), sp.Rational(13, 3)] and sp.limit(closed, rho, sp.oo) == 6,
                 "T4: at a fixed first-order turn 4M/b and charge ratio rho = P/Q the second-order term is 6 pi (5 + 4 rho + rho^2)/(3 + rho)^2 (M/b)^2, increasing (slope 12(1 + rho)/(3 + rho)^3): 10 pi/3 for rho -> 0, the comparator's 15 pi/4 exactly at rho = 1, 13 pi/3 at rho = 3, tending to 6 pi")

    kk, amp = sp.symbols("k A", positive=True)
    expo = turn_coefficients(r * sp.exp(kk * amp / r), 6)
    lam = [sp.simplify(expo[n - 1] / (kk * amp) ** n) for n in range(1, 7)]
    tree = [sp.simplify(sp.sqrt(sp.pi) * sp.Integer(n) ** n * sp.gamma(sp.Rational(n + 1, 2)) / (sp.factorial(n) * sp.gamma(sp.Rational(n, 2) + 1))) for n in range(1, 7)]
    first = [2, sp.pi, 6, 4 * sp.pi, sp.Rational(250, 9), sp.Rational(81, 4) * sp.pi]
    at_two = [sp.simplify(expo[i].subs({kk: 2, amp: m})) for i in range(3)]
    checks.check("E4", all(sp.simplify(lam[i] - tree[i]) == 0 and sp.simplify(lam[i] - first[i]) == 0 for i in range(6))
                 and at_two == [4 * m, 4 * sp.pi * m ** 2, 48 * m ** 3],
                 "T5: for the index e^(kA/r) the same expansion gives (kA/b)^n times sqrt(pi) n^n Gamma((n + 1)/2)/(n! Gamma(n/2 + 1)) = 2, pi, 6, 4 pi, 250/9, 81 pi/4 (the probes attempt's tree-function coefficients, by another route); with lengths (k = 2) at the same first-order turn 4M/b it gives 4 pi (M/b)^2 and 48 (M/b)^3 against the comparator's 15 pi/4 and 128/3")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses, block 60's curvature member for lengths and rates and the long-wave ray model of the walk; it reports how the walk's rays bend around a body at every order and what makes the body's two charges agree; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Lambert", "Bouguer", "Buchdahl", "Beig", "Keeton", "Petters", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the exterior fields, the index and the ray invariants (symbolic); the site equations from the member's bond form and a walker's energy on a side-4 box (symbolic)",
    "per_site: executed - every site equation at all 125 interior sites of a 7x7x7 box for a body at rest and for content on one bond, generic and balanced; the charges as wall fluxes; the ledger and the global identities",
    "per_mode: executed - the turn's coefficients to fourth order for the curvature member and to sixth for the log-linear completion; the comparator's series at equal charges",
    "per_block: executed - the capture threshold in closed form against the charge ratio, its derivative, its values and limit; the second-order coefficient against the charge ratio",
    "lattice_wide: T2 on any box with walls held at w = l = 1 for any content with fixed-state derivatives e and tau; T1, T3-T5 in the continuum exterior of a spherical body in the long-wave ray model of E = (w/l)|k|; the member, its number K, the ray model and the content are supplied, and whether bound walkers balance their charges is not derived",
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
    print("scope: around a body the curvature member bends long-wave rays with the index chi^3/N = (r + a)^3/(r^2 (r - p)); at equal charges p = a this is the comparator's index at every order (capture 3 sqrt(3) M, 15 pi/4 at second order); P - Q = (1/8K) sum [2 tau - e(1 - w)/w]/chi exactly, so a body at rest has P < Q and equal charges need hop energy to balance the slowed clocks; the log-linear completion gives capture e k A and 4 pi at second order with lengths; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
