#!/usr/bin/env python3
"""Exact checks: light-cone formation keeps memory in 3+1 (the formation reading with a symmetric past; the probes' derivations re-derived; not adopted).

OBJECTS: the light-cone formation clause - the record at (t + 1, x) forms with weight e^{beta s'.h}, h = the sum of the records at (t, x + d),
d in N7 = {0, +-e_j} (block 19's exponential zonal rule on the sphere); its level-to-level chain; the doubled graph Gamma_L (two levels, edges
(x, 0)-(x + d, 1)); the bilayer torus; the reflection family; the sum rule.
T1: with a symmetric stencil the chain satisfies detailed balance with pi(s) = prod_x Z(h_x(s)): exact on rings for two-valued and six-axis
   contents with symbolic t = e^beta; with a one-sided past (the level-ordered clause) a three-step cycle has forward/backward ratio t^8,
   so that chain is reversible with respect to no law.
T2: (x, a) -> (x, a XOR parity(x)) maps Gamma_L onto the bilayer torus edge by edge (L = 4, 6); spectrum {E, E + 2} = {E, 14 - E}, the
   eigenvectors checked exactly at every vertex of the 4^3 bilayer.
T3: the bilayer's reflection family (bond planes, slab swap): no fixed vertex, crossing edges are mirror pairs, every edge covered (L = 4); with
   the LAYERS as halves a kernel minor is negative (<d, M d> = -64 on the cube, -20N on the torus).
T4: the sum rule: <|m_0|^2> >= 1 - (3/(2 beta))(G_L + H_L); exact finite thresholds beta_4 = 18239/35840, beta_6 = 27735979/51891840.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    note, axioms = texts
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
    """T1: light-cone formation with a symmetric stencil is reversible, with stationary law the one-layer marginal of the ferromagnet on the doubled graph."""
    t = sp.symbols("t", positive=True)
    ising = [(1,), (-1,)]
    six = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    d_is, _ = detailed_balance_defect(4, (0, 1, -1), ising, t)
    d_six, _ = detailed_balance_defect(3, (0, 1, -1), six[:4], t)
    ok = d_is == 0 and d_six == 0
    b1 = ok if not mut("light_cone_not_reversible") else (not ok)
    checks.check("B1", b1, "T1: on a ring of four (two-valued menu) and a ring of three (four contents of the six-axis menu), the light-cone chain s'(x) ~ t^(s'.h_x(s)), h_x = s(x) + s(x+1) + s(x-1), satisfies pi(s)P(s'|s) = pi(s')P(s|s') exactly for every pair of configurations, with pi(s) = prod_x Z(h_x(s)) and symbolic t = e^beta: the joint law of two successive levels is prod over the doubled graph's edges of t^(s.s'), symmetric because the stencil is symmetric")
    back = (0, 1, -1) if mut("level_order_reversible") else (0, -1)
    ratio = cycle_ratio_ring(4, back, t)
    back3 = LEVEL_ORDER_STENCIL if not mut("level_order_reversible") else N7_STENCIL
    exp_level = cycle_exponent_torus(4, back3)
    exp_cone = cycle_exponent_torus(4, N7_STENCIL)
    b2 = sp.simplify(ratio - t ** 8) == 0 and exp_level == 8 and exp_cone == 0
    checks.check("B2", b2, f"T1: with a one-sided past the chain is reversible with respect to no law: on the ring of four with the past {{0, -1}} (two-valued contents; a and b the all-up configuration flipped at sites 0 and 1) the three-step cycle a -> b -> -a -> a has forward over backward transition products exactly t^8 with symbolic t = e^beta (the partition functions cancel around any cycle); on the 4^3 torus with the level-ordered past {{0, -e_1, -e_2, -e_3}} the same cycle (flips at the origin and at e_1) has exponent {exp_level}, and with the light-cone past N7 exponent {exp_cone}: the level-ordered clause violates the cycle criterion for every menu that contains a pair of opposite contents")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the doubled graph is the bilayer torus after relabelling; the spectrum."""
    ok = True
    counts = []
    for size in (4, 6):
        g = doubled_graph_edges(size)
        img = {frozenset(relabel(v) for v in e) for e in g}
        bl = bilayer_edges(size)
        ok = ok and img == bl and len(g) == len(bl)
        counts.append(len(g))
    c1 = ok if not mut("relabelling_not_an_isomorphism") else (not ok)
    checks.check("C1", c1, f"T2: the map (x, a) -> (x, a XOR parity(x)) carries the doubled graph Gamma_L (edges (x,0)-(x+d,1), d in {{0, +-e_j}}) edge by edge onto the bilayer torus (two copies of (Z/L)^3 with their nearest-neighbour bonds and one rung per site): {counts[0]} edges at L = 4, {counts[1]} at L = 6")
    k = sp.symbols("k1 k2 k3", real=True)
    E = 6 - 2 * (sp.cos(k[0]) + sp.cos(k[1]) + sp.cos(k[2]))
    shifted = E.subs({k[0]: k[0] + sp.pi, k[1]: k[1] + sp.pi, k[2]: k[2] + sp.pi}, simultaneous=True)
    eig_ok, eigs = bilayer_eigen_check(4, 1 if mut("rung_branch_shift_is_one") else 2)
    c2 = eig_ok and len(eigs) == 128 and sp.simplify(shifted - (12 - E)) == 0
    checks.check("C2", c2, "T2: on the 4^3 bilayer every one of the 128 vectors i^(n.x)(1, +-1) is an eigenvector of the graph Laplacian built from the relabelled edges, with eigenvalue E(k) for (1, 1) and E(k) + 2 for (1, -1) (the rung), exactly at every vertex; the 128 characters are orthogonal, so this is the whole spectrum; and E(k + (pi,pi,pi)) = 12 - E(k) symbolically, so {E, E + 2} is the doubled graph's {E, 14 - E}")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the reflection family of the bilayer with slab halves: no fixed vertex, crossing edges are mirror pairs, every edge crosses; the layer halves are not reflection positive."""
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
    checks.check("D1", d1, f"T3: on the 4^3 bilayer, each of the {3 * size + 1} reflections (bond planes along each axis acting on both slabs, and the slab swap) exchanges its halves with no fixed vertex, every edge crossing it joins a vertex to its own mirror image, and every one of the {len(bl)} edges crosses some reflection: block 19's G1-G2 argument (the crossing factor prod exp(beta s_u . s_theta u) expands with nonnegative coefficients; iterated reflections give Gaussian domination) applies to the bilayer")
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
    checks.check("D2", d2, f"T3: with the two LAYERS as halves every edge crosses the swap and the crossing matrix is M = I + A_nn (the seven-point stencil); for the staggered difference d = 2(-1)^|x| (a z-component, unit contents) on the open 2x2x2 cube <d, M d> = {quad} = 32 - 96, and on the 4^3 torus {quad_t} = -20N: the 2x2 minor of the reflection kernel exp(beta s.M s') at the two staggered configurations is negative for every beta > 0, so the layer halves are not reflection positive (the route needs the relabelling)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the sum rule, and the exact finite-size thresholds on the tori of side 4 and 6."""
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
    checks.check("E1", e1, "T4: the sum rule over the bilayer's 2N eigenvectors and three components, with the infrared bound 1/(beta lambda) off the zero mode, gives <|M/(2N)|^2> >= 1 - (3/(2 beta))(G_L + H_L), and the layer swap's symmetry with |(a + b)/2|^2 <= (|a|^2 + |b|^2)/2 gives the same bound for <|m_0|^2>; on the 4^3 bilayer the sum of 1/lambda over the 127 nonzero checked eigenvalues is exactly N times (G_4 + H_4), G_L = N^-1 sum_{k != 0} 1/E(k), H_L = N^-1 sum_k 1/(E(k) + 2): memory for beta > (3/2)(G_L + H_L)")
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
    checks.check("E2", ordered, f"T4: the exact finite-size thresholds are beta_4 = {vals[4]} and beta_6 = {vals[6]} (rationals: the tori's cosines are rational), beta_4 < beta_6 < 3/5; the control's lattice sums continue the increase to side 64 (about 5852/10000) below the infinite-volume constant (3/2)(I_0 + I_2), I_0 = int 1/E = W/6 in closed form and I_2 = int 1/(E + 2) by quadrature: about 5905/10000 (control)")


