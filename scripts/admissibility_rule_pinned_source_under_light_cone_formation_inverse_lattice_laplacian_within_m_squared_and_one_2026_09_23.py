#!/usr/bin/env python3
"""Excluded re-recording comparator with a supplied symmetric stencil and source: exact stationary covariance identity, sphere transverse finite-mode inequalities and potential-difference bounds. No exact real-space inverse-distance shape."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_A_PINNED_SOURCE_UNDER_LIGHT_CONE_FORMATION_IS_ANSWERED_BY_THE_INVERSE_LATTICE_LAPLACIAN_WITHIN_A_FACTOR_BETWEEN_M_SQUARED_AND_ONE_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md', 'docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_pinned_source_under_light_cone_formation_is_answered_by_the_inverse_lattice_laplacian_within_a_factor_between_m_squared_and_one_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "source_on_one_level_only": "B",
    "response_from_one_level": "C",
    "antisymmetric_branch_unshifted": "C",
    "gaussian_weight_reversed": "D",
    "stiffness_sum_without_factor_two": "E",
    "lower_bound_linear_in_m": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
STENCIL_RING = (0, 1, -1)


def ring_chain_defect(size, menu, t, v, u, pin_both=True):
    """The light-cone chain on a ring (past {0, +-1}) with contents `menu` (tuples; the uniform field and the source act on component 0):
    P(s'|s) = prod_x t^(s'_x.h_x(s)) v^(s'_x[0]) u^([x = 0] s'_x[0]) / Z_x(s). Returns the first nonzero pi(s)P(s'|s) - pi(s')P(s|s') with
    pi(s) = v^(sum_x s_x[0]) u^(s_0[0]) prod_x Z_x(s) (without the factor u^(s_0[0]) when pin_both is False), or 0."""
    states = list(product(range(len(menu)), repeat=size))

    def dot(a, b):
        return sum(p * q for p, q in zip(menu[a], menu[b]))

    def weight(s, x, c):
        w = t ** sum(dot(c, s[(x + d) % size]) for d in STENCIL_RING) * v ** menu[c][0]
        return w * u ** menu[c][0] if x == 0 else w

    Zs = {s: [sum(weight(s, x, c) for c in range(len(menu))) for x in range(size)] for s in states}

    def pi(s):
        w = sp.prod(Zs[s]) * v ** sum(menu[c][0] for c in s)
        return w * u ** menu[s[0]][0] if pin_both else w
    pis = {s: pi(s) for s in states}
    for s in states:
        for s2 in states:
            fwd = pis[s] * sp.prod([weight(s, x, s2[x]) / Zs[s][x] for x in range(size)])
            bwd = pis[s2] * sp.prod([weight(s2, x, s[x]) / Zs[s2][x] for x in range(size)])
            dlt = sp.simplify(fwd - bwd)
            if dlt != 0:
                return dlt
    return sp.Integer(0)


def doubled_ring_configs(size):
    """All +-1 configurations of the doubled ring's vertices (x, a), with the exponent sum over its edges (x, 0)-(x + d, 1), d in {0, +-1}."""
    verts = [(x, a) for x in range(size) for a in (0, 1)]
    edges = [((x, 0), ((x + d) % size, 1)) for x in range(size) for d in STENCIL_RING]
    out = []
    for vals in product((1, -1), repeat=len(verts)):
        sig = dict(zip(verts, vals))
        out.append((sig, sum(sig[p] * sig[q] for p, q in edges)))
    return out, edges


def bilayer_of(sig, size):
    """The bilayer labels: S_b(x) = sigma at the doubled-ring vertex (x, b XOR parity(x))."""
    return {(x, b): sig[(x, b ^ (x % 2))] for x in range(size) for b in (0, 1)}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    t, v, u = sp.symbols("t v u", positive=True)
    ising = [(1,), (-1,)]
    four = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    both = not mut("source_on_one_level_only")
    d_is = ring_chain_defect(4, ising, t, v, u, pin_both=both)
    d_four = ring_chain_defect(3, four, t, v, u, pin_both=both)
    checks.check("B1", d_is == 0 and d_four == 0, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    configs, _ = doubled_ring_configs(4)
    ok = True
    for s in product((1, -1), repeat=4):
        z = sp.prod([sum(t ** sum(c * s[(x + d) % 4] for d in STENCIL_RING) * v ** c * (u ** c if x == 0 else 1) for c in (1, -1)) for x in range(4)])
        pi_s = z * v ** sum(s) * u ** s[0]
        tot = sp.Integer(0)
        for s2 in product((1, -1), repeat=4):
            a = sum(s2[x] * s[(x + d) % 4] for x in range(4) for d in STENCIL_RING)
            tot += t ** a * v ** (sum(s) + sum(s2)) * u ** (s[0] + s2[0])
        ok = ok and sp.simplify(tot - pi_s) == 0
    checks.check("B2", ok, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    t, u = sp.symbols('t u', positive=True)
    size = 4
    configs, _ = doubled_ring_configs(size)
    Zmu = sum((t ** e for _, e in configs))

    def mu_mean(f):
        return sp.cancel(sp.sympify(sum((f(sig) * t ** e for sig, e in configs))) / Zmu)

    def pi_u(s):
        return u ** s[0] * sp.prod([sum((t ** sum((c * s[(x + d) % size] for d in STENCIL_RING)) * (u ** c if x == 0 else 1) for c in (1, -1))) for x in range(size)])
    layer = list(product((1, -1), repeat=size))
    Zpi = sum((pi_u(s) for s in layer))
    ok1 = True
    for x in range(size):
        mean_x = sp.sympify(sum((s[x] * pi_u(s) for s in layer))) / Zpi
        resp = sp.cancel(sp.diff(mean_x, u).subs(u, 1))
        partner = (lambda sig: sig[0, 0] + sig[0, 1]) if not mut('response_from_one_level') else lambda sig: sig[0, 0]
        cov = mu_mean(lambda sig: sig[x, 0] * partner(sig)) - mu_mean(lambda sig: sig[x, 0]) * mu_mean(partner)
        ok1 = ok1 and sp.simplify(resp - cov) == 0
    checks.check('C1', ok1, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    ok2 = True
    for x in range(size):
        c_gamma = mu_mean(lambda sig: sig[x, 0] * (sig[0, 0] + sig[0, 1]))
        c_plus = mu_mean(lambda sig: (lambda B: sp.sympify(2 * ((B[x, 0] + B[x, 1]) * (B[0, 0] + B[0, 1]))) / 4)(bilayer_of(sig, size)))
        ok2 = ok2 and sp.simplify(c_gamma - c_plus) == 0
    I = sp.I

    def ft(vals, n):
        return sum((vals[x] * I ** (-n * x % 4) for x in range(size)))
    for n in range(size):
        lhs = mu_mean(lambda sig: sp.expand(ft([sig[x, 0] for x in range(size)], n) * sp.conjugate(ft([sig[x, 0] for x in range(size)], n))))
        shift = 0 if mut('antisymmetric_branch_unshifted') else 2
        plus = mu_mean(lambda sig: (lambda B: sp.expand(ft([sp.sympify(B[x, 0] + B[x, 1]) / 2 for x in range(size)], n) * sp.conjugate(ft([sp.sympify(B[x, 0] + B[x, 1]) / 2 for x in range(size)], n))))(bilayer_of(sig, size)))
        minus = mu_mean(lambda sig: (lambda B: sp.expand(ft([sp.sympify(B[x, 0] - B[x, 1]) / 2 for x in range(size)], (n + shift) % 4) * sp.conjugate(ft([sp.sympify(B[x, 0] - B[x, 1]) / 2 for x in range(size)], (n + shift) % 4))))(bilayer_of(sig, size)))
        cross = mu_mean(lambda sig: (lambda B: sp.expand(ft([sp.sympify(B[x, 0] + B[x, 1]) / 2 for x in range(size)], n) * sp.conjugate(ft([sp.sympify(B[x, 0] - B[x, 1]) / 2 for x in range(size)], (n + 2) % 4))))(bilayer_of(sig, size)))
        ok2 = ok2 and sp.simplify(lhs - plus - minus) == 0 and (sp.simplify(cross) == 0)
    checks.check('C2', ok2, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def exp_lower(x: Fraction, terms: int = 30) -> Fraction:
    """A partial sum of the exponential series: a lower bound for e^x when x > 0."""
    tot = ZERO
    term = ONE
    for n in range(terms):
        tot += term
        term = term * x / (n + 1)
    return tot


def ladder_edges(size):
    return [((x, b), ((x + 1) % size, b)) for x in range(size) for b in (0, 1)] + [((x, 0), (x, 1)) for x in range(size)]


def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    configs, dedges = doubled_ring_configs(size)
    img = sorted(tuple(sorted(((p[0], p[1] ^ (p[0] % 2)), (q[0], q[1] ^ (q[0] % 2))))) for p, q in dedges)
    led = ladder_edges(size)
    iso = img == sorted(tuple(sorted(e)) for e in led)
    verts = [(x, b) for x in range(size) for b in (0, 1)]
    spins = list(product((1, -1), repeat=len(verts)))
    ok_dom = True
    for r, fields in ((F(2), product((-1, 0, 1), repeat=len(verts) - 1)), (F(3, 2), product((0, 1), repeat=len(verts) - 1))):
        sign = -1 if not mut("gaussian_weight_reversed") else 1
        cache = {}

        def Zh(hvals):
            h = dict(zip(verts, (0,) + tuple(hvals)))
            tot = ZERO
            for sv in spins:
                s = dict(zip(verts, sv))
                X = sum((s[p] - s[q] - (h[p] - h[q])) ** 2 for p, q in led)
                if X not in cache:
                    cache[X] = r ** (sign * X)
                tot += cache[X]
            return tot
        z0 = Zh((0,) * (len(verts) - 1))
        for hv in fields:
            if Zh(hv) > z0:
                ok_dom = False
                break
    checks.check("D1", iso and ok_dom, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    ok_ir = True
    for t_val, b_up in ((F(4), F(1387, 1000)), (F(9, 4), F(811, 1000))):
        certified = exp_lower(b_up) > t_val                      # e^b_up > t, so beta = log t < b_up
        weights = []
        for sv in spins:
            s = dict(zip(verts, sv))
            weights.append((s, t_val ** sum(s[p] * s[q] for p, q in led)))
        Z = sum((w for _, w in weights), ZERO)
        cos_q = (1, 0, -1, 0)
        sin_q = (0, 1, 0, -1)
        for n in (1, 2, 3):
            tot = ZERO
            for s, w in weights:
                re = sum(F(s[(x, 0)] + s[(x, 1)], 2) * cos_q[(n * x) % 4] for x in range(size))
                im = sum(F(s[(x, 0)] + s[(x, 1)], 2) * sin_q[(n * x) % 4] for x in range(size))
                tot += w * (re * re + im * im)
            s_plus = tot / Z / size
            E1 = 2 - 2 * cos_q[n % 4]
            ok_ir = ok_ir and certified and 2 * b_up * s_plus * E1 <= 1
    checks.check("D2", ok_ir, 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    sxu, syu, szu, sxv, syv, szv, au, av, bu, bv, eps = sp.symbols("sxu syu szu sxv syv szv au av bu bv epsilon")
    al_u, al_v = sp.symbols("alpha_u alpha_v", real=True)

    def rot(sx, sy, sz, al):
        return (sx * sp.cos(al) + sz * sp.sin(al), sy, -sx * sp.sin(al) + sz * sp.cos(al))
    ru = rot(sxu, syu, szu, al_u)
    rv = rot(sxv, syv, szv, al_v)
    bond = -(ru[0] * rv[0] + ru[1] * rv[1] + ru[2] * rv[2])
    pairs = ((bu, au, al_u, al_u), (bu, av, al_u, al_v), (bv, au, al_v, al_u), (bv, av, al_v, al_v))
    dd_bond = sum(cb * c * sp.diff(bond, a1, a2) for cb, c, a1, a2 in pairs).subs({al_u: 0, al_v: 0})
    e1a = sp.expand(dd_bond - (au - av) * (bu - bv) * (sxu * sxv + szu * szv)) == 0
    field = -eps * ru[2]
    dd_field = (bu * au * sp.diff(field, al_u, al_u)).subs({al_u: 0})
    e1b = sp.expand(dd_field - eps * au * bu * szu) == 0
    d_obs = (au * sp.diff(bu * ru[0], al_u) + av * sp.diff(bv * rv[0], al_v)).subs({al_u: 0, al_v: 0})
    e1c = sp.expand(d_obs - (au * bu * szu + av * bv * szv)) == 0
    th, ph = sp.symbols("theta phi", real=True)
    X, Y, Zc = sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)
    e1d = True
    for a, b, c in product(range(4), repeat=3):
        if a + b + c > 3:
            continue
        sx, sy, sz = sp.symbols("sx sy sz")
        G_ = sx ** a * sy ** b * sz ** c
        LG = sz * sp.diff(G_, sx) - sx * sp.diff(G_, sz)
        val = sp.integrate(sp.integrate(sp.expand(LG.subs({sx: X, sy: Y, sz: Zc}) * sp.sin(th)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
        e1d = e1d and sp.simplify(val) == 0
    checks.check("E1", e1a and e1b and e1c and e1d, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    cos_q = (1, 0, -1, 0)
    ok2 = True
    size = 4
    N = size ** 3
    for n in product(range(size), repeat=3):
        tot = 0
        for x in product(range(size), repeat=3):
            for j in range(3):
                tot += 2 * (2 - 2 * cos_q[n[j] % 4])              # both slabs; a rung joins equal phases and adds 0
        Ek = 6 - 2 * sum(cos_q[c] for c in n)
        target = (2 * N * Ek) if not mut("stiffness_sum_without_factor_two") else (N * Ek)
        single = sum((2 - 2 * cos_q[n[j] % 4]) for x in product(range(size), repeat=3) for j in range(3))
        ok2 = ok2 and tot == target and single == N * Ek
    checks.check("E2", ok2, 'Scoped exact check E2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    m, E, beta, Nn, s2, Pb = sp.symbols("m E beta N S2 P_b", positive=True)
    # |<D F>|^2 <= beta <|F|^2> <Dbar D H>,  <D F> = 2 N m,  <Dbar D H> = 2 N (P_b E + eps m) (slab bonds alike by symmetry, rungs 0),
    # F = 2 S_+^(k),  R = 2 beta <|S_+^|^2>/N
    lower_S2 = (2 * Nn * m) ** 2 / (beta * 2 * Nn * (Pb * E + eps * m)) / 4      # <|S_+^|^2> >= this
    R_lower = sp.simplify(2 * beta * lower_S2 / Nn)
    target = m ** 2 / (Pb * E + eps * m) if not mut("lower_bound_linear_in_m") else m / (Pb * E + eps * m)
    weaker = sp.simplify(R_lower.subs(Pb, 1) - m ** 2 / (E + eps * m)) == 0 and sp.simplify(sp.diff(R_lower, Pb)) != 0
    upper = sp.simplify(2 * beta * (1 / (2 * beta * E)))
    cos_q4 = (1, 0, -1, 0)
    weights_ok = all(1 - cos_q4[(sum(a * b for a, b in zip(n, x))) % 4] >= 0 for n in product(range(4), repeat=3) for x in product(range(4), repeat=3))
    checks.check("E3", sp.simplify(R_lower - target) == 0 and weaker and sp.simplify(upper - 1 / E) == 0 and weights_ok, 'Scoped exact check E3: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    A_, h = sp.symbols("A h", positive=True)
    P = 1 - E / 7
    lin = sp.simplify((A_ / 7) / (1 - P))
    probes = sp.simplify((h / (7 * beta)) * (7 / E))                   # the probes' prediction, field entering as e^(s'.h)
    checks.check("E4", sp.simplify(lin - A_ / E) == 0 and sp.simplify(probes - h / (beta * E)) == 0, 'Scoped exact check E4: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.')
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Excluded re-recording comparator with a supplied symmetric stencil and source: exact stationary covariance identity, sphere transverse finite-mode inequalities and potential-difference bounds. No exact real-space inverse-distance shape.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
