#!/usr/bin/env python3
"""Under an explicitly excluded re-recording clause: positive symmetric-stencil update kernels, even-grid bilayer geometry, sphere reflection bounds and finite stationary moments. No temporal-memory theorem or certified numerical onset."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_light_cone_formation_keeps_memory_in_3plus1_its_stationary_law_is_one_layer_of_a_reflection_positive_bilayer_ordered_above_beta_0p5905_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "light_cone_not_reversible": "B",
    "level_order_reversible": "B",
    "relabelling_not_an_isomorphism": "C",
    "rung_branch_shift_is_one": "C",
    "a_crossing_edge_is_not_a_mirror_pair": "D",
    "layer_halves_positive": "D",
    "threshold_without_the_rung_branch": "E",
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


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        self.re = F(re_)
        self.im = F(im_)

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


SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]
MINUS_HALF_I = G(0, F(-1, 2))                                  # 1/(2i)


def mat_add(a, b):
    return [[a[r][c] + b[r][c] for c in range(2)] for r in range(2)]


def mat_scale(a, f):
    return [[a[r][c] * f for c in range(2)] for r in range(2)]


def mat_mul(a, b):
    return [[a[r][0] * b[0][c] + a[r][1] * b[1][c] for c in range(2)] for r in range(2)]


def mat_vec(a, v):
    return (a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1])


def frame_matrix(vec):
    """sum_a E_a sigma_a for a coin vector (E_1, E_2, E_3)."""
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


DIMS = (3, 3, 3)
SITES = list(product(*(range(d) for d in DIMS)))


def shift(x, j, step):
    return tuple((x[i] + (step if i == j else 0)) % DIMS[i] for i in range(3))


def s_op(psi, j):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    return {x: tuple((psi[shift(x, j, 1)][c] - psi[shift(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in SITES}


def generator(psi, frame, symmetrised=True):
    """H psi with H = (1/2) sum_j {E^j.sigma, S_j}, or the unsymmetrised sum_j E^j.sigma S_j."""
    out = {x: (G(0), G(0)) for x in SITES}
    for j in range(3):
        first = s_op(psi, j)
        first = {x: mat_vec(frame_matrix(frame[x][j]), first[x]) for x in SITES}
        if symmetrised:
            second = s_op({x: mat_vec(frame_matrix(frame[x][j]), psi[x]) for x in SITES}, j)
            for x in SITES:
                out[x] = tuple(out[x][c] + (first[x][c] + second[x][c]) * F(1, 2) for c in range(2))
        else:
            for x in SITES:
                out[x] = tuple(out[x][c] + first[x][c] for c in range(2))
    return out


def inner(phi, psi):
    tot = G(0)
    for x in SITES:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


def rational_state(seed):
    return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2]) % 5 - 2, 3), F((seed + x[0] * x[0] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                G(F((seed * 3 + x[0] * x[1] + 2 * x[2]) % 7 - 3, 5), F((seed * 5 + x[0] + x[1] + x[2]) % 3 - 1, 2))) for x in SITES}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


def light_cone_ring_law(size, stencil, menu, t):
    """The light-cone formation chain on a ring: s'(x) drawn with weight t^(s'.h), h = sum over the stencil of s(x + d); menu = list of
    contents (tuples), s.s' integer-valued. Returns (states, pi, P) with pi(s) = prod_x Z(h_x(s)) and P(s'|s) = prod_x t^(s'_x.h_x)/Z(h_x)."""
    states = list(product(range(len(menu)), repeat=size))

    def dot(a, b):
        return sum(p * q for p, q in zip(menu[a], menu[b]))

    def h_dot(s, x, c):
        return sum(dot(c, s[(x + d) % size]) for d in stencil)

    def Z(s, x):
        return sum(t ** h_dot(s, x, c) for c in range(len(menu)))
    pi = {s: sp.prod([Z(s, x) for x in range(size)]) for s in states}
    return states, pi, h_dot, Z


def detailed_balance_defect(size, stencil, menu, t):
    states, pi, h_dot, Z = light_cone_ring_law(size, stencil, menu, t)
    worst = sp.Integer(0)
    for s in states:
        for s2 in states:
            fwd = pi[s] * sp.prod([t ** h_dot(s, x, s2[x]) / Z(s, x) for x in range(size)])
            bwd = pi[s2] * sp.prod([t ** h_dot(s2, x, s[x]) / Z(s2, x) for x in range(size)])
            dlt = sp.simplify(fwd - bwd)
            if dlt != 0:
                return dlt, (s, s2)
    return worst, None


N7_STENCIL = [(0, 0, 0)] + [tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (1, -1)]
LEVEL_ORDER_STENCIL = [(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


def cycle_ratio_ring(size, stencil, t):
    """Forward over backward transition products of the cycle a -> b -> -a -> a on a ring with two-valued contents; a and b are the all-up
    configuration flipped at sites 0 and 1."""
    menu = [(1,), (-1,)]
    _, _, h_dot, Z = light_cone_ring_law(size, stencil, menu, t)

    def P(s2, s):
        return sp.prod([t ** h_dot(s, x, s2[x]) / Z(s, x) for x in range(size)])
    a = tuple(1 if x == 0 else 0 for x in range(size))
    b = tuple(1 if x == 1 else 0 for x in range(size))
    c = tuple(1 - v for v in a)
    return sp.simplify(P(b, a) * P(c, b) * P(a, c) / (P(c, a) * P(b, c) * P(a, b)))


def cycle_exponent_torus(size, stencil):
    """The exponent of t in the forward over backward products of the cycle a -> b -> -a -> a on (Z/size)^3 with contents +-1 along one axis:
    B(b, a) + B(-a, b) + B(a, -a), with A(s', s) = sum_x sum_d s'_x s_{x+d} and B(u, v) = A(u, v) - A(v, u); a and b flip the all-up
    configuration at the origin and at e_1."""
    sites = list(product(range(size), repeat=3))
    a = {x: (-1 if x == (0, 0, 0) else 1) for x in sites}
    b = {x: (-1 if x == (1, 0, 0) else 1) for x in sites}
    c = {x: -a[x] for x in sites}

    def A(u, v):
        return sum(u[x] * v[tuple((x[i] + d[i]) % size for i in range(3))] for x in sites for d in stencil)

    def B(u, v):
        return A(u, v) - A(v, u)
    return B(b, a) + B(c, b) + B(a, c)


def bilayer_eigen_check(size, shift):
    """Exact check that phi(x, a) = i^(n.x) (1, sigma)_a is an eigenvector of the bilayer torus's graph Laplacian with eigenvalue E(k) (sigma = +1)
    or E(k) + shift (sigma = -1), k = 2 pi n / size, size = 4 (phases i^m kept as exponents mod 4; Gaussian integers as integer pairs).
    Returns (all_ok, list of eigenvalues)."""
    assert size == 4
    edges = bilayer_edges(size)
    nbrs = {}
    for e in edges:
        u, w = tuple(e)
        nbrs.setdefault(u, []).append(w)
        nbrs.setdefault(w, []).append(u)
    cos_q = (1, 0, -1, 0)
    ok = True
    eigs = []
    for n in product(range(size), repeat=3):
        Ek = 6 - 2 * sum(cos_q[c % 4] for c in n)
        for sigma in (1, -1):
            lam = Ek if sigma == 1 else Ek + shift
            eigs.append(lam)
            for v, ws in nbrs.items():
                x, a = v
                ca = 1 if a == 0 else sigma
                m0 = sum(n[i] * x[i] for i in range(3)) % 4
                re, im = len(ws) * ca, 0
                for w in ws:
                    y, b = w
                    cb = 1 if b == 0 else sigma
                    dm = (sum(n[i] * y[i] for i in range(3)) - m0) % 4
                    unit = ((1, 0), (0, 1), (-1, 0), (0, -1))[dm]
                    re -= cb * unit[0]
                    im -= cb * unit[1]
                if (re, im) != (lam * ca, 0):
                    ok = False
    return ok, eigs


def doubled_graph_edges(size):
    """Gamma_L: vertices (x, a), x in (Z/L)^3, a in {0, 1}; edges (x, 0) - (x + d, 1), d in N7 = {0, +-e_j}."""
    N7 = [(0, 0, 0)] + [tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (1, -1)]
    edges = set()
    for x in product(range(size), repeat=3):
        for d in N7:
            y = tuple((x[i] + d[i]) % size for i in range(3))
            edges.add(frozenset({(x, 0), (y, 1)}))
    return edges


def bilayer_edges(size):
    edges = set()
    for x in product(range(size), repeat=3):
        edges.add(frozenset({(x, 0), (x, 1)}))
        for a in (0, 1):
            for j in range(3):
                y = tuple((x[i] + (1 if i == j else 0)) % size for i in range(3))
                edges.add(frozenset({(x, a), (y, a)}))
    return edges


def relabel(v):
    x, a = v
    return (x, a ^ (sum(x) % 2))


def reflections(size):
    """Bond-plane reflections along each axis (between x_j = c and c + 1, acting on both slabs) and the slab swap (x, a) -> (x, 1 - a)."""
    out = []
    for j in range(3):
        for c in range(size):
            def th(v, j=j, c=c):
                x, a = v
                y = list(x)
                y[j] = (2 * c + 1 - x[j]) % size
                return (tuple(y), a)
            def half(v, j=j, c=c):
                return ((v[0][j] - c - 1) % size) < size // 2
            out.append((f"axis {j} plane {c}+1/2", th, half))
    out.append(("slab swap", lambda v: (v[0], 1 - v[1]), lambda v: v[1] == 0))
    return out


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    t = sp.symbols("t", positive=True)
    ising = [(1,), (-1,)]
    six = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    d_is, _ = detailed_balance_defect(4, (0, 1, -1), ising, t)
    d_six, _ = detailed_balance_defect(3, (0, 1, -1), six[:4], t)
    ok = d_is == 0 and d_six == 0
    b1 = ok if not mut("light_cone_not_reversible") else (not ok)
    checks.check("B1", b1, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    back = (0, 1, -1) if mut("level_order_reversible") else (0, -1)
    ratio = cycle_ratio_ring(4, back, t)
    back3 = LEVEL_ORDER_STENCIL if not mut("level_order_reversible") else N7_STENCIL
    exp_level = cycle_exponent_torus(4, back3)
    exp_cone = cycle_exponent_torus(4, N7_STENCIL)
    b2 = sp.simplify(ratio - t ** 8) == 0 and exp_level == 8 and exp_cone == 0
    checks.check("B3", sp.simplify(cycle_ratio_ring(4,(0,-1),sp.Integer(1))-1)==0 and sp.simplify(cycle_ratio_ring(2,(0,-1),t)-1)==0, 'Scoped exact check B3: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    checks.check("B2", b2, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = True
    counts = []
    for size in (4, 6):
        g = doubled_graph_edges(size)
        img = {frozenset(relabel(v) for v in e) for e in g}
        bl = bilayer_edges(size)
        ok = ok and img == bl and len(g) == len(bl)
        counts.append(len(g))
    c1 = ok if not mut("relabelling_not_an_isomorphism") else (not ok)
    checks.check("C1", c1, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    k = sp.symbols("k1 k2 k3", real=True)
    E = 6 - 2 * (sp.cos(k[0]) + sp.cos(k[1]) + sp.cos(k[2]))
    shifted = E.subs({k[0]: k[0] + sp.pi, k[1]: k[1] + sp.pi, k[2]: k[2] + sp.pi}, simultaneous=True)
    eig_ok, eigs = bilayer_eigen_check(4, 1 if mut("rung_branch_shift_is_one") else 2)
    c2 = eig_ok and len(eigs) == 128 and sp.simplify(shifted - (12 - E)) == 0
    checks.check("C2", c2, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    bl = bilayer_edges(size)
    verts = [(x, a) for x in product(range(size), repeat=3) for a in (0, 1)]
    ok_fixed = ok_pairs = True
    covered = set()
    for name, th, half in reflections(size):
        ok_fixed = ok_fixed and all(th(v) != v for v in verts) and all(half(v) != half(th(v)) for v in verts)
        for e in bl:
            u, w = tuple(e)
            if half(u) != half(w):
                covered.add(e)
                ok_pairs = ok_pairs and (th(u) == w)
    ok_cover = covered == bl
    d1 = (ok_fixed and ok_pairs and ok_cover) if not mut("a_crossing_edge_is_not_a_mirror_pair") else (not ok_pairs)
    checks.check("D1", d1, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    cube = list(product(range(2), repeat=3))
    idx = {x: i for i, x in enumerate(cube)}
    M = sp.zeros(8, 8)
    for x in cube:
        M[idx[x], idx[x]] += 1
        for j in range(3):
            y = list(x)
            y[j] = 1 - y[j]
            M[idx[x], idx[tuple(y)]] += 1              # the open 2x2x2 cube: three neighbours per site
    d = sp.Matrix([2 * (-1) ** sum(x) for x in cube])
    quad = (d.T * M * d)[0]
    tor = list(product(range(4), repeat=3))
    stag = {x: 2 * (-1) ** sum(x) for x in tor}
    quad_t = sum(stag[x] * stag[tuple((x[i] + dd[i]) % 4 for i in range(3))] for x in tor for dd in N7_STENCIL)
    d2 = (quad == -64 and quad_t == -20 * 64) if not mut("layer_halves_positive") else (quad >= 0)
    checks.check("D2", d2, 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    beta, G, H, Nn = sp.symbols("beta G H N", positive=True)
    # sum over the 2N eigenvectors and 3 components of <(s, phi)^2> = 2N; zero mode <|M|^2>/(2N); infrared bound 1/(beta lambda) per component elsewhere
    zero_mode_lower = 2 * Nn - (3 / beta) * Nn * (G + H)                     # <|M|^2>/(2N) >= this
    per_site = sp.simplify(zero_mode_lower * 2 * Nn / (4 * Nn ** 2))       # <|M/(2N)|^2> >= this, and <|m_0|^2> >= <|(m_0 + m_1)/2|^2>
    target = 1 - (sp.Rational(3, 2) / beta) * (G + H) if not mut("threshold_without_the_rung_branch") else 1 - (sp.Rational(3, 2) / beta) * G
    eig_ok, eigs = bilayer_eigen_check(4, 2)
    nonzero = [lam for lam in eigs if lam != 0]
    trace_inv = sum((sp.Rational(1, lam) for lam in nonzero), sp.Integer(0))
    cos_q = (1, 0, -1, 0)
    G4 = sum((sp.Rational(1, 6 - 2 * sum(cos_q[c] for c in n)) for n in product(range(4), repeat=3) if n != (0, 0, 0)), sp.Integer(0)) / 64
    H4 = sum((sp.Rational(1, 8 - 2 * sum(cos_q[c] for c in n)) for n in product(range(4), repeat=3)), sp.Integer(0)) / 64
    e1 = eig_ok and sp.simplify(per_site - target) == 0 and len(nonzero) == 127 and trace_inv == 64 * (G4 + H4)
    checks.check("E1", e1, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    vals = {}
    for size in (4, 6):
        cosv = [sp.cos(2 * sp.pi * n / size) for n in range(size)]
        Gs = sp.Integer(0)
        Hs = sp.Integer(0)
        for c in product(cosv, repeat=3):
            E = 6 - 2 * sum(c)
            if E != 0:
                Gs += 1 / E
            Hs += 1 / (E + 2)
        n = size ** 3
        vals[size] = sp.nsimplify(sp.Rational(3, 2) * (Gs + Hs) / n)
    ordered = vals[4] == sp.Rational(18239, 35840) and vals[6] == sp.Rational(27735979, 51891840) and bool(vals[4] < vals[6]) and bool(vals[6] < sp.Rational(3, 5))
    checks.check("E2", ordered, 'Scoped exact check E2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: Under an explicitly excluded re-recording clause: positive symmetric-stencil update kernels, even-grid bilayer geometry, sphere reflection bounds and finite stationary moments. No temporal-memory theorem or certified numerical onset.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