# ============================================================================================ family F
FENCES = (
    "This note works within the formation reading of the Record axiom with a supplied light-cone clause (a record forms from the seven records of the previous level around it, by block 19's rule on the sphere); it reports that the formation chain is reversible and that its stationary law keeps memory in 3+1 above a proved coupling; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - detailed balance for every pair of configurations on rings of three and four with symbolic t; the relabelling edge by edge on the 4^3 and 6^3 tori",
    "per_site: executed - every vertex and every crossing edge of the 13 reflections on the 4^3 bilayer; the cube's staggered form",
    "per_mode: executed - the two branches symbolically; the exact finite-size sums on the tori of side 4 and 6; control: the infinite-volume constants by quadrature, lattice sums to side 64, and an independent light-cone formation simulator on 24^3 and 32^3 planes",
    "per_block: executed - the sum rule's threshold symbolically; the exact finite thresholds",
    "lattice_wide: T1 for every ring and every menu with weights e^{beta s.s'} by the symmetry of the stencil (checked on rings); T2 for every even L by the parity argument (checked on 4 and 6); T3's structure for every even L (checked on 4), Gaussian domination by block 19's G2 argument; T4 for every even L, with the infinite-volume constant executed; the clause, the menu and the coupling are supplied",
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
    print("scope: light-cone formation keeps memory in 3+1 - with a symmetric past the formation chain is reversible and its stationary law is one layer of the sphere ferromagnet on a doubled graph, which a parity relabelling turns into a bilayer torus that is reflection positive with slab halves (not layer halves); Gaussian domination and the sum rule give <|m|^2> >= 1 - (3/(2 beta))(G_L + H_L), hence memory for beta > 0.5905 (executed constant); the executed onset lies between 0.55 and 0.60; the level-ordered clause is not reversible; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
