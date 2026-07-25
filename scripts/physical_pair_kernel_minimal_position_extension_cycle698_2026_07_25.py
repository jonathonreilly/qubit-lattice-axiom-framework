#!/usr/bin/env python3
"""Cycle 698: the minimal position-carrying extension of the Record readout
clause is a two-body kernel, and lattice covariance classifies it.

Cycle 693 showed that content determinacy plus finite additivity force every
scalar readout into the singleton-weight form.  An earlier rejected block
showed that such a readout is position-blind and cannot be both nonzero and
duplication-invariant; it did not exclude dimensionless extensive readouts such
as the record count.  This cycle asks the positive question: what is the
smallest relational structure that carries position, and what does proper-cubic
covariance say about it under the named downstream-law conditions?

M1  Read strictly, the additivity clause forbids irreducible multi-record terms
    in the scalar readout.  Records occupy distinct sites, so every finite
    record collection is pairwise disjoint and additivity applies to every
    splitting.  The space of additive functionals on a four-site fixture is
    exactly the four-dimensional one-body space, and intersecting the two-body
    cluster space with additivity returns the same one-body space: every pair
    coefficient is killed.  This does not forbid interactions in a separate
    action or dynamics, or information about an environment encoded in a
    singleton record's content.

M2  The minimal extension is a two-body kernel `K(s(r) - s(r'), c(r), c(r'))`.
    Translation covariance makes it depend on the displacement only; proper
    cubic covariance makes it a function on octahedral orbits; at
    nearest-neighbor range with one content class the proper rotations act
    transitively on the six face displacements, so the kernel is exactly ONE
    constant, and the readout is that constant times the number of adjacent
    record pairs.

M3  That functional is genuinely outside the Record class, and the failure is
    localized: it is additive for well-separated collections and fails exactly
    when the two collections are adjacent.

M4  The two-body kernel supplies the site-anchored readout that cycle 697
    showed was missing, in a specific form: the field at a site is the
    MARGINAL readout cost of placing a test record there.  At an occupied site
    it is position-dependent; at an empty site it is defined only through the
    test record.

M5  The field operator induced by the range-1 pair kernel lands inside the
    two-dimensional span{I, Laplacian} family that cycle 697 derived from the
    law side.  The source-action route and the law-classification route agree.

No dynamics, probability, measurement rule, carrier, or source action is
adopted; the pair kernel is exhibited as the classified shape of the missing
object, not supplied as framework content.  No axiom or primitive is proposed
or adopted.  Every scored row uses exact integer or Fraction arithmetic.  The
runner imports no repository content.
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


def rref(rows: list[list[F]]) -> tuple[list[list[F]], list[int]]:
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


Vec = tuple[int, int, int]

FACES: list[Vec] = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


def signed_permutations() -> list[tuple[Vec, Vec, Vec]]:
    out = []
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            out.append(
                tuple(
                    tuple(signs[i] * basis[perm[i]][k] for k in range(3))
                    for i in range(3)
                )
            )
    return out


def det3(m: tuple[Vec, Vec, Vec]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def apply(m: tuple[Vec, Vec, Vec], v: Vec) -> Vec:
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def adjacent(a: Vec, b: Vec) -> bool:
    return sum(abs(a[i] - b[i]) for i in range(3)) == 1


def pair_count(config: list[Vec]) -> int:
    return sum(
        1 for i, a in enumerate(config) for b in config[i + 1 :] if adjacent(a, b)
    )


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 698,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # ------------------------------------------------------------------
    # M1a  additive functionals on a four-record fixture are exactly one-body
    # ------------------------------------------------------------------
    nsites = 4
    subsets = [frozenset(s) for k in range(nsites + 1)
               for s in itertools.combinations(range(nsites), k)]
    sindex = {s: i for i, s in enumerate(subsets)}
    nvars = len(subsets)

    rows: list[list[F]] = []
    # F(empty) = 0
    row = [F(0)] * nvars
    row[sindex[frozenset()]] = F(1)
    rows.append(row)
    # F(A u B) = F(A) + F(B) for every disjoint pair
    for a in subsets:
        for b in subsets:
            if a & b:
                continue
            row = [F(0)] * nvars
            row[sindex[a | b]] += F(1)
            row[sindex[a]] -= F(1)
            row[sindex[b]] -= F(1)
            rows.append(row)
    additive_basis = nullspace(rows, nvars)
    # a one-body functional for comparison
    one_body = [F(0)] * nvars
    weights = [F(2), F(-3), F(5), F(7)]
    for s in subsets:
        one_body[sindex[s]] = sum((weights[i] for i in s), F(0))
    onebody_rows = [[b[i] for i in range(nvars)] for b in additive_basis]
    mat, piv = rref([list(r) for r in onebody_rows] + [one_body])
    one_body_in_span = len(piv) == len(additive_basis)
    check(
        "M1a the additive functionals on a four-record fixture form exactly a "
        "4-dimensional space, one weight per record, and a concrete one-body "
        "functional lies in it",
        len(additive_basis) == nsites and one_body_in_span,
        {
            "additive_dimension": len(additive_basis),
            "records": nsites,
            "one_body_functional_in_span": one_body_in_span,
        },
    )

    # ------------------------------------------------------------------
    # M1b  intersecting the two-body cluster space with additivity kills pairs
    # ------------------------------------------------------------------
    pairs = list(itertools.combinations(range(nsites), 2))
    npar = nsites + len(pairs)  # one-body weights then pair coefficients

    def cluster_value(params: list[F], s: frozenset[int]) -> F:
        total = sum((params[i] for i in s), F(0))
        for pi, (i, j) in enumerate(pairs):
            if i in s and j in s:
                total += params[nsites + pi]
        return total

    rows2: list[list[F]] = []
    for a in subsets:
        for b in subsets:
            if a & b:
                continue
            row = [F(0)] * npar
            for k in range(npar):
                probe = [F(0)] * npar
                probe[k] = F(1)
                row[k] = (
                    cluster_value(probe, a | b)
                    - cluster_value(probe, a)
                    - cluster_value(probe, b)
                )
            rows2.append(row)
    additive_cluster = nullspace(rows2, npar)
    pair_block_zero = all(
        all(v[nsites + pi] == 0 for pi in range(len(pairs)))
        for v in additive_cluster
    )
    # negative control: a concrete pair-only term violates additivity
    pair_probe = [F(0)] * npar
    pair_probe[nsites] = F(1)
    pair_probe_defect = (
        cluster_value(pair_probe, frozenset({0, 1}))
        - cluster_value(pair_probe, frozenset({0}))
        - cluster_value(pair_probe, frozenset({1}))
    )
    check(
        "M1b intersecting the 10-parameter two-body cluster space with strict "
        "additivity returns the 4-dimensional one-body space with every pair "
        "coefficient zero, while a concrete pair-only term has a nonzero "
        "additivity defect",
        len(additive_cluster) == nsites
        and pair_block_zero
        and pair_probe_defect != 0,
        {
            "cluster_parameters": npar,
            "additive_intersection_dimension": len(additive_cluster),
            "all_pair_coefficients_zero": pair_block_zero,
            "pair_only_probe_defect": pair_probe_defect,
        },
    )
    summary["strict_additivity_boundary"] = (
        "no irreducible multi-record term occurs in the scalar readout under "
        "the strict reading"
    )

    # ------------------------------------------------------------------
    # M2  covariance classifies the two-body kernel; range 1 gives ONE constant
    # ------------------------------------------------------------------
    proper = [m for m in signed_permutations() if det3(m) == 1]
    shell = FACES
    sindex2 = {v: i for i, v in enumerate(shell)}
    rows3: list[list[F]] = []
    for g in proper:
        for v in shell:
            w = apply(g, v)
            if w == v:
                continue
            row = [F(0)] * len(shell)
            row[sindex2[w]] += F(1)
            row[sindex2[v]] -= F(1)
            rows3.append(row)
    kernel_basis = nullspace(rows3, len(shell))
    inversion_included = any(apply(g, (1, 0, 0)) == (-1, 0, 0) for g in proper)
    single_face = [F(1) if v == (1, 0, 0) else F(0) for v in shell]
    single_face_violates = any(
        sum(row[i] * single_face[i] for i in range(len(shell))) != 0
        for row in rows3
    )
    check(
        "M2 the proper cubic rotations act transitively on the six face "
        "displacements, so the nearest-neighbor two-body kernel is exactly one "
        "constant; the displacement reversal is already inside the proper "
        "group, while a single-face kernel violates the covariance equations",
        len(kernel_basis) == 1 and inversion_included and single_face_violates,
        {
            "range_1_pair_kernel_dimension": len(kernel_basis),
            "reversal_in_proper_group": inversion_included,
            "single_face_negative_control_violates_covariance": single_face_violates,
        },
    )
    summary["range_1_pair_kernel_parameters"] = len(kernel_basis)

    # ------------------------------------------------------------------
    # M3  the pair count is additive at separation and fails exactly on contact
    # ------------------------------------------------------------------
    A = [(0, 0, 0), (1, 0, 0)]
    B_far = [(5, 0, 0), (6, 0, 0)]
    B_touch = [(2, 0, 0), (3, 0, 0)]
    far_additive = pair_count(A + B_far) == pair_count(A) + pair_count(B_far)
    touch_fails = pair_count(A + B_touch) != pair_count(A) + pair_count(B_touch)
    contact_excess = pair_count(A + B_touch) - pair_count(A) - pair_count(B_touch)
    cross_bonds = sum(1 for a in A for b in B_touch if adjacent(a, b))
    disjoint_sites = len(set(A + B_touch)) == len(A) + len(B_touch)
    fixture_sites = [(i, 0, 0) for i in range(5)]
    fixture_subsets = [
        list(s)
        for k in range(len(fixture_sites) + 1)
        for s in itertools.combinations(fixture_sites, k)
    ]
    exhaustive_cross_bond_identity = all(
        pair_count(a + b) - pair_count(a) - pair_count(b)
        == sum(1 for x in a for y in b if adjacent(x, y))
        for a in fixture_subsets
        for b in fixture_subsets
        if set(a).isdisjoint(b)
    )
    check(
        "M3 the adjacent-pair readout is additive for well-separated "
        "collections and fails exactly on contact, by exactly the number of "
        "cross bonds, even though the two collections occupy disjoint sites",
        far_additive
        and touch_fails
        and contact_excess == cross_bonds
        and cross_bonds > 0
        and disjoint_sites
        and exhaustive_cross_bond_identity,
        {
            "pairs_A": pair_count(A),
            "pairs_B_far": pair_count(B_far),
            "pairs_A_plus_B_far": pair_count(A + B_far),
            "pairs_A_plus_B_touching": pair_count(A + B_touch),
            "contact_excess": contact_excess,
            "independently_counted_cross_bonds": cross_bonds,
            "sites_disjoint": disjoint_sites,
            "exhaustive_disjoint_pairs_on_five_site_line": exhaustive_cross_bond_identity,
        },
    )

    # ------------------------------------------------------------------
    # M4  the field is the marginal readout cost of a test record
    # ------------------------------------------------------------------
    config = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (3, 3, 3)]

    def marginal(x: Vec, cfg: list[Vec]) -> int:
        return pair_count(cfg + [x]) - pair_count(cfg)

    def neighbours_occupied(x: Vec, cfg: list[Vec]) -> int:
        return sum(1 for r in cfg if adjacent(x, r))

    empty_sites = [(2, 0, 0), (0, 0, 1), (9, 9, 9)]
    sites_are_empty = all(x not in config for x in empty_sites)
    marginal_matches = all(
        marginal(x, config) == neighbours_occupied(x, config) for x in empty_sites
    )
    field_values = {str(x): marginal(x, config) for x in empty_sites}
    field_varies = len(set(field_values.values())) > 1
    # at occupied sites, two records of the same content can see different fields
    occ_field = {
        str(r): neighbours_occupied(r, [q for q in config if q != r]) for r in config
    }
    occupied_varies = len(set(occ_field.values())) > 1
    check(
        "M4 the marginal readout cost of a test record equals the number of "
        "occupied neighbors, so the pair kernel supplies a site-anchored value; "
        "it varies across empty sites and across occupied records",
        sites_are_empty and marginal_matches and field_varies and occupied_varies,
        {
            "field_at_empty_sites": field_values,
            "field_at_occupied_records": occ_field,
            "test_sites_unoccupied": sites_are_empty,
            "marginal_equals_neighbour_count": marginal_matches,
        },
    )
    summary["site_anchored_readout_shape"] = (
        "the field at a site is the marginal readout cost of a test record "
        "placed there; at an empty site it is defined only through that test "
        "record"
    )

    # ------------------------------------------------------------------
    # M5  the induced field operator lies in cycle 697's span{I, Laplacian}
    # ------------------------------------------------------------------
    size = 5
    sites = [(x, y, z) for x in range(size) for y in range(size) for z in range(size)]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)

    def kernel_matrix(kern: dict[Vec, F]) -> list[list[F]]:
        mat = [[F(0)] * n for _ in sites]
        for s in sites:
            for v, w in kern.items():
                if w == 0:
                    continue
                t = tuple((s[i] + v[i]) % size for i in range(3))
                mat[idx[s]][idx[t]] += w
        return mat

    pair_field = kernel_matrix({v: F(1) for v in FACES})
    ident = kernel_matrix({(0, 0, 0): F(1)})
    lap = kernel_matrix({(0, 0, 0): F(-6), **{v: F(1) for v in FACES}})
    matches = all(
        pair_field[i][j] == 6 * ident[i][j] + lap[i][j]
        for i in range(n)
        for j in range(n)
    )
    # negative control: an anisotropic pair kernel is excluded from the span,
    # established by an exact solve over Q rather than by sampling candidates
    def flat(mat: list[list[F]]) -> list[F]:
        return [v for row in mat for v in row]

    def in_span(target: list[F], cols: list[list[F]]) -> bool:
        nrows = len(target)
        aug = [
            [cols[j][i] for j in range(len(cols))] + [target[i]] for i in range(nrows)
        ]
        _, piv = rref(aug)
        return len(cols) not in piv

    aniso = kernel_matrix({(1, 0, 0): F(1), (-1, 0, 0): F(1)})
    basis_cols = [flat(ident), flat(lap)]
    aniso_excluded = not in_span(flat(aniso), basis_cols)
    pair_field_in_span = in_span(flat(pair_field), basis_cols)
    probe = [F((17 * i + 5) % 23 - 11) for i in range(n)]

    def matvec(mat: list[list[F]], vec: list[F]) -> list[F]:
        return [sum((mat[i][j] * vec[j] for j in range(n)), F(0)) for i in range(n)]

    direct_pair_action = [
        sum(
            (
                probe[idx[tuple((s[k] + v[k]) % size for k in range(3))]]
                for v in FACES
            ),
            F(0),
        )
        for s in sites
    ]
    direct_lap_action = [
        sum(
            (
                probe[idx[tuple((s[k] + v[k]) % size for k in range(3))]]
                - probe[idx[s]]
                for v in FACES
            ),
            F(0),
        )
        for s in sites
    ]
    independent_action_match = (
        matvec(pair_field, probe) == direct_pair_action
        and matvec(ident, probe) == probe
        and matvec(lap, probe) == direct_lap_action
        and all(
            direct_pair_action[i] == 6 * probe[i] + direct_lap_action[i]
            for i in range(n)
        )
    )
    check(
        "M5 the field operator induced by the range-1 pair kernel equals "
        "6*I + Laplacian exactly, so it lies inside the two-dimensional family "
        "the law-side classification gives, while a single-axis pair kernel "
        "does not",
        matches and independent_action_match and pair_field_in_span and aniso_excluded,
        {
            "induced_operator": "6*I + Laplacian",
            "exact_entrywise_match": matches,
            "independent_nonconstant_probe_action_match": independent_action_match,
            "pair_field_in_span_by_exact_solve": pair_field_in_span,
            "anisotropic_kernel_excluded_by_exact_solve": aniso_excluded,
            "box": f"{size}^3 periodic",
        },
    )
    summary["law_and_source_routes_agree"] = True

    summary["conclusion"] = (
        "Under the strict reading, Record additivity excludes irreducible "
        "multi-record terms from the scalar readout; it does not exclude a "
        "separate interaction law or dynamics. The minimal relational "
        "position-carrying extension is a two-body kernel; under the named "
        "downstream-law conditions, proper-cubic covariance reduces it at "
        "nearest-neighbor range to a single constant, the adjacent-pair count. "
        "That functional is additive only for separated collections, it "
        "supplies a site-anchored value as the marginal cost of a test record, "
        "and the field operator it induces lies in the same two-dimensional "
        "family as the landed law-side classification."
    )
    summary["firewalls"] = {
        "source_action_adopted": False,
        "dynamics_or_measurement_claimed": False,
        "carrier_identified": False,
        "new_axiom_or_primitive_proposed": False,
        "gravity_or_koide_lane_status_changed": False,
        "axiom_text_reinterpreted_as_authority": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_pair_kernel_minimal_position_extension_cycle698"
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
        print("RESULT PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_FAILED")
        return 1
    print("RESULT PAIR_KERNEL_RELATIONAL_EXTENSION_CLASSIFICATION_COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
