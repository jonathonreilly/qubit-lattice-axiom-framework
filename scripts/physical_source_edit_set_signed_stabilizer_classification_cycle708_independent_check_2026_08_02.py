#!/usr/bin/env python3
"""Independent exact check of the Cycle-708 signed-stabilizer algebra.

This checker does not import the primary runner or the supplied numerical
source-response compiler. It reconstructs the signed-permutation group with a
pure-integer representation, enumerates the four weighted direction domains,
and verifies the subgroup, coset, determinant-balance, collision, and profile
claims independently. It then compares those exact results with the primary
receipt and checks a noncommuting sidedness rejector.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
import sys


AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02.md",
    "outputs/physical_source_edit_set_signed_stabilizer_classification_cycle708_2026_08_02_receipt_2026-08-02.json",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / AUDIT_INPUT_PATHS[1]

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Vector = tuple[int, int, int]
Domain = tuple[tuple[Vector, int], ...]

PASS = 0
FAIL = 0


def gate(label: str, condition: bool) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}")
    else:
        FAIL += 1
        print(f"FAIL {label}")


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def matvec(a: Matrix, v: Vector) -> Vector:
    return tuple(sum(a[i][j] * v[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def determinant(a: Matrix) -> int:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def constant_sign(a: Matrix) -> int | None:
    signs: list[int] = []
    for row in a:
        nonzero = [entry for entry in row if entry]
        if len(nonzero) != 1:
            return None
        signs.append(nonzero[0])
    return signs[0] if all(sign == signs[0] for sign in signs) else None


def signed_permutations() -> tuple[Matrix, ...]:
    out: list[Matrix] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            out.append(
                tuple(
                    tuple(signs[i] if j == permutation[i] else 0 for j in range(3))
                    for i in range(3)
                )  # type: ignore[arg-type]
            )
    return tuple(out)


G48 = signed_permutations()
PROPER = tuple(matrix for matrix in G48 if determinant(matrix) == 1)
CS = tuple(matrix for matrix in G48 if constant_sign(matrix) is not None)
IDENTITY: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def transformed(domain: Domain, matrix: Matrix) -> Domain:
    return tuple(sorted((matvec(matrix, vector), weight) for vector, weight in domain))


def stabilizer(domain: Domain) -> tuple[Matrix, ...]:
    return tuple(matrix for matrix in G48 if transformed(domain, matrix) == domain)


def sign_set(frame: Matrix, stab: tuple[Matrix, ...]) -> tuple[int, ...]:
    return tuple(sorted({
        sign
        for element in stab
        if (sign := constant_sign(matmul(frame, element))) is not None
    }))


def wrong_sided_sign_set(frame: Matrix, stab: tuple[Matrix, ...]) -> tuple[int, ...]:
    return tuple(sorted({
        sign
        for element in stab
        if (sign := constant_sign(matmul(element, frame))) is not None
    }))


def class_name(signs: tuple[int, ...]) -> str:
    return {
        (): "broken",
        (1,): "plus",
        (-1,): "minus",
        (-1, 1): "both",
    }[signs]


def profile(stab: tuple[Matrix, ...]) -> dict[str, int]:
    counts = {"plus": 0, "minus": 0, "both": 0, "broken": 0}
    for frame in PROPER:
        counts[class_name(sign_set(frame, stab))] += 1
    return counts


AXIS_RAYS: tuple[Vector, ...] = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


def weighted_six_ray_domain(edits: dict[Vector, int]) -> Domain:
    return tuple(sorted((ray, edits.get(ray, 3)) for ray in AXIS_RAYS))


DOMAINS: dict[str, Domain] = {
    "one_edit": weighted_six_ray_domain({(1, 0, 0): 5}),
    "two_distinct_axis_edits": weighted_six_ray_domain({
        (1, 0, 0): 5,
        (0, 1, 0): 7,
    }),
    "three_distinct_axis_edits": weighted_six_ray_domain({
        (1, 0, 0): 5,
        (0, 1, 0): 7,
        (0, 0, 1): 11,
    }),
    "inversion_pair": weighted_six_ray_domain({
        (-1, 0, 0): 5,
        (1, 0, 0): 5,
    }),
}
EXPECTED = {
    "one_edit": {"stab": 8, "cs_stab": 2, "profile": [12, 12, 0, 0], "pairs": 48},
    "two_distinct_axis_edits": {
        "stab": 2, "cs_stab": 1, "profile": [6, 6, 0, 12], "pairs": 12,
    },
    "three_distinct_axis_edits": {
        "stab": 1, "cs_stab": 1, "profile": [3, 3, 0, 18], "pairs": 6,
    },
    "inversion_pair": {"stab": 16, "cs_stab": 4, "profile": [0, 0, 24, 0], "pairs": 96},
}


gate("group has 48 distinct signed permutations", len(G48) == len(set(G48)) == 48)
gate("proper subgroup has order 24", len(PROPER) == 24)
gate("constant-sign subgroup has order 12", len(CS) == 12)
gate("constant-sign set is closed", all(matmul(a, b) in CS for a in CS for b in CS))
gate(
    "constant-sign character is multiplicative",
    all(constant_sign(matmul(a, b)) == constant_sign(a) * constant_sign(b) for a in CS for b in CS),
)

receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
order = ("plus", "minus", "both", "broken")
for name, domain in DOMAINS.items():
    stab = stabilizer(domain)
    cs_stab = tuple(matrix for matrix in stab if matrix in CS)
    product = {matmul(cs_element, stab_element) for cs_element in CS for stab_element in stab}
    counts = profile(stab)
    lawful_hits = sum(
        sum(1 for element in stab if matmul(frame, element) in CS)
        for frame in PROPER
    )
    has_minus = any(constant_sign(matrix) == -1 for matrix in cs_stab)
    has_both = any(sign_set(frame, stab) == (-1, 1) for frame in PROPER)
    expected = EXPECTED[name]
    gate(f"{name} stabilizer order", len(stab) == expected["stab"])
    gate(f"{name} constant-sign intersection order", len(cs_stab) == expected["cs_stab"])
    gate(
        f"{name} subgroup-product formula",
        len(product) == len(CS) * len(stab) // len(cs_stab),
    )
    gate(f"{name} determinant balance", 2 * sum(determinant(matrix) == 1 for matrix in product) == len(product))
    gate(f"{name} exact proper-frame profile", [counts[key] for key in order] == expected["profile"])
    gate(f"{name} collision criterion", has_both == has_minus)
    gate(f"{name} every-representative census", lawful_hits == expected["pairs"])
    for size in (3, 7):
        observed = receipt["domains"][f"L{size}"][name]
        gate(f"{name} L={size} receipt profile", observed["predicted_profile"] == expected["profile"])
        gate(f"{name} L={size} primary agreement", observed["agreement"] == 24 and observed["forbidden_gap_hits"] == 0)
        gate(f"{name} L={size} receipt representative census", observed["lawful_pairs"] == expected["pairs"])

# Multiplication order is load-bearing. This deliberately asymmetric weighted
# domain makes left and right cosets disagree on eight proper frames.
SIDEDNESS_DOMAIN: Domain = (((-1, -1, 0), 2), ((-1, 0, 0), 3))
SIDEDNESS_STAB = stabilizer(SIDEDNESS_DOMAIN)
sidedness_disagreements = sum(
    sign_set(frame, SIDEDNESS_STAB) != wrong_sided_sign_set(frame, SIDEDNESS_STAB)
    for frame in PROPER
)
gate("right-coset sidedness rejector changes eight frame labels", sidedness_disagreements == 8)
gate("primary receipt reports no failed gates", receipt["gates"]["fail"] == 0)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
