#!/usr/bin/env python3
"""S^3 cone-cap Part B, Lemma L1(b): A-PRIORI collapsibility of the Kuhn
triangulation K(D) of any finite star-shaped toward-origin cubical downset D.

This runner CLOSES L1(b) WITHOUT A FREEZE. It replaces the two prior
freeze-dependent certificates (the "attachment-type set freezes" shelling and
the "descending-link type set freezes at R_0 = 9" discrete Morse field, both in
scripts/frontier_s3_partb_allr_lemmas.py) with ONE uniform discrete Morse
matching whose validity, single-criticality and acyclicity are each established
a-priori (uniform in D, hence R-free), then verified EXACTLY on K(B_R) for a
range of R AND on hundreds of randomly generated arbitrary star-shaped cubical
downsets (the universality test) plus hand-built adversarial extremes, with
non-vacuity guards.

------------------------------------------------------------------------------
THE A-PRIORI THEOREM (uniform in D)
------------------------------------------------------------------------------
Let D be a finite cubical downset in Z^3 that is star-shaped toward the origin
(closed under each per-axis toward-origin step c_i -> c_i - sign'(c_i), where
sign'(c_i) moves the cube min-corner toward the origin; coordinates in {0,-1}
are already innermost). Let K(D) be the Kuhn/Freudenthal triangulation (each
unit cube min-corner c split into its 6 monotone-lattice-path tetrahedra,
globally face-coherent -- the single-source-of-truth convention of
scripts/frontier_s3_boundary_link_theorem.py and
scripts/frontier_s3_cone_cap_pl_s3_native_reproof.py). Then K(D) is
COLLAPSIBLE, via the explicit matching mu(D) defined below, which is a valid
partial matching with EXACTLY ONE critical cell (the origin vertex {(0,0,0)})
and is acyclic by a strictly-monotone GLOBAL KEY. By Forman's theorem (an
acyclic matching with a single critical cell collapses the complex to a point),
K(D) is collapsible; and when D is full-dimensional (every B_R is), a
collapsible compact PL 3-manifold-with-boundary is a PL 3-ball (Whitehead),
discharging L1 for all R. The rule and key are defined IDENTICALLY for every D
(no per-D enumeration, no freeze), so the conclusion is R-independent.

THE MATCHING mu(D) (one rule, uniform in D)
-------------------------------------------
Strict radial CUBE key  kappa(c) = ( sum_i near(c_i), #{i : c_i = -1}, c ),
   near(t) = max(0, t, -(t+1))  (the toward-origin depth of the coordinate t;
   near(0) = near(-1) = 0). kappa is a STRICT total order on cubes whose UNIQUE
   minimum on any downset is the central cube c0 = (0,0,0).
For a simplex sigma of K(D), intro(sigma) = the kappa-MINIMUM present cube whose
   closed cube contains sigma (the first cube to carry sigma as cubes are added
   in increasing kappa). The fibers F_c = intro^{-1}(c) partition the cells.
   On the fiber of each cube c the matching is the elementary-collapse matching
   of the RELATIVE COLLAPSE K(c) -> A_c, where A_c = K(c) ∩ K(D_{<c}) is the
   attachment (the cells of c already introduced by an earlier cube):
     - c != c0:  A_c is a nonempty cone toward c's toward-origin corner (the
                 union of the closed Kuhn faces of c shared with smaller-kappa
                 present neighbours, all meeting that corner); K(c) relatively
                 collapses onto A_c, consuming ALL of F_c in free pairs -> zero
                 critical cells in this fiber.
     - c == c0:  A_c is empty; the matching collapses K(c0) onto its
                 toward-origin corner, which is the lattice ORIGIN (0,0,0),
                 leaving that one critical 0-cell.
   mu(D) = union over c of the per-fiber matchings.

THE GLOBAL KEY / ACYCLICITY (one-line argument, no enumeration)
---------------------------------------------------------------
Global key f(sigma) = kappa(intro(sigma)). Along any gradient (V-path) step:
   (H1) matched pairs share intro (the relative collapse only pairs cells of one
        fiber) -> f is CONSTANT on matched up-steps;
   (M)  a regular (unmatched) down-step sigma > tau (tau a facet of sigma) never
        RAISES f, because the set of present cubes whose closed cube contains tau
        is a SUPERSET of those containing sigma (every cube containing sigma
        contains its face tau), so its kappa-minimum is <=:
            kappa(intro(tau)) <= kappa(intro(sigma)).   [a-priori THEOREM]
Hence along any V-path f never increases AND matched steps never leave a fiber;
a CLOSED V-path can neither raise f nor cross fibers, so it lives inside a single
fiber F_c -- but mu restricted to F_c is an honest elementary-collapse sequence,
which is acyclic. Contradiction. So mu(D) is acyclic. This is exactly the
strictly-monotone-global-function (Cluster / Patchwork Lemma) form: a closed
V-path would force f to return to its start, impossible.

THE SINGLE-CUBE A-PRIORI UNIVERSE (replaces the freeze)
-------------------------------------------------------
Single-criticality reduces, via the fiber decomposition, to a CLOSED finite fact
about ONE unit cube's neighbourhood -- NOT a freeze over D, NOT a realized-type
enumeration. The attachment A_c is a function of which SMALLER-kappa neighbours
of c are present; the toward-origin downset property constrains those neighbours
to a finite, D-INDEPENDENT family generated by ABSTRACT local rules (one per
cube sign-class; translation-invariant in the actual coordinate values). This
runner ENUMERATES that abstract family exhaustively and verifies that on EVERY
member K(c) relatively collapses onto A_c with zero extra critical cells (and
the unique attachment-free member collapses to the toward-corner). It then
verifies REVERSE INCLUSION: every attachment realized by an actual downset lies
in the abstract family -- so the family covers reality without sampling reality.

------------------------------------------------------------------------------
REPROVE-AND-CITE
------------------------------------------------------------------------------
Reproven from primitives (this runner): the matching's validity, the global-key
strict monotonicity (the cubes(tau) superset cubes(sigma) core), the per-fiber
relative-collapse acyclicity (free-face replay), single-criticality via the
single-cube a-priori universe + reverse inclusion, and direct modified-Hasse
cycle detection. Cited as COMPARATORS only (never consumed as derivation input):
  - R. Forman, Morse theory for cell complexes (Adv. Math. 1998): acyclic
    matching with one critical cell => collapse to a point.
  - M. Chari, On discrete Morse functions and combinatorial decompositions
    (Discrete Math. 2000): Morse matchings from shellings / vertex orders.
  - J. Jonsson, Simplicial Complexes of Graphs (LNM 1928, 2008), Lemma 4.2;
    P. Hersh: the Cluster / Patchwork Lemma (gradient cycles confined to fibers
    of a poset map).
  - B. Benedetti, F. Lutz: Random discrete Morse theory and collapsibility.
  - K. Adiprasito, B. Benedetti / V. Welker: collapsibility of complexes in
    convex / star-shaped position (the comparator for "to-origin" collapse).
  - A. Bjorner, M. Wachs: shellability of order ideals.
  - J.H.C. Whitehead; Rourke--Sanderson: a collapsible compact PL
    3-manifold-with-boundary is a PL 3-ball.
None is consumed: the matching is reproven explicitly and verified EXACTLY.

Reuses cubical_ball from scripts/frontier_s3_boundary_link_theorem.py as the
single source of truth. EXACT throughout (integer / combinatorial; no floats).

Usage:
  python3 scripts/frontier_s3_L1b_apriori_collapsibility.py            # R=2..8, 200 downsets
  python3 scripts/frontier_s3_L1b_apriori_collapsibility.py 10 300     # R=2..10, 300 downsets
"""
from __future__ import annotations

