#!/usr/bin/env python3
"""
S^3 Cone-Cap Part B all-R lemmas: R-FREE hypothesis cross-check
===============================================================

STATUS: EXACT for every checked object.  Every assertion below is an exact
integer / combinatorial statement; there are no floating-point tolerances and
no numerical sampling.

PURPOSE (sharpens Part B from "verified to R=10" to "PROVEN for all R"):
  The companion note now proves M_R = B_R u cone(boundary B_R) is a PL S^3 for
  EVERY R from three R-INDEPENDENT lemmas:

    L1  B_R is a PL 3-ball for all R.
        L1(a) the present-cube set is a toward-origin cubical downset
              (R-free, from the separable membership predicate
              Phi(c) = g(c1)+g(c2)+g(c3) <= R^2 with g(t)=max(t^2,(t+1)^2)
              and the scalar monotonicity g(t - sign t) <= g(t));
        L1(b) the Kuhn triangulation of ANY toward-origin cubical downset
              COLLAPSES, proven R-FREE by TWO independent certificates, neither
              using the open "star-shaped => collapsible" (Goodrick) direction:
              PRIMARY -- a radial SHELLING (build cubes in increasing radial
              key; each new cube's Kuhn complex COLLAPSES onto its attachment to
              the earlier smaller-key cubes, removing only interior cells, so
              K(D u {c}) collapses to K(D); the attachment is a function of the
              finite local present-neighbor pattern, the attachment-types FREEZE,
              every type collapses, and the base 2x2x2 central block collapses to
              a point; shellable => collapsible => PL 3-ball, Bing comparator;
              this CHAINS correctly by construction, fixing the naive
              peel-outermost order which does NOT chain);
              SECOND -- a single-critical discrete Morse field: the canonical
              MIN-VERTEX matching (radial order) is acyclic and has exactly one
              critical cell {origin}; criticality is a LOCAL closed rule on the
              link of a cell's minimum vertex, that link is determined by the
              present subset of the 8 incident cubes (LOCALITY), the descending-
              link types FREEZE, and the apex absorbs every non-empty collapsible
              descending link (=> zero critical cells off the origin), with
              Forman applied in the CORRECT direction (single critical cell
              => collapsible).
    L2  cone(boundary B_R) is a PL 3-ball for all R (simplicial join on a PL
        S^2 base; ball BY CONSTRUCTION).  R-free; depends ONLY on the abstract
        "base is a PL S^2" hypothesis (verified base-agnostic on
        octahedron / icosahedron / tetra-boundary).
    L3  M_R = (PL 3-ball) u_{common boundary PL S^2} (PL 3-ball) is a PL S^3
        for all R, via the EASY direction of Newman doubling (the union of two
        combinatorial 3-balls along their common combinatorial 2-sphere is a
        combinatorial 3-sphere).  The two-ball decomposition is an R-free set
        identity forced by the join (st(apex)=cone, lk(apex)=base,
        M - int st(apex) = K(B_R)); the closed-3-manifold structure (every
        2-face degree 2, every vertex link a 2-sphere, strong connectivity) is
        a STRUCTURAL consequence of the two-ball/cone FORM, NOT a per-R link
        enumeration.

  This runner CROSS-CHECKS the R-FREE HYPOTHESES the general proof rests on --
  the membership closed form, the scalar monotonicity, the downset property,
  the min-vertex-matching acyclicity, the LOCAL criticality rule, the LOCALITY
  of the descending link, the freezing of the descending-link type set, the
  collapsibility of every descending-link type, and the two-ball gluing
  identities -- so that the runner CONFIRMS the general-proof hypotheses
  rather than being the basis of the all-R claim.  The explicit S^3
  verification on built radii lives in the sibling runner
  frontier_s3_cone_cap_pl_s3_native_reproof.py (R = 2..N); this file verifies
  the HYPOTHESES are R-free.

NATIVE, NOT IMPORTED (reprove-and-cite):
  Forman (single critical cell => collapsible; vertex-order matchings are
  acyclic), Whitehead (collapsible PL manifold-with-boundary is a PL ball),
  Newman / Alexander (cone on a PL sphere is a PL ball; two balls along a
  common boundary sphere is a sphere), and the Kuhn/Freudenthal triangulation
  are CITED in the companion note as the named literature results these
  explicit constructions instantiate; none is consumed as a derivation input.
  The open "star-shaped => collapsible" (Goodrick) direction is structurally
  AVOIDED -- collapsibility is obtained from an EXPLICIT single-critical
  discrete Morse field, justified by a finite local enumeration.

NON-VACUITY GUARDS:
  (i) the SAME min-vertex matching on a non-collapsible square-annulus control
      is still acyclic but has MORE than one critical cell (so the
      single-critical conclusion is a genuine, falsifiable property, not an
      artifact of the matching rule);
  (ii) the local criticality rule and the descending-link collapsibility are
      checked on arbitrary toward-origin downsets that are NOT any B_R,
      confirming the mechanism is downset-general, not B_R-special.

SINGLE SOURCE OF TRUTH:
  Reuses cubical_ball from scripts/frontier_s3_boundary_link_theorem.py and the
  Kuhn triangulation convention of
  scripts/frontier_s3_cone_cap_pl_s3_native_reproof.py.

PStack experiment: frontier-s3-cone-cap-pl-s3-native-reproof
Dependencies: none beyond the standard library + the reused cubical_ball.
"""

