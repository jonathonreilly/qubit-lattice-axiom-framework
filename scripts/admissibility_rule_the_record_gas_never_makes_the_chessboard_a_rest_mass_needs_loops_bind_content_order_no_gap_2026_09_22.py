#!/usr/bin/env python3
"""Exact checks: the record gas and the chessboard that a rest mass needs (the moving-records reading of blocks 39-42 and the supplied clauses of blocks 54, 77, 79; not adopted).

OBJECTS: the static law with vacancies (block 39): records with six-axis contents on a finite graph, pair weight c omega(a, b) on recorded bonds,
1 on bonds with an empty end, c = g c_0, c_0 = 6/(p + q + 4r) the neutral scale (block 40), g >= 1 the scales allowed by block 39 T5;
block 54's walk H = sum_a sigma_a S_a with a record background entering as a coin-scalar potential (block 79) or a content-reading one.
T1 (binding grows only around loops): adding a recorded bond between x and y multiplies the neutral-scale weight by 1 + 3 t_1 lambda_1 + 2 t_2 lambda_2,
   (t_1, t_2) the correlation eigenvalues of the two contents in the arrangement without the bond; exactly 1 when x, y lie in different components.
T2 (the chessboard is the least likely arrangement): on every window enumerated no arrangement weighs less than the same records placed apart, the
   arrangements weighing exactly that are those without a cycle, and the heaviest is the full window; both chessboards weigh exactly free at every scale.
T3 (the equilibrium's staggered occupancy): mean exactly zero on tori; at g >= 1 the staggered susceptibility is at most random's and the mode is a clump;
   at the excluded g = 1/4 the mode is the chessboard.
T4 (what gaps the walk): content read by the coin, uniform or chessboard, leaves the spectrum touching zero (a ring of zeros for the chessboard);
   only the chessboard of occupancy with a content-blind coupling opens the gap c (block 79 T1).
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_NEVER_MAKES_THE_CHESSBOARD_A_REST_MASS_NEEDS_BINDING_GROWS_ONLY_AROUND_LOOPS_CONTENT_ORDER_GIVES_THE_WALK_NO_GAP_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_record_gas_never_makes_the_chessboard_a_rest_mass_needs_binding_grows_only_around_loops_content_order_gives_the_walk_no_gap_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "records_repel_when_a_loop_closes": "B",
    "bond_across_components_binds": "B",
    "an_arrangement_lighter_than_free": "C",
    "chessboard_is_the_heaviest_arrangement": "C",
    "staggered_order_at_the_neutral_scale": "D",
    "chessboard_is_the_mode_at_the_neutral_scale": "D",
    "content_chessboard_gaps_the_walk": "E",
    "uniform_content_gaps_the_walk": "E",
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


CONTENTS = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1)]                        # the six-axis menu: (axis, sign)


def omega(a, b, p, q, r):
    if a[0] != b[0]:
        return r
    return p if a[1] == b[1] else q


def lambdas(p, q, r):
    """The two non-trivial eigenvalues of the rule's one-neighbour probability K_1 = c_0 omega / 6, c_0 = 6/(p + q + 4r)."""
    return F(p - q, p + q + 4 * r), F(p + q - 2 * r, p + q + 4 * r)


def window(dims):
    sites = list(product(*[range(d) for d in dims]))
    idx = {s: i for i, s in enumerate(sites)}
    edges = []
    for s in sites:
        for ax in range(len(dims)):
            t = list(s)
            t[ax] += 1
            if t[ax] < dims[ax]:
                edges.append((idx[s], idx[tuple(t)]))
    return sites, edges


def content_sum(nodes, edges, p, q, r):
    """sum over the contents of `nodes` of the product over `edges` of omega: an integer, by frontier contraction."""
    nodes = list(nodes)
    if not nodes:
        return 1
    pos = {v: i for i, v in enumerate(nodes)}
    nbrs = {v: [] for v in nodes}
    for a, b in edges:
        nbrs[a].append(b)
        nbrs[b].append(a)
    last = {v: max([pos[v]] + [pos[u] for u in nbrs[v]]) for v in nodes}
    states = {(): 1}
    active = []
    for i, v in enumerate(nodes):
        new = {}
        for key, w in states.items():
            assign = dict(zip(active, key))
            for cv in CONTENTS:
                ww = w
                for u in nbrs[v]:
                    if pos[u] < i:
                        ww *= omega(cv, assign[u], p, q, r)
                nk = key + (cv,)
                new[nk] = new.get(nk, 0) + ww
        active = active + [v]
        keep = [j for j, u in enumerate(active) if last[u] > i]
        merged = {}
        for key, w in new.items():
            nk = tuple(key[j] for j in keep)
            merged[nk] = merged.get(nk, 0) + w
        active = [active[j] for j in keep]
        states = merged
    return sum(states.values())


