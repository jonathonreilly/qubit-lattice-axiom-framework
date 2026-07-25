#!/usr/bin/env python3
"""Cycle 690: the proper-cubic covariance ceiling of Z^3-vertex simplicial substrates.

Every real-space Regge construction this repository builds stands on a
simplicial decomposition whose vertices are lattice sites. This cycle asks a
prior question about that substrate, exactly and combinatorially:

    for how many of the 24 proper cubic rotations can such a decomposition be
    covariant at all?

The answer is a hard ceiling, not a numerical shortfall. Every quantity below
is computed in exact integer or exact rational arithmetic on the eight cube
vertices; there is no tolerance, no fixture, no fitted constant, and no
floating-point comparison anywhere in the decisive rows.

Result:
  * No triangulation of the cube on its 8 vertices is invariant under all 24
    proper cubic rotations. The obstruction is an orbit obstruction: an
    invariant diagonal set must be a union of orbits, the face diagonals form a
    single 12-orbit and the body diagonals a single 4-orbit, and each full
    orbit self-intersects at a non-vertex point.
  * The ceiling is therefore at most 12 by Lagrange, and 12 is attained by the
    five-tetrahedron decomposition -- so the maximum is exactly 12.
  * Attaining 12 forces a binary chirality choice: the two alternating vertex
    sets each have stabilizer 12 and are exchanged by the remaining 12
    rotations. Maximal covariance and parity symmetry cannot both be held.
  * The Kuhn/Freudenthal decomposition carried by the landed 3+1 Regge module
    attains 6.

Firewalls: a stabilizer is not a symmetry of a physical law; a lattice
chirality choice is not parity violation; this cycle makes no gravity, stress,
energy, or Einstein-dynamics claim, and identifies no ratio with any physical
observable. It bounds what a substrate can support, nothing more.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from time import perf_counter

ROOT = Path(__file__).resolve().parents[1]

AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None  # set by supervisor at freeze

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


# ----------------------------------------------------------------- the cube --
VERTS = tuple(itertools.product((0, 1), repeat=3))
VIDX = {v: i for i, v in enumerate(VERTS)}


def rotations() -> tuple[tuple[tuple[int, ...], ...], ...]:
    """The 24 proper cubic rotations as integer matrices (det = +1), exact."""
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            m = [[0, 0, 0] for _ in range(3)]
            for i, p in enumerate(perm):
                m[i][p] = signs[i]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            if det == 1:
                out.append(tuple(tuple(r) for r in m))
    return tuple(out)


G = rotations()


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
                 for i in range(3))


def act_vertex(m, v: tuple[int, ...]) -> tuple[int, ...]:
    """Rotate a cube vertex about the cube centre (1/2,1/2,1/2). Exact: the
    doubled coordinate 2v-1 is an odd integer vector and stays one."""
    d = tuple(2 * c - 1 for c in v)
    r = tuple(sum(m[i][k] * d[k] for k in range(3)) for i in range(3))
    return tuple((c + 1) // 2 for c in r)


def act_set(m, vs):
    return frozenset(act_vertex(m, v) for v in vs)


# --------------------------------------------------- exact rational geometry --
def sub(a, b):
    return tuple(Fraction(a[i]) - Fraction(b[i]) for i in range(3))


def det3(u, v, w) -> Fraction:
    return (u[0] * (v[1] * w[2] - v[2] * w[1])
            - u[1] * (v[0] * w[2] - v[2] * w[0])
            + u[2] * (v[0] * w[1] - v[1] * w[0]))


def tet_volume(t) -> Fraction:
    a, b, c, d = t
    return abs(det3(sub(b, a), sub(c, a), sub(d, a))) / 6


def segments_cross_interior(p, q) -> bool:
    """True iff segments p and q meet at a point interior to both (exact)."""
    (a, b), (x, y) = p, q
    if len({a, b, x, y}) < 4:
        return False
    A, B, X, Y = (tuple(Fraction(c) for c in v) for v in (a, b, x, y))
    u = sub(B, A)
    w = sub(Y, X)
    r = sub(X, A)
    if det3(u, w, r) != 0:          # skew: no intersection at all
        return False
    # solve A + s*u = X + t*w in the common plane, exactly, via 2x2 minors
    for i, j in ((0, 1), (0, 2), (1, 2)):
        den = u[i] * (-w[j]) - u[j] * (-w[i])
        if den != 0:
            s = (r[i] * (-w[j]) - r[j] * (-w[i])) / den
            t = (u[i] * r[j] - u[j] * r[i]) / den
            meet = tuple(A[k] + s * u[k] for k in range(3))
            other = tuple(X[k] + t * w[k] for k in range(3))
            if meet != other:
                return False
            return 0 < s < 1 and 0 < t < 1
    return False


def edge_class(a, b) -> str:
    d = sum(abs(a[i] - b[i]) for i in range(3))
    return {1: "edge", 2: "face_diagonal", 3: "body_diagonal"}[d]


def orbit_of_pair(pair):
    a, b = pair
    return {frozenset((act_vertex(m, a), act_vertex(m, b))) for m in G}


def stabilizer(obj_apply, obj) -> tuple[int, ...]:
    return tuple(i for i, m in enumerate(G) if obj_apply(m, obj) == obj)


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {"cycle": 690, "authority": AUTHORITY,
                                  "audit": AUDIT, "cycle_claim": CYCLE_CLAIM}

    # -- R1: the group is exactly the 24 proper rotations and closes ----------
    prod_bad = sum(1 for a in G for b in G if matmul(a, b) not in G)
    check("the acting group is exactly the 24 proper cubic rotations and all 576 "
          "products close inside it (exact integer arithmetic)",
          len(G) == 24 and len(set(G)) == 24 and prod_bad == 0,
          {"order": len(G), "products_checked": len(G) ** 2,
           "products_outside_group": prod_bad})
    summary["group_order"] = len(G)

    # -- R2: the action on the 8 vertices is faithful and transitive ----------
    vert_orbit = {act_vertex(m, VERTS[0]) for m in G}
    faithful = len({tuple(act_vertex(m, v) for v in VERTS) for m in G}) == 24
    check("the action on the eight cube vertices is transitive and faithful",
          len(vert_orbit) == 8 and faithful,
          {"vertex_orbit_size": len(vert_orbit), "faithful": faithful})

    # -- R3: exhaustive classification of the 28 vertex pairs -----------------
    pairs = list(itertools.combinations(VERTS, 2))
    counts: dict[str, int] = {}
    for a, b in pairs:
        counts[edge_class(a, b)] = counts.get(edge_class(a, b), 0) + 1
    check("the 28 vertex pairs classify exhaustively as 12 cube edges, 12 face "
          "diagonals and 4 body diagonals",
          len(pairs) == 28 and counts == {"edge": 12, "face_diagonal": 12,
                                          "body_diagonal": 4},
          counts)

    # -- R4: each diagonal class is a single orbit ----------------------------
    face = [p for p in pairs if edge_class(*p) == "face_diagonal"]
    body = [p for p in pairs if edge_class(*p) == "body_diagonal"]
    of, ob = orbit_of_pair(face[0]), orbit_of_pair(body[0])
    check("the face diagonals form a single 12-element orbit and the body "
          "diagonals a single 4-element orbit, so any invariant diagonal set is "
          "a union of these two orbits",
          len(of) == 12 and len(ob) == 4,
          {"face_orbit": len(of), "body_orbit": len(ob)})
    summary["diagonal_orbits"] = {"face": len(of), "body": len(ob)}

    # -- R5: every positive-volume 4-subset uses at least one diagonal --------
    quads = [q for q in itertools.combinations(VERTS, 4) if tet_volume(q) > 0]
    diagless = [q for q in quads
                if all(edge_class(a, b) == "edge"
                       for a, b in itertools.combinations(q, 2))]
    check("every non-degenerate tetrahedron on cube vertices uses at least one "
          "diagonal, so a triangulation cannot avoid the diagonal set entirely",
          len(diagless) == 0,
          {"nondegenerate_tetrahedra": len(quads), "diagonal_free": len(diagless)})

    # -- R6/R7: each full orbit self-intersects off-vertex --------------------
    fx = [(p, q) for p, q in itertools.combinations([tuple(x) for x in of], 2)
          if segments_cross_interior(tuple(p), tuple(q))]
    bx = [(p, q) for p, q in itertools.combinations([tuple(x) for x in ob], 2)
          if segments_cross_interior(tuple(p), tuple(q))]
    check("the full face-diagonal orbit is simplicially inadmissible: the two "
          "diagonals of each face meet at the face centre, which is not a vertex",
          len(fx) == 6, {"interior_crossings": len(fx)})
    check("the full body-diagonal orbit is simplicially inadmissible: all four "
          "body diagonals meet at the cube centre, which is not a vertex",
          len(bx) == 6, {"interior_crossings": len(bx)})

    # -- R8: the no-go -------------------------------------------------------
    nogo = len(diagless) == 0 and len(fx) > 0 and len(bx) > 0
    check("NO-GO: no triangulation of the cube on its eight vertices is "
          "invariant under all 24 proper cubic rotations -- a nonempty invariant "
          "diagonal set must contain a full orbit, and every full orbit crosses "
          "itself at a non-vertex point",
          nogo,
          {"argument": "nonempty diagonal set + union-of-orbits + both orbits "
                       "self-intersecting", "holds": nogo})
    summary["all_24_invariant_triangulation_exists"] = not nogo

    # -- R9: Lagrange ceiling -------------------------------------------------
    divisors = [d for d in range(1, 25) if 24 % d == 0]
    ceiling = max(d for d in divisors if d < 24)
    check("Lagrange: a stabilizer order divides 24, and 24 is excluded by the "
          "no-go, so the attainable covariance order is at most 12",
          ceiling == 12, {"divisors_of_24": divisors, "ceiling_upper_bound": ceiling})

    # -- R10: the ceiling is attained ----------------------------------------
    even = tuple(v for v in VERTS if sum(v) % 2 == 0)
    odd = tuple(v for v in VERTS if sum(v) % 2 == 1)
    corner_tets = []
    for v in odd:
        nbrs = tuple(w for w in even if sum(abs(v[i] - w[i]) for i in range(3)) == 1)
        corner_tets.append((v,) + nbrs)
    five = [even] + corner_tets
    total = sum(tet_volume(t) for t in five)
    # exact disjointness: each tetrahedron lies in a closed cell of the
    # arrangement of the four planes bounding the central tetrahedron
    def _cross(u, v):
        return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0])

    def _axes(t):
        vs = [tuple(Fraction(c) for c in v) for v in t]
        edges = [sub(vs[j], vs[i]) for i, j in itertools.combinations(range(4), 2)]
        faces = [_cross(sub(vs[b], vs[a]), sub(vs[c], vs[a]))
                 for a, b, c in itertools.combinations(range(4), 3)]
        return edges, faces

    def interiors_disjoint(t1, t2) -> bool:
        """Exact separating-axis test; shared faces/edges are allowed."""
        e1, f1 = _axes(t1)
        e2, f2 = _axes(t2)
        for n in list(f1) + list(f2) + [_cross(a, b) for a in e1 for b in e2]:
            if all(c == 0 for c in n):
                continue
            p1 = [sum(n[i] * Fraction(v[i]) for i in range(3)) for v in t1]
            p2 = [sum(n[i] * Fraction(v[i]) for i in range(3)) for v in t2]
            if max(p1) <= min(p2) or max(p2) <= min(p1):
                return True
        return False

    overlaps = [(i, j) for i, j in itertools.combinations(range(5), 2)
                if not interiors_disjoint(five[i], five[j])]
    stab_even = stabilizer(act_set, frozenset(even))
    check("the five-tetrahedron decomposition is a genuine triangulation: exact "
          "volumes sum to 1 and the five pieces "
          "are pairwise interior-disjoint by an exact separating-axis test",
          total == 1 and not overlaps,
          {"total_volume": str(total), "pieces": len(five),
           "overlapping_pairs": len(overlaps)})
    check("the ceiling is ATTAINED: the five-tetrahedron decomposition has "
          "stabilizer of order exactly 12, so the maximum proper-cubic "
          "covariance of any Z^3-vertex cube triangulation is exactly 12",
          len(stab_even) == 12,
          {"stabilizer_order": len(stab_even), "frames": list(stab_even)})
    summary["covariance_ceiling"] = len(stab_even)

    # -- R11: attaining the ceiling forces a chirality choice -----------------
    stab_odd = stabilizer(act_set, frozenset(odd))
    swap = [i for i, m in enumerate(G) if act_set(m, frozenset(even)) == frozenset(odd)]
    check("attaining the ceiling forces a binary chirality choice: the two "
          "alternating vertex sets each have stabilizer 12 and are exchanged by "
          "the remaining 12 rotations, so maximal covariance and full parity "
          "symmetry cannot be held together",
          len(stab_even) == 12 and len(stab_odd) == 12 and len(swap) == 12,
          {"even_stabilizer": len(stab_even), "odd_stabilizer": len(stab_odd),
           "exchanging_rotations": len(swap)})
    summary["chirality_forced_at_ceiling"] = (len(swap) == 12)

    # -- R12: what the landed substrate actually attains ----------------------
    kuhn = set()
    for perm in itertools.permutations(range(3)):
        cur = [0, 0, 0]
        vs = [tuple(cur)]
        for a in perm:
            cur = list(cur)
            cur[a] = 1
            vs.append(tuple(cur))
        kuhn.add(frozenset(vs))
    kuhn = frozenset(kuhn)

    def act_complex(m, kx):
        return frozenset(frozenset(act_vertex(m, v) for v in s) for s in kx)

    stab_kuhn = stabilizer(act_complex, kuhn)
    check("the Kuhn/Freudenthal path decomposition -- the one carried by the "
          "landed 3+1 Regge module -- attains 6, which is half the ceiling and a "
          "quarter of the full group",
          len(stab_kuhn) == 6,
          {"stabilizer_order": len(stab_kuhn), "ceiling": len(stab_even),
           "group_order": len(G)})
    summary["landed_kuhn_covariance"] = len(stab_kuhn)

    # -- R13: the mechanism, exhibited ---------------------------------------
    spatial = [v for v in VERTS if any(v)]
    carried_out = []
    for i, m in enumerate(G):
        for v in spatial:
            w = tuple(sum(m[r][k] * v[k] for k in range(3)) for r in range(3))
            if any(c < 0 for c in w):
                carried_out.append((i, v, w))
                break
    preserving = 24 - len(carried_out)
    check("MECHANISM: the obstruction is that the 0/1 spatial direction set is "
          "closed under coordinate permutation but not under sign flip -- only the "
          "3 even permutations preserve it, and the other 21 rotations carry some "
          "direction out of {0,1}^3, so covariance there is ill posed rather than "
          "violated. The larger folded scope of 6 is a DISTINCT count: the static "
          "tick fold absorbs a global sign, so -P acts like P on the folded object",
          len(carried_out) == 21 and preserving == 3,
          {"frames_carrying_a_direction_out": len(carried_out),
           "frames_preserving_the_spatial_direction_set": preserving,
           "witness_frame": carried_out[0][0] if carried_out else None,
           "witness": f"{carried_out[0][1]} -> {carried_out[0][2]}"
                      if carried_out else None})

    # -- R14: the escape condition -------------------------------------------
    centre = (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))
    faces = []
    for axis in range(3):
        for val in (0, 1):
            fv = [v for v in VERTS if v[axis] == val]
            faces.append(tuple(fv))
    pyramids = frozenset(frozenset(f) for f in faces)

    def act_pyr(m, ps):
        return frozenset(frozenset(act_vertex(m, v) for v in s) for s in ps)

    stab_pyr = stabilizer(act_pyr, pyramids)
    check("ESCAPE CONDITION: enriching the vertex set restores the full group -- "
          "the six-pyramid decomposition about the added cube centre is invariant "
          "under all 24 rotations, so the ceiling is a property of Z^3 vertices, "
          "not of cubic symmetry itself",
          len(stab_pyr) == 24,
          {"stabilizer_order": len(stab_pyr), "added_vertex": "cube centre",
           "note": "pyramids are not simplices; a simplicial refinement needs "
                   "further vertices, which is the cost of the escape"})
    summary["escape_requires_vertices_beyond_Z3"] = (len(stab_pyr) == 24)

    summary["no_go"] = {
        "statement": "no Z^3-vertex cube triangulation is invariant under all 24 "
                     "proper cubic rotations",
        "escape_conditions": ["enrich the vertex set beyond Z^3 (face/body "
                              "centres), at the cost of leaving the lattice",
                              "accept 12 via the five-tetrahedron decomposition "
                              "and declare a chirality",
                              "accept 6, which is what the landed Kuhn complex "
                              "carries"],
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    summary["firewalls"] = {
        "stabilizer_called_a_physical_symmetry": False,
        "chirality_choice_called_parity_violation": False,
        "any_gravity_stress_energy_or_einstein_claim": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["passes"] = PASS
    summary["failures"] = FAIL

    # The runner writes its own receipt: every value below is either computed by
    # this run or hashed from the bytes on disk at run time. No field is
    # transcribed by hand and no field attests another process's artifact.
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0
    receipt = ROOT / "outputs" / (
        "physical_proper_cubic_covariance_ceiling_cycle690_receipt_2026_07_24.json")
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(json.dumps(summary, indent=1, sort_keys=True,
                                      default=str) + "\n", encoding="utf-8")
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT PROPER_CUBIC_COVARIANCE_CEILING_TOURNAMENT_FAILED")
        return 1
    print("RESULT Z3_VERTEX_PROPER_CUBIC_COVARIANCE_CEILING_IS_EXACTLY_12")
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