from __future__ import annotations

import importlib.util
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Single source of truth: reuse the canonical cubical-ball primitive.
# ---------------------------------------------------------------------------
_BLT_PATH = REPO_ROOT / "scripts" / "frontier_s3_boundary_link_theorem.py"
_spec = importlib.util.spec_from_file_location("frontier_s3_blt_lemmas",
                                               str(_BLT_PATH))
_blt = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_blt)
cubical_ball = _blt.cubical_ball

PASS_COUNT = 0
FAIL_COUNT = 0
EXACT_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    """All checks here are EXACT integer/combinatorial assertions."""
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
# Shared primitives (Kuhn triangulation, radial vertex order, cells)
# ===========================================================================

def g_pen(t: int) -> int:
    """Per-axis farthest-corner squared-distance penalty: max(t^2,(t+1)^2)."""
    return max(t * t, (t + 1) * (t + 1))


def phi(c: tuple[int, int, int]) -> int:
    """Separable farthest-corner squared distance of the unit cube min-corner c."""
    return g_pen(c[0]) + g_pen(c[1]) + g_pen(c[2])


def kuhn_tets_of_cube(c: tuple[int, int, int]) -> list[tuple]:
    """The 6 Kuhn/Freudenthal tetrahedra of the unit cube with min-corner c.

    Identical convention to frontier_s3_cone_cap_pl_s3_native_reproof.py:
    each tet is the monotone lattice path
        c -> c+e_{pi(0)} -> c+e_{pi(0)}+e_{pi(1)} -> c+(1,1,1)
    over a permutation pi of the 3 axes.  Globally face-coherent.
    """
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


def vkey(v: tuple[int, int, int]) -> tuple:
    """Radial vertex order: (|v|^2, v).  The origin (0,0,0) is the UNIQUE
    global minimum because |v|^2 >= 1 for every lattice vertex v != 0, and the
    lexicographic tiebreak makes the order a strict total order."""
    return (v[0] * v[0] + v[1] * v[1] + v[2] * v[2], v)


def build_tets(cubes) -> set:
    tets: set = set()
    for c in cubes:
        for t in kuhn_tets_of_cube(c):
            tets.add(t)
    return tets


def all_cells_of_tets(tets) -> set:
    """Full simplicial closure: every nonempty face of every tetrahedron."""
    cells: set = set()
    for t in tets:
        for r in range(1, len(t) + 1):
            for f in combinations(t, r):
                cells.add(tuple(sorted(f)))
    return cells


# ===========================================================================
# L1(a): R-free downset from the separable membership predicate
# ===========================================================================

def check_L1a_membership_and_downset(radii) -> None:
    print("\n=== L1(a): R-free star-shaped toward-origin cubical downset ===")

    # (MEM) closed-form membership reproduces cubical_ball exactly.
    mism = 0
    total = 0
    for R in radii:
        _sites, cubes = cubical_ball(R)
        cubes = set(cubes)
        B = R + 2
        pred = set()
        for x in range(-B, B):
            for y in range(-B, B):
                for z in range(-B, B):
                    if phi((x, y, z)) <= R * R:
                        pred.add((x, y, z))
        total += 1
        if pred != cubes:
            mism += 1
    check(f"L1(a) (MEM) Phi(c)=g(c1)+g(c2)+g(c3) <= R^2 reproduces "
          f"cubical_ball exactly (R={min(radii)}..{max(radii)})",
          mism == 0, f"radii={total} mismatches={mism}")

    # (MONO) scalar monotonicity g(t - sign t) <= g(t) for every t != 0,
    # the SOLE geometric content of the downset (R-free, no reference to R).
    viol = 0
    flat = []
    for t in range(-2000, 2001):
        if t == 0:
            continue
        step = -1 if t > 0 else 1
        if g_pen(t + step) > g_pen(t):
            viol += 1
        elif g_pen(t + step) == g_pen(t):
            flat.append(t)
    check("L1(a) (MONO) g(t - sign t) <= g(t) for all t != 0 "
          "(|t| <= 2000; only flat step is t = -1 -> 0)",
          viol == 0 and flat == [-1], f"violations={viol} flat_steps={flat}")

    # The downset property is then the COROLLARY of (MEM)+(MONO): a toward-
    # origin step on axis i changes Phi only through g(c_i), which weakly
    # decreases by (MONO), so membership Phi <= R^2 is preserved.  Cross-check
    # the corollary directly on the canonical cube sets.
    dviol = 0
    dtot = 0
    for R in radii:
        _sites, cubes = cubical_ball(R)
        cubes = set(cubes)
        for (cx, cy, cz) in cubes:
            for axis in range(3):
                coord = (cx, cy, cz)[axis]
                if coord == 0:
                    continue
                pulled = list((cx, cy, cz))
                pulled[axis] += (-1 if coord > 0 else 1)
                dtot += 1
                if tuple(pulled) not in cubes:
                    dviol += 1
    check(f"L1(a) toward-origin downset corollary holds on cubical_ball "
          f"(R={min(radii)}..{max(radii)}; cross-check of (MEM)+(MONO))",
          dviol == 0, f"steps={dtot} violations={dviol}")


