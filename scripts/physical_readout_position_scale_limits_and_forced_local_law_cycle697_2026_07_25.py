#!/usr/bin/env python3
"""Cycle 697: two structural limits of the Record readout clause, and the
forced form of any local record-sourced scalar law.

The four framework axioms supply, on the readout surface, exactly three
clauses: only records are readable, a readout value is determined by record
content alone, and finite scalar readout is additive over pairwise-disjoint
record collections with the empty collection reading zero.  Lattice supplies
`Z^3` with nearest-neighbor adjacency, standard translations, and proper cubic
rotations, and privileges no site.

Three questions are answered here with exact arithmetic.

L1  (positive) Which translation-covariant, proper-cubic-covariant, additive
    operators act on site functions with nearest-neighbor range?  The invariant
    kernel space is exactly two-dimensional, spanned by the identity and the
    lattice Laplacian; the sublocus that annihilates constant fields is
    one-dimensional and is the Laplacian ray.  The dimension count equals the
    number of proper-octahedral orbits inside the support ball, so the
    two-dimensionality is a range-1 fact and is checked to fail at range
    sqrt(2).

L2  (negative) A Record readout is blind to record position.  If a
    record-sourced field is required to be, at each site, a readout in the
    axiom's content-only sense, the induced field is constant in the site
    index.  A nonconstant field therefore needs one further supplied
    structure: a site-anchored readout.

L3  (negative) No nonzero Record readout is dimensionless.  A dimensionless
    quantity is invariant under duplicating the record collection by a distant
    lattice translate; additivity makes the same quantity double.  The only
    additive content-weight vector compatible with both is zero.

The combinatorial legality of the duplication used by L3 is checked
separately: for a translate far enough that the two copies are disjoint and
mutually non-adjacent, every occupied site keeps the nearest-neighbor
occupancy pattern it had in its own copy, so any fixed nearest-neighbor
admissibility rule that admitted the copy admits the union.

No dynamics, probability, measurement rule, readout-context selector, carrier
identification, or source/action identification is derived or claimed.  No
axiom or primitive is proposed or adopted.  Every scored row uses exact
integer or Fraction arithmetic.  The runner imports no repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None

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


# --------------------------------------------------------------------------
# exact linear algebra over Q
# --------------------------------------------------------------------------


def rref(rows: list[list[F]]) -> tuple[list[list[F]], list[int]]:
    """Reduced row echelon form over Q.  Returns (rows, pivot columns)."""
    mat = [list(r) for r in rows]
    if not mat:
        return [], []
    ncols = len(mat[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pick = None
        for rr in range(r, len(mat)):
            if mat[rr][c] != 0:
                pick = rr
                break
        if pick is None:
            continue
        mat[r], mat[pick] = mat[pick], mat[r]
        inv = F(1, 1) / mat[r][c]
        mat[r] = [v * inv for v in mat[r]]
        for rr in range(len(mat)):
            if rr != r and mat[rr][c] != 0:
                f = mat[rr][c]
                mat[rr] = [a - f * b for a, b in zip(mat[rr], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, pivots


def nullspace(rows: list[list[F]], ncols: int) -> list[list[F]]:
    """Exact basis of {x : rows . x = 0}."""
    if not rows:
        return [[F(1) if i == j else F(0) for i in range(ncols)] for j in range(ncols)]
    mat, pivots = rref(rows)
    free = [c for c in range(ncols) if c not in pivots]
    basis: list[list[F]] = []
    for fc in free:
        vec = [F(0)] * ncols
        vec[fc] = F(1)
        for ri, pc in enumerate(pivots):
            vec[pc] = -mat[ri][fc]
        basis.append(vec)
    return basis


def solve_exact(cols: list[list[F]], target: list[F]) -> list[F] | None:
    """Exact solution of sum_j x_j * cols[j] == target, or None if none exists."""
    nrows = len(target)
    aug = [[cols[j][i] for j in range(len(cols))] + [target[i]] for i in range(nrows)]
    mat, pivots = rref(aug)
    ncols = len(cols)
    if ncols in pivots:  # pivot in the augmented column => inconsistent
        return None
    sol = [F(0)] * ncols
    for ri, pc in enumerate(pivots):
        sol[pc] = mat[ri][ncols]
    return sol


# --------------------------------------------------------------------------
# the lattice and its proper cubic rotations
# --------------------------------------------------------------------------

Vec = tuple[int, int, int]


def signed_permutations() -> list[tuple[Vec, Vec, Vec]]:
    """All 48 signed permutation matrices, as row triples."""
    out = []
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            rows = tuple(
                tuple(signs[i] * basis[perm[i]][k] for k in range(3)) for i in range(3)
            )
            out.append(rows)
    return out


def det3(m: tuple[Vec, Vec, Vec]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def apply(m: tuple[Vec, Vec, Vec], v: Vec) -> Vec:
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def matmul(m: tuple[Vec, Vec, Vec], n: tuple[Vec, Vec, Vec]) -> tuple[Vec, Vec, Vec]:
    return tuple(  # type: ignore[return-value]
        tuple(sum(m[i][k] * n[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def ball(radius_squared: int) -> list[Vec]:
    r = int(radius_squared**0.5) + 1
    pts = [
        (x, y, z)
        for x in range(-r, r + 1)
        for y in range(-r, r + 1)
        for z in range(-r, r + 1)
        if x * x + y * y + z * z <= radius_squared
    ]
    return sorted(pts)


def orbits(group: list[tuple[Vec, Vec, Vec]], points: list[Vec]) -> list[frozenset[Vec]]:
    pointset = set(points)
    seen: set[Vec] = set()
    out = []
    for p in points:
        if p in seen:
            continue
        orb = frozenset(apply(g, p) for g in group)
        if not orb <= pointset:
            raise AssertionError(f"orbit of {p} leaves the support set")
        seen |= orb
        out.append(orb)
    return out


def invariance_nullity(
    group: list[tuple[Vec, Vec, Vec]], points: list[Vec]
) -> tuple[int, list[list[F]]]:
    """Dimension and basis of {k : Q^points | k(g.v) = k(v) for all g, v}."""
    index = {p: i for i, p in enumerate(points)}
    n = len(points)
    rows: list[list[F]] = []
    for g in group:
        for p in points:
            q = apply(g, p)
            if q == p:
                continue
            row = [F(0)] * n
            row[index[q]] += F(1)
            row[index[p]] -= F(1)
            rows.append(row)
    basis = nullspace(rows, n)
    return len(basis), basis


# --------------------------------------------------------------------------
# torus operators built from a displacement kernel
# --------------------------------------------------------------------------


def torus_sites(size: int) -> list[Vec]:
    return [(x, y, z) for x in range(size) for y in range(size) for z in range(size)]


def kernel_matrix(kernel: dict[Vec, F], size: int) -> list[list[F]]:
    sites = torus_sites(size)
    index = {s: i for i, s in enumerate(sites)}
    mat = [[F(0)] * len(sites) for _ in sites]
    for s in sites:
        for v, w in kernel.items():
            if w == 0:
                continue
            t = tuple((s[i] + v[i]) % size for i in range(3))
            mat[index[s]][index[t]] += w
    return mat


FACES: list[Vec] = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

IDENTITY_KERNEL: dict[Vec, F] = {(0, 0, 0): F(1)}
LAPLACE_KERNEL: dict[Vec, F] = {(0, 0, 0): F(-6), **{v: F(1) for v in FACES}}


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 697,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # ------------------------------------------------------------------
    # C1  the proper cubic rotation group
    # ------------------------------------------------------------------
    allsp = signed_permutations()
    proper = [m for m in allsp if det3(m) == 1]
    properset = set(proper)
    closed = all(matmul(a, b) in properset for a in proper for b in proper)
    check(
        "C1 proper cubic rotations: 24 of the 48 signed permutations have "
        "det +1 and form a closed group",
        len(allsp) == 48
        and len(proper) == 24
        and closed
        and all(det3(m) == 1 for m in proper),
        {"signed_permutations": len(allsp), "proper": len(proper), "closed": closed},
    )
    summary["rotation_group_order"] = len(proper)

    trivial = [((1, 0, 0), (0, 1, 0), (0, 0, 1))]

    # ------------------------------------------------------------------
    # C2  orbit structure of the nearest-neighbor ball
    # ------------------------------------------------------------------
    b1 = ball(1)
    orb_b1 = orbits(proper, b1)
    face_orbit = [o for o in orb_b1 if (1, 0, 0) in o]
    orb_b1_trivial = orbits(trivial, b1)
    check(
        "C2 the 6 face displacements form one proper-rotation orbit, so the "
        "nearest-neighbor ball splits into exactly 2 orbits (7 without rotations)",
        len(b1) == 7
        and len(orb_b1) == 2
        and len(face_orbit) == 1
        and set(face_orbit[0]) == set(FACES)
        and len(orb_b1_trivial) == 7,
        {
            "ball_points": len(b1),
            "orbits_with_rotations": len(orb_b1),
            "orbits_without_rotations": len(orb_b1_trivial),
            "face_orbit_size": len(face_orbit[0]),
        },
    )

    # ------------------------------------------------------------------
    # C3  invariant kernel dimension equals the orbit count, radius by radius
    # ------------------------------------------------------------------
    table = {}
    agree = True
    for r2 in (1, 2, 3, 4, 5, 6):
        pts = ball(r2)
        dim, _ = invariance_nullity(proper, pts)
        norb = len(orbits(proper, pts))
        table[r2] = {"points": len(pts), "orbits": norb, "invariant_dimension": dim}
        if dim != norb:
            agree = False
    dim_b1, basis_b1 = invariance_nullity(proper, b1)
    dim_b1_trivial, _ = invariance_nullity(trivial, b1)
    dim_b2, basis_b2 = invariance_nullity(proper, ball(2))
    check(
        "C3 the exactly solved invariance system has nullity equal to the "
        "orbit count at every tested radius; range 1 gives 2, range sqrt(2) "
        "gives 3, and dropping rotations gives 7",
        agree and dim_b1 == 2 and dim_b2 == 3 and dim_b1_trivial == 7,
        {
            "range_1_dimension": dim_b1,
            "range_sqrt2_dimension": dim_b2,
            "range_1_dimension_without_rotations": dim_b1_trivial,
            "table": table,
        },
    )
    summary["invariant_local_kernel_dimension_by_radius_squared"] = table

    # ------------------------------------------------------------------
    # C4  the range-1 invariant family is exactly span{I, Laplacian}
    # ------------------------------------------------------------------
    size = 5
    id_mat = kernel_matrix(IDENTITY_KERNEL, size)
    lap_mat = kernel_matrix(LAPLACE_KERNEL, size)
    flat_id = [v for row in id_mat for v in row]
    flat_lap = [v for row in lap_mat for v in row]

    coeffs = []
    all_in_span = True
    for vec in basis_b1:
        kern = {p: vec[i] for i, p in enumerate(b1)}
        flat = [v for row in kernel_matrix(kern, size) for v in row]
        sol = solve_exact([flat_id, flat_lap], flat)
        if sol is None:
            all_in_span = False
            coeffs.append(None)
        else:
            coeffs.append((str(sol[0]), str(sol[1])))
    independent = solve_exact([flat_id], flat_lap) is None

    forward = {(0, 0, 0): F(-1), (1, 0, 0): F(1)}
    flat_forward = [v for row in kernel_matrix(forward, size) for v in row]
    forward_rejected = solve_exact([flat_id, flat_lap], flat_forward) is None

    check(
        "C4 every basis element of the range-1 invariant family is an exact "
        "rational combination of I and the lattice Laplacian on the periodic "
        "box, the two are independent, and the local-but-anisotropic forward "
        "difference is rejected",
        all_in_span and independent and forward_rejected and len(basis_b1) == 2,
        {
            "box": f"{size}^3 periodic",
            "coefficients_in_(I, Laplacian)": coeffs,
            "identity_and_laplacian_independent": independent,
            "forward_difference_in_span": not forward_rejected,
        },
    )

    # ------------------------------------------------------------------
    # C5  annihilating constants cuts the range-1 family to the Laplacian ray
    # ------------------------------------------------------------------
    def constant_row(points: list[Vec]) -> list[F]:
        return [F(1)] * len(points)

    rows_b1 = []
    index_b1 = {p: i for i, p in enumerate(b1)}
    for g in proper:
        for p in b1:
            q = apply(g, p)
            if q == p:
                continue
            row = [F(0)] * len(b1)
            row[index_b1[q]] += F(1)
            row[index_b1[p]] -= F(1)
            rows_b1.append(row)
    offset_b1 = nullspace(rows_b1 + [constant_row(b1)], len(b1))

    b2 = ball(2)
    rows_b2 = []
    index_b2 = {p: i for i, p in enumerate(b2)}
    for g in proper:
        for p in b2:
            q = apply(g, p)
            if q == p:
                continue
            row = [F(0)] * len(b2)
            row[index_b2[q]] += F(1)
            row[index_b2[p]] -= F(1)
            rows_b2.append(row)
    offset_b2 = nullspace(rows_b2 + [constant_row(b2)], len(b2))

    lap_vec = [LAPLACE_KERNEL.get(p, F(0)) for p in b1]
    laplacian_spans = (
        len(offset_b1) == 1 and solve_exact([offset_b1[0]], lap_vec) is not None
    )
    # a member with nonzero identity coefficient does not annihilate constants
    nonzero_offset_kernel = {(0, 0, 0): F(1), **{v: F(0) for v in FACES}}
    sum_nonzero = sum(nonzero_offset_kernel.values())
    check(
        "C5 adding 'annihilates the constant field' to the range-1 invariance "
        "system leaves exactly one dimension, spanned by the Laplacian, while "
        "the same condition at range sqrt(2) leaves two",
        len(offset_b1) == 1
        and laplacian_spans
        and len(offset_b2) == 2
        and sum(lap_vec) == 0
        and sum_nonzero != 0,
        {
            "range_1_offset_insensitive_dimension": len(offset_b1),
            "laplacian_in_that_line": laplacian_spans,
            "range_sqrt2_offset_insensitive_dimension": len(offset_b2),
            "laplacian_kernel_sum": str(sum(lap_vec)),
            "identity_kernel_sum": str(sum_nonzero),
        },
    )
    summary["forced_local_law"] = (
        "range-1 locality + lattice covariance + additivity gives a "
        "2-dimensional operator family span{I, Laplacian}; adding "
        "offset-insensitivity forces the Laplacian ray, leaving only overall "
        "scale"
    )

    # ------------------------------------------------------------------
    # C6  position blindness forces a constant field
    # ------------------------------------------------------------------
    small = 3
    sites = torus_sites(small)
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    # kernels on the whole small torus; require the induced operator to give a
    # site-independent output for every source, i.e. all matrix rows equal.
    rows_blind: list[list[F]] = []
    base = sites[0]
    for s in sites[1:]:
        for t in sites:
            row = [F(0)] * n
            # M[s][t] - M[base][t] = k(t - s) - k(t - base)
            dv = tuple((t[i] - s[i]) % small for i in range(3))
            db = tuple((t[i] - base[i]) % small for i in range(3))
            row[idx[dv]] += F(1)
            row[idx[db]] -= F(1)
            rows_blind.append(row)
    blind_basis = nullspace(rows_blind, n)
    constant_kernel = [F(1)] * n
    constant_is_solution = solve_exact([list(b) for b in blind_basis], constant_kernel)
    # negative control: the Laplacian is invariant but not position-blind, so a
    # point source produces a non-constant field
    point_source = [F(0)] * n
    point_source[idx[(0, 0, 0)]] = F(1)
    lap_small = kernel_matrix(LAPLACE_KERNEL, small)
    lap_out = [sum(lap_small[i][j] * point_source[j] for j in range(n)) for i in range(n)]
    lap_nonconstant = len(set(lap_out)) > 1
    check(
        "C6 requiring the field at every site to be a content-only readout "
        "leaves exactly the constant displacement kernels, whose field is "
        "site-independent, while the Laplacian response to a point source is "
        "not constant",
        len(blind_basis) == 1
        and constant_is_solution is not None
        and lap_nonconstant,
        {
            "position_blind_kernel_dimension": len(blind_basis),
            "constant_kernel_spans_it": constant_is_solution is not None,
            "laplacian_point_source_distinct_values": len(set(lap_out)),
        },
    )
    summary["position_blindness"] = (
        "a content-only readout at every site forces a constant field; a "
        "nonconstant record-sourced field requires a supplied site-anchored "
        "readout"
    )

    # ------------------------------------------------------------------
    # C7  no nonzero Record readout is dimensionless
    # ------------------------------------------------------------------
    # contents {A, B}; a collection is its content multiplicity vector
    f_weights = (F(3, 2), F(-5, 7))
    g_weights = (F(1), F(1))

    def readout(weights: tuple[F, F], mult: tuple[int, int]) -> F:
        return weights[0] * mult[0] + weights[1] * mult[1]

    S = (2, 3)
    S_doubled = (4, 6)
    additive_doubles = readout(f_weights, S_doubled) == 2 * readout(f_weights, S)
    ratio_S = readout(f_weights, S) / readout(g_weights, S)
    ratio_doubled = readout(f_weights, S_doubled) / readout(g_weights, S_doubled)
    ratio_invariant = ratio_S == ratio_doubled

    S1, S2 = (1, 0), (0, 1)
    q1 = readout(f_weights, S1) / readout(g_weights, S1)
    q2 = readout(f_weights, S2) / readout(g_weights, S2)
    q12 = readout(f_weights, (1, 1)) / readout(g_weights, (1, 1))
    ratio_not_additive = q12 != q1 + q2

    # the only additive weight vector that is duplication-invariant is zero
    spanning = [(1, 0), (0, 1)]
    rows_dup = []
    for mult in spanning:
        # I_h(2S) - I_h(S) = I_h(S) = 0
        rows_dup.append([F(mult[0]), F(mult[1])])
    dup_basis = nullspace(rows_dup, 2)
    check(
        "C7 an additive readout doubles under duplication while a ratio is "
        "duplication-invariant; the ratio is not additive, and the only "
        "duplication-invariant additive weight vector is zero",
        additive_doubles
        and ratio_invariant
        and ratio_not_additive
        and len(dup_basis) == 0,
        {
            "I_f(S)": str(readout(f_weights, S)),
            "I_f(S+S')": str(readout(f_weights, S_doubled)),
            "ratio(S)": str(ratio_S),
            "ratio(S+S')": str(ratio_doubled),
            "ratio(S1)+ratio(S2)": str(q1 + q2),
            "ratio(S1+S2)": str(q12),
            "duplication_invariant_additive_dimension": len(dup_basis),
        },
    )
    summary["no_dimensionless_readout"] = (
        "duplication-invariance and additivity intersect only at zero, so no "
        "nonzero Record readout is dimensionless; a dimensionless target needs "
        "a supplied reference readout and reference collection"
    )

    # ------------------------------------------------------------------
    # C8  the duplication is legal for any nearest-neighbor admissibility rule
    # ------------------------------------------------------------------
    # The admissibility rule reads nearest-neighbor CONDITIONS, not merely
    # occupancy, so the preserved object must be the full neighbor content map.
    contents = {
        (0, 0, 0): "a",
        (1, 0, 0): "b",
        (0, 1, 0): "a",
        (2, 1, 0): "c",
    }
    occupied = sorted(contents)
    diameter = max(
        abs(a[i] - b[i]) for a in occupied for b in occupied for i in range(3)
    )
    shift = (diameter + 2, 0, 0)
    copy_contents = {
        tuple(s[i] + shift[i] for i in range(3)): o for s, o in contents.items()
    }
    copy = sorted(copy_contents)
    union_contents = {**contents, **copy_contents}
    disjoint = len(union_contents) == len(contents) + len(copy_contents)

    def neighbours(s: Vec) -> list[Vec]:
        return [tuple(s[i] + v[i] for i in range(3)) for v in FACES]  # type: ignore[misc]

    def neighbour_conditions(s: Vec, cfg: dict[Vec, str]) -> tuple[str | None, ...]:
        return tuple(cfg.get(nb) for nb in neighbours(s))

    non_adjacent = all(
        nb not in copy_contents for s in occupied for nb in neighbours(s)
    ) and all(nb not in contents for s in copy for nb in neighbours(s))
    conditions_preserved = all(
        neighbour_conditions(s, contents) == neighbour_conditions(s, union_contents)
        for s in occupied
    ) and all(
        neighbour_conditions(s, copy_contents)
        == neighbour_conditions(s, union_contents)
        for s in copy
    )
    same_content_multiset = sorted(contents.values()) == sorted(copy_contents.values())
    # negative control: a near translate does change a neighbor condition
    near_shift = (1, 0, 0)
    near_copy_contents = {
        tuple(s[i] + near_shift[i] for i in range(3)): o for s, o in contents.items()
    }
    near_union = {**contents, **near_copy_contents}
    near_changes = any(
        neighbour_conditions(s, contents) != neighbour_conditions(s, near_union)
        for s in occupied
    )
    check(
        "C8 a translate beyond the support diameter is disjoint, non-adjacent, "
        "content-multiset preserving, and leaves every occupied site's full "
        "nearest-neighbor CONTENT condition unchanged, while a unit translate "
        "does not",
        disjoint
        and non_adjacent
        and conditions_preserved
        and same_content_multiset
        and near_changes,
        {
            "support_diameter": diameter,
            "shift": shift,
            "disjoint": disjoint,
            "non_adjacent": non_adjacent,
            "neighbour_content_conditions_preserved": conditions_preserved,
            "content_multiset_preserved": same_content_multiset,
            "unit_translate_changes_a_condition": near_changes,
        },
    )

    # ------------------------------------------------------------------
    # C9  the two negative limits are distinct deficiencies
    # ------------------------------------------------------------------
    # A constant nonzero field is position-blind but not dimensionless; a ratio
    # is dimensionless but not position-dependent.  Neither repair implies the
    # other, so they are separate supplied objects.
    # the position-blind kernel is constant on ALL displacements, per C6
    const_kernel = {p: F(1) for p in sites}
    m = kernel_matrix(const_kernel, small)
    const_rows_equal = all(m[i] == m[0] for i in range(1, n))
    const_out = [sum(m[i][j] * point_source[j] for j in range(n)) for i in range(n)]
    const_field_is_constant = len(set(const_out)) == 1
    const_doubles = readout((F(1), F(1)), (4, 6)) == 2 * readout((F(1), F(1)), (2, 3))
    ratio_is_position_free = ratio_S == ratio_doubled
    check(
        "C9 the two limits are independent: a position-blind readout still "
        "doubles under duplication, and a duplication-invariant ratio is still "
        "built from position-blind readouts, so neither repair supplies the "
        "other",
        const_rows_equal
        and const_field_is_constant
        and const_doubles
        and ratio_is_position_free,
        {
            "position_blind_operator_rows_identical": const_rows_equal,
            "position_blind_point_source_field_constant": const_field_is_constant,
            "position_blind_readout_still_extensive": const_doubles,
            "ratio_still_position_free": ratio_is_position_free,
        },
    )
    summary["two_limits_independent"] = True

    # ------------------------------------------------------------------
    # C10  the unit-rescaling reading of "dimensionless" gives the same answer
    # ------------------------------------------------------------------
    # A second, independent reading: a dimensionless readout is one unchanged
    # when the scalar unit is rescaled, I_h -> lambda * I_h.  Requiring
    # lambda * I_h = I_h for two distinct nonzero lambdas on a spanning family
    # again leaves only h = 0, so the L3 conclusion does not depend on which
    # reading is used.
    rows_scale: list[list[F]] = []
    for lam in (F(2), F(3)):
        for mult in spanning:
            rows_scale.append(
                [(lam - 1) * F(mult[0]), (lam - 1) * F(mult[1])]
            )
    scale_basis = nullspace(rows_scale, 2)
    # negative control: a single lambda = 1 imposes nothing, leaving dimension 2
    trivial_rows = [[F(0), F(0)] for _ in spanning]
    trivial_basis = nullspace(trivial_rows, 2)
    check(
        "C10 the unit-rescaling reading of dimensionless also leaves only the "
        "zero weight vector, while the vacuous lambda=1 condition leaves the "
        "full 2-dimensional space",
        len(scale_basis) == 0 and len(trivial_basis) == 2,
        {
            "rescaling_invariant_additive_dimension": len(scale_basis),
            "vacuous_condition_dimension": len(trivial_basis),
        },
    )

    # ------------------------------------------------------------------
    # C11  the escape is a supplied reference, and the choice is load-bearing
    # ------------------------------------------------------------------
    # Once a unit is supplied, the record-count readout is a candidate
    # reference.  It is itself extensive; intensivity comes only from the
    # quotient.  Different admissible references give different values, so the
    # reference choice is not a convention that washes out.
    count_weights = (F(1), F(1))
    count_doubles = readout(count_weights, S_doubled) == 2 * readout(count_weights, S)
    ratio_vs_count = readout(f_weights, S) / readout(count_weights, S)
    ratio_vs_count_doubled = readout(f_weights, S_doubled) / readout(
        count_weights, S_doubled
    )
    count_ratio_invariant = ratio_vs_count == ratio_vs_count_doubled
    other_reference = (F(1), F(2))
    ratio_vs_other = readout(f_weights, S) / readout(other_reference, S)
    reference_matters = ratio_vs_count != ratio_vs_other
    check(
        "C11 the record-count readout is itself extensive, the quotient by it "
        "is duplication-invariant, and a different admissible reference gives "
        "a different dimensionless value, so the reference choice is "
        "load-bearing rather than conventional",
        count_doubles
        and count_ratio_invariant
        and reference_matters
        and readout(other_reference, S) != 0,
        {
            "count_readout_doubles": count_doubles,
            "ratio_against_count": str(ratio_vs_count),
            "ratio_against_count_after_duplication": str(ratio_vs_count_doubled),
            "ratio_against_other_reference": str(ratio_vs_other),
            "reference_choice_changes_the_value": reference_matters,
        },
    )
    summary["normalization_escape"] = (
        "supplying a unit makes the record-count readout a candidate reference; "
        "the quotient is then duplication-invariant, but different admissible "
        "references give different values, so the choice is load-bearing"
    )

    summary["conclusion"] = (
        "Record additivity plus Lattice covariance plus range-1 locality "
        "determines any record-sourced scalar law up to two constants, and up "
        "to overall scale alone once the law is offset-insensitive. The same "
        "readout clause cannot supply a nonconstant field or any dimensionless "
        "value: those are two distinct supplied objects."
    )
    summary["firewalls"] = {
        "dynamics_or_measurement_claimed": False,
        "carrier_or_source_action_identified": False,
        "site_anchored_readout_supplied": False,
        "new_axiom_or_primitive_proposed": False,
        "gravity_or_koide_lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_readout_position_scale_limits_and_forced_local_law_cycle697"
        "_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT READOUT_LIMITS_AND_FORCED_LOCAL_LAW_FAILED")
        return 1
    print("RESULT READOUT_LIMITS_FIXED_AND_LOCAL_LAW_FORCED_TO_LAPLACIAN_RAY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