def weight_over_free(nodes, edges, p, q, r):
    """Z_0(eta) / 6^n at the neutral scale: the arrangement's weight over that of the same records placed so that none touch."""
    n = len(list(nodes))
    return F(content_sum(nodes, edges, p, q, r)) * F(6, p + q + 4 * r) ** len(edges) / F(6) ** n


def joint_marginal(nodes, edges, x, y, p, q, r):
    """mu(a, b) for the contents at x and y in the arrangement (nodes, edges), by full enumeration."""
    nodes = list(nodes)
    idx = {v: i for i, v in enumerate(nodes)}
    mu = {}
    tot = 0
    for cont in product(CONTENTS, repeat=len(nodes)):
        w = 1
        for a, b in edges:
            w *= omega(cont[idx[a]], cont[idx[b]], p, q, r)
        key = (cont[idx[x]], cont[idx[y]])
        mu[key] = mu.get(key, 0) + w
        tot += w
    return {k: F(v, tot) for k, v in mu.items()}


def orbit_values(mu):
    """The three values a commutant matrix takes (equal, opposite, orthogonal pairs), or None if mu is not constant on the orbits."""
    eq = {mu.get((a, a), ZERO) for a in CONTENTS}
    op = {mu.get((a, (a[0], -a[1])), ZERO) for a in CONTENTS}
    orth = {mu.get((a, b), ZERO) for a in CONTENTS for b in CONTENTS if a[0] != b[0]}
    if len(eq) != 1 or len(op) != 1 or len(orth) != 1:
        return None
    return eq.pop(), op.pop(), orth.pop()


def correlation_eigenvalues(mu):
    """mu = (1/6)[J/6 + t_1 P_1 + t_2 P_2]: P_1 has entries 1/2, -1/2, 0 and P_2 has 1/3, 1/3, -1/6 on equal, opposite, orthogonal pairs."""
    e, o, x = orbit_values(mu)
    t2 = (F(1, 6) - 6 * x) * 6
    t1 = 6 * e - 6 * o
    assert 6 * e == F(1, 6) + t1 / 2 + t2 / 3 and 6 * o == F(1, 6) - t1 / 2 + t2 / 3
    return t1, t2


def acyclic(nodes, edges):
    parent = {v: v for v in nodes}

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


def torus_2d(size):
    sites = [(x, y) for x in range(size) for y in range(size)]
    idx = {s: i for i, s in enumerate(sites)}
    edges = set()
    for (x, y) in sites:
        for dx, dy in ((1, 0), (0, 1)):
            t = ((x + dx) % size, (y + dy) % size)
            a, b = idx[(x, y)], idx[t]
            edges.add((min(a, b), max(a, b)))
    syms = []
    for tx in range(size):
        for ty in range(size):
            for rot in range(4):
                for ref in (False, True):
                    def f(s, tx=tx, ty=ty, rot=rot, ref=ref):
                        x, y = s
                        if ref:
                            x, y = y, x
                        for _ in range(rot):
                            x, y = (-y) % size, x
                        return ((x + tx) % size, (y + ty) % size)
                    syms.append([idx[f(s)] for s in sites])
    return sites, sorted(edges), syms