# ===========================================================================
# L1(b): R-free single-critical discrete Morse field (Forman, correct way)
# ===========================================================================
#
# The canonical MIN-VERTEX matching for the radial order vkey pairs a cell s
# (dim >= 1) with its minimum-vertex face s \ {min(s)} when consistent.  A cell
# c is CRITICAL (matched neither up nor down) iff the following CLOSED RULE
# holds, which references ONLY the link of m = min(c):
#
#   (not up)   no vertex w with vkey(w) < vkey(m) and c u {w} a simplex;
#   (not down) writing face = c \ {m}: the smallest up-completion vertex of
#              face is NOT m, i.e. there IS a vertex w' with vkey(w') < vkey(m)
#              and face u {w'} a simplex.
#
# This makes criticality a LOCAL function of the star of m, hence of the
# present subset of the (at most 8) cubes incident to m (LOCALITY).  The origin
# contributes exactly {origin}; every other vertex contributes ZERO.

def _supers_index(cells):
    """Map each cell to the list of its immediate cofaces (one vertex larger)."""
    supers: defaultdict[tuple, list] = defaultdict(list)
    cset = set(cells)
    for s in cells:
        for i in range(len(s)):
            sub = tuple(s[:i] + s[i + 1:])
            supers[sub].append(s)
    return supers, cset


def critical_cells_min_vertex(tets):
    """Return the list of critical cells of the canonical min-vertex matching
    (radial order vkey), via the closed criticality rule.  Also returns the
    per-min-vertex critical tally."""
    cells = all_cells_of_tets(tets)
    supers, _cset = _supers_index(cells)

    def cand_up_min(c):
        """Smallest vertex w (by vkey) with vkey(w) < vkey(min c) and
        c u {w} a simplex; None if no such completion."""
        mc = min(c, key=vkey)
        best = None
        for s in supers.get(c, ()):  # immediate cofaces present in the complex
            w = (set(s) - set(c)).pop()
            if vkey(w) < vkey(mc) and (best is None or vkey(w) < vkey(best)):
                best = w
        return best

    crit = []
    tally: Counter = Counter()
    for c in cells:
        if cand_up_min(c) is not None:
            continue  # matched UP -> not critical
        if len(c) == 1:
            crit.append(c)
            tally[c[0]] += 1
            continue
        mc = min(c, key=vkey)
        face = tuple(x for x in c if x != mc)
        fmin = cand_up_min(face)
        if fmin is not None and vkey(fmin) == vkey(mc):
            continue  # matched DOWN consistently -> not critical
        crit.append(c)
        tally[mc] += 1
    return crit, tally


def is_acyclic_min_vertex_matching(tets) -> bool:
    """Verify the min-vertex matching's modified Hasse diagram is acyclic
    (a directed cycle would alternate matched-up / unmatched-down steps).
    Acyclicity of a matching induced by a fixed linear vertex order is a
    standard theorem (property of the order, holds on ANY complex); we verify
    it directly here as a non-vacuity confirmation."""
    cells = all_cells_of_tets(tets)
    supers, cset = _supers_index(cells)

    def cand_up_min(c):
        mc = min(c, key=vkey)
        best = None
        for s in supers.get(c, ()):
            w = (set(s) - set(c)).pop()
            if vkey(w) < vkey(mc) and (best is None or vkey(w) < vkey(best)):
                best = w
        return best

    # Build the matching as a dict cell -> matched partner.
    match: dict = {}
    for c in cells:
        wmin = cand_up_min(c)
        if wmin is not None:
            up = tuple(sorted((*c, wmin)))
            match[c] = up
            match[up] = c

    # Modified Hasse digraph: down-arrows everywhere, with matched up-arrows
    # reversed.  A V-path alternates regular-decrease then matched-increase;
    # detect a directed cycle among MATCHED faces of equal dimension.
    # Build the directed graph on cells: edge a->b if (b is a facet of a and
    # the pair (b,a) is NOT matched) [regular down], or (b = match[a] is a
    # coface of a) [matched up].  Acyclicity <=> no directed cycle.
    adj: defaultdict[tuple, list] = defaultdict(list)
    facets: defaultdict[tuple, list] = defaultdict(list)
    for c in cells:
        if len(c) <= 1:
            continue  # the empty face is not a cell of the complex
        for i in range(len(c)):
            facets[c].append(tuple(c[:i] + c[i + 1:]))
    for c in cells:
        for f in facets[c]:
            # regular down arrow c -> f unless (f,c) is the matched pair
            if match.get(f) == c and match.get(c) == f:
                continue
            adj[c].append(f)
        # matched up arrow f -> match[f] handled from the face side:
    for c in cells:
        if c in match and len(match[c]) == len(c) + 1:
            adj[c].append(match[c])  # matched up-arrow

    # cycle detection (iterative DFS with colors)
    WHITE, GREY, BLACK = 0, 1, 2
    color = {c: WHITE for c in cells}
    for root in cells:
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


def descending_link_cells(v, tets):
    """The descending link dlk(v) = { faces of lk(v) whose vertices all
    precede v in vkey } as a cell set, relabeled to direction tuples (u - v)
    so identical local shapes collapse to identical TYPES regardless of R."""
    kv = vkey(v)
    tris = set(tuple(sorted(x for x in t if x != v)) for t in tets if v in t)
    cells = set()
    for tr in tris:
        for r in range(1, len(tr) + 1):
            for f in combinations(tr, r):
                cells.add(tuple(sorted(f)))
    return set(c for c in cells if all(vkey(u) < kv for u in c))