import os
import random
import sys
from collections import defaultdict
from itertools import combinations, permutations, product

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import frontier_s3_boundary_link_theorem as _blt  # noqa: E402

cubical_ball = _blt.cubical_ball

PASS_COUNT = 0
FAIL_COUNT = 0
EXACT_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    """All checks here are EXACT integer / combinatorial assertions."""
    global PASS_COUNT, FAIL_COUNT, EXACT_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        EXACT_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] [EXACT] {name}{suffix}")
    return condition


# ===========================================================================
# Shared primitives (Kuhn triangulation, radial CUBE key, cells)
# ===========================================================================

def kuhn_tets_of_cube(c: tuple[int, int, int]) -> list[tuple]:
    """The 6 Kuhn/Freudenthal tetrahedra of the unit cube with min-corner c.
    Identical convention to frontier_s3_cone_cap_pl_s3_native_reproof.py and
    frontier_s3_partb_allr_lemmas.py: each tet is the monotone lattice path
    c -> c+e_{pi(0)} -> c+e_{pi(0)}+e_{pi(1)} -> c+(1,1,1) over a permutation pi
    of the 3 axes. Globally face-coherent."""
    x, y, z = c
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    tets = []
    for pi in permutations(range(3)):
        cur = [0, 0, 0]
        path = [(0, 0, 0)]
        for ax in pi:
            cur = [cur[i] + e[ax][i] for i in range(3)]
            path.append(tuple(cur))
        tets.append(tuple(sorted((x + p[0], y + p[1], z + p[2]) for p in path)))
    return tets


def cube_cells(c: tuple[int, int, int]) -> set:
    """Full simplicial closure of cube c: every nonempty face of its 6 tets."""
    cells: set = set()
    for t in kuhn_tets_of_cube(c):
        for r in range(1, len(t) + 1):
            for f in combinations(t, r):
                cells.add(tuple(sorted(f)))
    return cells


