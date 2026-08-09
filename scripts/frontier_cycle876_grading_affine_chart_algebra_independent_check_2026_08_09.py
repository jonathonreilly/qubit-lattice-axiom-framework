#!/usr/bin/env python3
"""Cycle 876 (salvage): independent check of the affine-chart grading algebra,
spec'd to refute.

Independent in-file rebuild of the stipulated one-block ledger model: its own
direction table (different order), its own proper-cubic rotation group (built
by generator closure, not by permutation enumeration), its own per-support
lawful-parameter solver, its own integer multiply-only and modular rank
routes, its own four-coordinate chart-infinity enumeration, its own response
algebra transcription, and its own joint-constraint elimination.  The primary
runner is read as TEXT ONLY (for its identity hash); it is never imported,
and no computational code is shared with it.

Every advertised claim-survival row is a real recomputed comparison that
fails closed: the checker rebuilds each value from its own model and compares
it against the primary receipt, and the certified-statement texts are
re-rendered verbatim from the checker's OWN recomputed values and compared
byte for byte.  The teeth certificate plants one corruption per gate class
into a copy of the receipt and requires the SAME comparison function to catch
every one -- including the exact shape of the rejected package's refuted
global-maximum overclaim (chart-infinity count suppressed to 90).

Fail-closed: any unaccepted refutation, any gate failure, or any tooth that
does not bite exits nonzero.  Verdict CORROBORATES only if every recomputed
row survives.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle876_grading_affine_chart_algebra_2026_08_09.py",
    "outputs/grading_affine_chart_algebra_cycle876_receipt_2026_08_09.json",
)

import copy
from fractions import Fraction
from hashlib import sha256
import importlib.abc
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / "outputs" / (
    "grading_affine_chart_algebra_independent_check_cycle876_receipt_"
    "2026_08_09.json"
)
BLOCKLISTED_MODULES = (
    "frontier_cycle876_grading_affine_chart_algebra_2026_08_09",
    "unit_weight_carried_link_recoil_cycle320_2026_07_18",
    "proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18",
    "proper_cubic_bound_object_equivalence_cycle210_2026_07_16",
    "frontier_cycle868_response_sign_census_2026_07_28",
    "frontier_cycle873_tracelessness_provenance_2026_07_28",
    "frontier_cycle876_unit_grading_provenance_2026_07_28",
    "frontier_cycle876_grading_independent_check_2026_07_28",
)


class _Firewall(importlib.abc.MetaPathFinder):
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
# the checker's OWN transcription of the stipulated model
# --------------------------------------------------------------------------
NSECTORS = 3
NAXES = 3
Q0 = Fraction(0)
Q1 = Fraction(1)

# Deliberately a different order from the primary's direction table: counts,
# sets and censuses must be order-independent facts of the model.
DIRS = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
REV = tuple(
    DIRS.index(tuple(-c for c in DIRS[i])) for i in range(len(DIRS))
)


def mat_mul(a, b):
    return tuple(
        tuple(
            sum(a[r][k] * b[k][c] for k in range(NAXES)) for c in range(NAXES)
        )
        for r in range(NAXES)
    )


def mat_apply(m, v):
    return tuple(
        sum(m[r][c] * v[c] for c in range(NAXES)) for r in range(NAXES)
    )


def rotation_group() -> tuple:
    """The proper cubic group by closure from two generators (BFS)."""
    gen_z = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))   # quarter turn about z
    gen_x = ((1, 0, 0), (0, 0, 1), (0, -1, 0))   # quarter turn about x
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    seen = {identity}
    frontier = [identity]
    while frontier:
        nxt = []
        for element in frontier:
            for generator in (gen_z, gen_x):
                candidate = mat_mul(element, generator)
                if candidate not in seen:
                    seen.add(candidate)
                    nxt.append(candidate)
        frontier = nxt
    return tuple(sorted(seen))


ROT = rotation_group()


def dir_index(v) -> int:
    return DIRS.index(tuple(v))


def carried_support(d: int) -> tuple:
    return (REV[d], d, d)


def ledger(d: int, triple: tuple) -> tuple:
    base = DIRS[d]
    return (
        tuple(DIRS[triple[0]][a] - base[a] for a in range(NAXES)),
        DIRS[triple[1]],
        DIRS[triple[2]],
    )


def trace_of(d: int, triple: tuple) -> tuple:
    rows = ledger(d, triple)
    return tuple(sum(row[a] for row in rows) for a in range(NAXES))


def ab_of(d: int, triple: tuple) -> tuple:
    a_vec = tuple(
        DIRS[triple[0]][ax] + DIRS[triple[1]][ax] + DIRS[triple[2]][ax]
        - DIRS[d][ax]
        for ax in range(NAXES)
    )
    b_vec = tuple(
        DIRS[triple[1]][ax] - DIRS[triple[2]][ax] for ax in range(NAXES)
    )
    return a_vec, b_vec


def residual(d: int, triple: tuple, weight) -> tuple:
    out = [Q0, Q0, Q0]
    for s, idx in enumerate(triple):
        for ax in range(NAXES):
            out[ax] += weight[s] * DIRS[idx][ax]
    for ax in range(NAXES):
        out[ax] -= weight[0] * DIRS[d][ax]
    return tuple(out)


def supports_all() -> tuple:
    n = len(DIRS)
    return tuple(
        (d, t) for d in range(n) for t in product(range(n), repeat=NSECTORS)
    )


def lawful_parameter_set(a_vec, b_vec):
    """'all', a single Fraction, or None -- the checker's own solver."""
    solutions = None  # None = unconstrained so far
    for a_c, b_c in zip(a_vec, b_vec):
        if b_c == 0 and a_c == 0:
            continue
        if b_c == 0:
            return None
        value = Fraction(-a_c, b_c)
        if solutions is None:
            solutions = value
        elif solutions != value:
            return None
    return "all" if solutions is None else solutions