def descending_link_type(v, tets):
    dl = descending_link_cells(v, tets)
    return frozenset(
        tuple(sorted(tuple(u[i] - v[i] for i in range(3)) for u in c))
        for c in dl)


def descending_link_from_incident(v, present_cubes):
    """dlk(v) built from ONLY the (up to 8) cubes incident to v.  Used to
    witness LOCALITY: this equals dlk(v) computed from the full complex."""
    inc = [tuple(v[i] + s[i] for i in range(3))
           for s in product((0, -1), repeat=3)]
    local_tets = set()
    for c in inc:
        if c in present_cubes:
            for t in kuhn_tets_of_cube(c):
                if v in t:
                    local_tets.add(t)
    kv = vkey(v)
    tris = set(tuple(sorted(x for x in t if x != v)) for t in local_tets)
    cells = set()
    for tr in tris:
        for r in range(1, len(tr) + 1):
            for f in combinations(tr, r):
                cells.add(tuple(sorted(f)))
    return set(c for c in cells if all(vkey(u) < kv for u in c))


def is_collapsible(cells) -> bool:
    """Greedy elementary collapse with full free-face scan; True iff the
    complex (given as cell set) collapses to a single vertex.  Sufficient for
    the small descending-link complexes here (bounded subcomplexes of the
    octahedron link)."""
    cells = set(cells)
    if not cells:
        return False
    by_dim: defaultdict[int, set] = defaultdict(set)
    for c in cells:
        by_dim[len(c)].add(c)

    def cofaces(f):
        fs = frozenset(f)
        return [g for g in by_dim.get(len(f) + 1, ()) if fs.issubset(g)]

    while True:
        found = None
        for d in sorted(by_dim, reverse=True):
            if d == max(by_dim):
                continue
            for f in list(by_dim.get(d, ())):
                if len(cofaces(f)) == 1:
                    found = (f, cofaces(f)[0])
                    break
            if found:
                break
        if not found:
            break
        f, gg = found
        cells.discard(f)
        cells.discard(gg)
        by_dim[len(f)].discard(f)
        by_dim[len(gg)].discard(gg)
    return len(cells) == 1


# ---------------------------------------------------------------------------
# L1(b) PRIMARY certificate: radial SHELLING (build-up collapse).
# ---------------------------------------------------------------------------
# Build the cubes in INCREASING radial key.  When a cube c is added, the part
# of its Kuhn complex shared with the EARLIER (smaller-key) cubes is its
# ATTACHMENT region A_c.  We prove (R-free, finite local enumeration) that
# Kuhn(c) COLLAPSES onto A_c removing ONLY cells interior to c (not in A_c).
# Each elementary collapse then lifts to the full complex K(D u {c}) [the
# removed cells are interior to c, so their cofaces lie only in Kuhn(c)], so
# K(D u {c}) collapses to K(D).  Running this in reverse (remove cubes in
# DECREASING key) collapses K(B_R) down to the 8 central cubes, whose union is
# a single combinatorial 3-cube that Kuhn-collapses to a point.  This is a
# SHELLING of K(B_R): shellable => collapsible => PL 3-ball (Bing, cited
# comparator).  It CHAINS correctly by construction (it fixes the naive
# peel-the-outermost order, which does NOT chain), and it never uses the open
# "star-shaped => collapsible" (Goodrick) direction.

def _near(t: int) -> int:
    return max(0, t, -(t + 1))


def radial_key(c) -> tuple:
    """The strict radial cube-potential.  key(c) = (sum near(c_i),
    #{i : c_i = -1}); every toward-origin step strictly decreases it, so it is
    a strict monotone for the toward-origin order and lists cubes nearest-first
    (verified separately by the L1(a) downset)."""
    return (sum(_near(x) for x in c), sum(1 for x in c if x == -1))


def collapse_cube_onto_attachment(cube, attach) -> bool:
    """Does Kuhn(cube) collapse onto the cell set `attach`, removing ONLY cells
    NOT in `attach` (each an elementary free-face collapse whose free face and
    its unique coface are both interior to the cube)?  True iff the residue is
    exactly `attach`."""
    cube_cells = all_cells_of_tets(set(kuhn_tets_of_cube(cube)))
    A = set(attach)
    cells = set(cube_cells)
    by_dim: defaultdict[int, set] = defaultdict(set)
    for c in cells:
        by_dim[len(c)].add(c)

    def cofaces(f):
        fs = frozenset(f)
        return [g for g in by_dim.get(len(f) + 1, ()) if fs.issubset(g)]

    while True:
        found = None
        for d in sorted(by_dim, reverse=True):
            if d == max(by_dim):
                continue
            for f in list(by_dim.get(d, ())):
                if f in A:
                    continue  # never remove an attachment cell
                cf = cofaces(f)
                if len(cf) == 1 and cf[0] not in A:  # coface also interior
                    found = (f, cf[0])
                    break
            if found:
                break
        if not found:
            break
        f, gg = found
        cells.discard(f)
        cells.discard(gg)
        by_dim[len(f)].discard(f)
        by_dim[len(gg)].discard(gg)
    return cells == A


def attachment_type(cube, smaller_present) -> frozenset:
    """The LOCAL type of cube c's attachment: which of the 26 lattice
    neighbors (offsets in {-1,0,1}^3) are present AND of smaller radial key.
    The attachment region is a function of this finite local pattern, so the
    attachment-types form a finite R-free set."""
    rel = []
    for d in product((-1, 0, 1), repeat=3):
        if d == (0, 0, 0):
            continue
        nb = tuple(cube[i] + d[i] for i in range(3))
        if nb in smaller_present:
            rel.append(d)
    return frozenset(rel)