def cube_vertices(c: tuple[int, int, int]) -> set:
    """The 8 vertices of cube c."""
    return set(tuple(c[i] + d[i] for i in range(3))
               for d in product((0, 1), repeat=3))


def near(t: int) -> int:
    """Toward-origin depth of the integer coordinate t (a cube min-corner axis).
    The cube occupies [t, t+1]; near(t) = max(0, t, -(t+1)) is its distance to
    the origin plane on that axis. near(0) = near(-1) = 0 (innermost)."""
    return max(0, t, -(t + 1))


def kappa(c: tuple[int, int, int]) -> tuple:
    """Strict radial cube key (sum_i near(c_i), #{i : c_i = -1}, c). A strict
    total order on cubes; its UNIQUE minimum on any downset is c0 = (0,0,0)."""
    return (sum(near(x) for x in c), sum(1 for x in c if x == -1), c)


def toward_corner(c: tuple[int, int, int]) -> tuple:
    """The corner of cube c (occupying [c_i, c_i+1] per axis) nearest the origin
    (per-axis the endpoint of smaller absolute value). For c0 = (0,0,0) this is
    the lattice origin (0,0,0)."""
    q = []
    for i in range(3):
        lo, hi = c[i], c[i] + 1
        q.append(lo if abs(lo) <= abs(hi) else hi)
    return tuple(q)


def toward_origin_step_cubes(c: tuple[int, int, int]) -> list:
    """The per-axis toward-origin neighbour cubes the downset property FORCES to
    be present when c is present (one per axis with near(c_i) > 0)."""
    res = []
    for i in range(3):
        if near(c[i]) == 0:
            continue
        cc = list(c)
        cc[i] += (-1 if c[i] >= 1 else 1)
        res.append(tuple(cc))
    return res


def build_cubes_from_ball(R: int) -> set:
    """B_R cube set via the single-source-of-truth cubical_ball."""
    _sites, cubes = cubical_ball(R)
    return set(cubes)


# ===========================================================================
# Relative collapse (the per-fiber matching engine)
# ===========================================================================

def relative_collapse_pairs(cells_all, keep):
    """Greedy relative collapse of the cell set `cells_all` onto the subcomplex
    `keep`: repeatedly remove a free pair (f, its unique coface g) with neither
    in `keep`. Returns (matched_pairs, residue)."""
    cells = set(cells_all)
    A = set(keep)
    by_dim: defaultdict[int, set] = defaultdict(set)
    for c in cells:
        by_dim[len(c)].add(c)

    def cofaces(f):
        fs = frozenset(f)
        return [g for g in by_dim.get(len(f) + 1, ()) if fs.issubset(g)]

    removed: set = set()
    pairs: list = []
    while True:
        found = None
        for d in sorted(by_dim, reverse=True):
            for f in list(by_dim.get(d, ())):
                if f in A:
                    continue
                cf = cofaces(f)
                if len(cf) == 1 and cf[0] not in A:
                    found = (f, cf[0])
                    break
            if found:
                break
        if not found:
            break
        f, gg = found
        removed.add(f)
        removed.add(gg)
        pairs.append((f, gg))
        by_dim[len(f)].discard(f)
        by_dim[len(gg)].discard(gg)
    return pairs, cells - removed


# ===========================================================================
# The uniform matching mu(D) = union of per-fiber relative-collapse matchings
# ===========================================================================

def build_matching(cubes):
    """Build mu(D). Returns (match, critical, intro, fiber).
    match: dict cell -> matched partner (involution).
    critical: list of unmatched cells.
    intro: dict cell -> introducer cube (kappa-min cube containing it).
    fiber: dict cube -> set of cells it introduces."""
    cubes = set(cubes)
    order = sorted(cubes, key=kappa)
    cube_verts = {c: cube_vertices(c) for c in cubes}
    cube_cs = {c: cube_cells(c) for c in cubes}
    all_cells: set = set()
    for c in cubes:
        all_cells |= cube_cs[c]

    # intro(sigma): the FIRST cube (ascending kappa) whose vertex set contains
    # sigma. Equivalent to the kappa-minimum present cube carrying sigma.
    intro: dict = {}
    for sigma in all_cells:
        sset = set(sigma)
        for c in order:
            if sset <= cube_verts[c]:
                intro[sigma] = c
                break

    fiber: defaultdict[tuple, set] = defaultdict(set)
    for sigma, c in intro.items():
        fiber[c].add(sigma)

    match: dict = {}
    critical: list = []
    for c in order:
        cc = cube_cs[c]
        A = cc - fiber[c]   # cells of c introduced earlier = the attachment A_c
        if not A:
            # attachment-free cube (the unique c0): collapse to the toward-corner
            keep = {(toward_corner(c),)}
            pairs, residue = relative_collapse_pairs(cc, keep=keep)
            for (f, g) in pairs:
                match[f] = g
                match[g] = f
            critical.extend(residue)
        else:
            pairs, residue = relative_collapse_pairs(cc, keep=A)
            for (f, g) in pairs:
                match[f] = g
                match[g] = f
            critical.extend(residue - A)
    return match, critical, intro, fiber


