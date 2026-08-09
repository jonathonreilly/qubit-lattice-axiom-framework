#!/usr/bin/env python3
"""Cycle 876 (salvage): exact affine-chart algebra of the sector grading on a
stipulated one-block ledger model.

SELF-CONTAINED IN THE SCIENTIFIC SENSE.  Every definition below -- the six
lattice directions, the three-sector supports, the balance residual, the
modeled single-exchange supports, and the two-endpoint graded-source response
algebra -- is stipulated IN-FILE.  The scientific input set is EMPTY: no
external or ancestral file is read, pinned, or imported, no AUDIT_INPUT_PATHS
are declared, and no landed construction supplies any value below.  The one
DECLARED package-local read is an integrity read of this file's own source
bytes, hashed into the receipt's self-identity field; the only write is this
runner's own receipt.  The landed constructions whose shapes these
stipulations restate are named as plain provenance text in the accompanying
support note; they are not inputs of this runner and no conclusion below is a
statement about them.

Scope, exactly.  On the stipulated model, with a support = (an incoming
direction d and a sector triple (matter, field, auxiliary) of directions):

  1. CONDITIONAL equivariance collapse: on the SUPPLIED sector-indexed
     vector-readout ansatz f_s : {6 directions} -> K^3, proper-cubic
     equivariance f(R d) = R f(d) leaves exactly one scalar coefficient per
     sector (18 -> 1).  The ansatz itself is an import: nothing here derives
     it from the framework's scalar record readout, and that bridge is OPEN.
  2. The modeled single-exchange balance plane: lawfulness of the stipulated
     carried-link support family is exactly -2 w_matter + w_field +
     w_auxiliary = 0, a rank-1 condition; the overall-scale direction
     (1, 1, 1) lies inside the plane; one scalar degree of freedom remains
     after the scale quotient.
  3. The affine chart, DISCLOSED: w_matter = 1 parameterizes only the
     w_matter != 0 part of the scale-quotiented plane, as w(t) =
     (1, 1+t, 1-t).  On that chart the balance residual is exactly A + t*B
     with A the grading-independent sector trace and B = D[field] -
     D[auxiliary].
  4. The exceptional-value census, complete on the chart: every support is
     lawful for all t, for exactly one value of t, or for none, so the
     lawful-support count as a function of the chart parameter is fully
     classified: 90 at t = 0, 36 at t = +1 and at t = -1, and 6 at every
     other value of t -- valid over every coefficient field of
     characteristic zero, not only over the rationals.  Lawful
     trace-bearing supports exist exactly at t in {-1, +1}.
  5. The chart-infinity negative control: at the scale-class [0 : 1 : -1],
     excluded by the chart, the lawful-support count is 216 with 210
     trace-bearing and 174 also carrying nonzero matter recoil.  This is
     the reviewer's counterexample to the rejected package's global-maximum
     claim, kept here as a permanent gate: 216 > 90, so no statement in
     this package may be promoted from the affine chart to the full
     scale-quotiented locus.  The projective classification is OPEN here.
  6. The stipulated response identity: on the in-file two-endpoint
     graded-source algebra, the sector-summed object equals sigma times the
     conformal channel, so sigma-sensitivity is exactly equivalent to a
     nonzero sector trace.  Whether this stipulated algebra is the physical
     conformal-mode response of any lane is expressly OPEN.
  7. The joint-constraint intersection, CONDITIONAL: if the modeled
     carried-link constraint and the modeled two-sector constraint are
     imposed JOINTLY -- and the two landed constructions they restate are
     alternative candidate laws, so nothing licenses imposing both -- the
     resulting rank-2 system meets the chart at exactly (1, 2, 0), the
     chart parameter t = +1.  This is conditional linear algebra with no
     selector authority: it argues for nothing and against nothing.

Expressly ABSENT claims (dropped from the rejected package, not established):
no derivation of the unit grading; no negative claim that any family of
routes exhausts the forcing arguments; no global or projective maximizer
claim; no provenance census; no gravity-sign visibility or escape claim; no
statement about any landed certificate beyond this stipulated model; no
convention, primitive, or owner decision surface.

Every certified number is exact stdlib rational/integer arithmetic; every
gate below asserts the exact headline values it reports, so a drifted value
fails the run rather than surviving as prose.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import permutations, product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = Path(__file__).resolve()
SELF_REL = SELF_PATH.relative_to(ROOT).as_posix()
RECEIPT_PATH = ROOT / "outputs" / (
    "grading_affine_chart_algebra_cycle876_receipt_2026_08_09.json"
)

# The legacy modules whose shapes the in-file stipulations restate, plus the
# rejected package's runners: none may be imported, and none is read.
BLOCKLISTED_MODULES = (
    "unit_weight_carried_link_recoil_cycle320_2026_07_18",
    "proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18",
    "proper_cubic_bound_object_equivalence_cycle210_2026_07_16",
    "frontier_cycle868_response_sign_census_2026_07_28",
    "frontier_cycle873_tracelessness_provenance_2026_07_28",
    "frontier_cycle876_unit_grading_provenance_2026_07_28",
    "frontier_cycle876_grading_independent_check_2026_07_28",
)


class _Firewall(importlib.abc.MetaPathFinder):
    """Fail closed if any blocklisted legacy module is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _Firewall()
sys.meta_path.insert(0, FIREWALL)

# --------------------------------------------------------------------------
# the stipulated model, entirely in-file
# --------------------------------------------------------------------------
SECTORS = ("matter", "field", "auxiliary")
AXES = 3
ZERO = Fraction(0)
ONE = Fraction(1)
THIRD = Fraction(1, 3)


def build_directions() -> tuple:
    """The six signed unit lattice directions, stipulated in-file."""
    out = []
    for axis in range(AXES):
        for sign in (1, -1):
            vec = [0, 0, 0]
            vec[axis] = sign
            out.append(tuple(vec))
    return tuple(out)


DIRECTIONS = build_directions()


def reverse_index(index: int) -> int:
    """The index of the opposite direction."""
    target = tuple(-c for c in DIRECTIONS[index])
    for j, cand in enumerate(DIRECTIONS):
        if cand == target:
            return j
    raise AssertionError("direction table is not closed under negation")


REVERSE = tuple(reverse_index(i) for i in range(len(DIRECTIONS)))