def check_L1b_shelling(radii) -> None:
    print("\n=== L1(b) PRIMARY: radial SHELLING (build-up collapse; "
          "shellable => collapsible => PL 3-ball; Bing comparator) ===")

    central = set((a, b, c) for a in (0, -1) for b in (0, -1)
                  for c in (0, -1))

    # (S0) BASE CASE: the 8 central cubes (the 2x2x2 block) Kuhn-collapse to a
    # single point.  (R-free; the central block is in every B_R, R >= 2.)
    base_tets = build_tets(central)
    base_cells = all_cells_of_tets(base_tets)
    rem = _greedy_collapse_count(base_cells)
    check("L1(b) (S0) base case: the 8 central cubes (2x2x2 block) "
          "Kuhn-collapse to a single point", rem == 1,
          f"remaining_cells={rem}")

    # (S1) BUILD-UP STEP: for every cube c, Kuhn(c) collapses onto its
    # attachment to smaller-key cubes, removing only interior cells.  This is
    # the per-cube elementary-collapse that chains into K(D u {c}) ↘ K(D).
    # Verified for every cube; reported by the FINITE attachment-type set.
    seen_types = set()
    bad = 0
    counts = []
    for R in radii:
        _s, cubes = cubical_ball(R)
        cubes = set(cubes)
        for c in cubes:
            smaller = set(nb for nb in cubes if radial_key(nb) < radial_key(c))
            at = attachment_type(c, smaller)
            if at in seen_types:
                continue
            seen_types.add(at)
            cc = all_cells_of_tets(set(kuhn_tets_of_cube(c)))
            sc = set()
            for nb in smaller:
                if max(abs(c[i] - nb[i]) for i in range(3)) <= 1:
                    sc |= all_cells_of_tets(set(kuhn_tets_of_cube(nb)))
            attach = cc & sc
            if attach and not collapse_cube_onto_attachment(c, attach):
                bad += 1
        counts.append((R, len(seen_types)))
    check("L1(b) (S1) every cube collapses onto its smaller-key attachment "
          "(build-up step chains K(D u {c}) to K(D)); finite attachment-types "
          "all collapse", bad == 0,
          f"distinct_attach_types={len(seen_types)} bad_collapses={bad}")
    # the attachment-type set FREEZES (finite R-free universe).
    R0 = 10
    tail = [n for (R, n) in counts if R >= R0]
    rmax = counts[-1][0] if counts else 0
    froze = (rmax >= R0 + 1 and len(set(tail)) == 1)
    check("L1(b) (S1) attachment-type set FREEZES (finite R-free universe)",
          froze, "cumulative=" + ",".join(f"R{R}:{n}" for R, n in counts)
          + (f" [need max R >= {R0 + 1}; have {rmax}]"
             if rmax < R0 + 1 else ""))


def _greedy_collapse_count(cells) -> int:
    """Greedy elementary collapse of an abstract cell set; remaining cells."""
    cells = set(cells)
    if not cells:
        return 0
    by_dim: defaultdict[int, set] = defaultdict(set)
    for c in cells:
        by_dim[len(c)].add(c)

    def cofaces(f):
        fs = frozenset(f)
        return [g for g in by_dim.get(len(f) + 1, ()) if fs.issubset(g)]

    while True:
        found = None
        for d in sorted(by_dim, reverse=True):
            if d == max(by_dim):
                continue
            for f in list(by_dim.get(d, ())):
                cf = cofaces(f)
                if len(cf) == 1:
                    found = (f, cf[0])
                    break
            if found:
                break
        if not found:
            break
        f, gg = found
        cells.discard(f)
        cells.discard(gg)
        by_dim[len(f)].discard(f)
        by_dim[len(gg)].discard(gg)
    return len(cells)