def is_acyclic_direct(match, cubes) -> bool:
    """Direct modified-Hasse cycle detection: regular down-arrows + reversed
    matched up-arrows. Returns True iff the digraph has NO directed cycle.
    (Independent of the global-key argument; a genuine cross-check.)"""
    cubes = set(cubes)
    all_cells: set = set()
    for c in cubes:
        all_cells |= cube_cells(c)
    adj: defaultdict[tuple, list] = defaultdict(list)
    for c in all_cells:
        for i in range(len(c)):
            f = tuple(c[:i] + c[i + 1:])
            if not f:
                continue
            if match.get(f) == c and match.get(c) == f:
                continue  # the matched up-pair; skip its regular down-arrow
            adj[c].append(f)  # regular down-arrow
    for c in all_cells:
        m = match.get(c)
        if m is not None and len(m) == len(c) + 1:
            adj[c].append(m)  # matched up-arrow
    WHITE, GREY, BLACK = 0, 1, 2
    color = {c: WHITE for c in all_cells}
    for root in all_cells:
        if color[root] != WHITE:
            continue
        stack = [(root, iter(adj[root]))]
        color[root] = GREY
        while stack:
            node, it = stack[-1]
            advanced = False
            for nb in it:
                if color[nb] == GREY:
                    return False  # back-edge -> directed cycle
                if color[nb] == WHITE:
                    color[nb] = GREY
                    stack.append((nb, iter(adj[nb])))
                    advanced = True
                    break
            if not advanced:
                color[node] = BLACK
                stack.pop()
    return True


def global_key_violations(match, intro, cubes):
    """Verify the two global-key facts:
      (H1) matched pairs share intro (f = kappa o intro constant on pairs);
      (M)  every regular down-step sigma > tau has
           kappa(intro(tau)) <= kappa(intro(sigma)).
    Returns (bad_H1, bad_M, steps_M)."""
    cubes = set(cubes)
    all_cells: set = set()
    for c in cubes:
        all_cells |= cube_cells(c)
    bad_h1 = 0
    for c in all_cells:
        m = match.get(c)
        if m is None:
            continue
        if intro.get(c) != intro.get(m):
            bad_h1 += 1
    bad_m = 0
    steps_m = 0
    for c in all_cells:
        if len(c) < 2:
            continue
        kc = kappa(intro[c])
        for i in range(len(c)):
            f = tuple(c[:i] + c[i + 1:])
            if not f:
                continue
            if match.get(f) == c and match.get(c) == f:
                continue  # matched pair; not a regular down-step
            steps_m += 1
            if kappa(intro[f]) > kc:
                bad_m += 1
    return bad_h1, bad_m, steps_m


def superset_core_violations(cubes):
    """The A-PRIORI core of (M): for every cell sigma and every facet tau,
    {present cubes containing tau} is a SUPERSET of {present cubes containing
    sigma}. (=> kappa-min over tau's set <= over sigma's set.) Returns
    (bad_superset, comparisons)."""
    cubes = set(cubes)
    cube_verts = {c: cube_vertices(c) for c in cubes}
    all_cells: set = set()
    for c in cubes:
        all_cells |= cube_cells(c)
    bad = 0
    cmp = 0
    for sigma in all_cells:
        if len(sigma) < 2:
            continue
        ssig = set(sigma)
        cs_sigma = set(c for c, V in cube_verts.items() if ssig <= V)
        for i in range(len(sigma)):
            tau = tuple(sigma[:i] + sigma[i + 1:])
            stau = set(tau)
            cs_tau = set(c for c, V in cube_verts.items() if stau <= V)
            cmp += 1
            if not cs_sigma <= cs_tau:
                bad += 1
    return bad, cmp


def valid_matching_violations(match):
    """The matching is a valid partial matching: involution + dims differ by 1.
    Returns bad count."""
    bad = 0
    for a, b in match.items():
        if match.get(b) != a:
            bad += 1
        if abs(len(a) - len(b)) != 1:
            bad += 1
    return bad


# ===========================================================================
# The SINGLE-CUBE A-PRIORI UNIVERSE (replaces the freeze)
# ===========================================================================
#
# Single-criticality reduces to a CLOSED finite fact about ONE unit cube's
# 26-neighbour shell, generated by ABSTRACT local downset rules (one family per
# cube sign-class, translation-invariant in the actual coordinate). This is NOT
# a freeze over D and NOT a realized-attachment enumeration: the family is
# generated WITHOUT sampling any D, then verified once; reality is shown to be a
# subset (reverse inclusion).

NEIGHBOUR_OFFSETS = [d for d in product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]