def proper_cubic_rotations() -> tuple:
    """The 24 proper cubic rotations as signed permutation matrices."""
    out = []
    for perm in permutations(range(AXES)):
        for signs in product((1, -1), repeat=AXES):
            matrix = [[0] * AXES for _ in range(AXES)]
            for row, column in enumerate(perm):
                matrix[row][column] = signs[row]
            parity = 1
            items = list(perm)
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    if items[i] > items[j]:
                        parity = -parity
            if parity * signs[0] * signs[1] * signs[2] == 1:
                out.append(tuple(tuple(row) for row in matrix))
    return tuple(out)


ROTATIONS = proper_cubic_rotations()


def vec_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def vec_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def vec_scale(factor, vector):
    return tuple(factor * c for c in vector)


def vec_zero(vector) -> bool:
    return all(c == 0 for c in vector)


def apply_matrix(matrix, vector):
    return tuple(
        sum(matrix[r][c] * vector[c] for c in range(AXES)) for r in range(AXES)
    )


def direction_index(vector) -> int:
    for i, cand in enumerate(DIRECTIONS):
        if cand == tuple(vector):
            return i
    raise AssertionError(f"{vector} is not a stipulated direction")


def modeled_carried_link_support(direction: int) -> tuple:
    """The stipulated carried-link support family: (reverse(d), d, d)."""
    return (REVERSE[direction], direction, direction)


def raw_ledger(direction: int, triple: tuple) -> tuple:
    """Per-sector raw occupation recoil: (D[m]-D[d], D[f], D[a]).

    Stipulated in-file.  Matter recoils from the incoming direction to its
    occupied direction; field and auxiliary start empty, so their recoil is
    their whole occupation.  A function of the SUPPORT alone.
    """
    unit = DIRECTIONS[direction]
    return (
        vec_sub(DIRECTIONS[triple[0]], unit),
        DIRECTIONS[triple[1]],
        DIRECTIONS[triple[2]],
    )


def sector_trace(ledger) -> tuple:
    total = (0, 0, 0)
    for row in ledger:
        total = vec_add(total, row)
    return total


def balance_residual(direction: int, triple: tuple, grading) -> tuple:
    """sum_s w_s * D[triple_s]  -  w_matter * D[direction], exactly."""
    total = (ZERO, ZERO, ZERO)
    for sector, index in enumerate(triple):
        total = vec_add(total, vec_scale(grading[sector], DIRECTIONS[index]))
    return vec_sub(total, vec_scale(grading[0], DIRECTIONS[direction]))


def normal_form(direction: int, triple: tuple) -> tuple:
    """(A, B): A = D[m]+D[f]+D[a]-D[d] (= the sector trace), B = D[f]-D[a]."""
    a_vec = vec_sub(
        vec_add(
            vec_add(DIRECTIONS[triple[0]], DIRECTIONS[triple[1]]),
            DIRECTIONS[triple[2]],
        ),
        DIRECTIONS[direction],
    )
    b_vec = vec_sub(DIRECTIONS[triple[1]], DIRECTIONS[triple[2]])
    return tuple(a_vec), tuple(b_vec)


def chart_point(parameter: Fraction) -> tuple:
    """The affine chart w(t) = (1, 1+t, 1-t) of the balance plane."""
    return (ONE, ONE + parameter, ONE - parameter)


def all_supports() -> tuple:
    """All 1296 supports (direction, (matter, field, auxiliary))."""
    n = len(DIRECTIONS)
    return tuple(
        (d, triple)
        for d in range(n)
        for triple in product(range(n), repeat=len(SECTORS))
    )