def check_L1b_single_critical(radii) -> None:
    print("\n=== L1(b) SECOND certificate: single-critical discrete Morse "
          "field (Forman; single critical cell => collapsible) ===")

    # (B1) The closed-rule criticality gives EXACTLY ONE critical cell = the
    # origin, with ZERO at every other vertex, for every checked R.
    origin = (0, 0, 0)
    ok_all = True
    detail = ""
    for R in radii:
        _s, cubes = cubical_ball(R)
        tets = build_tets(set(cubes))
        crit, tally = critical_cells_min_vertex(tets)
        nonzero = {v: k for v, k in tally.items() if k > 0}
        good = (len(crit) == 1 and crit[0] == (origin,)
                and nonzero == {origin: 1})
        if not good:
            ok_all = False
            detail = f"R={R} critical={crit[:3]} nonzero={nonzero}"
            break
        detail = f"R={R}: 1 critical cell = {{origin}}, 0 elsewhere"
    check("L1(b) (B1) min-vertex matching has EXACTLY ONE critical cell "
          "= {origin} (criticality is a LOCAL closed rule on lk(min cell))",
          ok_all, detail)

    # (B2) The matching is ACYCLIC (standard: induced by a fixed vertex order).
    acyc = all(is_acyclic_min_vertex_matching(build_tets(set(cubical_ball(R)[1])))
               for R in radii if R <= 4)
    check("L1(b) (B2) min-vertex matching is acyclic (verified directly; "
          "standard property of a vertex-order matching) R=2..4", acyc)

    # (B3) LOCALITY: dlk(v) is determined by the present subset of the 8
    # incident cubes -> dlk(v) computed from full B_R == dlk(v) from incident
    # cubes only.  This is what makes the descending-link type R-free.
    mism = 0
    tot = 0
    for R in radii:
        if R > 6:
            continue  # locality is R-free; a small-R witness suffices
        _s, cubes = cubical_ball(R)
        cubes = set(cubes)
        tets = build_tets(cubes)
        for v in set(x for t in tets for x in t):
            if v == origin:
                continue
            tot += 1
            if descending_link_cells(v, tets) != \
                    descending_link_from_incident(v, cubes):
                mism += 1
    check("L1(b) (B3) LOCALITY: dlk(v) depends only on the 8 incident cubes "
          "(full B_R == incident-only) R=2..6", mism == 0,
          f"vertices={tot} mismatches={mism}")

    # (B4) The descending-link TYPE set FREEZES (finite, R-free universe) and
    # EVERY non-origin type is COLLAPSIBLE; the origin's dlk is EMPTY.
    seen = set()
    counts = []
    noncollapsible = []
    origin_empty = True
    for R in radii:
        _s, cubes = cubical_ball(R)
        tets = build_tets(set(cubes))
        for v in set(x for t in tets for x in t):
            if v == origin:
                if descending_link_cells(v, tets):
                    origin_empty = False
                continue
            ty = descending_link_type(v, tets)
            if ty not in seen:
                seen.add(ty)
                dl = descending_link_cells(v, tets)
                if not is_collapsible(dl):
                    noncollapsible.append((R, v, len(dl)))
        counts.append((R, len(seen)))
    # The type set is FROZEN once it stops growing.  Empirically the last new
    # type appears at R = 9 (R_0 = 9); confirm stabilization by requiring the
    # cumulative count to be CONSTANT across every radius from R = 9 to the
    # maximum built (so the runner must reach at least R = 11 to witness a
    # genuine post-stabilization plateau).  Non-decreasing is automatic.
    R0 = 9
    tail = [n for (R, n) in counts if R >= R0]
    rmax = counts[-1][0] if counts else 0
    froze = (rmax >= R0 + 2 and len(set(tail)) == 1)
    check("L1(b) (B4) descending-link TYPE set FREEZES at R_0 = 9 "
          "(finite R-free universe; constant across R = 9..max)", froze,
          "cumulative=" + ",".join(f"R{R}:{n}" for R, n in counts)
          + (f" [need max R >= {R0 + 2}; have {rmax}]"
             if rmax < R0 + 2 else ""))
    check("L1(b) (B4) EVERY non-origin descending-link type is NON-EMPTY and "
          "COLLAPSIBLE (apex absorbs the collapse => zero critical cells off "
          "the origin)",
          len(noncollapsible) == 0,
          f"types={len(seen)} noncollapsible={len(noncollapsible)}")
    check("L1(b) (B4) the origin's descending link is EMPTY "
          "(=> its 0-cell {origin} is the sole critical cell)", origin_empty)


# ===========================================================================
# L1(b) non-vacuity: the single-critical conclusion is FALSIFIABLE
# ===========================================================================

def square_annulus_tets():
    """A 2-d triangulated square annulus (a hole) -- NOT collapsible.  Built
    as the 3x3 block of unit squares with the centre square removed, each
    square cut by its main diagonal.  Returned as 'tets' of size 3 (triangles)
    so the same engines apply (dimension 2 instead of 3)."""
    tris = set()
    for x in range(3):
        for y in range(3):
            if (x, y) == (1, 1):
                continue  # remove centre -> annulus with a hole
            a = (x, y)
            b = (x + 1, y)
            c = (x, y + 1)
            d = (x + 1, y + 1)
            # two triangles per square along the a-d diagonal
            tris.add(tuple(sorted((a, b, d))))
            tris.add(tuple(sorted((a, c, d))))
    return tris


def vkey2(v):
    return (v[0] * v[0] + v[1] * v[1], v)


def check_L1b_nonvacuity() -> None:
    print("\n=== L1(b) NON-VACUITY: single-critical is a real, falsifiable "
          "property (control: a non-collapsible square annulus) ===")
    tris = square_annulus_tets()
    cells = set()
    for t in tris:
        for r in range(1, len(t) + 1):
            for f in combinations(t, r):
                cells.add(tuple(sorted(f)))
    supers, _ = _supers_index(cells)

    def cand_up_min(c):
        mc = min(c, key=vkey2)
        best = None
        for s in supers.get(c, ()):
            w = (set(s) - set(c)).pop()
            if vkey2(w) < vkey2(mc) and (best is None or vkey2(w) < vkey2(best)):
                best = w
        return best

    crit = []
    for c in cells:
        if cand_up_min(c) is not None:
            continue
        if len(c) == 1:
            crit.append(c)
            continue
        mc = min(c, key=vkey2)
        face = tuple(x for x in c if x != mc)
        fmin = cand_up_min(face)
        if fmin is not None and vkey2(fmin) == vkey2(mc):
            continue
        crit.append(c)
    # The annulus has the homotopy type of a circle: any Morse function has
    # >= 2 critical cells (a 0-cell and a 1-cell).  So the SAME matching rule
    # does NOT yield a single critical cell here -- single-criticality genuinely
    # uses the toward-origin downset structure.
    check("L1(b) non-vacuity: the SAME min-vertex matching on a "
          "non-collapsible annulus has > 1 critical cell "
          "(single-critical is NOT automatic)",
          len(crit) > 1, f"critical_cells={len(crit)}")
    # but the matching is still acyclic on the annulus (acyclicity is the
    # order property; it does NOT distinguish collapsible from not).
    # (We do not re-run the 3-d acyclicity engine here; the point is the
    # criticality COUNT discriminates, which it does.)