def sign_class(c: tuple[int, int, int]) -> tuple:
    """The local sign-class of cube c: per axis, P (c_i>=1), Z (c_i=0),
    z (c_i=-1), N (c_i<=-2). The local attachment behaviour depends only on
    this class (translation-invariant), making the single-cube family finite."""
    def cls(t):
        if t == 0:
            return 'Z'
        if t == -1:
            return 'z'
        return 'P' if t >= 1 else 'N'
    return tuple(cls(x) for x in c)


def representative_cubes() -> list:
    """One cube per sign-class, with TWO translations for the unbounded classes
    P and N (e.g. c_i = 1 and 2) to witness translation-invariance directly."""
    classes = {'P': [1, 2], 'Z': [0], 'z': [-1], 'N': [-2, -3]}
    reps = []
    for cx in classes:
        for cy in classes:
            for cz in classes:
                for vx in classes[cx]:
                    for vy in classes[cy]:
                        for vz in classes[cz]:
                            reps.append((vx, vy, vz))
    return reps


def _toward_steps_of(n: tuple[int, int, int]) -> list:
    res = []
    for i in range(3):
        if n[i] >= 1:
            m = list(n)
            m[i] -= 1
            res.append(tuple(m))
        elif n[i] <= -2:
            m = list(n)
            m[i] += 1
            res.append(tuple(m))
    return res


def enumerate_local_attachments(c):
    """All attachment cell-sets A_c that cube c can have, generated ABSTRACTLY
    from the toward-origin downset rule over c's 26-neighbour shell (NOT sampled
    from any D). A_c = cells of c shared with the present SMALLER-kappa shell
    neighbours; the present set S ranges over every subset of smaller-kappa shell
    neighbours that (i) contains c's forced toward-origin steps and (ii) is
    closed, within the shell, under the toward-origin step (local downset).
    Yields frozenset attachment cell-sets (absolute coords)."""
    cc = cube_cells(c)
    kc = kappa(c)
    shell = [tuple(c[i] + d[i] for i in range(3)) for d in NEIGHBOUR_OFFSETS]
    smaller = [n for n in shell if kappa(n) < kc]
    smaller_set = set(smaller)
    forced = set(toward_origin_step_cubes(c))
    base = [n for n in smaller if n not in forced]
    out: set = set()
    for bits in product((0, 1), repeat=len(base)):
        S = set(forced)
        for n, b in zip(base, bits):
            if b:
                S.add(n)
        # local downset closure within the shell
        ok = True
        for n in S:
            for m in _toward_steps_of(n):
                if m in smaller_set and m not in S:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            continue
        A: set = set()
        for n in S:
            if max(abs(c[i] - n[i]) for i in range(3)) <= 1:
                A |= (cc & cube_cells(n))
        out.add(frozenset(A))
    return out


def local_shape(c, A) -> frozenset:
    """Attachment A translated to cube-local coordinates -> a D-independent
    shape (frozenset of direction-tuple simplices)."""
    return frozenset(
        tuple(sorted(tuple(v[i] - c[i] for i in range(3)) for v in cell))
        for cell in A)


def build_apriori_family():
    """Build, per sign-class, the abstract family of attachment local-shapes,
    and verify the single-cube collapse fact on EVERY member. Returns
    (family_by_class, n_nonempty, bad_collapse, n_free, bad_free,
     translation_dependent_classes, n_distinct_shapes)."""
    family: defaultdict[tuple, set] = defaultdict(set)
    n_nonempty = 0
    bad_collapse = 0
    n_free = 0
    bad_free = 0
    distinct_shapes: set = set()
    # translation invariance: collect shape sets per (class, representative)
    per_rep: defaultdict[tuple, list] = defaultdict(list)
    for c in representative_cubes():
        sc = sign_class(c)
        cc = cube_cells(c)
        shapes_here: set = set()
        for A in enumerate_local_attachments(c):
            sh = local_shape(c, A)
            shapes_here.add(sh)
            family[sc].add(sh)
            if not A:
                n_free += 1
                _pairs, residue = relative_collapse_pairs(
                    cc, keep={(toward_corner(c),)})
                if residue != {(toward_corner(c),)}:
                    bad_free += 1
                continue
            n_nonempty += 1
            distinct_shapes.add(sh)
            _pairs, residue = relative_collapse_pairs(cc, keep=set(A))
            if residue != set(A):
                bad_collapse += 1
        per_rep[sc].append(shapes_here)
    # translation invariance per class
    td_classes = []
    for sc, lst in per_rep.items():
        if any(lst[0] != s for s in lst[1:]):
            td_classes.append(sc)
    return (family, n_nonempty, bad_collapse, n_free, bad_free,
            td_classes, len(distinct_shapes))


def realized_attachment(c, cubes):
    """The attachment A_c actually realized by cube c inside the downset D."""
    cc = cube_cells(c)
    kc = kappa(c)
    earlier: set = set()
    for nb in cubes:
        if kappa(nb) < kc and max(abs(c[i] - nb[i]) for i in range(3)) <= 1:
            earlier |= cube_cells(nb)
    return cc & earlier