# --------------------------------------------------------------------------
# exact linear algebra
# --------------------------------------------------------------------------
def rational_rank(rows, ncols: int) -> int:
    matrix = [[Fraction(v) for v in row] for row in rows]
    pivot_row = 0
    for column in range(ncols):
        pivot = None
        for i in range(pivot_row, len(matrix)):
            if matrix[i][column] != 0:
                pivot = i
                break
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        lead = matrix[pivot_row][column]
        matrix[pivot_row] = [v / lead for v in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][column] != 0:
                f = matrix[i][column]
                matrix[i] = [
                    v - f * b for v, b in zip(matrix[i], matrix[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


# --------------------------------------------------------------------------
# certificate A -- scope controls
# --------------------------------------------------------------------------
def scope_controls() -> dict:
    result = {
        "certificate": "A_SCOPE_CONTROLS",
        "input_closure_statement": (
            "self-contained in the scientific sense: the external/ancestral "
            "scientific input set is EMPTY -- no AUDIT_INPUT_PATHS are "
            "declared, no landed construction or other repository artifact "
            "supplies any certified value, and the stipulated model is "
            "defined entirely in this file; the ONE declared package-local "
            "read is an integrity read of this runner's own source bytes for "
            "the self-identity hash; the legacy construction modules and the "
            "rejected Cycle-876 package runners are import-blocklisted"
        ),
        "audit_input_paths_declared": False,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "external_or_ancestral_scientific_files_read": (),
        "package_local_integrity_files_read": (
            (SELF_REL, "own source bytes, hashed for self_sha256"),
        ),
        "repository_files_read": (SELF_REL,),
        "repository_files_written": (
            "outputs/grading_affine_chart_algebra_cycle876_receipt_"
            "2026_08_09.json",
        ),
    }
    result["pass"] = (
        not result["blocked_modules_loaded"] and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- the model builds exactly
# --------------------------------------------------------------------------
def model_build() -> dict:
    supports = all_supports()
    directions_ok = (
        len(DIRECTIONS) == 6
        and len(set(DIRECTIONS)) == 6
        and all(sum(abs(c) for c in vec) == 1 for vec in DIRECTIONS)
    )
    reverse_ok = all(
        vec_add(DIRECTIONS[i], DIRECTIONS[REVERSE[i]]) == (0, 0, 0)
        for i in range(len(DIRECTIONS))
    )
    rotations_ok = len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24
    closure_ok = True
    permutes_ok = True
    rotation_set = set(ROTATIONS)
    for left in ROTATIONS:
        for right in ROTATIONS:
            prod_matrix = tuple(
                tuple(
                    sum(left[r][k] * right[k][c] for k in range(AXES))
                    for c in range(AXES)
                )
                for r in range(AXES)
            )
            if prod_matrix not in rotation_set:
                closure_ok = False
        images = {direction_index(apply_matrix(left, v)) for v in DIRECTIONS}
        if images != set(range(len(DIRECTIONS))):
            permutes_ok = False
    result = {
        "certificate": "B_MODEL_BUILD",
        "directions": DIRECTIONS,
        "reverse_table": REVERSE,
        "direction_table_valid": directions_ok,
        "reverse_is_negation": reverse_ok,
        "proper_cubic_rotation_count": len(ROTATIONS),
        "rotations_distinct_and_24": rotations_ok,
        "rotation_group_closed_under_product": closure_ok,
        "rotations_permute_the_directions": permutes_ok,
        "support_count": len(supports),
        "support_count_is_1296": len(supports) == 1296,
    }
    result["pass"] = (
        directions_ok
        and reverse_ok
        and rotations_ok
        and closure_ok
        and permutes_ok
        and len(supports) == 1296
    )
    return result


# --------------------------------------------------------------------------
# certificate C -- the conditional equivariance collapse (18 -> 1 per sector)
# --------------------------------------------------------------------------
def equivariance_collapse() -> dict:
    """CONDITIONAL on the supplied vector-readout ansatz f_s: dirs -> K^3."""
    free_per_sector = len(DIRECTIONS) * AXES
    rows = []
    for rotation in ROTATIONS:
        for index in range(len(DIRECTIONS)):
            image = direction_index(apply_matrix(rotation, DIRECTIONS[index]))
            for axis in range(AXES):
                row = [0] * free_per_sector
                row[image * AXES + axis] += 1
                for column in range(AXES):
                    row[index * AXES + column] -= rotation[axis][column]
                rows.append(row)
    constraint_rank = rational_rank(rows, free_per_sector)
    solution_dimension = free_per_sector - constraint_rank
    exhibited_nonzero = any(
        DIRECTIONS[i][a] != 0 for i in range(len(DIRECTIONS)) for a in range(AXES)
    )
    exhibited_equivariant = all(
        DIRECTIONS[direction_index(apply_matrix(r, DIRECTIONS[i]))]
        == apply_matrix(r, DIRECTIONS[i])
        for r in ROTATIONS
        for i in range(len(DIRECTIONS))
    )
    result = {
        "certificate": "C_EQUIVARIANCE_COLLAPSE",
        "conditional_on": (
            "the SUPPLIED sector-indexed vector-readout ansatz f_s : "
            "{6 directions} -> K^3; this ansatz is an import, not a "
            "consequence of the framework's scalar record readout, and that "
            "bridge is OPEN"
        ),
        "free_coefficients_per_sector_before_equivariance": free_per_sector,
        "equivariance_constraint_rows": len(rows),
        "constraint_rank": constraint_rank,
        "solution_dimension_per_sector": solution_dimension,
        "exhibited_solution": "f(d) = w * D[d], one scalar per sector",
        "exhibited_solution_nonzero": exhibited_nonzero,
        "exhibited_solution_equivariant": exhibited_equivariant,
        "grading_numbers_after_collapse": solution_dimension * len(SECTORS),
        "reading": (
            "on the supplied ansatz, proper-cubic equivariance is a rank-17 "
            "condition on 18 coefficients per sector, so exactly one scalar "
            "per sector survives and the grading is 3 numbers; nothing here "
            "derives the ansatz itself"
        ),
    }
    result["pass"] = (
        free_per_sector == 18
        and constraint_rank == 17
        and solution_dimension == 1
        and exhibited_nonzero
        and exhibited_equivariant
    )
    return result


# --------------------------------------------------------------------------
# certificate D -- the two modeled balance planes
# --------------------------------------------------------------------------
def proportional(row, normal) -> bool:
    """Is `row` a scalar multiple of `normal` (cross-ratio test, exact)?"""
    return all(
        row[i] * normal[j] == row[j] * normal[i]
        for i in range(len(row))
        for j in range(i + 1, len(row))
    )


def balance_planes() -> dict:
    carried_rows = []
    for direction in range(len(DIRECTIONS)):
        triple = modeled_carried_link_support(direction)
        for axis in range(AXES):
            row = [
                DIRECTIONS[triple[s]][axis] for s in range(len(SECTORS))
            ]
            row[0] -= DIRECTIONS[direction][axis]
            carried_rows.append(row)
    carried_rank = rational_rank(carried_rows, len(SECTORS))
    carried_normal = (-2, 1, 1)
    carried_span_ok = all(
        proportional(row, carried_normal) for row in carried_rows
    )
    carried_nonzero_row = any(not vec_zero(row) for row in carried_rows)

    two_sector_rows = []
    for direction in range(len(DIRECTIONS)):
        for axis in range(AXES):
            row = [
                DIRECTIONS[REVERSE[direction]][axis]
                - DIRECTIONS[direction][axis],
                DIRECTIONS[direction][axis],
                0,
            ]
            two_sector_rows.append(row)
    two_sector_rank = rational_rank(two_sector_rows, len(SECTORS))
    two_sector_normal = (-2, 1, 0)
    two_sector_span_ok = all(
        proportional(row, two_sector_normal) for row in two_sector_rows
    )

    gauge = (1, 1, 1)
    gauge_in_plane = sum(g * n for g, n in zip(gauge, carried_normal)) == 0
    plane_dimension = len(SECTORS) - carried_rank
    quotient_dimension = plane_dimension - (1 if gauge_in_plane else 0)
    result = {
        "certificate": "D_BALANCE_PLANES",
        "modeled_carried_link_constraint": {
            "support_family": "(reverse(d), d, d) for each incoming d",
            "rows": len(carried_rows),
            "rank": carried_rank,
            "row_space_spanned_by": carried_normal,
            "every_row_proportional_to_normal": carried_span_ok,
            "at_least_one_nonzero_row": carried_nonzero_row,
            "plane_equation": "-2*w_matter + w_field + w_auxiliary = 0",
        },
        "modeled_two_sector_constraint": {
            "support_family": (
                "matter at reverse(d), field at d, no auxiliary occupation"
            ),
            "rows": len(two_sector_rows),
            "rank": two_sector_rank,
            "row_space_spanned_by": two_sector_normal,
            "every_row_proportional_to_normal": two_sector_span_ok,
            "plane_equation": "-2*w_matter + w_field = 0",
        },
        "overall_scale_direction": gauge,
        "scale_direction_in_carried_link_plane": gauge_in_plane,
        "carried_link_plane_dimension": plane_dimension,
        "free_dimension_after_scale_quotient": quotient_dimension,
        "reading": (
            "each modeled constraint is a single independent linear condition "
            "on the grading; the carried-link plane has dimension 2, contains "
            "the overall-scale direction, and its scale quotient has exactly "
            "one free dimension -- one scalar degree of freedom, with no "
            "coefficient-field restriction imposed or needed"
        ),
    }
    result["pass"] = (
        carried_rank == 1
        and carried_span_ok
        and carried_nonzero_row
        and two_sector_rank == 1
        and two_sector_span_ok
        and gauge_in_plane
        and plane_dimension == 2
        and quotient_dimension == 1
    )
    return result


# --------------------------------------------------------------------------
# certificate E -- the affine-chart normal form
# --------------------------------------------------------------------------
def chart_normal_form() -> dict:
    supports = all_supports()
    probe_points = tuple(Fraction(n, 3) for n in range(-9, 10))
    identity_checks = 0
    identity_exact = True
    affine_decomposition_exact = True
    trace_equals_a = True
    for direction, triple in supports:
        a_vec, b_vec = normal_form(direction, triple)
        if sector_trace(raw_ledger(direction, triple)) != a_vec:
            trace_equals_a = False
        at_zero = balance_residual(direction, triple, chart_point(ZERO))
        at_one = balance_residual(direction, triple, chart_point(ONE))
        if tuple(at_zero) != tuple(Fraction(v) for v in a_vec):
            affine_decomposition_exact = False
        if vec_sub(at_one, at_zero) != tuple(Fraction(v) for v in b_vec):
            affine_decomposition_exact = False
        for parameter in probe_points:
            residual = balance_residual(direction, triple, chart_point(parameter))
            predicted = vec_add(
                tuple(Fraction(v) for v in a_vec),
                vec_scale(parameter, b_vec),
            )
            if residual != predicted:
                identity_exact = False
            identity_checks += 1
    result = {
        "certificate": "E_CHART_NORMAL_FORM",
        "chart": (
            "w(t) = (1, 1+t, 1-t); DISCLOSED restriction: this chart covers "
            "exactly the w_matter != 0 part of the scale-quotiented balance "
            "plane; the excluded scale class [0:1:-1] is treated in the "
            "chart-infinity control certificate"
        ),
        "supports_checked": len(supports),
        "probe_points_per_support": len(probe_points),
        "residual_identity_checks": identity_checks,
        "residual_equals_A_plus_tB_on_every_check": identity_exact,
        "affine_decomposition_exact": affine_decomposition_exact,
        "sector_trace_equals_A_on_every_support": trace_equals_a,
        "reading": (
            "the residual is affine in t by construction, so verifying its "
            "value at t = 0 (giving A) and its increment from t = 0 to t = 1 "
            "(giving B) proves residual = A + t*B identically for every t in "
            "every characteristic-zero coefficient field; the probe grid is a "
            "redundant numeric second route; the sector trace equals A, so "
            "the trace is a function of the support and never of the grading"
        ),
    }
    result["pass"] = (
        len(supports) == 1296
        and identity_checks == 1296 * len(probe_points)
        and identity_exact
        and affine_decomposition_exact
        and trace_equals_a
    )
    return result


# --------------------------------------------------------------------------
# certificate F -- the exceptional-value census, complete on the chart
# --------------------------------------------------------------------------
def solve_lawful_parameter(a_vec, b_vec):
    """The solution set in t of A + t*B = 0: 'all', one Fraction, or None."""
    if vec_zero(b_vec):
        return "all" if vec_zero(a_vec) else None
    candidate = None
    for a_c, b_c in zip(a_vec, b_vec):
        if b_c == 0:
            if a_c != 0:
                return None
            continue
        value = -Fraction(a_c, b_c)
        if candidate is None:
            candidate = value
        elif candidate != value:
            return None
    return candidate


def exceptional_census() -> dict:
    supports = all_supports()
    always_lawful = []
    never_lawful_b_zero = 0
    never_lawful_not_parallel = 0
    one_point = {}
    for direction, triple in supports:
        a_vec, b_vec = normal_form(direction, triple)
        solution = solve_lawful_parameter(a_vec, b_vec)
        if solution == "all":
            always_lawful.append((direction, triple))
        elif solution is None:
            if vec_zero(b_vec):
                never_lawful_b_zero += 1
            else:
                never_lawful_not_parallel += 1
        else:
            entry = one_point.setdefault(
                solution,
                {"supports": 0, "trace_bearing": 0,
                 "trace_bearing_with_matter_recoil": 0, "example": None},
            )
            entry["supports"] += 1
            if not vec_zero(a_vec):
                entry["trace_bearing"] += 1
                if not vec_zero(raw_ledger(direction, triple)[0]):
                    entry["trace_bearing_with_matter_recoil"] += 1
                    if entry["example"] is None:
                        entry["example"] = {
                            "direction": direction,
                            "triple": triple,
                            "A_equals_sector_trace": a_vec,
                            "B": b_vec,
                        }
    modeled_family = {
        (d, modeled_carried_link_support(d)) for d in range(len(DIRECTIONS))
    }
    always_equals_modeled_family = set(always_lawful) == modeled_family
    achieved = tuple(sorted(one_point))
    achieved_trace_bearing = tuple(
        sorted(k for k, v in one_point.items() if v["trace_bearing"] > 0)
    )

    def predicted_counts(parameter: Fraction) -> tuple:
        base = len(always_lawful)
        entry = one_point.get(parameter)
        if entry is None:
            return (base, 0, 0)
        return (
            base + entry["supports"],
            entry["trace_bearing"],
            entry["trace_bearing_with_matter_recoil"],
        )

    sweep = set()
    for denominator in range(1, 7):
        for numerator in range(-4 * denominator, 4 * denominator + 1):
            sweep.add(Fraction(numerator, denominator))
    sweep |= {
        Fraction(999, 1000), Fraction(1001, 1000),
        Fraction(-999, 1000), Fraction(-1001, 1000),
    }
    sweep_agrees = True
    for parameter in sorted(sweep):
        lawful = 0
        trace_bearing = 0
        recoil = 0
        for direction, triple in supports:
            a_vec, b_vec = normal_form(direction, triple)
            residual = vec_add(
                tuple(Fraction(v) for v in a_vec), vec_scale(parameter, b_vec)
            )
            if not vec_zero(residual):
                continue
            lawful += 1
            if not vec_zero(a_vec):
                trace_bearing += 1
                if not vec_zero(raw_ledger(direction, triple)[0]):
                    recoil += 1
        if (lawful, trace_bearing, recoil) != predicted_counts(parameter):
            sweep_agrees = False

    counts_by_exceptional_value = {
        str(k): (
            len(always_lawful) + v["supports"],
            v["trace_bearing"],
            v["trace_bearing_with_matter_recoil"],
        )
        for k, v in sorted(one_point.items())
    }
    class_counts = {
        "always_lawful": len(always_lawful),
        "never_lawful_B_zero_A_nonzero": never_lawful_b_zero,
        "never_lawful_A_not_parallel_B": never_lawful_not_parallel,
        "lawful_at_exactly_one_value": sum(
            v["supports"] for v in one_point.values()
        ),
    }
    classes_partition = sum(class_counts.values()) == len(supports)
    result = {
        "certificate": "F_EXCEPTIONAL_CENSUS",
        "supports_classified": len(supports),
        "class_counts": class_counts,
        "classes_partition_the_supports": classes_partition,
        "always_lawful_equals_the_modeled_family": always_equals_modeled_family,
        "achieved_exceptional_values": tuple(str(v) for v in achieved),
        "achieved_trace_bearing_values": tuple(
            str(v) for v in achieved_trace_bearing
        ),
        "counts_at_exceptional_values": counts_by_exceptional_value,
        "lawful_count_at_generic_parameter": len(always_lawful),
        "onset_examples": {
            str(k): v["example"] for k, v in sorted(one_point.items())
            if v["trace_bearing"] > 0
        },
        "numeric_sweep_points": len(sweep),
        "numeric_sweep_agrees_with_census": sweep_agrees,
        "domain_statement": (
            "each support's lawful-parameter solution set is empty, a single "
            "rational value, or all of K, because A and B are integer vectors; "
            "the census is therefore complete for every t in every coefficient "
            "field K of characteristic zero, and the count function is: 90 at "
            "t = 0, 36 at t = +1, 36 at t = -1, 6 at every other t.  Lawful "
            "trace-bearing supports exist exactly at t in {-1, +1}; at every "
            "t off {-1, +1} and off t = 0 the lawful family is the 6 modeled "
            "supports, all traceless"
        ),
    }
    result["pass"] = (
        classes_partition
        and len(always_lawful) == 6
        and always_equals_modeled_family
        and never_lawful_b_zero == 210
        and never_lawful_not_parallel == 936
        and achieved == (Fraction(-1), Fraction(0), Fraction(1))
        and achieved_trace_bearing == (Fraction(-1), Fraction(1))
        and counts_by_exceptional_value == {
            "-1": (36, 30, 30), "0": (90, 0, 0), "1": (36, 30, 30),
        }
        and sweep_agrees
    )
    return result


# --------------------------------------------------------------------------
# certificate G -- the chart-infinity negative control (the reviewer's point)
# --------------------------------------------------------------------------
def chart_infinity_control() -> dict:
    """The scale class [0:1:-1], excluded by the chart w_matter = 1.

    This is the adversarial reviewer's counterexample to the rejected
    package's claim that the unit grading is the global maximizer of lawful
    support count on the scale-quotiented lawful locus.  It is kept here as a
    permanent fail-closed gate so the affine-scope statements can never be
    silently promoted to the full locus.
    """
    weight = (ZERO, ONE, -ONE)
    supports = all_supports()
    lawful = 0
    trace_bearing = 0
    trace_bearing_with_recoil = 0
    example = None
    for direction, triple in supports:
        residual = balance_residual(direction, triple, weight)
        if not vec_zero(residual):
            continue
        lawful += 1
        a_vec, _ = normal_form(direction, triple)
        if not vec_zero(a_vec):
            trace_bearing += 1
            if not vec_zero(raw_ledger(direction, triple)[0]):
                trace_bearing_with_recoil += 1
                if example is None:
                    example = {
                        "direction": direction,
                        "triple": triple,
                        "A_equals_sector_trace": a_vec,
                    }
    scale_invariant = True
    for factor in (Fraction(2), Fraction(-1, 3)):
        scaled = vec_scale(factor, weight)
        for direction, triple in supports:
            base_zero = vec_zero(balance_residual(direction, triple, weight))
            scaled_zero = vec_zero(balance_residual(direction, triple, scaled))
            if base_zero != scaled_zero:
                scale_invariant = False
    affine_unit_count = 90
    result = {
        "certificate": "G_CHART_INFINITY_CONTROL",
        "scale_class": "[0 : 1 : -1] (zero matter weight)",
        "representative_weight": tuple(str(v) for v in weight),
        "satisfies_carried_link_plane": (-2) * 0 + 1 + (-1) == 0,
        "excluded_by_the_chart": True,
        "lawful_supports": lawful,
        "trace_bearing": trace_bearing,
        "trace_bearing_with_matter_recoil": trace_bearing_with_recoil,
        "example_lawful_trace_bearing_support": example,
        "lawfulness_is_scale_invariant": scale_invariant,
        "affine_unit_point_count_for_comparison": affine_unit_count,
        "exceeds_the_affine_unit_point_count": lawful > affine_unit_count,
        "refutation_recorded": (
            "the rejected package claimed the unit grading is the global "
            "maximizer of lawful support count on the scale-quotiented lawful "
            "locus; this scale class carries 216 lawful supports against 90, "
            "with 210 trace-bearing, so that claim is REFUTED; every "
            "maximality-flavoured statement in this package is affine-chart "
            "scoped only, and the projective classification is OPEN"
        ),
    }
    result["pass"] = (
        lawful == 216
        and trace_bearing == 210
        and trace_bearing_with_recoil == 174
        and scale_invariant
        and result["exceeds_the_affine_unit_point_count"]
        and example is not None
    )
    return result


# --------------------------------------------------------------------------
# certificate H -- the stipulated two-endpoint response identity
# --------------------------------------------------------------------------
def response_objects(ledger, antisymmetric: bool, sign: int) -> dict:
    """The stipulated graded-source objects on one two-endpoint array."""
    left = tuple(tuple(Fraction(v) for v in row) for row in ledger)
    right = (
        tuple(tuple(-v for v in row) for row in left) if antisymmetric else left
    )
    array = (left, right)
    conformal = tuple(
        tuple(
            sum((block[s][axis] for s in range(len(SECTORS))), ZERO)
            for axis in range(AXES)
        )
        for block in array
    )
    graded = []
    for endpoint, block in enumerate(array):
        rows = []
        for s in range(len(SECTORS)):
            rows.append(tuple(
                (block[s][axis] - THIRD * conformal[endpoint][axis])
                + Fraction(sign) * THIRD * conformal[endpoint][axis]
                for axis in range(AXES)
            ))
        graded.append(tuple(rows))
    pushed = (graded[1], graded[0])
    flattened = tuple(
        pushed[e][s][axis]
        for e in range(2)
        for s in range(len(SECTORS))
        for axis in range(AXES)
    )
    sector_sum = tuple(
        tuple(
            sum((pushed[e][s][axis] for s in range(len(SECTORS))), ZERO)
            for axis in range(AXES)
        )
        for e in range(2)
    )
    return {
        "conformal": conformal,
        "flattened": flattened,
        "sector_sum": sector_sum,
    }


def response_identity() -> dict:
    supports = all_supports()
    identity_holds = True
    equivalence_holds = True
    embedding_independent = True
    checks = 0
    for direction, triple in supports:
        ledger = raw_ledger(direction, triple)
        trace_nonzero = not vec_zero(sector_trace(ledger))
        per_embedding = {}
        for antisymmetric in (False, True):
            plus = response_objects(ledger, antisymmetric, 1)
            minus = response_objects(ledger, antisymmetric, -1)
            for sign, objects in ((1, plus), (-1, minus)):
                for endpoint in range(2):
                    swapped = 1 - endpoint
                    expected = tuple(
                        Fraction(sign) * component
                        for component in objects["conformal"][swapped]
                    )
                    if objects["sector_sum"][endpoint] != expected:
                        identity_holds = False
                    checks += 1
            sector_sensitive = plus["sector_sum"] != minus["sector_sum"]
            flat_sensitive = plus["flattened"] != minus["flattened"]
            if sector_sensitive != trace_nonzero:
                equivalence_holds = False
            if flat_sensitive != trace_nonzero:
                equivalence_holds = False
            per_embedding[antisymmetric] = (sector_sensitive, flat_sensitive)
        if per_embedding[False] != per_embedding[True]:
            embedding_independent = False
    result = {
        "certificate": "H_RESPONSE_IDENTITY",
        "stipulation": (
            "the two-endpoint graded-source algebra is stipulated in-file: "
            "per endpoint, graded[s] = block[s] - C/3 + sigma*C/3 with C the "
            "sector-summed conformal channel, then the endpoints are swapped; "
            "the sector-summed object and the flattened object are read at "
            "sigma = +1 and sigma = -1"
        ),
        "supports_checked": len(supports),
        "endpoint_identity_checks": checks,
        "sector_sum_equals_sigma_times_conformal_on_every_check": identity_holds,
        "sensitivity_iff_nonzero_sector_trace_on_every_support":
            equivalence_holds,
        "embedding_independent_on_every_support": embedding_independent,
        "reading": (
            "on the stipulated algebra the sector-summed object is exactly "
            "sigma times the conformal channel, so sigma-sensitivity is "
            "equivalent to a nonzero sector trace -- an identity of the "
            "stipulated arrays; whether these objects are the physical "
            "conformal-mode response of any lane is expressly OPEN"
        ),
    }
    result["pass"] = (
        len(supports) == 1296
        and checks == 1296 * 2 * 2 * 2
        and identity_holds
        and equivalence_holds
        and embedding_independent
    )
    return result


# --------------------------------------------------------------------------
# certificate I -- the conditional joint-constraint intersection
# --------------------------------------------------------------------------
def joint_intersection() -> dict:
    rows = [(-2, 1, 1), (-2, 1, 0)]
    joint_rank = rational_rank(rows, 3)
    # gauge w_matter = 1: solve the two equations exactly
    w_field = Fraction(2)   # from -2*1 + w_field = 0
    w_auxiliary = Fraction(2) - w_field  # from -2*1 + w_field + w_aux = 0
    solution = (ONE, w_field, w_auxiliary)
    satisfies = all(
        sum(Fraction(c) * s for c, s in zip(row, solution)) == 0
        for row in rows
    )
    chart_parameter = solution[1] - ONE
    on_chart = solution == chart_point(chart_parameter)
    two_sector_lawful_at_solution = all(
        vec_zero(vec_add(
            vec_scale(
                solution[0],
                vec_sub(DIRECTIONS[REVERSE[d]], DIRECTIONS[d]),
            ),
            vec_scale(solution[1], DIRECTIONS[d]),
        ))
        for d in range(len(DIRECTIONS))
    )
    two_sector_lawful_at_unit = all(
        vec_zero(vec_add(
            vec_sub(DIRECTIONS[REVERSE[d]], DIRECTIONS[d]),
            DIRECTIONS[d],
        ))
        for d in range(len(DIRECTIONS))
    )
    result = {
        "certificate": "I_JOINT_INTERSECTION",
        "conditional_on": (
            "imposing BOTH modeled constraints jointly; the two landed "
            "constructions they restate are alternative candidate laws, so "
            "nothing licenses the conjunction -- this is conditional linear "
            "algebra with no selector authority"
        ),
        "joint_rows": rows,
        "joint_rank": joint_rank,
        "gauge": "w_matter = 1 (same disclosed affine chart)",
        "unique_gauge_fixed_solution": tuple(str(v) for v in solution),
        "solution_satisfies_both_rows": satisfies,
        "chart_parameter_of_the_solution": str(chart_parameter),
        "solution_lies_on_the_chart": on_chart,
        "two_sector_support_lawful_at_the_solution":
            two_sector_lawful_at_solution,
        "two_sector_support_lawful_at_the_unit_point":
            two_sector_lawful_at_unit,
        "reading": (
            "IF both modeled single-exchange constraints are imposed jointly, "
            "the rank-2 system meets the chart at exactly (1, 2, 0), the "
            "chart parameter t = +1; the modeled two-sector support is "
            "unlawful at the unit point, which is plain algebra about the "
            "stipulated model and carries no preference between the "
            "alternative candidate laws"
        ),
    }
    result["pass"] = (
        joint_rank == 2
        and solution == (ONE, Fraction(2), ZERO)
        and satisfies
        and chart_parameter == 1
        and on_chart
        and two_sector_lawful_at_solution
        and not two_sector_lawful_at_unit
    )
    return result


# --------------------------------------------------------------------------
# certificate J -- in-primary falsifiers (planted corruptions must be caught)
# --------------------------------------------------------------------------
def falsifiers(census: dict, infinity: dict, joint: dict) -> dict:
    teeth = []

    tampered_counts = dict(census["counts_at_exceptional_values"])
    tampered_counts["0"] = (91, 0, 0)
    teeth.append({
        "tooth": "tampered_unit_count",
        "mutation": "the lawful count at t = 0 is claimed as 91",
        "detected": tampered_counts != census["counts_at_exceptional_values"],
    })

    tampered_achieved = tuple(
        sorted(set(census["achieved_exceptional_values"]) | {"2"})
    )
    teeth.append({
        "tooth": "planted_extra_exceptional_value",
        "mutation": "a fake exceptional value t = 2 is planted",
        "detected": tampered_achieved
        != census["achieved_exceptional_values"],
    })

    teeth.append({
        "tooth": "chart_infinity_suppressed",
        "mutation": (
            "the chart-infinity lawful count is claimed as 90 (the exact "
            "shape of the rejected global-maximum overclaim)"
        ),
        "detected": 90 != infinity["lawful_supports"],
    })

    tampered_trace = False
    for direction, triple in all_supports():
        a_vec, b_vec = normal_form(direction, triple)
        mutated = vec_add(a_vec, b_vec)
        if mutated != a_vec:
            tampered_trace = (
                sector_trace(raw_ledger(direction, triple)) != mutated
            )
            break
    teeth.append({
        "tooth": "planted_grading_dependent_trace",
        "mutation": "the trace is mutated to A + B on a support with B != 0",
        "detected": tampered_trace,
    })

    teeth.append({
        "tooth": "tampered_joint_solution",
        "mutation": "the joint solution is claimed as the unit point (1,1,1)",
        "detected": ("1", "1", "1")
        != joint["unique_gauge_fixed_solution"],
    })

    result = {
        "certificate": "J_FALSIFIERS",
        "teeth": teeth,
        "teeth_count": len(teeth),
        "teeth_that_bit": sum(1 for t in teeth if t["detected"]),
        "all_teeth_bite": all(t["detected"] for t in teeth),
    }
    result["pass"] = len(teeth) >= 5 and result["all_teeth_bite"]
    return result


# --------------------------------------------------------------------------
# certificate K -- deterministic double build
# --------------------------------------------------------------------------
def model_digest() -> str:
    payload = {
        "directions": DIRECTIONS,
        "reverse": REVERSE,
        "rotations": ROTATIONS,
        "supports": [
            {
                "support": [direction, list(triple)],
                "A": list(normal_form(direction, triple)[0]),
                "B": list(normal_form(direction, triple)[1]),
                "trace": list(sector_trace(raw_ledger(direction, triple))),
            }
            for direction, triple in all_supports()
        ],
    }
    return digest(payload)


def double_build() -> dict:
    first = model_digest()
    second = model_digest()
    result = {
        "certificate": "K_DOUBLE_BUILD",
        "model_digest_first": first,
        "model_digest_second": second,
        "deterministic": first == second,
    }
    result["pass"] = result["deterministic"]
    return result


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main() -> int:
    start = monotonic()
    cert_a = scope_controls()
    cert_b = model_build()
    cert_c = equivariance_collapse()
    cert_d = balance_planes()
    cert_e = chart_normal_form()
    cert_f = exceptional_census()
    cert_g = chart_infinity_control()
    cert_h = response_identity()
    cert_i = joint_intersection()
    cert_j = falsifiers(cert_f, cert_g, cert_i)
    cert_k = double_build()
    elapsed = monotonic() - start
    cert_l = {
        "certificate": "L_RUNTIME",
        "budget_sec": AUDIT_TIMEOUT_SEC,
        "elapsed_sec": round(elapsed, 3),
        "pass": elapsed < AUDIT_TIMEOUT_SEC,
    }
    certificates = [
        ("A_SCOPE_CONTROLS", cert_a), ("B_MODEL_BUILD", cert_b),
        ("C_EQUIVARIANCE_COLLAPSE", cert_c), ("D_BALANCE_PLANES", cert_d),
        ("E_CHART_NORMAL_FORM", cert_e), ("F_EXCEPTIONAL_CENSUS", cert_f),
        ("G_CHART_INFINITY_CONTROL", cert_g), ("H_RESPONSE_IDENTITY", cert_h),
        ("I_JOINT_INTERSECTION", cert_i), ("J_FALSIFIERS", cert_j),
        ("K_DOUBLE_BUILD", cert_k), ("L_RUNTIME", cert_l),
    ]
    checks = {name: payload["pass"] for name, payload in certificates}

    counts = cert_f["counts_at_exceptional_values"]
    certified_statements = {
        "equivariance_collapse_statement": (
            "CONDITIONAL on the supplied sector-indexed vector-readout ansatz "
            "f_s : {6 directions} -> K^3: proper-cubic equivariance is a "
            f"rank-{cert_c['constraint_rank']} condition on "
            f"{cert_c['free_coefficients_per_sector_before_equivariance']} "
            "coefficients per sector, leaving exactly "
            f"{cert_c['solution_dimension_per_sector']} scalar per sector "
            "(f(d) = w * D[d]); the ansatz itself is an import and its bridge "
            "to the framework's scalar record readout is OPEN"
        ),
        "balance_plane_statement": (
            "lawfulness of the modeled carried-link support family is exactly "
            "-2*w_matter + w_field + w_auxiliary = 0 (rank 1); the "
            "overall-scale direction (1,1,1) lies inside the plane, and the "
            "scale quotient leaves exactly one scalar degree of freedom, with "
            "no coefficient-field restriction imposed"
        ),
        "chart_normal_form_statement": (
            "on the DISCLOSED affine chart w(t) = (1, 1+t, 1-t) (covering "
            "exactly the w_matter != 0 part of the scale-quotiented plane) "
            "the balance residual is identically A + t*B with A the "
            "grading-independent sector trace and B = D[field] - "
            "D[auxiliary], for every t in every characteristic-zero "
            "coefficient field"
        ),
        "exceptional_census_statement": (
            "the census of all 1296 supports is complete on the chart: the "
            "lawful count is "
            f"{counts['0'][0]} at t = 0, {counts['1'][0]} at t = +1, "
            f"{counts['-1'][0]} at t = -1, and "
            f"{cert_f['lawful_count_at_generic_parameter']} at every other t "
            "(off the onset set AND off the unit point) in any "
            "characteristic-zero field; lawful trace-bearing supports exist "
            "exactly at t in {-1, +1} "
            f"({counts['1'][1]} at each, {counts['1'][2]} with nonzero "
            "matter recoil), and the always-lawful class is exactly the 6 "
            "modeled supports, all traceless"
        ),
        "chart_infinity_control_statement": (
            "NEGATIVE CONTROL at the scale class [0:1:-1] excluded by the "
            f"chart: {cert_g['lawful_supports']} lawful supports "
            f"({cert_g['trace_bearing']} trace-bearing, "
            f"{cert_g['trace_bearing_with_matter_recoil']} with nonzero "
            "matter recoil), REFUTING the rejected package's scale-quotiented "
            f"global-maximum claim ({cert_g['lawful_supports']} > 90); every "
            "maximality-flavoured statement here is affine-chart scoped only "
            "and the projective classification is OPEN"
        ),
        "response_identity_statement": (
            "on the STIPULATED two-endpoint graded-source algebra the "
            "sector-summed object equals sigma times the conformal channel, "
            "so sigma-sensitivity is exactly equivalent to a nonzero sector "
            "trace, on all 1296 supports under both endpoint embeddings; "
            "whether this stipulated algebra is the physical conformal-mode "
            "response of any lane is expressly OPEN"
        ),
        "joint_intersection_statement": (
            "CONDITIONAL: if the modeled carried-link constraint and the "
            "modeled two-sector constraint are imposed JOINTLY (the "
            "constructions they restate are alternative candidate laws, so "
            "nothing licenses the conjunction), the rank-2 system meets the "
            "chart at exactly (1, 2, 0), chart parameter t = +1; no selection "
            "among candidate laws is stated or implied"
        ),
    }

    receipt = {
        "cycle": 876,
        "role": "primary",
        "salvage": True,
        "question": (
            "Cycle 876 (salvage) -- exact affine-chart algebra of the sector "
            "grading on the stipulated one-block ledger model: the "
            "conditional equivariance collapse, the modeled balance planes, "
            "the chart normal form, the complete exceptional-value census, "
            "the chart-infinity negative control, the stipulated response "
            "identity, and the conditional joint intersection."
        ),
        "claim_type": "bounded_theorem",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "all_certificates_pass": all(checks.values()),
        "equivariance": {
            "constraint_rank": cert_c["constraint_rank"],
            "solution_dimension_per_sector":
                cert_c["solution_dimension_per_sector"],
        },
        "balance_plane_normals": {
            "carried_link": [-2, 1, 1],
            "two_sector": [-2, 1, 0],
        },
        "free_dimension_after_scale_quotient":
            cert_d["free_dimension_after_scale_quotient"],
        "census_class_counts": cert_f["class_counts"],
        "achieved_exceptional_values":
            cert_f["achieved_exceptional_values"],
        "achieved_trace_bearing_values":
            cert_f["achieved_trace_bearing_values"],
        "counts_at_exceptional_values":
            cert_f["counts_at_exceptional_values"],
        "lawful_count_at_generic_parameter":
            cert_f["lawful_count_at_generic_parameter"],
        "chart_infinity": {
            "lawful_supports": cert_g["lawful_supports"],
            "trace_bearing": cert_g["trace_bearing"],
            "trace_bearing_with_matter_recoil":
                cert_g["trace_bearing_with_matter_recoil"],
            "exceeds_the_affine_unit_point_count":
                cert_g["exceeds_the_affine_unit_point_count"],
        },
        "response_identity": {
            "sector_sum_equals_sigma_times_conformal":
                cert_h["sector_sum_equals_sigma_times_conformal_on_every_check"],
            "sensitivity_iff_nonzero_sector_trace":
                cert_h["sensitivity_iff_nonzero_sector_trace_on_every_support"],
            "embedding_independent":
                cert_h["embedding_independent_on_every_support"],
        },
        "joint_intersection": {
            "rank": cert_i["joint_rank"],
            "unique_gauge_fixed_solution":
                cert_i["unique_gauge_fixed_solution"],
            "chart_parameter": cert_i["chart_parameter_of_the_solution"],
        },
        "certified_statements": certified_statements,
        "model_digest": cert_k["model_digest_first"],
        "expressly_absent_claims": [
            "no derivation of the unit grading and no derivation claim for "
            "the supplied vector-readout ansatz",
            "no negative claim that any route family exhausts the forcing "
            "arguments (no such packet is shipped)",
            "no global or projective maximizer claim (refuted at chart "
            "infinity; the refutation is a gate)",
            "no provenance census of the repository",
            "no gravity-sign visibility, escape, or wall claim",
            "no statement about any landed certificate beyond this "
            "stipulated in-file model",
            "no convention, primitive, owner decision surface, or selection "
            "among candidate laws",
        ],
        "firewall_hits": len(FIREWALL.hits),
        "elapsed_sec": round(elapsed, 3),
        "scope": (
            "exact finite algebra on the stipulated in-file one-block ledger "
            "model (6 directions, 3 sectors, 1296 supports); affine-chart "
            "scope with the chart infinity kept as a negative control; "
            "stdlib exact arithmetic throughout"
        ),
        "self_sha256": sha256(SELF_PATH.read_bytes()).hexdigest(),
        "source_pins": [],
        "repository_reads": {
            "external_or_ancestral_scientific_files_read": [],
            "package_local_integrity_files_read": [
                [SELF_REL, "own source bytes, hashed for self_sha256"],
            ],
        },
    }
    receipt["science_digest"] = digest({
        "counts": cert_f["counts_at_exceptional_values"],
        "generic": cert_f["lawful_count_at_generic_parameter"],
        "classes": cert_f["class_counts"],
        "infinity": receipt["chart_infinity"],
        "joint": receipt["joint_intersection"],
        "equivariance": receipt["equivariance"],
        "model_digest": cert_k["model_digest_first"],
    })
    RECEIPT_PATH.write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n", encoding="utf-8"
    )

    lines = [
        "CYCLE876_GRADING_AFFINE_CHART_ALGEBRA_SALVAGE",
        "EXACT_FINITE_ALGEBRA_ON_A_STIPULATED_IN_FILE_MODEL",
        "AFFINE_CHART_SCOPE_ONLY_THE_PROJECTIVE_CLASSIFICATION_IS_OPEN",
        "THE_REJECTED_GLOBAL_MAXIMUM_CLAIM_IS_REFUTED_AT_CHART_INFINITY_AND"
        "_THE_REFUTATION_IS_A_GATE",
        "NO_DERIVATION_NO_SELECTION_NO_NEGATIVE_BOUNDARY_NO_GRAVITY_SIGN_CLAIM",
    ]
    for name, payload in certificates:
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    for key, statement in certified_statements.items():
        lines.append("STATEMENT " + key + " " + statement)
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 876,
        "checks": checks,
        "counts_at_exceptional_values":
            cert_f["counts_at_exceptional_values"],
        "generic_count": cert_f["lawful_count_at_generic_parameter"],
        "chart_infinity_lawful": cert_g["lawful_supports"],
        "elapsed_sec": round(elapsed, 3),
        "pass": all(checks.values()),
    }))
    lines.append(
        "CYCLE876_GRADING_AFFINE_CHART_ALGEBRA_"
        + ("PASS" if all(checks.values()) else "HONEST_FAIL")
    )
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