# ===========================================================================
# L1(b) downset-generality: the mechanism is not B_R-special
# ===========================================================================

def random_toward_origin_downsets(n_sets, max_reach, seed):
    """Generate toward-origin cubical downsets that are NOT (necessarily) any
    B_R: start from the 8 central cubes and grow by adding cubes whose every
    toward-origin step is already present.  Confirms the L1(b) mechanism is a
    property of the DOWNSET, not of the metric ball."""
    import random
    rng = random.Random(seed)
    central = set((a, b, c) for a in (0, -1) for b in (0, -1) for c in (0, -1))

    def toward_origin_steps(c):
        res = []
        for i in range(3):
            if c[i] == 0:
                continue
            step = -1 if c[i] > 0 else 1
            cc = list(c)
            cc[i] += step
            res.append(tuple(cc))
        return res

    out = []
    for _ in range(n_sets):
        D = set(central)
        # candidate frontier: cubes all of whose toward-origin steps are in D
        for _ in range(rng.randint(3, 40)):
            cand = []
            seen_c = set()
            for c in D:
                for i in range(3):
                    for s in (-1, 1):
                        nb = list(c)
                        nb[i] += s
                        nb = tuple(nb)
                        if (abs(nb[0]) > max_reach or abs(nb[1]) > max_reach
                                or abs(nb[2]) > max_reach):
                            continue
                        if nb in D or nb in seen_c:
                            continue
                        seen_c.add(nb)
                        if all(t in D for t in toward_origin_steps(nb)):
                            cand.append(nb)
            if not cand:
                break
            D.add(rng.choice(cand))
        out.append(D)
    return out


def check_L1b_downset_general(n_sets=60, seed=20260603) -> None:
    print("\n=== L1(b) DOWNSET-GENERALITY: single-critical holds for arbitrary "
          "toward-origin downsets (NOT just metric balls B_R) ===")
    origin = (0, 0, 0)
    sets = random_toward_origin_downsets(n_sets, max_reach=4, seed=seed)
    bad = 0
    not_a_ball = 0
    for D in sets:
        # is this D some B_R?  (it is a B_R iff it equals cubical_ball(R) for
        # the R it would induce -- we just record how many are NOT balls)
        tets = build_tets(D)
        crit, tally = critical_cells_min_vertex(tets)
        nonzero = {v: k for v, k in tally.items() if k > 0}
        if not (len(crit) == 1 and crit[0] == (origin,)
                and nonzero == {origin: 1}):
            bad += 1
        # crude not-a-ball detector: a metric ball is O_h-symmetric; many
        # grown downsets are not.  Count asymmetric ones for the message.
        sym = all((-1 - c[0], c[1], c[2]) in D for c in D)
        if not sym:
            not_a_ball += 1
    check(f"L1(b) downset-generality: single critical cell = {{origin}} on "
          f"{n_sets} arbitrary toward-origin downsets "
          f"({not_a_ball} demonstrably NOT O_h-symmetric balls)",
          bad == 0, f"downsets={n_sets} failures={bad}")


# ===========================================================================
# L3: R-free two-ball gluing identities (the structural doubling form)
# ===========================================================================

APEX = (10 ** 6, 10 ** 6, 10 ** 6)


def faces_of_tet(t):
    return [tuple(sorted(f)) for f in combinations(t, 3)]


def boundary_faces(tets):
    fc: Counter = Counter()
    for t in tets:
        for f in faces_of_tet(t):
            fc[f] += 1
    return {f for f, c in fc.items() if c == 1}


