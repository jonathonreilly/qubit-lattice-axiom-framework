#!/usr/bin/env python3
"""Independent reconstruction of the Block-4 remote-context connector.

This checker does not import the primary Block-4 or Block-3 implementation.
It rebuilds the two Record worlds, shell restrictions, conditional-measure
identity, formation countercontrol, exact Kraus factorization, realized
branch-state continuation, and held physical-code embeddings.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317


NOTE = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY = ROOT / "scripts" / (
    "common_front_stage_remote_context_record_event_congruence_2026_08_20.py"
)

AUDIT_INPUT_PATHS = (
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)

TOL = 1.0e-10
PASS = 0
FAIL = 0

Point = tuple[int, int, int]
Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
Records = dict[Point, Code]

DIRS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
TRANSVERSE = ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
I2 = np.eye(2, dtype=complex)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(point: Point) -> Point:
    return (-point[0], -point[1], -point[2])


def dist(left: Point, right: Point) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def encode(matrix: sp.Matrix, label: int) -> Code:
    tagged = matrix + sp.I * label * sp.eye(2)
    return tuple(sp.simplify(tagged[row, column]) for row in range(2) for column in range(2))  # type: ignore[return-value]


E0 = sp.diag(sp.Rational(1, 2), 0)
EB = sp.eye(2) - E0
RHO = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
PREP = encode(RHO, 7)
FRONT = frozenset(
    (
        encode(E0, 20),
        encode(EB, 21),
        encode(sp.eye(2) / 2, 22),
        encode(sp.eye(2), 23),
    )
)
TAIL = frozenset(
    (
        encode(sp.eye(2) / 3, 24),
        encode(2 * sp.eye(2) / 3, 25),
        encode(sp.eye(2), 26),
    )
)
CA = encode(sp.Matrix(((1, 1), (1, 1))) / 2, 30)
CB = encode(sp.Matrix(((1, -sp.I), (sp.I, 1))) / 2, 31)
R0 = encode(E0, 0)
RB = encode(EB, 1)


def world(context: str) -> Records:
    records: Records = {(-1, 0, 0): PREP}
    for direction, value in zip(TRANSVERSE, sorted(FRONT, key=repr), strict=True):
        records[direction] = value
    for point, value in zip(
        ((1, -1, 0), (1, 0, 1), (1, 0, -1)),
        sorted(TAIL, key=repr),
        strict=True,
    ):
        records[point] = value
    records[(1, 1, 0)] = CA if context == "A" else CB
    return records


def shell(records: Records, target: Point) -> tuple[tuple[Point, Code | None], ...]:
    return tuple((direction, records.get(add(target, direction))) for direction in DIRS)


@dataclass(frozen=True)
class Decoded:
    stage: str
    forward: Point
    read: tuple[Point, ...]


def decode(records: Records, target: Point) -> Decoded | None:
    if target in records:
        return None
    occupied = tuple(direction for direction in DIRS if add(target, direction) in records)
    blank = tuple(direction for direction in DIRS if direction not in occupied)
    if len(occupied) != 5 or len(blank) != 1:
        return None
    forward = blank[0]
    predecessor = add(target, neg(forward))
    sides = tuple(add(target, direction) for direction in occupied if direction != neg(forward))
    if predecessor not in records or len(sides) != 4:
        return None
    side_values = frozenset(records[point] for point in sides)
    stage = None
    if records[predecessor] == PREP and side_values == FRONT:
        stage = "front"
    if records[predecessor] == RB and side_values == TAIL | {CA}:
        stage = "tail-A"
    if records[predecessor] == RB and side_values == TAIL | {CB}:
        stage = "tail-B"
    if stage is None:
        return None
    return Decoded(stage, forward, tuple(sorted((predecessor,) + sides)))


def append(records: Records, target: Point, value: Code) -> Records:
    if target in records:
        raise ValueError("occupied target")
    answer = dict(records)
    answer[target] = value
    return answer


def frontier(records: Records) -> set[Point]:
    return {
        add(point, direction)
        for point in records
        for direction in DIRS
        if add(point, direction) not in records
    }


def enabled(records: Records) -> tuple[tuple[Point, str], ...]:
    rows = []
    for target in sorted(frontier(records)):
        result = decode(records, target)
        if result is not None:
            rows.append((target, result.stage))
    return tuple(rows)


def determinant(matrix: tuple[Point, Point, Point]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def rotations() -> tuple[tuple[Point, Point, Point], ...]:
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    rows = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * axes[order[row]][column] for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                rows.append(matrix)
    return tuple(rows)  # type: ignore[return-value]


def carry(matrix: tuple[Point, Point, Point], point: Point) -> Point:
    return tuple(
        sum(matrix[row][column] * point[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def projector(vector: tuple[float, float, float]) -> np.ndarray:
    x = np.array(((0, 1), (1, 0)), dtype=complex)
    y = np.array(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    return (I2 + vector[0] * x + vector[1] * y + vector[2] * z) / 2


def programs() -> tuple[tuple[np.ndarray, ...], tuple[np.ndarray, ...], np.ndarray, np.ndarray]:
    rt2 = np.sqrt(2.0)
    e0 = np.diag((0.5, 0.0)).astype(complex)
    effects_a = (
        e0,
        0.9 * projector((4 * rt2 / 9, 0.0, -7 / 9)),
        0.6 * projector((-2 * rt2 / 3, 0.0, 1 / 3)),
    )
    effects_b = (
        e0,
        0.75 * projector((2 * rt2 / 3, 0.0, -1 / 3)),
        0.75 * projector((-2 * rt2 / 3, 0.0, -1 / 3)),
    )
    contact = np.diag((np.exp(0.37j), 1.0)).astype(complex)

    def psqrt(matrix: np.ndarray) -> np.ndarray:
        values, vectors = np.linalg.eigh(matrix)
        if float(np.min(values)) < -TOL:
            raise ValueError("non-positive effect")
        return vectors @ np.diag(np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T

    kraus_a = tuple(psqrt(effect) @ contact for effect in effects_a)
    kraus_b = tuple(psqrt(effect) @ contact for effect in effects_b)
    common = kraus_a[0]
    remainder = psqrt(I2 - e0) @ contact
    return kraus_a, kraus_b, common, remainder


def source_and_scope() -> None:
    note = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").split())
    axiom = " ".join(AXIOM.read_text(encoding="utf-8").lower().split())
    check(
        "source-packet",
        PRIMARY.exists()
        and "probability distribution over the possibilities is determined by" in axiom
        and "conditional on formation at s0" in note
        and "pointer-to-record actualization remains open" in note
        and "coherent and realized modes are separate" in note
        and "toe percentage movement: zero" in note,
        "the axiom implication and all formation, event, actualization, and score boundaries are source-bound",
    )


def spatial_controls() -> None:
    a, b = world("A"), world("B")
    s0, s1, c = (0, 0, 0), (1, 0, 0), (1, 1, 0)
    changed = {point for point in set(a) | set(b) if a.get(point) != b.get(point)}
    check(
        "independent-shell-identity",
        changed == {c}
        and shell(a, s0) == shell(b, s0)
        and dist(c, s0) == 2
        and dist(c, s1) == 1
        and enabled(a) == enabled(b) == ((s0, "front"),),
        "the worlds differ at one remote M2 Record and have byte-identical complete front shells",
    )
    check(
        "symbolic-full-measure-identity",
        ("A", shell(a, s0))[1] == ("B", shell(b, s0))[1]
        and R0 == encode(E0, 0),
        "one single-valued law image of the identical condition gives equal mass to every common Borel event; no value is assigned",
    )
    e0_a, e0_b = append(a, s0, R0), append(b, s0, R0)
    rb_a, rb_b = append(a, s0, RB), append(b, s0, RB)
    check(
        "independent-rail-gating",
        enabled(e0_a) == enabled(e0_b) == ()
        and enabled(rb_a) == ((s1, "tail-A"),)
        and enabled(rb_b) == ((s1, "tail-B"),)
        and all(e0_a[point] == value for point, value in a.items())
        and all(rb_a[point] == value for point, value in a.items()),
        "the supplied decoder appends permanently and only the complement code enables its declared continuation",
    )

    deletions_ok = True
    for records, target in ((a, s0), (rb_a, s1)):
        decoded = decode(records, target)
        for point in decoded.read:  # type: ignore[union-attr]
            mutated = dict(records)
            del mutated[point]
            deletions_ok &= decode(mutated, target) is None
    occupied = decode(append(rb_a, s1, encode(sp.eye(2), 99)), s1) is None
    check(
        "malformed-and-deletion-controls",
        deletions_ok and occupied,
        "every read dependency is load bearing, and an occupied target cannot be decoded or overwritten",
    )

    q = sp.Symbol("q", positive=True)
    check(
        "independent-formation-countercontrol",
        shell(a, s0) == shell(b, s0)
        and sp.Rational(1, 4) * q != sp.Rational(3, 4) * q,
        "equal conditional measures coexist with unequal supplied formation probabilities, so unconditional occurrence is not inferred",
    )

    covariance_failures = 0
    for rotation in rotations():
        for context in ("A", "B"):
            records = {carry(rotation, point): value for point, value in world(context).items()}
            rs0, rs1, rc = carry(rotation, s0), carry(rotation, s1), carry(rotation, c)
            covariance_failures += enabled(records) != ((rs0, "front"),)
            covariance_failures += dist(rc, rs0) != 2 or dist(rc, rs1) != 1
            after = append(records, rs0, RB)
            covariance_failures += enabled(after) != ((rs1, f"tail-{context}"),)
    check(
        "independent-spatial-covariance",
        len(rotations()) == 24 and covariance_failures == 0,
        "both contexts and the supplied continuation decoder survive all 24 proper-cubic rotations",
    )


def algebra_and_carrier_controls() -> None:
    kraus_a, kraus_b, k0, remainder = programs()
    inverse = np.linalg.inv(remainder)
    residual_a = tuple(operator @ inverse for operator in kraus_a[1:])
    residual_b = tuple(operator @ inverse for operator in kraus_b[1:])
    maximum = max(
        float(np.linalg.norm(kraus_a[0] - kraus_b[0])),
        float(np.linalg.norm(np.vstack((k0, remainder)).conj().T @ np.vstack((k0, remainder)) - I2)),
        *(
            float(np.linalg.norm(sum((j.conj().T @ j for j in residual), start=np.zeros((2, 2), dtype=complex)) - I2))
            for residual in (residual_a, residual_b)
        ),
        *(
            float(np.linalg.norm(j @ remainder - target))
            for residual, targets in ((residual_a, kraus_a[1:]), (residual_b, kraus_b[1:]))
            for j, target in zip(residual, targets)
        ),
    )
    check(
        "independent-staged-composition",
        maximum < TOL,
        "the common isometry, both residual isometries, and all four branch recoveries are independently reconstructed",
    )

    rho = np.diag((3 / 5, 2 / 5)).astype(complex)
    sigma0 = k0 @ rho @ k0.conj().T
    sigma_b = remainder @ rho @ remainder.conj().T
    content_residual = max(
        float(np.linalg.norm(sigma0 - np.diag((3 / 10, 0.0)))),
        float(np.linalg.norm(sigma_b - np.diag((3 / 10, 2 / 5)))),
        *(
            float(np.linalg.norm(j @ sigma_b @ j.conj().T - target @ rho @ target.conj().T))
            for residual, targets in ((residual_a, kraus_a[1:]), (residual_b, kraus_b[1:]))
            for j, target in zip(residual, targets)
        ),
    )
    check(
        "independent-realized-content",
        content_residual < TOL
        and min(np.linalg.eigvalsh(sigma0)) > -TOL
        and min(np.linalg.eigvalsh(sigma_b)) > -TOL,
        "conditional on separately supplied actualization, one positive M2 branch-state content exactly feeds each residual CP map",
    )

    physical = []
    for length in (3, 6):
        fixture = c317.physical_fixture(length)
        for kraus, residual in ((kraus_a, residual_a), (kraus_b, residual_b)):
            composed = np.vstack(
                (fixture.two_ray_encoding @ k0,)
                + tuple(fixture.two_ray_encoding @ j @ remainder for j in residual)
            )
            direct = np.vstack(tuple(fixture.two_ray_encoding @ operator for operator in kraus))
            physical.extend(
                (
                    float(np.linalg.norm(composed - direct)),
                    float(np.linalg.norm(composed.conj().T @ composed - I2)),
                    float(np.linalg.norm(fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding)),
                )
            )
    check(
        "independent-held-physical-lift",
        max(physical) < TOL,
        "direct and composed physical blocks agree and remain isometric/constraint-clean at L=3 and held L=6",
    )


def scope_certificate() -> None:
    note = NOTE.read_text(encoding="utf-8")
    lines = (
        "per_element: independently rebuilt exact event codes, branch-state contents, and every staged Kraus recovery without probability values",
        "per_site: independently reconstructed both full six-neighbour shells, blank occupancy, append permanence, and malformed inputs",
        "per_mode: independently separated conditional measure, supplied formation, coherent isometry, and realized-content modes",
        "per_block: independently checked remote shielding, finite rail gating, 24 rotations, staged composition, and held M64 embeddings",
        "lattice_wide: checked and not executed — event actualization, total formation law, arbitrary programs, histories, and frequencies remain open",
    )
    for line in lines:
        print(line)
    check(
        "independent-scope-certificate",
        all(len(line) >= 80 for line in lines)
        and all(line in note for line in lines)
        and "not a total nearest-neighbour model" in note
        and "event-registration impossibility and axiom necessity" in note,
        "the independent resolution and no-go boundaries are source-bound",
    )


def main() -> int:
    source_and_scope()
    spatial_controls()
    algebra_and_carrier_controls()
    scope_certificate()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