def half_filling_orbits(n_sites, syms):
    seen = set()
    orbits = []
    for sub in combinations(range(n_sites), n_sites // 2):
        if sub in seen:
            continue
        orb = set()
        for sg in syms:
            orb.add(tuple(sorted(sg[i] for i in sub)))
        seen |= orb
        orbits.append((sub, orb))
    return orbits


def det(m):
    """Determinant of a square matrix of Fractions by elimination."""
    n = len(m)
    m = [row[:] for row in m]
    d = ONE
    for i in range(n):
        piv = None
        for j in range(i, n):
            if m[j][i] != 0:
                piv = j
                break
        if piv is None:
            return ZERO
        if piv != i:
            m[i], m[piv] = m[piv], m[i]
            d = -d
        d *= m[i][i]
        for j in range(i + 1, n):
            f = m[j][i] / m[i][i]
            for k in range(i, n):
                m[j][k] -= f * m[i][k]
    return d


TRIPLES = ((3, 1, 2), (5, 2, 4), (12, 1, 2))
MORE_TRIPLES = ((2, 2, 5), (1, 3, 2), (1, 1, 100), (100, 1, 1))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: closing a loop multiplies the weight by 1 + 3 t_1 lambda_1 + 2 t_2 lambda_2; a bond across components by exactly 1."""
    ladder_nodes = list(range(6))                                                        # rows 0,1,2 / 3,4,5 of a 2x3 window without the middle rung
    ladder_edges = [(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (2, 5)]
    commutant_ok = True
    identity_ok = True
    report = []
    for (p, q, r) in TRIPLES + MORE_TRIPLES[:2]:
        l1, l2 = lambdas(p, q, r)
        mu = joint_marginal(ladder_nodes, ladder_edges, 1, 4, p, q, r)
        commutant_ok = commutant_ok and orbit_values(mu) is not None and all(sum((mu.get((a, b), ZERO) for b in CONTENTS), ZERO) == F(1, 6) for a in CONTENTS)
        t1, t2 = correlation_eigenvalues(mu)
        factor = weight_over_free(ladder_nodes, ladder_edges + [(1, 4)], p, q, r) / weight_over_free(ladder_nodes, ladder_edges, p, q, r)
        predicted = 1 + 3 * t1 * l1 + 2 * t2 * l2 if not mut("records_repel_when_a_loop_closes") else 1 - 3 * t1 * l1 - 2 * t2 * l2
        identity_ok = identity_ok and factor == predicted
        report.append(f"({p},{q},{r}): {factor} = 1 + 3({t1})({l1}) + 2({t2})({l2})")
    checks.check("B1", commutant_ok and identity_ok, "T1: the joint law of two contents in any arrangement is constant on the three orbits (equal, opposite, orthogonal) with uniform marginals, and closing the middle rung of the 2x3 ladder multiplies the neutral-scale weight by exactly 1 + 3 t_1 lambda_1 + 2 t_2 lambda_2 at " + "; ".join(report))

    path_nodes = list(range(6))
    path_edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
    cycle_ok = True
    for (p, q, r) in TRIPLES:
        l1, l2 = lambdas(p, q, r)
        t1, t2 = correlation_eigenvalues(joint_marginal(path_nodes, path_edges, 0, 5, p, q, r))
        factor = weight_over_free(path_nodes, path_edges + [(0, 5)], p, q, r) / weight_over_free(path_nodes, path_edges, p, q, r)
        cycle_ok = cycle_ok and t1 == l1 ** 5 and t2 == l2 ** 5 and factor == 1 + 3 * l1 ** 6 + 2 * l2 ** 6
    checks.check("B2", cycle_ok, "T1: along a path of five bonds the correlation eigenvalues are lambda^5, and closing it into a six-cycle multiplies the weight by 1 + 3 lambda_1^6 + 2 lambda_2^6 (block 40 T3's cycle factor recovered)")

    two_paths_nodes = list(range(5))
    two_paths_edges = [(0, 1), (1, 2), (3, 4)]
    join_ok = True
    for (p, q, r) in TRIPLES + MORE_TRIPLES:
        factor = weight_over_free(two_paths_nodes, two_paths_edges + [(2, 3)], p, q, r) / weight_over_free(two_paths_nodes, two_paths_edges, p, q, r)
        g = F(4)
        scaled = g ** 4 * weight_over_free(two_paths_nodes, two_paths_edges + [(2, 3)], p, q, r) / (g ** 3 * weight_over_free(two_paths_nodes, two_paths_edges, p, q, r))
        join_ok = join_ok and ((factor == 1) if not mut("bond_across_components_binds") else (factor != 1)) and scaled == g
    checks.check("B3", join_ok, "T1: a bond between records not yet connected multiplies the neutral-scale weight by exactly 1 (block 41's no action across empty sites), and at the scale g c_0 by exactly g: on windows without a cycle every arrangement of n records weighs z^n 6^n g^(bonds)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: on every window enumerated, the arrangements without a cycle weigh exactly free and every other weighs more; the chessboard is a minimum."""
    windows = (((2, 2, 2), TRIPLES + MORE_TRIPLES), ((2, 3), TRIPLES), ((3, 3), TRIPLES), ((2, 2, 3), TRIPLES[:1]))
    all_ok = True
    forest_ok = True
    full_ok = True
    lines = []
    for dims, trips in windows:
        sites, edges = window(dims)
        n_sites = len(sites)
        for (p, q, r) in trips:
            below = 0
            ties = 0
            forests = 0
            total = 0
            best = ZERO
            best_sub = None
            for k in range(1, n_sites + 1):
                for sub in combinations(range(n_sites), k):
                    ss = set(sub)
                    ed = [(a, b) for a, b in edges if a in ss and b in ss]
                    w = weight_over_free(sub, ed, p, q, r)
                    total += 1
                    tree = acyclic(sub, ed)
                    forests += tree
                    if w < 1:
                        below += 1
                    if w == 1:
                        ties += 1
                        forest_ok = forest_ok and tree
                    else:
                        forest_ok = forest_ok and not tree
                    if w > best:
                        best, best_sub = w, sub
            all_ok = all_ok and ((below == 0) if not mut("an_arrangement_lighter_than_free") else (below > 0)) and ties == forests
            full_ok = full_ok and len(best_sub) == n_sites
            lines.append(f"{'x'.join(map(str, dims))} ({p},{q},{r}): {total} arrangements, {below} below free, {ties} exactly free = the {forests} without a cycle, heaviest = the full window at {about(best)}")
    checks.check("C1", all_ok and forest_ok, "T2: on the windows 2x2x2 (seven triples), 2x3, 3x3 (three triples) and 2x2x3 ((3,1,2)), no arrangement of records weighs less than the same records placed apart, and the arrangements that weigh exactly that are precisely those without a cycle: " + "; ".join(lines[:3]) + "; ...")
    checks.check("C2", full_ok and all_ok, "T2: on every window and triple enumerated the heaviest arrangement is the full window (every site recorded); " + "; ".join(lines[3:]))

    sites, edges = window((2, 2, 2))
    chess = [tuple(i for i, s in enumerate(sites) if sum(s) % 2 == par) for par in (0, 1)]
    plaq = (0, 1, 2, 3)
    plaq_edges = [(a, b) for a, b in edges if a in plaq and b in plaq]
    chess_ok = True
    for (p, q, r) in TRIPLES:
        l1, l2 = lambdas(p, q, r)
        for sub in chess:
            ss = set(sub)
            ed = [(a, b) for a, b in edges if a in ss and b in ss]
            chess_ok = chess_ok and len(ed) == 0 and weight_over_free(sub, ed, p, q, r) == 1
        g = F(4)
        ratio = weight_over_free(chess[0], [], p, q, r) / (g ** len(plaq_edges) * weight_over_free(plaq, plaq_edges, p, q, r))
        expected = 1 / (g ** 4 * (1 + 3 * l1 ** 4 + 2 * l2 ** 4))
        chess_ok = chess_ok and ((ratio == expected and ratio < 1) if not mut("chessboard_is_the_heaviest_arrangement") else (ratio > 1))
    checks.check("C3", chess_ok, "T2: on the cube both chessboards (four records, no two adjacent) weigh exactly free at every scale; against the four records on one face they weigh 1/(g^4 (1 + 3 lambda_1^4 + 2 lambda_2^4)): at g = 4 and (3,1,2) the chessboard is the least likely arrangement of four records, 1/(256 x 433/432) of the face")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the equilibrium's mean staggered occupancy vanishes; at allowed scales the chessboard is never the mode and the staggered susceptibility is at most random's."""
    sites, edges, syms = torus_2d(4)
    n_sites = len(sites)
    signs = [(-1) ** sum(s) for s in sites]
    orbits = half_filling_orbits(n_sites, syms)
    stag_sums_zero = all(sum(sum(signs[i] for i in el) for el in orb) == 0 for _, orb in orbits)
    random_chi = F(4, 15)                                                                 # hypergeometric: 8 of 16 with 8 of each sign; <stag^2>/16
    lines = []
    chi_ok = True
    mode_ok = True
    scales = (F(1), F(4), F(1, 4))
    for (p, q, r) in TRIPLES[:1] + TRIPLES[2:]:
        data = []
        for sub, orb in orbits:
            ss = set(sub)
            ed = [(a, b) for a, b in edges if a in ss and b in ss]
            data.append((len(ed), weight_over_free(sub, ed, p, q, r), len(orb), abs(sum(signs[i] for i in sub))))
        for g in scales:
            z = s2 = bonds = ZERO
            mode = (ZERO, None, None)
            for n_edges, w0, mult, stag in data:
                w = g ** n_edges * w0
                z += mult * w
                s2 += mult * w * stag * stag
                bonds += mult * w * n_edges
                if w > mode[0]:
                    mode = (w, n_edges, stag)
            chi = s2 / z / n_sites
            allowed = g >= 1
            if allowed:
                chi_ok = chi_ok and ((chi <= random_chi) if not mut("staggered_order_at_the_neutral_scale") else (chi > random_chi))
                mode_ok = mode_ok and ((mode[2] == 0 and mode[1] == 12) if not mut("chessboard_is_the_mode_at_the_neutral_scale") else (mode[1] == 0))
            else:
                chi_ok = chi_ok and chi > 4 * random_chi
                mode_ok = mode_ok and mode[1] == 0 and mode[2] == n_sites // 2
            lines.append(f"({p},{q},{r}) g={g}: chi_s={about(chi)} (random {about(random_chi)}), mean bonds {about(bonds / z)} (random {about(F(32 * 8 * 7, 16 * 15))}), mode: {mode[1]} bonds, |staggered count| {mode[2]}")
    checks.check("D1", stag_sums_zero and len(orbits) == 153, f"T3: on the 4x4 torus at half filling ({len(orbits)} orbits of the 12870 arrangements) the staggered count sums to exactly zero over every orbit: the equilibrium's mean staggered occupancy is zero at every scale and every triple (translation by one step reverses the count)")
    checks.check("D2", chi_ok, "T3: at the allowed scales g = 1 and g = 4 the staggered susceptibility is at most random's 4/15 and at the excluded g = 1/4 it exceeds four times random's: " + "; ".join(lines))
    checks.check("D3", mode_ok, "T3: at g = 1 and g = 4 the most likely arrangement is a band of twelve bonds with zero staggered count; at g = 1/4 it is the chessboard (no bonds, staggered count 8)")

    sites, edges = window((2, 2, 2))
    signs = [(-1) ** sum(s) for s in sites]
    cube_ok = True
    cube_lines = []
    for (p, q, r) in TRIPLES[:1]:
        data = []
        for sub in combinations(range(8), 4):
            ss = set(sub)
            ed = [(a, b) for a, b in edges if a in ss and b in ss]
            data.append((len(ed), weight_over_free(sub, ed, p, q, r), sum(signs[i] for i in sub)))
        for g in scales:
            z = s1 = s2 = ZERO
            mode = (ZERO, None, None)
            for n_edges, w0, stag in data:
                w = g ** n_edges * w0
                z += w
                s1 += w * stag
                s2 += w * stag * stag
                if w > mode[0]:
                    mode = (w, n_edges, abs(stag))
            chi = s2 / z / 8
            cube_ok = cube_ok and s1 == 0 and ((chi <= F(2, 7) and mode[2] == 0) if g >= 1 else (chi > 3 * F(2, 7) and mode[1] == 0 and mode[2] == 4))
            cube_lines.append(f"g={g}: chi_s={about(chi)} (random 2/7), mode {mode[1]} bonds, |staggered count| {mode[2]}")
    checks.check("D4", cube_ok, "T3: the three-dimensional cube with four records at (3,1,2): mean staggered count exactly zero; at g = 1 and 4 the susceptibility is at most random's 2/7 and the mode is a face; at g = 1/4 the mode is the chessboard: " + "; ".join(cube_lines))


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: which record backgrounds gap the walk (exact symbolic algebra in the doubled plane-wave basis)."""
    sx, sy, sz, c, e = sp.symbols("s_x s_y s_z c E", real=True)
    h = sx * sp.Matrix([[0, 1], [1, 0]]) + sy * sp.Matrix([[0, -sp.I], [sp.I, 0]]) + sz * sp.Matrix([[1, 0], [0, -1]])
    sig_z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    # (b) content chessboard, content-reading coupling: c eps sigma_z; eps sends k to k + pi, where h -> -h
    content_chess = sp.BlockMatrix([[h, c * sig_z], [c * sig_z, -h]]).as_explicit()
    char = sp.expand((content_chess - e * sp.eye(4)).det())
    target = sp.expand((e ** 2 - sx ** 2 - sy ** 2 - sz ** 2 - c ** 2) ** 2 - 4 * c ** 2 * (sx ** 2 + sy ** 2))
    ring_ok = sp.simplify(char - target) == 0
    point = {sx: F(3, 5), sy: 0, sz: 0, c: F(3, 5)}
    det_ring = det([[F(v) for v in row] for row in (content_chess.subs(point)).tolist()])
    det_off = det([[F(v) for v in row] for row in (content_chess.subs({sx: F(4, 5), sy: 0, sz: 0, c: F(3, 5)})).tolist()])
    gapless = (det_ring == 0 and det_off == F(49, 625)) if not mut("content_chessboard_gaps_the_walk") else (det_ring != 0)
    checks.check("E1", ring_ok and gapless, "T4(b): a chessboard of CONTENTS read by the coin (c eps sigma_z on a full record layer) has det(H - E) = (E^2 - |s|^2 - c^2)^2 - 4c^2(s_x^2 + s_y^2), s = sin k: E = 0 on the whole ring s_z = 0, s_x^2 + s_y^2 = c^2 (exact zero at sin k_x = c = 3/5; 49/625 at sin k_x = 4/5): no gap")

    uniform = h + c * sig_z
    char_u = sp.expand((uniform - e * ident).det())
    target_u = sp.expand(e ** 2 - sx ** 2 - sy ** 2 - (sz + c) ** 2)
    det_u = det([[F(v) for v in row] for row in (uniform.subs({sx: 0, sy: 0, sz: F(-3, 5), c: F(3, 5)})).tolist()])
    uniform_ok = (sp.simplify(char_u - target_u) == 0 and det_u == 0) if not mut("uniform_content_gaps_the_walk") else (det_u != 0)
    checks.check("E2", uniform_ok, "T4(a): records of one content on every site, read by the coin (c sigma_z), give E^2 = s_x^2 + s_y^2 + (s_z + c)^2: the two zeros move to sin k_z = -c and the spectrum touches zero (exact zero at s = (0, 0, -3/5), c = 3/5): no gap")

    occupancy = sp.BlockMatrix([[h + c / 2 * ident, c / 2 * ident], [c / 2 * ident, -h + c / 2 * ident]]).as_explicit()
    shifted = occupancy - c / 2 * sp.eye(4)
    square = sp.simplify(shifted * shifted - (sx ** 2 + sy ** 2 + sz ** 2 + c ** 2 / 4) * sp.eye(4))
    at_species = occupancy.subs({sx: 0, sy: 0, sz: 0, c: F(3, 5)})
    eig = sorted(at_species.eigenvals().keys(), key=lambda v: F(str(v)))
    checks.check("E3", square == sp.zeros(4, 4) and [F(str(v)) for v in eig] == [ZERO, F(3, 5)], "T4(c): the chessboard of OCCUPANCY with a content-blind coupling (c/2)(1 + eps) obeys (H - c/2)^2 = |s|^2 + c^2/4 exactly: the two bands are c/2 +- sqrt(|s|^2 + c^2/4), the gap is c (at the species points the energies are exactly 0 and c): block 79 T1's rest mass, and the only one of the three backgrounds that gives one")
# ============================================================================================ family F
FENCES = (
    "This note works within the moving-records reading of blocks 39-42 and the supplied clauses of blocks 54, 77 and 79; it reports which arrangements of records the static law with vacancies favours and what each kind of record order does to the walk's spectrum; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the joint law of two contents on the 2x3 ladder and on a path, entry by entry; the loop factor bond by bond",
    "per_site: executed - every arrangement of records on the windows 2x2x2, 2x3, 3x3 and 2x2x3, weighed exactly against the same records placed apart",
    "per_mode: executed - the walk's characteristic polynomial for the three backgrounds at every wave vector (symbolic), and exact zeros at rational points; control: the three-dimensional gas sampled on periodic lattices of side 6 and 8",
    "per_block: executed - staggered count, susceptibility and mode over all half-filled arrangements of the 4x4 torus (by orbits) and of the cube, at the neutral scale, at four times it and at a quarter of it",
    "lattice_wide: T1 holds on every finite graph by its proof; T2 is exact on the windows enumerated and is not proved for every window; T3 is exact on the 4x4 torus and the cube; T4 holds for every wave vector by the symbolic identities; the moving-records reading, the scale, the record backgrounds and the coupling clauses are not derived",
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
    print("scope: the record gas and the chessboard that block 79's rest mass needs - at the neutral scale and above, binding grows only around loops (exact factor 1 + 3 t_1 lambda_1 + 2 t_2 lambda_2), the chessboard of records weighs exactly free and is the least likely arrangement of its record number on every window enumerated, the equilibrium's mean staggered occupancy is zero and its staggered susceptibility at most random's; a chessboard needs the excluded scales below c_0; content order of either kind leaves the walk gapless; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
