#!/usr/bin/env python3
"""Cycle 872: exact-support classification of a stipulated response grammar.

The reviewed Cycle-868 package proved, as exact algebraic support on its own
stipulated surface, that its six stipulated response objects are blind to the
sector-trace grading sign sigma, and named as a boundary of that support
statement: a response object LINEAR in the endpoint exchange R -- not
factoring through R*R and not a sector-orthogonal contraction -- escapes its
structural sigma-evenness mechanism.  That boundary was named, not
classified.

This runner classifies it exactly INSIDE a stipulated constructor grammar.
Over the identical stipulated scope (same source family, same stipulated
traceless recoil ledger, same grading, all restated in-file), it declares a
constructor GRAMMAR as data -- the grading G_sigma, the endpoint exchange R,
rational linear combination, sector / endpoint / axis contraction and tensor
square -- enumerates every object the grammar generates at source degree one
and two, filters that class by two response-class covariance conditions
DECLARED AS DATA in this file (direction-reversal parity; endpoint-exchange
equivariance -- their well-posedness on the family is re-derived in-file, but
the conditions themselves are stipulations, not consequences of any axiom),
and asks of every survivor whether it separates sigma=+1 from sigma=-1 on the
declared family.  The classification is exhaustive over all declared members
under both declared conformally loaded probe ledgers; no sampled census
stands in for a declared-family claim.

Everything is scoped: the result is exact support on the stipulated grammar
only.  It does NOT establish that the grammar exhausts physically allowed
response objects, does NOT identify sigma with the physical conformal-mode
sign, and does NOT identify the stipulated objects with any unlanded response
lineage; those are open bridges carried in the note.  The six Cycle-868
stipulated objects are re-derived in-file and matched into the class so the
class demonstrably contains them; the escape-shaped objects are given an
operational test and cross-tabbed against their syntactic description; and an
off-grammar object that IS sigma-sensitive on the declared family is pushed
through the identical pipeline to prove the classifier can return the
opposite outcome.  Every decisive certificate gates the exact submitted
boundary and fails closed on any other outcome.

Both cited inputs (the reviewed Cycle-868 runner and its pinned stdout, at
their blobs landed on origin/main) are SHA-pinned text/AST evidence behind a
meta-path import firewall.  Arithmetic is exact: the source is pre-scaled by
three so the conformal projector stays integral, and every object is carried
as a univariate integer polynomial in the formal sigma.  No floating point
enters any certified quantity.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle868_response_sign_census_2026_07_28.py",
    "logs/runner-cache/frontier_cycle868_response_sign_census_2026_07_28.txt",
)

import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import product
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PYTHON_PATHS = tuple(path for path in AUDIT_INPUT_PATHS if path.endswith(".py"))
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in PYTHON_PATHS)
# Both pins are the blobs landed on origin/main after Cycle 868's review
# fixes (iterations 1 and 2).  The formerly pinned Cycle-320/322/768/812
# lineage is provenance-only, non-load-bearing context (the 768/812 stack is
# unlanded on origin/main); it is NOT an input of this runner, and every
# definition this classification depends on is stipulated in-file.
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "dca6b71b9dec65adbacff348e75085bf2c24fe96f621b949a4c8fb96f74cf89a",
    AUDIT_INPUT_PATHS[1]:
        "efb45439065ca7c92db20e29a1f261cfeaec71f96ae21d5774e617dfdc295c55",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c155a2dafaccde60c17047303c6de358445711c3",
    AUDIT_INPUT_PATHS[1]: "38a0ecf77aaef1b37d1c9fcca49bbd74edd40796",
}
REQUIRED_AST_MARKERS = {
    AUDIT_INPUT_PATHS[0]: (
        "adjoint_pullback", "census_certificate", "grading_operator",
        "response_objects", "stipulated_ledger", "verdict_certificate",
    ),
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited source-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# the exact submitted boundary: every decisive certificate gates these values,
# so any other scientific outcome -- a sensitive pair, a non-constant
# generator, a different census -- fails its certificate and exits nonzero.
# --------------------------------------------------------------------------
SUBMITTED_BOUNDARY = {
    "family_member_count": 1368,
    "generator_count": 384,
    "covariance_filtered_count": 344,
    "classified_pair_count": 1368 * 344,
    "sensitive_pairs": 0,
    "nonconstant_generators": 0,
    "random_algebra_elements_sensitive": 0,
    "escape_shaped_count": 180,
    "escape_shaped_sensitive_pairs_on_declared_family": 0,
    "max_sigma_degree_on_loaded_family": 4,
    "verdict": "OUTCOME_B_CONSTRUCTOR_ALGEBRA_BLIND_ESCAPE_B_SHAPED_BUT_VOID",
}

# --------------------------------------------------------------------------
# the declared scope: identical to the reviewed Cycle-868 stipulated surface,
# restated in-file as stipulations (nothing below is read from another file)
# --------------------------------------------------------------------------
SECTORS = ("matter", "field", "auxiliary")
SECTOR_COUNT = len(SECTORS)
AXES = 3
ENDPOINTS = ("LEFT", "RIGHT")
ENDPOINT_COUNT = len(ENDPOINTS)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_REVERSE = (1, 0, 3, 2, 5, 4)
HELD_EDGE_LENGTH = 6
WEIGHTS = tuple(range(1, HELD_EDGE_LENGTH + 1))
SCALE = SECTOR_COUNT  # every graded quantity times 3 stays an integer
INDEX_DIMENSION = {"e": ENDPOINT_COUNT, "s": SECTOR_COUNT, "a": AXES,
                   "b": AXES, "t": SECTOR_COUNT}


def stipulated_ledger(weight: int) -> tuple[int, int, int]:
    """The stipulated traceless recoil ledger (-2d, +d, +d), declared in-file."""
    return (-2 * weight, weight, weight)


def detuned_ledger(weight: int) -> tuple[int, int, int]:
    """OFF-SCOPE calibration ledger: sector sum +1, so the conformal load is on."""
    return (-2 * weight, weight, weight + 1)


def pure_conformal_ledger(weight: int) -> tuple[int, int, int]:
    """OFF-SCOPE calibration ledger: purely conformal, no trace-free part."""
    return (weight, weight, weight)


# --------------------------------------------------------------------------
# exact univariate integer polynomials in the formal conformal sign sigma
# --------------------------------------------------------------------------
Poly = tuple


def p_trim(values: list) -> Poly:
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


def p_const(value: int) -> Poly:
    return (value,) if value else ()


def p_add(left: Poly, right: Poly) -> Poly:
    if not left:
        return right
    if not right:
        return left
    if len(left) == 1 and len(right) == 1:
        total = left[0] + right[0]
        return (total,) if total else ()
    width = max(len(left), len(right))
    return p_trim([
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(width)
    ])


def p_sub(left: Poly, right: Poly) -> Poly:
    return p_add(left, p_scale(right, -1))


def p_scale(poly: Poly, factor: int) -> Poly:
    if factor == 0 or not poly:
        return ()
    return tuple(factor * value for value in poly)


def p_shift(poly: Poly, degree: int) -> Poly:
    return ((0,) * degree + poly) if poly else ()


def p_mul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return ()
    if len(left) == 1 and len(right) == 1:
        value = left[0] * right[0]
        return (value,) if value else ()
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            out[i + j] += a * b
    return p_trim(out)


def p_divide_exact(poly: Poly, divisor: int) -> Poly:
    out = []
    for value in poly:
        quotient, remainder = divmod(value, divisor)
        if remainder:
            raise AssertionError("conformal projection left a remainder")
        out.append(quotient)
    return p_trim(out)


def p_eval(poly: Poly, point: int) -> int:
    total = 0
    power = 1
    for value in poly:
        total += value * power
        power *= point
    return total


def p_odd_part_is_zero(poly: Poly) -> bool:
    return all(value == 0 for value in poly[1::2])


def p_degree(poly: Poly) -> int:
    return len(poly) - 1


def p_text(poly: Poly) -> str:
    return "0" if not poly else "+".join(
        f"{value}s^{index}" for index, value in enumerate(poly) if value
    )


# --------------------------------------------------------------------------
# the declared source family (identical stipulated scope, independent enumeration)
# --------------------------------------------------------------------------
def enumerate_family() -> tuple[tuple, ...]:
    members: list[tuple] = []
    for endpoint in range(ENDPOINT_COUNT):
        for direction in range(len(DIRECTIONS)):
            for weight in WEIGHTS:
                members.append(("k1", endpoint, direction, weight))
    for left_direction in range(len(DIRECTIONS)):
        for left_weight in WEIGHTS:
            for right_direction in range(len(DIRECTIONS)):
                for right_weight in WEIGHTS:
                    members.append(("k2", left_direction, left_weight,
                                    right_direction, right_weight))
    return tuple(members)


def member_sources(member: tuple) -> tuple[tuple[int, int, int], ...]:
    if member[0] == "k1":
        return ((member[1], member[2], member[3]),)
    return ((0, member[1], member[2]), (1, member[3], member[4]))


def reverse_member(member: tuple) -> tuple:
    """Reverse every carried direction through the stipulated reversal involution."""
    if member[0] == "k1":
        return ("k1", member[1], DIRECTION_REVERSE[member[2]], member[3])
    return ("k2", DIRECTION_REVERSE[member[1]], member[2],
            DIRECTION_REVERSE[member[3]], member[4])


def swap_member(member: tuple) -> tuple:
    """Exchange the two endpoints of the configuration."""
    if member[0] == "k1":
        return ("k1", ENDPOINT_COUNT - 1 - member[1], member[2], member[3])
    return ("k2", member[3], member[4], member[1], member[2])


def scaled_source(member: tuple, ledger=stipulated_ledger) -> tuple:
    """SCALE * S[endpoint][sector][axis] as exact integers."""
    grid = [[[0] * AXES for _sector in range(SECTOR_COUNT)]
            for _endpoint in range(ENDPOINT_COUNT)]
    for endpoint, direction, weight in member_sources(member):
        unit = DIRECTIONS[direction]
        for sector, coefficient in enumerate(ledger(weight)):
            for axis in range(AXES):
                grid[endpoint][sector][axis] += SCALE * coefficient * unit[axis]
    return tuple(tuple(tuple(row) for row in block) for block in grid)


def conformal_channel(scaled: tuple) -> tuple:
    """SCALE * (sector trace)/3 per endpoint and axis: the conformal channel."""
    return tuple(
        tuple(
            sum(block[sector][axis] for sector in range(SECTOR_COUNT)) // SCALE
            for axis in range(AXES)
        )
        for block in scaled
    )


def lift(scaled: tuple) -> tuple:
    return tuple(
        tuple(tuple(p_const(value) for value in row) for row in block)
        for block in scaled
    )


# --------------------------------------------------------------------------
# the stipulated constructors
# --------------------------------------------------------------------------
def grade(array: tuple, live: bool = True) -> tuple:
    """G_sigma = Pi_tracefree + sigma * Pi_conformal on the sector index.

    live=False is the adversary control: the conformal channel is carried at
    sigma-degree zero, which disables the probe and changes nothing else.
    """
    degree = 1 if live else 0
    out = []
    for endpoint in range(ENDPOINT_COUNT):
        conformal = tuple(
            p_divide_exact(
                p_add(p_add(array[endpoint][0][axis], array[endpoint][1][axis]),
                      array[endpoint][2][axis]),
                SECTOR_COUNT,
            )
            for axis in range(AXES)
        )
        block = []
        for sector in range(SECTOR_COUNT):
            block.append(tuple(
                p_add(p_sub(array[endpoint][sector][axis], conformal[axis]),
                      p_shift(conformal[axis], degree))
                for axis in range(AXES)
            ))
        out.append(tuple(block))
    return tuple(out)


def grade_tracefree_channel(array: tuple) -> tuple:
    """OFF-GRAMMAR grading: sigma multiplies the TRACE-FREE channel instead.

    This violates the declared grammar -- the lineage fixes the graded channel
    to be the conformal one -- and exists only as the planted adversary that
    proves the classifier can return a sigma-sensitive verdict.
    """
    out = []
    for endpoint in range(ENDPOINT_COUNT):
        conformal = tuple(
            p_divide_exact(
                p_add(p_add(array[endpoint][0][axis], array[endpoint][1][axis]),
                      array[endpoint][2][axis]),
                SECTOR_COUNT,
            )
            for axis in range(AXES)
        )
        block = []
        for sector in range(SECTOR_COUNT):
            block.append(tuple(
                p_add(
                    p_shift(p_sub(array[endpoint][sector][axis],
                                  conformal[axis]), 1),
                    conformal[axis],
                )
                for axis in range(AXES)
            ))
        out.append(tuple(block))
    return tuple(out)


def apply_identity(array: tuple) -> tuple:
    return array


def apply_exchange(array: tuple) -> tuple:
    return tuple(array[ENDPOINT_COUNT - 1 - endpoint]
                 for endpoint in range(ENDPOINT_COUNT))


def apply_symmetric(array: tuple) -> tuple:
    swapped = apply_exchange(array)
    return tuple(
        tuple(tuple(p_add(array[e][s][a], swapped[e][s][a]) for a in range(AXES))
              for s in range(SECTOR_COUNT))
        for e in range(ENDPOINT_COUNT)
    )


def apply_antisymmetric(array: tuple) -> tuple:
    swapped = apply_exchange(array)
    return tuple(
        tuple(tuple(p_sub(array[e][s][a], swapped[e][s][a]) for a in range(AXES))
              for s in range(SECTOR_COUNT))
        for e in range(ENDPOINT_COUNT)
    )


PREMAPS = (
    ("id", apply_identity, "identity"),
    ("R", apply_exchange, "endpoint exchange R"),
    ("I+R", apply_symmetric, "linear combination I+R"),
    ("I-R", apply_antisymmetric, "linear combination I-R"),
)
GRADE_POWERS = (1, 2)
PRE_KEYS = tuple((name, power) for power in GRADE_POWERS
                 for name, _fn, _doc in PREMAPS)

CONTRACTIONS = (
    ("none", ()),
    ("sector", ("s",)),
    ("endpoint", ("e",)),
    ("axis", ("a",)),
    ("endpoint.sector", ("e", "s")),
    ("sector.axis", ("s", "a")),
    ("endpoint.axis", ("e", "a")),
    ("endpoint.sector.axis", ("e", "s", "a")),
)


def contract(array: tuple, killed: tuple) -> tuple[tuple, tuple]:
    keep = tuple(name for name in ("e", "s", "a") if name not in killed)
    out = []
    for index in product(*[range(INDEX_DIMENSION[name]) for name in keep]):
        position = dict(zip(keep, index))
        endpoints = ((position["e"],) if "e" in position
                     else range(ENDPOINT_COUNT))
        sectors = (position["s"],) if "s" in position else range(SECTOR_COUNT)
        axes = (position["a"],) if "a" in position else range(AXES)
        total: Poly = ()
        for e in endpoints:
            for s in sectors:
                for a in axes:
                    total = p_add(total, array[e][s][a])
        out.append(total)
    return tuple(out), keep


def pair_gram(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    total: Poly = ()
    for e in range(ENDPOINT_COUNT):
        for s in range(SECTOR_COUNT):
            for a in range(AXES):
                total = p_add(total, p_mul(left[e][s][a], right[e][s][a]))
    return (total,), ()


def pair_sector_contract(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    out = []
    for e in range(ENDPOINT_COUNT):
        for a in range(AXES):
            for b in range(AXES):
                entry: Poly = ()
                for s in range(SECTOR_COUNT):
                    entry = p_add(entry, p_mul(left[e][s][a], right[e][s][b]))
                out.append(entry)
    return tuple(out), ("e", "a", "b")


def pair_axis_contract(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    out = []
    for e in range(ENDPOINT_COUNT):
        for s in range(SECTOR_COUNT):
            for t in range(SECTOR_COUNT):
                entry: Poly = ()
                for a in range(AXES):
                    entry = p_add(entry, p_mul(left[e][s][a], right[e][t][a]))
                out.append(entry)
    return tuple(out), ("e", "s", "t")


def pair_endpoint_transfer(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    total: Poly = ()
    for s in range(SECTOR_COUNT):
        for a in range(AXES):
            total = p_add(total, p_mul(left[0][s][a], right[1][s][a]))
    return (total,), ()


def pair_sector_trace_square(left: tuple, right: tuple) -> tuple[tuple, tuple]:
    out = []
    for e in range(ENDPOINT_COUNT):
        for a in range(AXES):
            left_trace: Poly = ()
            right_trace: Poly = ()
            for s in range(SECTOR_COUNT):
                left_trace = p_add(left_trace, left[e][s][a])
                right_trace = p_add(right_trace, right[e][s][a])
            out.append(p_mul(left_trace, right_trace))
    return tuple(out), ("e", "a")


PAIRINGS = (
    ("gram", pair_gram, "sum over all indices of the tensor square"),
    ("sector_contract", pair_sector_contract, "contract the sector index"),
    ("axis_contract", pair_axis_contract, "contract the axis index"),
    ("endpoint_transfer", pair_endpoint_transfer,
     "contract LEFT against RIGHT across the held edge"),
    ("sector_trace_square", pair_sector_trace_square,
     "product of the two sector traces"),
)


GRAMMAR = {
    "state": "S[endpoint][sector][axis], the stipulated recoil source, "
             "pre-scaled by 3",
    "generators": {
        "G_sigma": "grading: Pi_tracefree + sigma * Pi_conformal on the sector index",
        "R": "endpoint exchange, the LEFT/RIGHT reversal involution",
        "linear_combination": "rational combinations of endpoint-space operators",
        "sector_contraction": "sum over the sector index",
        "endpoint_contraction": "sum over the endpoint index",
        "axis_contraction": "sum over the axis index",
        "tensor_square": "bilinear pairing of two constructed copies",
    },
    "productions": (
        "PRE   ::= P o G_sigma^m applied to S,   P in {id,R,I+R,I-R}, m in {1,2}",
        "LIN   ::= C(PRE),   C any subset-contraction of {endpoint,sector,axis}",
        "QUAD  ::= B(PRE_1, PRE_2),   B in {gram, sector_contract, axis_contract, "
        "endpoint_transfer, sector_trace_square}",
        "CLASS ::= LIN | QUAD, then closed under rational linear combination and "
        "product (the generated algebra)",
    ),
    "source_degree_bound": 2,
    "grade_power_bound": 2,
    "admissibility_constraints": (
        "direction-reversal parity (working label K1): reversing every carried "
        "direction sends S to -S, so a surviving object must carry definite "
        "parity (-1)^degree; degree-mixed combinations are filtered out",
        "endpoint-exchange equivariance (working label K2): exchanging the two "
        "endpoints of the configuration sends S to R S, so a surviving object "
        "must satisfy F(swap m) = eps * pi(F(m)) with eps in {+1,-1} fixed and "
        "pi the reversal of the object's own surviving endpoint index",
    ),
    "label_convention": (
        "every use of 'admissible'/'admissibility' in this runner's payload "
        "keys and text abbreviates 'satisfying the two stipulated response-"
        "class covariance filters above (direction-reversal parity; endpoint-"
        "exchange equivariance), both DECLARED AS DATA in this file'. The term "
        "is a working label of this package only: it does not invoke, is not "
        "derived from, and asserts nothing about the framework Admissibility "
        "axiom, and no theorem is claimed that these two filters characterize "
        "physically permitted response objects"
    ),
}


def class_readings(scaled: tuple, live: bool = True,
                   grade_fn=None) -> dict[tuple, tuple]:
    """Every generator of the declared class, evaluated on one source."""
    grader = grade_fn or (lambda arr: grade(arr, live))
    base = lift(scaled)
    graded = {}
    current = base
    for power in range(1, max(GRADE_POWERS) + 1):
        current = grader(current)
        graded[power] = current
    pre = {}
    for power in GRADE_POWERS:
        for name, function, _doc in PREMAPS:
            pre[(name, power)] = function(graded[power])
    readings: dict[tuple, tuple] = {}
    for key in PRE_KEYS:
        array = pre[key]
        for label, killed in CONTRACTIONS:
            values, layout = contract(array, killed)
            readings[("L", key[0], key[1], label)] = (values, layout)
    for left_key in PRE_KEYS:
        for right_key in PRE_KEYS:
            for label, function, _doc in PAIRINGS:
                values, layout = function(pre[left_key], pre[right_key])
                readings[("Q", left_key, right_key, label)] = (values, layout)
    return readings


GENERATOR_IDS = tuple(
    [("L", key[0], key[1], label) for key in PRE_KEYS
     for label, _killed in CONTRACTIONS]
    + [("Q", left, right, label) for left in PRE_KEYS for right in PRE_KEYS
       for label, _fn, _doc in PAIRINGS]
)
GENERATOR_DEGREE = {gid: (1 if gid[0] == "L" else 2) for gid in GENERATOR_IDS}


def endpoint_reversal_map(layout: tuple) -> tuple:
    """Positions of the flattened reading under reversal of the endpoint index."""
    sizes = [INDEX_DIMENSION[name] for name in layout]
    total = 1
    for size in sizes:
        total *= size
    if "e" not in layout:
        return tuple(range(total))
    slot = layout.index("e")
    mapping = []
    for flat in range(total):
        digits = []
        rest = flat
        for size in reversed(sizes):
            rest, digit = divmod(rest, size)
            digits.append(digit)
        digits.reverse()
        digits[slot] = ENDPOINT_COUNT - 1 - digits[slot]
        value = 0
        for digit, size in zip(digits, sizes):
            value = value * size + digit
        mapping.append(value)
    return tuple(mapping)


LAYOUTS = {}
_PROBE_READINGS = class_readings(scaled_source(("k2", 0, 1, 2, 3)))
for _gid, (_values, _layout) in _PROBE_READINGS.items():
    LAYOUTS[_gid] = _layout
REVERSAL_MAPS = {gid: endpoint_reversal_map(LAYOUTS[gid]) for gid in GENERATOR_IDS}
GENERATOR_ARITY = {gid: len(_PROBE_READINGS[gid][0]) for gid in GENERATOR_IDS}


# --------------------------------------------------------------------------
# serialisation helpers
# --------------------------------------------------------------------------
def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def gid_text(gid: tuple) -> str:
    if gid[0] == "L":
        return f"LIN[{gid[1]}|G^{gid[2]}|{gid[3]}]"
    return (f"QUAD[{gid[1][0]}|G^{gid[1][1]}] x "
            f"[{gid[2][0]}|G^{gid[2][1]}] :: {gid[3]}")


# --------------------------------------------------------------------------
# certificate A -- the declared constructor grammar, as data
# --------------------------------------------------------------------------
def grammar_certificate() -> dict[str, object]:
    linear_closed_form = len(PRE_KEYS) * len(CONTRACTIONS)
    quadratic_closed_form = len(PRE_KEYS) ** 2 * len(PAIRINGS)
    arity_rows = tuple(
        {"contraction": label,
         "arity": len(contract(lift(scaled_source(("k1", 0, 0, 1))), killed)[0])}
        for label, killed in CONTRACTIONS
    )
    contraction_arity_sum = sum(row["arity"] for row in arity_rows)
    pairing_rows = tuple(
        {"pairing": label, "arity": GENERATOR_ARITY[("Q", PRE_KEYS[0],
                                                     PRE_KEYS[0], label)],
         "layout": LAYOUTS[("Q", PRE_KEYS[0], PRE_KEYS[0], label)]}
        for label, _fn, _doc in PAIRINGS
    )
    result = {
        "grammar": GRAMMAR,
        "premaps": tuple((name, doc) for name, _fn, doc in PREMAPS),
        "grade_powers": GRADE_POWERS,
        "contractions": tuple(label for label, _killed in CONTRACTIONS),
        "contraction_arities": arity_rows,
        "contraction_arity_sum": contraction_arity_sum,
        "pairings": tuple((label, doc) for label, _fn, doc in PAIRINGS),
        "pairing_arities": pairing_rows,
        "linear_generator_count": sum(1 for gid in GENERATOR_IDS if gid[0] == "L"),
        "quadratic_generator_count": sum(1 for gid in GENERATOR_IDS if gid[0] == "Q"),
        "linear_closed_form": linear_closed_form,
        "quadratic_closed_form": quadratic_closed_form,
        "generator_count": len(GENERATOR_IDS),
        "closed_form_equation": "(4 premaps * 2 grades) * 8 contractions + "
                                "(4*2)^2 pre-pairs * 5 pairings",
        "generator_ids_are_distinct": len(set(GENERATOR_IDS)) == len(GENERATOR_IDS),
        "total_scalar_components": sum(GENERATOR_ARITY.values()),
        "grammar_digest": digest(GRAMMAR),
        "finding": (
            f"The constructor grammar is declared as data and generates a "
            f"finite class: {len(PRE_KEYS)} pre-states (four endpoint-space "
            f"combinations of the identity and the exchange, each at grading "
            f"power one or two), {len(CONTRACTIONS)} index-subset contractions "
            f"and {len(PAIRINGS)} tensor-square pairings, for "
            f"{linear_closed_form} objects linear in the graded source and "
            f"{quadratic_closed_form} quadratic ones, "
            f"{len(GENERATOR_IDS)} generators in total carrying "
            f"{sum(GENERATOR_ARITY.values())} scalar components. The class is "
            f"then closed under rational linear combination and product, so "
            f"what is classified is the generated algebra and not merely the "
            f"generator list."
        ),
    }
    result["pass"] = (
        result["linear_generator_count"] == linear_closed_form
        and result["quadratic_generator_count"] == quadratic_closed_form
        and result["generator_count"] == linear_closed_form + quadratic_closed_form
        and result["generator_ids_are_distinct"]
        and contraction_arity_sum == 48
        and all(row["arity"] > 0 for row in arity_rows)
    )
    return result


# --------------------------------------------------------------------------
# certificate B -- the stipulated covariance filters, shown well posed
# --------------------------------------------------------------------------
def lineage_certificate(members: tuple) -> dict[str, object]:
    reverse_involution = all(
        DIRECTION_REVERSE[DIRECTION_REVERSE[i]] == i
        for i in range(len(DIRECTIONS))
    )
    reverse_negates = all(
        tuple(-c for c in DIRECTIONS[i]) == DIRECTIONS[DIRECTION_REVERSE[i]]
        for i in range(len(DIRECTIONS))
    )
    reverse_free = all(DIRECTION_REVERSE[i] != i for i in range(len(DIRECTIONS)))
    reversal_negates_source = True
    swap_exchanges_source = True
    conformal_zero_members = 0
    reverse_closes_family = True
    swap_closes_family = True
    member_set = set(members)
    for member in members:
        scaled = scaled_source(member)
        reversed_scaled = scaled_source(reverse_member(member))
        swapped_scaled = scaled_source(swap_member(member))
        if reverse_member(member) not in member_set:
            reverse_closes_family = False
        if swap_member(member) not in member_set:
            swap_closes_family = False
        for e in range(ENDPOINT_COUNT):
            for s in range(SECTOR_COUNT):
                for a in range(AXES):
                    if reversed_scaled[e][s][a] != -scaled[e][s][a]:
                        reversal_negates_source = False
                    if swapped_scaled[e][s][a] != \
                            scaled[ENDPOINT_COUNT - 1 - e][s][a]:
                        swap_exchanges_source = False
        channel = conformal_channel(scaled)
        if any(value for block in channel for value in block):
            conformal_zero_members += 1
    # the weight ladder d = 1..6 is a truncation; close it symbolically
    symbolic = (p_shift(p_const(-2), 1), p_shift(p_const(1), 1),
                p_shift(p_const(1), 1))
    symbolic_sum = p_add(p_add(symbolic[0], symbolic[1]), symbolic[2])
    exchange_is_involution = True
    probe = lift(scaled_source(("k2", 3, 5, 1, 2), ledger=detuned_ledger))
    if apply_exchange(apply_exchange(probe)) != probe:
        exchange_is_involution = False
    result = {
        "direction_reversal_parity_K1": (
            "the stipulated reversal permutation is a fixed-point-free "
            "involution that negates every direction vector, and the source is "
            "linear in the carried direction, so reversing a configuration "
            "sends S to -S; the parity FILTER built on this fact is a declared "
            "response-class condition, not an axiom consequence"
        ),
        "reverse_is_involution": reverse_involution,
        "reverse_is_fixed_point_free": reverse_free,
        "reverse_negates_direction": reverse_negates,
        "reversal_negates_source_on_every_member": reversal_negates_source,
        "reversal_closes_the_family": reverse_closes_family,
        "endpoint_exchange_equivariance_K2": (
            "exchanging the two endpoints of a configuration acts on the source "
            "exactly as the exchange operator R, and R is an involution; the "
            "equivariance FILTER built on this fact is a declared response-"
            "class condition, not an axiom consequence"
        ),
        "swap_acts_as_exchange_on_every_member": swap_exchanges_source,
        "swap_closes_the_family": swap_closes_family,
        "exchange_is_involution": exchange_is_involution,
        "declared_family_conformal_nonzero_members": conformal_zero_members,
        "family_member_count": len(members),
        "symbolic_ledger_in_d": tuple(p_text(poly) for poly in symbolic),
        "symbolic_ledger_sector_sum": p_text(symbolic_sum),
        "symbolic_sector_sum_is_zero_polynomial": symbolic_sum == (),
        "finding": (
            f"The two stipulated covariance filters are shown WELL POSED here "
            f"(their content stays declared data). Reversing every carried "
            f"direction negates the source on "
            + ("every one" if reversal_negates_source else "NOT every one")
            + f" of the {len(members)} family members, and the reversal keeps "
            f"the family closed, so parity under reversal is a well posed "
            f"requirement. Exchanging the endpoints of a configuration acts on "
            f"the source exactly as the exchange operator on "
            + ("every member" if swap_exchanges_source else "NOT every member")
            + ", and the exchange squares to the identity, so equivariance is "
            f"well posed too. Carrying the weight as a formal indeterminate "
            f"makes the ledger's sector sum "
            + ("the zero polynomial, so the conformal channel of a stipulated "
               "source vanishes at every weight and not merely the six swept"
               if symbolic_sum == () else
               f"the nonzero polynomial {p_text(symbolic_sum)}")
            + f"; {conformal_zero_members} of {len(members)} declared members "
            f"carry a nonzero conformal channel."
        ),
    }
    result["pass"] = (
        reverse_involution and reverse_free and reverse_negates
        and reversal_negates_source and swap_exchanges_source
        and reverse_closes_family and swap_closes_family
        and exchange_is_involution
        # decisive: the sector sum must BE the zero polynomial (the previous
        # isinstance() gate was fail-open) and no declared member may carry a
        # conformal channel -- both are load-bearing for the blindness claim
        and symbolic_sum == ()
        and conformal_zero_members == 0
        and len(members) == SUBMITTED_BOUNDARY["family_member_count"]
    )
    return result


# --------------------------------------------------------------------------
# certificate C -- containment of the six Cycle-868 stipulated objects
# --------------------------------------------------------------------------
def cycle868_stipulated_objects(scaled: tuple) -> dict[str, tuple]:
    """The six Cycle-868 stipulated response objects, re-derived in-file."""
    graded = grade(lift(scaled))
    pushed = apply_exchange(graded)
    pulled = grade(apply_exchange(apply_exchange(graded)))
    o1 = tuple(pushed[e][s][a] for e in range(ENDPOINT_COUNT)
               for s in range(SECTOR_COUNT) for a in range(AXES))
    o2 = tuple(pulled[e][s][a] for e in range(ENDPOINT_COUNT)
               for s in range(SECTOR_COUNT) for a in range(AXES))
    o3 = tuple(
        p_add(p_add(pushed[e][0][a], pushed[e][1][a]), pushed[e][2][a])
        for e in range(ENDPOINT_COUNT) for a in range(AXES)
    )
    gram: Poly = ()
    for value in o1:
        gram = p_add(gram, p_mul(value, value))
    o5 = []
    for e in range(ENDPOINT_COUNT):
        for left in range(AXES):
            for right in range(AXES):
                entry: Poly = ()
                for s in range(SECTOR_COUNT):
                    entry = p_add(entry, p_mul(pushed[e][s][left],
                                               pushed[e][s][right]))
                o5.append(entry)
    transfer: Poly = ()
    for s in range(SECTOR_COUNT):
        for a in range(AXES):
            transfer = p_add(transfer, p_mul(graded[0][s][a], graded[1][s][a]))
    return {
        "O1_PUSHFORWARD": o1,
        "O2_ADJOINT_PULLBACK": o2,
        "O3_FLUX_BALANCE": o3,
        "O4_RESPONSE_GRAM": (gram,),
        "O5_RESPONSE_TENSOR": tuple(o5),
        "O6_EDGE_TRANSFER": (transfer,),
    }


CLAIMED_EMBEDDING = {
    "O1_PUSHFORWARD": ("L", "R", 1, "none"),
    "O2_ADJOINT_PULLBACK": ("L", "id", 2, "none"),
    "O3_FLUX_BALANCE": ("L", "R", 1, "sector"),
    "O4_RESPONSE_GRAM": ("Q", ("R", 1), ("R", 1), "gram"),
    "O5_RESPONSE_TENSOR": ("Q", ("R", 1), ("R", 1), "sector_contract"),
    "O6_EDGE_TRANSFER": ("Q", ("id", 1), ("id", 1), "endpoint_transfer"),
}


def containment_certificate(members: tuple) -> dict[str, object]:
    probe_members = members[:24] + members[-24:] + (
        ("k2", 0, 1, 2, 3), ("k1", 1, 4, 5),
    )
    rows = []
    all_match = True
    for name, gid in sorted(CLAIMED_EMBEDDING.items()):
        matches = True
        for member in probe_members:
            for ledger in (stipulated_ledger, detuned_ledger, pure_conformal_ledger):
                scaled = scaled_source(member, ledger)
                reference = cycle868_stipulated_objects(scaled)[name]
                mine = class_readings(scaled)[gid][0]
                if tuple(reference) != tuple(mine):
                    matches = False
        all_match = all_match and matches
        rows.append({
            "cycle868_object": name,
            "class_generator": gid_text(gid),
            "arity": GENERATOR_ARITY[gid],
            "reproduced_exactly": matches,
        })
    result = {
        "embedding_rows": tuple(rows),
        "probe_member_count": len(probe_members),
        "probe_ledgers": ("stipulated", "detuned_OFF_SCOPE", "pure_conformal_OFF_SCOPE"),
        "all_six_stipulated_868_objects_are_class_members": all_match,
        "finding": (
            f"The six response objects stipulated by the reviewed Cycle-868 "
            f"package are re-derived in-file and matched component-for-"
            f"component against named members of the declared class over "
            f"{len(probe_members)} configurations under three ledgers "
            f"including two off-scope conformally loaded ones. "
            + ("All six reproduce exactly, so the stipulated class CONTAINS "
               "the six stipulated objects and the classification proved over "
               "the class applies to them at this stipulated scope. Nothing "
               "more is inherited: the reviewed Cycle-868 result remains exact "
               "support with its own open identifications, which this package "
               "carries forward unchanged."
               if all_match else
               "At least one object FAILED to reproduce, so the class does not "
               "contain the six stipulated objects and no containment may be "
               "claimed.")
        ),
    }
    result["pass"] = all_match and len(rows) == 6
    return result


# --------------------------------------------------------------------------
# certificate D -- the stipulated covariance filter (working label: admissible)
# --------------------------------------------------------------------------
def admissibility_certificate(members: tuple) -> tuple[tuple, dict[str, object]]:
    parity_ok = {gid: True for gid in GENERATOR_IDS}
    equivariance_sign = {gid: {1, -1} for gid in GENERATOR_IDS}
    for member in members:
        base = class_readings(scaled_source(member))
        reversed_reading = class_readings(scaled_source(reverse_member(member)))
        swapped_reading = class_readings(scaled_source(swap_member(member)))
        for gid in GENERATOR_IDS:
            degree = GENERATOR_DEGREE[gid]
            expected = tuple(
                p_scale(poly, (-1) ** degree) for poly in base[gid][0]
            )
            if tuple(reversed_reading[gid][0]) != expected:
                parity_ok[gid] = False
            mapping = REVERSAL_MAPS[gid]
            permuted = tuple(base[gid][0][mapping[i]]
                             for i in range(len(mapping)))
            survivors = set()
            for eps in equivariance_sign[gid]:
                if tuple(swapped_reading[gid][0]) == tuple(
                        p_scale(poly, eps) for poly in permuted):
                    survivors.add(eps)
            equivariance_sign[gid] = survivors
    admissible = tuple(
        gid for gid in GENERATOR_IDS
        if parity_ok[gid] and equivariance_sign[gid]
    )
    inadmissible = tuple(gid for gid in GENERATOR_IDS if gid not in set(admissible))
    # the K1 filter must have teeth: a degree-mixed object must be rejected
    mixed_rejected = 0
    mixed_tested = 0
    for member in members[:200]:
        base = class_readings(scaled_source(member))
        rev = class_readings(scaled_source(reverse_member(member)))
        linear_value = base[("L", "R", 1, "none")][0][0]
        quadratic_value = base[("Q", ("R", 1), ("R", 1), "gram")][0][0]
        mixed = p_add(linear_value, quadratic_value)
        mixed_reversed = p_add(rev[("L", "R", 1, "none")][0][0],
                               rev[("Q", ("R", 1), ("R", 1), "gram")][0][0])
        mixed_tested += 1
        if mixed_reversed != mixed and mixed_reversed != p_scale(mixed, -1):
            mixed_rejected += 1
    result = {
        "constraint_set": GRAMMAR["admissibility_constraints"],
        "generators_tested": len(GENERATOR_IDS),
        "members_swept": len(members),
        "K1_parity_failures": sum(1 for gid in GENERATOR_IDS if not parity_ok[gid]),
        "K2_equivariance_failures": sum(
            1 for gid in GENERATOR_IDS if not equivariance_sign[gid]
        ),
        "K2_sign_census": {
            "eps_plus_only": sum(1 for gid in GENERATOR_IDS
                                 if equivariance_sign[gid] == {1}),
            "eps_minus_only": sum(1 for gid in GENERATOR_IDS
                                  if equivariance_sign[gid] == {-1}),
            "eps_both": sum(1 for gid in GENERATOR_IDS
                            if equivariance_sign[gid] == {1, -1}),
            "eps_none": sum(1 for gid in GENERATOR_IDS
                            if not equivariance_sign[gid]),
        },
        "admissible_count": len(admissible),
        "inadmissible_count": len(inadmissible),
        "inadmissible_sample": tuple(gid_text(gid) for gid in inadmissible[:24]),
        "degree_mixed_probe": "LIN[R|G^1|none][0] + QUAD[R|G^1]x[R|G^1]::gram",
        "degree_mixed_tested": mixed_tested,
        "degree_mixed_rejected_by_K1": mixed_rejected,
        "K1_filter_has_teeth": mixed_rejected > 0,
        "admissible_digest": digest(tuple(gid_text(gid) for gid in admissible)),
        "finding": (
            f"Every one of the {len(GENERATOR_IDS)} generators was tested "
            f"against both stipulated covariance filters on all {len(members)} "
            f"family members. "
            f"{sum(1 for gid in GENERATOR_IDS if not parity_ok[gid])} "
            f"failed direction-reversal parity and "
            f"{sum(1 for gid in GENERATOR_IDS if not equivariance_sign[gid])} "
            f"failed endpoint-exchange equivariance, leaving "
            f"{len(admissible)} admissible objects. The parity constraint is "
            f"not vacuous: an explicitly degree-mixed combination of an "
            f"admissible linear object and an admissible quadratic one was "
            f"rejected on {mixed_rejected} of {mixed_tested} tested members, so "
            f"K1 does real work by forcing homogeneity."
        ),
    }
    result["pass"] = (
        len(admissible) + len(inadmissible) == len(GENERATOR_IDS)
        and not (set(admissible) & set(inadmissible))
        and mixed_tested > 0
        and all(
            equivariance_sign[gid] <= {1, -1} for gid in GENERATOR_IDS
        )
        # decisive: the parity filter must demonstrably reject a degree-mixed
        # object, and the filtered census must equal the submitted boundary
        and mixed_rejected > 0
        and len(GENERATOR_IDS) == SUBMITTED_BOUNDARY["generator_count"]
        and len(admissible) == SUBMITTED_BOUNDARY["covariance_filtered_count"]
    )
    return admissible, result


# --------------------------------------------------------------------------
# certificate E -- the exhaustive classification on the declared family
# --------------------------------------------------------------------------
def classify(members: tuple, admissible: tuple, ledger=stipulated_ledger,
             live: bool = True, grade_fn=None) -> dict[str, object]:
    sensitive_pairs = 0
    blind_pairs = 0
    disagreements = 0
    degree_census = {}
    sensitive_generators = set()
    nonconstant_generators = set()
    stream = sha256()
    for member in members:
        scaled = scaled_source(member, ledger)
        readings = class_readings(scaled, live=live, grade_fn=grade_fn)
        for gid in admissible:
            values = readings[gid][0]
            plus = tuple(p_eval(poly, 1) for poly in values)
            minus = tuple(p_eval(poly, -1) for poly in values)
            by_evaluation = plus != minus
            by_odd_part = not all(p_odd_part_is_zero(poly) for poly in values)
            if by_evaluation != by_odd_part:
                disagreements += 1
            if by_evaluation:
                sensitive_pairs += 1
                sensitive_generators.add(gid)
            else:
                blind_pairs += 1
            top = max((p_degree(poly) for poly in values if poly), default=-1)
            degree_census[top] = degree_census.get(top, 0) + 1
            if top > 0:
                nonconstant_generators.add(gid)
            stream.update(compact({
                "m": member, "g": gid, "p": plus, "n": minus,
                "s": by_evaluation, "d": top,
            }).encode())
    return {
        "member_count": len(members),
        "generator_count": len(admissible),
        "pair_count": len(members) * len(admissible),
        "sensitive_pairs": sensitive_pairs,
        "blind_pairs": blind_pairs,
        "sensitive_generator_count": len(sensitive_generators),
        "sensitive_generator_sample": tuple(
            sorted(gid_text(gid) for gid in sensitive_generators)[:16]
        ),
        "sigma_degree_census": {str(key): value
                                for key, value in sorted(degree_census.items())},
        "nonconstant_generator_count": len(nonconstant_generators),
        "two_tests_disagreements": disagreements,
        "stream_sha256": stream.hexdigest(),
    }


def declared_family_certificate(census: dict[str, object]) -> dict[str, object]:
    result = {
        **census,
        "test_definition": (
            "an object is sigma-SENSITIVE on a member when its exact reading at "
            "sigma=+1 differs from its reading at sigma=-1; the same call also "
            "computes sensitivity a second way, as a nonvanishing odd part of "
            "the sigma polynomial, and the two are cross-checked pair by pair"
        ),
        "partition_exact": (
            census["sensitive_pairs"] + census["blind_pairs"]
            == census["pair_count"]
        ),
        "cross_check_clean": census["two_tests_disagreements"] == 0,
        "all_readings_constant_in_sigma": census["nonconstant_generator_count"] == 0,
        "scale_convention": (
            "the source is pre-scaled by 3 so the conformal projector stays "
            "integral; the scale is one fixed nonzero rational per homogeneous "
            "degree and equality of two readings is invariant under it"
        ),
        "finding": (
            f"Every covariance-filtered object in the class was evaluated on "
            f"every member of the complete declared source family: "
            f"{census['pair_count']} exact (member, object) pairs. "
            f"{census['sensitive_pairs']} separate sigma=+1 from sigma=-1 and "
            f"{census['blind_pairs']} do not. The sigma-degree census over "
            f"those pairs is {compact(census['sigma_degree_census'])}, and "
            f"{census['nonconstant_generator_count']} generators carry any "
            f"sigma dependence at all on the declared family. The two "
            f"independent sensitivity tests -- evaluation at the two signs, and "
            f"the odd part of the polynomial -- disagreed on "
            f"{census['two_tests_disagreements']} pairs."
        ),
    }
    result["pass"] = (
        result["partition_exact"]
        and result["cross_check_clean"]
        and census["pair_count"] == census["member_count"] * census["generator_count"]
        # decisive: the submitted theorem outcome itself is gated -- any
        # sensitive pair or non-constant reading fails this certificate
        and census["sensitive_pairs"] == SUBMITTED_BOUNDARY["sensitive_pairs"]
        and census["nonconstant_generator_count"]
        == SUBMITTED_BOUNDARY["nonconstant_generators"]
        and result["all_readings_constant_in_sigma"]
        and census["member_count"] == SUBMITTED_BOUNDARY["family_member_count"]
        and census["generator_count"]
        == SUBMITTED_BOUNDARY["covariance_filtered_count"]
        and census["pair_count"] == SUBMITTED_BOUNDARY["classified_pair_count"]
    )
    return result


# --------------------------------------------------------------------------
# certificate F -- closure of the blindness statement to the generated algebra
# --------------------------------------------------------------------------
def closure_certificate(members: tuple, admissible: tuple,
                        census: dict[str, object]) -> dict[str, object]:
    rng = random.Random(87_201)
    ring_tests = 0
    ring_ok = True
    for _trial in range(400):
        left = p_const(rng.randint(-40, 40))
        right = p_const(rng.randint(-40, 40))
        ring_tests += 1
        if p_degree(p_add(left, right)) > 0 or p_degree(p_mul(left, right)) > 0:
            ring_ok = False
        if p_degree(p_scale(left, rng.randint(-9, 9))) > 0:
            ring_ok = False
    graded_ring_ok = True
    for _trial in range(200):
        left = (rng.randint(-9, 9), rng.randint(-9, 9))
        right = (rng.randint(-9, 9), rng.randint(-9, 9))
        product_poly = p_mul(p_trim(list(left)), p_trim(list(right)))
        if product_poly and p_degree(product_poly) > 2:
            graded_ring_ok = False
    sample_members = [members[rng.randrange(len(members))] for _ in range(48)]
    component_index = []
    for gid in admissible:
        for slot in range(GENERATOR_ARITY[gid]):
            component_index.append((gid, slot))
    element_count = 0
    element_nonconstant = 0
    element_sensitive = 0
    max_monomial_degree = 0
    for _trial in range(500):
        terms = []
        for _term in range(rng.randint(1, 4)):
            factors = [component_index[rng.randrange(len(component_index))]
                       for _ in range(rng.randint(1, 4))]
            terms.append((rng.randint(-9, 9), tuple(factors)))
            max_monomial_degree = max(max_monomial_degree, len(factors))
        member = sample_members[rng.randrange(len(sample_members))]
        readings = class_readings(scaled_source(member))
        total: Poly = ()
        for coefficient, factors in terms:
            monomial: Poly = (1,)
            for gid, slot in factors:
                monomial = p_mul(monomial, readings[gid][0][slot])
            total = p_add(total, p_scale(monomial, coefficient))
        element_count += 1
        if p_degree(total) > 0:
            element_nonconstant += 1
        if p_eval(total, 1) != p_eval(total, -1):
            element_sensitive += 1
    result = {
        "closure_claim": (
            "on the declared family every covariance-filtered generator reads "
            "as a sigma-CONSTANT, and constants are closed under rational "
            "linear combination and product, so every element of the algebra "
            "the stipulated grammar generates -- at any degree, not merely one "
            "and two -- is sigma-constant and therefore blind AT THIS "
            "STIPULATED SCOPE"
        ),
        "hypothesis_all_generators_constant":
            census["nonconstant_generator_count"] == 0,
        "ring_law_tests": ring_tests,
        "constants_closed_under_ring_operations": ring_ok,
        "degree_addition_law_holds": graded_ring_ok,
        "random_algebra_elements_tested": element_count,
        "random_element_max_monomial_degree": max_monomial_degree,
        "random_element_member_sample": len(sample_members),
        "random_elements_nonconstant_in_sigma": element_nonconstant,
        "random_elements_sigma_sensitive": element_sensitive,
        "component_base_width": len(component_index),
        "seed": 87_201,
        "finding": (
            f"The blindness statement is pushed from the generator list to the "
            f"generated algebra, still at the stipulated scope only. The "
            f"hypothesis -- every covariance-filtered generator reads as a "
            f"sigma-constant on the declared family -- is "
            + ("met" if census["nonconstant_generator_count"] == 0 else "NOT met")
            + f", and the ring operations were checked to preserve constancy on "
            f"{ring_tests} random cases. {element_count} random algebra "
            f"elements were then built from the {len(component_index)} scalar "
            f"components -- sums of up to four monomials of up to "
            f"{max_monomial_degree} factors each with random integer "
            f"coefficients -- and evaluated on random declared members: "
            f"{element_nonconstant} carried any sigma dependence and "
            f"{element_sensitive} separated the two signs."
        ),
    }
    result["pass"] = (
        ring_ok and graded_ring_ok and element_count == 500
        and len(component_index) > 0 and ring_tests == 400
        # decisive: the closure hypothesis and both reported zero counts are
        # gated -- a non-constant or sensitive algebra element fails here
        and result["hypothesis_all_generators_constant"]
        and element_nonconstant == 0
        and element_sensitive
        == SUBMITTED_BOUNDARY["random_algebra_elements_sensitive"]
    )
    return result


# --------------------------------------------------------------------------
# certificate G -- the escape-(b) classification and the exact obstruction
# --------------------------------------------------------------------------
ESCAPE_PROBE_MEMBERS = (
    ("k2", 0, 1, 2, 3), ("k2", 1, 3, 4, 2), ("k2", 2, 4, 5, 3),
    ("k1", 0, 0, 1), ("k1", 1, 5, 6), ("k2", 3, 6, 0, 1),
)


def escape_certificate(members: tuple, admissible: tuple) -> dict[str, object]:
    # EXHAUSTIVE census (review fix): the escape-shaped class is decided over
    # EVERY declared member under BOTH declared loaded probe ledgers, not over
    # a probe sample.  The witness identity is likewise verified on every
    # member under all three ledgers.
    witness_gid = ("L", "id", 1, "sector")
    survives_M1 = set()
    max_loaded_degree = -1
    witness_matches_sigma_times_conformal = True
    witness_fires_when_loaded = 0
    witness_loaded_cases = 0
    for member in members:
        for ledger in (detuned_ledger, pure_conformal_ledger):
            scaled = scaled_source(member, ledger)
            readings = class_readings(scaled)
            for gid in admissible:
                values = readings[gid][0]
                for poly in values:
                    max_loaded_degree = max(max_loaded_degree, p_degree(poly))
                if not all(p_odd_part_is_zero(poly) for poly in values):
                    survives_M1.add(gid)
            channel = conformal_channel(scaled)
            values = readings[witness_gid][0]
            expected = tuple(
                p_shift(p_const(SECTOR_COUNT * channel[e][a]), 1)
                for e in range(ENDPOINT_COUNT) for a in range(AXES)
            )
            if tuple(values) != expected:
                witness_matches_sigma_times_conformal = False
            if any(value for block in channel for value in block):
                witness_loaded_cases += 1
                if tuple(p_eval(poly, 1) for poly in values) != \
                        tuple(p_eval(poly, -1) for poly in values):
                    witness_fires_when_loaded += 1
    syntactic = {}
    for gid in admissible:
        if gid[0] == "L":
            grade_powers = (gid[2],)
        else:
            grade_powers = (gid[1][1], gid[2][1])
        syntactic[gid] = {
            "source_degree": GENERATOR_DEGREE[gid],
            "grade_power_one_only": all(power == 1 for power in grade_powers),
        }
    cross_tab = {}
    for gid in admissible:
        key = (
            f"source_degree_{syntactic[gid]['source_degree']}",
            ("grade_power_one_only" if syntactic[gid]["grade_power_one_only"]
             else "touches_grade_power_two"),
            "odd" if gid in survives_M1 else "even",
        )
        cross_tab[key] = cross_tab.get(key, 0) + 1
    odd_by_pairing = {label: 0 for label, _fn, _doc in PAIRINGS}
    total_by_pairing = {label: 0 for label, _fn, _doc in PAIRINGS}
    for gid in admissible:
        if gid[0] != "Q":
            continue
        total_by_pairing[gid[3]] += 1
        if gid in survives_M1:
            odd_by_pairing[gid[3]] += 1
    sector_contracting = ("gram", "sector_contract", "endpoint_transfer")
    odd_same_grade = {label: 0 for label, _fn, _doc in PAIRINGS}
    total_same_grade = {label: 0 for label, _fn, _doc in PAIRINGS}
    odd_mixed_grade = {label: 0 for label, _fn, _doc in PAIRINGS}
    total_mixed_grade = {label: 0 for label, _fn, _doc in PAIRINGS}
    for gid in admissible:
        if gid[0] != "Q":
            continue
        same = gid[1][1] == gid[2][1]
        (total_same_grade if same else total_mixed_grade)[gid[3]] += 1
        if gid in survives_M1:
            (odd_same_grade if same else odd_mixed_grade)[gid[3]] += 1
    m1_broad_statement_holds = all(
        odd_by_pairing[label] == 0 for label, _fn, _doc in PAIRINGS
    )
    sector_contracting_even_at_equal_grade = all(
        odd_same_grade[label] == 0 for label in sector_contracting
    )
    free_sector_pairings_odd_at_equal_grade = tuple(
        label for label, _fn, _doc in PAIRINGS
        if label not in sector_contracting and odd_same_grade[label] > 0
    )
    mixed_grade_breaks_sector_contracting = tuple(
        label for label in sector_contracting if odd_mixed_grade[label] > 0
    )
    # the decisive witness (a sufficient obstruction, NOT claimed unique):
    # its identity was verified on every member under both loaded ledgers
    # above; here it is verified on every member under the stipulated ledger,
    # and the escape-shaped class is swept for sensitivity on the declared
    # family -- both loops are exhaustive
    escape_b_on_declared_sensitive = 0
    for member in members:
        scaled = scaled_source(member)
        readings = class_readings(scaled)
        channel = conformal_channel(scaled)
        values = readings[witness_gid][0]
        expected = tuple(
            p_shift(p_const(SECTOR_COUNT * channel[e][a]), 1)
            for e in range(ENDPOINT_COUNT) for a in range(AXES)
        )
        if tuple(values) != expected:
            witness_matches_sigma_times_conformal = False
        for gid in survives_M1:
            values = readings[gid][0]
            if tuple(p_eval(poly, 1) for poly in values) != \
                    tuple(p_eval(poly, -1) for poly in values):
                escape_b_on_declared_sensitive += 1
    result = {
        "escape_b_as_named_by_868": (
            "the second named boundary of the reviewed Cycle-868 support "
            "statement (its 'escape (b)'): a response object linear in the "
            "endpoint exchange R rather than factoring through R*R, and not a "
            "sector-orthogonal contraction"
        ),
        "operational_test": (
            "an object has the escape-(b) shape exactly when its sigma "
            "polynomial has a nonvanishing ODD part on an off-scope "
            "conformally loaded source, decided EXHAUSTIVELY over every "
            "declared member under both declared loaded probe ledgers; "
            "objects that factor through R*R or contract sector-orthogonally "
            "are even in sigma for every source and cannot have it"
        ),
        "escape_census_exhaustive": True,
        "escape_b_shaped_count": len(survives_M1),
        "escape_b_shaped_fraction_of_admissible":
            f"{len(survives_M1)}/{len(admissible)}",
        "escape_b_shaped_sample": tuple(
            sorted(gid_text(gid) for gid in survives_M1)[:16]
        ),
        "syntax_semantics_cross_tab": {
            "|".join(key): value for key, value in sorted(cross_tab.items())
        },
        "quadratic_odd_by_pairing": odd_by_pairing,
        "quadratic_total_by_pairing": total_by_pairing,
        "sector_contracting_pairings": sector_contracting,
        "quadratic_odd_by_pairing_equal_grade_power": odd_same_grade,
        "quadratic_total_by_pairing_equal_grade_power": total_same_grade,
        "quadratic_odd_by_pairing_mixed_grade_power": odd_mixed_grade,
        "quadratic_total_by_pairing_mixed_grade_power": total_mixed_grade,
        "M1_as_stated_at_868_covers_every_quadratic": m1_broad_statement_holds,
        "sector_contracting_even_at_equal_grade_power":
            sector_contracting_even_at_equal_grade,
        "free_sector_pairings_odd_at_equal_grade_power":
            free_sector_pairings_odd_at_equal_grade,
        "mixed_grade_power_breaks_sector_contracting":
            mixed_grade_breaks_sector_contracting,
        "max_sigma_degree_on_loaded_family": max_loaded_degree,
        "escape_b_shaped_sensitive_pairs_on_declared_family":
            escape_b_on_declared_sensitive,
        "obstruction_witness": gid_text(witness_gid),
        "witness_identity": (
            "the sector contraction of the graded source equals the sector "
            "count times sigma times the source's sector trace -- i.e. it reads "
            "sigma multiplied into the conformal channel and nothing else, "
            "exactly and componentwise; it is a DECISIVE WITNESS (sufficient "
            "for the only-if direction), with no uniqueness claimed -- other "
            "sigma-odd elements exist and are counted above"
        ),
        "witness_identity_verified": witness_matches_sigma_times_conformal,
        "witness_loaded_cases": witness_loaded_cases,
        "witness_fired_on_loaded_cases": witness_fires_when_loaded,
        "iff_statement": (
            "for any source in the declared scope: every element of the "
            "generated algebra is blind to sigma IF AND ONLY IF the source's "
            "conformal channel vanishes. Only if -- the witness above is an "
            "algebra element reading sigma times that channel, so a nonzero "
            "channel is seen. If -- a vanishing channel makes the grading act "
            "as the identity on the source, so every construction is "
            "sigma-independent"
        ),
        "finding": (
            f"The escape-(b) shape is classified rather than left named, "
            f"exhaustively over every declared member under both declared "
            f"loaded probe ledgers. Of the {len(admissible)} covariance-"
            f"filtered objects, {len(survives_M1)} have the escape-(b) shape: "
            f"they carry a genuinely ODD sigma dependence on a conformally "
            f"loaded source, so the shape is "
            + ("realisable inside the stipulated constructor algebra"
               if survives_M1 else
               "NOT realisable inside the stipulated constructor algebra")
            + f". On the declared family those same objects produced "
            f"{escape_b_on_declared_sensitive} sign-sensitive pairs. The shape "
            f"is not confined to objects linear in the source: the odd count "
            f"by tensor-square pairing is {compact(odd_by_pairing)} out of "
            f"{compact(total_by_pairing)}. The reviewed Cycle-868 structural "
            f"sigma-evenness mechanism, if read as a general claim that any "
            f"contraction quadratic in the graded source is even, is "
            + ("too broad for this wider stipulated grammar (its own six-"
               "object statement is unaffected), in two separable ways. "
               "First, pairings that leave the sector index free "
               f"({', '.join(free_sector_pairings_odd_at_equal_grade)}) "
               "are already odd at equal grading power, so it is the "
               "sector-orthogonality of the contraction and not the quadratic "
               "degree that forces evenness. Second, the sector-contracting "
               "pairings are "
               + ("even at equal grading power" if
                  sector_contracting_even_at_equal_grade else
                  "NOT even even at equal grading power")
               + " but "
               + (f"broken by mixing the two grading powers "
                  f"({', '.join(mixed_grade_breaks_sector_contracting)}), "
                  f"which admits sigma^3 terms -- the top sigma degree observed "
                  f"on a loaded member is {max_loaded_degree}, above the degree "
                  f"bound 2 that held for the six Cycle-868 objects"
                  if mixed_grade_breaks_sector_contracting else
                  "not broken by mixing the grading powers")
               if not m1_broad_statement_holds else
               "confirmed at full breadth here")
            + f". The reason nothing fires on the declared family is exact and "
            f"is exhibited by a decisive witness element (sufficient, not "
            f"unique): the sector contraction of the graded source reads sigma "
            f"multiplied into the conformal channel "
            + ("identically" if witness_matches_sigma_times_conformal
               else "NOT identically")
            + f", and it fired on {witness_fires_when_loaded} of the "
            f"{witness_loaded_cases} conformally loaded member evaluations. "
            f"WITHIN THE STIPULATED GRAMMAR the two boundaries named by the "
            f"reviewed Cycle-868 note are therefore not independent: the "
            f"escape-(b) shape sees sigma only through a nonzero conformal "
            f"channel, which is boundary (a). Whether physically relevant "
            f"response objects lie inside this grammar is OPEN, so no "
            f"statement about physical escape routes follows."
        ),
    }
    result["pass"] = (
        witness_matches_sigma_times_conformal
        and witness_loaded_cases > 0
        and witness_fires_when_loaded == witness_loaded_cases
        and sum(cross_tab.values()) == len(admissible)
        # decisive: the exhaustive census must equal the submitted boundary,
        # the shaped class must be nonempty, and declared-family sensitivity
        # of the shaped class must be exactly the submitted zero
        and len(survives_M1) == SUBMITTED_BOUNDARY["escape_shaped_count"]
        and len(survives_M1) > 0
        and escape_b_on_declared_sensitive
        == SUBMITTED_BOUNDARY["escape_shaped_sensitive_pairs_on_declared_family"]
        and max_loaded_degree
        == SUBMITTED_BOUNDARY["max_sigma_degree_on_loaded_family"]
    )
    return result


# --------------------------------------------------------------------------
# certificate H -- calibration, including a planted sigma-sensitive object
# --------------------------------------------------------------------------
PREREGISTERED_CONTROLS = {
    "P1_detuned_ledger": "CLASS_CONTAINS_SENSITIVE_OBJECTS",
    "P2_pure_conformal_ledger": "CLASS_CONTAINS_SENSITIVE_OBJECTS",
    "P3_stipulated_ledger": "REPORTED_NOT_GATED",
    "P4_adversary_disabled_grading": "CLASS_BLIND",
    "P5_planted_off_grammar_object": "CLASSIFIER_RETURNS_SENSITIVE_ON_LANDED",
}


def calibration_certificate(admissible: tuple) -> dict[str, object]:
    probe = ESCAPE_PROBE_MEMBERS
    p1 = classify(probe, admissible, ledger=detuned_ledger)
    p2 = classify(probe, admissible, ledger=pure_conformal_ledger)
    p3 = classify(probe, admissible, ledger=stipulated_ledger)
    p4 = classify(probe, admissible, ledger=detuned_ledger, live=False)
    p5 = classify(probe, admissible, ledger=stipulated_ledger,
                  grade_fn=grade_tracefree_channel)
    p5_full = classify(ESCAPE_PROBE_MEMBERS, admissible, ledger=stipulated_ledger,
                       grade_fn=grade_tracefree_channel)
    p1_ok = p1["sensitive_pairs"] > 0
    p2_ok = p2["sensitive_pairs"] > 0
    p4_ok = p4["sensitive_pairs"] == 0
    p5_ok = p5["sensitive_pairs"] > 0
    result = {
        "preregistered": PREREGISTERED_CONTROLS,
        "probe_members": probe,
        "P1_detuned_sensitive_pairs": p1["sensitive_pairs"],
        "P1_detuned_sensitive_generators": p1["sensitive_generator_count"],
        "P2_pure_conformal_sensitive_pairs": p2["sensitive_pairs"],
        "P2_pure_conformal_sensitive_generators": p2["sensitive_generator_count"],
        "P3_stipulated_ledger_sensitive_pairs": p3["sensitive_pairs"],
        "P4_disabled_grading_sensitive_pairs": p4["sensitive_pairs"],
        "P5_planted_object_sensitive_pairs": p5["sensitive_pairs"],
        "P5_planted_object_sensitive_generators": p5["sensitive_generator_count"],
        "P5_planted_reproducible": p5["stream_sha256"] == p5_full["stream_sha256"],
        "P1_met": p1_ok,
        "P2_met": p2_ok,
        "P4_met": p4_ok,
        "P5_met": p5_ok,
        "calibration_scope_note": (
            "P1, P2, P4 and P5 are OFF-SCOPE. P1 and P2 detune the recoil "
            "ledger, P4 disables the sigma probe while changing nothing else, "
            "and P5 replaces the stipulated grading with an off-grammar one "
            "that grades the TRACE-FREE channel instead. None is evidence about "
            "the declared family; together they establish that a blind reading "
            "is a property of the object class and not of a dead instrument."
        ),
        "P5_description": (
            "the planted object set is the identical covariance-filtered "
            "class run through an off-grammar grading that carries sigma on "
            "the trace-free channel, so it IS sigma-sensitive on the declared "
            "family under the stipulated ledger; it proves the classifier's "
            "sensitive branch is reachable through the same code path that "
            "reports the declared-family result. It is also a CONCRETE "
            "outside-grammar object that sees sigma while the conformal "
            "channel is zero, exhibiting why the classification cannot close "
            "any physical escape route beyond the stipulated grammar"
        ),
        "finding": (
            f"Five pre-registered controls. Detuning the ledger made "
            f"{p1['sensitive_generator_count']} class objects sign-sensitive "
            f"over {p1['sensitive_pairs']} pairs and a purely conformal ledger "
            f"made {p2['sensitive_generator_count']} sensitive over "
            f"{p2['sensitive_pairs']}, so the class can see the sign when the "
            f"sign is carried. The adversary run that carries the conformal "
            f"channel at sigma-degree zero -- disabling the probe and changing "
            f"nothing else -- returned {p4['sensitive_pairs']} sensitive pairs "
            f"even on the detuned source. The planted off-grammar object, "
            f"graded on the trace-free channel instead, returned "
            f"{p5['sensitive_pairs']} sensitive pairs on the declared family "
            f"under the stipulated ledger, so the classifier demonstrably "
            f"reports sensitivity through this exact code path when a "
            f"sigma-visible object is present -- and that planted object lies "
            f"OUTSIDE the stipulated grammar, marking the open exhaustiveness "
            f"boundary. The stipulated ledger itself returned "
            f"{p3['sensitive_pairs']} sensitive pairs on the same probes; that "
            f"number is reported here and gated in the declared-family "
            f"certificate."
        ),
    }
    result["pass"] = p1_ok and p2_ok and p4_ok and p5_ok
    return result


# --------------------------------------------------------------------------
# certificate I -- the verdict, produced by a stated total function
# --------------------------------------------------------------------------
def verdict_certificate(declared: dict[str, object], closure: dict[str, object],
                        escape: dict[str, object]) -> dict[str, object]:
    sensitive = declared["sensitive_pairs"]
    constant = declared["nonconstant_generator_count"] == 0
    algebra_clean = closure["random_elements_sigma_sensitive"] == 0
    escape_shaped = escape["escape_b_shaped_count"]
    if sensitive > 0:
        verdict = "OUTCOME_A_LAWFUL_SIGMA_VISIBLE_OBJECT_EXISTS"
    elif not (constant and algebra_clean):
        verdict = "OUTCOME_C_CLASSIFICATION_INCOMPLETE"
    elif escape_shaped > 0:
        verdict = "OUTCOME_B_CONSTRUCTOR_ALGEBRA_BLIND_ESCAPE_B_SHAPED_BUT_VOID"
    else:
        verdict = "OUTCOME_B_CONSTRUCTOR_ALGEBRA_BLIND_ESCAPE_B_UNREALISABLE"
    result = {
        "verdict_function": (
            "sensitive_pairs>0 -> OUTCOME_A; else if any generator or random "
            "algebra element is non-constant in sigma -> OUTCOME_C; else if "
            "escape-(b)-shaped objects exist -> OUTCOME_B (shaped but void); "
            "else OUTCOME_B (shape unrealisable). ONLY the submitted outcome "
            "-- OUTCOME_B shaped-but-void with the submitted counts -- passes "
            "this certificate; every alternative outcome is emitted as a "
            "non-PASS diagnostic and drives a nonzero exit"
        ),
        "sensitive_pairs": sensitive,
        "all_generators_constant_in_sigma": constant,
        "random_algebra_elements_sensitive":
            closure["random_elements_sigma_sensitive"],
        "escape_b_shaped_count": escape_shaped,
        "verdict": verdict,
        "classification_boundary": (
            "CERTIFIED (as exact support on stipulated data): the algebra "
            "generated by the stipulated constructors -- grading G_sigma at "
            "powers one and two, the endpoint exchange R, rational linear "
            "combination, contraction over any subset of the endpoint / sector "
            "/ axis indices, and the tensor square with the five declared "
            "pairings -- acting on the declared k<=2 source family with the "
            "stipulated traceless (-2d,+d,+d) ledger on the two-endpoint held "
            "L=6 surface (weight ladder d=1..6 an explicit scope input), "
            "filtered by the two declared covariance conditions, closed under "
            "sums and products at arbitrary degree. "
            "NOT CERTIFIED and outside the boundary: constructions that change "
            "the ledger so a source acquires a nonzero sector trace; "
            "constructions that admit sigma itself as a scalar coefficient "
            "rather than reading it through the grading; gradings that put "
            "sigma on a channel other than the conformal one; non-polynomial "
            "objects such as ratios, norms with roots or thresholded readings; "
            "any object reading data outside S, R and G_sigma; ANY claim that "
            "this grammar exhausts physically allowed response objects; and "
            "ANY identification of sigma with the physical conformal-mode sign "
            "or of these objects with an unlanded response lineage"
        ),
        "relation_to_cycle868": (
            "the reviewed Cycle-868 package proved its six stipulated objects "
            "blind as exact support and named two boundaries of that support "
            "statement. This cycle re-derives those six objects in-file, shows "
            "the stipulated constructor algebra contains them, extends the "
            "blindness to that whole algebra at the same stipulated scope, and "
            "shows that WITHIN THIS GRAMMAR the second named boundary sees "
            "sigma only through the first (a nonzero conformal channel). The "
            "reviewed Cycle-868 open identifications are inherited unchanged, "
            "and no physical escape-route statement follows"
        ),
        "what_is_not_claimed": (
            "no statement about the VALUE of the conformal sign; no statement "
            "about lanes outside this scope; no statement about objects "
            "outside the stipulated constructor grammar (the planted control "
            "exhibits such an object seeing sigma with the conformal channel "
            "zero); no claim that the grammar exhausts physically allowed "
            "response objects (a target-equivalent open lemma); no "
            "identification of sigma with the physical conformal-mode sign; no "
            "identification with the unlanded Cycle-749/768/812 lineage"
        ),
        "finding": (
            f"No covariance-filtered object in the stipulated constructor "
            f"algebra separates sigma=+1 from sigma=-1 on any member of the "
            f"complete declared source family: {declared['pair_count']} exact "
            f"pairs, {sensitive} sensitive. Every generator reads as a "
            f"sigma-constant there, and constants are closed under the "
            f"algebra's own operations, so the blindness extends to every sum "
            f"and product at any degree rather than stopping at the enumerated "
            f"generators. {escape_shaped} objects do carry the escape-(b) "
            f"shape and would see the sign the moment a source carried a "
            f"conformal channel, so the shape is real and the obstruction is "
            f"arithmetic: the stipulated recoil ledger annihilates the only "
            f"channel sigma touches INSIDE THIS GRAMMAR. All of this is exact "
            f"support on the stipulated surface; the grammar-exhaustiveness "
            f"lemma and both physical identifications remain open, so no "
            f"physical escape route is closed."
        ) if verdict.startswith("OUTCOME_B") else (
            f"The classification found {sensitive} sign-sensitive pairs inside "
            f"the covariance-filtered class on the declared family. A "
            f"sigma-visible object exists at the stipulated scope; the "
            f"sensitive objects are recorded in the declared-family "
            f"certificate. This is NOT the submitted outcome; the run fails."
        ) if sensitive > 0 else (
            f"The classification is incomplete: the declared family produced "
            f"no sensitive pair, but "
            f"{closure['random_elements_sigma_sensitive']} random algebra "
            f"elements or non-constant generators remain, so the closure to "
            f"the generated algebra is not established. This is NOT the "
            f"submitted outcome; the run fails."
        ),
    }
    # decisive: only the exact submitted boundary passes -- a refutation, an
    # incomplete classification, or a count drift all exit nonzero
    result["pass"] = (
        verdict == SUBMITTED_BOUNDARY["verdict"]
        and sensitive == SUBMITTED_BOUNDARY["sensitive_pairs"]
        and constant
        and algebra_clean
        and escape_shaped == SUBMITTED_BOUNDARY["escape_shaped_count"]
    )
    return result


# --------------------------------------------------------------------------
# certificate J -- source and process controls
# --------------------------------------------------------------------------
def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    rows = []
    markers_ok = True
    for path in AUDIT_INPUT_PATHS:
        payload = payloads[path]
        present = True
        if path in REQUIRED_AST_MARKERS:
            tree = ast.parse(payload, filename=path)
            names: set[str] = set()
            for node in tree.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef,
                                     ast.ClassDef)):
                    names.add(node.name)
                elif isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            names.add(target.id)
                elif isinstance(node, ast.AnnAssign) and \
                        isinstance(node.target, ast.Name):
                    names.add(node.target.id)
            present = set(REQUIRED_AST_MARKERS[path]) <= names
            markers_ok = markers_ok and present
        rows.append({
            "path": path,
            "exists_worktree_relative":
                not Path(path).is_absolute() and (ROOT / path).is_file(),
            "sha256": sha256(payload).hexdigest(),
            "sha256_exact": sha256(payload).hexdigest() == EXPECTED_SHA256[path],
            "git_blob": git_blob(payload),
            "git_blob_exact": git_blob(payload) == EXPECTED_GIT_BLOBS[path],
            "required_markers": REQUIRED_AST_MARKERS.get(path, ()),
            "required_markers_present": present,
            "access": "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY" if path.endswith(".py")
                      else "TEXT_ONLY_PINNED_STDOUT",
        })
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 2,
        "source_rows": tuple(rows),
        "all_markers_present": markers_ok,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "executable_science_inputs": (),
    }
    result["sources_pass"] = (
        len(rows) <= 2
        and all(row["exists_worktree_relative"] and row["sha256_exact"]
                and row["git_blob_exact"] and row["required_markers_present"]
                for row in rows)
        and markers_ok
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# emission
# --------------------------------------------------------------------------
LABELS = (
    "A_GRAMMAR",
    "B_LINEAGE_CONSTRAINTS",
    "C_CONTAINMENT_OF_868",
    "D_ADMISSIBILITY",
    "E_DECLARED_FAMILY_CLASSIFICATION",
    "F_ALGEBRA_CLOSURE",
    "G_ESCAPE_B",
    "H_CALIBRATION",
    "I_VERDICT",
    "J_CONTROLS",
)


def render_fixed_point(certificates: dict[str, dict[str, object]]) -> str:
    for _attempt in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        terminal = {
            "terminal": (
                "CYCLE872_SIGMA_ADMISSIBILITY_CLASSIFICATION_COMPLETE"
                if all(checks.values())
                else "CYCLE872_SIGMA_ADMISSIBILITY_CLASSIFICATION_INCOMPLETE"
            ),
            "checks": checks,
            "verdict": certificates["I_VERDICT"]["verdict"],
            "generators_declared": certificates["A_GRAMMAR"]["generator_count"],
            "generators_admissible": certificates["D_ADMISSIBILITY"]["admissible_count"],
            "pairs_classified":
                certificates["E_DECLARED_FAMILY_CLASSIFICATION"]["pair_count"],
            "sigma_sensitive_pairs":
                certificates["E_DECLARED_FAMILY_CLASSIFICATION"]["sensitive_pairs"],
            "escape_b_shaped_objects":
                certificates["G_ESCAPE_B"]["escape_b_shaped_count"],
            "random_algebra_elements_sensitive":
                certificates["F_ALGEBRA_CLOSURE"]["random_elements_sigma_sensitive"],
            "runtime_seconds": certificates["J_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["J_CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in LABELS:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
                f"{compact(certificates[label])}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["J_CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass"] and controls["stdout_under_limit"]
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    grammar = grammar_certificate()
    members = enumerate_family()
    lineage = lineage_certificate(members)
    containment = containment_certificate(members)
    admissible, admissibility = admissibility_certificate(members)
    census = classify(members, admissible)
    declared = declared_family_certificate(census)
    closure = closure_certificate(members, admissible, census)
    escape = escape_certificate(members, admissible)
    calibration = calibration_certificate(admissible)
    verdict = verdict_certificate(declared, closure, escape)

    replay_members = enumerate_family()
    replay_census = classify(replay_members, admissible)
    replay_closure = closure_certificate(replay_members, admissible, replay_census)
    deterministic = (
        replay_members == members
        and replay_census["stream_sha256"] == census["stream_sha256"]
        and replay_census["sensitive_pairs"] == census["sensitive_pairs"]
        and replay_census["sigma_degree_census"] == census["sigma_degree_census"]
        and replay_closure["random_elements_sigma_sensitive"]
        == closure["random_elements_sigma_sensitive"]
    )
    elapsed = monotonic() - started
    controls = {
        **sources,
        "determinism": {
            "scope": (
                "the family enumeration, the complete classification stream "
                "over every admissible object, and the seeded random algebra "
                "sweep were recomputed from scratch and compared "
                "digest-for-digest"
            ),
            "first_classification_sha256": census["stream_sha256"],
            "second_classification_sha256": replay_census["stream_sha256"],
            "exact": deterministic,
        },
        "arithmetic_route": (
            "exact integer univariate polynomials in the formal sigma over a "
            "source pre-scaled by three; no floating point and no rational "
            "rounding enters any certified quantity"
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_modules_loaded_after_science": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_after_science": tuple(FIREWALL.hits),
        "finding": (
            "Both cited inputs -- the reviewed Cycle-868 runner and its pinned "
            "stdout, pinned at the blobs landed on origin/main after that "
            "package's review fixes -- are literal worktree-relative paths "
            "matching their pinned SHA-256 and git blob hashes, carrying their "
            "required AST markers, consumed as text or AST only behind an "
            "import firewall that was never tripped. The formerly cited "
            "Cycle-320/322/768/812 lineage is provenance-only and is no longer "
            "an input. The whole classification and the seeded algebra sweep "
            "were recomputed from scratch and reproduced digest-for-digest, "
            "and both the runtime and stdout caps were respected."
        ),
    }
    controls["base_pass"] = (
        sources["sources_pass"] and deterministic
        and controls["runtime_under_limit"]
        and not controls["blocked_modules_loaded_after_science"]
        and not controls["firewall_hits_after_science"]
    )
    controls["pass"] = controls["base_pass"]

    certificates = {
        "A_GRAMMAR": grammar,
        "B_LINEAGE_CONSTRAINTS": lineage,
        "C_CONTAINMENT_OF_868": containment,
        "D_ADMISSIBILITY": admissibility,
        "E_DECLARED_FAMILY_CLASSIFICATION": declared,
        "F_ALGEBRA_CLOSURE": closure,
        "G_ESCAPE_B": escape,
        "H_CALIBRATION": calibration,
        "I_VERDICT": verdict,
        "J_CONTROLS": controls,
    }
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
