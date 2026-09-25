#!/usr/bin/env python3
"""Exact checks: the curvature member's constraint algebra closes on the lattice, at linear order, exactly when beta = -alpha, and at
that ratio the walker's own stationary states cannot be its content (a harvest block from three Grok-refereed probes attempts; blocks 60,
62 and 101 as landed supplied; not adopted).

B (T1): the linear bracket of two lapse constraints equals the relabelling generator on a 4^3 torus iff c = 1/2 (beta = -alpha), with
        face terms timed symmetrically; one-corner timing and other ratios fail; the obstruction lies outside the relabellings (3^3 rank).
C (T2): at beta = -alpha the gradient relabelling changes the action by a total derivative plus zeta [(2 alpha/(K wbar^2)) e'' + p.Theta.p/2].
D (T3): the equations of motion at alpha + beta = 0 give e'' = -(K wbar^2/(4 alpha)) p.Theta.p, the second derivative of continuity.
E (T4): a stationary two-wave state of the walk has e'' = 0 and p.Theta.p != 0: no solution at beta = -alpha, no static solution at all.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_THE_CURVATURE_MEMBERS_CONSTRAINT_ALGEBRA_CLOSES_ON_THE_LATTICE_ONLY_AT_BETA_EQUALS_MINUS_ALPHA_AND_THERE_THE_WALKERS_OWN_STATES_CANNOT_BE_ITS_CONTENT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_curvature_members_constraint_algebra_closes_on_the_lattice_only_at_beta_equals_minus_alpha_and_there_the_walkers_own_states_cannot_be_its_content_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "one_corner_taken_to_close": "B",
    "noether_source_dropped": "C",
    "identity_speed_forged": "D",
    "stress_taken_divergence_free": "E",
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
PAIRS = ((0, 1), (0, 2), (1, 2))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the clocks, the lengths, the kinetic term and the walk are supplied clauses)")


# ============================================================================================ family B
def unit(j):
    return tuple(1 if k == j else 0 for k in range(3))


def torus(side):
    sites = list(product(range(side), repeat=3))

    def sh(x, v, s=1):
        return tuple((x[k] + s * v[k]) % side for k in range(3))
    return sites, sh


def lapse_bracket(sites, sh, n, m, alpha, c, timing):
    """Coefficients of the momenta in B[N, M] = sum over strains of dR1[N]/dh times dkin[M]/dP (block 62's staggered placement)."""
    coef = {}
    for x in sites:
        second = [n[sh(x, unit(i))] - 2 * n[x] + n[sh(x, unit(i), -1)] for i in range(3)]
        grads = [-sum(second, ZERO) + second[j] for j in range(3)]           # dR1[N]/dh_jj(x), R1 = p^2 tr h - p.h.p
        total = sum(grads, ZERO)
        for j in range(3):
            coef[("d", x, j)] = m[x] / (2 * alpha) * (grads[j] - c * total)
    for y in sites:
        for (i, j) in PAIRS:
            corners = {"four": [y, sh(y, unit(i)), sh(y, unit(j)), sh(sh(y, unit(i)), unit(j))],
                       "diagonal": [y, sh(sh(y, unit(i)), unit(j))], "antidiagonal": [sh(y, unit(i)), sh(y, unit(j))], "one": [y]}[timing]
            mean = sum((m[z] for z in corners), ZERO) / len(corners)
            mixed = n[y] - n[sh(y, unit(i))] - n[sh(y, unit(j))] + n[sh(sh(y, unit(i)), unit(j))]
            coef[("f", y, (i, j))] = mean / (4 * alpha) * 2 * mixed
    return coef


def relabelling(sites, sh, xi):
    """Coefficients of the momenta in G[xi] = sum P.(d_i xi_j + d_j xi_i), xi_j on the bond from x to x + e_j."""
    coef = {}
    for x in sites:
        for j in range(3):
            coef[("d", x, j)] = 2 * (xi[(x, j)] - xi[(sh(x, unit(j), -1), j)])
    for y in sites:
        for (i, j) in PAIRS:
            coef[("f", y, (i, j))] = xi[(sh(y, unit(i)), j)] - xi[(y, j)] + xi[(sh(y, unit(j)), i)] - xi[(y, i)]
    return coef


def closing_field(sites, sh, n, m, alpha, kk):
    return {(x, j): kk / (4 * alpha) * (n[sh(x, unit(j))] * m[x] - n[x] * m[sh(x, unit(j))]) for x in sites for j in range(3)}


def linear_bracket(sites, sh, n, m, alpha, kk, c, timing):
    b1 = lapse_bracket(sites, sh, n, m, alpha, c, timing)
    b2 = lapse_bracket(sites, sh, m, n, alpha, c, timing)
    return {k: kk * (b1[k] - b2[k]) for k in b1}


def rank_of(rows):
    rows = [list(r) for r in rows]
    rank, col = 0, 0
    ncols = len(rows[0]) if rows else 0
    while rank < len(rows) and col < ncols:
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][col]
        rows[rank] = [v / pv for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [a - fac * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
        col += 1
    return rank


def family_b(checks: Checks) -> None:
    """T1: closure of the lapse constraints onto the strains' relabelling, on the lattice, at linear order."""
    alpha, kk = F(3, 7), F(5, 11)
    sites, sh = torus(4)
    lapses = [({x: F((2 * x[0] + 3 * x[1] + 5 * x[2] + 1) * (x[0] + 1) % 7 - 3) for x in sites}, {x: F((x[0] * x[1] + 4 * x[2] + 2) % 5 - 2) for x in sites}),
              ({x: F((x[0] + 2 * x[1] * x[2] + 3) % 6 - 2) for x in sites}, {x: F((3 * x[0] * x[2] + x[1] + 1) % 7 - 3) for x in sites}),
              ({x: F(x[0] * x[0] - x[1] + 2 * x[2]) for x in sites}, {x: F((x[0] + x[1] + x[2]) % 3) for x in sites})]
    closing = ("four", "diagonal", "antidiagonal") + (("one",) if mut("one_corner_taken_to_close") else ())
    ok = True
    for n, m in lapses:
        g = relabelling(sites, sh, closing_field(sites, sh, n, m, alpha, kk))
        for timing in closing:
            lin = linear_bracket(sites, sh, n, m, alpha, kk, F(1, 2), timing)
            ok = ok and all(lin[k] == g[k] for k in lin)
    checks.check("B1", ok, "T1: on the 4^3 torus, for three lapse pairs, alpha = 3/7 and K = 5/11, the part of {C[N], C[M]} linear in the strains, K(B[N,M] - B[M,N]), equals the relabelling generator G[xi] exactly, with xi_j(x -> x + e_j) = (K/(4 alpha))(N_(x + e_j) M_x - N_x M_(x + e_j)), at c = beta/(alpha + 3 beta) = 1/2 (beta = -alpha), with each face term timed by the mean of its four corners or of either pair of opposite corners")
    n, m = lapses[0]
    g = relabelling(sites, sh, closing_field(sites, sh, n, m, alpha, kk))
    fails = []
    for c, timing in ((F(1, 2), "one"), (F(0), "four"), (F(1, 3), "four"), (F(1, 4), "diagonal")):
        lin = linear_bracket(sites, sh, n, m, alpha, kk, c, timing)
        fails.append(any(lin[k] != g[k] for k in lin))
    s3, sh3 = torus(3)
    delta0 = {x: F(1) if x == (0, 0, 0) else ZERO for x in s3}
    delta1 = {x: F(1) if x == (1, 0, 0) else ZERO for x in s3}
    keys = sorted(linear_bracket(s3, sh3, delta0, delta1, alpha, kk, F(1, 2), "four"))
    b_half = linear_bracket(s3, sh3, delta0, delta1, alpha, kk, F(1, 2), "four")
    b_zero = linear_bracket(s3, sh3, delta0, delta1, alpha, kk, ZERO, "four")
    b_third = linear_bracket(s3, sh3, delta0, delta1, alpha, kk, F(1, 3), "four")
    affine = all(b_third[k] - b_half[k] == (1 - 2 * F(1, 3)) * (b_zero[k] - b_half[k]) for k in keys)
    obstruction = [b_zero[k] - b_half[k] for k in keys]
    columns = []
    for x in s3:
        for j in range(3):
            xi = {(z, l): (F(1) if (z, l) == (x, j) else ZERO) for z in s3 for l in range(3)}
            gcol = relabelling(s3, sh3, xi)
            columns.append([gcol[k] for k in keys])
    base = rank_of(columns)
    extended = rank_of(columns + [obstruction])
    checks.check("B2", all(fails) and affine and any(v != 0 for v in obstruction) and extended == base + 1,
                 f"T1: the closure needs both conditions - one-corner timing at beta = -alpha, and c = 0, 1/3, 1/4 with symmetric timing, all miss G[xi]; on the 3^3 torus with lapses at 0 and e1 the bracket is affine in c, b(c) = b(1/2) + (1 - 2c) b1, and b1 lies outside the span of all relabellings (rank {base} -> {extended}): for c != 1/2 no relabelling field closes the algebra")


# ============================================================================================ family C
T = sp.symbols("t", real=True)
AL, BE, KK, WB, PP = sp.symbols("alpha beta K wbar p", positive=True)


def mode_lagrangian(beta):
    """Block 101's quadratic action along p = p z, with the source e u and block 62's stress coupling (1/2) Theta_ij h_ij."""
    phi, aa, bb, cx, cy, xl, uu, ee = [sp.Function(nm)(T) for nm in ("phi", "a", "b", "cx", "cy", "xl", "u", "e")]
    th = {k: sp.Function("Theta_" + k)(T) for k in ("xx", "yy", "zz", "xy", "xz", "yz")}
    h = sp.Matrix([[phi + aa, bb, cx], [bb, phi - aa, cy], [cx, cy, 2 * xl]])
    p = sp.Matrix([0, 0, PP])
    trh = h.trace()
    r1 = PP ** 2 * trh - (p.T * h * p)[0, 0]
    hp = h * p
    r2 = -(PP ** 2 / 4) * (h * h).trace() + (hp.T * hp)[0, 0] / 2 - (p.T * h * p)[0, 0] * trh / 2 + PP ** 2 * trh ** 2 / 4
    hd = h.diff(T)
    kin = (AL * (hd * hd).trace() + beta * hd.trace() ** 2) / WB
    src = -ee * uu + sp.Rational(1, 2) * (th["xx"] * h[0, 0] + th["yy"] * h[1, 1] + th["zz"] * h[2, 2] + 2 * th["xy"] * h[0, 1] + 2 * th["xz"] * h[0, 2] + 2 * th["yz"] * h[1, 2])
    lag = kin + KK * WB * (uu * r1 + r2) + src
    return lag, dict(phi=phi, xl=xl, u=uu, e=ee, th=th, r1=sp.expand(r1), r2=sp.expand(r2))


def family_c(checks: Checks) -> None:
    """T2: at beta = -alpha the gradient relabelling is a symmetry up to a total derivative and the sources' identity."""
    zeta = sp.Function("zeta")(T)
    lag, f = mode_lagrangian(-AL)
    shifted = lag.subs({f["xl"]: f["xl"] + PP ** 2 * zeta / 2, f["u"]: f["u"] - 2 * AL / (KK * WB ** 2) * zeta.diff(T, 2)}).doit()
    delta = sp.expand(shifted - lag)
    boundary = -(4 * AL * PP ** 2 / WB) * zeta.diff(T) * f["phi"] + 2 * AL / (KK * WB ** 2) * (f["e"] * zeta.diff(T) - f["e"].diff(T) * zeta)
    source = (2 * AL / (KK * WB ** 2) * f["e"].diff(T, 2) + (0 if mut("noether_source_dropped") else PP ** 2 / 2 * f["th"]["zz"])) * zeta
    ok_sym = sp.simplify(delta - boundary.diff(T) - source) == 0
    lag_b, f_b = mode_lagrangian(BE)
    shifted_b = lag_b.subs({f_b["xl"]: f_b["xl"] + PP ** 2 * zeta / 2, f_b["u"]: f_b["u"] - 2 * AL / (KK * WB ** 2) * zeta.diff(T, 2)}).doit()
    rest = sp.expand(shifted_b - lag_b - boundary.subs(f["phi"], f_b["phi"]).diff(T) - source.subs(f["th"]["zz"], f_b["th"]["zz"]))
    extra = sp.factor(sp.expand(rest))
    ok_other = extra != 0 and sp.simplify(extra.subs(BE, -AL)) == 0
    r1_ok = sp.simplify(f["r1"] - 2 * PP ** 2 * f["phi"]) == 0
    checks.check("C1", ok_sym and ok_other and r1_ok,
                 "T2: along p = p z, with R1 = 2 p^2 phi and block 62's coupling, the gradient relabelling h -> h + p p^T zeta, u -> u - (2 alpha/(K wbar^2)) zeta'' changes the action at beta = -alpha by a total derivative plus zeta [(2 alpha/(K wbar^2)) e'' + (p^2/2) Theta_zz] exactly; for beta != -alpha an extra term proportional to alpha + beta remains: the ratio that closes the algebra is the ratio at which gradient relabellings are a symmetry, and then the sources must obey (2 alpha/(K wbar^2)) e'' + p.Theta.p/2 = 0")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: from the equations of motion at alpha + beta = 0, e'' = -(K wbar^2/(4 alpha)) p.Theta.p."""
    lag, f = mode_lagrangian(-AL)
    xl, phi, uu, ee, thz = f["xl"], f["phi"], f["u"], f["e"], f["th"]["zz"]
    el_xl = sp.expand(sp.diff(lag, xl.diff(T)).diff(T) - sp.diff(lag, xl))
    el_u = sp.expand(sp.diff(lag, uu))
    phi_sol = sp.solve(sp.Eq(el_u, 0), phi)[0]
    reduced = sp.expand(el_xl.subs(phi, phi_sol).doit())
    speed = KK * WB ** 2 / (4 * AL) if not mut("identity_speed_forged") else KK * WB ** 2 / (2 * AL)
    e2_sol = sp.solve(sp.Eq(reduced, 0), ee.diff(T, 2))
    ok1 = len(e2_sol) == 1 and sp.simplify(e2_sol[0] + speed * PP ** 2 * thz) == 0 and sp.simplify(phi_sol - ee / (2 * KK * WB * PP ** 2)) == 0
    cc, qq = sp.symbols("c q", positive=True)
    jj = sp.Function("J")(T)
    pm = sp.Function("P")(T)
    th = sp.Function("Theta")(T)
    e1 = sp.Function("e")(T)
    cont = sp.Eq(e1.diff(T), -sp.I * qq * jj)
    mom = sp.Eq(pm.diff(T), -sp.I * qq * th)
    e2 = cont.rhs.subs(jj, cc * pm).diff(T).subs(pm.diff(T), mom.rhs)
    ok2 = sp.simplify(e2 + cc * qq ** 2 * th) == 0
    checks.check("D1", ok1 and ok2,
                 "T3: at alpha + beta = 0 the u-equation is the constraint 2 K wbar p^2 phi = e and the longitudinal relabelling's equation then reads e'' = -(K wbar^2/(4 alpha)) p.Theta.p (p along z: p.Theta.p = p^2 Theta_zz); this is the second derivative of continuity e' + i p.J = 0 with momentum balance P' + i p.Theta = 0 exactly when J = (K wbar^2/(4 alpha)) P, not continuity itself (a constant e' stays free)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: a stationary two-wave state of the walk has e'' = 0 and p.Theta.p != 0 at its difference wave vector."""
    ii = sp.I
    sig = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -ii], [ii, 0]]), sp.Matrix([[1, 0], [0, -1]]))
    sa, ca, sb, cb = sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 13), sp.Rational(12, 13)
    s1 = (sa, sb, sp.Integer(0))                                   # sin k1, k1 = (a, b, 0)
    s2 = (-sb, sa, sp.Integer(0))                                  # sin k2, k2 = (-b, a, 0)
    eps = sp.sqrt(sa ** 2 + sb ** 2)
    chis = [sp.Matrix([s[0] - ii * s[1], eps]) for s in (s1, s2)]
    eig_ok = all(sp.simplify(sum((sig[j] * s[j] for j in range(3)), sp.zeros(2, 2)) * ch - eps * ch) == sp.zeros(2, 1) for s, ch in zip((s1, s2), chis))
    same_energy = sum(x ** 2 for x in s1) == sum(x ** 2 for x in s2)
    cos_q = (cb * ca - sb * sa, ca * cb + sa * sb, sp.Integer(1))    # q = k2 - k1 = (-(a + b), a - b, 0)
    p = (-sp.sqrt(2 - 2 * cos_q[0]), sp.sqrt(2 - 2 * cos_q[1]), sp.Integer(0))
    theta = sp.zeros(3, 3)
    for a_ in range(3):
        amp = (chis[0].H * sig[a_] * chis[1])[0, 0] / 2
        for j in range(3):
            theta[a_, j] = amp * (s1[j] + s2[j])
    sym = (theta + theta.T) / 2
    ptp = sp.simplify(sum((p[a_] * sym[a_, j] * p[j] for a_ in range(3) for j in range(3)), sp.Integer(0)))
    div = [sp.simplify(sum((p[a_] * sym[a_, j] for a_ in range(3)), sp.Integer(0))) for j in range(3)]
    want = 128 * sp.sqrt(2146) * (1 - ii) / 65 ** 4
    nonzero = (ptp != 0) if not mut("stress_taken_divergence_free") else (ptp == 0)
    checks.check("E1", eig_ok and same_energy and nonzero and sp.simplify(ptp - want) == 0 and all(d != 0 for d in div),
                 f"T4: the walk's positive-branch waves k1 = (a, b, 0), k2 = (-b, a, 0) with sin a = 3/5, sin b = 5/13 have the same energy (squared 2146/4225), so their superposition is stationary and e'' = 0 at q = k2 - k1; its frame response there (block 62: Theta_a^j = (1/2) chi1^dag sigma_a chi2 (sin k1 + sin k2)_j) has p.Theta.p = 128 sqrt(2146)(1 - i)/65^4 != 0 and p.Theta != 0 in every component: at beta = -alpha, T3 has no solution with the walk as content, and by block 62 T5 as landed the static equations have none at any ratio")