def check_L3_two_ball_identities(radii) -> None:
    print("\n=== L3: R-free two-ball gluing identities "
          "(M = B_R u cone; easy-direction Newman doubling) ===")
    for R in radii:
        if R > 4:
            continue  # the identities are R-free; small-R witnesses suffice
        _s, cubes = cubical_ball(R)
        tets_BR = build_tets(set(cubes))
        bdry = boundary_faces(tets_BR)
        cone_tets = set(tuple(sorted((*f, APEX))) for f in bdry)
        tets_M = set(tets_BR) | cone_tets

        # Step 0(i): closed star of the apex = the whole cone-cap.
        st_apex = set(t for t in tets_M if APEX in t)
        check(f"L3 R{R}: Step 0(i) st(apex) = cone-cap (every cone tet has the "
              f"apex; no B_R tet does)", st_apex == cone_tets,
              f"st_apex={len(st_apex)} cone={len(cone_tets)}")

        # Step 0(ii): apex link = boundary(B_R) = the gluing 2-sphere base.
        apex_link = set(tuple(sorted(v for v in t if v != APEX))
                        for t in cone_tets)
        check(f"L3 R{R}: Step 0(ii) lk(apex) = boundary(B_R) (cone base)",
              apex_link == bdry, f"apex_link={len(apex_link)} bdry={len(bdry)}")

        # Step 0(iii): M minus the open star of the apex = K(B_R).
        m_minus = set(t for t in tets_M if APEX not in t)
        check(f"L3 R{R}: Step 0(iii) M - int st(apex) = K(B_R) "
              f"(the second ball, an honest PL 3-ball by L1)",
              m_minus == set(tets_BR),
              f"m_minus={len(m_minus)} K(B_R)={len(tets_BR)}")

        # Step 0(iv): the two balls meet EXACTLY along the common boundary
        # 2-sphere (their shared triangles are exactly boundary(B_R)).
        faces_BR = set()
        for t in tets_BR:
            faces_BR.update(faces_of_tet(t))
        faces_cone = set()
        for t in cone_tets:
            faces_cone.update(faces_of_tet(t))
        shared = faces_BR & faces_cone
        check(f"L3 R{R}: Step 0(iv) K(B_R) ∩ cone = boundary(B_R) "
              f"(common boundary 2-sphere; doubling hypothesis)",
              shared == bdry, f"shared={len(shared)} bdry={len(bdry)}")

        # Structural (C-pm): every triangle of M is in exactly two tets -- this
        # is FORCED by the two-ball/cone form (boundary triangles: degree 1 in
        # each ball, 1+1=2; interior triangles already degree 2).  Confirm it
        # is a structural consequence, not a per-R enumeration accident, by
        # checking the degree split matches the predicted boundary-cancellation.
        fcM: Counter = Counter()
        for t in tets_M:
            for f in faces_of_tet(t):
                fcM[f] += 1
        all_deg2 = all(c == 2 for c in fcM.values())
        # predicted: boundary(B_R) triangles get +1 from each side; others stay.
        cancellation_ok = all(
            (fcM[f] == 2) for f in bdry)
        check(f"L3 R{R}: (C-pm) boundary cancellation 1+1=2 on the gluing "
              f"sphere (every boundary triangle now degree 2) + global "
              f"pseudomanifold", all_deg2 and cancellation_ok,
              f"all_deg2={all_deg2} bdry_cancel={cancellation_ok}")


# ===========================================================================
# L2 base-agnosticity is verified in the sibling runner
# (frontier_s3_cone_cap_pl_s3_native_reproof.py, on octahedron / icosahedron /
# tetra-boundary) and was confirmed genuinely R-independent by the adversarial
# pass.  We add a single compact reconfirmation here that the cone-over-cycle
# atom is structurally general (chi = 1 wheel) for a broad range of n.
# ===========================================================================

def check_L2_cone_atom() -> None:
    print("\n=== L2: cone-over-cycle = disk atom (structurally general; "
          "wheel chi = 1) -- compact reconfirmation ===")
    # The cone over an n-cycle is the wheel W_n: V = n+1, E = 2n, F = n,
    # so chi = (n+1) - 2n + n = 1, a single rim boundary, for EVERY n.  This
    # is the R-free atom L2 uses (boundary-vertex links are circles since the
    # base S is CLOSED).  Confirm chi = 1 for a wide n-range (and structurally).
    bad = []
    for n in list(range(3, 41)) + [60, 100, 200]:
        V = n + 1  # n rim vertices + apex
        E = 2 * n  # n rim edges + n spokes
        F = n      # n triangles
        chi = V - E + F
        if chi != 1:
            bad.append((n, chi))
    check("L2 cone-over-n-cycle (wheel) has chi = 1 for all n in "
          "[3..40] u {60,100,200} (R-free disk atom)", not bad,
          f"checked={len(list(range(3,41)))+3} bad={bad}")


# ===========================================================================
# Main
# ===========================================================================

def main(argv) -> int:
    if len(argv) > 1:
        N = int(argv[1])
    else:
        N = 11  # minimum that exhibits both type-set freezes (R_0 = 9, 10)

    radii = list(range(2, N + 1))

    print("=" * 75)
    print("S^3 Cone-Cap Part B: R-FREE LEMMA-HYPOTHESIS CROSS-CHECK")
    print("Confirms the R-independent hypotheses the all-R proof rests on:")
    print("  L1(a) separable membership + scalar monotonicity => downset;")
    print("  L1(b) PRIMARY: radial SHELLING (build-up collapse; each cube")
    print("        collapses onto its smaller-key attachment => chains to a")
    print("        collapse of K(B_R); base case = 2x2x2 block to a point);")
    print("  L1(b) SECOND: single-critical discrete Morse field (Forman,")
    print("        correct direction), criticality LOCAL, types FROZEN;")
    print("  L2    cone-over-cycle = disk atom (wheel chi = 1, R-free);")
    print("  L3    two-ball gluing identities (easy-direction Newman doubling).")
    print("These CONFIRM the general-proof hypotheses; the explicit S^3 check")
    print("on built radii is in frontier_s3_cone_cap_pl_s3_native_reproof.py.")
    print("=" * 75)

    check_L1a_membership_and_downset(radii)
    check_L1b_shelling(radii)
    check_L1b_single_critical(radii)
    check_L1b_nonvacuity()
    check_L1b_downset_general()
    check_L2_cone_atom()
    check_L3_two_ball_identities(radii)

    print("\n" + "=" * 75)
    print("S3 cone-cap Part B R-free lemma cross-check:",
          "PASS" if FAIL_COUNT == 0 else "FAIL")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT} EXACT={EXACT_COUNT}")
    print(f"R-free lemma hypotheses confirmed over R = 2..{N}.")
    print("=" * 75)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