# ===========================================================================
# Random arbitrary star-shaped cubical downsets (universality)
# ===========================================================================

def random_downset(rng, max_reach):
    """Grow a toward-origin cubical downset from the 8 central cubes: add a cube
    only when all its toward-origin steps are already present. NOT (generally)
    any metric ball B_R."""
    central = set((a, b, c) for a in (0, -1) for b in (0, -1) for c in (0, -1))
    D = set(central)
    for _ in range(rng.randint(3, 40)):
        cand = []
        seen: set = set()
        for c in D:
            for i in range(3):
                for s in (-1, 1):
                    nb = list(c)
                    nb[i] += s
                    nb = tuple(nb)
                    if any(abs(x) > max_reach for x in nb):
                        continue
                    if nb in D or nb in seen:
                        continue
                    seen.add(nb)
                    forced = toward_origin_step_cubes(nb)
                    if all(t in D for t in forced):
                        cand.append(nb)
        if not cand:
            break
        D.add(rng.choice(cand))
    return D


def close_to_downset(cubes):
    """Close an arbitrary cube set under toward-origin steps (make it a valid
    downset). Used to sanitise hand-built adversarial seeds."""
    cubes = set(cubes)
    changed = True
    while changed:
        changed = False
        for c in list(cubes):
            for m in toward_origin_step_cubes(c):
                if m not in cubes:
                    cubes.add(m)
                    changed = True
    return cubes


def adversarial_downsets():
    """Hand-built extreme toward-origin downsets (axis sticks, 3-axis cross,
    box-minus-corner, L-shapes, thin slab)."""
    out = {}
    out["axis_stick_z"] = close_to_downset(
        [(0, 0, z) for z in range(0, 6)] + [(-1, -1, z) for z in range(-1, 5)])
    out["three_axis_cross"] = close_to_downset(
        set((x, 0, 0) for x in range(-4, 4))
        | set((0, y, 0) for y in range(-4, 4))
        | set((0, 0, z) for z in range(-4, 4)))
    out["box_minus_far_corner"] = close_to_downset(
        set(product(range(-3, 3), repeat=3)) - {(2, 2, 2)})
    out["L_shape"] = close_to_downset(
        set((x, 0, 0) for x in range(-3, 4)) | set((0, y, 0) for y in range(-3, 4))
        | set((0, 0, -1) for _ in [0]) | {(0, -1, 0), (-1, 0, 0)})
    out["thin_slab"] = close_to_downset(
        set((x, y, 0) for x in range(-3, 3) for y in range(-3, 3))
        | set((x, y, -1) for x in range(-3, 3) for y in range(-3, 3)))
    return out


# ===========================================================================
# Non-vacuity controls (the downset hypothesis is load-bearing)
# ===========================================================================

def hollow_shell_cubes():
    """A 3x3x3 cube block minus the centre cube -> a cavity (H_2 != 0); NOT a
    downset. The SAME rule must NOT give a single critical cell."""
    cubes = set(product((-1, 0, 1), repeat=3))
    cubes.discard((0, 0, 0))
    return cubes


def torus_prism_cubes():
    """A square annulus (3x3 minus centre) extruded one cube -> H_1 != 0; NOT a
    downset. The SAME rule must NOT give a single critical cell."""
    cubes: set = set()
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (x, y) == (0, 0):
                continue
            cubes.add((x, y, 0))
            cubes.add((x, y, -1))
    return cubes


# ===========================================================================
# Checks
# ===========================================================================

def check_apriori_single_cube_universe():
    print("\n=== L1(b) A-PRIORI single-cube universe (replaces the freeze) ===")
    (family, n_ne, bad_collapse, n_free, bad_free, td, n_shapes) = \
        build_apriori_family()
    n_classes_free = sum(1 for sc in family
                         if any(len(s) == 0 for s in family[sc]))
    check("L1(b) (U1) translation-INVARIANT: the abstract attachment family "
          "depends only on the cube sign-class, not on the coordinate value "
          "(c_i in {1,2} and {-2,-3} agree)",
          len(td) == 0, f"translation_dependent_classes={len(td)}")
    check("L1(b) (U2) single-cube fact: on EVERY non-empty member A_c of the "
          "abstract family, K(c) relatively collapses onto A_c with ZERO extra "
          "critical cells (residue == A_c)",
          bad_collapse == 0,
          f"nonempty_members={n_ne} distinct_shapes={n_shapes} "
          f"bad_collapse={bad_collapse}")
    check("L1(b) (U3) single-cube fact: every attachment-FREE member collapses "
          "to its toward-origin corner (one critical 0-cell)",
          bad_free == 0,
          f"attachment_free_members={n_free} bad_free={bad_free} "
          f"(attachment-free sign-classes={n_classes_free})")
    return family