# ============================================================================================ family F
FENCES = (
    "This note works within block 60's curvature member, block 62's placement, kinetic family and frame response, and block 101's quadratic action, all as landed on main; it reports at which ratio the lapse constraints close on the lattice and whether the walker can then be the member's content; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Noether", "DeWitt", "Dirac", "Bergmann", "Teitelboim", "Hojman", "Kuchar", "Fierz", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the gradient relabelling's change of the mode action, and the equations of motion at alpha + beta = 0 (symbolic)",
    "per_site: executed - the linear bracket against the relabelling generator at every strain of a 4^3 torus for three lapse pairs and four face timings",
    "per_mode: executed - the walk's stationary two-wave state and its frame response at the difference wave vector (exact algebraic numbers)",
    "per_block: executed - the obstruction's rank against all relabellings on the 3^3 torus; the affine dependence on the kinetic ratio",
    "lattice_wide: T1 at linear order for block 62's staggered placement on every torus of side >= 3 and every lapse; T2-T3 for block 101's quadratic action at every lattice wave vector; T4 for block 62's frame response as the stress; the member, the kinetic family, the face timing and the coupling are supplied",
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
    print("scope: the curvature member's lapse constraints close onto the strains' relabelling on the lattice at linear order exactly when beta = -alpha with symmetric face timing; there the gradient relabelling is a symmetry and the sources must obey e'' = -(K wbar^2/(4 alpha)) p.Theta.p, which the walk's own stationary states violate; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