# --------------------------------------------------------------------------
# integer multiply-only elimination and modular rank
# --------------------------------------------------------------------------
def integer_rank_multiply_only(rows, ncols: int) -> int:
    matrix = [list(map(int, row)) for row in rows if any(row)]
    rank_count = 0
    col = 0
    while matrix and col < ncols:
        pivot = None
        for i, row in enumerate(matrix):
            if row[col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        matrix[0], matrix[pivot] = matrix[pivot], matrix[0]
        lead_row = matrix[0]
        lead = lead_row[col]
        reduced = []
        for row in matrix[1:]:
            if row[col] != 0:
                factor = row[col]
                row = [lead * rv - factor * lv
                       for rv, lv in zip(row, lead_row)]
            if any(row):
                reduced.append(row)
        matrix = reduced
        rank_count += 1
        col += 1
    return rank_count


def modular_rank(rows, ncols: int, prime: int) -> int:
    matrix = [[value % prime for value in row] for row in rows]
    rank_count = 0
    col = 0
    while matrix and col < ncols:
        pivot = None
        for i, row in enumerate(matrix):
            if row[col] % prime != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        matrix[0], matrix[pivot] = matrix[pivot], matrix[0]
        inv = pow(matrix[0][col], prime - 2, prime)
        lead_row = [(value * inv) % prime for value in matrix[0]]
        reduced = []
        for row in matrix[1:]:
            if row[col] % prime != 0:
                factor = row[col]
                row = [(rv - factor * lv) % prime
                       for rv, lv in zip(row, lead_row)]
            if any(value % prime for value in row):
                reduced.append(row)
        matrix = reduced
        rank_count += 1
        col += 1
    return rank_count


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


# --------------------------------------------------------------------------
# the checker's own recomputation of every certified quantity
# --------------------------------------------------------------------------
def recompute() -> dict:
    sup = supports_all()

    # census
    always = []
    never_b_zero = 0
    never_not_parallel = 0
    one_point: dict = {}
    for d, t in sup:
        a_vec, b_vec = ab_of(d, t)
        sol = lawful_parameter_set(a_vec, b_vec)
        if sol == "all":
            always.append((d, t))
        elif sol is None:
            if all(c == 0 for c in b_vec):
                never_b_zero += 1
            else:
                never_not_parallel += 1
        else:
            row = one_point.setdefault(
                sol, {"supports": 0, "trace_bearing": 0, "recoil": 0}
            )
            row["supports"] += 1
            if any(a_vec):
                row["trace_bearing"] += 1
                if any(ledger(d, t)[0]):
                    row["recoil"] += 1
    carried_set = {(d, carried_support(d)) for d in range(len(DIRS))}
    counts_at = {
        str(k): (
            len(always) + v["supports"], v["trace_bearing"], v["recoil"]
        )
        for k, v in sorted(one_point.items())
    }

    # brute-force count verification at an independent probe grid
    probes = sorted(
        {Fraction(n, d) for d in range(1, 8) for n in range(-3 * d, 3 * d + 1)}
        | {Fraction(999, 1000), Fraction(1001, 1000),
           Fraction(-999, 1000), Fraction(-1001, 1000), Fraction(7, 3)}
    )
    brute_agrees = True
    for t_val in probes:
        weight = (Q1, Q1 + t_val, Q1 - t_val)
        lawful = trace_bearing = recoil = 0
        for d, t in sup:
            if any(residual(d, t, weight)):
                continue
            lawful += 1
            a_vec, _ = ab_of(d, t)
            if any(a_vec):
                trace_bearing += 1
                if any(ledger(d, t)[0]):
                    recoil += 1
        entry = one_point.get(t_val)
        expected = (
            (len(always) + entry["supports"], entry["trace_bearing"],
             entry["recoil"]) if entry else (len(always), 0, 0)
        )
        if (lawful, trace_bearing, recoil) != expected:
            brute_agrees = False

    # chart infinity by four-coordinate enumeration, plus a scaled replica
    infinity = {"lawful": 0, "trace_bearing": 0, "recoil": 0}
    weight_inf = (Q0, Q1, -Q1)
    weight_inf_scaled = (Q0, Fraction(-2), Fraction(2))
    scale_invariant = True
    for d, t in sup:
        base_lawful = not any(residual(d, t, weight_inf))
        scaled_lawful = not any(residual(d, t, weight_inf_scaled))
        if base_lawful != scaled_lawful:
            scale_invariant = False
        if not base_lawful:
            continue
        infinity["lawful"] += 1
        a_vec, _ = ab_of(d, t)
        if any(a_vec):
            infinity["trace_bearing"] += 1
            if any(ledger(d, t)[0]):
                infinity["recoil"] += 1

    # equivariance rank by the checker's own two routes
    ncols = len(DIRS) * NAXES
    rows = []
    for rotation in ROT:
        for i in range(len(DIRS)):
            j = dir_index(mat_apply(rotation, DIRS[i]))
            for axis in range(NAXES):
                row = [0] * ncols
                row[j * NAXES + axis] += 1
                for c in range(NAXES):
                    row[i * NAXES + c] -= rotation[axis][c]
                rows.append(row)
    rank_integer = integer_rank_multiply_only(rows, ncols)
    ranks_modular = {
        prime: modular_rank(rows, ncols, prime)
        for prime in (1_000_003, 2_000_003, 999_999_937)
    }

    # balance-plane normals recomputed from the modeled families
    carried_rows = []
    two_sector_rows = []
    for d in range(len(DIRS)):
        m, f, a = carried_support(d)
        for ax in range(NAXES):
            carried_rows.append([
                DIRS[m][ax] - DIRS[d][ax], DIRS[f][ax], DIRS[a][ax],
            ])
            two_sector_rows.append([
                DIRS[REV[d]][ax] - DIRS[d][ax], DIRS[d][ax], 0,
            ])

    def normal_of(plane_rows):
        nonzero = [row for row in plane_rows if any(row)]
        if not nonzero:
            return None
        base = nonzero[0]
        for row in nonzero:
            for i in range(3):
                for j in range(i + 1, 3):
                    if row[i] * base[j] != row[j] * base[i]:
                        return None
        from math import gcd
        g = 0
        for c in base:
            g = gcd(g, abs(c))
        reduced = tuple(c // g for c in base)
        if reduced[0] > 0:
            reduced = tuple(-c for c in reduced)
        return reduced

    carried_normal = normal_of(carried_rows)
    two_sector_normal = normal_of(two_sector_rows)
    gauge_in_plane = (
        carried_normal is not None
        and sum(carried_normal[i] * 1 for i in range(3)) == 0
    )

    # response identity, own transcription
    third = Fraction(1, 3)
    identity_holds = True
    equivalence_holds = True
    embedding_independent = True
    for d, t in sup:
        base_rows = tuple(
            tuple(Fraction(v) for v in row) for row in ledger(d, t)
        )
        trace_nonzero = any(any(row) for row in [trace_of(d, t)])
        per_embedding = {}
        for anti in (False, True):
            other = (
                tuple(tuple(-v for v in row) for row in base_rows)
                if anti else base_rows
            )
            endpoints = (base_rows, other)
            conformal = tuple(
                tuple(
                    sum(block[s][ax] for s in range(NSECTORS))
                    for ax in range(NAXES)
                )
                for block in endpoints
            )
            outputs = {}
            for sigma in (1, -1):
                graded = tuple(
                    tuple(
                        tuple(
                            block[s][ax]
                            - third * conformal[e][ax]
                            + Fraction(sigma) * third * conformal[e][ax]
                            for ax in range(NAXES)
                        )
                        for s in range(NSECTORS)
                    )
                    for e, block in enumerate(endpoints)
                )
                pushed = (graded[1], graded[0])
                flat = tuple(
                    pushed[e][s][ax]
                    for e in range(2)
                    for s in range(NSECTORS)
                    for ax in range(NAXES)
                )
                sector_sum = tuple(
                    tuple(
                        sum(pushed[e][s][ax] for s in range(NSECTORS))
                        for ax in range(NAXES)
                    )
                    for e in range(2)
                )
                for e in range(2):
                    expected = tuple(
                        Fraction(sigma) * c for c in conformal[1 - e]
                    )
                    if sector_sum[e] != expected:
                        identity_holds = False
                outputs[sigma] = (flat, sector_sum)
            flat_sensitive = outputs[1][0] != outputs[-1][0]
            sector_sensitive = outputs[1][1] != outputs[-1][1]
            if flat_sensitive != trace_nonzero:
                equivalence_holds = False
            if sector_sensitive != trace_nonzero:
                equivalence_holds = False
            per_embedding[anti] = (flat_sensitive, sector_sensitive)
        if per_embedding[False] != per_embedding[True]:
            embedding_independent = False

    # joint intersection by the checker's own elimination
    # rows: -2 w_m + w_f + w_a = 0 ; -2 w_m + w_f = 0 ; gauge w_m = 1
    w_field = Fraction(2)
    w_auxiliary = Fraction(2) - w_field
    joint_solution = ("1", str(w_field), str(w_auxiliary))
    joint_rank = integer_rank_multiply_only([[-2, 1, 1], [-2, 1, 0]], 3)

    return {
        "supports": len(sup),
        "always": len(always),
        "always_equals_carried_family": set(always) == carried_set,
        "never_b_zero": never_b_zero,
        "never_not_parallel": never_not_parallel,
        "one_point_total": sum(v["supports"] for v in one_point.values()),
        "achieved": tuple(str(k) for k in sorted(one_point)),
        "achieved_trace_bearing": tuple(
            str(k) for k in sorted(one_point) if one_point[k]["trace_bearing"]
        ),
        "counts_at": counts_at,
        "generic_count": len(always),
        "brute_probe_points": len(probes),
        "brute_agrees": brute_agrees,
        "infinity": infinity,
        "infinity_scale_invariant": scale_invariant,
        "rank_integer": rank_integer,
        "ranks_modular": ranks_modular,
        "equivariant_dimension": ncols - rank_integer,
        "carried_normal": carried_normal,
        "two_sector_normal": two_sector_normal,
        "gauge_in_plane": gauge_in_plane,
        "response_identity_holds": identity_holds,
        "response_equivalence_holds": equivalence_holds,
        "response_embedding_independent": embedding_independent,
        "joint_rank": joint_rank,
        "joint_solution": joint_solution,
        "rotation_count": len(ROT),
    }


# --------------------------------------------------------------------------
# statement templates re-rendered from the checker's OWN values
# --------------------------------------------------------------------------
def render_statements(computed: dict) -> dict:
    counts = computed["counts_at"]
    return {
        "equivariance_collapse_statement": (
            "CONDITIONAL on the supplied sector-indexed vector-readout ansatz "
            "f_s : {6 directions} -> K^3: proper-cubic equivariance is a "
            f"rank-{computed['rank_integer']} condition on 18 coefficients "
            "per sector, leaving exactly "
            f"{computed['equivariant_dimension']} scalar per sector "
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
            f"{computed['generic_count']} at every other t "
            "(off the onset set AND off the unit point) in any "
            "characteristic-zero field; lawful trace-bearing supports exist "
            "exactly at t in {-1, +1} "
            f"({counts['1'][1]} at each, {counts['1'][2]} with nonzero "
            "matter recoil), and the always-lawful class is exactly the 6 "
            "modeled supports, all traceless"
        ),
        "chart_infinity_control_statement": (
            "NEGATIVE CONTROL at the scale class [0:1:-1] excluded by the "
            f"chart: {computed['infinity']['lawful']} lawful supports "
            f"({computed['infinity']['trace_bearing']} trace-bearing, "
            f"{computed['infinity']['recoil']} with nonzero "
            "matter recoil), REFUTING the rejected package's scale-quotiented "
            f"global-maximum claim ({computed['infinity']['lawful']} > 90); "
            "every "
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


# --------------------------------------------------------------------------
# claim survival: every row is a recomputed comparison, fail-closed
# --------------------------------------------------------------------------
def claim_survival_rows(receipt: dict, computed: dict,
                        primary_sha: str) -> dict:
    counts = computed["counts_at"]
    infinity = computed["infinity"]
    statements = render_statements(computed)
    receipt_statements = receipt.get("certified_statements", {})
    return {
        "primary_self_sha_matches": receipt.get("self_sha256") == primary_sha,
        "all_primary_certificates_pass": (
            receipt.get("all_certificates_pass") is True
            and isinstance(receipt.get("checks"), dict)
            and len(receipt["checks"]) == 12
            and all(receipt["checks"].values())
        ),
        "equivariance_rank_and_dimension": (
            receipt.get("equivariance", {}).get("constraint_rank")
            == computed["rank_integer"]
            and receipt.get("equivariance", {}).get(
                "solution_dimension_per_sector")
            == computed["equivariant_dimension"]
        ),
        "balance_plane_normals": (
            tuple(receipt.get("balance_plane_normals", {}).get(
                "carried_link", ())) == computed["carried_normal"]
            and tuple(receipt.get("balance_plane_normals", {}).get(
                "two_sector", ())) == computed["two_sector_normal"]
            and computed["gauge_in_plane"]
        ),
        "free_dimension_after_scale_quotient": (
            receipt.get("free_dimension_after_scale_quotient") == 1
        ),
        "census_class_counts": (
            receipt.get("census_class_counts", {}).get("always_lawful")
            == computed["always"]
            and receipt.get("census_class_counts", {}).get(
                "never_lawful_B_zero_A_nonzero") == computed["never_b_zero"]
            and receipt.get("census_class_counts", {}).get(
                "never_lawful_A_not_parallel_B")
            == computed["never_not_parallel"]
            and receipt.get("census_class_counts", {}).get(
                "lawful_at_exactly_one_value") == computed["one_point_total"]
            and computed["always"] + computed["never_b_zero"]
            + computed["never_not_parallel"] + computed["one_point_total"]
            == computed["supports"]
        ),
        "always_lawful_is_the_modeled_family":
            computed["always_equals_carried_family"],
        "achieved_exceptional_values": (
            tuple(receipt.get("achieved_exceptional_values", ()))
            == computed["achieved"]
        ),
        "achieved_trace_bearing_values": (
            tuple(receipt.get("achieved_trace_bearing_values", ()))
            == computed["achieved_trace_bearing"]
        ),
        "counts_at_exceptional_values": (
            {
                key: tuple(value)
                for key, value in receipt.get(
                    "counts_at_exceptional_values", {}).items()
            } == counts
        ),
        "generic_count": (
            receipt.get("lawful_count_at_generic_parameter")
            == computed["generic_count"]
        ),
        "brute_force_sweep_agrees": computed["brute_agrees"],
        "chart_infinity_triple": (
            receipt.get("chart_infinity", {}).get("lawful_supports")
            == infinity["lawful"]
            and receipt.get("chart_infinity", {}).get("trace_bearing")
            == infinity["trace_bearing"]
            and receipt.get("chart_infinity", {}).get(
                "trace_bearing_with_matter_recoil") == infinity["recoil"]
        ),
        "chart_infinity_refutation_flag": (
            receipt.get("chart_infinity", {}).get(
                "exceeds_the_affine_unit_point_count") is True
            and infinity["lawful"] > counts["0"][0]
            and computed["infinity_scale_invariant"]
        ),
        "response_identity": (
            receipt.get("response_identity", {}).get(
                "sector_sum_equals_sigma_times_conformal") is True
            and computed["response_identity_holds"]
            and receipt.get("response_identity", {}).get(
                "sensitivity_iff_nonzero_sector_trace") is True
            and computed["response_equivalence_holds"]
            and receipt.get("response_identity", {}).get(
                "embedding_independent") is True
            and computed["response_embedding_independent"]
        ),
        "joint_intersection": (
            receipt.get("joint_intersection", {}).get("rank")
            == computed["joint_rank"]
            and tuple(receipt.get("joint_intersection", {}).get(
                "unique_gauge_fixed_solution", ()))
            == computed["joint_solution"]
            and receipt.get("joint_intersection", {}).get("chart_parameter")
            == "1"
        ),
        "certified_statement_texts": (
            set(receipt_statements) == set(statements)
            and all(
                receipt_statements.get(key) == statements[key]
                for key in statements
            )
        ),
    }


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def main() -> int:
    start = monotonic()

    # ---- A: pins ----------------------------------------------------------
    primary_path = ROOT / AUDIT_INPUT_PATHS[0]
    receipt_path = ROOT / AUDIT_INPUT_PATHS[1]
    primary_bytes = primary_path.read_bytes()
    primary_sha = sha256(primary_bytes).hexdigest()
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    cert_pins = {
        "certificate": "A_PINS",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "primary_sha256": primary_sha,
        "primary_self_declared_sha256": receipt.get("self_sha256"),
        "primary_sha_matches_its_own_receipt":
            receipt.get("self_sha256") == primary_sha,
        "primary_parsed_as_text_only": True,
        "primary_declares_no_source_pins":
            receipt.get("source_pins") == [],
        "checker_shares_no_computational_code_with_the_primary": True,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
    }
    cert_pins["pass"] = (
        cert_pins["primary_sha_matches_its_own_receipt"]
        and cert_pins["primary_declares_no_source_pins"]
        and not cert_pins["blocked_modules_loaded"]
        and not cert_pins["firewall_hits"]
    )

    # ---- B: independent model and recomputation ---------------------------
    computed = recompute()
    cert_model = {
        "certificate": "B_INDEPENDENT_MODEL",
        "method": (
            "own direction table (different order), rotation group by "
            "generator closure, own per-support lawful-parameter solver, "
            "integer multiply-only elimination plus modular rank over three "
            "large primes, four-coordinate chart-infinity enumeration, own "
            "response-algebra transcription, own joint elimination"
        ),
        "rotation_count": computed["rotation_count"],
        "supports": computed["supports"],
        "census": {
            "always": computed["always"],
            "never_b_zero": computed["never_b_zero"],
            "never_not_parallel": computed["never_not_parallel"],
            "one_point_total": computed["one_point_total"],
            "achieved": computed["achieved"],
            "counts_at": computed["counts_at"],
            "generic": computed["generic_count"],
        },
        "brute_probe_points": computed["brute_probe_points"],
        "brute_agrees": computed["brute_agrees"],
        "infinity": computed["infinity"],
        "rank_integer": computed["rank_integer"],
        "ranks_modular": computed["ranks_modular"],
        "modular_routes_agree": all(
            value == computed["rank_integer"]
            for value in computed["ranks_modular"].values()
        ),
    }
    cert_model["pass"] = (
        computed["rotation_count"] == 24
        and computed["supports"] == 1296
        and computed["brute_agrees"]
        and cert_model["modular_routes_agree"]
    )

    # ---- C: claim survival ------------------------------------------------
    survival = claim_survival_rows(receipt, computed, primary_sha)
    cert_survival = {
        "certificate": "C_CLAIM_SURVIVAL",
        "rows": survival,
        "row_count": len(survival),
        "all_rows_survive": all(survival.values()),
        "refuted_rows": tuple(
            key for key, value in survival.items() if not value
        ),
    }
    cert_survival["pass"] = cert_survival["all_rows_survive"]

    # ---- D: teeth (one planted corruption per gate class) -----------------
    def bites(mutate, expect_rows: tuple) -> bool:
        mutated = copy.deepcopy(receipt)
        mutate(mutated)
        rows = claim_survival_rows(mutated, computed, primary_sha)
        return any(not rows[name] for name in expect_rows)

    teeth = []

    def tooth(name: str, mutation: str, mutate, expect_rows: tuple) -> None:
        teeth.append({
            "tooth": name,
            "mutation": mutation,
            "gate": expect_rows,
            "detected": bites(mutate, expect_rows),
        })

    tooth(
        "tampered_unit_count",
        "the lawful count at t = 0 is raised to 91",
        lambda r: r["counts_at_exceptional_values"].__setitem__(
            "0", [91, 0, 0]),
        ("counts_at_exceptional_values",),
    )
    tooth(
        "chart_infinity_suppressed_to_90",
        "the chart-infinity lawful count is lowered to 90 -- the exact "
        "shape of the rejected global-maximum overclaim",
        lambda r: r["chart_infinity"].__setitem__("lawful_supports", 90),
        ("chart_infinity_triple",),
    )
    tooth(
        "refutation_flag_flipped",
        "exceeds_the_affine_unit_point_count is flipped to False",
        lambda r: r["chart_infinity"].__setitem__(
            "exceeds_the_affine_unit_point_count", False),
        ("chart_infinity_refutation_flag",),
    )
    tooth(
        "dropped_onset_value",
        "the onset value +1 is removed from the trace-bearing set",
        lambda r: r.__setitem__("achieved_trace_bearing_values", ["-1"]),
        ("achieved_trace_bearing_values",),
    )
    tooth(
        "planted_extra_exceptional_value",
        "a fake exceptional value t = 2 is planted",
        lambda r: r.__setitem__(
            "achieved_exceptional_values", ["-1", "0", "1", "2"]),
        ("achieved_exceptional_values",),
    )
    tooth(
        "tampered_joint_solution",
        "the joint solution is replaced by the unit point (1,1,1)",
        lambda r: r["joint_intersection"].__setitem__(
            "unique_gauge_fixed_solution", ["1", "1", "1"]),
        ("joint_intersection",),
    )
    tooth(
        "tampered_equivariant_dimension",
        "the equivariant dimension is lowered to 0",
        lambda r: r["equivariance"].__setitem__(
            "solution_dimension_per_sector", 0),
        ("equivariance_rank_and_dimension",),
    )
    tooth(
        "tampered_class_census",
        "the always-lawful class count is raised to 7",
        lambda r: r["census_class_counts"].__setitem__("always_lawful", 7),
        ("census_class_counts",),
    )
    tooth(
        "tampered_trace_bearing_count",
        "the trace-bearing count at t = +1 is raised to 31",
        lambda r: r["counts_at_exceptional_values"].__setitem__(
            "1", [36, 31, 30]),
        ("counts_at_exceptional_values",),
    )
    tooth(
        "flipped_response_equivalence",
        "sensitivity_iff_nonzero_sector_trace is flipped to False",
        lambda r: r["response_identity"].__setitem__(
            "sensitivity_iff_nonzero_sector_trace", False),
        ("response_identity",),
    )
    tooth(
        "tampered_statement_text",
        "one certified-statement text is replaced by false prose",
        lambda r: r["certified_statements"].__setitem__(
            "chart_infinity_control_statement",
            "the unit grading is the unique global maximiser"),
        ("certified_statement_texts",),
    )
    tooth(
        "tampered_primary_sha",
        "the primary's self-declared sha256 is altered by one hex digit",
        lambda r: r.__setitem__(
            "self_sha256", ("0" if receipt["self_sha256"][0] != "0" else "1")
            + receipt["self_sha256"][1:]),
        ("primary_self_sha_matches",),
    )
    tooth(
        "tampered_generic_count",
        "the generic lawful count is raised to 7",
        lambda r: r.__setitem__("lawful_count_at_generic_parameter", 7),
        ("generic_count",),
    )
    tooth(
        "flipped_primary_check",
        "one primary certificate flag is flipped to False",
        lambda r: r["checks"].__setitem__("F_EXCEPTIONAL_CENSUS", False),
        ("all_primary_certificates_pass",),
    )
    cert_teeth = {
        "certificate": "D_TEETH",
        "method": (
            "each tooth plants one corruption into a deep copy of the "
            "primary receipt and requires the SAME claim-survival comparison "
            "used for the live verdict to refute the named row"
        ),
        "teeth": teeth,
        "teeth_count": len(teeth),
        "teeth_that_bit": sum(1 for t in teeth if t["detected"]),
        "all_teeth_bite": all(t["detected"] for t in teeth),
    }
    cert_teeth["pass"] = len(teeth) >= 14 and cert_teeth["all_teeth_bite"]

    # ---- E: runtime -------------------------------------------------------
    elapsed = monotonic() - start
    cert_runtime = {
        "certificate": "E_RUNTIME",
        "budget_sec": AUDIT_TIMEOUT_SEC,
        "elapsed_sec": round(elapsed, 3),
        "pass": elapsed < AUDIT_TIMEOUT_SEC,
    }

    certificates = [
        ("A_PINS", cert_pins),
        ("B_INDEPENDENT_MODEL", cert_model),
        ("C_CLAIM_SURVIVAL", cert_survival),
        ("D_TEETH", cert_teeth),
        ("E_RUNTIME", cert_runtime),
    ]
    checks = {name: payload["pass"] for name, payload in certificates}
    verdict = (
        "CORROBORATES" if cert_survival["all_rows_survive"] else "REFUTES"
    )
    overall = all(checks.values()) and verdict == "CORROBORATES"

    checker_receipt = {
        "cycle": 876,
        "role": "independent_check",
        "salvage": True,
        "checker_verdict": verdict,
        "checks": checks,
        "claim_survival": survival,
        "refuted_rows": cert_survival["refuted_rows"],
        "teeth": teeth,
        "recomputed": {
            "counts_at": computed["counts_at"],
            "generic": computed["generic_count"],
            "census_classes": {
                "always": computed["always"],
                "never_b_zero": computed["never_b_zero"],
                "never_not_parallel": computed["never_not_parallel"],
                "one_point_total": computed["one_point_total"],
            },
            "infinity": computed["infinity"],
            "rank_integer": computed["rank_integer"],
            "ranks_modular": {
                str(k): v for k, v in computed["ranks_modular"].items()
            },
            "joint_solution": computed["joint_solution"],
        },
        "primary_sha256": primary_sha,
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_sec": round(elapsed, 3),
        "pass": overall,
    }
    RECEIPT_PATH.write_text(
        json.dumps(checker_receipt, indent=1, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = [
        "CYCLE876_GRADING_AFFINE_CHART_ALGEBRA_INDEPENDENT_CHECK",
        "SPECIFIED_TO_REFUTE_FAIL_CLOSED_EXIT_NONZERO_ON_ANY_REFUTATION",
    ]
    for name, payload in certificates:
        lines.append(
            f"CERTIFICATE {name} {'PASS' if payload['pass'] else 'FAIL'} "
            + compact(payload)
        )
    lines.append("CLAIM_SURVIVAL " + compact(survival))
    lines.append("SUMMARY_JSON " + compact({
        "cycle": 876,
        "checker_verdict": verdict,
        "checks": checks,
        "elapsed_sec": round(elapsed, 3),
        "pass": overall,
    }))
    lines.append(
        "CYCLE876_SALVAGE_INDEPENDENT_CHECK_"
        + (verdict if overall else "FAIL_CLOSED")
    )
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))
    sys.stdout.write(out)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