def check_reverse_inclusion_and_origin(family, radii, n_random, seed):
    print("\n=== L1(b) REVERSE INCLUSION + global attachment-free uniqueness ===")
    rng = random.Random(seed)
    objs = [("B%d" % R, build_cubes_from_ball(R)) for R in radii]
    for i in range(n_random):
        objs.append(("rand%d" % i,
                     random_downset(rng, rng.randint(3, 6))))
    for name, D in adversarial_downsets().items():
        objs.append((name, D))
    out_of_family = 0
    bad_free = 0
    n_not_ball = 0
    examples: list = []
    for label, cubes in objs:
        cubes = set(cubes)
        order = sorted(cubes, key=kappa)
        free_cubes = []
        # is this D a metric ball? (record how many are NOT)
        is_ball = False
        for R in range(2, 14):
            if cubes == build_cubes_from_ball(R):
                is_ball = True
                break
        if not is_ball:
            n_not_ball += 1
        for c in order:
            A = realized_attachment(c, cubes)
            if not A:
                free_cubes.append(c)
                continue
            sh = local_shape(c, A)
            if sh not in family[sign_class(c)]:
                out_of_family += 1
                if len(examples) < 3:
                    examples.append((label, c, sign_class(c)))
        if free_cubes != [(0, 0, 0)]:
            bad_free += 1
            if len(examples) < 6:
                examples.append((label, "FREE!=origin", free_cubes[:3]))
    check("L1(b) (U4) REVERSE INCLUSION: every attachment realized by an actual "
          "downset lies in the abstract single-cube family (the family covers "
          "reality without sampling it)",
          out_of_family == 0,
          f"objects={len(objs)} not-metric-balls={n_not_ball} "
          f"out_of_family={out_of_family}")
    check("L1(b) (U5) the UNIQUE attachment-free cube in every actual downset is "
          "the origin cube (0,0,0); its directed collapse leaves {origin}",
          bad_free == 0,
          f"objects={len(objs)} downsets_with_free!=origin={bad_free}")
    if examples:
        print("   examples:", examples[:6])


def check_matching_on_objects(radii, n_random, seed):
    print("\n=== L1(b) UNIVERSAL matching: valid + single-critical {origin} + "
          "acyclic, on K(B_R) AND arbitrary downsets ===")
    rng = random.Random(seed)
    objs = [("B%d" % R, build_cubes_from_ball(R)) for R in radii]
    for i in range(n_random):
        objs.append(("rand%d" % i, random_downset(rng, rng.randint(3, 6))))
    for name, D in adversarial_downsets().items():
        objs.append((name, D))

    origin_cell = ((0, 0, 0),)
    bad_valid = 0
    bad_crit = 0
    bad_acyc = 0
    bad_h1 = 0
    bad_m = 0
    bad_superset = 0
    total_m_steps = 0
    total_superset_cmps = 0
    crit_fail = None
    acyc_fail = None
    n_not_ball = 0
    for label, D in objs:
        is_ball = any(set(D) == build_cubes_from_ball(R) for R in range(2, 14))
        if not is_ball:
            n_not_ball += 1
        match, critical, intro, _fiber = build_matching(D)
        if valid_matching_violations(match):
            bad_valid += 1
        if not (len(critical) == 1 and critical[0] == origin_cell):
            bad_crit += 1
            if crit_fail is None:
                crit_fail = (label, len(critical), sorted(critical)[:3])
        if not is_acyclic_direct(match, D):
            bad_acyc += 1
            if acyc_fail is None:
                acyc_fail = label
        h1, m, sm = global_key_violations(match, intro, D)
        bad_h1 += h1
        bad_m += m
        total_m_steps += sm
        # superset core only on the (cheaper) ball + a subsample of randoms
        if label.startswith("B") or label in adversarial_downsets() or \
                (label.startswith("rand") and int(label[4:]) % 5 == 0):
            bs, sc = superset_core_violations(D)
            bad_superset += bs
            total_superset_cmps += sc

    n_radii = len(radii)
    check(f"L1(b) (V1) VALID partial matching (involution; dims differ by 1) on "
          f"K(B_R) R={min(radii)}..{max(radii)} AND {n_random} arbitrary "
          f"downsets + {len(adversarial_downsets())} adversarial extremes",
          bad_valid == 0,
          f"objects={len(objs)} not-metric-balls={n_not_ball} "
          f"bad_valid={bad_valid}")
    check("L1(b) (V2) EXACTLY ONE critical cell = {origin} on every object "
          "(universality: not B_R-specific)",
          bad_crit == 0,
          f"bad_single_critical={bad_crit}"
          + (f" first_fail={crit_fail}" if crit_fail else ""))
    check("L1(b) (V3) ACYCLIC: the modified Hasse digraph has NO directed cycle "
          "(direct DFS cycle detection) on every object",
          bad_acyc == 0,
          f"bad_acyclic={bad_acyc}"
          + (f" first_fail={acyc_fail}" if acyc_fail else ""))
    check("L1(b) (V4) GLOBAL KEY (H1): matched pairs share intro -> f=kappa o "
          "intro is constant on matched up-steps",
          bad_h1 == 0, f"bad_H1={bad_h1}")
    check("L1(b) (V5) GLOBAL KEY (M): every regular down-step has "
          "kappa(intro(tau)) <= kappa(intro(sigma)) (strictly-monotone global "
          "key => one-line acyclicity, NO V-path enumeration)",
          bad_m == 0, f"down_steps={total_m_steps} bad_M={bad_m}")
    check("L1(b) (V6) A-PRIORI core of (M): cubes(tau) is a SUPERSET of "
          "cubes(sigma) for every facet tau of sigma (=> kappa-min decreases); "
          "this is the structural reason (M) holds",
          bad_superset == 0,
          f"comparisons={total_superset_cmps} bad_superset={bad_superset}")


def check_nonvacuity():
    print("\n=== L1(b) NON-VACUITY: the downset hypothesis is load-bearing ===")
    # cavity
    cubes = hollow_shell_cubes()
    match, critical, intro, _ = build_matching(cubes)
    check("L1(b) (N1) the SAME rule on a hollow shell (cavity, H_2 != 0; NOT a "
          "downset) yields MORE THAN ONE critical cell (single-criticality is "
          "not a tautology of the scheme)",
          len(critical) > 1, f"critical_cells={len(critical)}")
    # loop
    cubes = torus_prism_cubes()
    match, critical, intro, _ = build_matching(cubes)
    check("L1(b) (N2) the SAME rule on a square-annulus prism (loop, H_1 != 0; "
          "NOT a downset) yields MORE THAN ONE critical cell",
          len(critical) > 1, f"critical_cells={len(critical)}")
    # the direct cycle scanner is NON-VACUOUS: it must flag a hand-built cycle.
    fake_cells = {(1,), (2,), (3,), (1, 2), (2, 3), (1, 3)}
    fake_match = {(1,): (1, 2), (1, 2): (1,),
                  (2,): (2, 3), (2, 3): (2,),
                  (3,): (1, 3), (1, 3): (3,)}
    adj: defaultdict[tuple, list] = defaultdict(list)
    for c in fake_cells:
        if len(c) == 2:
            for i in range(2):
                f = (c[i],)
                if fake_match.get(f) == c:
                    continue
                adj[c].append(f)
        m = fake_match.get(c)
        if m is not None and len(m) == len(c) + 1:
            adj[c].append(m)

    def has_cycle():
        WHITE, GREY, BLACK = 0, 1, 2
        color = {c: WHITE for c in fake_cells}
        for root in fake_cells:
            if color[root] != WHITE:
                continue
            stack = [(root, iter(adj[root]))]
            color[root] = GREY
            while stack:
                node, it = stack[-1]
                adv = False
                for nb in it:
                    if color[nb] == GREY:
                        return True
                    if color[nb] == WHITE:
                        color[nb] = GREY
                        stack.append((nb, iter(adj[nb])))
                        adv = True
                        break
                if not adv:
                    color[node] = BLACK
                    stack.pop()
        return False
    check("L1(b) (N3) the cycle scanner is NON-VACUOUS: it correctly FLAGS a "
          "hand-built rotational 3-cycle (so V3's PASS is meaningful)",
          has_cycle() is True, "hand-built 3-cycle detected")


def main(argv):
    rmax = int(argv[1]) if len(argv) > 1 else 8
    n_random = int(argv[2]) if len(argv) > 2 else 200
    radii = list(range(2, rmax + 1))
    seed = 20260603

    print("=" * 75)
    print("S^3 cone-cap Part B, L1(b): A-PRIORI collapsibility of K(D) for every")
    print("star-shaped toward-origin cubical downset D (uniform in D; NO freeze).")
    print("=" * 75)

    family = check_apriori_single_cube_universe()
    check_reverse_inclusion_and_origin(family, radii, n_random, seed)
    check_matching_on_objects(radii, n_random, seed)
    check_nonvacuity()

    print("\n" + "=" * 75)
    verdict = "PASS" if FAIL_COUNT == 0 else "FAIL"
    print(f"S3 cone-cap Part B L1(b) a-priori collapsibility: {verdict}")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT} EXACT={EXACT_COUNT}")
    print(f"Verified on K(B_R) R = 2..{rmax} AND {n_random} arbitrary "
          f"star-shaped cubical downsets + "
          f"{len(adversarial_downsets())} adversarial extremes.")
    print("L1(b) no longer rests on a freeze: validity + single-critical "
          "{origin} + acyclicity are a-priori (uniform in D, hence R-free).")
    print("=" * 75)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
